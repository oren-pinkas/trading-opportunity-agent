---
id: 2026-07-14-deutsche-bank-q2-fy26
title: Deutsche Bank reports Q2 2026 earnings July 29
status: researched
created: '2026-07-14T01:15:00Z'
event:
  type: earnings
  summary: Deutsche Bank reports Q2 FY26 results July 29, 2026, amid a strong run
    for European bank earnings this cycle.
  impact_window: '2026-07-29'
tickers:
- DB
sources:
- title: Deutsche Bank Aktiengesellschaft Q2 2026 Earnings Report
  url: https://www.marketbeat.com/earnings/reports/2026-7-29-deutsche-bank-aktiengesellschaft-stock/
  accessed_at: '2026-07-14T01:15:00Z'
hypothesis:
  statement: DB enters the 2026-07-29 print already extended, up USD 14.1 percent
    over six weeks (USD 31.71 on 2026-06-01 to USD 36.195 on 2026-07-15, twelvedata
    real prints, still accelerating into the last week), with no DB-specific
    non-priced catalyst identified. Bull's three pillars - the sub-65 percent
    cost-income trajectory, CET1-funded buybacks, and "standout" FIC trading -
    are the most-discussed, already-in-the-tape storylines, asserted by Bull but
    unsourced (the dossier itself carries only a MarketBeat earnings-calendar
    link, no consensus EPS, cost-income ratio, CET1 level, or peer comp data).
    Bear and Quant converged independently on no_trade via different methods -
    Bear qualitatively (priced-in sector-cycle narrative, litigation/legacy
    overhang, volatile FIC comps, EUR-USD ADR translation risk, capital-return
    "sell the news" risk on an already-extended rally) and Quant quantitatively
    (naked directional long nets roughly -0.43 percent EV at P(up)=0.52, still
    only about +0.08 percent net EV even at an optimistic P(up)=0.58, both far
    under the approximately 2 percent no-trade threshold). Quant's EV moved
    further negative, to roughly -0.85 percent, once Bear's fuller six-week
    price-run framing was incorporated (steeper downside skew, not a wider base
    move). Bull conceded the priced-in critique in rebuttal and downgraded from
    a naked long/calls proposal to, at most, a small contingent defined-risk call
    spread pending pre-print confirmation of consensus estimates and the
    options-implied move - data this session could not obtain (no working web
    search or options access for any persona).
  direction: no_trade
  confidence: 78
plan:
  ticker: DB
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: null
  note: No long - naked directional long has negative expected value at every
    tested up-probability through 0.58, the proposed entry (USD 36.20-36.50) sits
    within about 1 percent of the last real print with no dip bought (chasing an
    extended rally into a binary event), and the proposed USD 34.50 stop does not
    protect against the actual tail risk (a litigation/provision gap or EUR-USD
    ADR translation move can gap past a mechanical stop overnight). No defined-risk
    spread (bull's call spread or bear's "sell the news" put spread) can be sized
    responsibly without the options-implied move and sell-side consensus data
    this session lacked - sizing either would be a guess, not a trade.
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
  dissent: Bull's contingent case is unrefuted, only unverifiable this session.
    It would be correct if pre-print sourcing showed (a) consensus EPS/RoTE set
    materially below management's own cost-income target trajectory (a low bar
    DB can clear), and (b) an options-implied move priced cheap relative to the
    approximately 4.5 percent base-rate single-day move - making a defined-risk
    August call spread (roughly USD 37 long / USD 39-40 short) positively convex.
    Both conditions require sell-side consensus and options data no persona could
    access this session. Action item - re-run this opportunity only after
    obtaining verified consensus EPS/RoTE, cost-income and CET1 figures, and the
    options-implied move; absent those, no_trade stands.
  lessons_applied:
  - NKE confidence/EV no-trade filter (session 2026-07-06)
  - DAL priced-in-run no-trade filter (session 2026-07-12)
  - LEVI no-manufactured-position filter (session 2026-07-12)
  last_updated: '2026-07-16T11:02:44Z'
---

## Scouted 2026-07-14T01:15:00Z

## Researched 2026-07-16T11:02:44Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 78/100
confidence. Bear and Quant converged independently - Bear on priced-in sector
narrative plus litigation/FX/capital-return tail risk, Quant on negative EV
(roughly -0.43 percent, worsening to roughly -0.85 percent after adopting Bear's
fuller six-week run-up framing) - and Bull conceded the priced-in critique in
rebuttal, downgrading from a naked long to, at best, a small contingent
defined-risk spread pending consensus/options data this session could not
obtain. No position taken; re-run gated on real consensus EPS/RoTE and
options-implied-move data. Full transcript: `transcript.md`.
