---
id: 2026-07-12-humana-q2-guidance-cut
title: Humana Q2 2026 earnings test post-guidance-cut outlook
status: researched
created: '2026-07-12T18:06:04Z'
event:
  type: earnings
  summary: Humana reports Q2 2026 results July 29 after cutting FY26 GAAP EPS guidance
    to at least $8.36 from $8.89 on Medicare Advantage Star Ratings headwinds.
  impact_window: '2026-07-29'
tickers:
- HUM
sources:
- title: Humana to release Q2 2026 results on July 29, 2026
  url: https://scanx.trade/stock-market-news/companies/humana-to-release-q2-2026-results-on-july-29-2026/43707846
  accessed_at: '2026-07-12T18:06:04Z'
hypothesis:
  statement: >-
    The panel's edge collapses on a single unresolved fork: the Medicare Advantage
    Star Ratings bonus-payment lag length (~1yr vs ~2yr), which determines whether
    the already-disclosed guidance cut ($8.89→at least $8.36) is stale, fully-priced
    news by 2026-07-29, or the first installment of a multi-year headwind with a live
    down-tail at the print. Neither regime was resolved with real data. Reframing
    Round 1's single 45/25/30 distribution as an honest ~50/50-to-60/40 blend of the
    two regimes (+2.3% EV if stale vs -3.2% EV if first-of-many) drops blended gross
    EV to roughly -0.45% to +0.10%, inside/below a ~9:1 noise-to-signal band even
    before costs. All three panelists independently moved toward lower confidence and
    NO TRADE across rounds (bull 42→38, bear 28→24, quant 42→35).
  direction: none
  confidence: 30
plan:
  ticker: HUM
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
    The Star Ratings bonus-payment lag length (~1yr vs ~2yr) between bull and bear is
    the strongest unresolved disagreement. The bull's "stale news, no fresh data at
    this print" thesis requires ~2yr; the bear's "first cut in a multi-year headwind,
    live down-tail risk" thesis requires ~1yr. The quant showed an honest 50/50-to-60/40
    prior across the two regimes erases the Round-1 edge. Score this NO-TRADE against
    which regime actually played out: a sharp move on fresh Star-Ratings-driven news
    at the print vindicates standing down; a non-event print means the stale regime
    held and a small long was the missed edge.
  last_updated: '2026-07-12T22:37:45Z'
---

## Scouted 2026-07-12T18:06:04Z

## Researched 2026-07-12T22:37:45Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation on
this opportunity only. Core finding: the guidance cut is public and known, but whether
it's stale (no fresh info at the 7/29 print) or the first of a multi-year Star Ratings
headwind (live down-tail risk at the print) hinges entirely on the CMS bonus-payment lag
length, which no persona could pin down with real data (~1yr per bear vs ~2yr per bull).
The quant decomposed Round 1's single 45/25/30 up/flat/down distribution into an explicit
two-regime mixture (+2.3% EV if stale, -3.2% EV if first-of-many) and showed an honest
50/50-to-60/40 blend erases the Round-1 edge (+0.75% gross → -0.45% to +0.10% gross).
All three personas converged downward in confidence and toward NO TRADE across rounds.
Additional open gaps: consensus EPS vs the $8.36 floor, BMO/AMC timing for the 7/29
print, live options-chain data, and pre-cut vs post-cut price action. Revisit
2026-07-24 to 2026-07-26 (3-5 days pre-print) once these resolve; only reconsider a
long (call debit spread, long ~$87/short ~$92-95 strike, August expiry) if the lag
resolves to ~2yr and the other gaps come in supportively. Full debate in
`transcript.md`.
