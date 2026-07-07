---
id: 2026-06-25-constellation-q1-fy27
title: Constellation Brands Q1 FY2027 earnings after close June 30
status: simulated
created: '2026-06-25T09:22:56Z'
event:
  type: earnings
  summary: Constellation Brands (beer/wine/spirits, Modelo/Corona) reports fiscal
    Q1 FY2027 (quarter ended 5/31) on 6/30 AFTER close, call 7/1 8am ET. Reaction
    trades at the 7/1 open. Consensus EPS ~$3.28 on revenue ~$2.42B (down ~4% YoY).
  impact_window: '2026-06-30'
tickers:
- STZ
sources:
- title: Constellation Brands to Report First Quarter Fiscal 2027 Financial Results
  url: https://www.stocktitan.net/news/STZ/constellation-brands-to-report-first-quarter-fiscal-2027-financial-zsu72k906iz4.html
  accessed_at: '2026-06-25T09:22:56Z'
- title: Barchart — Constellation Brands earnings preview
  url: https://www.barchart.com/story/news/2625379/constellation-brands-earnings-preview-what-to-expect
  accessed_at: '2026-06-25T12:00:00Z'
- title: 247WallSt — TD Cowen upgrades STZ, calls beer guidance "overly conservative"
  url: https://247wallst.com/investing/2026/04/13/td-cowen-upgrades-constellation-brands-to-buy-calling-its-beer-guidance-overly-conservative/
  accessed_at: '2026-06-25T12:00:00Z'
hypothesis:
  statement: 'PANEL VERDICT IS EFFECTIVELY NO TRADE — no positive-EV directional edge.
    Recorded as a minimal LONG expression only. Rationale for the long tilt: a serial
    beater (3 of 4 beats) into a trough ~12x multiple with a low bar ($3.28 EPS) and
    World Cup beer loading; the quant found a SHORT is net-negative (the beat history
    removes the down-skew) while a long is ~coin-flip (~0 EV). Direction: long, very
    low conviction.'
  direction: long
  confidence: 33
plan:
  ticker: STZ
  action: buy
  entry:
    time: '2026-06-30T19:50:00Z'
    target_price: 143.5
  exit:
    time: '2026-07-01T13:45:00Z'
    target_price: 144.2
  expected_profit_pct: 0.5
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
  dissent: '2 of 3 panelists = NO TRADE. Quant (opus, tiebreaker): short net EV ~-0.4%,
    long net EV ~0.0% after costs — the market''s ~6% implied move means it has no
    directional conviction, and the 3-of-4 beat history removes the left skew, so
    neither side clears the bar. Bear: the April +8.5% re-rating is already consumed
    and the Q4 +0.6% depletion "inflection" is a compositional artifact (driven by
    Pacifico +21% / Victoria +17%, while Modelo Especial -1% and Corona -6%); the
    structural Hispanic-consumer headwind (~50% of beer revenue) is unresolved.'
  last_updated: '2026-06-25T12:10:00Z'
simulation:
  ran_at: '2026-07-06T22:30:05Z'
  fills:
  - leg: entry
    planned_price: 143.5
    actual_price: 138.19
    source: https://api.twelvedata.com/time_series?symbol=STZ&interval=1min&date=2026-06-30&timezone=UTC
    fetched_at: 2026-06-30T19:50Z
  - leg: exit
    planned_price: 144.2
    actual_price: 141.67
    source: https://api.twelvedata.com/time_series?symbol=STZ&interval=1min&date=2026-07-01&timezone=UTC
    fetched_at: 2026-07-01T13:45Z
  realized_profit_pct: 2.5183
  outcome: win
  matched_hypothesis: 'yes'
---

## Scouted 2026-06-25T09:22:56Z

## Researched 2026-06-25T12:10:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real price ~$143
(NOT the stub's $107.74). The panel did **not** find a tradable edge: the quant (the
designed tiebreaker) computed a short at net EV ~-0.4% and a long at ~0.0% after costs,
and the bear preferred standing aside. Recorded as a minimal LONG expression at
confidence 33 to keep the call in the learning loop; the no-trade verdict is the real
output. Full debate with citations in `transcript.md`.

---
### Revision 2026-07-06T22:30:05Z
Simulated STZ buy: 2.5183% (win, matched=yes)
