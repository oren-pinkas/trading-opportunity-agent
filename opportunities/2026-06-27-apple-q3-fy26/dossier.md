---
id: 2026-06-27-apple-q3-fy26
title: Apple Q3 FY2026 earnings (report July 30 AMC)
status: researched
created: '2026-06-27T11:00:05Z'
event:
  type: earnings
  summary: Apple reports fiscal Q3 after close July 30 amid recent hardware price
    hikes and demand reassessment; Cook's final call before Ternus CEO transition.
  impact_window: '2026-07-30'
tickers:
- AAPL
sources:
- title: Apple Inc (AAPL) Earnings Dates - TipRanks
  url: https://www.tipranks.com/stocks/aapl/earnings
  accessed_at: '2026-06-27T11:00:05Z'
hypothesis:
  statement: >-
    Apple's Q3 FY26 print is a near-symmetric event on a 50/50 directional base
    rate (recent 8 prints split 4 up / 4 down), where the options market implies a
    ~3.5-4% move against a realized ~2.4-2.6% average — making long-volatility
    negative-EV after IV crush and the directional overnight-gap EV roughly -0.15%
    after slippage. The bull's conditional edge (a +6.97% upward estimate-revision
    tape plus the non-recurring Cook->Ternus CEO handoff) and the bear's conditional
    short (China iPhone shipments -19% YoY in May, a Q4-guidance/margin setup) are
    both real but each only nudges a coin-flip; neither breaks the symmetry enough
    to clear the implied-move premium. With no live implied move <2.0% in hand and
    no hard guidance signal today, the calibrated call is to stand aside.
  direction: none
  confidence: 20
plan:
  ticker: AAPL
  action: no-trade
  entry:
    time: '2026-07-30T19:50:00Z'
    target_price: null
  exit:
    time: '2026-07-31T13:45:00Z'
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
    Whether the +6.97% upward estimate-revision tape and the one-time Ternus/Cook
    handoff constitute genuine conditional directional skew (bull) or are already
    absorbed into a 50/50 event the quant's symmetric EV model treats as noise
    (quant). The bull argues post-earnings drift from rising revisions plus a
    non-recurring catalyst is structurally invisible to a base-rate model; the quant
    counters any such edge is dwarfed by the ~3.5-4% implied-move premium and stays
    unconfirmed until the live implied move prints <2.0%. Testable post-mortem: did
    AAPL gap directionally with the revision tape, or land inside the implied move?
  last_updated: '2026-06-27T12:20:00Z'
---

## Scouted 2026-06-27T11:00:05Z

## Researched 2026-06-27T12:20:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Apple reports
fiscal Q3 FY2026 AMC Thursday 2026-07-30; the tradable move is the overnight gap, so
the structurally valid plan is enter ~19:50Z 7/30 (before the print), exit ~13:45Z
7/31 (after the open gap settles). The QUANT's EV calibration was decisive: realized
1-day move averages ~2.4-2.6% while options imply ~3.5-4% (long-vol is negative-EV via
IV crush), and the recent 8 prints split 4 up / 4 down — a coin-flip with directional
gap EV ≈ -0.15% after slippage. The BULL conceded its +5-8% target was a ~2σ tail and
narrowed to a thin, conditional low-vega long; the BEAR conceded the -12% pullback
removed downside fuel and moved toward "SKIP unless China/margin deteriorate." Verdict:
NO-TRADE (not scheduled, not simulated). Flips only on a live implied move <2.0%
(long-vol) or a hard guidance break. Full debate with citations in `transcript.md`.
