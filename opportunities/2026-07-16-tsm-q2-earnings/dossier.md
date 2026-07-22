---
id: 2026-07-16-tsm-q2-earnings
title: TSMC Q2 2026 earnings report
status: researched
created: '2026-07-16T03:59:59Z'
event:
  type: earnings
  summary: TSMC reports Q2 2026 results on 2026-07-16 as a bellwether for AI chip
    demand after the recent chip selloff
  impact_window: '2026-07-16'
tickers:
- TSM
sources:
- title: TSMC Earnings Preview - Investing Engineer
  url: https://investingengineer.com/tsmc-earnings-preview-july-16-2026/
  accessed_at: '2026-07-16T03:59:59Z'
- title: "TSMC Reports Second Quarter EPS of NT$27.25 (TSMC investor relations)"
  url: https://pr.tsmc.com/english/news/3326
  accessed_at: '2026-07-22T17:35:30Z'
- title: "TSMC to invest additional USD 100 billion in Arizona after second-quarter profit soars 77% - CNBC"
  url: https://www.cnbc.com/2026/07/16/tsmc-second-quarter-profit-.html
  accessed_at: '2026-07-22T17:35:30Z'
- title: "TSMC (TSM) Breaks Q2 2026 Records, Then Falls 5 percent: Reason Explained - TradingKey"
  url: https://www.tradingkey.com/analysis/stocks/us-stocks/262036881-tsmc-tsm-breaks-q2-2026-records-tradingkey
  accessed_at: '2026-07-22T17:35:30Z'
hypothesis:
  statement: "TSMC's Q2 2026 beat-and-raise (revenue USD 40.20B +36 percent YoY,
    EPS ~USD 4.31/ADR beating consensus by ~12-13 percent, FY guidance raised) was
    genuinely strong, but the market's two-way reaction has already fully played
    out: a sell-the-beat drop on capex/FCF-overhang concerns to a USD 397.63 trough
    (7/17), then a full mean-reversion to USD 425.07 (7/21) that faded to USD 417.52
    by 7/22 (now) -- a net move of roughly -0.4 percent versus the true USD 419.40
    pre-earnings reference. With the catalyst spent, no fresh forward driver in the
    tape, and every panel-tested trade structure (long, short, options) pricing to
    negative net EV after costs, there is no tradeable edge left in this event."
  direction: none
  confidence: 82
plan:
  ticker: TSM
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
  dissent: "Whether the 7/21 reversal to USD 425.07 was TSM-specific alpha (fundamental
    re-rating on the beat-and-raise) or merely sector beta (a bounce in the broader
    Philly Semi Index that TSM rode). The bull conceded he could not yet distinguish
    the two and flagged it as his largest open risk; the quant priced P(win) at only
    ~25 percent on a continuation trade precisely because the reversal faded into
    7/22 rather than extending, but that fade is equally consistent with either
    explanation. Resolving it needs data the panel did not have: TSM-vs-SOX relative
    performance, volume/flow confirmation of a break above USD 425.07 or below
    USD 397.63, and any forward capex/FCF guidance revision."
  last_updated: '2026-07-22T17:35:30Z'
---

## Scouted 2026-07-16T03:59:59Z

## Researched 2026-07-22T17:35:30Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), judged strictly
on this opportunity's own merits. TSMC's Q2 2026 print (7/16) was a genuine
beat-and-raise: revenue USD 40.20B (+36 percent YoY), EPS ~USD 4.31/ADR (+77.4 percent
YoY, ~12-13 percent above consensus), FY2026 and Q3 guidance raised, alongside a
capex raise to USD 60-64B and an incremental USD 100B Arizona pledge. The stock sold
off to a USD 397.63 trough (7/17) on capex/FCF-overhang concerns amid a broader
Philly Semi Index correction, then fully reversed to USD 425.07 (7/21) -- above the
true USD 419.40 pre-earnings reference -- before fading to USD 417.52 by 7/22 (now).
The QUANT's verified toa/twelvedata price series was decisive: because the round
trip is already complete and reference-price-independent, every structure (Bull's
downsized long to USD 450-470, a short, or an options play) priced to roughly zero
or negative net EV after costs. The BULL started at 62/100 confidence LONG and
conceded to 48/100 with a downsized, defined-risk structure once shown the move he
wanted to catch had already happened before any real fill. The BEAR corrected an
own-goal (mislabeled trough date, stale price anchor) but held NO-TRADE at 58/100
via unhedgeable tail risk (export-control/geopolitical, customer concentration,
sector de-rating). Verdict: NO-TRADE (not scheduled, not simulated). Full debate
with citations in `transcript.md`.
