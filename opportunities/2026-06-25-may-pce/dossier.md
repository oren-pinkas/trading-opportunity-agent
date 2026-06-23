---
id: 2026-06-25-may-pce
title: May PCE print → rate-sensitive assets
status: scheduled
created: '2026-06-23T11:00:00Z'
event:
  type: economic
  summary: May PCE (Fed's preferred inflation gauge) + Q1 GDP 3rd est release Thu
    Jun 25 08:30 ET; futures lean toward a hike on sticky inflation.
  impact_window: '2026-06-25'
tickers:
- TLT
- SPY
sources:
- title: Schwab Market Update
  url: https://www.schwab.com/learn/story/stock-market-update-open
  accessed_at: '2026-06-23T11:00:00Z'
hypothesis:
  statement: May PCE is the Fed's preferred gauge in a hawkish Warsh regime; only
    a hot (>=0.4% MoM core / energy-driven) surprise meaningfully pushes 20yr yields
    up and TLT down. Base case is an in-line print that is largely priced. Recorded
    as a small short-TLT expression of the ~25% hot tail.
  direction: short
  confidence: 45
plan:
  ticker: TLT
  action: short
  entry:
    time: '2026-06-25T13:35:00Z'
    target_price: 85.8
  exit:
    time: '2026-06-25T19:00:00Z'
    target_price: 84.9
  expected_profit_pct: 1.0
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: 'Bear: no trade, move fully priced post-June-17 FOMC. Quant: enter only
    conditionally after a hot >=0.4% MoM print confirms; recorded plan is unconditional,
    so an in-line print should produce ~flat/negative and vindicate the caution.'
  last_updated: '2026-06-23T11:10:00Z'
---

## Scouted 2026-06-23T11:00:00Z

---
### Revision 2026-06-23T11:10:00Z
Research debate (three-round-panel): low-confidence small short TLT; EV +0.25%, tail-dependent.
