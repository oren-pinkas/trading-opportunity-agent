import pytest
from lib.pnl import compute_pnl


def test_long_gain_is_win():
    r = compute_pnl("buy", 100.0, 110.0)
    assert r["realized_profit_pct"] == 10.0
    assert r["outcome"] == "win"


def test_short_gain_when_price_falls():
    r = compute_pnl("short", 100.0, 90.0)
    assert r["realized_profit_pct"] == 10.0
    assert r["outcome"] == "win"


def test_long_loss():
    r = compute_pnl("buy", 100.0, 95.0)
    assert r["realized_profit_pct"] == -5.0
    assert r["outcome"] == "loss"


def test_tiny_move_is_neutral():
    assert compute_pnl("buy", 100.0, 100.05)["outcome"] == "neutral"


def test_invalid_action_raises():
    with pytest.raises(ValueError):
        compute_pnl("hold", 100.0, 110.0)
