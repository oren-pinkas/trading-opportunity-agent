---
id: 2026-07-15-cintas-q4-fy26-earnings
title: Cintas Q4 FY26 Earnings
status: researched
created: '2026-07-14T05:08:14Z'
event:
  type: earnings
  summary: Cintas reports Q4 FY26 results and initial FY27 guidance Jul 15, a bellwether
    for uniform/facility-services demand
  impact_window: '2026-07-15'
tickers:
- CTAS
sources:
- title: Earnings Calendar and Analysis for This Week (July 13-17) | Kiplinger
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-14T05:08:14Z'
- title: toa price CTAS (twelvedata provider, reconciled close series)
  url: internal://toa-price-cli
  accessed_at: '2026-07-21T14:00:00Z'
hypothesis:
  statement: >-
    CTAS delivered a genuine post-earnings re-rating, not a mechanical pop:
    close series (twelvedata, reconciled) 7/14 pre-print USD 184.26 to 7/15
    USD 192.18 (+4.30%) to 7/16 USD 205.77 (+7.07% follow-through, true peak)
    to 7/17 USD 204.34 (-0.70%) to 7/20 USD 202.01 (-1.14%), net +9.6% versus
    the pre-print anchor. The move is ~6 days stale as of 2026-07-21 and the
    7/17-7/20 pullback is directionally ambiguous without volume data no
    panelist possessed. No panelist had WebSearch access to confirm actual
    EPS, revenue, or FY27 guidance figures versus consensus, so the
    fundamental quality of the beat driving the re-rating is unverified —
    this debate is price-action-only. Quant's EV calc, after conceding the
    bull's strongest point (the 7/16 follow-through is real, not mechanical)
    and correcting an initial price-data error, still lands marginally
    negative for a fresh long from USD 202.01 over a 2-3 week horizon
    (P(+2%)=0.42, P(flat)=0.33, P(-3.5%)=0.25, gross EV -0.04%, net of costs
    approximately -0.15%). The bear's stale-edge/priced-in dissent aligns
    with that negative EV rather than opposing it.
  direction: none
  confidence: 60
plan:
  ticker: CTAS
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
    Strongest unresolved disagreement: interpretation of the 7/17-7/20
    pullback (-1.8% off the USD 205.77 high) with no volume data available to
    any panelist. Bull reads it as normal consolidation within an intact
    re-rating; bear reads it as early distribution/profit-taking and argues
    bull cannot claim momentum-persistence for the up-leg while dismissing the
    down-leg as noise. Judged genuinely unresolvable pending volume/breadth
    data. Flip triggers for a future revisit: a close back above USD 205.77 on
    above-average volume (bullish, small tactical long, stop USD 198), or
    confirmed FY27 guidance materially above consensus (would justify a
    fundamentals-anchored directional entry). Neither condition was met as of
    2026-07-21. Process lesson: all three panelists initially pulled
    conflicting price prints for the same dates (intraday vs. close mismatches,
    a mislabeled peak) and burned most of Round 1/2 reconciling data that
    should have been a single shared, source-verified, close-based series
    established before Round 1 opinions were formed.
  last_updated: '2026-07-21T14:00:00Z'
---

## Scouted 2026-07-14T05:08:14Z

## Researched 2026-07-21T14:00:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). CTAS
reported Q4 FY26 and initial FY27 guidance on 2026-07-15. Reconciled close
series (twelvedata): 7/14 pre-print USD 184.26, 7/15 USD 192.18 (+4.30%), 7/16
USD 205.77 (+7.07% follow-through, true peak — corrected from an initial
mislabeling that put the peak on 7/17), 7/17 USD 204.34 (-0.70%), 7/20 USD
202.01 (-1.14%); net +9.6% versus pre-print. BULL argued the second
consecutive up-day (7/16) is a genuine re-rating signal (sell-side price-target
revisions landing T+1), not a mechanical pop, and read the subsequent pullback
as normal consolidation; conceded ground in Round 2 and downsized to a
half-size, tight-stop (USD 198), 3-5 day tactical long. BEAR argued the edge is
already 6 days stale and priced in, flagged CTAS's already-premium multiple as
raising the bar for further re-rating, read the pullback as a distribution
tell, and flagged an unconfirmed macro risk (labor-market softening versus
FY27 guidance assumptions); leaned toward NO-TRADE over its own fade idea by
Round 2. QUANT initially mis-tabulated the price series and dismissed the 7/16
follow-through as already-consumed PEAD; corrected the data in Round 2,
conceded the follow-through was a real signal, and re-ran EV from the
corrected USD 202.01 entry: gross EV -0.04%, net of costs approximately
-0.15% — still negative, confidence in NO-TRADE loosened from <45% to ~52%.
No persona had WebSearch access to confirm actual EPS/revenue/FY27 guidance
figures — the entire debate is price-action-only, a material gap flagged
explicitly by all three panelists and by the synthesizer. Verdict: NO-TRADE.
Flips only on a reclaim/hold above USD 205.77 on volume, or confirmed FY27
guidance materially above consensus. Full debate in `transcript.md`.
