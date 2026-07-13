---
id: 2026-07-13-jetblue-bankruptcy-risk
title: JetBlue bankruptcy-risk model spikes ahead of Q2 earnings
status: researched
created: '2026-07-13T07:44:04Z'
event:
  type: earnings
  summary: Fitch's CCC+ rating and a ~37% 24-month bankruptcy-probability model intensify
    scrutiny of JetBlue's balance sheet ahead of its July 28 Q2 report.
  impact_window: '2026-07-28'
tickers:
- JBLU
sources:
- title: DeepArrival
  url: https://deeparrival.com/news/jetblue-bankruptcy-risk-ccc-rating/
  accessed_at: '2026-07-13T07:44:04Z'
hypothesis:
  statement: Into JBLU's July 28 2026 Q2 print, the directional edge is genuinely
    two-sided (P(up>10%)=30% vs P(down>10%)=28%; tails 12%/12%), and the one
    structurally-defensible bull idea — defined-risk OTM calls — carries negative
    expected value once priced at realistic event-IV. The bull's "IV-compressed,
    priced for disaster" premise is unsupported into a scheduled binary catalyst,
    and its "high short interest → squeeze" premise was never backed by an actual
    short-interest figure. The two highest-rigor seats (quant, bear) converge on
    avoidance from independent angles.
  direction: none
  confidence: 64
plan:
  ticker: JBLU
  action: no_trade
  reasoning: 'EV is negative on every in-mandate structure (outright long/short
    -2% to -3.2% after frictions/borrow; $6 ~2-week call E[intrinsic]~$0.29 vs
    realistic ask $0.35-0.50 => EV -17% to -31% on premium). The only positive-EV
    structure (straddle) is out of mandate and roughly flat. No entry/exit set;
    stays flat through the July 28 catalyst. Conditional, non-triggered allowance
    logged: if live $6 ~2-week call quotes at <=$0.30, a 25-40bps single-tranche
    long-call lotto (exit T+1 post-print) would flip to allowed.'
research:
  last_updated: '2026-07-13T15:58:00Z'
  dissent: 'Primary: the IV-richness assumption ($0.35-0.50 ask on the $6 ~2wk
    call) was never checked against a live option quote — if actual IV is softer
    (<=$0.30), the bull''s defined-risk lotto flips positive-EV and this verdict
    is wrong. Secondary: the bull''s squeeze thesis was asserted without a JBLU-specific
    short-interest/days-to-cover figure; if July 28 shows squeeze characteristics,
    the symmetric-distribution framing understated the right tail.'
---

## Scouted 2026-07-13T07:44:04Z

## Researched 2026-07-13T15:58:00Z

Three-round debate panel (bull/bear/quant, synthesizer) converged on **NO TRADE**.
Confidence 64. Full transcript: see `transcript.md`. Live price at research time:
JBLU $5.74 (2026-07-13T15:30Z, twelvedata).
