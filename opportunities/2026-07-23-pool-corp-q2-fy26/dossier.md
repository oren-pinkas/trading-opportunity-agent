---
id: 2026-07-23-pool-corp-q2-fy26
title: Pool Corp Q2 2026 Earnings
status: researched
created: '2026-07-23T01:19:37Z'
event:
  type: earnings
  summary: Pool Corp reports Q2 2026 results with consensus EPS of USD 5.35 on
    USD 1.82B revenue
  impact_window: '2026-07-23'
tickers:
- POOL
sources:
- title: Pool Q2 2026 Earnings Preview - Alphastreet
  url: https://news.alphastreet.com/pool-q2-2026-earnings-preview-july-23-street-expects-5-35-eps/
  accessed_at: '2026-07-23T01:19:37Z'
- title: "Pool Corporation Reports Second Quarter Results; Confirms Annual Earnings\
    \ Guidance Range, Excluding CEO Transition Costs - GlobeNewswire"
  url: https://www.globenewswire.com/news-release/2026/07/23/3332008/10055/en/Pool-Corporation-Reports-Second-Quarter-Results-Confirms-Annual-Earnings-Guidance-Range-Excluding-CEO-Transition-Costs.html
  accessed_at: '2026-07-25T21:45:25Z'
- title: "Is Pool Corp (POOL) Undervalued at 43.1%? Q2 Earnings Report Shows EPS\
    \ of USD 5.38, Beating Estimates of USD 5.32 - Gurufocus"
  url: https://www.gurufocus.com/news/8974735/is-pool-corp-pool-undervalued-at-431-q2-earnings-report-shows-eps-of-538-beating-estimates-of-532
  accessed_at: '2026-07-25T21:45:25Z'
- title: "Pool Corp. (POOL) Q2 Earnings and Revenues Beat Estimates - Yahoo Finance"
  url: https://finance.yahoo.com/markets/stocks/articles/pool-corp-pool-q2-earnings-121504178.html
  accessed_at: '2026-07-25T21:45:25Z'
- title: "Pool (NASDAQ:POOL) Posts Q2 CY2026 Sales In Line With Estimates - StockStory"
  url: https://stockstory.org/us/stocks/nasdaq/pool/news/earnings/pool-nasdaqpool-posts-q2-cy2026-sales-in-line-with-estimates
  accessed_at: '2026-07-25T21:45:25Z'
hypothesis:
  statement: >-
    POOL's Q2 FY26 print was a low-magnitude, low-information event: a ~+0.4% to
    +1.1% adjusted-EPS beat (bottom-quintile surprise) on in-line sales, with FY26
    ex-charge guidance of USD 10.87-11.17 CONFIRMED (not cut) and straddling
    ~USD 11.08 consensus. The only genuine negatives (gross margin 29.7% vs 30.0%,
    GAAP operating income -2%, GAAP EPS USD 5.17 dragged by USD 8.3M CEO-transition
    costs) are non-recurring or second-order. The modest print-day move (likely
    +1-2%, per secondary-source corroboration) already absorbed most of the
    reaction; residual 5-session PEAD drift of roughly +0.15% does not clear
    ~20bp round-trip costs in either direction. Independently, no citable
    minute-bar price was obtainable at any point in this debate (twelvedata
    HTTP 429 throughout), so neither entry nor exit could be filled or verified.
  direction: none
  confidence: 80
plan:
  ticker: POOL
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
    The strongest residual issue is process integrity, not analytical
    disagreement — all three personas converged on NO-TRADE, but partly through
    claims later retracted. Bull's Round 1 "+1.19% on print day" was aggregator
    boilerplate, self-contradicted by a second aggregator ("+USD 1.44 to
    USD 197.63"). Quant's Round 1 "-6.55% to USD 183.77, near 52-week low" was
    mis-sourced and retracted in Round 2 — yet it was the load-bearing input for
    quant's original "drift already consumed" call AND for bull's Round 2
    capitulation; bull conceded to a number that was wrong. Bear's Round 1/2
    "guidance cut even ex-CEO-costs" was factually wrong (ex-charge guidance was
    CONFIRMED), and bear's Round 2 endorsement of the -6.55% figure compounded
    the error — bear's entire thesis rested on two retracted facts. The panel
    reached the right answer via wrong reasoning twice over, briefly forming
    false consensus on a fabricated price path. Also flagged: toa/twelvedata
    HTTP 429 persisted across the ENTIRE multi-round debate on a covered US
    large-cap (not a known venue-coverage gap) — a fresh availability failure
    mode, independent of thesis correctness, that argues for a pre-debate
    data-availability gate before spending rounds on an unexecutable thesis.
    Exact print-day move magnitude remains unverified (only inferred +1-2% from
    weak secondary sources); direction is probably right, magnitude is not
    established.
  last_updated: '2026-07-25T21:45:25Z'
---

## Scouted 2026-07-23T01:19:37Z

## Researched 2026-07-25T21:45:25Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). POOL reported Q2
FY26 on 2026-07-23: adjusted diluted EPS USD 5.38 (bottom-quintile beat vs
~USD 5.32-5.36 consensus), net sales USD 1.82B in line (+2.2% y/y), gross margin 29.7%
vs 30.0% y/y (-30bp, inbound freight/mix), GAAP operating income -2% to USD 267.7M,
GAAP diluted EPS USD 5.17 (dragged by USD 8.3M new-CEO-transition costs). FY26 GAAP
guidance USD 10.66-10.96, but ex-charge guidance of USD 10.87-11.17 was CONFIRMED (not
cut), straddling the ~USD 11.08 street consensus. New CEO John Watwood has served since
2026-05-04 following the prior CEO's unexpected departure. The debate itself repeatedly
self-corrected: both bull and quant initially cited wrong print-day price moves
(opposite signs) sourced from unreliable secondary aggregators, and quant/bear
initially mis-stated the ex-charge guidance as a cut; all were retracted by Round 2 once
cross-checked. `toa price POOL --provider twelvedata` returned HTTP 429 on every
attempted timestamp across all three rounds — no citable minute bar was ever obtained,
an independent execution blocker regardless of thesis. QUANT's revised EV: residual
5-session drift ≈ +0.15% vs ~20bp round-trip costs → net EV long ≈ -0.05%, short ≈
-0.35% (dividend/borrow drag); per-trade Sharpe ≈ 0.036; cost-adjusted confidence 41%,
below the 45% no-trade filter. Verdict: NO-TRADE — negative post-cost EV plus an
unresolved price-data blocker. Full debate with the self-corrections in
`transcript.md`.
