---
id: 2026-07-13-lululemon-guidance-cut
title: Lululemon slashes FY2026 sales and EPS guidance
status: researched
created: '2026-07-13T18:24:37Z'
event:
  type: earnings
  summary: Lululemon cut FY2026 sales guidance to .0-11.15B (from .35-11.50B) and
    EPS to .95-11.15 (from .10-12.30), citing weak demand and misfired launches; next
    print will test the reset.
  impact_window: '2026-09-05'
tickers:
- LULU
sources:
- title: Lululemon (LULU) earnings Q1 2026
  url: https://www.cnbc.com/2026/06/04/lululemon-lulu-earnings-q1-2026.html
  accessed_at: '2026-07-13T18:24:37Z'
hypothesis:
  statement: >-
    The FY2026 guidance cut is a stale, fully public catalyst with no remaining
    information edge. The disproportionate EPS-vs-sales haircut (~9% vs ~4%)
    signals real margin compression, but that news is already reflected in the
    reset $120.70 spot. Directional expected value over the post-print window
    (to the 2026-09-05 print) is roughly flat-to-slightly-negative (~-0.1%), and
    the adverse-tail-to-edge ratio (~12% downside tail vs <1% net edge) sits well
    past a tradable threshold. Neither the bull's relief-rally case nor the
    bear's continued-deterioration case produced quantifiable evidence of
    mispricing; both conceded to no-trade in rebuttal.
  direction: none
  confidence: 38
plan:
  ticker: LULU
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
    The strongest unresolved disagreement is the unconfirmed short-volatility
    hypothesis raised by the quant: the only theoretically defensible edge is
    non-directional (selling elevated pre-print IV via an iron condor/short
    strangle against the now-reset, lowered bar), never tested because no actual
    IV/skew data was pulled. Secondary dissent: the bear's negative-skew concern
    that continued promotional markdowns could underweight the modeled
    P(down>8%)=25% tail, which the bear admitted isn't quantifiable without more
    data. Testable post-mortem: pull LULU IV/skew before the 09-05 print to
    confirm or kill the short-vol thesis, and check whether the actual move
    exceeds the modeled ~12% downside tail.
  last_updated: '2026-07-13T18:50:00Z'
---

## Scouted 2026-07-13T18:24:37Z

## Researched 2026-07-13T18:50:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), judged strictly
on LULU's own merits. The guidance cut (FY26 sales to $10.85-11.15B from
$11.35-11.50B; EPS to $10.95-11.15 from $12.10-12.30) is real but already public and
priced into the $120.695 spot (2026-07-13T18:35Z, twelvedata). QUANT's EV math was
decisive: net directional EV ≈ -0.1% into the 2026-09-05 print, with an adverse-tail-
to-edge ratio (~12% downside vs <1% edge) well past the no-trade threshold from the
NKE/DAL lessons. Both BULL (call debit spread, contingent on downside-priced
confirmation) and BEAR (put debit spread, contingent on continued deterioration)
conceded in rebuttal that they had no evidence of mispricing beyond narrative and
dropped their proposals per the LEVI no-manufactured-position lesson. Verdict:
NO-TRADE (not scheduled, not simulated). The only unconfirmed edge worth watching is
short-vol (selling rich pre-print IV) if the surface justifies it — untested here for
lack of IV data. Full debate with citations in `transcript.md`.
