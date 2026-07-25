---
id: 2026-07-23-pan-american-silver-q2-earnings
title: Pan American Silver reports Q2 2026 results Aug 12
status: researched
created: '2026-07-23T00:14:58Z'
event:
  type: earnings
  summary: Pan American Silver will announce unaudited Q2 2026 results after close on 2026-08-12, with consensus anticipating over 100 percent YoY EPS growth on high silver and gold prices
  impact_window: '2026-08-12'
tickers:
- PAAS
sources:
- title: Pan American Silver to Announce Second Quarter 2026 Unaudited Financial Results
  url: https://www.stocktitan.net/news/PAAS/pan-american-silver-to-announce-second-quarter-2026-unaudited-qbc5zzuo2v1l.html
  accessed_at: '2026-07-23T00:14:58Z'
hypothesis:
  statement: PAAS Q2 2026 earnings carry no exploitable directional edge. The consensus USD 100 percent-plus YoY EPS growth figure is a near-deterministic function of already-public Q2 metal prices and pre-guided production, so it is fully embedded in the Zacks USD 0.93 consensus rather than being new information. The one genuinely uncertain line, AISC, is unforecastable by this panel and plausibly already reflected in guidance and consensus. The panel's best estimate is P(up) 0.47 versus P(down) 0.53, conditional moves of roughly plus 5.5 percent versus minus 6.0 percent, giving unconditional event EV of about minus 0.60 percent before costs.
  direction: neutral
  confidence: 80
plan:
  ticker: PAAS
  action: no-trade
  entry:
    time: '2026-08-12T20:00:00Z'
    target_price: 43.5
  exit:
    time: '2026-08-13T20:00:00Z'
    target_price: 43.5
  expected_profit_pct: 0.0
  reasoning: No position in either direction. A naked long needs P(up) roughly 0.60 or higher to clear costs on the event alone, and roughly 0.65 for a full pre-event-window hold; the panel's best estimate is 0.47. A naked short is the same negative-EV structure sign-flipped once the bear conceded the priced-in-at-a-fresh-high framing did not apply here (PAAS was already about 35 percent off its USD 69.99 52-week high, mid-range, not extended). Event-isolated, beta-hedged (vs SLV/SIL), and options constructions were all evaluated and net to roughly zero or negative EV after costs. Separately, live PAAS quotes failed with HTTP 429 three consecutive times across the debate, so any entry anchored to a live pre-event quote is unverifiable with the current data provider.
research:
  strategy: debate-three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-25T20:18:45Z'
  dissent: 'Unresolved falsifier named by the quant and never checked by anyone: was the reported AISC guidance cut (from USD 15.75-18.25 per oz to USD 14.50-15.50 per oz, single-sourced and ambiguous) published before or after the last refresh of the Zacks USD 0.93 consensus? If the cut post-dates the consensus refresh, roughly USD 1.25-3.75 per oz of unit-cost improvement is not in the USD 0.93 number, the print mechanically beats, and the correct call flips from NO TRADE to a sized long. A weaker open item: the quant assumed oversold-squeeze potential and negative pre-event momentum roughly cancel to hold P(up) at 0.47 after a greater-than-30-percent drawdown; that cancellation was assumed, not measured.'
---

## Scouted 2026-07-23T00:14:58Z

## Researched 2026-07-25T20:18:45Z

Three-round panel debate (bull/bear/quant, synthesized by opus) converged independently
on NO TRADE. Full transcript: see `transcript.md`. Bull started at confidence 55/100
long and conceded down to ~35, ultimately agreeing "the quant's EV math probably still
wins this argument." Bear started at ~65-70% confidence for fade/short and converged
to NO TRADE once the "priced-in at a fresh high" framing was conceded not to apply
(PAAS traded ~35 percent off its 52-week high, not extended). Quant held NO TRADE
throughout and finished at confidence 80/100, noting both opponents' strongest
arguments widened the tails of the distribution without moving its slightly-negative
mean. Key unresolved falsifier carried into any future revisit: AISC guidance-cut
timing versus the last consensus refresh (see `dissent` above).
