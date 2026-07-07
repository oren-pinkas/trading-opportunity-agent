---
id: 2026-07-09-pepsico-q2-fy26
title: PepsiCo Q2 FY26 earnings
status: researched
created: '2026-07-06T22:05:13Z'
event:
  type: earnings
  summary: PEP reports Q2 FY26 before open Jul 9; Street ~$2.21 EPS on $23.96B rev,
    targets recently cut.
  impact_window: '2026-07-09'
tickers:
- PEP
sources:
- title: PepsiCo sets July 9 date to reveal Q2 2026 earnings
  url: https://www.stocktitan.net/news/PEP/pepsi-co-announces-timing-and-availability-of-second-quarter-2026-qw5aeek7utzl.html
  accessed_at: '2026-07-06T22:05:13Z'
hypothesis:
  statement: PEP's Q2 print carries a mildly long directional lean (P(up)~0.62, 84%
    positive 1-day base rate), but the bull's cheap-convexity edge was arithmetically
    refuted and net EV (+0.37%) sits far below the ~2% bar, so the recorded verdict
    is NO-TRADE.
  direction: long
  confidence: 82
plan:
  ticker: PEP
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.37
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
  dissent: Bull maintains that Quant's own P(up)=0.62 plus Bear's Elliott margin-improvement
    positive tail is a live long catalyst that a downside-capped debit spread should
    monetize; the panel counters that the spread is a long-premium structure with
    EV -15% to -25% once the ~2.6x-rich implied vol crushes, so being directionally
    right still loses money.
  last_updated: '2026-07-07T18:30:48Z'
---

## Scouted 2026-07-06T22:05:13Z

## Researched 2026-07-07T18:30:48Z — NO-TRADE

The panel converged on **NO-TRADE**. The crux was the bull's convexity claim: options implied ~4.14% vs an alleged trailing-4Q realized **7.42%**. Bear and Quant refuted it arithmetically — with three known prints (+2.3%/+1.49%/+1.16%), a 7.42% average forces a 4th move of ~**24.7%**, impossible for a sub-0.6-beta staple; true realized is ~**1.6%**, making implied ~4.2% roughly **2.6x rich**. That inverts the edge: the bull call debit spread is a long-premium bet against IV crush, re-priced at **EV -15% to -25% of premium** even when direction is right. The residual read is mildly long (P(up)~0.62, 84% positive base rate, median +1.3%), but the best directional structure nets only **+0.37%** — far below the **~2%** EV bar and sub-scale. Two personas plus the numeric tie-breaker (Quant) agree: no positive-EV structure survives, so stand aside.
