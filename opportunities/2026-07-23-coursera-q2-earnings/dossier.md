---
id: 2026-07-23-coursera-q2-earnings
title: Coursera Q2 2026 earnings due July 29
status: researched
created: '2026-07-23T17:49:00Z'
event:
  type: earnings
  summary: Coursera reports Q2 2026 results July 29, 2026, a read on enterprise/degree
    segment growth and AI-driven course demand amid a growing EdTech AI adoption tailwind
  impact_window: '2026-07-29'
tickers:
- COUR
sources:
- title: 'ainvest.com: Emerging EdTech Stocks Poised for Growth in 2026'
  url: https://www.ainvest.com/news/emerging-edtech-stocks-poised-growth-2026-2512/
  accessed_at: '2026-07-23T17:49:00Z'
hypothesis:
  statement: 'Stand-aside: there is no COUR-specific edge into the 2026-07-29 print.
    The only bull catalyst is a dated sector listicle (ainvest.com "Emerging EdTech
    Stocks Poised for Growth in 2026"), conceded by the bull himself as near-zero
    alpha, and the 3-month USD 5.375-5.985 range (last USD 5.485) is read by the
    bull as a coiled spring and by the bear as informed selling into the print —
    the same tape with opposite signs, i.e. no directional information. With
    P(up)=P(down)=0.50, a +-12% median earnings move, +-25-32% tails, and ~90bp
    round-trip friction on a sub-USD-1B cap, long EV is -1.65% net and short EV is
    -0.15% net against a ~32% un-hedgeable squeeze tail (~60x tail-to-edge vs a
    7-8x no-trade threshold). Both directional expressions are negative EV; the
    correct action is no position.'
  direction: neutral
  confidence: 80
plan:
  ticker: COUR
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-25T07:56:06Z'
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
  confidence: 80
  lessons_applied:
  - '2026-06-25-nike-q4-fy26: conf<=45 + net EV<2% + tail/edge>>7-8x is a no-trade
    filter, not a size-down'
  - '2026-06-25-nike-q4-fy26: discount negative base rates near 52-wk low (did NOT
    apply — COUR sits mid-range, not at its low, though drifting down)'
  - '2026-06-26-delta-q2-fy26: a catalyst that already drove a multi-week run into
    the print is priced in (did NOT apply — COUR has been range-bound, not
    trending; the disqualifying factor here was absence of any edge, not a stale
    run-up)'
  - '2026-06-26-delta-q2-fy26: when the strongest unrebutted dissent aligns with
    the quant''s own EV math, synthesize to NO-TRADE rather than a quarter-size
    directional position'
  - '2026-07-02-levi-q2-fy26: when the quant says directional EV is ~0/negative and
    the only positive-EV structure is out of mandate, log NO TRADE — do not
    manufacture a minimal directional position for the learning loop'
  dissent: 'Bull''s residual case: a small defined-risk long becomes rational only
    if the tail-to-edge ratio compresses to roughly 10x, which requires a live
    implied-move quote for the 2026-07-29 expiry that nobody on the panel had —
    quant''s ~60x is a modelled estimate, not a market-priced one, and remains
    untested. Bear''s residual case: the fundamental risks (consumer erosion to
    free/AI-native substitutes, enterprise budget cuts, guidance-cut risk) may be
    directionally correct about the print yet still be un-actionable as a naked
    short given the un-hedgeable squeeze tail — a defined-risk put spread would be
    the correct expression but is out of the common-stock mandate.'
  transcript: transcript.md
---

## Scouted 2026-07-23T17:49:00Z

## Researched 2026-07-25T07:56:06Z
Verdict: NO-TRADE (neutral, confidence 80). Three-round panel (bull/bear sonnet,
quant opus; synthesizer opus). Bull's catalyst — enterprise/degree mix-shift and
AI-driven course demand — traced to a generic ainvest.com sector listicle, not a
COUR-specific data point; bull conceded this in Round 2. Price anchors (twelvedata):
COUR at USD 5.485 on 2026-07-24, USD 5.985 on 2026-06-24, USD 5.375 on 2026-04-24 —
range-bound roughly USD 5.35-6.00 over the trailing 3 months, currently mid-to-low
range. Bull read the tight range as a coiled spring; bear read the drift down from
USD 6.00 as informed selling into the print; quant showed these are the same tape
read with opposite signs, carrying no real directional information (P(up)=P(down)
=0.50 after Round 2). Quant's EV: long -1.65% net, short -0.15% net against a
widened ~32% un-hedgeable squeeze tail (~60x tail-to-edge ratio vs the 7-8x
no-trade threshold). Both bull and bear converged to no-trade by Round 2 — bull
deferred to the quant's EV as the deciding number, bear conceded the short is not
investable given the squeeze tail despite believing the fundamental risks (consumer
erosion, enterprise budget cuts) are real. Full debate with citations in
`transcript.md`.
