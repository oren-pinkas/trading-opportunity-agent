---
id: 2026-07-16-onex-westjet-strike-deadline
title: Onex faces WestJet strike deadline after 99% strike-authorization vote
status: scouted
created: '2026-07-16T07:53:17Z'
event:
  type: economic
  summary: WestJet flight attendants voted 99% to authorize a strike; a 21-day cooling-off
    period puts a legal strike date as early as Aug 2, 2026, exposing owner Onex Corp
    to disruption at its airline holding.
  impact_window: '2026-08-02'
tickers:
- ONEX
sources:
- title: Union representing WestJet says 99 per cent of members voted for strike
  url: https://www.cp24.com/video/2026/07/15/union-representing-westjet-says-99-per-cent-of-members-voted-for-strike/
  accessed_at: '2026-07-16T07:53:17Z'
hypothesis:
  statement: "A 99% WestJet flight-attendant strike-authorization vote (earliest legal strike 2026-08-02) will move Onex Corp (ONEX) stock, but authorization votes are typically settlement leverage with a low base rate of actual strikes, WestJet is only a single-digit-to-low-teens percent of Onex's diversified NAV, and Canadian back-to-work precedent further caps downside - leaving no reliable directional edge."
  direction: none
  confidence: 20
plan:
  ticker: ONEX
  action: skip
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  strategy: three-round-panel
  personas: [bull, bear, quant]
  dissent: "Whether thin sell-side coverage of ONEX creates a genuine mispricing the market hasn't discounted (bull's residual point) versus that same illiquidity simply meaning wide spreads that swallow any edge (bear/quant) - unresolved, though moot given the missing price feed."
  overall_confidence: 88
  last_updated: '2026-07-22T13:02:09Z'
status: researched
---

## Scouted 2026-07-16T07:53:17Z

## Researched 2026-07-22T13:02:09Z

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) converged on
**skip**. Blocking issue #1: `toa price` returns HTTP 404/400 for ONEX/ONEX.TO/ONEX:TSX via
the twelvedata provider - no verifiable, fillable price feed exists for this ticker, so no
entry/exit can be marked or reproduced. Blocking issue #2: even setting tradability aside,
quant's EV calculation (P(strike)=18%, WestJet=10-20% of Onex NAV, -1.5%/+0.3% move
assumptions) comes out to roughly -0.02%, and stays within -0.15% to +0.12% across a
P(strike) sensitivity range of 10-25% - inside round-trip transaction costs on an illiquid
TSX name in every case. Bull conceded both points by round 2 (confidence 55-60% -> 25%).
Full transcript: [transcript.md](./transcript.md).
