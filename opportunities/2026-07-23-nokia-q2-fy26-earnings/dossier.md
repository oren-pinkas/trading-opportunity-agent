---
id: 2026-07-23-nokia-q2-fy26-earnings
title: Nokia Q2/H1 FY26 earnings
status: researched
created: '2026-07-22T08:05:47Z'
event:
  type: earnings
  summary: Nokia reports Q2 and half-year 2026 results Thursday July 23, with optical/networking
    chip demand in focus.
  impact_window: '2026-07-23'
tickers:
- NOK
sources:
- title: TipRanks - Nokia Earnings Dates
  url: https://www.tipranks.com/stocks/nok/earnings
  accessed_at: '2026-07-22T08:05:47Z'
hypothesis:
  statement: "Nokia's Q2 FY26 print was fundamentally positive (EPS beat, sales beat,
    Optical Networks +20% YoY cc, AI & Cloud +103% YoY on EUR 2.8B orders, gross
    margin +70bps, FY26 guidance raised), but the two-day -11.5% selloff (USD 10.28
    to USD 9.10) reflects genuinely new negative information -- a EUR 800M
    restructuring charge (~3x prior estimate) that pushed reported operating margin
    to -1.0% and FCF deeply negative, plus a CEO warning that memory supply
    constraints persist through 2027 -- not a sentiment overreaction. PEAD base
    rates favor continuation in the direction of the abnormal return (down), but
    break-even for a long needs P(up) >= 0.395 against an estimated 0.355, and even
    on the bullish case the signal-to-noise ratio (~0.07 vs ~3.5% daily vol) is
    roughly half the ~0.15 tradeable floor. A short carries an un-hedgeable
    gap-up tail (raised guidance, 11 Buy ratings, USD 15.10 consensus target) at
    roughly 90x adverse-tail-to-edge versus a 7-8x reject line. The position is
    also unverifiable end to end: the twelvedata price provider returned HTTP 429
    (account-level quota exhaustion, confirmed via a control ticker) on every
    attempt, so no entry/exit price can be confirmed fillable, and this harness
    cannot enforce a protective stop even if one were proposed."
  direction: none
  confidence: 76
plan:
  ticker: NOK
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  rationale: "Three independent disqualifiers, any one sufficient: (1) unpriceable
    -- provider quota exhausted, no verified quote available; (2) sub-threshold
    signal-to-noise (~0.07 vs a ~0.15 floor) even granting the bull case's own
    price target; (3) the only directionally favored side (short) carries a
    roughly 90x adverse-tail-to-edge ratio versus a 7-8x reject line, and a long's
    stop is unenforceable in this harness."
research:
  last_updated: '2026-07-25T19:38:54Z'
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: "Strongest unresolved disagreement: whether the -11.5% two-day selloff
    is a durable repricing or an overreaction to one CEO remark. Bull's claim that
    the initial +6.9% pop showed an incrementally positive read, that the reversal
    tracked one memory-supply comment rather than a re-rating of the AI/optical
    thesis, and that zero analysts cut estimates or targets post-print, went
    unrefuted -- Quant's rebuttal reused the same 2-day PEAD framework rather than
    engaging the multi-week horizon Bull was actually arguing. Separately, Bear's
    Round 2 concession that the EUR 800M reveal is fresh negative information (not
    just high expectations already priced in) implies a real down-signal that is
    merely unmonetizable -- a different epistemic claim from Quant's 'no edge
    exists either way' (26/100). If Bear is right, the correct lesson is
    instrument design (defined-risk structure, longer horizon), not signal
    absence. This is the 5th logged instance of the twelvedata data layer gating
    a decision end-to-end; an account-level quota/freshness pre-flight check is
    warranted before spending debate budget on an unpriceable opportunity."
  transcript: transcript.md
---

## Scouted 2026-07-22T08:05:47Z

## Researched 2026-07-25T19:38:54Z

NO-TRADE. Three-round panel (bull/bear/quant) converged on caution: the print was
fundamentally strong (EPS and sales beat, AI & Cloud +103% YoY, guidance raised)
but the market's -11.5% two-day reaction reflects a genuinely new EUR 800M
restructuring charge (~3x prior estimate) and a multi-year memory-supply warning,
not simple overreaction. Neither direction clears a tradeable bar: the long fails
on signal-to-noise (~0.07 vs a ~0.15 floor) even under the bull's own price
target, and the short fails on an un-hedgeable gap-up tail (~90x
adverse-tail-to-edge vs a 7-8x reject line) into raised guidance and 11 Buy
ratings. The position could not be independently verified as fillable: the
twelvedata price provider returned HTTP 429 (account-level quota exhaustion,
confirmed against a control ticker) on every attempt across both research
rounds. Full transcript: `transcript.md`.
