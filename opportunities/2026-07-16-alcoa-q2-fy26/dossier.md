---
id: 2026-07-16-alcoa-q2-fy26
title: Alcoa Q2 FY26 earnings
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: earnings
  summary: Alcoa reports Q2 2026 results Jul 16 after the close, a read on aluminum
    demand and tariff cost pass-through.
  impact_window: '2026-07-16'
tickers:
- AA
sources:
- title: Alcoa sets Q2 2026 earnings call for July 16 - StockTitan
  url: https://www.stocktitan.net/news/AA/alcoa-schedules-second-quarter-2026-earnings-release-and-conference-a79h97yp3oyj.html
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: >-
    By the research date (2026-07-22) the scouted July 16 catalyst has already fired
    and fully priced: AA fell from USD 48.57 (7/15 pre-print) to USD 46.87 (day-of)
    to a trough of USD 43.655 (7/20) on an EPS miss (USD 2.12 actual vs ~USD 2.24
    consensus), an alumina production guidance cut (Pinjarra refinery), and an
    unresolved South32 acquisition financing overhang, before a single-day bounce to
    USD 44.28 (7/21). A fresh position entered now is a new post-event bet, not the
    pre-event trade the dossier scouted. The two live directional leans cancel: PEAD
    (post-earnings drift) argues for continued weakness of roughly -1% to -2% given
    the confirmed miss and guide-down, while an oversold-bounce case (RSI ~28 on
    7/17, all analyst targets USD 51-80 above spot, a guided ~USD 10M Q3 Section 232
    tariff give-back, structural aluminum deficit) argues for roughly +1% to +2% —
    but the RSI-28 signal already failed once (AA made a lower low on 7/20 after it
    fired). Net EV computes to roughly -0.1% to -0.3% after round-trip costs, with an
    unhedged fundamental left tail (South32 financing, further alumina/LME weakness)
    on a beta-1.63 name. No side's edge clears the confidence bar to trade.
  direction: none
  confidence: 20
plan:
  ticker: AA
  action: no-trade
  entry:
    time: '2026-07-22T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-22T13:30:00Z'
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
    By Round 2 the bear and quant agree on direction — PEAD says the confirmed miss
    plus alumina guide-down should keep AA drifting down, and the bear raised its
    directional-correctness confidence from 42 to 48 on exactly this basis. Yet both
    decline to short, citing squeeze risk on a beta-1.63 name and a net EV near zero.
    The bull reads the same tape (lower low on 7/20, then a one-day bounce) as an
    oversold mean-reversion setup with every analyst target above spot. Unresolved:
    does the PEAD down-drift constitute a tradable defined-risk short edge (small put
    spread), or is it genuinely neutralized by the oversold-bounce/relief-rally pull
    and squeeze risk down to ~0 EV? Neither side disproved the other; the down-drift
    lean was never quantified above the trade bar, and the mean-reversion lean rests
    on a stale RSI signal that already failed once. Testable post-mortem: does the
    7/21 bounce extend or fade, and does AA's realized drift over the following weeks
    match PEAD (down) or mean-reversion (up)?
  last_updated: '2026-07-22T07:55:00Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-22T07:55:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). By the research
date the July 16 print had already fired and fully priced: AA fell from USD 48.57
(7/15) to a trough of USD 43.655 (7/20) on an EPS miss (USD 2.12 vs ~USD 2.24
consensus) and an alumina guidance cut (Pinjarra refinery), then bounced one day to
USD 44.28 (7/21). The QUANT's EV calibration was decisive both rounds: Round 1's
~50x adverse-tail-to-edge ratio (binary earnings gap) evaporated once the event had
already resolved, but was replaced by a genuine ~0 EV problem for a fresh position —
PEAD-driven continued weakness (~-1% to -2%) roughly cancels an oversold-bounce case
(~+1% to +2%), netting -0.1% to -0.3% after costs, against an unhedged fundamental
left tail (South32 acquisition financing, further alumina/LME weakness). The BULL
held a defined-risk call-debit-spread recommendation (confidence 42) but conceded
its own Round 1 pre-commitment: a stale, already-priced catalyst defaults to
NO-TRADE. The BEAR raised directional-correctness confidence to 48 on PEAD grounds
but still would not size a naked short given beta-1.63 squeeze risk. Verdict:
NO-TRADE. Full debate with citations in `transcript.md`.
