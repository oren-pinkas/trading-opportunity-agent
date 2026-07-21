---
id: 2026-07-15-united-airlines-q2-fy26
title: United Airlines Q2 FY26 earnings
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: earnings
  summary: United Airlines reports Q2 2026 results Wed Jul 15, watched for domestic
    capacity discipline and fare trends.
  impact_window: '2026-07-15'
tickers:
- UAL
sources:
- title: 'United Airlines to Report Q2 Earnings: What''s in Store for the Stock? -
    Yahoo Finance'
  url: https://finance.yahoo.com/markets/stocks/articles/united-airlines-report-q2-earnings-161100141.html
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: UAL's Q2 FY26 print was a sell-the-news event on the known capacity-discipline/fare-trend
    swing factor, driving a cumulative ~-4% slide (USD 126.25 close 07-10 to USD 116.64
    open 07-16) with only a single, undifferentiated +1.82% intraday bounce off the
    low. No confirmed, positive-EV expression -- bullish or bearish -- exists for
    a new entry as of 07-16/07-17.
  direction: none
  confidence: 74
plan:
  ticker: UAL
  action: no-trade
  entry:
    time: n/a
    target_price: null
  exit:
    time: n/a
    target_price: null
  expected_profit_pct: 0.0
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
  dissent: 'Strongest unresolved disagreement: whether the 07-16 +1.82% intraday bounce
    off USD 116.64 carries any signal. Bull held it marks real buyers defending a
    USD 116-120 dip-buy zone, pending 07-17 confirmation. Bear countered it is an
    indistinguishable dead-cat-bounce base rate that doesn''t separate oversold noise
    from continued UAL-specific repricing -- underscored by UAL selling off despite
    a favorable sector backdrop (peer DAL at a 52-week high pre-print). Never resolved:
    n=1 provides no distribution, and the confirming 07-17 data point was unavailable
    within the debate window. Quant found near-zero-to-negative EV across every structure
    examined (long-through-print: -0.59% net; post-flush bounce-buy stock: +0.09%
    net, statistically zero; bounce-buy via options: negative after friction).'
  last_updated: '2026-07-21T15:44:59Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-21T15:44:59Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real prices via twelvedata: UAL closed USD 126.25 (07-10), opened USD 121.52 and closed USD 120.78 on the 07-15 event day, gapped to USD 116.64 at the 07-16 open (-3.43%), then bounced intraday to USD 118.76 close (+1.82% off the open). Bull initially framed a catalyst-pop long, but the tape refuted it and the thesis was revised to a defined-risk dip-buy (confidence fell 35 -> 22 across rounds, ultimately withdrawn pending unconfirmed 07-17 follow-through). Bear held no-long throughout (confidence 68 -> 72), citing the Yahoo preview's own framing of capacity-discipline/fare-trends as a known swing factor, peer DAL's pre-print run to a 52-week high reducing UAL's room for beat-euphoria, and UAL under performing a favorable sector backdrop. Quant modeled EV for every structure examined -- long-through-print (net -0.59%, breakeven needs P(up) > 0.53), and bull's revised post-flush mean-reversion bounce-buy (net ~+0.09% in stock, negative once options friction is included) -- concluding no tradeable directional edge (confidence 22 -> 26) and recommending 0% size throughout. All three personas converged on NO TRADE. Full debate with citations in `transcript.md`.
