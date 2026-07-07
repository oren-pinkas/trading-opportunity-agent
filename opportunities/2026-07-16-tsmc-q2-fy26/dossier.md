---
id: 2026-07-16-tsmc-q2-fy26
title: TSMC Q2 FY26 earnings
status: researched
created: '2026-07-07T05:39:26Z'
event:
  type: earnings
  summary: Taiwan Semiconductor reports Q2 on Jul 16; AI-demand guidance read-through
    for NVDA/AI supply chain
  impact_window: '2026-07-16'
tickers:
- TSM
- NVDA
sources:
- title: TSMC Q2 2026 Earnings Conference
  url: https://investor.tsmc.com/english/quarterly-results/teleconference
  accessed_at: '2026-07-07T05:39:26Z'
hypothesis:
  statement: 'TSMC Q2 FY26 fundamental bias is a beat-and-raise (long), but the entire
    edge lands in the un-capturable overnight ADR gap that closes before the 13:30Z
    US cash open; only ~0.8-1.5% of directionless intraday drift is in-session tradeable,
    netting ~0-0.2% EV after costs - an order of magnitude below the 2% threshold,
    with a ~7-15x adverse-tail-to-edge ratio and no options hedge available. NO-TRADE.'
  direction: long
  confidence: 34
plan:
  ticker: TSM
  action: buy
  entry:
    time: '2026-07-16T13:46:00Z'
    target_price: 474.45
  exit:
    time: '2026-07-16T19:58:00Z'
    target_price: 474.45
  expected_profit_pct: 0
  note: 'NO-TRADE (panel consensus). Only executable expression is a conditional de-minimis
    TSM long gated on a green opening tape (target +1.5%), which nets ~0% EV after
    costs and fails the no-trade filter. Deliberately left at status researched (not
    scheduled) so simulate-plans does not fill it. NVDA leg rejected as second-derivative
    noise.'
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-07T23:40:00Z'
---

## Scouted 2026-07-07T05:39:26Z

## Researched 2026-07-07T23:40:00Z

**Verdict: NO-TRADE** (three-round-panel; bull sonnet, bear sonnet, quant opus, synthesizer opus).

The panel converged on no-trade. Fundamental bias is genuinely long — TSMC beat-and-raise
remains the base case, AI/HPC demand capacity-constrained (CoWoS packaging, N2 ramp). But
TSMC reports before the US open (Taiwan morning), so the ADR gaps overnight to the print
and ~70-85% of the ~4-6% earnings-day move is realized before the 13:30Z US cash open —
un-capturable under equity-only, in-session fill constraints. What remains is ~0.8-1.5% of
near-directionless intraday drift at a ~52-56% continuation hit rate. Every EV path (blind
or confirmation-gated) nets ~0.0% to +0.2% after costs — an order of magnitude below the 2%
threshold, against a ~7-15x adverse-tail-to-edge ratio with no options hedge to define the
tail. Textbook no-trade filter. NVDA rejected as a strictly worse second-derivative vehicle.

- Bull folded 58 -> 40 (conceded the +4-6% target double-counted the un-capturable gap).
- Bear hardened to 78 no-trade conviction (identified the bull's double-count).
- Quant held no-trade, ~66 conviction (conditioned EV still -0.03% to +0.19%).

**Dissent:** the bull's contention that a same-day in-session catalyst (sell-side PT-revision
cascade or NVDA sympathy momentum with volume confirmation by ~13:45Z) could widen the
capturable fraction enough to matter — unresolvable without live tape.

Full debate with citations: [transcript.md](transcript.md).
