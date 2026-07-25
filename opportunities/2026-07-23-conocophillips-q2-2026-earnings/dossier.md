---
id: 2026-07-23-conocophillips-q2-2026-earnings
title: ConocoPhillips Q2 2026 Earnings
status: researched
created: '2026-07-23T05:29:18Z'
event:
  type: earnings
  summary: COP reports Q2 2026 results Aug 6 with analysts expecting EPS up over 100%
    y/y; oil majors' quarter bracketed by falling WTI/Brent amid supply glut
  impact_window: '2026-08-06'
tickers:
- COP
sources:
- title: ConocoPhillips to hold second-quarter earnings conference call on Thursday,
    Aug. 6
  url: https://www.conocophillips.com/news-media/story/conocophillips-to-hold-second-quarter-earnings-conference-call-on-thursday-aug-6/
  accessed_at: '2026-07-23T05:29:18Z'
hypothesis:
  statement: 'Stand-aside: the "EPS +100% y/y" headline is a comp-base artifact against
    a depressed Q2 2025 print, not a fundamental signal — consensus IS the doubling,
    so clearing it carries no incremental information. COP has also run +16.3% off
    its Jul 1 low (USD 103.55 to USD 120.44) into the print, near the top of its 2026
    range, which is priced-in-catalyst territory (DAL pattern), not a beaten-down
    snapback setup (NKE pattern does not apply here). Net directional EV is negative
    on both sides after costs, and the adverse-tail-to-edge ratio breaches the no-trade
    filter by a wide margin.'
  direction: neutral
  confidence: 45
plan:
  ticker: COP
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-25T07:48:14Z'
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
  verdict: no-trade
  confidence: 45
  lessons_applied:
  - '2026-06-25-nike-q4-fy26: no-trade filter when conf<=45 + net EV<2% + tail/edge>>7-8x
    is a no-trade filter, not a size-down'
  - '2026-06-25-nike-q4-fy26: discount negative base rates near 52-wk low (did NOT
    apply — COP is near its 2026 high, not its low)'
  - '2026-06-26-delta-q2-fy26: a catalyst that already drove a large multi-week run
    into the print is priced in, do not re-bet the same fundamental as a fresh gap
    trigger (COP +16.3% off its Jul 1 low into the Aug 6 print)'
  - '2026-06-26-delta-q2-fy26: when the strongest unrebutted dissent aligns with the
    quant''s own EV math, synthesize to NO-TRADE rather than a quarter-size directional
    position'
  - '2026-07-02-levi-q2-fy26: when the quant says directional EV is ~0/negative and
    the only positive-EV structure is out of mandate, log NO TRADE — do not manufacture
    a minimal directional position for the learning loop'
  dissent: 'Bull''s residual case: a small, defined-risk call debit spread (<=0.25%
    of book) would be worth expressing IF a live implied-move quote showed the options
    market pricing the Aug 6 move below ~2%, i.e. underpricing the sector-overhang
    asymmetry. Nobody on the panel had an actual IV quote to confirm or refute this
    — it is the one falsifiable condition that could flip the verdict, and it remains
    untested.'
  transcript: transcript.md
---

## Scouted 2026-07-23T05:29:18Z

## Researched 2026-07-25T07:48:14Z
Verdict: NO-TRADE (neutral, confidence 45). Three-round panel (bull/bear sonnet, quant
opus; synthesizer opus). The "+100% y/y" EPS headline is a comp-base artifact (Q2 2025
was a depressed base) that consensus already embeds — beating it is not informative.
Quant's live price pull (twelvedata) showed COP at USD 120.44 on 2026-07-24, up 16.3%
from its USD 103.55 Jul 1 low and within 1.3% of its USD 121.97 2026 high — a
multi-week run into the print, not a beaten-down snapback setup. Net EV negative on
both directions after costs (quant's revised calc: -0.52% net EV, ~12.5x adverse-tail-
to-edge ratio, far past the ~7-8x no-trade threshold). Short side also fails: positive
gross EV wiped by frictions, plus an un-hedgeable positive tail (buyback/dividend/
Willow-LNG news). Bull conceded the y/y-comp point and downgraded to a small
IV-contingent call spread, but no IV quote was available to confirm the move isn't
already priced in. Full debate with citations in `transcript.md`.
