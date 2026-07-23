---
id: 2026-07-22-kratos-q2-2026-earnings
title: Kratos Defense Q2 2026 earnings
status: researched
created: '2026-07-22T07:00:28Z'
event:
  type: earnings
  summary: KTOS reports Q2 2026 results amid fresh USD 156 million counter-drone contract
    win and defense budget tailwinds
  impact_window: '2026-07-30'
tickers:
- KTOS
sources:
- title: StockTitan - Kratos Awarded Counter-Drone Contract
  url: https://www.stocktitan.net/news/KTOS/kratos-receives-mobile-counter-unmanned-aircraft-system-c-uas-nz7j9czkxfzz.html
  accessed_at: '2026-07-22T07:00:28Z'
hypothesis:
  statement: >-
    The panel converges on standing aside. KTOS drifted ~-3.6 percent over the
    trailing week ($49.705 on 7/15 to $47.93 on 7/22 close), including a -0.7
    percent close on the very day the USD 156 million counter-drone contract was
    announced. The bear's read - a same-day, catalyst-specific rejection - is
    more parsimonious than the bull's "waiting for confirmation" alternative,
    and it independently corroborates the quant's EV math. The 156 million award
    is roughly 13 percent of one year's ~1.2 billion revenue but spread over an
    unknown multi-year delivery schedule, making it immaterial to the Q2 print
    itself. With no dossier-grounded consensus estimate or options-implied move
    to anchor probabilities, the quant's directional EV came out negative in
    both rounds (-0.34 percent gross in round 1, worsening to -0.93 percent
    gross in round 2 after weighting the same-day selloff), and even the bull's
    admissible defined-risk call spread structure scores negative expectancy
    since a plausible beat only partially fills the OTM band while the debit is
    a guaranteed drag. The institutional no-trade filter fires.
  direction: none
  confidence: 72
plan:
  ticker: KTOS
  action: no-trade
  entry:
    time: '2026-07-29T19:59:00Z'
    target_price: null
  exit:
    time: '2026-07-30T19:59:00Z'
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
    Bull's contention that the -3.6 percent weekly drift is over-read - soft
    pre-print tape conflated with earnings-specific information - versus bear's
    more parsimonious "same-day rejection is catalyst-specific" read, which
    rests on a single price observation. The decisive test bear proposed -
    whether the 7/22 selloff was index/ETF-driven (XAR/ITA also down) versus
    KTOS-specific - was never verified with data in this debate; the no-trade
    verdict is robust under either resolution of that gap.
  last_updated: '2026-07-23T18:30:02Z'
---

## Scouted 2026-07-22T07:00:28Z

## Researched 2026-07-23T18:30:02Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). KTOS reports Q2
2026 with impact window 2026-07-30 (exact pre/post-market timing not confirmed in the
dossier). Price data via `toa price` (twelvedata): $49.705 close 7/15, $48.20 close
7/21, $48.20 open 7/22, $47.93 close 7/22 (-0.7 percent the same day the USD 156
million counter-drone contract hit the wire) - a net ~-3.6 percent trailing-week
drift despite the positive headline.

The BEAR's same-day-selloff read was the decisive data point: a genuinely bullish,
unpriced catalyst does not get sold into on its own announcement day. The QUANT's EV
math corroborated this independently - round 1 gross EV of -0.34 percent worsened to
-0.93 percent in round 2 after re-weighting P(beat) down and P(miss) up given the
tape. The BULL conceded the quant's structural point (an unhedged directional bet has
a fat left tail with no dossier-grounded edge to size against) and retreated from
"trade the gap" to at most a small defined-risk call spread - which the quant then
also scored negative-EV, since a plausible beat only partially fills the OTM band
while the debit is a guaranteed drag.

Verdict: NO-TRADE. direction=none, confidence=72. Open gap: whether the 7/22 selloff
was index/ETF-driven (XAR/ITA also down that day) versus KTOS-specific was never
verified - this caps confidence rather than raising it, but the no-trade call is
robust either way. Full debate with citations in `transcript.md`.
