---
id: 2026-07-14-ubs-q2-fy26
title: UBS reports Q2 2026 earnings July 30
status: researched
created: '2026-07-14T01:15:00Z'
event:
  type: earnings
  summary: UBS Group reports Q2 FY26 results July 30, 2026, with analysts expecting
    EPS to surge ~86% YoY.
  impact_window: '2026-07-30'
tickers:
- UBS
sources:
- title: Deutsche Bank, Other Fast-Moving European Bank Earnings Due
  url: https://www.inkl.com/news/deutsche-bank-other-fast-moving-european-bank-earnings-due-could-they-match-u-s-lenders
  accessed_at: '2026-07-14T01:15:00Z'
hypothesis:
  statement: >-
    The headline ~86% YoY EPS growth estimate for UBS Q2 FY26 is almost certainly a
    mechanical base-effect artifact (prior-year quarter distorted by Credit Suisse
    integration charges/badwill), not new information, and is likely already
    reflected in price. No verified directional edge exists into the July 30 print
    — modeled P(up) is approx 0.50-0.52 (near coin-flip), gross EV approx
    0.00-0.12%, and net EV is negative after approx 0.20% round-trip costs. The
    recent 3-day pullback (USD 54.11 on 7/14 to USD 52.62 on 7/17) sits within
    normal single-name volatility bands and is noise, not signal.
  direction: none
  confidence: 84
plan:
  ticker: UBS
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
    The strongest flag for post-mortem is structural, not a persona disagreement:
    no persona had live market-data tools to verify the two variables that would
    actually move the verdict -- the options-implied move vs. realized-move
    distribution, and the true consensus EPS/whisper number vs. the single
    unverified "86% YoY" source. The NO-TRADE convergence is robust given the
    information available, but it is a decision made under a data blackout, not
    one that has ruled out an edge. The bear's downside-tail intuition (legacy
    Credit Suisse litigation, FINMA capital rules, CHF/EUR/USD FX) remains
    genuinely unquantified -- correctly excluded from the trade decision, but a
    suppressed variable, not a resolved one.
  last_updated: '2026-07-21T10:47:21Z'
---

## Scouted 2026-07-14T01:15:00Z

## Researched 2026-07-21T10:47:21Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas independently researched, then converged after rebuttal. BULL opened
long via a defined-risk OTM call spread on the "room to re-rate" pullback thesis
(confidence 55) but conceded in Round 2 that the 86% YoY figure is an unverified
base-effect artifact and the quant's EV math was unrebutted, cutting to 30. BEAR
opened skeptical (35), citing the base-effect illusion, sell-the-news risk on a
well-telegraphed Credit Suisse integration program, and unquantified
litigation/FINMA/FX tail risk; in Round 2 it applied the DAL-lesson pattern
(unrebutted skeptic + aligning quant EV -> synthesize to NO-TRADE) and conceded
its own risk list was caution, not tradable alpha, rising to 72. QUANT opened at
NO-TRADE (78): P(up)=0.52/P(down)=0.48, gross EV +0.12%, round-trip costs ~0.20%,
net EV -0.08%, adverse-tail-to-edge ratio >50:1 (breaches the NKE-lesson filter);
in Round 2 it showed the base-effect argument only reinforces a near-coin-flip and
that even the bull's premium-capped structure fails on paying into event-IV with
no compensating edge, rising to 82. Verdict: NO-TRADE, confidence 84. No verified
options-implied-move or consensus-vs-whisper data was available to any persona
(no WebSearch/WebFetch access this run) -- flagged as a structural data gap for
the post-mortem rather than a resolved disagreement. Full debate in
`transcript.md`.
