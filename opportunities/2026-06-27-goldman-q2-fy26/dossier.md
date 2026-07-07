---
id: 2026-06-27-goldman-q2-fy26
title: Goldman Sachs Q2 FY2026 earnings (week-one bank season, ~July 15)
status: researched
created: '2026-06-27T11:00:05Z'
event:
  type: earnings
  summary: Goldman reports Q2 mid-July; capital-markets/trading and IB-fee thesis
    distinct from consumer banks, sensitive to 2026 market volatility.
  impact_window: '2026-07-14'
tickers:
- GS
sources:
- title: Earnings Season Calendar 2026 | EarningsNxt
  url: https://www.earningsnxt.ai/insights/earnings-season-calendar-2026
  accessed_at: '2026-06-27T11:00:05Z'
- title: Goldman Sachs (GS) earnings 1Q 2026 — CNBC
  url: https://www.cnbc.com/2026/04/13/goldman-sachs-gs-earnings-1q-2026.html
  accessed_at: '2026-06-27T12:18:00Z'
hypothesis:
  statement: >-
    Unlike the sibling JPMorgan case, the GS open-gap-vs-intraday decomposition is
    NOT a clean disqualifier — GS Q1 2026 (a headline EPS beat) gapped DOWN ~3% at
    the open on the FICC miss disclosed in the press release, so GS's
    capital-markets/FICC-composition story reprices AT the open and IS structurally
    capturable by a gap-hold (whereas JPM's NII-guidance fade lands intraday on the
    call). However, that same Q1 open gap-down then mean-reverted toward flat by the
    close, the open-gap SIGN is driven by an unknowable FICC print, and the
    directional base rate is up 6 of 8. With the quant's directional EV at +0.27%
    (sub-threshold) against a rich ~6.8% earnings-day straddle, the expected harvest
    net of slippage is indistinguishable from zero.
  direction: none
  confidence: 30
plan:
  ticker: GS
  action: no-trade
  entry:
    time: '2026-07-13T19:50:00Z'
    target_price: null
  exit:
    time: '2026-07-14T13:45:00Z'
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
    GS, unlike JPM, demonstrably DOES gap at the open on earnings (Q1 2026 opened
    ~-3% on the FICC miss), so a gap-hold here is mechanically capable of capturing
    the move — the JPM "zero open gap" disqualifier does not transfer. What remains
    unresolved is SIGN and PERSISTENCE: the open gap is driven entirely by the
    unknowable FICC/GBM composition (Q1's beat-and-drop came purely from a ~$910M
    FICC miss), the base rate is up 6 of 8, and Q1's gap-down mean-reverted to flat
    by the close. The quant's pre-condition (FICC consensus set below the Q1
    run-rate, raising P(up)) cannot be evaluated until the live consensus prints.
  last_updated: '2026-06-27T12:20:00Z'
---

## Scouted 2026-06-27T11:00:05Z

## Researched 2026-06-27T12:20:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Research confirmed
GS reports Q2 FY2026 BMO Tuesday 2026-07-14 (impact_window corrected from the scout's
stale 07-15). Structurally valid trade would be a gap-hold: enter ~19:50Z 7/13, exit
~13:45Z 7/14. KEY FINDING vs the sibling JPM NO-TRADE: GS's reaction is NOT a zero-gap
intraday fade — GS Q1 2026 gapped DOWN ~3% at the OPEN on the FICC miss, so the move IS
capturable. But the open-gap SIGN is a coin-flip on the unknowable FICC/GBM composition
(Q1 beat-and-dropped purely on a ~$910M FICC miss), the base rate is up 6 of 8, and the
Q1 gap mean-reverted to flat by the close. The BULL trimmed to a thin +3-5% long-stock
view (conceding the quant's "vol gap" was a category error); the BEAR conceded SKIP as
base case, reserving a short only as a conditional fade on a 2%+ gap-up. QUANT EV ≈
+0.27% (sub-threshold) vs a ~6.8% straddle. Verdict: NO-TRADE. Flips only on a live
straddle <=3.5% or a FICC consensus set below the Q1 run-rate. Full debate in
`transcript.md`.
