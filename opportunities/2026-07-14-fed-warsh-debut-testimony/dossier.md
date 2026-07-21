---
id: 2026-07-14-fed-warsh-debut-testimony
title: Fed Chair Warsh delivers debut congressional testimony
status: researched
created: '2026-07-12T08:53:04Z'
event:
  type: economic
  summary: New Fed Chair Kevin Warsh gives his first semiannual monetary policy testimony
    to the House (Jul 14) and Senate (Jul 15), 90 minutes after June CPI, with rate
    path, inflation, and crypto regulation all in focus.
  impact_window: '2026-07-15'
tickers:
- IEF
sources:
- title: Fed Chair Warsh to Testify Before Congress July 15 - BigGo Finance
  url: https://finance.biggo.com/news/61688676-c0ec-4382-b752-11b26e01a3db
  accessed_at: '2026-07-12T08:53:04Z'
hypothesis:
  statement: Warsh's debut testimony carries genuine first-appearance uncertainty,
    but it is two-sided (a volatility story, not a directional one), any testimony-
    attributable IEF move is small relative to base rates (~15-35bps typical), and
    the move is confounded by June CPI released ~90 minutes prior. No directional
    edge over what the confirmation record already priced in was established across
    three debate rounds. Best directional variant (long) nets approximately -0.10
    to -0.11 percent after ~5bps costs; forced-directional math favors short at
    roughly 0.00 percent net. Neither clears the cost hurdle.
  direction: none
  confidence: 72
plan:
  ticker: IEF
  action: no-trade
  entry:
    time: '2026-07-14T14:35:00Z'
    target_price: null
  exit:
    time: '2026-07-15T20:00:00Z'
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
  dissent: "Whether Warsh's reaction function was actually priced in during Senate
    confirmation, or whether adversarial House testimony Q&A could produce a genuine
    unpriced surprise. The bull argues confirmation hearings are courtesy theater
    while House Q&A is adversarial and unscripted, exactly where debut surprises
    originate; neither bear nor quant evidenced the 'priced in' premise either. This
    is non-load-bearing for the no-trade decision because quant's EV math reaches
    skip independently of that premise (modal outcome is a non-event even after
    widening tails to honor the bull's variance argument) - but if this trade is
    post-mortemed as a miss, this is where to look: whether the debut reference
    class deserved fatter, asymmetric (not merely wider) tails than quant assigned."
  last_updated: '2026-07-21T08:45:00Z'
---

## Scouted 2026-07-12T08:53:04Z

## Researched 2026-07-21T08:45:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), restricted to
this opportunity alone. Bull proposed long IEF anchored at USD 93.68
(2026-07-14T14:35Z), thesis being that a new chair's debut testimony has outsized
informational value since markets have no track record pricing his reaction
function. Bear and quant independently converged on no-trade for convergent-but-
distinct reasons: bear argued the "outsized informational value" claim was never
evidenced and Warsh's leanings were largely litigated during Senate confirmation;
quant's explicit EV math (scenario probabilities for hawkish/dovish/in-line
outcomes) returned negative net EV for long (~-0.10 to -0.11 percent after costs)
and ~0.00 percent for short even after widening both tails to accommodate the
bull's variance argument - the widening left the math pointing short, the opposite
of bull's call. Bull's own CPI-contingency ("void or flip if CPI surprises hot")
concedes the position is really a CPI bet wearing a testimony costume, with the
proximate driver sitting outside the stated thesis. The two round-1 anchor prices
(USD 93.68 vs USD 93.60, ~0.09 percent apart within one session) are themselves the
same order of magnitude as the purported signal. Verdict: NO-TRADE (not scheduled,
not simulated). Full debate with citations in `transcript.md`.
