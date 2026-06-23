from lib.index import render_index

ROWS = [
    {"id": "2026-06-22-oil", "title": "Oil down", "status": "simulated", "outcome": "win"},
    {"id": "2026-06-21-nvda", "title": "NVDA up", "status": "scouted", "outcome": None},
]


def test_index_has_disclaimer_and_sorted_rows():
    out = render_index(ROWS)
    assert "NOT FINANCIAL ADVICE" in out
    assert out.index("2026-06-21-nvda") < out.index("2026-06-22-oil")  # sorted by id


def test_index_renders_missing_outcome_as_dash():
    out = render_index(ROWS)
    assert "| — |" in out or "| —" in out
