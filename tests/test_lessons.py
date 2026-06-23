from lib.lessons import filter_relevant

LESSONS = [
    {"event_type": "geopolitical", "tickers": ["USO"], "text": "oil prices in fast"},
    {"event_type": "earnings", "tickers": ["NVDA"], "text": "earnings already priced"},
    {"event_type": "geopolitical", "tickers": ["XOM"], "text": "oil prices in fast"},  # dup text
]


def test_matches_by_event_type():
    out = filter_relevant(LESSONS, "geopolitical", ["TSLA"])
    assert [l["text"] for l in out] == ["oil prices in fast"]   # deduped


def test_matches_by_ticker():
    out = filter_relevant(LESSONS, "macro", ["NVDA"])
    assert out[0]["text"] == "earnings already priced"


def test_no_match_returns_empty():
    assert filter_relevant(LESSONS, "macro", ["TSLA"]) == []
