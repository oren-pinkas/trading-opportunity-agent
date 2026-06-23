"""Ledger navigation and deterministic simulation over the opportunities tree."""
import os
from datetime import datetime

from lib import dossier as _dossier

LEDGER_DIR = "opportunities"


def _parse_iso(ts: str) -> datetime:
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
