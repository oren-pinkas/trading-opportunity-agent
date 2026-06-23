"""Ledger navigation and deterministic simulation over the opportunities tree."""
import os
from datetime import datetime, timezone

from lib import dossier as _dossier

LEDGER_DIR = "opportunities"


def _parse_iso(ts) -> datetime:
    # Accept a str or a datetime (PyYAML parses unquoted ISO timestamps to datetime).
    if isinstance(ts, datetime):
        return ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def list_by_status(status: str, base: str = LEDGER_DIR) -> list[dict]:
    out: list[dict] = []
    if not os.path.isdir(base):
        return out
    for entry in sorted(os.listdir(base)):
        path = os.path.join(base, entry, "dossier.md")
        if not os.path.isfile(path):
            continue
        fm, _ = _dossier.load(path)
        if fm.get("status") == status:
            out.append({"id": fm.get("id", entry), "path": path, "fm": fm})
    return out


def find_simulatable(now: str, base: str = LEDGER_DIR) -> list[dict]:
    now_dt = _parse_iso(now)
    out: list[dict] = []
    for item in list_by_status("scheduled", base):
        fm = item["fm"]
        if fm.get("simulation"):
            continue
        exit_time = fm.get("plan", {}).get("exit", {}).get("time")
        if exit_time and _parse_iso(exit_time) <= now_dt:
            out.append(item)
    return out


from lib import pnl as _pnl
from lib import marketdata as _marketdata


def matched_hypothesis(expected_pct: float, realized_pct: float) -> str:
    if realized_pct <= 0:
        return "no"
    if realized_pct >= 0.5 * expected_pct:
        return "yes"
    return "partial"


def build_simulation_block(plan: dict, now: str, provider: str = "stub",
                           get_price=_marketdata.get_price) -> dict:
    ticker = plan["ticker"]
    entry = get_price(ticker, plan["entry"]["time"], provider)
    exit_ = get_price(ticker, plan["exit"]["time"], provider)
    pl = _pnl.compute_pnl(plan["action"], entry["price"], exit_["price"])
    fills = [
        {"leg": "entry", "planned_price": plan["entry"].get("target_price"),
         "actual_price": entry["price"], "source": entry["source"],
         "fetched_at": entry["fetched_at"]},
        {"leg": "exit", "planned_price": plan["exit"].get("target_price"),
         "actual_price": exit_["price"], "source": exit_["source"],
         "fetched_at": exit_["fetched_at"]},
    ]
    return {
        "ran_at": now, "fills": fills,
        "realized_profit_pct": pl["realized_profit_pct"],
        "outcome": pl["outcome"],
        "matched_hypothesis": matched_hypothesis(
            plan.get("expected_profit_pct", 0.0), pl["realized_profit_pct"]),
    }


def simulate_dossier(path: str, now: str, provider: str = "stub",
                     get_price=_marketdata.get_price) -> dict:
    fm, _ = _dossier.load(path)
    try:
        block = build_simulation_block(fm["plan"], now, provider, get_price)
        note = (f"Simulated {fm['plan']['ticker']} {fm['plan']['action']}: "
                f"{block['realized_profit_pct']}% "
                f"({block['outcome']}, matched={block['matched_hypothesis']})")
    except (_marketdata.MarketDataUnavailable, KeyError) as exc:
        block = {"ran_at": now, "fills": [], "realized_profit_pct": 0.0,
                 "outcome": "neutral", "matched_hypothesis": "no",
                 "note": f"market data unavailable: {exc}"}
        note = f"Skipped {fm['plan']['ticker']}: market data unavailable ({exc})"
    _dossier.append_revision(path, {"status": "simulated", "simulation": block},
                             note, ts=now)
    return {"id": fm.get("id"), "outcome": block["outcome"],
            "realized_profit_pct": block["realized_profit_pct"],
            "matched_hypothesis": block["matched_hypothesis"]}


from lib import index as _index


def regenerate_index(base: str = LEDGER_DIR, out_path: str = "INDEX.md") -> str:
    rows: list[dict] = []
    if os.path.isdir(base):
        for entry in sorted(os.listdir(base)):
            p = os.path.join(base, entry, "dossier.md")
            if not os.path.isfile(p):
                continue
            fm, _ = _dossier.load(p)
            rows.append({"id": fm.get("id", entry), "title": fm.get("title", ""),
                         "status": fm.get("status", ""),
                         "outcome": (fm.get("simulation") or {}).get("outcome")})
    text = _index.render_index(rows)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return text


from lib import lessons as _lessons


def find_postmortem_targets(base: str = LEDGER_DIR) -> list[dict]:
    out: list[dict] = []
    for item in list_by_status("simulated", base):
        sim = item["fm"].get("simulation") or {}
        outcome = sim.get("outcome")
        matched = sim.get("matched_hypothesis")
        if outcome == "loss" or (outcome in {"win", "neutral"} and matched == "no"):
            out.append(item)
    return out


def create_opportunity(oid: str, title: str, event: dict, tickers: list,
                       sources: list, now: str, base: str = LEDGER_DIR) -> str:
    d = os.path.join(base, oid)
    os.makedirs(d, exist_ok=True)
    fm = {"id": oid, "title": title, "status": "scouted", "created": now,
          "event": event, "tickers": tickers, "sources": sources}
    path = os.path.join(d, "dossier.md")
    _dossier.save(path, fm, f"## Scouted {now}\n")
    return path


def existing_for_dedup(base: str = LEDGER_DIR) -> list[dict]:
    rows: list[dict] = []
    if not os.path.isdir(base):
        return rows
    for entry in sorted(os.listdir(base)):
        p = os.path.join(base, entry, "dossier.md")
        if not os.path.isfile(p):
            continue
        fm, _ = _dossier.load(p)
        seen = (fm.get("research") or {}).get("last_updated") or fm.get("created", "")
        seen = str(seen)[:10]
        rows.append({"tickers": fm.get("tickers", []), "last_seen": seen})
    return rows


def record_postmortem(path: str, root_cause: str, lessons: list, now: str,
                      lessons_path: str = "lessons.yaml") -> dict:
    fm, _ = _dossier.load(path)
    block = {"ran_at": now, "root_cause": root_cause, "lessons": lessons}
    _dossier.append_revision(path, {"status": "analyzed", "postmortem": block},
                             f"Post-mortem: {root_cause}", ts=now)
    event_type = (fm.get("event") or {}).get("type")
    tickers = fm.get("tickers", [])
    for text in lessons:
        _lessons.append_lesson(lessons_path, {
            "event_type": event_type, "tickers": tickers,
            "text": text, "date": now[:10], "source_id": fm.get("id")})
    return {"id": fm.get("id"), "root_cause": root_cause, "lessons_added": len(lessons)}
