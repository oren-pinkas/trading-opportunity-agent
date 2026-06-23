import json
import subprocess
import sys


def _run(*args):
    return subprocess.run([sys.executable, "-m", "lib.cli", *args],
                          capture_output=True, text=True)


def test_cli_price_stub():
    r = _run("price", "NVDA", "2026-07-10T13:00:00Z")
    assert r.returncode == 0
    assert json.loads(r.stdout)["source"] == "stub:deterministic"


def test_cli_pnl():
    r = _run("pnl", "buy", "100", "110")
    assert json.loads(r.stdout)["outcome"] == "win"


from lib import dossier, ledger  # noqa: F401  (ledger import ensures module present)


def _seed_scheduled(tmp_path, oid):
    fm = {
        "id": oid, "title": "t", "status": "scheduled",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"], "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
        "hypothesis": {"statement": "h", "direction": "short", "confidence": 65},
        "plan": {"ticker": "USO", "action": "short",
                 "entry": {"time": "2026-07-10T13:00:00Z", "target_price": 100.0},
                 "exit": {"time": "2026-07-10T13:12:00Z", "target_price": 90.0},
                 "expected_profit_pct": 2.0},
        "research": {"strategy": "three-round-panel", "models": {"bull": "sonnet"},
                     "last_updated": "2026-06-22T11:00:00Z"},
    }
    d = tmp_path / oid; d.mkdir(parents=True)
    path = str(d / "dossier.md")
    dossier.save(path, fm, "## Seed\n")
    return path


def test_cli_simulate_writes_outcome(tmp_path):
    path = _seed_scheduled(tmp_path, "x")
    r = _run("simulate", path, "--now", "2026-07-11T00:00:00Z")
    assert r.returncode == 0
    out = json.loads(r.stdout)
    assert out["id"] == "x"
    assert out["outcome"] in {"win", "loss", "neutral"}


def test_cli_simulatable_lists_due(tmp_path):
    _seed_scheduled(tmp_path, "x")
    r = _run("simulatable", "--now", "2026-07-11T00:00:00Z", "--base", str(tmp_path))
    assert json.loads(r.stdout)["ids"] == ["x"]


def test_cli_dedup_check(tmp_path):
    _seed_scheduled(tmp_path, "x")  # tickers [USO], created 2026-06-22
    r = _run("dedup-check", "--tickers", "USO", "--today", "2026-06-23", "--base", str(tmp_path))
    assert json.loads(r.stdout)["duplicate"] is True


def test_cli_postmortem_targets_empty(tmp_path):
    r = _run("postmortem-targets", "--base", str(tmp_path))
    assert json.loads(r.stdout)["ids"] == []


def test_cli_new_opportunity(tmp_path):
    r = _run("new-opportunity", "--id", "2026-06-23-fed", "--title", "Fed holds",
             "--type", "macro", "--summary", "s", "--impact-window", "2026-07-30",
             "--tickers", "SPY", "--source-title", "wire", "--source-url", "https://x",
             "--now", "2026-06-23T10:00:00Z", "--base", str(tmp_path))
    assert json.loads(r.stdout)["status"] == "scouted"
