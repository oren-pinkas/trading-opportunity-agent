---
id: 2026-07-22-india-us-trade-deadline
title: India-US trade deal tariff deadline
status: researched
created: '2026-07-22T07:00:28Z'
event:
  type: geopolitical
  summary: India-US negotiators race toward July 24 2026 tariff deadline with talks
    in final stage
  impact_window: '2026-07-24'
tickers:
- INFY
sources:
- title: Blitz India Media - India-US trade agreement nears as tariff deadline looms
  url: https://blitzindiamedia.com/news/india-us-trade-agreement-july-2026/
  accessed_at: '2026-07-22T07:00:28Z'
hypothesis:
  statement: >-
    A single low-tier source ("final stage" per Blitz India Media) reporting
    progress toward the July 24 2026 India-US tariff deadline does not establish
    a tradable edge in INFY. The probability-weighted outcome is negative -- the
    modal result (extension or vague framework, roughly 45 percent) pays close to
    zero, the downside branch (breakdown, roughly 25 percent, about -4 percent)
    carries more magnitude than the upside branch (clean deal, roughly 30
    percent, about +3 percent), and the sim cannot path-monitor, so any
    intraday stop or target framing is prose rather than an executable risk
    control. Gross EV is slightly negative (about -0.10 percent) and turns
    solidly negative (about -0.4 to -0.6 percent) net of costs. Compounding
    this, INFY is an IT-services name whose revenue is not mechanically tied to
    goods-tariff relief, so even a favorable, well-sourced outcome may not
    transmit to the instrument.
  direction: none
  confidence: 18
plan:
  ticker: INFY
  action: no-trade
  entry:
    time: 'n/a'
    target_price: null
  exit:
    time: 'n/a'
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
    The convergence on NO-TRADE masks a genuine split over WHY, and the two
    reasons imply different futures. The quant's objection is quantitative and
    curable -- an information-quality and EV problem, where tier-1
    corroboration shifting the probability weights (raising the clean-deal
    branch) could flip the sign and make a small long rational. The bear's
    deeper objection is structural and may be incurable -- the
    goods-tariff-vs-IT-services instrument mismatch means the causal link
    between the catalyst and INFY's price may be spurious, so no amount of
    better sourcing rescues INFY specifically; better news would justify a
    trade in a DIFFERENT instrument, not this one. The unresolved question that
    would resurface the instant a tier-1 source confirms: is the residual INFY
    move on trade headlines a real, tradable sentiment/beta effect, or pure
    noise/reflexive correlation that will not pay reliably? That disagreement
    was never settled because the EV was negative enough that both sides could
    agree to stand down without resolving it -- but it is the pivot on which
    any future re-entry, and choice of instrument, entirely depends.
  last_updated: '2026-07-23T17:30:06Z'
---

## Scouted 2026-07-22T07:00:28Z

## Researched 2026-07-23T17:30:06Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), evaluated on this
opportunity's own merits alone. BULL opened long INFY (entry USD 10.67, target
USD 11.20-11.50, about 5-8 percent) on the "both deal-and-extension outcomes skew
positive" framing, but conceded in Round 2 after BEAR and QUANT showed the framing
collapses once weighted: the modal outcome (extension/framework, about 45 percent)
pays close to zero, and the downside branch (-4 percent) exceeds the upside branch
(+3 percent). QUANT's EV = 0.30(+3%) + 0.45(0%) + 0.25(-4%) = about -0.10 percent
gross, about -0.4 to -0.6 percent net of costs. Two structural problems drove the
convergence: (1) single low-tier source (Blitz India Media, no PTI/Reuters/USTR
corroboration) on a pattern of "final stage" language that has recurred since 2024
without a signed deal, and (2) instrument mismatch -- INFY is IT-services, not a
goods exporter, so tariff relief does not mechanically transmit to its revenue. The
sim's lack of path-dependent monitoring also means no exit/invalidation clause can
be relied on as a real stop. Verdict: NO-TRADE. Re-entry trigger: a tier-1 source
(Reuters/PTI/USTR/Indian Commerce Ministry) corroborating "final stage" before the
deadline, and even then, prefer a goods-exposed instrument over INFY, sized only to
the clean-deal branch. Full debate in `transcript.md`.
