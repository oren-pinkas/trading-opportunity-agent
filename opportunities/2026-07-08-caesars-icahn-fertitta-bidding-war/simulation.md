# Simulation — 2026-07-08-caesars-icahn-fertitta-bidding-war

**Plan:** Buy CZR at 2026-07-10 14:00 UTC (target $31.50), exit 2026-07-11 20:00 UTC (target $32.00). Expected profit 1.6%. Thesis (confidence 35, low-conviction): Caesars' go-shop window (expiring 2026-07-11) resolves with modest positive EV — Fertitta matches or Icahn wins outright in ~60% of scenarios, deal-break/fade in ~30% — but the panel could not agree whether the available price series reflected real signal, so the position was sized as a token long, not a conviction bet.

**Result: neutral / no fill.** The exit time (2026-07-11 20:00 UTC) falls on a Saturday — markets were closed, so no price data exists for either the entry or exit leg. `toa simulate` recorded `market data unavailable: CZR 2026-07-11: HTTP 400` and closed the plan as neutral (0.0% realized) rather than fabricating a fill.

**Hypothesis match: no** — not because the thesis was wrong, but because the plan was never actually testable against real prices; the go-shop deadline event itself may still have resolved as expected, but this dossier can't confirm or refute it.

**Lesson:** the panel flagged low confidence in the price series being real signal — this data-availability gap (weekend deadline, no market open) is a separate and more basic failure mode than the pricing question they debated, and should factor into future entry/exit scheduling around dates that fall on non-trading days.
