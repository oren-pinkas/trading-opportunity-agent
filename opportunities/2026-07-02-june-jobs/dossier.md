---
id: 2026-07-02-june-jobs
title: June jobs report → rates & equities
status: scheduled
created: '2026-06-24T12:00:00Z'
event:
  type: economic
  summary: June nonfarm payrolls + unemployment, Thu Jul 2 08:30 ET (Jul 3 market
    holiday). Hawkish Warsh Fed makes a hot print bond-bearish.
  impact_window: '2026-07-02'
tickers:
- SPY
- TLT
sources:
- title: BLS Employment Situation schedule
  url: https://www.bls.gov/schedule/news_release/empsit.htm
  accessed_at: '2026-06-24T12:00:00Z'
hypothesis:
  statement: A June NFP print at/above ~130k on Jul 2 confirms the Warsh-Fed hike
    path, lifts 10yr yields 15-20bp and pushes TLT lower intraday; recorded as a low-confidence
    short captured from the cash open.
  direction: short
  confidence: 58
plan:
  ticker: TLT
  action: short
  entry:
    time: '2026-07-02T13:35:00Z'
    target_price: 86.8
  exit:
    time: '2026-07-02T17:00:00Z'
    target_price: 84.5
  expected_profit_pct: 2.65
research:
  strategy: panel-in-one-agent
  models:
    panel: sonnet
  dissent: The modal ~130k in-line print may already be priced into TLT's $87 level
    post-June-17 dot-flip, making the selloff short-lived and faded by duration buyers.
  last_updated: '2026-06-24T12:30:00Z'
---

## Scouted 2026-06-24T12:00:00Z

---
### Revision 2026-06-24T12:30:00Z
Research: short TLT (conf 58).
