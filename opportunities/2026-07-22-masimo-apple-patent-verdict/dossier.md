---
id: 2026-07-22-masimo-apple-patent-verdict
title: Masimo patent verdict against Apple upheld by federal judge
status: researched
created: '2026-07-22T11:19:27Z'
event:
  type: regulatory
  summary: A California federal judge rejected Apple's bid to overturn a jury verdict
    awarding Masimo USD 634 million for Apple Watch pulse-oximetry patent infringement,
    raising damages and injunction-enforcement risk for Apple while removing a major
    overhang for Masimo.
  impact_window: '2026-09-30'
tickers:
- MASI
- AAPL
sources:
- title: 'Law360: Apple Can''t Get Judge To Toss Masimo''s 634M Patent Verdict'
  url: https://www.law360.com/articles/2503506/apple-can-t-get-judge-to-toss-masimo-s-634m-patent-verdict
  accessed_at: '2026-07-22T11:19:27Z'
hypothesis:
  statement: "This ruling is not a tradeable edge. It is a procedural denial of a
    motion to overturn a jury verdict that has been public since early 2025, so the
    base liability outcome (P(denial) roughly 80-85 percent) was largely priced in
    already. The only leg with real dollar magnitude, MASI (the USD 634 million
    award is roughly 7.5 percent of its ~USD 8.5 billion market cap), is structurally
    unpriceable in this system: twelvedata returned HTTP 404 for every MASI
    timestamp tested by three independent personas, so any MASI plan would resolve
    as an uninformative neutral rather than a real edge test. AAPL is priceable
    (twelvedata returned a clean quote near USD 321-324) but the award is about
    0.018 percent of AAPL's roughly USD 3.5 trillion market cap, an order of
    magnitude below the panel's 0.15 durable-edge SNR threshold, with negative
    expected value after costs. Apple retains a live Federal Circuit appeal,
    injunction/import enforcement is likely stayed pending that appeal, and Apple
    has already shipped a pulse-oximetry workaround, so no cash or business-mix
    impact is expected by the 2026-09-30 impact window. All three personas
    (bull, bear, quant) converged to no-trade by Round 2."
  direction: none
  confidence: 88
plan:
  ticker: MASI
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: "Bear's short-duration fade-the-pop MASI short is the one un-actioned
    idea with a plausible edge: it only needs to observe that a pop occurred
    (verifiable via news wires or options IV even without a clean twelvedata entry
    fill), so it partially sidesteps the pricing blocker that kills the bull's MASI
    long. It stayed unresolved because the panel would not manufacture a trade
    without a verified price print, given quant's SNR math. If MASI pricing were
    ever solved, this fade short, not the bull's long, is the defensible direction."
  last_updated: '2026-07-23T19:52:00Z'
---

## Scouted 2026-07-22T11:19:27Z

## Researched 2026-07-23T19:52:00Z
