---
id: 2026-07-23-iliad-altice-france-merger-review
title: EU refers Iliad-Altice France asset carve-up to French regulator
status: researched
created: '2026-07-23T12:27:01Z'
event:
  type: regulatory
  summary: European Commission referred antitrust review of Iliad's acquisition of
    Altice France (SFR) telecom assets to France's competition authority on 2026-07-17;
    Bouygues takes 52%, Iliad 27%, Orange 21% of carved-out revenue
  impact_window: '2026-09-30'
tickers:
- ILD
- BOUY
sources:
- title: SatNews
  url: https://satnews.com/2026/07/18/european-commission-defers-iliad-altice-telecom-merger-review-to-french-watchdog/
  accessed_at: '2026-07-23T12:27:01Z'
hypothesis:
  statement: 'UNTRADEABLE AT THE DATA LAYER, independent of directional merit. Even
    granting the Bull''s read that the EU-to-France referral is procedural de-risking
    for a pre-negotiated 52/27/21 carve-up, the expected move is inside transaction
    costs (Quant: gross EV ~+0.15% on BOUY, negative net of ~0.20-0.30% round-trip
    costs; signal-to-noise ~0.01, two orders of magnitude below the ~0.15 durability
    floor). Decisively, neither leg can be priced: toa price (twelvedata) returns
    HTTP 404 for every symbol form tried (ILD, BOUY, BOUY.PA, ILD.PA, EN.PA), a structural
    Euronext Paris coverage gap (same class as the known NSE gap), independently
    re-verified by the orchestrator. ILD is additionally not a live listed equity
    (Iliad went private in 2021).'
  direction: none
  confidence: 3
plan:
  ticker: BOUY
  action: no-trade
  entry:
    time: '2026-09-29T07:00:00Z'
    target_price: null
  exit:
    time: '2026-09-30T15:30:00Z'
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
  dissent: 'Panel converged on the action (no-trade) but never resolved the substance.
    Bull: the referral is genuine procedural de-risking and BOUY (52% carve-up share)
    is the correct vehicle for a re-rating. Bear: the referral is a week-stale, low-information
    procedural handoff and the 52/27/21 split is only proposed, subject to regulatory
    renegotiation; signal-to-noise on a minority carve-out stake inside two conglomerates
    is hopeless regardless of direction. Quant''s base rate (~15-20% of such referrals
    produce a >2% move; this one arrives pre-remedied, lowering surprise) leans toward
    Bear but does not adjudicate the mechanism. If Euronext Paris coverage is ever
    added before 2026-09-30, re-litigate Bull''s re-rating mechanism vs. Bear''s stale-news/S-N
    objection.'
  last_updated: '2026-07-25T13:35:00Z'
---

## Scouted 2026-07-23T12:27:01Z

## Researched 2026-07-25T13:35:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Quant test-queried
`toa price` (twelvedata) for ILD, BOUY, BOUY.PA, ILD.PA, and EN.PA — all returned HTTP
404, a structural Euronext Paris coverage gap (same class as the documented NSE gap),
independently re-verified by the orchestrator. ILD is additionally not a live listed
equity (Iliad went private in 2021). All three personas converged on PASS/no-trade:
even setting the pricing gap aside, the qualitative edge was already inside transaction
costs (gross EV ~+0.15% on BOUY, negative net; S/N ~0.01 vs. a ~0.15 durability floor).
Marked untradeable at the data layer, independent of directional merit. Full debate
with citations in `transcript.md`.
