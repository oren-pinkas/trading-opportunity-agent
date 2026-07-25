---
id: 2026-07-23-bouygues-sfr-telecom-consolidation
title: Bouygues, Iliad, Orange carve up SFR in French telecom consolidation
status: researched
created: '2026-07-23T19:57:39Z'
event:
  type: regulatory
  summary: Bouygues is set to acquire roughly 52% of SFR's carved-out assets, with
    Iliad taking 27% and Orange 21%, in one of the biggest recent European telecom
    deals; regulatory approval is the key forward catalyst for Bouygues and Orange.
  impact_window: '2026-12-31'
tickers:
- BOUYY
- ORAN
sources:
- title: 'TeleGeography: M&A Monthly: June/July 2026'
  url: https://resources.telegeography.com/mergers-acquisitions-june-july-2026
  accessed_at: '2026-07-23T19:57:39Z'
hypothesis:
  statement: The Bouygues/Iliad/Orange carve-up of SFR is real and already priced;
    the only residual edge is regulatory-approval timing, and the modal outcome
    (60-65 percent) is that the deal is still pending EC/ADLC Phase 2 review at
    2026-12-31, making the stated impact window a non-event. Even if the
    directional call were right, the instruments are untradeable - ORAN returns
    HTTP 404 from the price provider at every date tried, and BOUYY is a
    near-dark ADR (14-21 bars per session, ~5-8k shares, volume-zero minutes)
    with 60-100bps round-trip spread. Net EV after slippage/carry is roughly
    -1.2 to -1.3 percent; SNR is about 0.02 versus a ~0.15 durability floor.
  direction: none
  confidence: 12
plan:
  ticker: BOUYY
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
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
  dissent: "Bull's unresolved residual - a Phase 2 announcement itself may be an
    undersized tradeable volatility event, distinct from the deal-outcome trade
    the panel priced. All three personas modeled directional drift into the fixed
    window; none modeled headline-day vol expansion on the regulatory-decision
    date itself. The two knockouts (regulatory timing, market microstructure) are
    not symmetric against this variant - the timing knockout does not bind an
    event-triggered clip, but ORAN remains unpriceable regardless and BOUYY
    spreads should widen further on a headline day. Post-mortem test: if a Phase
    2 or clearance headline lands before 2026-12-31, record BOUYY's realized
    1-day move and observed spread, and check whether a same-day clip would have
    cleared costs."
  last_updated: '2026-07-25T05:22:07Z'
---

## Scouted 2026-07-23T19:57:39Z

## Researched 2026-07-25T05:22:07Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation
on this opportunity only. Deal terms (Bouygues 52%/Iliad 27%/Orange 21% of SFR carve-up)
have been public since June/July 2026 and are already priced; the only un-priced variable
is regulatory approval timing. Quant's base rates put P(clean approval by 2026-12-31)
at ~12 percent and P(approval with remedies) at ~20 percent, versus ~60-65 percent for
"still pending Phase II" - the modal outcome, consistent with precedent for 4-to-3 EU
mobile consolidations (Hutchison/Three UK, Telenor/TeliaSonera Denmark, Orange/MasMovil-
Vodafone Spain), which typically run 5-18+ months in Phase 2. Separately and
independently disqualifying: `toa price ORAN --provider twelvedata` returned HTTP 404
on every date tried (ORAN is not priceable by the real provider), and BOUYY is a
near-dark ADR with 60-100bps realistic round-trip spread, making the net EV negative
(~-1.2 to -1.3 percent) even before weighing the regulatory-timing risk. SNR ~0.02 is
roughly 7x below the ~0.15 durability floor. The bull conceded both the timeline
argument and the microstructure dealbreaker over Round 2, withdrawing the ORAN hedge
and the standing BOUYY position. Verdict: NO-TRADE (not scheduled, not simulated).
Full debate with citations in `transcript.md`.
