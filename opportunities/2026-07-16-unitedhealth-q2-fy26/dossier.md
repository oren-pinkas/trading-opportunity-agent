---
id: 2026-07-16-unitedhealth-q2-fy26
title: UnitedHealth Q2 FY26 earnings
status: researched
created: '2026-07-07T05:39:26Z'
event:
  type: earnings
  summary: UNH reports Q2 before open Jul 16; medical-cost trend and 2026 guidance
    credibility in focus after prior-year guidance cuts
  impact_window: '2026-07-16'
tickers:
- UNH
sources:
- title: UnitedHealth Group Q2 2026 Earnings Preview (Hudson Labs)
  url: https://www.hudson-labs.com/research/unitedhealth-group-unh-q2-2026-earnings-preview
  accessed_at: '2026-07-07T05:39:26Z'
- title: UnitedHealth Q1 2026 earnings call transcript (beats, stock +9.3%)
  url: https://www.investing.com/news/transcripts/earnings-call-transcript-unitedhealth-q1-2026-beats-expectations-stock-rises-93CH-4637516
  accessed_at: '2026-07-08T01:30:00Z'
- title: What to Expect From UnitedHealth's Q2 2026 Earnings (Barchart)
  url: https://www.barchart.com/story/news/2642725/what-to-expect-from-unitedhealth-group-s-q2-2026-earnings-report
  accessed_at: '2026-07-08T01:30:00Z'
- title: UNH earnings history and implied move (OptionSlam / MarketChameleon)
  url: https://www.optionslam.com/earnings/stocks/UNH
  accessed_at: '2026-07-08T01:30:00Z'
- title: Wall Street upgraded UNH six times in two weeks; PT roundup (MEXC)
  url: https://www.mexc.co/en-IN/learn/article/wall-street-upgraded-unh-six-times-in-two-weeks-can-unitedhealth-stock-hit-492-unh-price-target-2026-2030/1
  accessed_at: '2026-07-08T01:30:00Z'
- title: UnitedHealth Group Faces DOJ Probe And Regulatory Questions (Yahoo Finance)
  url: https://finance.yahoo.com/news/unitedhealth-group-faces-doj-probe-021104084.html
  accessed_at: '2026-07-08T01:30:00Z'
hypothesis:
  statement: >-
    No tradeable edge. UNH prints Q2 BMO Jul 16 into a high bar — the stock has
    ~doubled off its 52-week low ($234.60) to $472.17, trades above the sell-side
    consensus target band (~$407-416), and absorbed six analyst upgrades in six
    weeks, with a buy-side whisper (Bernstein adj EPS ~$5.22) well above the ~$4.54
    headline, so an in-line-to-headline print gets punished. Recent earnings
    reactions are ~50/50 on direction with a fat LEFT tail (Q4'25 -19.6%, Q2'25
    -7%, Q1'26 +7%) and a ~6.8% options-implied move; the
    negative-base-rate-near-52wk-low lesson is inapplicable (name is near its
    highs). The only way to capture a BMO gap in an equity-only simulator is a
    naked overnight hold — precisely the un-hedgeable exposure the institutional
    filter forbids given the fresh -19.6% precedent — and a whisper-adjusted EV for
    that long is NEGATIVE (~-2.1% net). An intraday-only trade is structurally
    edgeless because by the first fillable bar (13:30Z) the gap is already set.
    Both a naked long and a naked short face symmetric fat un-hedgeable tails.
    Verdict PASS.
  direction: none
  confidence: 38
plan:
  ticker: UNH
  action: no-trade
  entry: null
  exit: null
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
  dissent: 'Bull''s residual case: a clean beat-and-raise on the MCR KPI with confident
    H2 language remains a real path to a repeat of the Q1 +9.3% pop, and a CONDITIONAL
    post-gap intraday long (enter ~14:15Z only if UNH opens green, exit ~19:55Z, zero
    overnight/gap tail) would sidestep the fat overnight tail the quant priced. The
    trade dies only because the simulator cannot enforce the "only-if-green" entry
    condition — an unconditional fill collapses it back to a coin-flip minus costs.
    Unresolved: whether the whisper bar (~$5.22 vs $4.54 headline) is real; if
    consensus ~= whisper, the quant''s long EV returns toward breakeven (still <2%,
    still not tradeable). DATA CONFLICT flagged by quant + bear: the 472.17 anchor
    sits above the market-data 52wk high (~430) and the reported post-Q1 close (~344);
    the simulated price series is internally inconsistent, though it does not change
    the no-trade verdict.'
  last_updated: '2026-07-08T01:38:00Z'
---

## Scouted 2026-07-07T05:39:26Z

## Researched 2026-07-08T01:38:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Anchor UNH
$472.17 @ 2026-07-07T19:59Z. The panel converged hard on **NO-TRADE**. UNH reports
Q2 before the open on Jul 16 into a high bar: ~doubled off its 52-week low, trading
above the sell-side target band, six upgrades in six weeks, and a buy-side whisper
(~$5.22 adj EPS) above the ~$4.54 headline — so an in-line print risks a sell-the-news
fade. Earnings reactions are ~50/50 on direction with a fat left tail (Q4'25 -19.6%)
and a ~6.8% implied move. In an equity-only simulator the only way to capture a BMO
gap is a naked overnight hold, which the whisper-adjusted EV makes negative (~-2.1%
net) and which the institutional filter forbids (un-hedgeable tail, no options);
an intraday-only trade is edgeless because the gap is already set by the first
fillable bar. Bull conceded from 58→44, bear hardened caution 68→80, quant confirmed
PASS at 75. Full debate with citations in `transcript.md`.
