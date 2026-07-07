---
id: 2026-07-07-fomc-july-decision
title: FOMC July 2026 rate decision
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: macro
  summary: FOMC decides Jul 29; hawkish June dot-plot shift raised odds of a 25bp
    hike vs expected hold.
  impact_window: '2026-07-29'
tickers:
- SPY
sources:
- title: Federal Reserve FOMC calendar
  url: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: The Jul 29 FOMC outcome is a ~70/30 hold/hike coin-flip already reflected
    in the curve and equity vol; an in-line hold is a priced-in non-event that gets
    faded, and the only genuinely positive-EV path (long into a collapsed hike tail)
    is a conditional post-Jul-14-CPI entry the harness cannot pre-commit.
  direction: none
  confidence: 78
plan:
  ticker: SPY
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
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
  dissent: 'Whether a benign June CPI on Jul 14 collapses the hike tail enough to
    make a long into Jul 29 genuinely +EV. Bull says yes (stand-down trigger: live
    hike odds >40%); Bear/Quant say even then an in-line hold delivers vol crush not
    a rally, and the edge stays inside market-implied noise. Resolvable only by re-anchoring
    after the Jul 14 CPI print.'
  last_updated: '2026-07-07T22:16:16Z'
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:16:16Z — NO-TRADE

Three-round panel converged on NO TRADE. The June dot-flip is already in the curve and equity vol; at market-implied ~30% hike odds the executable Jul 29 cash-session leg nets ~0 gross and negative after costs (bull's own inputs: 0.695(+0.75%)+0.305(-1.75%) = -0.013%). Every positive-EV path is a conditional long that depends on the Jul 14 CPI collapsing the hike tail — an entry the harness cannot pre-commit (lesson 3), resting on a 22-day stale anchor (lesson 1). Re-open after the Jul 14 2026 CPI print with a live SPY quote and updated implied hike odds; act only on a ≥10-15pt divergence from ~30%.
