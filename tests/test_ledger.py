from lib import dossier, ledger


def _scheduled_fm(oid, exit_time):
    return {
        "id": oid, "title": "t", "status": "scheduled",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"],
        "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
        "hypothesis": {"statement": "h", "direction": "short", "confidence": 65},
        "plan": {"ticker": "USO", "action": "short",
                 "entry": {"time": "2026-07-10T13:00:00Z", "target_price": 100.0},
                 "exit": {"time": exit_time, "target_price": 90.0},
                 "expected_profit_pct": 2.0},
        "research": {"strategy": "three-round-panel",
                     "models": {"bull": "sonnet"}, "last_updated": "2026-06-22T11:00:00Z"},
    }


def _seed(base, oid, fm):
    d = base / oid
    d.mkdir(parents=True)
    dossier.save(str(d / "dossier.md"), fm, "## Seed\n")


def test_list_by_status_filters(tmp_path):
    _seed(tmp_path, "a", _scheduled_fm("a", "2026-07-10T13:12:00Z"))
    fm_other = _scheduled_fm("b", "2026-07-10T13:12:00Z"); fm_other["status"] = "scouted"
    _seed(tmp_path, "b", fm_other)
    got = ledger.list_by_status("scheduled", base=str(tmp_path))
    assert [i["id"] for i in got] == ["a"]


def test_find_simulatable_respects_exit_time(tmp_path):
    _seed(tmp_path, "past", _scheduled_fm("past", "2026-07-10T13:12:00Z"))
    _seed(tmp_path, "future", _scheduled_fm("future", "2026-12-31T13:12:00Z"))
    got = ledger.find_simulatable("2026-07-11T00:00:00Z", base=str(tmp_path))
    assert [i["id"] for i in got] == ["past"]


def test_missing_base_returns_empty():
    assert ledger.list_by_status("scheduled", base="/nonexistent/path") == []


from lib.ledger import matched_hypothesis, build_simulation_block


def test_matched_hypothesis_rule():
    assert matched_hypothesis(2.0, -1.0) == "no"
    assert matched_hypothesis(2.0, 1.5) == "yes"
    assert matched_hypothesis(2.0, 0.5) == "partial"


def test_build_simulation_block_uses_injected_prices():
    plan = _scheduled_fm("x", "2026-07-10T13:12:00Z")["plan"]

    def fake_price(ticker, ts, provider):
        price = 100.0 if "13:00" in ts else 90.0   # short 100->90 = +10%
        return {"price": price, "source": f"test:{ticker}", "fetched_at": ts}

    block = build_simulation_block(plan, "2026-07-11T00:00:00Z",
                                   get_price=fake_price)
    assert block["realized_profit_pct"] == 10.0
    assert block["outcome"] == "win"
    assert block["matched_hypothesis"] == "yes"      # 10 >= 0.5*2.0
    assert block["fills"][0]["leg"] == "entry"
    assert block["fills"][0]["actual_price"] == 100.0
    assert block["fills"][1]["actual_price"] == 90.0
    assert block["fills"][0]["source"] == "test:USO"


from lib.ledger import simulate_dossier


def test_simulate_dossier_writes_valid_simulated(tmp_path):
    _seed(tmp_path, "x", _scheduled_fm("x", "2026-07-10T13:12:00Z"))
    path = str(tmp_path / "x" / "dossier.md")
    summary = simulate_dossier(path, "2026-07-11T00:00:00Z", provider="stub")
    assert summary["id"] == "x"
    assert summary["outcome"] in {"win", "loss", "neutral"}
    fm, body = dossier.load(path)
    assert fm["status"] == "simulated"
    assert fm["simulation"]["ran_at"] == "2026-07-11T00:00:00Z"
    assert dossier.validate_frontmatter(fm) == []     # conforms at new status
    assert "Simulated" in body                        # narrative revision appended


def test_simulate_dossier_handles_missing_data(tmp_path):
    from lib.marketdata import MarketDataUnavailable
    _seed(tmp_path, "h", _scheduled_fm("h", "2026-07-10T13:12:00Z"))
    path = str(tmp_path / "h" / "dossier.md")

    def no_data(ticker, ts, provider):
        raise MarketDataUnavailable("no data for holiday")

    summary = simulate_dossier(path, "2026-07-11T00:00:00Z", get_price=no_data)
    assert summary["outcome"] == "neutral"
    fm, body = dossier.load(path)
    assert fm["status"] == "simulated"                # terminal, not retried forever
    assert dossier.validate_frontmatter(fm) == []
    assert "unavailable" in body.lower()


def test_simulate_dossier_from_unquoted_yaml_timestamps(tmp_path):
    # PyYAML parses unquoted ISO timestamps into datetime objects; the simulator
    # must handle that, not just the string timestamps a Python dict fixture yields.
    d = tmp_path / "u"; d.mkdir()
    path = str(d / "dossier.md")
    (d / "dossier.md").write_text(
        "---\n"
        "id: u\n"
        "title: t\n"
        "status: scheduled\n"
        "created: 2026-06-22T09:00:00Z\n"
        "event: {type: geopolitical, summary: s, impact_window: 2026-06-22}\n"
        "tickers: [USO]\n"
        "sources: [{title: a, url: u, accessed_at: x}]\n"
        "hypothesis: {statement: h, direction: short, confidence: 65}\n"
        "plan:\n"
        "  ticker: USO\n"
        "  action: short\n"
        "  entry: {time: 2026-06-22T14:00:00Z, target_price: 78.5}\n"
        "  exit: {time: 2026-06-22T15:30:00Z, target_price: 78.1}\n"
        "  expected_profit_pct: 0.5\n"
        "research: {strategy: three-round-panel, models: {bull: sonnet}, last_updated: 2026-06-22T11:00:00Z}\n"
        "---\n\n## Seed\n"
    )
    summary = ledger.simulate_dossier(path, "2026-06-23T00:00:00Z", provider="stub")
    assert summary["outcome"] in {"win", "loss", "neutral"}
    fm, _ = dossier.load(path)
    assert fm["status"] == "simulated"
    assert dossier.validate_frontmatter(fm) == []


from lib.ledger import regenerate_index


def test_regenerate_index_writes_rows(tmp_path):
    _seed(tmp_path, "a", _scheduled_fm("a", "2026-07-10T13:12:00Z"))
    out = tmp_path / "INDEX.md"
    text = regenerate_index(base=str(tmp_path), out_path=str(out))
    assert "NOT FINANCIAL ADVICE" in text
    assert "| a |" in text
    assert out.read_text() == text


from lib.ledger import (find_postmortem_targets, create_opportunity,
                        existing_for_dedup, record_postmortem)
from lib.lessons import load_lessons


def _simulated_fm(oid, outcome, matched):
    fm = _scheduled_fm(oid, "2026-07-10T13:12:00Z")
    fm["status"] = "simulated"
    fm["simulation"] = {"ran_at": "2026-07-11T00:00:00Z", "fills": [],
                        "realized_profit_pct": -1.0, "outcome": outcome,
                        "matched_hypothesis": matched}
    return fm


def test_find_postmortem_targets_picks_losers_and_flukes(tmp_path):
    _seed(tmp_path, "loss", _simulated_fm("loss", "loss", "no"))
    _seed(tmp_path, "fluke", _simulated_fm("fluke", "win", "no"))
    _seed(tmp_path, "clean", _simulated_fm("clean", "win", "yes"))
    ids = sorted(i["id"] for i in find_postmortem_targets(base=str(tmp_path)))
    assert ids == ["fluke", "loss"]


def test_create_opportunity_writes_valid_scouted(tmp_path):
    path = create_opportunity(
        "2026-06-23-fed", "Fed holds", {"type": "macro", "summary": "s", "impact_window": "2026-07-30"},
        ["SPY"], [{"title": "t", "url": "u", "accessed_at": "2026-06-23T10:00:00Z"}],
        "2026-06-23T10:00:00Z", base=str(tmp_path))
    fm, _ = dossier.load(path)
    assert fm["status"] == "scouted"
    assert fm["id"] == "2026-06-23-fed"
    assert dossier.validate_frontmatter(fm) == []


def test_existing_for_dedup_lists_tickers_and_date(tmp_path):
    create_opportunity("2026-06-23-fed", "Fed", {"type": "macro", "summary": "s", "impact_window": "2026-07-30"},
                       ["SPY", "QQQ"], [{"title": "t", "url": "u", "accessed_at": "x"}],
                       "2026-06-23T10:00:00Z", base=str(tmp_path))
    rows = existing_for_dedup(base=str(tmp_path))
    assert rows == [{"tickers": ["SPY", "QQQ"], "last_seen": "2026-06-23"}]


def test_record_postmortem_writes_block_and_lessons(tmp_path):
    _seed(tmp_path, "loss", _simulated_fm("loss", "loss", "no"))
    path = str(tmp_path / "loss" / "dossier.md")
    store = str(tmp_path / "lessons.yaml")
    summary = record_postmortem(path, "priced-in", ["entered too late"],
                                "2026-07-12T00:00:00Z", lessons_path=store)
    assert summary["lessons_added"] == 1
    fm, _ = dossier.load(path)
    assert fm["status"] == "analyzed"
    assert fm["postmortem"]["root_cause"] == "priced-in"
    assert dossier.validate_frontmatter(fm) == []
    lessons = load_lessons(store)
    assert lessons[0]["text"] == "entered too late"
    assert lessons[0]["event_type"] == "geopolitical"
    assert "USO" in lessons[0]["tickers"]
