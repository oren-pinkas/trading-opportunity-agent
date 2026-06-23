"""Deterministic realized P/L for a simulated round-trip."""

_LONG = {"buy"}
_SHORT = {"sell", "short"}


def compute_pnl(action: str, entry_price: float, exit_price: float,
                neutral_band_pct: float = 0.1) -> dict:
    if action in _LONG:
        pct = (exit_price - entry_price) / entry_price * 100.0
    elif action in _SHORT:
        pct = (entry_price - exit_price) / entry_price * 100.0
    else:
        raise ValueError(f"unknown action: {action!r}")
    pct = round(pct, 4)
    if abs(pct) <= neutral_band_pct:
        outcome = "neutral"
    else:
        outcome = "win" if pct > 0 else "loss"
    return {"realized_profit_pct": pct, "outcome": outcome}
