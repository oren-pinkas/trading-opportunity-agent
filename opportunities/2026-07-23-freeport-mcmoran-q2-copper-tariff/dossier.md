---
id: 2026-07-23-freeport-mcmoran-q2-copper-tariff
title: Freeport-McMoRan Q2 earnings to show first full-quarter copper-tariff windfall
status: researched
created: '2026-07-13T23:47:30Z'
event:
  type: earnings
  summary: FCX reports Q2 2026 results July 23 with EPS seen up ~7% YoY, the first
    quarter fully reflecting the 50% Section 232 copper tariff and tight COMEX-driven
    pricing.
  impact_window: '2026-07-23'
tickers:
- FCX
sources:
- title: Freeport-McMoRan jumps as copper prices strengthen on tariff-driven dislocations
  url: https://www.quiverquant.com/news/Freeport-McMoRan+jumps+as+copper+prices+strengthen+on+tariff-driven+dislocations+and+tightening+supply+signals
  accessed_at: '2026-07-13T23:47:30Z'
hypothesis:
  statement: >-
    FCX's Q2 2026 print (reported 2026-07-23) confirmed the Section 232 50% copper
    tariff windfall but delivered no fresh directional edge: the catalyst was already
    discounted into the +3.63% pre-print run ("USD 62.55" on 07-21 19:59Z to
    "USD 64.82" on 07-22 19:59Z), the print produced an unresolved two-way whipsaw
    (gap-down open "USD 62.64" at 13:30Z, 5-minute reversal to "USD 64.46" at 13:35Z,
    fade to a "USD 63.28" close at 19:59Z), and by Round 2 all three panelists had
    converged on near-zero-to-negative expected value. The quant's EV re-run after
    steelmanning both the bull's structural-margin case (continuation 25% to 28%) and
    the bear's distribution read (full round-trip tail 15% to 18%) produced EV_gross
    of +0.08% against 0.15-0.20% costs, i.e. EV_net of roughly -0.07% to -0.12% --
    worse after scrutiny, not better, with an adverse-tail-to-edge ratio beyond 28:1.
    No panelist's confidence in a directional bet exceeded 54, and the highest-rigor
    panelist's directional confidence rose only from 18 to 20. Correct output is no
    position and a watch list.
  direction: none
  confidence: 80
plan:
  ticker: FCX
  action: no-trade
  entry:
    time: '2026-07-23T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-23T19:59:00Z'
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
    The strongest unresolved disagreement is the bull's structural argument (Round 2
    confidence 54): the 50% Section 232 tariff is not a one-time headline but a
    durable level-shift in FCX's realized copper price, so the 07-23 print supplied
    magnitude and durability confirmation -- actual margin realization -- that a
    "known for months" catalyst cannot by definition have fully discounted. Under
    the bull's reweighting (~35/20/20/15/10 vs the quant's 25/20/20/20/15) EV_gross
    flips meaningfully positive and the no-trade call inverts. The quant conceded
    only 3pp of this (continuation 25% to 28%), arguing the rest is double-counting
    the same already-priced catalyst, and simultaneously raised the round-trip tail
    18% on the bear's distribution read (sellers into "USD 64.46", close "USD 63.28",
    gap low "USD 62.64" beneath the "USD 62.55" pre-run-up base never defended) -- so
    the concession was net EV-negative. This is unresolved rather than refuted: the
    bull's own falsifiers (next-session gap-down, break of "USD 62.64" on volume,
    COMEX/LME tariff-arbitrage spread structurally unwinding) and the bear's
    confirmation requirement (break of "USD 62.55") both point at data not yet in
    hand as of the 07-23 close. Whether the print was a re-rating absorbed by
    real-money demand (close +1.02% above the "USD 62.64" open) or distribution into
    strength (-1.83% off the "USD 64.46" high) cannot be adjudicated from a single
    session's two-way volatility.
  last_updated: '2026-07-25T11:35:00Z'
---

## Scouted 2026-07-13T23:47:30Z

## Researched 2026-07-25T11:35:00Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). FCX reported Q2
2026 results 2026-07-23, the first quarter fully reflecting the 50% Section 232
copper tariff. Verified toa/twelvedata price series: "USD 62.55" close 07-21 19:59Z,
"USD 64.82" close 07-22 19:59Z (+3.63% pre-print run), "USD 62.64" open 07-23 13:30Z
(-3.36% gap-down), "USD 64.46" at 13:35Z (+2.9% five-minute reversal), "USD 63.28"
close 07-23 19:59Z (+1.02% vs open, -1.83% off the intraday high). The BULL (58->54)
read the reversal as real-money demand confirming a durable, structural tariff-driven
margin re-rating, proposing a long or a "USD 64-66" call spread. The BEAR (25->15)
read the same tape as classic sell-the-news on an already-discounted catalyst, with
the close-off-highs pattern as distribution, not accumulation, and declined to go
short outright pending next-session confirmation. The QUANT (18->20) ran explicit EV
math: after steelmanning both rebuttals (continuation 25%->28% for the bull's
structural case, round-trip tail 15%->18% for the bear's distribution read), EV_gross
came to +0.08% against 0.15-0.20% round-trip costs/slippage, giving EV_net of roughly
-0.07% to -0.12% -- the edge got worse under scrutiny, not better -- with an
adverse-tail-to-edge ratio beyond 28:1, failing the NKE 2026-07-06 no-trade filter
outright. The quant also rejected the bull's call-spread as a fix: its strikes sit
above the failed "USD 64.46" intraday high, so it needs a rejected level reclaimed
and exceeded before expiry while paying debit into post-event IV crush. Per the LEVI
and DAL 2026-07-12 lessons, when the highest-rigor panelist computes directional EV
at or below zero and the strongest dissent aligns with that math, the call is
NO-TRADE rather than a token position. Verdict: NO-TRADE, confidence 80. Re-engage
triggers (next-session confirmation required, no anticipation): long on a held close
above "USD 64.46" on expanding volume; short on a decisive break of "USD 62.55".
Full debate with citations in `transcript.md`.
