# Simulation — 2026-07-02-june-jobs

Simulated 2026-07-06T22:30:05Z (provider: twelvedata). PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Plan intent:** SHORT TLT (20yr Treasury ETF) around the June jobs report, confidence 58,
intraday on 2026-07-02. Thesis: a strong payrolls print pushes yields up / TLT down.

**Fills:**
- Entry (short): planned 86.80, filled **85.475** on 2026-07-02 (TLT 1min bar, [source](https://api.twelvedata.com/time_series?symbol=TLT&interval=1min&date=2026-07-02&timezone=UTC), fetched 2026-07-02T13:35Z).
- Exit (cover): planned 84.50, filled **85.48** on 2026-07-02 (TLT 1min bar, [source](https://api.twelvedata.com/time_series?symbol=TLT&interval=1min&date=2026-07-02&timezone=UTC), fetched 2026-07-02T17:00Z).

**Result:** -0.0058% — **neutral**. TLT was flat over the hold (85.475 → 85.48), a hair
against the short.

**Hypothesis match:** no. No directional payoff; the report did not move long-end yields
enough to matter intraday. Non-event.
