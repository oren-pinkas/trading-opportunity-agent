---
id: 2026-07-22-henry-boot-profit-warning
title: Henry Boot issues second profit warning of 2026
status: researched
created: '2026-07-22T17:49:00Z'
event:
  type: earnings
  summary: UK property and construction group Henry Boot (BOOT.L) warned annual pre-tax
    profit will be significantly below the GBP 20.4M market expectation, citing Middle
    East conflict and domestic political uncertainty hitting land-plot sales; next
    preliminary results expected around March 2027.
  impact_window: '2027-03-24'
tickers:
- BOOT.L
sources:
- title: "UK's Henry Boot warns on profit again as Iran war, domestic nerves hit sales - MarketScreener"
  url: https://www.marketscreener.com/news/uk-s-henry-boot-warns-on-profit-again-as-iran-war-domestic-nerves-hit-sales-ce7f51d8d08ff62d
  accessed_at: '2026-07-22T17:49:00Z'
hypothesis:
  statement: >-
    Henry Boot's second 2026 profit warning is plausibly a deferral-driven
    overshoot with a mildly right-skewed payoff (quant's corrected EV sketch:
    +4.5% up-tail vs -6.0% down-tail, center of mass still negative). But no
    verified price, market cap, volatility, borrow cost, or options chain
    exists for BOOT.L (twelvedata returns HTTP 404 for this LSE ticker), and
    an 8-month data-free window to the 2027-03-24 prelims removes any
    validating datapoint before then. With direction unresolved and structure
    unpriceable, there is no measurable edge to act on today.
  direction: none
  confidence: 62
plan:
  ticker: BOOT.L
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
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
  dissent: >-
    The convergence to NO TRADE is a data-availability verdict, not a resolved
    directional one. Strip away the missing price feed and the residual sign
    disagreement leans mild-bullish, not neutral: quant's own corrected math
    shows a right-skewed distribution where long convexity beats short, and
    quant explicitly sided with the bull over the bear on structure. The
    unresolved crux is the bear's unfalsifiability argument -- "deferred not
    destroyed" and "capitulation overshoot" are both unprovable without
    price/order-book data -- which quant made the tiebreaker. Post-mortem
    gold: if BOOT.L later bounced, log whether NO TRADE cost us a
    positive-skew long we correctly identified but couldn't size because of a
    tooling gap (twelvedata 404 on this LSE ticker), i.e. an infrastructure
    failure masquerading as analytical prudence.
  last_updated: '2026-07-23T17:15:20Z'
---

## Scouted 2026-07-22T17:49:00Z

## Researched 2026-07-23T17:15:20Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Blocked
throughout by a data gap: twelvedata returns HTTP 404 for BOOT.L, so no panelist
ever had a verified price, market cap, vol, or borrow cost. Bull argued
deferred-not-destroyed land-plot revenue plus a capitulation-overshoot setup for
a delayed long entry; bear called both claims unfalsifiable without price/volume
data and flagged repeat-warning credibility risk plus an 8-month dead zone to
the 2027-03-24 prelims; quant's EV sketch (corrected in R2) showed a
right-skewed but net-negative gross EV (+4.5% up-tail vs -6.0% down-tail),
siding with bull on structure (long convexity beats short) but with bear on
tradeability (no price feed, no options chain, no near-term catalyst). Verdict:
NO-TRADE, confidence 62. Contingent revisit only if all three hold: (a) a live
quote confirms the post-warning gap is under 8-10% (overshoot incomplete), (b)
borrow cost or an options chain becomes available, (c) a defined stop can be
set -- in which case the corrected skew favors a small long or defined-risk
long-convexity structure, never a short. Full debate in `transcript.md`.
