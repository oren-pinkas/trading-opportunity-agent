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


from lib.lessons import load_lessons, append_lesson, render_lessons_md


def test_append_then_load_roundtrips(tmp_path):
    p = str(tmp_path / "lessons.yaml")
    assert load_lessons(p) == []
    append_lesson(p, {"event_type": "geopolitical", "tickers": ["USO"],
                      "text": "oil reacts in minutes", "date": "2026-07-11", "source_id": "x"})
    rows = load_lessons(p)
    assert rows[0]["text"] == "oil reacts in minutes"


def test_render_lessons_md_has_disclaimer_and_text():
    md = render_lessons_md([{"event_type": "macro", "tickers": ["SPY"], "text": "priced in early"}])
    assert "NOT FINANCIAL ADVICE" in md
    assert "priced in early" in md
