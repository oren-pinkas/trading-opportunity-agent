---
id: 2026-07-23-navitas-q2-2026-earnings
title: Navitas Semiconductor Q2 2026 earnings
status: researched
created: '2026-07-23T18:53:42Z'
event:
  type: earnings
  summary: NVTS reports Q2 2026 results after close Monday Jul 27; prior two prints
    averaged roughly 13.6 percent one-day moves, with guide of USD 10.0M revenue and
    39.25 percent gross margin midpoint
  impact_window: '2026-07-27'
tickers:
- NVTS
sources:
- title: Navitas Semiconductor to Report Q2 2026 Financial Results on Monday
  url: https://www.stocktitan.net/news/NVTS/navitas-semiconductor-to-report-q2-2026-financial-results-on-monday-o9f0gizwbm89.html
  accessed_at: '2026-07-23T18:53:42Z'
hypothesis:
  statement: "NVTS Q2 2026 earnings is a high-magnitude, direction-unknown volatility\
    \ event, not a directional edge. The only quantified estimate (n=2 prior prints,\
    \ roughly 13.6 percent mean absolute one-day move, no directional skew) supplies\
    \ magnitude with zero directional information; breakeven for an unhedged directional\
    \ long requires p(up) greater than or equal to 0.533 after roughly 0.9 percent\
    \ all-in frictions, and nothing in the research supplies that edge. The bull's\
    \ AI-datacenter and Nvidia 800V HVDC narrative is a magnitude argument dressed\
    \ as a direction argument, and its asymmetric-payoff rebuttal was never backed\
    \ with actual call IV or skew quotes. Independently, live price data was unavailable\
    \ across four toa price NVTS --provider twelvedata attempts (HTTP 429), so no\
    \ anchor price, spread, or bar availability could be verified -- the plan is\
    \ unpriceable and therefore unfillable."
  direction: none
  confidence: 82
plan:
  ticker: NVTS
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  note: "NO TRADE. Logged due to an independent negative-EV finding (approximately\
    \ -0.9 percent net EV on an unhedged directional long, worse on the bull's\
    \ proposed short-dated call once IV crush and theta are added) plus persistent\
    \ twelvedata 429s that foreclosed any anchorable entry or exit price."
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-25T18:34:00Z'
---

## Scouted 2026-07-23T18:53:42Z

## Researched 2026-07-25T18:34:00Z

Three-round-panel debate (bull/bear/quant -> synthesizer) converged on **NO TRADE**.
See `transcript.md` for the full debate. Summary: the panel's only quantified input
was the n=2 base rate of roughly 13.6 percent mean absolute one-day move on prior
prints -- magnitude, not direction, with an enormous standard error given the sample
size. The quant's EV math for an unhedged directional long (p(up)=0.5, +/-13.6
percent, minus roughly 0.9 percent all-in costs) landed at approximately -0.9 percent
net EV, requiring p(up) greater than or equal to 0.533 to break even, which nothing
in the dossier or debate supplied. The bull argued the AI-datacenter/Nvidia 800V HVDC
narrative and a capped-loss/uncapped-upside call structure could clear that bar, but
never produced a live IV or skew quote to back it. The bear fully agreed with the
quant's NO TRADE call from Round 1 onward. Independently, `toa price NVTS --provider
twelvedata` returned HTTP 429 on all four attempts across both debate rounds, so no
anchor price or bar availability could be verified -- the plan is unpriceable
regardless of the directional call. Strongest unresolved dissent: whether p(up)=0.5
is a neutral prior or a smuggled bearish assumption, and whether the Jul 31 straddle's
implied vol actually exceeds the realized-move distribution -- unresolved because no
live option chain or spot quote was obtainable. Post-mortem check: was the actual
2026-07-28 move >= 13.6 percent, and if so was the straddle priced below it?
