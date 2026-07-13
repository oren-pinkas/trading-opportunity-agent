---
id: 2026-07-13-amd-advancing-ai-event
title: AMD's Advancing AI 2026 event sets up Q2 earnings catalyst
status: researched
created: '2026-07-13T19:27:39Z'
event:
  type: product
  summary: AMD hosts its Advancing AI 2026 event July 22-23 in San Francisco ahead
    of Q2 earnings expected around Aug 4, with the Zen 6 EPYC launch and AI accelerator
    roadmap in focus after the stock's 130% YTD surge.
  impact_window: '2026-07-22'
tickers:
- AMD
sources:
- title: AMD Stock Forecast | Advancing AI Event, Q2 Earnings
  url: https://capital.com/en-int/market-updates/amd-stock-forecast-23-06-2026
  accessed_at: '2026-07-13T19:27:39Z'
hypothesis:
  statement: AMD's Advancing AI event (Jul 22-23) is a self-hosted, roadmap-heavy
    promotional event whose informational content is largely pre-priced after a
    +141% YTD run. Base rates for AMD product events cluster around plus-or-minus
    3-5% moves; the naive-long EV at roughly $546 is slightly negative net of costs
    (about -0.25% to -0.30%), and the fat right-tail (a named-hyperscaler dollar
    commitment could gap AMD +10-15%) makes a naked short uninvestable. A defined-risk
    sell-the-news fade only earns positive EV if options IV and skew confirm the
    event is crowded and rich, and that data was never obtained. The real information
    event is the Aug 4 earnings print, a separate and independently-sized decision
    out of scope for this dossier. No trade around the July 22-23 event itself.
  direction: no_trade
  confidence: 72
plan:
  ticker: AMD
  action: pass
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
  dissent: The bull's unresolved objection is that the quant's own fat-right-tail,
    the same asymmetry used to reject a naked short, logically argues for a small
    convex defined-risk long (a call spread) rather than a full pass. The quant
    counters that the naive-long net EV is negative and that a convex long only
    pays off if implied vol is cheap versus history, which was never measured.
    This stayed unresolved because the deciding input, options IV term structure
    and skew plus any hyperscaler order confirmation, was never pulled. Post-mortem
    should check whether pre-event IV was cheap or rich relative to the historical
    plus-or-minus 3-5% event-day base rate, since that single data point would
    have told the debate which direction, if any, actually had edge, rather than
    defaulting to pass on a data gap.
  last_updated: '2026-07-13T21:05:00Z'
---

## Scouted 2026-07-13T19:27:39Z

## Researched 2026-07-13T21:05:00Z

Three-round panel debate (bull/bear/quant, synthesized by opus). Bull opened long
on the double-catalyst (event + Aug 4 earnings) setup but conceded most ground in
rebuttal after re-pulling prices with `--provider twelvedata` and engaging quant's
EV math; bear and quant independently converged on "already priced in, stalling
momentum" via different methods (technical re-test vs historical base-rate/EV).
All three ended agreeing no one should hold a directional position through both
catalysts. Verdict: no_trade, confidence 72, action pass. The bull's Round-1 price
series was corrupted by the known `toa price` stub-data bug (no `--provider
twelvedata`); always pull with that flag. Full transcript in `transcript.md`.
Central dissent: a tiny defined-risk position (either direction) might have cleared
the bar with options IV/skew data, which was never pulled — flagged for post-mortem.
