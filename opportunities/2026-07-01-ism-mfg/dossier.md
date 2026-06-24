---
id: 2026-07-01-ism-mfg
title: ISM Manufacturing PMI → industrials
status: scheduled
created: '2026-06-24T12:00:00Z'
event:
  type: economic
  summary: ISM Manufacturing PMI for June, Wed Jul 1 10:00 ET; gauge of factory activity,
    moves industrials and broad market.
  impact_window: '2026-07-01'
tickers:
- XLI
- SPY
sources:
- title: Trading Economics US calendar
  url: https://tradingeconomics.com/united-states/calendar
  accessed_at: '2026-06-24T12:00:00Z'
hypothesis:
  statement: A June ISM Manufacturing print at/above ~51 (after May's 54.0) surprises
    a skeptical consensus and drives XLI ~1% intraday as industrials reprice the upcycle.
  direction: long
  confidence: 58
plan:
  ticker: XLI
  action: buy
  entry:
    time: '2026-07-01T14:05:00Z'
    target_price: 180.81
  exit:
    time: '2026-07-01T17:00:00Z'
    target_price: 182.62
  expected_profit_pct: 1.0
research:
  strategy: panel-in-one-agent
  models:
    panel: sonnet
  dissent: XLI is within ~1.2% of its 52wk high; a sub-50 mean-reversion miss (~30%)
    could cut 1.5-2% against a slim positive EV.
  last_updated: '2026-06-24T12:30:00Z'
---

## Scouted 2026-06-24T12:00:00Z

---
### Revision 2026-06-24T12:30:00Z
Research: buy XLI (conf 58).
