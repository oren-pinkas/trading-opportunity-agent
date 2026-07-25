---
id: 2026-07-23-rba-august-rate-decision
title: 'RBA August rate decision: hold vs hike split'
status: researched
created: '2026-07-23T11:19:21Z'
event:
  type: economic
  summary: The Reserve Bank of Australia meets Aug 11, 2026 with economists split
    between a hold at 4.35 percent (CBA, NAB, ANZ) and a hike (Westpac) on persistent
    inflation risk.
  impact_window: '2026-08-11'
tickers:
- EWA
- FXA
sources:
- title: What experts predict for the RBA's August 2026 interest rate decision
  url: https://www.aussie.com.au/insights/news/expert-predictions-rba-rates/
  accessed_at: '2026-07-23T11:19:21Z'
hypothesis:
  statement: 'The fractured 3-1 RBA forecaster split (CBA, NAB, ANZ hold at 4.35
    percent vs Westpac hike) does not create a tradeable edge in EWA or FXA ahead
    of the Aug 11, 2026 decision: on a derived P(hike) of about 20 percent (vs a
    required breakeven above 33.3 percent at 20bp friction, above 47.6 percent at
    realistic 30-40bp overnight-gap friction) and an assumed ~0.9 percent FXA hike-response,
    every executable structure is net-negative EV, and the announcement lands ~04:30
    UTC with US cash markets closed, so the move arrives as an unfillable overnight
    gap rather than a fillable price path. EWA is separately rejected on instrument
    construction (offsetting equity and FX legs). The dossier also lacks the two
    inputs that could overturn this (market-implied odds, live price anchor), so
    the correct action is to stand aside.'
  direction: none
  confidence: 84
plan:
  ticker: FXA
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: 'Sharpest unresolved disagreement is Bull vs Quant on the magnitude input
    the whole NO-TRADE verdict rests on: Quant assumes a hike surprise moves FXA
    ~0.9 percent (hold ~-0.15 percent), giving breakeven p* of 33.3 percent (20bp
    friction) to 47.6 percent (realistic gap friction), both above Quant''s own 20
    percent estimate and Bull''s undefended 30-35 percent. Bull argued the true response
    could be 1.3-1.5 percent-plus but conceded no dossier-grade evidence exists for
    it; Quant conceded a +2 percent move would drop breakeven to above 10 percent,
    which its own 20 percent estimate clears. The unanimity is unanimity over an
    invented number. Secondary point: Bear''s "priced in" (informational) and Quant''s
    "fails cost math regardless" (structural) are independent gates that would respond
    in opposite directions to a revealed market-implied probability - agreement here
    is not corroboration, per the project lesson on false consensus under a data
    blackout. Reopen only if an empirical FXA gap distribution, revealed market-implied
    odds, or a convex instrument becomes available.'
  last_updated: '2026-07-25T23:39:17Z'
---

## Scouted 2026-07-23T11:19:21Z

## Researched 2026-07-25T23:39:17Z

Three-round panel debate (bull/bear/quant) converged unanimously on NO TRADE by
Round 2. Bull conceded the execution-reality objection (RBA announces ~04:30 UTC
while US cash markets are closed, so the entire move arrives as an unfillable
overnight gap) kills every version of the proposed long-FXA plan. Bear hardened
from "token size" to full skip once the same execution-window finding revealed the
position would be unhedgeable overnight regardless of direction. Quant's structural
EV argument (long FXA net EV -0.137% to -0.262% at 20bp friction; breakeven requires
P(hike) > 33.3%, or > 47.6% under realistic overnight-gap friction, against a derived
P(hike) of ~20%) survived every stress test, including a three-state model built to
be maximally generous to the bull case. Full transcript: `transcript.md`.

Not recorded as a live trade. See dossier frontmatter `hypothesis`/`plan`/`research`
and `transcript.md` for full reasoning and the unresolved dissent (the FXA
hike-response magnitude is unanchored — invented at ~0.9% vs a plausible 1.5-2%+
that would flip the verdict).
