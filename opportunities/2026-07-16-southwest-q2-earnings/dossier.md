---
id: 2026-07-16-southwest-q2-earnings
title: Southwest Airlines Q2 2026 earnings
status: researched
created: '2026-07-16T05:04:39Z'
event:
  type: earnings
  summary: Southwest reports Q2 2026 results Jul 22 before the open, first full quarter
    since restructuring initiatives took hold
  impact_window: '2026-07-23'
tickers:
- LUV
sources:
- title: Southwest Airlines to Discuss Second Quarter 2026 Financial Results
  url: https://www.stocktitan.net/news/LUV/southwest-airlines-to-discuss-second-quarter-2026-financial-results-dc2hvnc5qbpu.html
  accessed_at: '2026-07-16T05:04:39Z'
hypothesis:
  statement: 'LUV''s Q2 2026 print is a year-telegraphed, priced-in restructuring
    quarter: a sub-2 percent open gap (real prior-close-to-open move -1.77 percent,
    per twelvedata) that went flat (-0.09 percent intraday, -1.86 percent vs prior
    close as of 14:53Z) is a muted, in-line reaction with no post-earnings-drift
    continuation edge below the roughly 5 percent surprise threshold that historically
    matters for airline prints. Neither the bull''s unconfirmed "buyers quietly
    defending the gap" read nor a directional fade has positive expected value net
    of costs.'
  direction: none
  confidence: 22
plan:
  ticker: LUV
  action: no-trade
  entry:
    time: '2026-07-22T13:30:00Z'
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
  dissent: "The bull holds that flat-after-gap-down with no follow-through selling
    is informational (buyers defending the level) and warrants a sized-down long
    into a reversion back toward the USD 49.00 pre-earnings reference, whereas the
    bear and quant say that read is indistinguishable from simple indifference
    without volume, order-flow, or options-skew confirmation, and the quant''s EV
    math rounds to roughly zero-to-negative for both directions once costs are
    included (long-to-target EV about -0.06 percent; short-continuation EV about
    -0.22 to -0.26 percent)."
  last_updated: '2026-07-22T14:53:35Z'
---

## Scouted 2026-07-16T05:04:39Z

## Researched 2026-07-22T14:53:35Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real prices via
`toa price LUV --provider twelvedata`: prior close (2026-07-21 19:59Z) USD 48.66, open
(2026-07-22 13:30Z) USD 47.80 (-1.77 percent gap), and USD 47.755 at 14:53Z (-0.09
percent intraday, -1.86 percent vs prior close) — the bull's initial reference to the
07-16 price (USD 49.02) was stale and overstated the gap as -2.5 percent; the quant
corrected it in Round 1. The muted, sub-2-percent reaction to the first full quarter
under Southwest's telegraphed restructuring (assigned seating, basic economy, route
cuts, Elliott-driven cost discipline) sits below the roughly 5-percent threshold where
post-earnings drift has historically shown any continuation edge, and the flat tape 80+
minutes post-open shows no order-flow confirmation either direction. Bull argued the
stabilization itself is informational and proposed a sized-down long back toward USD
49.00; bear and quant held that "hasn't cracked further" is indistinguishable from "no
edge left" absent volume/skew evidence, and the quant's EV calculation was negative-to-
flat for both a long-to-target and a short-continuation trade after costs. Synthesized
to NO TRADE (confidence 22) per the DAL/LEVI institutional lessons: when the
highest-confidence panelist's EV math is ~0 and the strongest dissent doesn't clear it,
log no-trade rather than manufacture a directional position. Full debate with citations
in `transcript.md`.
