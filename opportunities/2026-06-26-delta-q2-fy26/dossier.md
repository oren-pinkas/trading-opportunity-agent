---
id: 2026-06-26-delta-q2-fy26
title: Delta Air Lines Q2 FY2026 earnings (report July 10 BMO)
status: analyzed
created: '2026-06-26T11:00:05Z'
event:
  type: earnings
  summary: Delta reports June-quarter results July 10 BEFORE market open; Street models
    EPS ~$1.43, a ~32% YoY drop, and the print sets the tone for airline earnings.
    Tradable as an overnight gap-hold into the 7/10 open.
  impact_window: '2026-07-10'
tickers:
- DAL
sources:
- title: Delta Air Lines Q2 2026 webcast set for July 10 (StockTitan)
  url: https://www.stocktitan.net/news/DAL/delta-air-lines-announces-webcast-of-june-quarter-2026-financial-ffsbw6az35wm.html
  accessed_at: '2026-06-26T11:00:05Z'
- title: What to Expect From Delta Air Lines' Q2 2026 Earnings Report (Barchart)
  url: https://www.barchart.com/story/news/2639811/what-to-expect-from-delta-air-lines-q2-2026-earnings-report
  accessed_at: '2026-06-26T12:05:00Z'
- title: Oil price June 24, 2026 — Brent ~$74 after US-Iran de-escalation (Fortune)
  url: https://fortune.com/article/price-of-oil-06-24-2026/
  accessed_at: '2026-06-26T12:05:00Z'
- title: DAL implied/realized post-earnings move distribution (MarketChameleon)
  url: https://marketchameleon.com/Overview/DAL/Earnings/Earnings-Charts/
  accessed_at: '2026-06-26T12:05:00Z'
hypothesis:
  statement: DAL reports BMO July 10 into a concrete, recent fuel windfall — Brent
    fell ~19% to ~$74 on US-Iran de-escalation since the April guidance was set at
    $4.30/gal jet fuel, a tailwind not yet in the print, atop 4 straight EPS beats
    and a 22/24 Strong Buy tilt. Expressed as a quarter-size LONG held across the
    7/10 pre-open print into the open gap. Conviction is capped because the closest
    analog (Q1 2026 beat-with-fuel-narrative) gapped only +3.74%, realized magnitude
    is ~3.5% (not 9%), and DAL already ran ~40% to a 52-wk high above the Street mean
    target (~$82) — so much of the catalyst may already be priced.
  direction: long
  confidence: 56
plan:
  ticker: DAL
  action: buy
  entry:
    time: '2026-07-09T19:50:00Z'
    target_price: 91.5
  exit:
    time: '2026-07-10T13:45:00Z'
    target_price: 94.7
  expected_profit_pct: 3.5
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: 'The bear''s strongest unrebutted point: the fuel tailwind the bull/quant
    treat as a fresh catalyst already drove DAL''s ~40% 90-day run to a 52-wk high
    ABOVE the Street mean target (~$82). If the windfall is already in the price,
    it cannot also be the gap catalyst, leaving a coin-flip that is negative-EV after
    an overnight levered hold''s costs. Quant concurs the long is only positive if
    P(up) > ~0.54 and pays only ~+0.5% net even then. Post-mortem must test whether
    the realized gap tracks the magnitude of the pre-print run-up (priced-in) vs the
    fuel-vs-guidance delta (not-priced-in).'
  last_updated: '2026-06-26T12:10:39Z'
simulation:
  ran_at: '2026-07-10T22:46:36Z'
  fills:
  - leg: entry
    planned_price: 91.5
    actual_price: 88.77
    source: https://api.twelvedata.com/time_series?symbol=DAL&interval=1min&date=2026-07-09&timezone=UTC
    fetched_at: 2026-07-09T19:50Z
  - leg: exit
    planned_price: 94.7
    actual_price: 86.5501
    source: https://api.twelvedata.com/time_series?symbol=DAL&interval=1min&date=2026-07-10&timezone=UTC
    fetched_at: 2026-07-10T13:45Z
  realized_profit_pct: -2.5007
  outcome: loss
  matched_hypothesis: 'no'
postmortem:
  ran_at: '2026-07-12T23:30:05Z'
  root_cause: priced-in
  lessons:
  - A catalyst that already drove a large multi-week run to a 52-week high above the
    Street mean target is priced in — do not re-bet the same fundamental as a fresh
    gap trigger for the print.
  - When the strongest unrebutted dissent aligns with the quant's own EV math (long
    only positive if P(up) > 0.54, netting ~+0.5% if forced), synthesize to NO-TRADE
    rather than a quarter-size directional position.
---

## Scouted 2026-06-26T11:00:05Z

## Researched 2026-06-26T12:10:39Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). DAL reports
BEFORE the open July 10 (Friday), so the tradable move is the overnight gap — entry
at the 7/9 close (~19:50Z), exit ~15 min after the 7/10 open (13:45Z). Real price
~$91-92 near the 52-week high, NOT the stub. The panel split: the BULL argued a
low-conviction LONG (the April guidance assumed $4.30/gal jet fuel; Brent is now
~$74 after US-Iran de-escalation — a fuel windfall that postdates the bar and isn't
in the print). The BULL also debunked an initial "fell 5 straight quarters" base
rate — the two most recent BMO prints actually SPLIT (Q1 2026 +3.8%, Q4 2025 -2.4%).
The BEAR held NO-TRADE: the fuel relief already drove the ~40% run to a high above
all targets, so it's priced in, leaving a coin-flip. The QUANT landed at NO-TRADE on
EV (long only positive if P(up) > ~0.54; ~+0.5% net even at 0.60) but conceded the
only defensible DIRECTION is long. Synthesizer converged on a quarter-size LONG,
+3.5% target inside the ~5.7% implied / ~3.5% realized move, confidence 56. Full
debate with citations in `transcript.md`.

---
### Revision 2026-07-10T22:46:36Z
Simulated DAL buy: -2.5007% (loss, matched=no)

---
### Revision 2026-07-12T23:30:05Z
Post-mortem: priced-in
