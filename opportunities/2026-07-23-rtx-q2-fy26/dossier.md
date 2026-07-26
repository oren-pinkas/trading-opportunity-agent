---
id: 2026-07-23-rtx-q2-fy26
title: RTX Q2 2026 Earnings
status: researched
created: '2026-07-23T01:19:37Z'
event:
  type: earnings
  summary: RTX reports Q2 2026 results with consensus EPS of $1.66, up 36% YoY on
    defense/aero demand
  impact_window: '2026-07-23'
tickers:
- RTX
sources:
- title: RTX Q2 2026 Earnings Preview - Alphastreet
  url: https://news.alphastreet.com/rtx-q2-2026-earnings-preview-july-23-street-expects-1-66-eps/
  accessed_at: '2026-07-23T01:19:37Z'
hypothesis:
  statement: >-
    RTX's Q2 2026 beat-and-raise (adj EPS USD 1.89 vs USD 1.66 consensus, revenue
    USD 24.71B +14.5% YoY, FY26 guide lifted to adj EPS USD 7.10-7.25 / sales USD
    95-96B, record USD 289B backlog) was fully discharged into price in a single
    overnight gap. Verified price decomposition (toa price, twelvedata): USD 194.60
    (2026-07-22 19:59Z, pre-print close) to USD 208.61 (2026-07-23 13:35Z,
    post-gap open) is a +7.20% gap; USD 208.61 to USD 209.10 (2026-07-23 19:59Z
    close) is only +0.24% intraday continuation on the print day itself; USD
    209.10 to USD 213.05 (2026-07-24 19:59Z close) is +1.89% day-2 drift.
    Cumulative move +9.48%, leaving the stock 0.68% below its new 52-week high of
    USD 214.50 and ~6.5% below the sell-side consensus target of USD 226.82 —
    a target that Baird (USD 240), Susquehanna (USD 245), BofA (USD 235), and
    Wells Fargo (USD 230) all published before the day-2 move, meaning the
    revision re-rate the bull wanted to ride was already reflected in price, not
    still ahead of it. Explicit EV math at every horizon a fresh entry (3 days
    after the print) could realistically hold: at 1-3 days, net EV +0.075% (7bps
    after ~13bps round-trip costs) against a 2-sigma adverse tail of -4.0%, a
    ~53x tail-to-edge ratio; even stretched to the bull's proposed 7.5-day
    horizon, net EV +0.74% against an 8.8% 2-sigma tail is still ~11.9x: both
    far past the ~7-8x institutional no-trade filter. Solving for the horizon
    that clears the filter requires ~18 trading days, which abandons the
    event-trade thesis entirely and bleeds into the Q3 print. The fundamental
    story (backlog, guide raise, margin trajectory) may well be correct; a
    correct view already fully priced in three days ago is not a trade.
  direction: none
  confidence: 76
plan:
  ticker: RTX
  action: no_trade
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
  dissent: >-
    Two unresolved items worth flagging for post-mortem. (1) The forward view
    rests on a single post-event session: 2026-07-23 was a Thursday, 2026-07-24
    Friday was the only full post-gap trading day before research ran on
    2026-07-26 (a weekend), so the quant's posterior drift estimate of
    0.116%/day is a heavy Bayesian shrink of one 1.89% observation (classified
    1.18-sigma, i.e. statistical noise). Whether day-2 was "consumption of the
    catalyst" (bear/quant's read) or "leg one of a breakout" (would require the
    stock to clear USD 214.50) cannot be separated from a two-session sample.
    The quant logged an explicit trip-wire: 3+ consecutive continuation days
    would raise the shrinkage weight enough to flip this toward a small starter
    long — testable only from 2026-07-29 onward. (2) An unreconciled price
    discrepancy: the bear's Round 1 opening cited "~USD 209.16 by 2026-07-26"
    while the quant independently verified a USD 213.05 close on 2026-07-24 (a
    1.9% gap between two personas' spot anchors), never challenged or
    reconciled in Round 2. Since 07-25/07-26 are a weekend, USD 213.05 is the
    correct last print; the bear's figure was likely a stale event-day quote.
    This means the bear reached the correct verdict off a wrong number — the
    real gap to the 52-week high was 0.68%, not 2.5%, which if anything
    strengthens the bear's stretched-valuation case, but the unchallenged
    cross-persona discrepancy is itself a process gap: three-way agreement is
    weaker evidence when the underlying anchors silently disagree by 1.9%.
    Post-mortem action: check whether RTX broke USD 214.50 on 2026-07-27/28; if
    it broke out convincingly, the panel's "gap-and-stall" read was a two-session
    sampling artifact rather than a property of the event.
  last_updated: '2026-07-26T01:12:34Z'
---

## Scouted 2026-07-23T01:19:37Z

## Researched 2026-07-26T01:12:34Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). No RTX-specific
lessons in institutional memory; generic earnings-trade lessons applied instead. RTX
reported Q2 2026 on 2026-07-23: adj EPS USD 1.89 vs USD 1.66 consensus (+13.9% beat),
revenue USD 24.71B (+14.5% YoY, +16% organic), FY26 guide raised to adj EPS USD
7.10-7.25 (from USD 6.70-6.90) and sales USD 95-96B, record USD 289B backlog. Verified
price series via `toa price RTX --provider twelvedata`: USD 194.60 (07-22 19:59Z
pre-print close) to USD 208.61 (07-23 13:35Z post-gap open, +7.20%), to USD 209.10
(07-23 19:59Z close, +0.24% intraday continuation) to USD 213.05 (07-24 19:59Z close,
+1.89% day-2 drift) — cumulative +9.48%, 0.68% below the new 52-week high of USD
214.50. BULL opened long on the beat-and-raise thesis (confidence 55) but fully
conceded in Round 2 after seeing the quant's EV math, dropping to confidence 40 on
NO-TRADE: never modeled the 5-10 day drift thesis quantitatively, and a defined-risk
call spread doesn't fix the tail-ratio problem since it pays vol premium against
~zero expected edge. BEAR held NO-TRADE throughout (confidence 30 to 45), noting
sell-side already re-rated targets (Baird USD 240, Susquehanna USD 245, BofA USD
235, Wells Fargo USD 230; consensus USD 226.82) before the day-2 move — the
"analyst-revision drift" the bull wanted to ride was already in the price. QUANT
(confidence 72 to 78) ran the decisive numbers: gross EV +0.205% at a 1-3 day
horizon, net +0.075% (7bps) after ~13bps round-trip costs, against a 2-sigma adverse
tail of -4.0% (~53x tail-to-edge ratio, versus the 7-8x institutional no-trade
filter). Re-run at the bull's proposed 7.5-day horizon: net EV +0.74% against an
8.8% tail, ~11.9x — still fails. Clearing the filter requires ~18 trading days,
which is no longer an event trade and bleeds into the Q3 print; the bull's proposed
3-4% trailing stop would also likely be triggered by pure noise (~55-65% first-
passage probability within 10 days) before any drift plays out. Verdict: NO-TRADE,
confidence 76. Would flip only with 3+ consecutive continuation days confirming
real (not noise) drift, or a convincing breakout above USD 214.50. Full debate in
`transcript.md`.
