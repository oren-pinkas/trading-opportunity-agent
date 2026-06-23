"""Scout duplicate detection within a rolling window."""
from datetime import date


def _d(s: str) -> date:
    return date.fromisoformat(s)


def is_duplicate(candidate: dict, existing: list[dict], today: str,
                 window_days: int = 14) -> bool:
    cand_tickers = set(candidate.get("tickers", []))
    for e in existing:
        if cand_tickers & set(e.get("tickers", [])):
            age = (_d(today) - _d(e["last_seen"])).days
            if 0 <= age <= window_days:
                return True
    return False
