---
id: 2026-07-15-johnson-johnson-q2-fy26
title: Johnson & Johnson Q2 FY26 earnings
status: researched
created: '2026-07-07T05:39:26Z'
event:
  type: earnings
  summary: JNJ reports Q2 before open Jul 15; MedTech/pharma growth and full-year
    guidance update the read
  impact_window: '2026-07-15'
tickers:
- JNJ
sources:
- title: Johnson & Johnson Q2 2026 Earnings Report (MarketBeat)
  url: https://www.marketbeat.com/earnings/reports/2026-7-15-johnson-johnson-stock/
  accessed_at: '2026-07-07T05:39:26Z'
hypothesis:
  statement: JNJ Q2 FY26 is priced for perfection with the stock at/above every sell-side
    Buy target under the $278.99 sim anchor, leaving no upside headroom, thin net
    EV below fee drag, and an un-hedgeable talc/Stelara left tail. No edge survives
    after costs.
  direction: neutral
  confidence: 40
plan:
  ticker: JNJ
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
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
  dissent: 'The bull''s confirmation-gated long survives partially: a 13:31Z gap-up-hold
    entry truncates the down-gap tail and could be a realistic +0.5-0.8% token probe
    (Quant scored it ~breakeven, +0.04-0.08%, firing in only ~50-55% of paths). Had
    the sim printed a genuine confirmed gap-up above $278.99, the least-bad trade
    would be that small gated long rather than zero. The unresolved crux: whether
    a near-zero-EV gated probe is worth the fee/tail risk. Two personas say no, and
    the bull''s own headroom precondition is removed by the anchor.'
  last_updated: '2026-07-07T20:26:21Z'
---

## Scouted 2026-07-07T05:39:26Z

## Researched 2026-07-07T20:26:21Z — NO-TRADE

Two of three personas (bear, quant) concluded NO-TRADE, and the bull conceded to confidence 38 conditioned on a price-headroom precondition. Under the ground-truth sim anchor of $278.99, JNJ trades at or above every cited Buy target (Guggenheim $270; HSBC $290), eliminating that precondition and strengthening the 'priced for perfection' read. Quant's math is decisive: gross directional EV ~+0.03% flips to ~-0.09% net of ~0.12% costs, and even the gated long only reaches ~breakeven (+0.04-0.08%) while owning just residual intraday continuation after the overnight gap. The talc/Stelara left tail is un-hedgeable and asymmetric to the downside; both option structures lose because implied >= realized. Confidence ~40 (< 45) against an asymmetric adverse tail is a textbook no-trade filter, never a naked short. Revisit only on a genuine gap-down, pre-print IV collapse, or talc resolution.
