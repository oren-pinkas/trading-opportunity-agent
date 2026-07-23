---
id: 2026-07-22-eurobank-q2-earnings
title: Eurobank sets Q2 2026 earnings date amid Greek bank rally
status: researched
created: '2026-07-22T17:49:00Z'
event:
  type: earnings
  summary: Eurobank (EUROB.AT) will release Q2 2026 results on July 30 with a same-day
    conference call, part of a broader European/Greek/Cypriot bank profit upswing
    from higher-for-longer rates, loan growth and trading income.
  impact_window: '2026-07-30'
tickers:
- EUROB.AT
sources:
- title: Eurobank sets date for second quarter earnings announcement - Cyprus Mail
  url: https://cyprus-mail.com/2026/07/22/eurobank-sets-date-for-second-quarter-earnings-announcement
  accessed_at: '2026-07-22T17:49:00Z'
hypothesis:
  statement: Eurobank (EUROB.AT) reports Q2 2026 earnings on 2026-07-30 into a
    sector-wide Greek/Cypriot bank profit upswing, but the only dossier-confirmed
    fact is the earnings date; no directional edge is verifiable without a live
    quote, consensus estimate, or options data.
  direction: none
  confidence: 8
plan:
  status: NO-TRADE
  ticker: EUROB.AT
  action: stand aside (size = 0)
  disqualifying_reasons:
  - "no live price feed for EUROB.AT (TwelveData 404s -- Athens Exchange coverage gap); no verifiable entry or range context"
  - "no options chain available; no defined-risk structure can be constructed -- unexecutable, i.e. undefined EV, not merely poorly priced"
  - "no consensus EPS/NII estimate; 4 of 5 EV inputs missing; modeled slippage (1.5-3% round-trip) exceeds any theoretical edge; Kelly-optimal size = 0"
  - "catalyst is administrative (date-setting), not fundamental; sector tailwind already priced in, mild adverse asymmetry for a naive long"
  re_entry_conditions:
  - "working live EUROB.AT quote feed appears"
  - "consensus Q2 2026 estimate (EPS/NII) becomes available"
  - "implied-move / options-chain data becomes available"
  re_entry_deadline: '2026-07-29'
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
  dissent: "Bull's re-rating/upside-optionality claim and bear's near-highs/downside-skew
    claim are both unfalsifiable given zero verified price data for EUROB.AT; the
    arbiter (quant) resolves the pre-print skew as UNKNOWN rather than picking a
    side, and treats that unfalsifiability itself as an independent reason to stand
    aside."
  transcript: transcript.md
  last_updated: '2026-07-23T13:53:56Z'
---

## Scouted 2026-07-22T17:49:00Z

## Researched 2026-07-23T13:53:56Z

Three-round panel (bull/bear/quant) unanimously converged on NO-TRADE. The dossier
confirms only the earnings date; no live price feed exists for EUROB.AT via our
tooling (TwelveData 404s, Athens Exchange coverage gap), and no consensus estimate
or options data was available to construct a defined-risk trade or an EV
calculation. Full debate in `transcript.md`.
