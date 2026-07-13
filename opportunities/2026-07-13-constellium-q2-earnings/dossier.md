---
id: 2026-07-13-constellium-q2-earnings
title: Constellium Q2 2026 earnings
status: researched
created: '2026-07-13T20:42:00Z'
event:
  type: earnings
  summary: Constellium reports Q2 2026 results ~July 28-29; aluminum products demand
    and tariff cost pass-through read
  impact_window: '2026-07-29'
tickers:
- CSTM
sources:
- title: Constellium Q2 2026 Earnings Report
  url: https://www.marketbeat.com/earnings/reports/2026-7-28-constellium-se-stock/
  accessed_at: '2026-07-13T20:42:00Z'
hypothesis:
  statement: 'CSTM enters its ~2026-07-28/29 Q2 print with genuinely strong fundamentals
    (two consecutive beat-and-raise quarters, FY26 EBITDA guide raised to $900-940M,
    2.2x leverage) but no exploitable directional edge, because the two structural
    tailwinds behind the historical earnings-day base rate -- a rising LME metal
    price and a shortage-driven pricing/allocation regime -- are both reversing
    inside this exact reporting window. Q1 EBITDA included a ~$97M non-cash
    metal-price-lag benefit that flips toward a headwind after aluminum''s 16% June
    drop; the Novelis Oswego restart (2026-06-10) begins normalizing the NA
    auto-sheet shortage; and the 2026-06-01 Section 232 change (duty on full
    customs value, US-content threshold 95% to 85%) complicates pass-through. The
    quant''s own EV model, rebuilt to take these mechanisms seriously, flips from
    Round 1''s positive read to EV(long) ~= -1.2% net at a coin-flip P(up)=0.50
    with a widened -8% downside. The bull''s best counters (Novelis'' 4-6 month
    ramp, the CEO''s "very minor impact" tariff comment, LME''s partial rebound to
    ~$3,200/t) are real and were visible to the quant in synthesis, yet did not
    restore positive long EV. EV(short) is only nominally positive (~+0.8% net)
    and rests on an unverified downside-skew assumption -- not a basis to
    initiate short risk either.'
  direction: no-trade
  confidence: 70
plan:
  ticker: CSTM
  action: no-trade
  rationale: 'Two of three personas (bear, quant) independently converged on
    NO-TRADE/cautious before seeing each other''s reasoning. The quant''s EV
    model, once it incorporated the bear''s three dated Q2-specific mechanisms
    (metal-price-lag reversal, Novelis Oswego shortage normalization, Section 232
    customs-value expansion), flipped from +0.76-1.0% net EV (Round 1) to -1.2%
    net EV for a long (Round 2). The symmetric case leaves short EV only
    marginally positive (+0.8% net) and built entirely on an unverified
    downside-skew assumption -- no options-implied-move data, zero historical
    down-move data points in the sample. Per the LEVI lesson (2026-07-12): when
    the highest-confidence panelist finds no clean positive-EV directional edge,
    log NO TRADE rather than manufacture a minimal directional position for the
    learning loop.'
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
  dissent: 'The strongest unresolved disagreement is the timing of the two
    structural reversals versus the Q2 reporting window. The bull''s Novelis-ramp
    argument (restart-to-full-requalified-capacity runs 4-6 months, so the NA
    sheet shortage and its pricing power plausibly persist through Q2 and into
    Q3) is a direct, evidence-backed challenge to the bear/quant premise that the
    shortage is normalizing within this exact window. If the bull is right on
    timing, Q2 could still print as a third clean beat-and-raise with the
    tailwind intact. The synthesis resolved against the bull only because the
    quant already had this counter-evidence in view and it did not restore
    positive long EV, and because "quality of the beat" is a distinct
    re-rating-down risk even on a headline beat. Post-mortem should check whether
    the shortage tailwind was in fact still live in Q2, and whether LME''s July
    rebound (to ~$3,200/t from the $3,146 trough) held or reversed by the print
    date.'
  last_updated: '2026-07-13T23:20:00Z'
---

## Scouted 2026-07-13T20:42:00Z

## Researched 2026-07-13T23:20:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real price
$28.84 (close 2026-07-13, NOT the stub). All three personas independently
researched CSTM's Q2 2026 setup, then rebutted each other. The BULL argued a
defined-risk LONG (call vertical): two beat-and-raise quarters, tariff tailwind
reaffirmed by management, and a ~19% pullback into the print that worked off
"priced for perfection" risk (confidence 60 -> 64). The BEAR held NO-TRADE / small
defined-risk short bias: three dated, quantifiable Q2-specific risks land in the
same 90-day window -- a metal-price-lag reversal (LME aluminum -16% in June), the
Novelis Oswego restart normalizing the NA auto-sheet shortage that gave CSTM
pricing power, and a June 1 Section 232 customs-value expansion complicating
tariff pass-through -- plus two sell-side downgrades right before the print
(confidence 48 -> 52). The QUANT started NO-TRADE on thin positive EV (+0.76-1.0%
net, confidence 42), then rebuilt its model taking the bear's mechanisms
seriously: P(up) dropped from 0.58 to a coin-flip 0.50, the downside magnitude
widened to -8%, and EV(long) flipped to -1.2% net -- a full reversal (confidence
42 -> 65). Two of three personas converged on NO-TRADE independently; per the
LEVI lesson, the panel logged genuine NO TRADE rather than manufacture a minimal
directional position. Synthesizer confidence 70. Full debate with citations in
`transcript.md`.
