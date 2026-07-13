---
id: 2026-07-13-okyo-urcosimod-fda-phase3
title: OKYO Pharma gets positive FDA feedback, advances urcosimod to Phase 3
status: researched
created: '2026-07-13T05:37:17Z'
event:
  type: regulatory
  summary: OKYO announced positive FDA Type D meeting feedback endorsing a single-trial
    registration pathway for urcosimod in neuropathic corneal pain, accelerating the
    NEPTUNE Phase 3 pivotal trial.
  impact_window: '2026-07-08'
tickers:
- OKYO
sources:
- title: OKYO Pharma Reports Positive Feedback from FDA Type D Meeting and Accelerates
    Urcosimod into Global Phase 3 Pivotal Trial for Neuropathic Corneal Pain
  url: https://www.globenewswire.com/news-release/2026/07/08/3323947/0/en/okyo-pharma-reports-positive-feedback-from-fda-type-d-meeting-and-accelerates-urcosimod-into-global-phase-3-pivotal-trial-for-neuropathic-corneal-pain.html
  accessed_at: '2026-07-13T05:37:17Z'
hypothesis:
  statement: The tradable edge in OKYO's positive FDA Type D feedback is already gone.
    The event pop (+12.5% on 2026-07-08 to $1.80) round-tripped ~80% in a single
    session to $1.6422 by T+1, falsifying a multi-day drift thesis and leaving only
    ~2.5% of residual downside to the $1.60 pre-event level for a fade/short. Type D
    feedback is non-binding, the next real catalyst (NEPTUNE readout) is undated and
    12+ months out, and a dilutive raise is the most probable near-term corporate
    action for a cash-burning nano-cap that just committed to a global pivotal trial.
    Compounding all of this, no 1-minute bar is printable for OKYO today (2026-07-13),
    a binding, direction-independent execution constraint. Both directional EVs are
    negative net of friction (long approx -5% to -10%, short approx -3% with a fat
    squeeze/borrow tail). No-trade is the correct posture today.
  direction: no_trade
  confidence: 88
plan:
  ticker: OKYO
  action: no_action
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
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
  dissent: 'Whether "no_trade" means "no edge with current data" (temporary,
    re-openable) or "no edge in this name, period." Bull and Bear both left the door
    open to a future trade -- bull wants a small capped-risk long optionality position
    if liquidity returns in the $1.55-1.70 zone with a dated NEPTUNE/FDA-correspondence
    catalyst inside 1-3 months and no dilution; bear wants an event-triggered short-vol
    trade if the stock pops again on no new fundamental news with cheap borrow
    available. Quant explicitly repriced the bull''s "buy-now-hold-for-next-catalyst"
    as a separate trade at EV approx -9% to -10% net -- worse than fading the
    already-dead pop -- because an undated catalyst means paying carry/dilution
    overhang with no dated exit, and held that dilution risk improves a short''s
    central case but does not fix its squeeze/borrow tail. The debate did not resolve
    whether restored liquidity plus a dated catalyst would actually flip long EV
    positive, or whether dilution overhang keeps it structurally negative regardless
    of entry price -- that is the open question for a future revisit.'
  last_updated: '2026-07-13T20:20:00Z'
---

## Scouted 2026-07-13T05:37:17Z

## Researched 2026-07-13T20:20:00Z — NO_TRADE

Three-round panel debate (bull/bear/quant, synthesizer opus) converged on **no_trade /
no_action** (confidence 88). Verified real prices (`toa price OKYO <ts> --provider
twelvedata`, independently re-confirmed by the orchestrator): $1.60 pre-announcement
(2026-07-07) -> $1.80 on the 2026-07-08 announcement day (+12.5% intraday) -> $1.6422
by T+1 (+2.5% vs pre-event -- roughly 80% of the pop had already faded within a single
session). No 1-minute bar exists for 2026-07-10 or 2026-07-13 (today), an illiquidity
gap that is itself disqualifying for any position size regardless of direction.

Bull opened long (structural regulatory de-risking, thin-float overreaction pattern)
but conceded in Round 2 that the momentum-drift trade was "dead on the data" once
shown the real fade, downgrading to a token, capped-risk (<=0.25-0.5% NAV) optionality
position contingent on restored liquidity and a dated future catalyst. Bear opened
avoid/fade (Type D feedback non-binding, dilution-into-strength risk, thin-float
round-trip risk) and had the fade thesis validated faster than expected, but agreed a
fresh short is now poor risk/reward too -- most of the give-back already happened,
leaving little room and a fat squeeze tail. Quant priced every variant explicitly:
riding the fade nets to about -5.2%, an outright short nets to about -3.0% with
squeeze/borrow tail risk, and the bull's "hold for the next catalyst" reframe prices
worse (-9% to -10%) once the undated dilution-window carry is included. Full
transcript: `transcript.md`.
