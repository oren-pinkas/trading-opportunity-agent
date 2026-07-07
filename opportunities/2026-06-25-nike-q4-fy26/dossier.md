---
id: 2026-06-25-nike-q4-fy26
title: Nike Q4/FY2026 earnings after close June 30
status: analyzed
created: '2026-06-25T09:22:56Z'
event:
  type: earnings
  summary: Nike reports fiscal Q4 + full-year results 6/30 AFTER close; report may
    include a one-time ~$1B tariff-refund gain, EPS est ~$0.11 (down ~21% YoY). FY27
    guidance likely withheld until a fall Investor Day. Reaction trades at the 7/1
    open.
  impact_window: '2026-06-30'
tickers:
- NKE
sources:
- title: NIKE, Inc. Announces Fourth Quarter Fiscal 2026 Earnings and Conference Call
  url: https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2026/NIKE-Inc--Announces-Fourth-Quarter-Fiscal-2026-Earnings-and-Conference-Call/default.aspx
  accessed_at: '2026-06-25T09:22:56Z'
- title: Trefis — How will Nike stock react to its upcoming earnings
  url: https://www.trefis.com/stock/nke/articles/604056/how-will-nike-stock-react-to-its-upcoming-earnings-3/2026-06-23
  accessed_at: '2026-06-25T12:00:00Z'
- title: Benzinga/BofA — Why guidance matters more than earnings for Nike
  url: https://www.benzinga.com/analyst-stock-ratings/reiteration/26/06/60076842/why-this-analyst-thinks-nike-guidance-matters-more-than-earnings
  accessed_at: '2026-06-25T12:00:00Z'
hypothesis:
  statement: NKE's post-earnings reaction skews down — historically negative ~65%
    of days after the print with a median ~-6.9%, and FY27 guidance is likely withheld
    until a fall Investor Day (a setup that historically sells off). Expressed as
    a SHORT held across the 6/30 AMC print into the 7/1 open gap. Conviction is capped
    by a live positive tail — a one-time ~$1B tariff-refund EPS beat plus short-cover
    buying could produce a +10-15% squeeze against the short.
  direction: short
  confidence: 42
plan:
  ticker: NKE
  action: short
  entry:
    time: '2026-06-30T19:50:00Z'
    target_price: 41.85
  exit:
    time: '2026-07-01T13:45:00Z'
    target_price: 40.95
  expected_profit_pct: 2.0
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
  dissent: 'Un-hedgeable positive tail: a larger-than-modeled ~$1B tariff-refund EPS
    beat and/or any FY27 guidance reinstatement triggers a +10-15% short-cover gap
    against the short (Bull). Quant: net EV only ~+1.8% after costs against a ~7-8x
    adverse-tail-to-edge ratio on a naked short — rates a quarter-size position OR
    no-trade as equally defensible. Bear trimmed conviction to 60 after conceding
    short interest (~3.5-5%) is too low for a mechanical squeeze, but the tariff-beat
    EPS scenario is real.'
  last_updated: '2026-06-25T12:10:00Z'
simulation:
  ran_at: '2026-07-06T22:30:05Z'
  fills:
  - leg: entry
    planned_price: 41.85
    actual_price: 41.25
    source: https://api.twelvedata.com/time_series?symbol=NKE&interval=1min&date=2026-06-30&timezone=UTC
    fetched_at: 2026-06-30T19:50Z
  - leg: exit
    planned_price: 40.95
    actual_price: 41.48
    source: https://api.twelvedata.com/time_series?symbol=NKE&interval=1min&date=2026-07-01&timezone=UTC
    fetched_at: 2026-07-01T13:45Z
  realized_profit_pct: -0.5576
  outcome: loss
  matched_hypothesis: 'no'
postmortem:
  ran_at: '2026-07-06T23:30:00Z'
  root_cause: priced-in
  lessons:
  - Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
    ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express
    such earnings gap-shorts via defined-risk options, never a naked short.
  - 'Discount post-earnings negative base rates when the name is already at/near its
    52-week low: most of the drawdown is priced in and a benign or one-time-beat print
    flips the reaction positive.'
---

## Scouted 2026-06-25T09:22:56Z

## Researched 2026-06-25T12:10:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real price
~$41.8 near the 52-week low ($41.31), NOT the stub's $76.85. The panel converged on
a low-conviction SHORT held across the after-close print into the 7/1 open gap: the
base rate (down ~65% of prints, median -6.9%; last two prints -20% and -15.5%) and
likely FY27 guidance withholding outweigh the one-time tariff-refund narrative, but
a tariff-beat + short-cover squeeze is a live positive tail that caps confidence at
42. Full debate with citations in `transcript.md`.

---
### Revision 2026-07-06T22:30:05Z
Simulated NKE short: -0.5576% (loss, matched=no)

---
### Revision 2026-07-06T23:30:00Z
Post-mortem: priced-in
