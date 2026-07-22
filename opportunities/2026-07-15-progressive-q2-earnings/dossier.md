---
id: 2026-07-15-progressive-q2-earnings
title: Progressive Q2 FY26 Earnings
status: researched
created: '2026-07-14T05:08:14Z'
event:
  type: earnings
  summary: Progressive reports Q2 2026 results Jul 15, testing whether its underwriting-margin
    lead over peers holds up
  impact_window: '2026-07-15'
tickers:
- PGR
sources:
- title: Earnings Calendar and Analysis for This Week (July 13-17) | Kiplinger
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-14T05:08:14Z'
hypothesis:
  statement: PGR reports monthly underwriting results via 8-K, so the Q2 quarterly
    print on 2026-07-15 pre-releases roughly two of the quarter's three months and
    structurally compresses the quarterly-day surprise. Reference price USD 226.35
    at 2026-07-14T19:55Z followed a roughly 2.2 percent intraday fade into the
    print (opened USD 230.98, closed USD 225.81), consistent with distribution
    rather than clean momentum. The quant's expected-value model (gross about plus
    0.046 percent, net about minus 0.07 percent flat-magnitude; about minus 0.5
    percent under a give-back magnitude skew) went essentially unrebutted; the
    bull conceded his 60 to 63 confidence was narrative rather than calibrated and
    withdrew the call-spread trade, and the bear conceded the priced-for-perfection
    thesis is a real risk-management read but not a quantified directional edge
    (no evidence P-down exceeds 0.57). All three panelists converged on NO TRADE by
    round 2.
  direction: no_trade
  confidence: 80
plan:
  ticker: PGR
  action: pass
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
  dissent: The quant's give-back magnitude skew (P-up 0.50 at plus 2.0 percent,
    P-down 0.50 at minus 3.0 percent) implies the mirror short or put-spread
    structure carries a roughly plus 0.5 percent gross positive lean, corroborated
    by the bear's priced-for-perfection thesis and the confirmed intraday fade
    into the print (USD 230.98 open to USD 225.81 close on 2026-07-14). All three
    panelists killed the trade because confidence in that downside asymmetry sat
    under 45, below the NKE no-trade-filter bar, and no hard evidence established
    P-down above 0.57 -- but the asymmetry was never disproven, only deemed
    insufficiently confident. Worth revisiting with better data (options
    skew/IV term structure, historical post-monthly-disclosure quarterly-day
    return distribution) to see whether confidence could clear the threshold and
    convert this from a no-trade into a defined-risk short.
  last_updated: '2026-07-22T07:45:00Z'
---

## Scouted 2026-07-14T05:08:14Z

## Researched 2026-07-22T07:45:00Z -- NO TRADE

Three-round panel debate (bull/bear/quant, synthesized by opus). Bull opened long
via a defined-risk call spread (confidence 60-63/100), framing the Jul 15 print as a
confirmation event given PGR's monthly 8-K disclosure cadence and YTD momentum
(USD 213.63 on 2026-01-02 to USD 230.98 at the 2026-07-14 open). Bear opened
cautious/short-leaning, citing a priced-for-perfection setup after a roughly 15
percent one-month run and a same-week pullback (USD 234.09 close on 2026-07-13 to
USD 225.81 close on 2026-07-14). Quant opened NO TRADE in round 1: PGR's monthly
disclosure structurally compresses the quarterly-day surprise, so P(up) about 0.51
against a symmetric roughly 2.3 percent move nets to about minus 0.07 percent after
costs -- no evidentiary basis for the roughly 0.57 P(up) needed to clear the bar. By
round 2 the bull conceded the EV math and withdrew the call spread; the bear
resolved a cross-persona price discrepancy (open USD 230.98 vs close USD 225.81,
both real, different timestamps) confirming a roughly 2.2 percent intraday fade
into the print, but also conceded the quant's math undercut his own short-bias lean
absent a quantified edge. Quant re-ran EV with a give-back magnitude skew
(long EV drops to about minus 0.5 percent) but held confidence in that skew under
45, below the NKE no-trade-filter bar. Verdict: no_trade, confidence 80. Full
transcript in `transcript.md`. Central dissent: the give-back skew implies a small
positive-EV lean for a defined-risk short, but confidence in that asymmetry never
cleared the trade bar -- worth revisiting with options-skew or historical
post-monthly-disclosure return-distribution data.
