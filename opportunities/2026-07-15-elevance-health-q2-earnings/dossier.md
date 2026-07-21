---
id: 2026-07-15-elevance-health-q2-earnings
title: Elevance Health Q2 FY26 Earnings
status: researched
created: '2026-07-14T05:08:14Z'
event:
  type: earnings
  summary: Elevance Health reports Q2 2026 results Jul 15 amid sector-wide scrutiny
    of medical cost trend after peer guidance cuts
  impact_window: '2026-07-15'
tickers:
- ELV
sources:
- title: Earnings Calendar and Analysis for This Week (July 13-17) | Kiplinger
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-14T05:08:14Z'
hypothesis:
  statement: >-
    ELV reported Q2 2026 on 2026-07-15 (adjusted EPS USD 7.45 vs USD 6.21 consensus,
    +~20% surprise; revenue USD 49.8B beat) and RAISED FY2026 adjusted EPS guidance
    to "at least USD 27" plus 12%+ 2027 growth -- a raise, not a cut, contrary to
    peers. Shares still fell ~10.6% on the print (USD 426.79 -> ~USD 381.62) on
    Medicaid-margin and "earnings quality" concerns (MLR up 80bps to 89.7%, guided
    to 90.2%+/-50bps; Medicaid "trough year" at -1.75% margin with further state
    exits signaled). Research ran 2026-07-21, six days after the print, which the
    panel found decisive: the catalyst is fully realized and priced. No persona
    could construct a positive-EV forward structure from today's ~USD 383 spot --
    the bear's structural thesis is a lagging echo of the information that already
    caused the gap (put spread near-breakeven at its own target), and the bull's
    overreaction/reversion case rests on a Street re-rate (consensus PT ~USD 434)
    that already happened and produced four flat sessions, not a bounce (EV inside
    noise, ~+1.1% gross). The only structure with plausible edge -- long volatility
    into upcoming peer MCO earnings -- cannot be priced without a live option chain.
    Unanimous NO TRADE.
  direction: none
  confidence: 18
plan:
  ticker: ELV
  action: no-trade
  entry:
    time: '2026-07-15T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-15T19:59:00Z'
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
    The bear's structural Medicaid-margin thesis (real, multi-quarter, corroborated
    by sector-wide peer MA/Medicaid guidance cuts) versus the bull's/quant's
    technical read that four flat sessions post-gap ($380-383) signal seller
    exhaustion / market efficiency rather than pending continuation. Neither side
    has a live options chain or fresh peer-earnings data to resolve which reading
    is right. Flips on the next peer MCO print (UNH/HUM/CI/CVS) or a fresh
    ELV-specific Medicaid catalyst (state exit/rate announcement).
  last_updated: '2026-07-21T14:15:00Z'
---

## Scouted 2026-07-14T05:08:14Z

## Researched 2026-07-21T14:15:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run 2026-07-21 --
six days after the 2026-07-15 print. Real prices via `toa price ELV --provider
twelvedata`: USD 426.73 (07-14 pre-print) -> USD 388.69 close / ~USD 381.62 premarket
(07-15) -> USD 383.26 (07-20). ELV beat and RAISED guidance (adjusted EPS USD 7.45 vs
USD 6.21 est; FY26 guide raised to "at least USD 27") yet fell ~10.6% on Medicaid-margin
and earnings-quality concerns -- the dossier's premise (ELV at risk of a peer-style
guidance cut) was inverted by reality. The QUANT's timing finding was decisive: the
impact window is already past, so any pre-print positioning is lookahead bias; even
reframed as a post-drift trade entered today, no structure clears a positive-EV bar --
the bear's put spread is near-breakeven at its own target, the bull's reversion long is
inside statistical noise (+1.1% gross), and the only structure with real edge potential
(long vol into peer MCO earnings) can't be priced without a live option chain. BULL
conceded from an implicit ~55-60 to 12/100; BEAR conceded from 35 to 22/100; QUANT held
NO TRADE at 20/100 (up from 10, since the reframing is actionable but still edgeless).
Verdict: NO-TRADE (not scheduled, not simulated). Flips only on a peer MCO print
resolving the two-sided variance, or a live option chain showing peer-earnings vol
mispriced. Full debate with citations in `transcript.md`.
