---
id: 2026-07-13-tariff-section122-expiry
title: Section 122 tariffs expire July 24, reciprocal tariff reversion
status: scheduled
created: '2026-07-13T18:24:37Z'
event:
  type: regulatory
  summary: 10% Section 122 balance-of-payments tariffs expire July 24; reciprocal
    tariffs reverted higher July 9 absent extension, hitting importers (PG) while
    benefiting onshoring plays (STLD).
  impact_window: '2026-07-24'
tickers:
- PG
- STLD
sources:
- title: 'July Market Outlook: Tariffs, Trade and the Next Inflation Test'
  url: https://www.investing.com/analysis/july-market-outlook-tariffs-trade-and-the-next-inflation-test-200682939
  accessed_at: '2026-07-13T18:24:37Z'
hypothesis:
  statement: 'Panel found no positive-EV directional edge. The tariff move that actually
    happened - reciprocal tariffs reverting higher on July 9 - is bullish for domestic
    steel and already realized (STLD moved about +1.6% into 2026-07-15); the July 24
    Section 122 expiry is a separate, smaller, and likely opposite-signed event because
    it removes a narrow balance-of-payments import protection while leaving the
    dominant Section 232 steel duties untouched, making it mildly negative (not
    positive) for STLD and mildly positive (not negative) for importer PG, inverting
    the framing in the original dossier. PG was dropped as a trade candidate on sign
    and immateriality grounds. The only residual read is a small contrarian fade in
    STLD if the market applied the same conflated logic the original dossier used.
    Recorded as a minimal low-conviction short expression to keep this in the
    learning loop, not because a real edge was established.'
  direction: short
  confidence: 18
plan:
  ticker: STLD
  action: short
  entry:
    time: '2026-07-22T14:00:00Z'
    target_price: 233.67
  exit:
    time: '2026-07-24T19:45:00Z'
    target_price: 232.97
  expected_profit_pct: 0.3
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
  dissent: 'Unresolved: whether Section 122 balance-of-payments tariff authority
    actually overlaps with any steel-relevant duties at all, or is orthogonal to
    the Section 232 steel regime, in which case even the mildly-negative-for-STLD
    thesis collapses to noise. Also unresolved: whether the market already priced
    the correct sign for the July 24 expiry (mild negative for STLD, mild positive
    for PG) or applied the same conflated positive-positive logic the original
    dossier used, which determines whether this recorded short is a valid
    contrarian fade or itself on the wrong side. Tail risk: a last-minute
    tariff-authority extension or replacement action (IEEPA, Section 301, or
    Section 232) before July 24, a pattern this administration has shown on other
    tariff deadlines. No panelist could confirm the hard-sunset date or the
    Section 122 scope against a primary source (Federal Register or USTR); the
    entire debate rests on one Investing.com dossier source.'
  last_updated: '2026-07-16T04:30:05Z'
---

## Scouted 2026-07-13T18:24:37Z

## Researched 2026-07-16T04:30:05Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real prices pulled
via twelvedata (NOT the stub default): PG ~USD 147.58-149.45, STLD ~USD 229.91-234.20
across 2026-07-08 through 2026-07-15. The panel did **not** find a tradable edge: bull
withdrew the original long-STLD thesis after quant showed the dossier had conflated
two opposite-signed mechanisms (the already-realized, bullish-for-steel July 9
reciprocal-tariff reversion, versus the mildly bearish-for-steel July 24 Section 122
expiry, which removes import protection rather than adding it). PG was dropped
entirely on immateriality and wrong-sign grounds. Recorded as a minimal SHORT STLD
expression at confidence 18 to keep the call in the learning loop; the real output is
"no clean edge, thin single-source dossier, sign of the STLD thesis was likely
inverted." Full debate with citations in `transcript.md`.
