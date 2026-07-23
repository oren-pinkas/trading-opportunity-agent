---
id: 2026-07-22-draftkings-prediction-market-share-loss
title: DraftKings loses user momentum to Kalshi/Polymarket during World Cup
status: researched
created: '2026-07-22T17:49:00Z'
event:
  type: earnings
  summary: DraftKings daily active users fell 36% from their June 15 peak while Kalshi
    (38% audience share) and Polymarket (13%) grew during World Cup betting; DraftKings'
    own DKeX exchange holds ~0.01% notional volume share; Q2 2026 results due Aug
    6 will show whether prediction-market competition is denting the core sportsbook.
  impact_window: '2026-08-06'
tickers:
- DKNG
sources:
- title: Prediction markets swell to 27% of sports bets during World Cup - Fortune
  url: https://fortune.com/2026/07/19/prediction-markets-sports-betting-world-cup-kalshi-polymarket-fan-duel-draftkings/
  accessed_at: '2026-07-22T17:49:00Z'
hypothesis:
  statement: 'The DKNG prediction-market share-loss story is genuine but already public
    since 2026-07-19, resting on a peak-to-trough DAU figure that is at least partly
    World Cup seasonality, plus a DKeX 0.01% notional-share data point immaterial
    to Q2 revenue and arguably the wrong metric for the actual risk (users leaving
    DraftKings'' core book for Kalshi/Polymarket, not DraftKings'' own exchange underperforming).
    Neither a long nor a short is supported: the quant''s defined-risk short EV fell
    from +0.8% to net-negative (-0.16%) between rounds with no new data, the bull''s
    oversold-relief-rally pattern is missing its required precondition (no evidence
    DKNG is near a 52-week low or de-risked into the print), and the one structurally
    sound idea (short-vol / IV-crush harvest into the Aug 6 print) cannot be priced
    or sized without a verified options chain and IV-rank, which the panel does not
    have.'
  direction: no-trade
  confidence: 78
plan:
  ticker: DKNG
  action: no-trade
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
  dissent: Bull vs. bear/quant on whether the share-shift is structural or seasonal,
    and conditionally, whether a verified stretched put skew would justify a long.
    The bull's Round 2 fallback -- a vol/oversold mean-reversion play, live if real
    IV skew were confirmed stretched to the put side -- was never resolved because
    the panel had no options data to confirm or refute it. The bear counters the core
    risk (users defecting to cheaper, CFTC-regulated Kalshi/Polymarket) is structural
    and the DAU dip may be an early signal, not noise. The abstention was forced by
    a missing IV/positioning data gap, not by settling the seasonal-vs-structural
    question. If the Aug 6 print produces a large move on a vol crush, revisit whether
    a verified options chain would have converted this into a tradeable short-vol
    setup.
  last_updated: '2026-07-23T16:30:06Z'
---

## Scouted 2026-07-22T17:49:00Z

## Researched 2026-07-23T16:30:06Z — NO-TRADE

Panel: bull, bear, quant (three-round-panel). Full transcript: transcript.md.

Verdict: NO TRADE. Quant's defined-risk short EV moved from +0.8% (Round 1, priors P(down)=42%/P(up-flat)=58%) to -0.16% (Round 2, priors 41%/59%) with no new data -- below the ~2% no-trade threshold and then negative. Bull's relief-rally thesis (negative narrative already priced in ahead of the Aug 6 print, so a non-confirming print triggers a bounce) borrows the conclusion of a prior lesson without its precondition: nothing in the dossier places DKNG near a 52-week low or otherwise de-risked. Bear's structural share-shift case (Kalshi 38% / Polymarket 13% audience share during the World Cup vs. DKeX's 0.01% notional share) is directionally plausible but concedes the narrative has been public since 2026-07-19 (partially priced in) and carries fat right-tail risk on a naked short if management reframes the DAU dip or offsets with iGaming/hold-rate strength. No verified options chain, IV-rank, or 52-week-range data was available to any panelist; the only positive-EV structure identified (short-vol into post-print IV crush) is out of mandate and unpriceable without that data. Per institutional lesson, logged as NO TRADE rather than manufacturing a token directional position for the learning loop. The DKNG price quote returned by `toa price` ($225.84) was flagged by all three panelists as unverified stub data and never anchored to.
