---
id: 2026-07-10-bloom-energy-short-report
title: Bloom Energy shares hit by Hunterbrook short-seller report
status: researched
created: '2026-07-10T14:11:11Z'
event:
  type: economic
  summary: Hunterbrook's short report challenged Bloom Energy's China-free scandium
    supply claims and its unaudited $20B order backlog, sending BE shares down as
    much as 12%; company disputes the findings.
  impact_window: '2026-07-08'
tickers:
- BE
sources:
- title: Bloom Energy rejects short-seller report on finances and supply chain
  url: https://www.streetinsider.com/Corporate+News/Bloom+Energy+rejects+short-seller+report+on+its+financials/26750598.html
  accessed_at: '2026-07-10T14:11:11Z'
hypothesis:
  statement: An activist short report (Hunterbrook) plus a same-day company
    rebuttal, with no independent corroboration and a fundamentally unverifiable
    core allegation (unaudited ~$20B backlog + China-scandium sourcing) on a
    1-3 session horizon, produces a near-coin-flip directional distribution
    whose expected value is negative in both directions after realistic
    round-trip friction (long approx -0.33R to -0.53R; short approx -0.30R to
    -0.45R with a fatter short-squeeze tail). Independently and dispositively,
    the paper-trading harness's BE price feed is a broken/incoherent
    deterministic stub in this environment, so no valid live entry anchor
    exists.
  direction: no_trade
  confidence: 88
plan:
  ticker: BE
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: No long — the reflexive dip-buy/reversion bounce is real but already
    inside the quant's scenario weighting and does not survive ~1.2% round-trip
    friction; Bloom's own prior accounting/backlog scrutiny history caps
    conviction in a clean rebuttal. No short — the 12% drop already happened
    (chasing, not a fresh edge), short-squeeze tail risk is fatter than the
    bleed case, and elevated post-report borrow costs further erode EV. The BE
    price feed in this harness is non-coherent (10-30x swings within hours) and
    was not used for any entry/exit target — its brokenness is an independent
    hard veto per the standing anchoring lesson, regardless of thesis. Revisit
    only if (a) the price feed is restored to a coherent live quote AND (b) a
    falsifiable, third-party-verifiable resolution of the scandium sourcing or
    backlog claims arrives (documented exoneration favors a small tactical
    long; independent corroboration favors a short, sized against squeeze
    risk).
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
  dissent: 'Bear vs. Quant over whether Bloom''s prior accounting/backlog
    scrutiny history (base rate A: P(allegation has substance | prior-scrutinized
    name), legitimately elevated) should shift the 1-3 session directional bet
    (base rate B: P(stock direction | gap-down + rebuttal + no corroboration),
    which Quant holds near a coin flip since substance resolves over
    weeks/quarters, not the trading window). Bear raised confidence to 78/100
    partly on this basis; Quant called it a conflation of two distinct base
    rates and held distribution nearly flat (32% bleed / 28% reversion / 40%
    chop). Bull separately noted Bear never named a specific prior incident and
    argued the reversion bucket is underweighted given Bloom''s independent
    data-center-power demand story. Unresolved: did allegation-substance
    predict short-horizon direction, or only long-horizon outcome? Preserved
    for post-mortem.'
  last_updated: '2026-07-12T08:10:00Z'
---

## Scouted 2026-07-10T14:11:11Z

## Researched 2026-07-12T08:10:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas independently converged on NO TRADE. Bull opened long/rebound
(confidence 42) but retreated to 25 after conceding the price-feed veto and
weak evidentiary weight of the same-day rebuttal signal. Bear held no-trade
throughout (70 -> 78), citing Bloom's prior accounting/backlog scrutiny history
and an unpriced compliance-tail risk (scandium sourcing vs. tariff/IRA-credit
eligibility). Quant (85/100 in the no-trade conclusion) computed negative EV
after costs on both long and short, and independently flagged the BE price
feed as a broken/incoherent deterministic stub (10-30x swings within hours)
that vetoes any entry regardless of thesis. Synthesis: no_trade, confidence 88.
Full debate with citations in `transcript.md`.
