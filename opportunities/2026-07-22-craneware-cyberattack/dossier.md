---
id: 2026-07-22-craneware-cyberattack
title: Craneware discloses cyberattack with data exfiltration
status: researched
created: '2026-07-22T11:19:27Z'
event:
  type: regulatory
  summary: UK healthcare billing software firm Craneware disclosed on July 20, 2026
    that attackers exfiltrated a significant volume of file names before being removed
    from its systems; ongoing US/UK forensic investigation could reveal further scope
    or customer-notification costs.
  impact_window: '2026-08-20'
tickers:
- CRW.L
sources:
- title: 'TechRepublic: Craneware Confirms Data Theft After Cyberattack'
  url: https://www.techrepublic.com/article/news-craneware-cyberattack-data-theft-2026/
  accessed_at: '2026-07-22T11:19:27Z'
hypothesis:
  statement: >-
    Craneware's file-names-only exfiltration is one of the milder cyber-disclosure
    categories (base-rate abnormal returns of -1 to -5 percent with typical
    partial-to-full recovery), but the trade is not takeable on two extra-thesis
    grounds that all three personas converged on. First, executability -- CRW.L,
    CRW:LSE, CRW.LON and CRW all return HTTP 404 on twelvedata, so the instrument is
    unpriceable via our real provider and simulated P/L is structurally zero
    regardless of direction (the NYAX unpriceable-resolves-neutral lesson). Second,
    economics -- the quant's gross EV of +1.25 percent (0.30x+6, 0.45x+1, 0.25x-4) is
    erased by AIM round-trip costs of 1.5 to 2.5 percent for net EV near -0.75
    percent, and even granting the bull's most favorable skew the net lands at
    roughly -0.5 to +0.5 percent, a coin-flip inside the noise band with
    signal-to-noise of 0.12 to 0.15, at or below the 0.15 durability floor. Sourcing
    is a single secondary TechRepublic article with no primary RNS or ICO filing, and
    the 2026-08-20 impact window is a soft analyst date rather than a scheduled
    catalyst. Stand aside.
  direction: none
  confidence: 18
plan:
  ticker: CRW.L
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
    The one unresolved disagreement is hypothetical direction if the instrument were
    suddenly priceable and properly sourced -- moot this cycle since size is 0, but
    logged for the post-mortem rather than papered over. The bull would go long
    (initial cyber headlines are systematically fear-overpriced, sticky hospital RCM
    customers imply low churn, file-names-only is a mild category). The quant leans
    weak-fade/short on the -1 to -5 percent breach base rate but flags the edge is
    not separable from noise. The bear declines any directional side, arguing both
    the bull and quant underweight forensic-scope-growth risk (breach scope
    historically widens, not narrows), which fattens the left tail without creating
    a bull case. Testable post-mortem trigger to revisit -- a working alternate
    price feed for CRW.L, a primary RNS/ICO source quantifying PHI-adjacent
    exposure, AND the soft 2026-08-20 date replaced by an actual scheduled event.
  last_updated: '2026-07-23T11:34:55Z'
---

## Scouted 2026-07-22T11:19:27Z

## Researched 2026-07-23T11:34:55Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Unanimous
stand-aside at 0% size, for three complementary reasons. Executability (bear):
CRW.L is unpriceable -- CRW.L / CRW:LSE / CRW.LON / CRW all 404 on twelvedata, so
simulated P/L is structurally 0 (NYAX unpriceable-resolves-neutral lesson).
Economics (quant): gross EV +1.25% (0.30x+6% + 0.45x+1% + 0.25x-4%) is erased by
1.5-2.5% AIM round-trip costs, net approximately -0.75%; even the bull's most
favorable skew nets -0.5% to +0.5%, a coin-flip with signal-to-noise 0.12-0.15
at/below the 0.15 floor. Thesis (bull): the "contained file-names-only" read and the
bear's "PHI-adjacent" read are both unconfirmed absent a primary RNS/ICO filing --
the directional thesis is untestable. The bull conceded the 404 is dispositive and
dropped the "exit near/before Aug 20" precision; Aug 20 is a soft analyst date, not a
scheduled catalyst. Sole source is one secondary TechRepublic article. Verdict:
NO-TRADE (not scheduled, not simulated). Revisit only on (a) a working alternate
CRW.L price feed, (b) a primary RNS/ICO source quantifying PHI-adjacent scope, AND
(c) Aug 20 replaced by a real scheduled event. Full debate in `transcript.md`.
