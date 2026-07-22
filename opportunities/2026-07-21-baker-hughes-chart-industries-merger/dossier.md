---
id: 2026-07-21-baker-hughes-chart-industries-merger
title: Baker Hughes-Chart Industries merger EU clearance
status: scouted
created: '2026-07-21T13:14:56Z'
event:
  type: regulatory
  summary: BKR/GTLS merger awaits EU Phase I clearance with limited commitments; deal
    expected to close July 2026
  impact_window: '2026-07-31'
tickers:
- BKR
- GTLS
sources:
- title: Chart Industries Nears EU Approval for Baker Hughes Merger
  url: https://www.tipranks.com/news/company-announcements/chart-industries-nears-eu-approval-for-baker-hughes-merger
  accessed_at: '2026-07-21T13:14:56Z'
status: researched
hypothesis:
  statement: 'The BKR/GTLS merger is very likely to close (EU Phase I clearance
    with limited/behavioral remedies is a genuine positive signal), but the
    GTLS spread-capture trade as specified is not tradeable: the live GTLS
    price/spread is unverified (provider returned HTTP 400 for GTLS at every
    timestamp tried) and US antitrust (HSR/DOJ-FTC) status is unconfirmed.
    Under a reasonable P(close) haircut (about 0.87, decomposing EU about 0.97
    times US about 0.90-0.93 times other about 0.98) the panel''s EV estimate
    goes negative (about negative 1.5 percent at a 1.0 percent spread, about
    negative 1.0 percent at a 1.5 percent spread) at any plausible observed
    spread. High confidence the deal closes; low confidence there is a
    positive-EV edge after costs given unobservable inputs. Reference price
    USD 55.88 for BKR (twelvedata, 2026-07-21T15:30Z); no GTLS price could be
    obtained.'
  direction: none
  confidence: 78
plan:
  ticker: GTLS
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-22T19:56:51Z'
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: 'The strongest unresolved disagreement is the bull''s residual
    BKR-only long: a reduced-size directional bet on BKR (USD 55.88, the only
    confirmed price) as a "good business getting better via deal completion,"
    decoupled from the GTLS spread. The bull dropped to 35 percent confidence
    and abandoned GTLS spread-capture but continued to defend this narrower
    idea. It was never tested by the bear or quant, who stayed focused on
    refuting the arb setup, so no EV estimate, valuation basis, or catalyst
    was ever attached to it. It survives only by not having been examined,
    not by having been validated. Future post-mortem should note whether
    decoupling from the spread genuinely removes deal-break exposure, or
    merely relabels the same completion-and-antitrust risk the panel flagged
    as unresolved.'
---

## Scouted 2026-07-21T13:14:56Z

## Researched 2026-07-22T19:56:51Z

Three-round panel (bull/bear/quant) converged on NO TRADE. BKR confirmed at
USD 55.88 via twelvedata (2026-07-21T15:30Z); GTLS intraday price was NOT
obtainable — the provider returned HTTP 400 for GTLS at every timestamp
tried, so the actual arb spread was never observed.

Bull opened bullish on EU Phase I clearance with limited (non-divestiture)
remedies as a strong completion signal, proposing long GTLS primary plus a
smaller long BKR secondary (confidence 65/100), while explicitly flagging the
missing GTLS price. Bear opened skeptical (confidence 70/100 that this is not
a good tradeable setup), arguing the clearance narrative is already priced in
by arb desks, that unconfirmed US antitrust (HSR/DOJ-FTC) status is the more
binary domestic risk EU clearance says nothing about, and warning against
mapping "expected close July 2026" directly onto the 2026-07-31 impact window
without a confirmed valid-session catalyst. Quant opened with an EV
calculation assuming (unverified, from the source article) roughly USD
210/share cash consideration, P(close)=0.95, a 1.0 percent spread, and an 18
percent break-downside — yielding an economically zero EV of +0.05
percent/share that does not clear costs (confidence 55/100).

In rebuttal, bull conceded the missing-spread and overweighted-EU-clearance
critiques were fair and dropped confidence to 35/100, abandoning GTLS
spread-capture but floating an unvetted BKR-only directional long as a
narrower residual idea. Bear held firm (confidence 75/100), arguing quant's
"improved" EV case only appears by stacking two unverified favorable
assumptions, and that BKR acquiring a US industrial-gas/equipment target is
exactly the profile that invites independent DOJ/FTC scrutiny. Quant conceded
the P(close)=0.95 base rate silently assumed all jurisdictions were trending
clear; decomposing EU/US/other risk separately haircuts P(close) to about
0.87, which flips the EV calculation to roughly negative 1.47 percent/share —
negative at the point estimate (confidence 80/100 not tradeable as
specified).

All three personas converged on NO TRADE by Round 2-3. Revisit only if a live
GTLS quote confirms a spread of at least 1.5 percent against confirmed cash
terms, US HSR/DOJ-FTC clearance is confirmed (restoring P(close) to at least
0.95), and a valid-session catalyst (not a mechanical 2026-07-31 mapping)
governs the exit. Full debate transcript recorded in `transcript.md`.
