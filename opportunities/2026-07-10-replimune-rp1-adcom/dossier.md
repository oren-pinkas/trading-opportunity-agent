---
id: 2026-07-10-replimune-rp1-adcom
title: Replimune FDA Advisory Committee for RP1 melanoma BLA
status: researched
created: '2026-07-10T07:38:15Z'
event:
  type: regulatory
  summary: FDA Cellular, Tissue and Gene Therapies AdCom meets July 30, 2026 on Replimune's
    BLA for RP1 (vusolimogene oderparepvec) plus nivolumab in advanced melanoma.
  impact_window: '2026-07-30'
tickers:
- REPL
sources:
- title: Cellular, Tissue, and Gene Therapies Advisory Committee - Replimune, Inc.
  url: https://www.federalregister.gov/documents/2026/07/08/2026-13810/cellular-tissue-and-gene-therapies-advisory-committee-notice-of-meeting-establishment-of-a-public
  accessed_at: '2026-07-10T07:38:15Z'
hypothesis:
  statement: >-
    The panel converged on a documented bearish lean but no executable naked-stock
    position: two prior CRLs on the identical single-arm/heterogeneity defect, a
    "minor" Class 1 resubmission with no new pivotal trial, and the market's own
    bearish read of the June 26 AdCom-convening (REPL fell premarket on the
    announcement) put P(negative vote) around 0.60-0.62 per the bear's revised case.
    Yet the only nominally positive-EV stock position (a naked short) has its entire
    edge riding on an unverified squeeze-tail assumption — it flips to roughly flat
    to negative if the up-move is a ~120% squeeze rather than the assumed ~75%, and
    no short-interest, borrow-rate, or options-implied-move data exists to price that
    tail. The single fact that would resolve the standoff — the AdCom voting-question
    framing (adequacy-of-evidence vs. benefit-risk/unmet-need) — is not yet public,
    and the stub price feed (~40-60x off the real ~$10 tape, ±60-90% adjacent swings)
    cannot support responsible entry/stop sizing. All three personas preferred a
    defined-risk options structure this plan schema cannot express.
  direction: none
  confidence: 58
plan:
  ticker: REPL
  action: no-trade
  entry:
    time: '2026-07-29T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-30T20:00:00Z'
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
  dissent: "The strongest unresolved disagreement is the AdCom voting-question framing
    fork, tightly coupled to the short-side microstructure data gap. If FDA frames the
    vote around adequacy of evidence, the twice-cited structural defect dominates and
    P(negative) rises toward ~0.70 (bear/short case). If framed around benefit-risk in
    an unmet-need population with zero approved alternatives, the durable-response
    data (CR 15%, DOR ~21-28mo, 3yr OS 47.8%) becomes the decision axis and
    P(negative) falls toward ~0.45 (bull case) — both bull and bear explicitly agreed
    they would flip sides on this single, not-yet-public fact. Separately, even
    granting the bear's P(negative)~0.62, the quant showed the short's entire edge is
    an artifact of an assumed +75% up-tail; without short-interest, borrow-rate, or
    options-implied-move data, the short cannot be responsibly priced. Post-mortem
    test: did the FDA briefing frame the question as adequacy or benefit-risk, and did
    REPL's realized move match the assumed +/-55-75% or blow through it as a squeeze?"
  last_updated: '2026-07-12T13:40:00Z'
---

## Scouted 2026-07-10T07:38:15Z

## Researched 2026-07-12T13:40:00Z — NO-TRADE (documented short lean)

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation
on this opportunity only. REPL's RP1+nivolumab has already taken two CRLs
(2025-07-22, 2026-04-10) on the identical IGNYTE single-arm/heterogeneity objection;
the current resubmission is a Class 1 (minor) response with no new pivotal trial, and
the market read the 2026-06-26 AdCom-convening itself as bearish (REPL fell
premarket). The bear pushed P(negative vote) to ~0.60-0.65; under those probabilities
the quant's EV table flips a naked short to nominally +10.65% net — but that entire
edge is an artifact of an unverified ~75% up-tail assumption, collapsing to
flat-to-negative (~-0.6%) if a squeeze produces ~+120% instead (no short-interest /
borrow / options-implied-move data available to resolve this). All three personas
independently preferred a defined-risk options structure (calls, puts, or a
put-spread) over any naked stock position — a structure this plan schema cannot
express — and the price feed is ~40-60x off the real tape and internally incoherent,
blocking responsible entry/stop sizing regardless. Verdict: NO-TRADE, direction none,
confidence 58/100, with the bearish lean and its blocking conditions documented for
the post-mortem. Full debate with citations in `transcript.md`.
