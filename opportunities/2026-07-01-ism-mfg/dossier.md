---
id: 2026-07-01-ism-mfg
title: ISM Manufacturing PMI → industrials
status: analyzed
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
simulation:
  ran_at: '2026-07-06T22:30:05Z'
  fills:
  - leg: entry
    planned_price: 180.81
    actual_price: 184.63
    source: https://api.twelvedata.com/time_series?symbol=XLI&interval=1min&date=2026-07-01&timezone=UTC
    fetched_at: 2026-07-01T14:05Z
  - leg: exit
    planned_price: 182.62
    actual_price: 184.62
    source: https://api.twelvedata.com/time_series?symbol=XLI&interval=1min&date=2026-07-01&timezone=UTC
    fetched_at: 2026-07-01T17:00Z
  realized_profit_pct: -0.0054
  outcome: neutral
  matched_hypothesis: 'no'
postmortem:
  ran_at: '2026-07-06T23:30:00Z'
  root_cause: data
  lessons:
  - Anchor entry to a live pre-event quote, not the research-day price; if the live
    price has drifted >~0.5-1% from the plan anchor, re-derive targets/EV or void
    the trade rather than filling blind.
  - 'When the thesis is ''catalyst reprices X higher'' and X has already rallied to
    its 52-week high before the event, treat the move as priced-in: fade or shrink,
    don''t chase the entry.'
---

## Scouted 2026-06-24T12:00:00Z

---
### Revision 2026-06-24T12:30:00Z
Research: buy XLI (conf 58).

---
### Revision 2026-07-06T22:30:05Z
Simulated XLI buy: -0.0054% (neutral, matched=no)

---
### Revision 2026-07-06T23:30:00Z
Post-mortem: data
