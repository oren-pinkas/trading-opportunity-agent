---
id: 2026-07-16-ge-aerospace-q2-fy26
title: GE Aerospace Q2 FY26 earnings
status: researched
created: '2026-07-07T22:42:46Z'
event:
  type: earnings
  summary: GE Aerospace reports Q2 2026 results on July 16; aftermarket demand and
    2026 guidance in focus.
  impact_window: '2026-07-16'
tickers:
- GE
sources:
- title: MarketBeat GE earnings
  url: https://www.marketbeat.com/stocks/NYSE/GE/earnings/
  accessed_at: '2026-07-07T22:42:46Z'
hypothesis:
  statement: No executable edge. GE Aerospace's Q2 FY26 payoff is the pre-open gap
    on 2026-07-16, which the simulator cannot fill (regular-session 1-min equity bars
    only, no overnight/gap/options fills). The only sim-legal vehicle — a post-open
    intraday continuation long — has no reliable positive intraday autocorrelation
    and computes to negative EV after costs (~-0.25% to -0.35%), with a tight stop
    inside ~1-sigma event-day noise. Fundamental bias is mildly long (LEAP aftermarket
    ramp, services-margin annuity, sell-side re-rating) but not tradable in this simulator.
  direction: none
  confidence: 80
plan:
  ticker: GE
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
  dissent: 'Bull vs Quant: whether post-open intraday drift on a confirmed guidance-raise
    gap-up is a real positive-EV continuation edge (Bull: thin PEAD/gap-and-go premium,
    conf 40) or noise indistinguishable from zero-to-negative that a tight stop turns
    negative after costs (Quant, conf 82). Unresolvable without GE-specific open-to-close-conditional-on-up-gap
    drift stats (t-stat > 2). Latent secondary disagreement: even if gaps were fillable,
    Bull goes WITH the gap (continuation) while Bear FADES a gap-up (buy-the-rumor
    exhaustion at ~40x) — opposite directional calls on the same event.'
  last_updated: '2026-07-07T23:35:00Z'
---

## Scouted 2026-07-07T22:42:46Z

## Researched 2026-07-07T23:35:00Z — NO-TRADE

Three-round panel (bull sonnet / bear sonnet / quant opus; synthesizer opus). Anchor GE = 344.49 @ 2026-07-07T19:59Z. Verdict NO-TRADE on two independent grounds: (1) the information-rich directional payoff is the 2026-07-16 pre-open gap, which the sim cannot fill; (2) the one sim-legal intraday continuation long is negative-EV after costs, and a naked un-hedgeable earnings bet trips the institutional no-trade filter (no options available). Bull withdrew its unconditional long on rebuttal (58 -> 40, only a thin conditional gap-and-go contingent on unknowable/unfillable info); bear 32; quant 82. Fundamental long thesis intact on a multi-day horizon but inexpressible here. Full debate in transcript.md.
