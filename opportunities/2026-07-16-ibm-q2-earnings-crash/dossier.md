---
id: 2026-07-16-ibm-q2-earnings-crash
title: IBM shares crash 25pct, worst day since 1968, on Q2 revenue miss
status: researched
created: '2026-07-16T10:24:00Z'
event:
  type: earnings
  summary: IBM Q2 revenue USD 17.2B missed estimates as enterprises delayed deals
    to buy AI servers/memory instead; stock had its worst day on record
  impact_window: '2026-10-15'
tickers:
- IBM
sources:
- title: 'Stock Market Today, July 14: IBM Slides After Profit Warning Weighs on Dow'
  url: https://www.fool.com/coverage/stock-market-today/2026/07/14/stock-market-today-july-14-ibm-slides-after-profit-warning-weighs-on-dow/
  accessed_at: '2026-07-16T10:24:00Z'
hypothesis:
  statement: IBM has stabilized around USD 211 after a structural (not purely
    emotional) ~25pct re-rating on the Q2 revenue miss. The bull's near-term
    grind-up case and the bear's continued-downside case are both plausible but
    under-evidenced, and the quant's two-sided EV stress test shows the edge on
    either side is smaller than transaction/carry cost plus tail risk. No
    risk-adjusted edge in any direction until hard evidence arrives (Q3
    backlog/RPO, AI-capex comp reads from peers, more than 4 days of post-crash
    tape).
  direction: no_trade
  confidence: 68
plan:
  ticker: IBM
  action: no_trade
  note: Net EV on a long is USD +0.41pct over 85 days to the 2026-10-15 print
    (about 1.7pct annualized), below the risk-free rate and failing the
    "net EV under 2pct plus high adverse-tail ratio" no-trade filter; the
    mirror short is also net-negative after borrow/carry since most of the
    re-rating is already priced in. Only structure the panel would entertain
    is a small defined-risk call spread (long-shot on the relief scenario,
    risk capped at 1-2pct of capital, expiring at/before 2026-10-15) -
    optional lottery exposure, not an edge. Watch triggers to reopen the
    debate - Q3 backlog/RPO print, deferred-deal conversion commentary,
    AI-capex comp reads from NVDA/hyperscalers/memory makers, and post-crash
    tape extending the bounce into a sustained reclaim of USD 218-225.
    Re-evaluate no later than 2026-10-15.
  expected_profit_pct: 0
research:
  last_updated: '2026-07-22T10:53:20Z'
  strategy: three-round-panel
  personas:
    bull: {model: sonnet, confidence: 45}
    bear: {model: sonnet, confidence: 20}
    quant: {model: opus, confidence: 41}
  lessons_reviewed:
  - 'earnings/NKE: confidence <=45 with un-hedgeable positive tail and net EV
    <2pct against a 7-8x adverse-tail-to-edge ratio is a no-trade filter, not
    a size-down'
  - 'earnings/DAL: when the strongest unrebutted dissent aligns with the
    quant''s own EV math, synthesize to NO-TRADE rather than a quarter-size
    directional position'
  - 'earnings/LEVI: when directional EV is ~0 and the only positive-EV
    structure is out of mandate, log NO TRADE rather than manufacturing a
    minimal directional position for the learning loop'
  dissent: Is the relief-scenario probability ~25pct (quant/bull base case) or
    ~17-20pct (bear haircut)? The long/no-trade boundary hinges on this ~5-8pt
    of probability mass - at 25pct the bull-tilt EV clears +2pct; redistributed
    to the down-tails it flips decisively negative. Checkable at the
    2026-10-15 Q3 print - re-accelerating revenue plus confirmed backlog/RPO
    conversion would validate the bull's weight and the passed long
    (USD 211 to 218-240); a second consecutive miss with continued deal
    deferral would validate the bear's haircut and the no-trade call.
---

## Scouted 2026-07-16T10:24:00Z

## Researched 2026-07-22T10:53:20Z

Three-round-panel debate (bull/bear/quant) converged on NO TRADE. Full transcript:
`transcript.md`. Synthesizer confidence 68/100 in the no-trade conclusion; net EV on
either a long or short fails to clear costs/carry against a binary 2026-10-15
earnings print. Revisit at or before that date, or sooner if Q3 backlog/RPO or
AI-capex comp data emerges.
