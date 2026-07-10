---
id: 2026-07-08-ferrari-q2-earnings
title: Ferrari Q2 2026 earnings
status: researched
created: '2026-07-08T17:21:22Z'
event:
  type: earnings
  summary: Ferrari reports Group results for the second quarter of 2026 on July 30.
  impact_window: '2026-07-30'
tickers:
- RACE
sources:
- title: Ferrari N.V. - Form 6-K - FY2026 (corporate calendar)
  url: https://www.sec.gov/Archives/edgar/data/0001648416/000164841626000008/fnvcorpcal26prex.htm
  accessed_at: '2026-07-08T17:21:22Z'
hypothesis:
  statement: >-
    All three personas independently converged on the same core finding: there
    is no reliable pre-print directional edge in RACE common equity into the
    2026-07-30 Q2 report. The bull ultimately abandoned a static long for a
    momentum-confirmation entry (a reactive trade), the bear defaulted to
    no-trade absent a live trigger, and the quant showed linear-equity EV is
    negative in both directions (gross ~0%, net ~-0.2% to -0.4% after
    slippage/costs/borrow) because the only genuine edge -- short volatility --
    is inexpressible on an equity-only platform. The dominant structural fact
    is a "quality beat" setup: at ~36.5x P/E with a fresh pre-print upgrade
    cluster (UBS $497 / MS OW $438 / Wolfe Outperform) raising the bar, and
    Q1'26's beat-and-reaffirm-then-sell-4% as the tightest comp, a mere
    reaffirm likely sells the news while only an explicit guidance raise
    justifies a pop -- and the un-hedgeable beat-driven squeeze tail (Q2'25
    -10.81%, Q4'25 +5%) disqualifies a naked short on the risk filter alone.
    The only live disagreement is what to do after the market reacts (a
    post-open gap + fundamental-trigger PEAD flip), which is conditional logic
    the flat plan schema cannot encode. Calibrated pre-print directional edge
    is effectively nil.
  direction: none
  confidence: 8
plan:
  ticker: RACE
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
    The strongest unresolved disagreement is post-reaction directional skew:
    the bear argues the reaction is structurally downside-heavy (all three
    historical down-prints -10.81%/-3.97%/-3.5% exceed the up-prints
    +5%/+2.71% in magnitude, and a reaffirm-not-raise "quality beat" will sell
    as it did in Q1'26), while the quant argues the tails are effectively
    symmetric with reaction autocorrelation ~0, making the print a coin flip
    whose only exploitable feature is variance -- and the bull argues the
    richer Q2 catalyst stack (full-quarter F80, Amalfi/849 Testarossa/296
    Speciale ramp) could flip the fork toward a guidance raise and an upside
    gap. Testable post-mortem: (1) did Ferrari reaffirm vs. raise FY2026
    guidance, and did the 29.5% EBIT margin floor hold or move; (2) what was
    the realized same-day close move and sign -- a sell on beat-and-reaffirm
    confirms the bear, a pop on a raise vindicates the bull, a move well
    inside the ~8% implied straddle regardless of sign vindicates the quant's
    short-vol thesis; (3) did day-1 direction persist into day 2-3 (PEAD) or
    mean-revert, testing whether the un-encodable conditional flip would
    actually have paid.
  last_updated: '2026-07-10T13:20:00Z'
---

## Scouted 2026-07-08T17:21:22Z

## Researched 2026-07-10T13:20:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Ferrari
reports Q2 2026 results 2026-07-30 (pre-market Europe, ahead of the 13:30Z NYSE
open). All three personas converged on NO pre-print directional edge: the
BULL's catalyst case (order book to end-2027, F80/12Cilindri mix, three
pre-print sell-side upgrades to $438-497) collapsed under its own concession
that Q1 2026 -- a clean beat with reaffirmed guidance -- still sold off ~4%,
the closest available comp for a likely "quality beat, no raise" Q2. The BEAR's
skepticism (margin at the 29.5% floor, -4.4% unit deliveries, tariff/FX drag)
was real but not strong enough to support an outright short given a real,
un-hedgeable beat-driven squeeze tail (Q4'25 +5%) and a still-net-bullish
consensus (11 Buy/3 Hold/0 Sell) -- both bull and bear ultimately downgraded to
reactive, trigger-only trades rather than pre-print positions. The QUANT was
decisive: RACE's only positive-EV structure is short volatility (implied ~8%
weekly vs. ~5.2% mean realized move), which this equity-only, 1-min-bar
platform cannot execute; stripped of its capping wings and forced into linear
equity, the same edge becomes an unbounded coin-flip bet with net EV of
roughly -0.2% to -0.4% after costs in either direction. Verdict: NO-TRADE
(not scheduled, not simulated). All three personas independently designed a
post-open reactive/PEAD-style flip (long on a confirmed guidance-raise gap-up,
short on a confirmed gap-down + hard fundamental trigger) -- valuable as
process but not encodable in this platform's static entry/exit plan schema, so
it is recorded here as narrative only. Flips to an active pre-print position
only on a hard guidance signal (explicit raise or a cut through the 29.5% EBIT
floor) surfacing before 2026-07-30. Note: local `toa price` returned the
offline stub ($423.86); persona targets used the real web-researched spot
(~$375 as of 2026-07-09/10). Full debate with citations in `transcript.md`.
