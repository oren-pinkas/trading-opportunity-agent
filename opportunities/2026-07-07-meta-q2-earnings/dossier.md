---
id: 2026-07-07-meta-q2-earnings
title: Meta Platforms Q2 2026 earnings
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: earnings
  summary: Meta reports Jul 29; ad revenue and AI capex trajectory are the catalyst.
  impact_window: '2026-07-29'
tickers:
- META
sources:
- title: EarningsWhispers calendar
  url: https://www.earningswhispers.com/calendar
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: >-
    META Q2 2026 earnings offer no positive-expected-value expression under the
    equity-only, options-non-executable simulator: the earnings-gap direction is a
    coin flip (signed 8-qtr avg +1.04%) with a huge ±11.8% average magnitude and an
    un-hedgeable ±26% overnight tail, so any position held through the AMC print is a
    naked gap and every no-trade filter trips. The only edge-positive vehicles
    (defined-risk spread, long straddle exploiting the 63% implied-move beat rate)
    are non-executable, and the pre-print positioning-drift alternative nets to
    roughly zero (~-0.05% to -0.10%) after slippage.
  direction: neutral
  confidence: 72
plan:
  ticker: META
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  rationale: >-
    NO-TRADE. Binding constraint: the simulator fills only US-equity 1-minute bars
    (13:30-19:59Z) and options are non-executable, so no defined-risk earnings
    structure exists. Holding equity through the 2026-07-29 AMC print is a naked
    overnight gap with an un-hedgeable ±26% tail; direction is ~50/50 and naked-long
    EV is ≈-1.0% net (probs 28% up / 38% down / 34% muted). A naked short is
    prohibited and carries the positive-tail squeeze realized twice in the last four
    prints (Q4'25 +10%, Q2'25 +11.3%). The pre-print drift fallback nets ~+0.15%
    gross / ~-0.05% to -0.10% net. All four institutional no-trade filters trip.
research:
  last_updated: '2026-07-07T22:37:55Z'
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
  reference_price:
    ticker: META
    price: 327.31
    at: '2026-07-07T19:59:00Z'
    source: stub:deterministic
  lessons_applied:
  - 2026-06-25-nike-q4-fy26
  - 2026-07-02-tesla-deliveries
  dissent: >-
    The bull's pre-print positioning-drift trade (enter 2026-07-28T13:35Z, flat by
    2026-07-29T19:59Z before the AMC release) is gap-free and equity-executable,
    sidestepping the naked-overnight objection. The synthesis rejects it on the
    quant's PEAD adjudication that single-name pre-print drift is ~50/50 noise
    netting near zero after slippage — but that near-zero EV is an estimate, not a
    demonstrated negative edge. If mega-cap positioning drift into a high-attention
    print is even marginally positive, a small gap-free long was the one defensible
    trade left on the table.
  transcript: transcript.md
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:37:55Z

Three-round panel debate (bull/bear/quant → neutral synthesizer). **Verdict: NO-TRADE
(neutral), confidence 72/100.** The decisive constraint is that this simulator fills
only US-equity 1-minute bars (13:30–19:59Z) with no executable options, so every
defined-risk earnings structure the personas reached for is unavailable. That leaves
only naked equity across the 2026-07-29 AMC print — a coin-flip direction with an
un-hedgeable ±26% overnight tail and ≈-1.0% net EV on the long side, while a naked
short is prohibited. The pre-print positioning-drift fallback nets ~breakeven-negative.
All four institutional no-trade filters trip. See `transcript.md` for the full debate
and citations.
