---
id: 2026-07-08-caesars-icahn-fertitta-bidding-war
title: Caesars go-shop deadline amid Icahn rival bid to Fertitta's $17.6B deal
status: simulated
created: '2026-07-08T17:21:22Z'
event:
  type: regulatory
  summary: Carl Icahn made a rival $33/share bid topping Fertitta's accepted $31/share
    buyout; Caesars' 45-day go-shop window (during which it can pursue superior offers)
    expires July 11.
  impact_window: '2026-07-11'
tickers:
- CZR
sources:
- title: Caesars stock pulls back as Icahn rival bid looms over Fertitta deal - Las
    Vegas Sun
  url: https://lasvegassun.com/news/2026/jul/08/caesars-stock-pulls-back-wednesday-as-icahn-rival/
  accessed_at: '2026-07-08T17:21:22Z'
hypothesis:
  statement: The go-shop resolution has a modest positive real-world expected value
    (Fertitta matches or Icahn wins outright in ~60% of outcomes, only ~30% see the
    premium fade/deal break), but that edge is largely priced in and the panel could
    not agree whether the observed price series reflects real signal or noise. Net
    call is a minimal, low-conviction long into the 2026-07-11 go-shop deadline, not
    a conviction bet.
  direction: long
  confidence: 35
plan:
  ticker: CZR
  action: buy
  entry:
    time: 2026-07-10 14:00:00+00:00
    target_price: 31.5
  exit:
    time: 2026-07-11 20:00:00+00:00
    target_price: 32.0
  expected_profit_pct: 1.6
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-10T07:41:56Z'
simulation:
  ran_at: '2026-07-11T22:34:53Z'
  fills: []
  realized_profit_pct: 0.0
  outcome: neutral
  matched_hypothesis: 'no'
  note: 'market data unavailable: CZR 2026-07-11: HTTP 400'
---

## Scouted 2026-07-08T17:21:22Z

## Researched 2026-07-10T07:41:56Z

Three-round panel (bull/bear/quant → opus synthesis) converged on a minimal,
low-conviction long. Full transcript: `transcript.md`. Key tension the panel could
not resolve: whether the `toa price` series available in this sandbox is usable
signal or pure noise relative to deal economics — see dissent in transcript. Sized
the plan as a token position (not a conviction trade) per the quant persona's
Kelly-near-zero finding.

---
### Revision 2026-07-11T22:34:53Z
Skipped CZR: market data unavailable (CZR 2026-07-11: HTTP 400)
