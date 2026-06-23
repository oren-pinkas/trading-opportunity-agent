from lib.dedup import is_duplicate

EXISTING = [{"tickers": ["USO", "BNO"], "last_seen": "2026-06-20"}]


def test_recent_shared_ticker_is_duplicate():
    cand = {"tickers": ["USO"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-06-23") is True


def test_old_entry_not_duplicate():
    cand = {"tickers": ["USO"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-07-30") is False


def test_no_ticker_overlap_not_duplicate():
    cand = {"tickers": ["NVDA"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-06-23") is False
