---
id: 2026-07-22-otsuka-nuedexta-patent-expiry
title: Nuedexta patent expiry opens door to Hetero generic launch
status: researched
created: '2026-07-22T09:10:18Z'
event:
  type: regulatory
  summary: Federal Circuit's injunction blocking Hetero's generic Nuedexta only holds
    until the underlying Otsuka patent expires in August 2026, setting up a launch/re-litigation
    catalyst
  impact_window: '2026-08-31'
tickers:
- OTSKY
sources:
- title: Federal Circuit Affirms Preliminary Injunction Against Generic Nuedexta
  url: https://www.lit-ip.aoshearman.com/federal-circuit-affirms-preliminary-injunction-against-generic-nuedexta
  accessed_at: '2026-07-22T09:10:18Z'
hypothesis:
  statement: >-
    The Aug-2026 injunction expiry is a real but immaterial corporate event for
    Otsuka (Nuedexta is only ~1-2 percent of group revenue) and the generic entry
    has been long-anticipated and largely priced. More decisively, the scoped
    instrument OTSKY (OTC pink ADR) is not where real price discovery happens
    (that lives on Tokyo-listed 4578.T) and is so illiquid that the real data
    provider (twelvedata) returned only 12 one-minute bars for the entire session
    on 2026-07-22, several at zero volume, price pinned in a ~USD 0.11 band
    (USD 33.50-33.61), and returned zero matching bars at multiple other tested
    intraday timestamps across two separate sessions. There is no capturable,
    priceable edge in OTSKY.
  direction: none
  confidence: 8
plan:
  ticker: OTSKY
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
  dissent: >-
    Whether the zero-matching-bars result is a genuine liquidity fact about OTSKY
    or partly a twelvedata provider/API artifact (symbol mapping, coverage gap)
    is unresolved and worth confirming with a second source before treating
    "unpriceable" as permanent. Separately, both bull and bear noted the
    underlying corporate action might be legitimately tradeable via Tokyo-listed
    4578.T (real liquidity, real price discovery) or a liquid pharma peer/basket
    -- quant declined to launder the OTSKY thesis through a substitute ticker,
    since that would be a different, separately-scoped opportunity. Open question
    for scouting, not this dossier: is a 4578.T variant worth its own scout entry
    (note the ~1-2 percent revenue materiality problem travels with it regardless
    of venue).
  last_updated: '2026-07-23T21:51:35Z'
---

## Scouted 2026-07-22T09:10:18Z

## Researched 2026-07-23T21:51:35Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three personas
independently converged on SKIP via three different routes: immateriality (Nuedexta
~1-2% of Otsuka's consolidated revenue), stale/priced information (the injunction and
its Aug-2026 expiry have been public/litigated for months), and -- decisively --
execution impossibility. Real-provider price check (twelvedata) confirmed OTSKY printed
only 12 one-minute bars across the entire 2026-07-22 session, several at zero volume,
price pinned USD 33.50-33.61, and returned zero matching bars for several other tested
intraday timestamps across two sessions. The bull fully conceded (self-confidence
dropped 3.5/10 -> 1/10), agreeing OTSKY is unpriceable/unfillable regardless of thesis
quality. Verdict: this is not a "trade zero size" outcome but a "no valid entry/exit
plan can be produced" outcome -- a plan the real provider can't price resolves as an
uninformative neutral per institutional lesson. No position, no size, no entry, no exit.
Full debate in `transcript.md`.
