---
id: 2026-07-16-june-retail-sales
title: June 2026 Advance Retail Sales report
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: macro
  summary: Census Bureau releases June 2026 Advance Monthly Retail Sales on Jul 16,
    a read on consumer spending strength heading into H2.
  impact_window: '2026-07-16'
tickers:
- XRT
sources:
- title: When Is the Next US Retail Sales Report? - Finance Calendar
  url: https://www.financecalendar.com/us-retail-sales/
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: >-
    Researched at T+6 trading days post-print (today 2026-07-22 vs event
    2026-07-16), all three seats agree the June retail-sales catalyst itself
    offers no tradeable edge in XRT: the only clean signal was a +0.4%
    report-day pop (USD 89.94 to USD 90.31), and the subsequent drift to
    USD 88.49 by T+3 is real but unattributable from price alone -- both a
    "good headline, weak internals" read and a "mixed print, delayed fade"
    read fit the same four data points, which the bear correctly flagged as
    disqualifying. The quant's EV calc for the print-specific trade was
    decisive: P(edge live at T+6) ~12%, EV_net ~-0.09% after ~15bps
    round-trip costs, negative even at double the assumed probability. A
    separate reframe -- an oversold-bounce-into-Q2-retailer-earnings trade --
    was proposed by the bull and priced hypothetically by the quant as
    marginally EV-positive (~+0.19%), but rests on an assumed, not measured,
    ~50% mean-reversion base rate, with no XRT-vs-SPY relative-performance
    check, no confirmed TGT/WMT earnings dates, and no historical base-rate
    study completed within this debate. Actioning that idea now would
    misrepresent it as a researched trade when it is not.
  direction: none
  confidence: 78
plan:
  ticker: XRT
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
  dissent: >-
    Quant priced the reframed oversold-bounce-into-earnings trade at
    marginally positive EV (~+0.19%, R:R ~1.6:1) and would permit it at
    <0.25% of book as a pure technical stop/target trade, whereas the bear
    (and this synthesis) holds that a positive EV resting on an assumed,
    unmeasured ~50% base rate is indistinguishable from noise net of costs,
    and that actioning an idea which fails its own stated validation
    prerequisites (relative-performance check, earnings-date confirmation,
    historical base-rate study) corrupts the "researched trade" record. If
    the assumed base rate is roughly right, standing aside forfeits a small
    real edge; if not, entering would have logged a fluke. Testable
    post-mortem: did XRT actually bounce off the ~USD 88.50 area into
    Q2 retailer earnings, and would a relative-performance check have called
    it in advance?
  last_updated: '2026-07-22T11:55:00Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-22T11:55:00Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run at T+6
trading days post-print. XRT price path: USD 89.94 (pre-print, 7/16) -> USD 90.31
(report-day close, +0.4%) -> USD 89.32 (T+1) -> USD 88.49 (T+3, -2.0% from
report-day close). All three personas agreed the print-driven catalyst is dead:
bear's circularity point (the same four price points fit both a "good-but-shrugged"
and a "mixed-and-faded" read) was never rebutted, and the quant's EV_net of -0.09%
for the print trade held even under generous sensitivity. The bull's reframed
oversold-bounce-into-Q2-earnings idea was priced by the quant as marginally
EV-positive (~+0.19%) but was built on an assumed, not measured, ~50% reversion
base rate with none of its own stated prerequisites (XRT/SPY relative-performance
check, confirmed earnings dates, historical base-rate study) actually completed.
Verdict: NO-TRADE (not scheduled, not simulated). The bounce idea is a candidate
for a future, separate research pass, not an actionable trade from this debate.
Full debate with citations in `transcript.md`.
