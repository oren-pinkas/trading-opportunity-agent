---
id: 2026-07-07-june-cpi-report
title: June 2026 CPI report
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: economic
  summary: June CPI released Jul 14; prior print ran hot at 4.2% YoY, a key input
    to July FOMC and rate-sensitive assets.
  impact_window: '2026-07-14'
tickers:
- TLT
sources:
- title: BLS CPI release schedule
  url: https://www.bls.gov/schedule/news_release/cpi.htm
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: June 2026 CPI (released 07-14, prior hot at 4.2% YoY) prints against
    a consensus already forecasting deceleration to ~4.0%, so an in-line print is
    already in the curve and only a differentiated miss moves TLT. A TLT long held
    through the 12:30 UTC print gap faces a roughly symmetric outcome distribution
    with a mild hot tilt, yielding ~-0.20% net EV; the bull case requires an unproven
    >=10pp hot->soft distribution shift with no line-item evidence. No executable
    edge at current information.
  direction: none
  confidence: 22
plan:
  ticker: TLT
  action: no-trade
  entry:
    time: '2026-07-13T20:00:00Z'
    target_price: 462.11
  exit:
    time: '2026-07-14T15:00:00Z'
    target_price: 471.0
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
  dissent: 'Bull vs Quant on the mild-hot tilt in the outcome distribution. Bull reads
    it as the market bracing for hot, so a directional TLT long harvests a mispricing
    that mean-reverts dovish (cool bought, hot faded). Quant reads the same symmetric
    gap plus mild hot tilt as simply -EV: absent a MEASURED option put-skew richer
    than his 30% P(hot), or a forecast that beats the ~4.0% consensus, there is no
    mispricing to harvest, only a coin flip with costs. Resolves at execution time
    via three currently-unavailable inputs: (1) live consensus number -- if ~4.1%+,
    the deceleration thesis IS consensus and the edge is gone; bull needs a concrete
    sub-3.7% line-item case. (2) TLT/TY option put-skew -- rich downside skew confirms
    the market is paying up for hot protection (supports bull, could flip EV positive);
    flat skew confirms Quant''s coin-flip. (3) Live TLT level vs 52wk high -- if extended
    to highs, the dovish repricing is already in (lesson 2: fade/shrink), independently
    killing the long. All three fail or are unmeasured now, which is the reason for
    SKIP.'
  last_updated: '2026-07-07T22:30:00Z'
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:30:00Z — NO-TRADE

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Converged verdict: SKIP (2 of 3).** Bear and Quant both reached no-trade; the Bull amended to a half-size long but conditioned it on live checks (consensus, skew, 52wk-high) that all fail or are unmeasured at current information.

**Quant EV (decisive):** Held-through-gap long, distribution consensus ~4.0% -> Hot >=4.3% 30% x -2.0%; In-line 45% x ~0%; Soft <=3.7% 25% x +2.0% = -0.10% gross, ~= -0.20% net after ~0.10% round-trip cost + overnight carry. Breakeven needs P(soft)-P(hot) >= ~10pp beyond consensus (unproven) OR rich hot option skew (unmeasured). The stub anchor 462.11 (2026-07-07T20:00Z) must be re-derived off a live pre-event quote per lesson 1; a >~0.5-1% drift voids the plan.

**Would-have-been trade (recorded for post-mortem):** BUY TLT, entry 2026-07-13T20:00Z ~462.11, exit 2026-07-14T15:00Z, target ~471 (+2%). Bull's stated stop ~458 (-1%) flagged FICTIONAL by Quant -- a hot print gaps through it, filling near -2.0% to -2.5%, so realized R/R is worse and more symmetric than advertised.

**Lessons applied:** #3 fillability is NOT the blocker here (the 7/13-close entry is a fillable order that owns the gap, not a pre-market conditional); #4 is -- the bull's 'cool bought / hot faded' is a reaction-function assertion, not a differentiated surprise vs consensus; #1 anchor drift; #2 pending the live 52wk-high check.

Full round-by-round debate in transcript.md.
