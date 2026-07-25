---
id: 2026-07-23-aig-q2-earnings
title: AIG Q2 FY26 earnings
status: researched
created: '2026-07-23T19:57:39Z'
event:
  type: earnings
  summary: American International Group reports Q2 2026 results Aug 6 after market
    close; analysts forecast adjusted EPS of USD 1.93, up 6.6% year over year, with
    AIG having beaten estimates each of the last four quarters.
  impact_window: '2026-08-06'
tickers:
- AIG
sources:
- title: 'Yahoo Finance: American International''s Q2 2026 Earnings: What to Expect'
  url: https://finance.yahoo.com/markets/stocks/articles/american-internationals-q2-2026-earnings-122027527.html
  accessed_at: '2026-07-23T19:57:39Z'
hypothesis:
  statement: AIG's Q2 2026 print is a well-telegraphed catalyst with no identified
    information edge; the 4-quarter beat streak and consensus +6.6% YoY EPS growth
    are already in the USD 79.14 reference price, and the variables that would
    actually move the stock (beat magnitude, long-tail casualty reserve
    development, buyback pace, cat-loss framing mid-hurricane-season, portfolio
    rate sensitivity) are unknowable pre-print and asymmetric in kind (reserve
    charges re-rate book value permanently vs. an EPS beat re-rating one
    quarter).
  direction: no-trade
  confidence: 74
plan:
  ticker: AIG
  action: none
  entry: null
  exit: null
  expected_profit_pct: 0.0
  note: No position taken; see transcript.md for the conditions (reserve-development
    edge, buyback authorization signal, in-mandate volatility structure, or
    post-print 08-07 confirmation trade) that would make this tradeable on a
    future revisit.
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: 'The width and direction of the left tail was never adjudicated with
    data: the bull argues it is overstated given AIG''s de-risking/Corebridge
    separation (true tail -4%/-5%, EV flips positive), while bear and quant
    argue it is understated, since reserve development is
    low-frequency/high-severity and can hide beneath a clean-looking beat.
    See transcript.md.'
  last_updated: '2026-07-25T00:55:57Z'
---

## Scouted 2026-07-23T19:57:39Z

## Researched 2026-07-25T00:55:57Z

Three-round-panel debate (bull/bear/quant → synthesizer) concluded NO-TRADE, confidence 74.
Quant EV for a naive long-the-beat trade: net ≈ -0.42% after rebuttal, adverse-tail-to-edge ratio
≈ 26:1 — fails the no-trade filter. Full transcript: `transcript.md`.
