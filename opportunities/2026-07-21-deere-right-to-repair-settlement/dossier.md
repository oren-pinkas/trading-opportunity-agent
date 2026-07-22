---
id: 2026-07-21-deere-right-to-repair-settlement
title: Deere FTC right to repair settlement
status: researched
created: '2026-07-21T15:25:19Z'
event:
  type: regulatory
  summary: FTC and five states secured a 10 year settlement requiring Deere to give
    farmers and independent repair providers equal access to repair software
  impact_window: '2026-07-08'
tickers:
- DE
sources:
- title: FTC, States Secure Settlement with Deere and Company - FTC
  url: https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-secure-settlement-deere-company-advancing-farmers-right-repair
  accessed_at: '2026-07-21T15:25:19Z'
hypothesis:
  statement: The USD 2.96 percent one-session move on DE reflects a relief rally on
    removal of regulatory tail risk (10 year FTC right-to-repair consent decree),
    not a fundamental repricing. Base rates for mega-cap industrial overhang-clearing
    settlements favor mean-reversion or fade over durable drift, while the embedded
    structural cost to Deere parts/service margin lands 1-2 quarters out, past any
    2-3 session trade window. Neither a fresh long nor a tactical fade offers edge
    that reliably survives slippage and squeeze/gap risk on the 2-3 session horizon.
    The panel converged - bull would only commit on a confirmed hold above USD 607,
    bear and quant lean fade, and quant's base case is pass.
  direction: none
  confidence: 62
plan:
  ticker: DE
  action: no-trade
  entry:
    time: '2026-07-23T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-24T20:00:00Z'
    target_price: null
  expected_profit_pct: 0
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
  dissent: "The strongest unresolved disagreement is whether the settlement is economically
    a net positive or net negative for DE. The bull holds that equal software access
    only (no hardware or business-model rewrite, no monetary penalty) is best-case and
    protects the high-margin parts/service annuity by capping litigation risk; the bear
    holds the identical mechanism is precisely what lets independent providers capture
    that service revenue, making it a permanent multi-quarter margin drag disguised as
    a settlement. Unresolvable within the trade window because the cash-flow impact
    does not surface in guidance for 1-2 quarters, well past the 2-3 session exit."
  last_updated: '2026-07-22T22:30:05Z'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-22T22:30:05Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). DE ran from
590.22 (2026-07-21T15:25Z) to 607.70 (2026-07-22T19:59Z), +2.96% in about one
session on the FTC right-to-repair settlement headline. The QUANT's base-rate
analysis was decisive: overhang-clearing regulatory settlements on mega-cap
industrials mean-revert ~60% of the time within 3-5 sessions, and this remedy
(software access only, no fine, no unit-sales hit) is operationally minor for
near-term earnings, so the pop is very likely a relief rally already capturing (or
overshooting) the news. The structural cost the BEAR raised (parts/service margin
erosion from independent repair competition) is directionally real but lands 1-2
quarters out, past any tradeable 2-3 session window, so it can't be harvested here
either. Net: neither the BULL's continuation long nor the BEAR's structural fade
clears costs with conviction; a conditional quarter-size fade only turns marginally
positive if the open fails to hold, and a conditional quarter-size long only turns
marginally positive if it holds with volume — both are footnotes, not the base case.
Verdict: NO-TRADE (not scheduled, not simulated). Full debate with citations in
`transcript.md`.
