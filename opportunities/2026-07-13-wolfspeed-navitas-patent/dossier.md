---
id: 2026-07-13-wolfspeed-navitas-patent
title: Wolfspeed sues Navitas over patent infringement, NVTS drops 7%
status: researched
created: '2026-07-13T19:27:39Z'
event:
  type: regulatory
  summary: Wolfspeed filed a patent infringement suit against Navitas Semiconductor
    in Delaware federal court over GaN power products; NVTS shares fell 7% on the
    filing.
  impact_window: '2026-08-13'
tickers:
- NVTS
- WOLF
sources:
- title: Navitas Semiconductor Shares Drop After Wolfspeed Files Patent Infringement
    Lawsuit
  url: https://finance.yahoo.com/technology/articles/navitas-semiconductor-shares-drop-wolfspeed-133256201.html
  accessed_at: '2026-07-13T19:27:39Z'
hypothesis:
  statement: >-
    The 7% NVTS drop is a headline-driven reaction to a patent-suit filing whose
    earliest possible legal catalyst (ruling, injunction) falls well outside the
    impact window, leaving no dated, tradeable event by 2026-08-13. The modest
    mean-reversion edge is fully consumed by transaction costs and dominated by an
    uncatalyzed left-tail (preliminary-injunction, sales-injunction, or settlement
    headline risk that can land on any day, not just the impact-window date).
  direction: none
  confidence: 74
plan:
  ticker: NVTS
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
    Is there a tradeable edge in the absence of a dated legal catalyst? Bull argued
    yes: the thesis is flow/sentiment (panic-seller exhaustion), which does not
    require a litigation-timeline catalyst, and the quant's own down-tail is itself
    uncatalyzed. Bear, joined substantively by quant, argued no: with no dated
    catalyst this is drift/pattern trading mislabeled as a lawsuit thesis, the true
    edge is centered at zero-to-negative, and an unscheduled settlement or
    preliminary-injunction headline can strike on any day, making the risk
    genuinely asymmetric against a long. Unresolved because the volume signature
    (light gap-down vs. heavy distribution) that would confirm or kill the
    panic-exhaustion premise was never checked - flagged by both personas as the
    key variable for a future revisit.
  last_updated: '2026-07-16T08:39:22Z'
---

## Scouted 2026-07-13T19:27:39Z

## Researched 2026-07-16T08:39:22Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), single-source
dossier (one Yahoo Finance wire item on the filing). Real market data (twelvedata)
has no coverage for this event's date; only flagged stub/fake prices were available
and carried no evidentiary weight. All three personas converged on NVTS as the only
candidate long (never WOLF, given its balance-sheet distress) and agreed the
2026-08-13 impact_window is a dossier reference date, not a scheduled legal
event - Delaware patent suits take 12-24+ months to reach a ruling, so no
adjudicable catalyst falls inside this window. Quant's fully-costed EV was negative
in both the no-PI-aware case (net approx -0.20% to -0.30%) and the
PI-aware case, after pricing an explicit preliminary-injunction left-tail (net
approx -1.45% to -1.55%). Bull folded from a full-size long to a conditional
0.25-0.4%-of-book fade gated on two unverified facts (no PI motion on file; suit
scope not expanded by a second source) - since neither is confirmed, the default
outcome is no trade. Bear held no-trade throughout. Verdict: NO-TRADE, confidence
74. Flips only if a second source confirms damages-only relief plus panic-volume
exhaustion (reopens a small tactical NVTS long) or confirms a preliminary/sales
injunction (flips bias toward short-into-strength on NVTS). Full debate in
`transcript.md`.
