---
id: 2026-07-15-asml-q2-fy26
title: ASML reports Q2 FY26 earnings before market open
status: researched
created: '2026-07-12T23:20:25Z'
event:
  type: earnings
  summary: ASML reports Q2 2026 results on July 15; lithography order backlog and
    China export-control commentary are key swing factors for chip-equipment names.
  impact_window: '2026-07-15'
tickers:
- ASML
sources:
- title: 'ASML Q2 Earnings Loom: Buy, Sell or Hold the Stock Ahead of Results?'
  url: https://finance.yahoo.com/markets/stocks/articles/asml-q2-earnings-loom-buy-153000600.html
  accessed_at: '2026-07-12T23:20:25Z'
hypothesis:
  statement: >-
    After a 10.4% pre-print drawdown (USD 1990.45 on 06-30 to USD 1783.59 on
    07-14), ASML's Q2 beat produced only a modest +1.76% print-day pop to USD
    1815.04 that sits well within its normal ~7% earnings-day variance,
    indicating no durable directional edge. Residual China export-control risk
    is one-sided to the downside, so even a post-confirmation intraday
    continuation entry carries a fat left tail; the quant's conditional EV
    (+0.09% gross) is flat-to-negative after costs and fails the ~2% net-EV
    no-trade filter by an order of magnitude.
  direction: long
  confidence: 32
plan:
  ticker: ASML
  action: no-trade
  entry:
    time: '2026-07-15T13:35:00Z'
    target_price: null
  exit:
    time: '2026-07-15T19:59:00Z'
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
    Tail symmetry and whether a post-confirmation entry changes the trade. The
    bull maintains the pre-print selloff was overdone and the print confirmed a
    genuine re-rate, so a post-pop entry is a valid (if small) momentum-
    continuation trade; the bear maintains the China known-unknown makes the
    downside tail structurally fatter than the upside, so the conditional edge
    is negatively skewed, not merely thin. The quant's conditional tree
    (+0.09% gross EV) numerically favors the bear's asymmetry view, but no
    participant established the actual probability or magnitude of a
    China-headline shock between entry and exit, leaving the true shape of the
    left tail unquantified.
  last_updated: '2026-07-21T13:30:06Z'
---

## Scouted 2026-07-12T23:20:25Z

## Researched 2026-07-21T13:30:06Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), rerun with
real prices (`toa price`, provider twelvedata) after a prior 2026-07-07 run was
blocked by a stub-data outage. ASML fell 10.4% pre-print (USD 1990.45 on 06-30
to USD 1783.59 on 07-14), then popped only +1.76% on the print-day close (USD
1815.04) — inside its normal ~7% earnings-day variance, not a breakout. The
BULL conceded the pre-print decline plausibly reflected a genuine, unpriced
China export-control risk and downgraded from a re-rating thesis to a small
confirmed-momentum continuation play. The BEAR held structural NO-TRADE
throughout and argued the China known-unknown skews the downside tail fatter
than the upside. The QUANT's conditional EV recompute (+0.09% gross,
flat-to-negative net) was decisive: no framing clears the ~2% net-EV /
defined-risk-only filter. Verdict: NO-TRADE. Full debate with citations in
`transcript.md`.
