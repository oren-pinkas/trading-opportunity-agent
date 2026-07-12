---
id: 2026-07-10-section122-tariff-expiration
title: Section 122 10% global tariff surcharge sunsets July 24
status: researched
created: '2026-07-10T15:17:34Z'
event:
  type: regulatory
  summary: The Section 122 10% global import surcharge, in effect since February 24,
    expires by operation of law at 12:01am EDT July 24, 2026 absent congressional
    extension, easing cost pressure on import-heavy retailers.
  impact_window: '2026-07-24'
tickers:
- COST
- BBY
- FIVE
sources:
- title: Section 122 Global Surcharge Set to Expire July 24 by Operation of Law
  url: https://www.tradelawcounsel.com/insights-news/2026/7/4/section-122-surcharge-sunsets-july-24-what-importers-should-do-beforeand-afterthe-150-day-clock-runs-out
  accessed_at: '2026-07-10T15:17:34Z'
hypothesis:
  statement: >-
    The July 24, 2026 sunset of the Section 122 10% global tariff surcharge is a
    pre-announced, mechanical statutory event (150-day clock public since Feb 24)
    that is substantially priced into COST/BBY/FIVE, and it carries a hidden third
    outcome -- extension or replacement via IEEPA/Section 301 that can fire with
    little warning -- leaving no positive-expectancy directional edge in the 12-day
    window as of July 12. Bear and quant converged on NO TRADE from independent
    methodologies (legal/disconfirmation reasoning vs. explicit EV math) with rising
    confidence across rounds, while quant's EV for the cleanest expression (long BBY)
    degraded from -0.19% to -0.455% after absorbing the replacement-authority risk.
  direction: none
  confidence: 26
plan:
  ticker: BBY
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
    Whether quant's p(extension/replacement)=0.25 is a stale prior that should
    mechanically decay toward 5-10% as July 20 passes in legislative silence
    (flipping EV positive on a small long BBY, per bull) or is an irreducible tail
    because IEEPA/Section 301 replacement authority can be invoked with zero warning
    and therefore does NOT decay with silence (per quant, who explicitly rejects
    silence-as-signal). This is the single variable that would move the call from
    NO TRADE to a small conditional long. Testable post-mortem: did the surcharge
    expire cleanly with no replacement signal by July 20-24, and if so, was the
    silence-decay logic vindicated or was the lack of a move simply confirmation
    that it was priced in all along?
  last_updated: '2026-07-12T13:55:00Z'
---

## Scouted 2026-07-10T15:17:34Z

## Researched 2026-07-12T13:55:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation
on this opportunity alone. The Section 122 10% global surcharge sunsets by operation
of law at 12:01am EDT July 24 absent congressional extension. BULL proposed long
BBY/FIVE (highest import-cost sensitivity, thin margins) starting confidence 62,
built on the sunset being a clean, dated, mechanical trigger. BEAR called it textbook
"priced in" (a 5-month-public statutory clock) and flagged replacement-authority risk
(IEEPA/Section 301) plus magnitude mismatch for large diversified retailers;
confidence in skepticism rose 70->78 across rounds. QUANT's explicit EV calc for BBY
started at -0.19% net of costs and degraded to -0.455% after weighting the
replacement-risk tail more heavily (p 0.20->0.25, adverse move -2.5%->-3.0%);
confidence rose 72->76. BULL conceded the single-source dossier gap and COST as dead
weight, narrowed to a smaller conditional BBY-only long contingent on legislative
silence through July 18-20, and confidence fell 62->55 -- weakening under scrutiny
rather than strengthening. Two independent methodologies converging on NO TRADE with
rising conviction, against a bull thesis that lost conviction, was decisive.
Verdict: NO-TRADE (not scheduled, not simulated). Optionality preserved via a
watch-plan: revisit a small long BBY only if no extension/replacement signal
surfaces by ~July 18-20 AND a corroborating second source appears; any
extension/replacement headline kills the idea permanently. Full debate with
citations in `transcript.md`.
