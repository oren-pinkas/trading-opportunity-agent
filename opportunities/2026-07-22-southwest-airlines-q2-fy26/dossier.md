---
id: 2026-07-22-southwest-airlines-q2-fy26
title: Southwest Airlines Q2 FY26 earnings
status: researched
created: '2026-07-07T20:34:02Z'
event:
  type: earnings
  summary: LUV reports Q2 FY26 before open July 22; unit revenue, capacity and new-revenue-initiative
    traction in focus
  impact_window: '2026-07-22'
tickers:
- LUV
sources:
- title: Southwest Airlines (LUV) Earnings Dates - TipRanks
  url: https://www.tipranks.com/stocks/luv/earnings
  accessed_at: '2026-07-07T20:34:02Z'
- title: Southwest Airlines earnings preview (Q2 FY26)
  url: https://www.barchart.com/story/news/3073497/southwest-airlines-earnings-preview-what-to-expect
  accessed_at: '2026-07-08T02:06:27Z'
- title: LUV historical earnings moves / implied move
  url: https://www.optionslam.com/earnings/stocks/LUV
  accessed_at: '2026-07-08T02:06:27Z'
- title: Southwest has fallen 34% from its high — TIKR
  url: https://www.tikr.com/blog/southwest-airlines-has-fallen-34-from-its-high-heres-where-the-stock-could-go-in-2026
  accessed_at: '2026-07-08T02:06:27Z'
- title: Fitch revises Southwest outlook to Negative
  url: https://www.investing.com/news/stock-market-news/southwest-airlines-outlook-revised-to-negative-by-fitch-maintains-bbb-rating-93CH-3966362
  accessed_at: '2026-07-08T02:06:27Z'
- title: IATA — Middle East disruptions, high fuel prices halve airline profitability
  url: https://www.iata.org/en/pressroom/2026-releases/06-07-middle-east-disruptions-high-fuel-prices-halve-airline-industry-profitability/
  accessed_at: '2026-07-08T02:06:27Z'
hypothesis:
  statement: >-
    NO-TRADE / stand aside. LUV's Q2 print carries a large (~10.35% options-implied)
    directional move that sits almost entirely in the unhedgeable pre-open overnight
    gap; by the 13:31Z equity open the news is already priced, leaving only a ~+/-1.2%
    intraday residual that historically fades rather than extends (Apr-23 print:
    -6.35% intraday then +2.3% recovery into close). The only permitted instrument
    (intraday US equity) nets ~0% EV after costs, far below the 2% bar, and the real
    edge lives in a gap that options cannot hedge in-sim and lesson 1 forbids holding
    naked. A mild long fundamental lean survives (RASM +11.2% Q1 beat, Q2 guide
    +16.5-18.5%, upsell/loyalty inflection) but it is not tradable in the residual.
  direction: long
  confidence: 28
plan:
  ticker: LUV
  action: buy
  entry:
    time: '2026-07-22T13:31:00Z'
    target_price: 339.46
  exit:
    time: '2026-07-22T19:59:00Z'
    target_price: 339.46
  expected_profit_pct: 0.0
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-08T02:06:27Z'
---

## Scouted 2026-07-07T20:34:02Z

## Researched 2026-07-08T02:06:27Z

**Verdict: NO-TRADE (stand aside).** Status held at `researched` (not promoted to
`scheduled`) so the no-trade is never picked up for simulation. The `plan` block
records the debated least-bad executable reference (intraday long, entry 13:31Z /
exit 19:59Z, `expected_profit_pct: 0.0`) purely to satisfy the schema — it is
**not recommended**.

Three-round bull/bear/quant panel converged unanimously on stand-aside:
- **Bull** 58 -> 38: conceded lesson-2 ("off-lows bounce") was misapplied (LUV is
  mid/upper range, up ~55-58% trailing year, not near its 52wk low), and that the
  Apr-23 -4.06% close refutes the intraday-drift-continuation thesis. Still rejects
  a short (fundamentals genuinely delivering) but sees no defensible tradable long.
- **Bear** 30 -> 35: reconciled the price paradox (52wk low $28.98 -> ~$60 Jan peak
  -> ~$39.50 Mar fuel-shock trough -> ~$42-50 now; "up 55%" and "down 34%" both true
  off different anchors). Dropped the short-if-forced lean; unhedged fuel + possible
  Q3 guidance-cut risk also sits in the untradeable gap.
- **Quant** 25 -> 22: implied move ~10.35% lives in the open gap; intraday residual
  ~+/-1.2% and often a fade; restated net EV ~-0.01% to +0.04%. To clear the 2% bar
  at +/-1.2% needs P(win) >= ~0.87 (implausible). Not reachable.

Full transcript with citations in `transcript.md`.
