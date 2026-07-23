---
id: 2026-07-22-accenture-source-code-breach
title: Accenture confirms breach after threat actor claims stolen source code
status: researched
created: '2026-07-22T18:56:53Z'
event:
  type: regulatory
  summary: Accenture confirmed a security breach after a threat actor claimed to have
    stolen 35GB of source code and other data, raising client-disclosure and liability
    questions.
  impact_window: '2026-08-15'
tickers:
- ACN
sources:
- title: 'Hacked, leaked, and held for ransom: The worst breaches of 2026 so far'
  url: https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/
  accessed_at: '2026-07-22T18:56:53Z'
hypothesis:
  statement: "The Accenture (ACN) source-code breach is not a tradeable edge -- no confirmed
    materiality, only a single secondary source, and the dossier was accessed 16 days
    post-disclosure, well beyond the 4-6 day reaction half-life, leaving negative expected
    value (approx -0.37% after costs) with most of any base-rate move already reverted."
  direction: neutral
  confidence: 80
plan:
  ticker: ACN
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: "The only surviving disagreement is the bull's residual tail-risk optionality --
    that second-order client-contract-review or reputational drag could still surface a
    fresh downward catalyst into the 2026-08-15 window, which the base-rate EV model would
    systematically under-weight if this breach proves atypical in materiality. Judged too
    speculative and unfunded by evidence to trade, but worth checking in a post-mortem if
    ACN moves materially before 2026-08-15."
  last_updated: '2026-07-23T04:30:04Z'
---

## Scouted 2026-07-22T18:56:53Z

## Researched 2026-07-23T04:30:04Z

Three-round panel debate (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) converged
on NO TRADE. Quant's EV model (net EV approx -0.37% after costs) was decisive: cyber-breach
disclosures on large diversified IT-services names are near-noise events that mostly mean-revert
within 5-15 trading days, and this dossier was accessed 16 days post-disclosure -- past the
typical 4-6 day reaction half-life, with no price data confirming any overreaction to fade in
the first place. Bull conceded from 55 to 25 confidence; bear moved from 15 to 8. Full transcript
in `transcript.md`.
