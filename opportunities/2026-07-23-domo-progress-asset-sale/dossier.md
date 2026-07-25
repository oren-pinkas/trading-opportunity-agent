---
id: 2026-07-23-domo-progress-asset-sale
title: Domo sells assets to Progress Software for USD 400 million, becomes cash shell
status: researched
created: '2026-07-23T21:02:37Z'
event:
  type: earnings
  summary: Domo agreed to sell substantially all operating assets to Progress Software
    for USD 400 million cash, leaving a debt-free public shell with roughly USD 246
    million net cash and over USD 900 million in tax-loss assets; deal expected to
    close before Progress's fiscal year end Nov 30 2026
  impact_window: '2026-11-30'
tickers:
- DOMO
- PRGS
sources:
- title: Why Is Domo (DOMO) Stock Rallying Over 23% After Hours Today? - Benzinga
  url: https://www.benzinga.com/markets/equities/26/07/60628806/why-is-domo-domo-stock-rallying-over-23-after-hours-today
  accessed_at: '2026-07-23T21:02:37Z'
hypothesis:
  statement: 'Domo''s sale of its operating assets to Progress Software for USD 400
    million cash converts DOMO into a debt-free cash shell (roughly USD 246 million
    stated net cash, over USD 900 million in NOLs), but the panel could not verify
    the one number the thesis depends on -- diluted net-cash-per-share -- so no
    mispricing was ever established. The market had a full liquid session to price
    the deal and marked DOMO down net (open +4.0% to USD 4.0299, close -5.5% to
    USD 3.66 vs the USD 3.875 pre-announcement print), which is completed price
    discovery, not an unnoticed NAV gap. Shell base rates (10-30% discounts to net
    cash persisting for quarters, NOLs worth roughly 0-10 cents per dollar under
    Section 382, unquantified wind-down/tax/public-company costs against gross
    stated cash) plus unresolved deal-completion risk (shareholder vote, possible
    regulatory review, no disclosed breakup fee or MAC terms, roughly a 4-month
    runway to Progress''s Nov 30 2026 fiscal year end) mean neither a computable
    edge nor a defined-risk expression exists. The long fails on cost/EV arithmetic
    (net approximately -0.3% over 5-10 days) and on the absence of a verified NAV
    gap over any horizon; the short fails on a roughly 14x tail ratio versus a 7-8x
    threshold with no usable options chain. PRGS carries zero confirming accretion
    data and prices as noise.'
  direction: neutral
  confidence: 85
plan:
  ticker: DOMO
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-25T08:21:06Z'
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
  verdict: no-trade
  confidence: 85
  lessons_applied:
  - '2026-06-25-nike-q4-fy26: conf<=45 + net EV<2% + tail/edge>>7-8x is a no-trade
    filter, not a size-down -- applied to the DOMO short (~14x tail ratio, no
    options chain to express defined-risk)'
  - '2026-06-26-delta-q2-fy26: a catalyst that already drove a run is priced in --
    applied to the AH +23% print, which fully reversed to a net loss within the
    next regular session (open +4.0%, close -5.5% vs pre-announcement)'
  - '2026-07-02-levi-q2-fy26: when the quant says directional EV is ~0/negative,
    log NO TRADE rather than manufacture a minimal directional position for the
    learning loop -- applied directly; no token starter position was booked'
  - '2026-07-02-levi-q2-fy26: anchor entry prices to a live quote at the actual
    entry timestamp, not a stale pre-move reference -- the bull''s R1 framing
    anchored to the stale USD 3.875 pre-announcement print and was corrected in
    R2'
  dissent: 'Bull''s residual case: a small starter long becomes rational only if
    three checkable conditions are confirmed -- (1) verified diluted net-cash-per-share
    meaningfully above the current price (bull''s unconfirmed ~24-25M share
    estimate implies ~USD 10/share against a USD 3.66 close), (2) a committed
    return-of-capital mechanism (declared special distribution or formal
    liquidation plan, not open-ended reinvestment/reverse-merger discretion), and
    (3) a dated re-rating catalyst (record date, vote date, or stated distribution
    timeline). Quant and bear do not concede even if all three land: quant notes
    that even a verified 15-20% NAV gap only reaches EV~=0 once a ~12% deal-break
    probability at a ~-30% break-case gap is priced in, and that the NAV-gap
    condition is negatively correlated with the NOL sweetener (a reverse merger
    that monetizes the NOLs triggers a Section 382 ownership change that impairs
    them). Bear notes deal-completion risk (no disclosed breakup fee, MAC clause,
    or antitrust/CFIUS terms) and forced-selling risk (DOMO ceasing to screen as
    an operating company for small-cap mandates) are independent of any pricing
    resolution and cannot be hedged given the absence of a usable options chain.'
  transcript: transcript.md
---

## Scouted 2026-07-23T21:02:37Z

## Researched 2026-07-25T08:21:06Z
Verdict: NO-TRADE (neutral, confidence 85). Three-round panel (bull/bear sonnet,
quant opus; synthesizer opus). Verified prices (twelvedata): DOMO USD 3.875 on
2026-07-23 15:00 UTC (pre-announcement), USD 4.0299 at the 2026-07-24 13:31 UTC
open (+4.0%), USD 3.66 at the 2026-07-24 19:59 UTC close (-5.5% vs
pre-announcement, -9.2% off the open); PRGS USD 37.48 pre-announcement. The
headline "+23% after hours" pop fully reversed within the next regular session --
a completed price-discovery event, not an unnoticed NAV gap. Bull's terminal-value
thesis (USD 246 million net cash plus USD 900 million+ NOLs against DOMO's market
cap) could not be priced because no diluted share count / net-cash-per-share
figure was verified by any panelist; bull downsized from an accumulation-style
long to a small conditional starter position in Round 2. Quant's EV: DOMO long
over 5-10 days nets approximately -0.3% after costs; DOMO short nets
approximately -1.5% to -1.7% with a ~14x adverse-tail-to-edge ratio (vs a 7-8x
no-trade threshold) and no usable options chain to express defined-risk; PRGS
nets approximately 0, noise. Full transcript in transcript.md.
