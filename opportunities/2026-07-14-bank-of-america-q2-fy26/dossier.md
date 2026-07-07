---
id: 2026-07-14-bank-of-america-q2-fy26
title: Bank of America Q2 FY26 earnings
status: researched
created: '2026-07-07T11:00:01Z'
event:
  type: earnings
  summary: Bank of America reports Q2 2026 results July 14; net interest income and
    credit trends in focus.
  impact_window: '2026-07-14'
tickers:
- BAC
sources:
- title: Bank of America to release Q2 2026 earnings on July 14 (Pluang)
  url: https://pluang.com/en/news-feed/bank-of-america-laporkan-hasil-keuangan-kuartal-ii-2026
  accessed_at: '2026-07-07T11:00:01Z'
- title: Bank of America options point to ~3.5% move on earnings day (Investing.com)
  url: https://www.investing.com/news/stock-market-news/bank-of-america-options-point-to-35-move-on-earnings-day-93CH-4779608
  accessed_at: '2026-07-07T19:50:00Z'
- title: OptionSlam — BAC historical earnings moves
  url: https://www.optionslam.com/earnings/stocks/BAC
  accessed_at: '2026-07-07T19:50:00Z'
- title: StockAnalysis — BAC price and 52-week range
  url: https://stockanalysis.com/stocks/bac/
  accessed_at: '2026-07-07T19:50:00Z'
- title: BofA newsroom — Q2 2026 results date confirmation (pre-market July 14)
  url: https://www.stocktitan.net/news/BAC/bank-of-america-to-report-second-quarter-2026-financial-results-and-3lujrw96uxvp.html
  accessed_at: '2026-07-07T19:55:00Z'
hypothesis:
  statement: "The fundamental lean is mildly long — BAC's beat-and-raise setup (raised
    FY26 NII guide to 6-8%, clean credit, eight straight beats, positive sell-side
    revisions) makes an earnings beat the base case. It is NOT tradable here because
    the event gap fires ~10:45Z pre-market, before the 13:30Z bar open, so the bulk
    (~70-80%, ~1.9%) of the reaction is un-capturable; the only executable window is
    intraday residual drift whose EV is ~0% to slightly negative after costs,
    worsened by near-52-week-high negative asymmetry, a priced-in NII guide, and
    non-repeatable Q1 reserve dynamics."
  direction: long
  confidence: 38
plan:
  ticker: BAC
  action: buy
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  decision: no-trade
  rationale: "The catalyst resolves in the pre-market gap ahead of the 13:30Z open,
    leaving only intraday residual drift with EV near zero to negative after
    0.06-0.10% costs (quant EV table gross +0.05%, net ~-0.02%; capturable drift
    ~-0.10% before costs, ~0% even granting the capital-return catalyst its maximum
    benefit). Bull conceded its two load-bearing points — capital-return is a
    decoupled post-CCAR event (~late June), not a 7/14 earnings catalyst, and there
    is no basis for a blind 13:35Z entry. Its surviving idea is a conditional
    'enter only if the open holds above the pre-market gap high on volume'
    continuation trade, which cannot be expressed as a deterministic pre-committed
    entry/exit and so fails the simulation's bar-mapping requirement. Combined with
    near-high negative asymmetry and Lesson #1 (confidence sub-45, un-hedgeable
    positive tail, net EV <~2%), this is a NO-TRADE filter, not a size-down. Stand
    aside; status held at researched (never scheduled), so no fill is taken."
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-07T20:05:22Z'
---

## Scouted 2026-07-07T11:00:01Z

## Researched 2026-07-07T20:05:22Z

**Verdict: NO-TRADE (direction long, confidence 38).** Three-round panel (bull/bear
on sonnet, quant/synthesizer on opus). Fundamentals lean bullish (beat-and-raise:
FY26 NII guide 6-8%, Q1 NII +9% YoY, clean credit, 8 straight beats), but the print
lands pre-market ~10:45Z before the 13:30Z bar open, so ~70-80% of the reaction is
un-capturable. The only executable intraday-drift window carries net EV ≈ 0 to
slightly negative after costs, compounded by priced-for-perfection positioning near
the 52-week high. Fails the Lesson #1 no-trade filter. Full debate in
`transcript.md`.
