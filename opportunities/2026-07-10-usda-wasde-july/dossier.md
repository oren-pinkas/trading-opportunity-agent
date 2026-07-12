---
id: 2026-07-10-usda-wasde-july
title: USDA July WASDE report due, soybean prices near 2-month high
status: researched
created: '2026-07-08T14:26:18Z'
event:
  type: economic
  summary: USDA's July 10 WASDE report lands with soybean futures at a two-month high
    (.27/bu) on rising crush/export demand forecasts, setting up a volatility catalyst
    for ag processors and fertilizer names.
  impact_window: '2026-07-10'
tickers:
- ADM
- MOS
sources:
- title: Special Edition – Market Trends Report – USDA Report July 6, 2026 - Grain
    Farmers of Ontario
  url: https://gfo.ca/market-trends/special-edition-market-trends-report-usda-report-july-6-2026/
  accessed_at: '2026-07-08T14:26:18Z'
hypothesis:
  statement: >-
    No credible, tradeable edge exists in ADM or MOS on the July WASDE catalyst. The
    observed report-day price series (~25-40 sigma moves, +51.8% ADM / +28% MOS)
    is non-credible and reads as stub/feed-glitch data (P(feed materially wrong)
    ~= 0.90); the directional "spike-fade-stabilize" pattern is inseparable from
    the disputed magnitude and cannot be trusted on sign alone. Independently, even
    at face value the catalyst is stale (2 days old at analysis time), the pre-report
    thesis (crush/export demand, soy futures at 2-month highs) was already priced
    in before the print, and both names are already fading from report-day highs.
    MOS also has weak, indirect fundamental linkage to a soy-specific WASDE. Every
    instrument/sizing/direction considered carries negative or fictitious
    (phantom-P&L) expected value.
  direction: none
  confidence: 90
plan:
  ticker: ADM/MOS
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
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
    Convergence was full and genuine (Bull opened Round 1 long ADM at $67.75 and
    explicitly conceded to no-trade in Round 2), so no directional disagreement
    survives. The residual worth preserving for post-mortem is a difference in
    reasoning path: Bull retains a weaker belief that a real-but-smaller signal
    could exist beneath the corrupted feed (a differentiated WASDE surprise a
    clean data source might confirm), whereas Bear/Quant hold a more totalizing
    skepticism grounded in the priced-in/stale-catalyst argument, which kills the
    trade even if the data were pristine. Revisit only if ALL of: (1) an
    independent, verified feed confirms the report-day moves were ordinary-scale
    (~+/-1-4%), collapsing the feed-glitch null; (2) evidence of a genuine
    differentiated WASDE surprise not already reflected in pre-print futures
    positioning; (3) fresh positioning available before the next print, since the
    only ever-positive-EV path was pre-report entry.
  last_updated: '2026-07-12T16:37:26Z'
---

## Scouted 2026-07-08T14:26:18Z

## Researched 2026-07-12T16:37:26Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three personas
converged on NO-TRADE for both ADM and MOS. Two independent, sufficient reasons drove
the verdict: (1) the observed report-day price series (+51.8% ADM, +28.0% MOS
single-session) is a ~25-40 sigma outlier for these large-cap, low-vol names on a
routine monthly WASDE release — quant assigned P(feed materially wrong) ~= 0.90, and
bear noted moves of this scale would be front-page/halt-triggering and aren't; (2)
even taking the data at face value, the catalyst is stale (analysis run 2 days after
the July 10 print) and the pre-report bullish narrative (crush/export demand, soy
futures at a two-month high) was already priced in before the report, so there is no
differentiated surprise left to trade — both names are already fading from
report-day highs. BULL opened Round 1 long ADM (entry $67.75, target $70.40, stop $65,
half-size) but fully conceded in Round 2 once bear's "already priced in" point broke
the confirmation framing at its root. QUANT formalized the "can't trust direction
while discarding magnitude" argument as a category error (percentage moves are
defined by the disputed anchor) and ran EV for every instrument/sizing considered:
long ADM blended EV ~= -2.75%/unit (worst leg), short-MOS fade blended EV ~= -0.27%
(edge fictitious in the 90%-broken-feed branch) — unambiguously no-trade at 90/100
confidence. Verdict: NO-TRADE (not scheduled, not simulated). Full debate with
citations in `transcript.md`.
