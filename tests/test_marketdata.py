import json
from pathlib import Path

import pytest

import lib.marketdata as md
from lib.marketdata import get_price, parse_twelvedata


def _payload():
    return json.loads(Path("tests/fixtures/twelvedata_nvda_1min.json").read_text())


# --- stub provider (Task 5) ---

def test_stub_is_deterministic():
    a = get_price("NVDA", "2026-07-10T13:00:00Z")
    b = get_price("NVDA", "2026-07-10T13:00:00Z")
    assert a["price"] == b["price"]
    assert a["source"] == "stub:deterministic"


def test_stub_varies_by_minute():
    a = get_price("NVDA", "2026-07-10T13:00:00Z")
    b = get_price("NVDA", "2026-07-10T13:12:00Z")
    assert a["price"] != b["price"]


def test_stub_price_in_plausible_range():
    p = get_price("AAPL", "2026-07-10T14:30:00Z")["price"]
    assert 10.0 <= p <= 500.0


# --- Twelve Data parser (Task 6) ---

def test_parse_returns_open_of_matching_minute():
    assert parse_twelvedata(_payload(), "2026-07-10T13:00:00Z") == 118.20


def test_parse_ignores_seconds():
    assert parse_twelvedata(_payload(), "2026-07-10T13:12:45Z") == 120.50


def test_parse_missing_minute_raises():
    with pytest.raises(KeyError):
        parse_twelvedata(_payload(), "2026-07-10T15:00:00Z")


def test_parse_error_status_raises():
    with pytest.raises(ValueError):
        parse_twelvedata({"status": "error", "message": "bad key"}, "2026-07-10T13:00:00Z")


# --- live provider wiring (Task 7) ---

def test_twelvedata_provider_uses_fetch_and_parse(monkeypatch):
    calls = {"n": 0}

    def fake_fetch(ticker, date, api_key):
        calls["n"] += 1
        return _payload()

    monkeypatch.setattr(md, "_fetch_twelvedata", fake_fetch)
    monkeypatch.setenv("TWELVEDATA_API_KEY", "test-key")
    md._CACHE.clear()
    r1 = md.get_price("NVDA", "2026-07-10T13:00:00Z", provider="twelvedata")
    r2 = md.get_price("NVDA", "2026-07-10T13:12:00Z", provider="twelvedata")
    assert r1["price"] == 118.20 and r2["price"] == 120.50
    assert calls["n"] == 1                       # same (ticker,date) cached
    assert "twelvedata.com" in r1["source"]


def test_twelvedata_missing_key_raises(monkeypatch):
    monkeypatch.delenv("TWELVEDATA_API_KEY", raising=False)
    md._CACHE.clear()
    with pytest.raises(RuntimeError):
        md.get_price("NVDA", "2026-07-10T13:00:00Z", provider="twelvedata")
