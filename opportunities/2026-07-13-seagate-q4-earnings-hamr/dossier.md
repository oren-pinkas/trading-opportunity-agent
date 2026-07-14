---
id: 2026-07-13-seagate-q4-earnings-hamr
title: Seagate Technology earnings amid HAMR ramp and memory supercycle
status: researched
created: '2026-07-13T15:12:42Z'
event:
  type: earnings
  summary: STX reports July 16; Mozaic HAMR drives qualified across all major cloud
    customers as storage demand rides AI/memory supercycle
  impact_window: '2026-07-16'
tickers:
- STX
sources:
- title: Seagate's 485% Run Isn't Over and Our Target Proves It
  url: https://finance.yahoo.com/markets/stocks/articles/seagate-485-run-isn-t-134506188.html
  accessed_at: '2026-07-13T15:12:42Z'
hypothesis:
  statement: All three personas independently converged on no_trade for the 2026-07-16
    print. The HAMR-qualification catalyst carries approximately zero fresh
    informational edge - it is the narrative that produced the prior 485 percent
    run, not new information the market will learn on the call. Every directional
    structure fails a filter - long shares and long calls are negative EV against a
    negatively-skewed post-print distribution for an extreme-momentum name, median
    analyst target USD 771 sits about 12 percent below the USD 874 spot reference
    (2026-07-13T15:30Z, twelvedata), and trailing PE near 97 to 102x (about 347
    percent above the 10-year average) leaves no valuation room for anything short
    of a blowout. A naked short or short-vol structure is forbidden by the
    adverse-tail-to-edge filter given STX already demonstrated a greater than
    12 percent one-day move on 2026-06-26 on sector-sentiment news alone (SK Hynix
    HBM-capex-slowdown headlines), which the quant used to revise the assumed
    earnings-day implied move up from 10.5 percent to about 14 percent - closing
    the one escape hatch (a long put spread, viable only if implied is at or below
    7 to 8 percent) that existed after round 1.
  direction: no_trade
  confidence: 80
plan:
  ticker: STX
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: No long - EV_long_shares is about -3.5 percent after costs and EV_long_calls
    is below zero because options already price the move rich; the qualification
    narrative is fully subsumed by the prior run and bull's own round-1 confidence
    (42) sat below its own 45 no-trade filter threshold. No naked short or short-vol
    structure (e.g. iron condor) - the adverse-tail-to-edge ratio is 3.5 to 7x and
    STX has demonstrated greater than 12 percent single-day gap capacity, an
    un-hedgeable positive tail. No put spread - EV is at or below zero once implied
    volatility is revised up to about 14 percent using the 2026-06-26 realized-move
    evidence. Reopen only the long put spread, and only if a live option chain shows
    an implied one-day move at or below 7 to 8 percent (never actually pulled in
    this debate - the 14 percent figure is inferred from realized vol, not quoted).
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
  dissent: The strongest still-live disagreement is horizon scope, not print-day
    direction - bear registered an explicit dissent that a medium-term
    overextension/short thesis (about 55/100 confidence, resting on the extreme PE,
    the Fox Advisors Equal-Weight downgrade warning HDD pricing "may be getting
    ahead" of realized increases, and insider selling flagged around 2026-07-02)
    remains live and was never adjudicated - the panel only resolved the 48-hour
    print-day window. Two nested sub-disputes also stayed open - whether the
    bearish median analyst target predates or postdates the HAMR qualification
    news (bull's timing-ambiguity point, never confirmed), and whether quant's
    revised P(gap up)=0.34 is still too generous given the valuation gap (bear's
    contention).
  lessons_applied:
  - "NKE 2026-07-06 - un-hedgeable positive tail with thin net EV is a no-trade
    filter, not a size-down - applied to reject the naked short and any short-vol
    structure."
  - "DAL 2026-07-12 - a catalyst that already drove a large run to a high above the
    Street mean target is priced in, do not re-bet it as a fresh gap trigger -
    applied to the HAMR qualification narrative directly."
  - "LEVI 2026-07-12 - when the quant says directional EV is about zero and the only
    positive-EV structure is out of mandate, log NO TRADE rather than manufacture a
    minimal position - applied to the final synthesis."
  - "LEVI 2026-07-12 - anchor entry prices to a live quote at the actual entry
    timestamp, not a stale pre-move reference - carried forward as the condition
    that would apply if the put-spread reopen trigger is ever met."
  last_updated: '2026-07-14T04:40:21Z'
---

## Scouted 2026-07-13T15:12:42Z

## Researched 2026-07-14T04:40:21Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 80/100
confidence. The HAMR-qualification catalyst is judged to carry near-zero fresh
edge against an already-485-percent run; every long, short, and spread structure
failed an EV or tail-risk filter once bear's valuation data (median target USD 771
vs USD 874 spot, PE about 97-102x) and the 2026-06-26 realized-vol precedent were
weighed in. Bull conceded from 42 to 22/100 confidence; bear and quant converged at
78 and 80/100 respectively. A medium-term overextension thesis from bear
(about 55/100) remains an unadjudicated dissent for the post-mortem record. The one
reopen condition - a live option chain showing implied one-day move at or below
7-8 percent - was never checked in this debate. Full transcript: `transcript.md`.
