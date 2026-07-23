---
id: 2026-07-21-intel-q2-earnings
title: Intel Q2 2026 earnings report
status: researched
created: '2026-07-21T15:25:19Z'
event:
  type: earnings
  summary: Intel reports Q2 2026 earnings July 23 2026 as a key AI capex demand signal
    alongside Alphabet and Tesla
  impact_window: '2026-07-23'
tickers:
- INTC
sources:
- title: Alphabet, Tesla, and Intel Earnings Are the First Real Test of AI Capex at
    Scale - Tech Times
  url: https://www.techtimes.com/articles/321101/20260720/alphabet-tesla-intel-earnings-are-first-real-test-ai-capex-scale.htm
  accessed_at: '2026-07-21T15:25:19Z'
hypothesis:
  statement: >-
    INTC's Q2 2026 print carries a large (roughly 8%), fat-tailed, negatively-skewed
    1-day reaction distribution. INTC is a heavily-scrutinized turnaround story
    (foundry losses, share loss to AMD/Nvidia and stalled positioning versus the
    "clean" AI-capex beneficiaries), so the pre-print drop of about 2.5 percent (USD
    105.535 on 07-21 to USD 102.85 on 07-22) is ambiguous between routine de-risking
    and leaked or sector-wide (Alphabet/Tesla capex-basket) negative sentiment, and
    it does not create a positive directional edge. Every candidate defined-risk
    structure (call debit spread, long straddle, iron condor) fails the panel's
    net-EV-greater-than-2-percent / adverse-tail-ratio-under-7-to-8x no-trade filter
    once elevated pre-earnings implied volatility and slippage are priced in.
  direction: none
  confidence: 74
plan:
  ticker: INTC
  action: no-trade
  entry:
    time: '2026-07-23T19:50:00Z'
    target_price: null
  exit:
    time: '2026-07-24T13:45:00Z'
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
    The bull's unrebutted point: the negative skew cited by bear and quant is
    largely a prior about the company (a stale, already-priced-in turnaround
    narrative), risking double-counting sentiment already reflected in the 2.5
    percent pre-print drop; the panel never resolved whether that drop is
    mechanical de-risking (bullish-neutral) or leaked/sector-wide bad news
    (bearish). If the print is a clean beat and the drop was mechanical
    de-risking, a small defined-risk call debit spread with a hard same-day exit
    would have been the correct, profitable trade, and this no-trade call forgoes
    it. Testable post-mortem: does INTC move up materially more than roughly 5-6
    percent (the spread's breakeven) despite the negative-skew thesis?
  last_updated: '2026-07-22T23:56:00Z'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-22T23:56:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Reference
prices: INTC USD 105.535 (2026-07-21 19:59Z close), USD 102.85 (2026-07-22 19:59Z
close) — a roughly 2.5 percent pre-print drop with no confirmed Intel-specific
news. The panel converged on NO TRADE: quant's base-rate model puts the expected
1-day move at roughly 8 percent, fat-tailed and negatively skewed given INTC's
turnaround/share-loss track record, yielding a negative expected value for a
directional long (about -0.5 percent even after crediting the bull's "de-risked
setup" read) and an adverse-tail-to-edge ratio near 10:1 that fails the
institutional no-trade filter on every structure tested (call debit spread, long
straddle, iron condor). Bear converged from an initially ambiguous stance (40) down
to 30, agreeing the fat-tail math sharpens rather than resolves the skepticism.
Bull held the weakest but most persistent dissent — that the negative skew may be
double-counting an already-priced-in narrative — but could not produce confirming
negative-fundamental evidence to force a trade. Full debate with citations in
`transcript.md`.
