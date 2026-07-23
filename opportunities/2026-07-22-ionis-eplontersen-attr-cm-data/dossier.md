---
id: 2026-07-22-ionis-eplontersen-attr-cm-data
title: Ionis/AstraZeneca eplontersen ATTR-CM Phase 3 data at conference
status: researched
created: '2026-07-22T12:26:30Z'
event:
  type: earnings
  summary: Ionis and AstraZeneca's eplontersen (Wainua) ATTR-CM cardiomyopathy Phase
    3 data set for conference presentation Aug 31 2026, after missing the primary
    composite endpoint in an earlier readout
  impact_window: '2026-08-31'
tickers:
- IONS
- AZN
sources:
- title: Biotech Catalyst Calendar 2026 — FDA PDUFA Dates & Readouts
  url: https://www.biotech-edge.com/catalysts
  accessed_at: '2026-07-22T12:26:30Z'
hypothesis:
  statement: >-
    The 2026-08-31 event is a re-presentation of an already-known Phase 3 primary
    composite-endpoint miss for eplontersen (Wainua) in ATTR-CM, adding only
    descriptive texture (secondary/subgroup detail) rather than new topline
    information. EV math shows a gross catalyst edge of only ~+15bp against a ~20:1
    adverse-tail-to-edge ratio, and a 5-week holding period whose beta/drift variance
    swamps any catalyst edge, so there is no exploitable directional edge in IONS or
    AZN. The sole low-tier source (biotech-edge.com) leaves a gating fork
    unresolved -- re-presentation vs first-disclosure -- that caps confidence rather
    than justifying a speculative position.
  direction: none
  confidence: 15
plan:
  ticker: IONS
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
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
    The single low-tier source (biotech-edge.com) leaves the event-type fork
    unresolved: all three personas assumed re-presentation of a known miss, but the
    quant flagged that if 08-31 is instead the FIRST disclosure of the data, the
    setup flips from a muted ~15bp non-event into a genuine binary catalyst, which
    would invalidate the no-trade conclusion entirely. A secondary, unresolved
    distribution-shape disagreement: the bull maintained the +/-3% symmetric EV
    assumption may understate the right tail if expectations are anchored
    abnormally low, whereas quant/bear treated the symmetric muted-move
    distribution as adequate. Neither is resolvable without tier-1 confirmation of
    event type, verified price reaction to the original miss, miss
    magnitude/nature, and competitive context (Alnylam vutrisiran, Pfizer
    tafamidis).
  last_updated: '2026-07-23T17:35:17Z'
---

## Scouted 2026-07-22T12:26:30Z

## Researched 2026-07-23T17:35:17Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas independently opened near no-trade/token-position and fully converged by
Round 2. The QUANT's EV calibration was decisive: this is a data-detail
presentation of an ALREADY-FAILED primary composite endpoint, not a fresh binary --
the market-moving event already fired at the earlier readout. EV on IONS: P(positive
detail)=0.25 (+3%), P(non-event)=0.55 (0%), P(negative detail)=0.20 (-3%) =>
EV_gross = +0.15%, inside costs/noise, further diluted by 5 weeks of unrelated
beta/drift over the 07-23 -> 08-31 hold. The BULL conceded its "priced in" and
"spotlight = bullish signal" reasoning was under-evidenced (no verified 52-week
price history, no data on how the stock reacted to the original miss) and moved off
its proposed call-spread toward no-trade. The BEAR concurred and pushed confidence
in no-trade toward ~90 given the unresolved source-quality gate. Verdict: NO-TRADE
(not scheduled, not simulated). AZN was dead on arrival for either persona given its
size/diversification. Flips only on tier-1 confirmation that 08-31 is a first
disclosure (not re-presentation) or verified evidence the original miss produced a
large, un-recovered drawdown. Full debate with citations in `transcript.md`.
