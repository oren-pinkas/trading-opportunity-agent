---
id: 2026-07-14-compass-digital-key-mining-vote
title: Compass Digital SPAC votes July 15 to extend Key Mining deal deadline
status: researched
created: '2026-07-14T01:15:00Z'
event:
  type: regulatory
  summary: Compass Digital Acquisition Corp shareholders vote July 15, 2026 on a fifth
    extension (to as late as Jan 2027) to complete its merger with Key Mining Corp.
  impact_window: '2026-07-15'
tickers:
- CDAQF
sources:
- title: Compass Digital seeks SPAC deadline extension vote
  url: https://www.stocktitan.net/sec-filings/CDAQF/def-14a-compass-digital-acquisition-corp-definitive-proxy-statement-9bbdef7d1318.html
  accessed_at: '2026-07-14T01:15:00Z'
hypothesis:
  statement: 'Across three rounds the panel converged to no positive-EV trade in CDAQF.
    The July 15 vote is near-certain to pass (P approximately 0.97) because roughly
    98 percent of the voting bloc is insider-locked and dissenters exit at trust NAV
    via redemption rather than voting no, so the vote itself carries essentially zero
    tradeable information and produces no vote-day pop. The forward question, whether
    the Key Mining de-SPAC actually closes, was revised only modestly upward on S-4/A
    registration activity and prior non-redemption agreements, but those are read
    as costly signals of sponsor intent rather than evidence of survival, and the
    running 10-Q going-concern language plus a fifth extension keep the completion
    probability low (panel range roughly 0.15 to 0.40, quant midpoint 0.37). The single
    structurally valid trade, redemption arbitrage versus the approximately USD 11.82
    accreted trust NAV, is killed by a friction wall: OTC/pink-sheet round-trip cost
    of 2 to 6 percent, worsened by a very thin post-redemption float after cumulative
    redemptions of about USD 225M against a USD 200M raise, meets or exceeds any plausible
    discount to NAV, and no live/citable bid-ask ever surfaced (twelvedata returned
    HTTP 400 on CDAQF and 404 on CDAQ). With an unmeasurable and likely unfillable
    edge, blended EV rounds to zero and skews negative after the thin-float slippage
    tail, so the calibrated view is stand aside.'
  direction: none
  confidence: 87
plan:
  ticker: CDAQF
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
  dissent: 'The strongest unresolved disagreement is the P(deal closes) spread and,
    downstream of it, what a live quote would reveal. The three personas never reconciled:
    bear anchored lowest at 0.15 to 0.25, treating going-concern doubt as the dominant
    fact; quant sat at 0.37; bull nudged highest to 0.35 to 0.40 on S-4/A plus NRA
    signals. This gap was never resolved because it is orthogonal to the only executable
    trade (redemption pays NAV regardless of merger outcome), so the panel set it
    aside rather than settling it. The deeper unresolved unknown is empirical, not
    probabilistic: no persona ever obtained a live bid-ask, so whether CDAQF actually
    trades at a discount to the approximately USD 11.82 NAV wide enough to clear 2
    to 6 percent friction, and whether shares are even sourceable at that discount,
    remains untested. A future post-mortem should record that the case died on a data
    gap (no citable quote), not on a resolved probability judgment.'
  last_updated: '2026-07-16T10:54:57Z'
---

## Scouted 2026-07-14T01:15:00Z

## Researched 2026-07-16T10:54:57Z — NO-TRADE

The panel debated Compass Digital (CDAQF), a five-times-extended SPAC whose shareholders vote July 15 on a further extension to close the Key Mining merger. All three personas agreed the vote is a formality, roughly 98 percent insider-locked, low-information, and with no vote-day pop to trade, so the edge, if any, had to live in the de-SPAC completion trajectory or in redemption arbitrage versus the accreted trust NAV of about USD 11.82. The bull conceded fully by Round 2, dropping redemption arb to quant's cost math and reframing its only live idea as waiting for an S-4/A effectiveness checkpoint; the bear held firm on going-concern doubt and unresolved illiquidity; the quant re-ran the arb and found EV approximately zero, skewed negative after thin-float slippage. A structural fact defeated every version of the trade: no live or citable price for CDAQF/CDAQ ever surfaced across either round (twelvedata 400/404), making the edge unmeasurable and likely unfillable. Verdict is no-trade / pass at confidence 87, reflecting the panel's near-unanimous convergence. Full debate with citations in `transcript.md`. This is a paper-trading simulation, not financial advice.
