---
id: 2026-07-23-shake-shack-q2-earnings
title: Shake Shack Q2 2026 earnings, Aug 5
status: researched
created: '2026-07-23T16:29:19Z'
event:
  type: earnings
  summary: Shake Shack reports Q2 2026 results before market open Aug 5 2026, after
    previously trimming its Q2 profit and revenue outlook
  impact_window: '2026-08-05'
tickers:
- SHAK
sources:
- title: Shake Shack to Announce Second Quarter 2026 Financial Results on August 5,
    2026
  url: https://finance.yahoo.com/news/shake-shack-announce-second-quarter-120000451.html
  accessed_at: '2026-07-23T16:29:19Z'
hypothesis:
  statement: The July guide-cut is plausibly a kitchen-sink reset setting up a
    beat-and-raise into the Aug 5 BMO print, but the panel could not establish an
    edge large enough to trade. Anchor price SHAK = USD 57.24 at 2026-07-24T17:00Z
    (twelvedata). Against an assumed ~9 percent implied move, the directional base
    rate is only ~50-55 percent, producing gross EV of roughly +0.1 percent (long)
    to +0.9 percent (short at a generous P down of 0.55) before ~0.3-0.5 percent
    round-trip costs, i.e. net EV inside the ~0 plus or minus 0.4 percent noise
    band either direction. An unhedged directional expression carries a ~45x
    adverse-tail-to-edge ratio versus the 7-8x no-trade threshold; a defined-risk
    call debit spread rescales rather than repairs EV.
  direction: none
  confidence: 18
plan:
  ticker: SHAK
  action: no_trade
  entry: 'None. Revisit only if all of: (1) a verified real options quote shows
    straddle width 6 percent or less; (2) P(up) 0.62 or higher justified by a
    named traffic-led datum (e.g. Placer.ai or Black Box Intelligence showing
    SHAK traffic outperforming category by more than 200bps); (3) resolved
    traffic-vs-pricing decomposition confirming any expected beat is
    traffic-driven not menu-price-driven. Alternatively a structure swap to
    trade post-print drift instead of the binary event is a different trade.'
  exit: 'N/A, no position. Any future entry must show modeled net EV outside the
    ~0 plus or minus 0.4 percent band after costs, and an adverse-tail-to-edge
    ratio below the 7-8x threshold. Binary-event window closes at the Aug 5
    print.'
  expected_profit_pct: 0.0
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  confidence: 73
  dissent: 'Bear (Round 2, unresolved): the kitchen-sink thesis assumes a single
    complete reset. Casual-dining margin cascades (a second guide-down within
    1-2 quarters) are common when the first cut does not fully reset the bar.
    If Q2 commentary shows further margin pressure into Q3/Q4, the priced-in
    thesis breaks retroactively, and this narrative risk is not hedged by a
    defined-risk options structure. Quant partial counter: the cascade branch
    is already embedded in the 50-55 percent base rate; flipping the prior to
    P(up)=0.47 merely flips EV sign with identical thinness, reinforcing
    NO TRADE rather than supporting a short. Open for post-mortem: whether the
    base rate genuinely priced the cascade branch or whether that was an
    untested assertion.'
  last_updated: '2026-07-26T02:02:06Z'
---

## Scouted 2026-07-23T16:29:19Z

## Researched 2026-07-26T02:02:06Z

Three-round panel (bull/bear/quant) converged unanimously on NO TRADE. Verified
anchor price SHAK = USD 57.24 at 2026-07-24T17:00Z (twelvedata, resolved cleanly,
no rate-limit issue). Directional EV in both directions is thin (~0 plus or minus
0.4 percent after costs) against an assumed ~9 percent implied move and ~50-55
percent base rate skew, and an unhedged directional expression carries a ~45x
adverse-tail-to-edge ratio versus the 7-8x no-trade threshold — a defined-risk
call debit spread rescales the payoff but does not repair the EV once
transaction costs are included. Full transcript: transcript.md.
