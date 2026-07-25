---
id: 2026-07-23-macau-july-ggr-release
title: Macau July gaming revenue release
status: researched
created: '2026-07-23T09:13:03Z'
event:
  type: economic
  summary: Macau's official July gross gaming revenue print due August 1 is expected
    to show a second straight sharp YoY decline as the World Cup diverted bettors,
    testing whether the mid-July pickup materializes
  impact_window: '2026-08-01'
tickers:
- 1928.HK
- WYNN
- LVS
sources:
- title: CLSA cuts Macau 2026 GGR growth forecast to 2pct as July revenue seen down
    12pct
  url: https://www.ggrasia.com/clsa-cuts-macau-2026-ggr-growth-forecast-to-2pct-as-july-revenue-seen-down-12pct
  accessed_at: '2026-07-23T09:13:03Z'
hypothesis:
  statement: The Macau July 2026 GGR print (due Saturday 2026-08-01) offers no exploitable
    edge - the headline miss was already published a week early by CLSA on 2026-07-23
    (July GGR down 12pct YoY, FY26 growth cut to 2pct) and is priced in, and the print
    lands on a Saturday when NYSE and HKEX are both closed, so no reactive leg exists
    inside the impact window. The only fillable structure - a naked Friday 2026-07-31
    close to Monday 2026-08-03 open weekend-gap hold in WYNN - cannot react to the
    number and degrades to undifferentiated 2-day market beta; modeled gross long EV
    of roughly +0.28pct is fully consumed by 25-35bp round-trip friction, leaving net
    EV at or below zero with Sharpe ~0.1. No live price anchor was obtainable for any
    of the three tickers (twelvedata 429 on WYNN, LVS, 1928.HK), and 1928.HK is
    additionally presumed-untradeable given prior confirmed non-US venue coverage
    gaps. Alternate constructions (options, ticker substitution, wider window) were
    checked and are strictly worse.
  direction: none
  confidence: 91
plan:
  ticker: WYNN
  action: no_trade
  entry:
    time: n/a
    target_price: null
  exit:
    time: n/a
    target_price: null
  expected_profit_pct: 0.0
research:
  last_updated: '2026-07-25T16:17:34Z'
  dissent: Convergence on PASS was genuinely clean - all three personas arrived there
    via two logically independent routes (execution-structural - no venue open on
    the Saturday print date; information-structural - a stale, pre-telegraphed miss
    already priced). Residual disagreement worth remembering for post-mortem - the
    underlying "less-bad-than-feared snapback" pattern claim is unresolved not settled,
    the stated flip condition (verified channel-check ADR gap vs the 12pct consensus
    by 7/29) was never actually checked, and quant frames the Saturday finding as
    demanding a hard scout-time catalyst-timestamp-vs-venue-calendar gate while bear
    treats it as a soft scoring penalty stacked on an already-priced event. See
    transcript.md for full detail.
---

## Scouted 2026-07-23T09:13:03Z

## Researched 2026-07-25T16:17:34Z

Three-round-panel debate (bull/bear/quant) converged unanimously on PASS via two
independent lines: (1) execution-structural - 2026-08-01 is a Saturday, so no venue
(NYSE, HKEX) is open inside the impact window and the only fillable structure is a
naked Friday-close-to-Monday-open weekend-gap hold that cannot react to the print;
(2) information-structural - the CLSA -12pct July GGR estimate was published a full
week ahead of the print and is already priced in. No live price anchor was obtainable
for WYNN, LVS, or 1928.HK (twelvedata rate-limited); 1928.HK additionally presumed
untradeable given prior confirmed non-US venue coverage gaps. No trade recorded. Full
transcript: transcript.md.
