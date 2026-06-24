---
id: 2026-07-07-lime-ipo
title: Lime IPO Nasdaq debut
status: scheduled
created: '2026-06-24T12:00:00Z'
event:
  type: ipo
  summary: Lime (micromobility) targeting Nasdaq IPO under ticker LIME in late June/early
    July 2026; first-day trading dynamics.
  impact_window: '2026-07-07'
tickers:
- LIME
sources:
- title: US News upcoming IPOs 2026
  url: https://money.usnews.com/investing/articles/new-and-upcoming-ipos-in-2026
  accessed_at: '2026-06-24T12:00:00Z'
hypothesis:
  statement: Lime's Nasdaq debut (~Jul 1) produces a moderate first-day pop; entering
    at the listing-day open and exiting mid-morning captures ~8% before the typical
    midday fade.
  direction: long
  confidence: 52
plan:
  ticker: LIME
  action: buy
  entry:
    time: '2026-07-01T13:35:00Z'
    target_price: 28.0
  exit:
    time: '2026-07-01T15:30:00Z'
    target_price: 30.24
  expected_profit_pct: 8.0
research:
  strategy: panel-in-one-agent
  models:
    panel: sonnet
  dissent: Buying at the open already absorbs most of the offer-to-open pop; residual
    gain is thin vs the binary risk of a flat/negative open if listing-day conditions
    deteriorate.
  last_updated: '2026-06-24T12:30:00Z'
---

## Scouted 2026-06-24T12:00:00Z

---
### Revision 2026-06-24T12:30:00Z
Research: buy LIME (conf 52).
