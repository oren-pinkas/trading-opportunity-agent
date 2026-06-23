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


from lib.ledger import regenerate_index


def test_regenerate_index_writes_rows(tmp_path):
    _seed(tmp_path, "a", _scheduled_fm("a", "2026-07-10T13:12:00Z"))
    out = tmp_path / "INDEX.md"
    text = regenerate_index(base=str(tmp_path), out_path=str(out))
    assert "NOT FINANCIAL ADVICE" in text
    assert "| a |" in text
    assert out.read_text() == text
