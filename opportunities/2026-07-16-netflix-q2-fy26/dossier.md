---
id: 2026-07-16-netflix-q2-fy26
title: Netflix Q2 FY26 earnings
status: researched
created: '2026-07-06T22:05:13Z'
event:
  type: earnings
  summary: NFLX reports Q2 FY26 after close Jul 16; guides ~$12.57B rev (+13.5% YoY),
    32.6% op margin, ad-tier scaling in focus.
  impact_window: '2026-07-16'
tickers:
- NFLX
sources:
- title: Netflix Q2 2026 earnings release set for July 16
  url: https://www.stocktitan.net/news/NFLX/netflix-to-announce-second-quarter-2026-financial-x553fsh638xh.html
  accessed_at: '2026-07-06T22:05:13Z'
hypothesis:
  statement: No forecastable edge. The NFLX Q2 FY26 guide ($12.57B rev / +13.5% YoY
    / 32.6% op margin) is Netflix's own public sandbag with no information asymmetry
    to trade; the print lands after close 7/16 so the only event exposure is a naked,
    unhedgeable overnight gap (options do not fill), and the sim price feed is a non-continuous
    per-timestamp hash with zero autocorrelation, so no intraday drift is forecastable.
    All three personas converged on NO-TRADE after each independently verified the
    stub.
  direction: neutral
  confidence: 88
plan:
  ticker: NFLX
  action: no-trade
  entry: null
  exit: null
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
  dissent: 'The simulator will FILL the bull''s discarded trade at the same deterministic
    stub values and book a +40.3% ''win'' (buy 2026-07-16T13:30Z @260.98, sell 19:59Z
    @366.25). If the simulate/post-mortem stage scores realized P/L without flagging
    that entry and exit were two independent draws from a non-continuous generator,
    a naive optimizer is pulled toward exactly this zero-edge non-trade. Unresolved:
    does the harness distinguish a fluke fill from a forecastable edge on a non-continuous
    price stub? If not, this dossier looks like a jackpot but is a landmine.'
  last_updated: '2026-07-07T23:14:33Z'
---

## Scouted 2026-07-06T22:05:13Z

## Researched 2026-07-07T23:14:33Z — NO-TRADE

Consensus NO-TRADE (bull 86 / bear 90 / quant 89; synthesis 88). Load-bearing fact, independently verified by all three personas and the orchestrator: the NFLX sim feed is a non-continuous per-timestamp deterministic hash (7/16 session: 260.98 -> 167.67 -> 106.08 -> 366.25; consecutive minutes 13:30 260.98 / 13:31 143.46 / 13:32 131.02). No autocorrelation => no forecastable intraday drift (E[drift]=0, -0.4% after costs). Earnings prints after close 7/16; options do not fill => only event exposure is a naked unhedgeable overnight gap (net EV -0.37% vs effectively-infinite adverse-tail/edge ratio; lesson-1 no-trade filter). The bull's +40% intraday 'run' is a hindsight artifact of two favorable hash draws, not an ex-ante edge. Full debate in transcript.md.
