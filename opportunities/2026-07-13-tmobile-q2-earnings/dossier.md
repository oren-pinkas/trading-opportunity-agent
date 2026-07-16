---
id: 2026-07-13-tmobile-q2-earnings
title: T-Mobile Q2 2026 earnings
status: researched
created: '2026-07-13T20:41:00Z'
event:
  type: earnings
  summary: T-Mobile hosts Q2 2026 earnings call July 23; subscriber growth and Starlink-competition
    read for telecom
  impact_window: '2026-07-23'
tickers:
- TMUS
sources:
- title: T-Mobile to Host Q2 2026 Earnings Call on July 23, 2026
  url: https://www.t-mobile.com/news/stories/t-mobile-to-host-q2-2026-earnings-call-on-july-23-2026
  accessed_at: '2026-07-13T20:41:00Z'
hypothesis:
  statement: TMUS enters its Q2 print as a directional coin flip with no verifiable
    edge in either direction. The only live, hard evidence in the debate -- TMUS's
    own last-5-quarters earnings-reaction tape (Q1'25 -11.16%, Q2'25 +5.69%, Q3'25
    -3.12%, Q4'25 +0.95%, Q1'26 -2.26%) -- shows a 3-down/2-up split with a downside-skewed
    magnitude profile, even though the stock sits near its 52-week low (USD 187.44
    on 2026-07-15, vs a trailing 52-week range of roughly USD 184.48-261.87). That
    combination undercuts the bull's mean-reversion thesis (the 'washed-out longs
    get rewarded near the low' pattern does not appear in this name's own tape) without
    handing the bear a positive-expectancy short (the un-hedgeable positive tail --
    a beat-and-raise gap -- rules out a naked short). EV modeled with the panel's
    best-defensible inputs (P(up) 0.52-0.53, magnitudes +3.5%/-4.0% to -4.3%, ~0.15%
    costs) is negative for long (~-0.25% to -0.32%) and roughly flat for short (~-0.05%
    to +0.02%, but tail-blocked). Long breakeven requires P(up) >= ~0.571; nobody
    on the panel bridged the gap from 0.53 with new evidence.
  direction: no-trade
  confidence: 74
plan:
  ticker: TMUS
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  note: 'No position funded. Revisit only if: (1) live options-implied-vol/expected-move
    data becomes available and shows the ATM straddle priced below the ~4.6% realized
    mean-absolute earnings-day move (would support a defined-risk long-vol structure,
    not a directional bet); or (2) forward fundamentals emerge (guidance-raise cadence
    confirmation, T-Satellite monetization timeline, FWA net-add trajectory vs the
    ~12-13M ceiling, cable-MVNO ARPU trend) that resolve whether the 52-week-low positioning
    is a washed-out reversal setup or trend-continuation of deterioration. If reopened,
    anchor entry to a live quote fetched at the actual entry minute (not this reference
    price) and set entry/exit timestamps at least one minute inside the session boundary
    (19:59:00Z, not 20:00:00Z).'
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
  dissent: 'Bull vs bear on what the 52-week-low position means, left unresolved.
    Bull (round 2, confidence 42) reads USD 187.44 near the 52-week low as a washed-out,
    sentiment-exhausted reversal setup (NKE-style: punished longs get rewarded on
    a benign print). Bear (round 2, confidence 60) reads the same price as possible
    trend-continuation of genuine deterioration, noting the slide from ~USD 261 to
    ~USD 184 happened partly through earnings itself (3 of the last 5 reactions were
    negative) rather than a single macro air-pocket that would later mean-revert.
    Quant (round 2, confidence 72) supplied the decisive-but-not-dispositive fact
    -- TMUS''s own reaction tape is downside-skewed even at the low (largest single
    move -11.16%, 3-of-5 negative), which undercuts the bull''s mean-reversion pattern
    but is backward-looking reaction data, not forward fundamental data, so it cannot
    confirm the bear''s deterioration-continues causal claim either. Nobody pulled
    the forward-looking evidence (guidance cadence, T-Satellite monetization, FWA
    trajectory, options-implied expected move) that would discriminate between the
    two regimes. The actual 2026-07-23 reaction is the natural experiment that adjudicates
    this for the post-mortem.'
  last_updated: '2026-07-16T04:39:51Z'
---

## Scouted 2026-07-13T20:41:00Z

## Researched 2026-07-16T04:39:51Z — NO-TRADE

**Panel:** bull (sonnet, confidence 55->42), bear (sonnet, confidence 35->60), quant (opus, confidence 68->72). Bull and bear had no live market-data/web-search access this session and reasoned from structural priors, explicitly flagged and discounted accordingly; quant had live twelvedata access throughout and pulled TMUS's actual last-5-quarters earnings-day reactions (Q1'25 -11.16%, Q2'25 +5.69%, Q3'25 -3.12%, Q4'25 +0.95%, Q1'26 -2.26%; mean abs move ~4.6%, ex-tail ~3.0%; direction split 3-down/2-up) and confirmed the reference price (USD 187.44, 2026-07-15T19:59Z, twelvedata) sits ~2% off the 52-week low (~USD 184.48) and ~28% below the 52-week high (~USD 261.87). Bull's initial long thesis (T-Satellite/Starlink carrier-partner framing, postpaid net-add leadership, Home Internet/fiber diversification, guidance-raise cadence, buyback/dividend floor) and bear's initial short thesis (crowded premium-multiple long, cable-MVNO ARPU competition, FWA subscriber ceiling ~12-13M, Sprint-merger leverage/buyback-dependent EPS, satellite capex-without-monetization) both had their key valuation-level assumption resolved by quant's data: bear's 'crowded premium long near highs' framing was wrong (stock is near lows, favoring bull), but quant's own-tape evidence showed the near-low position does not carry a favorable reaction skew for TMUS specifically (undercutting bull's reversal read). Bull and bear's qualitative EV nudges (P(up) 0.52->0.53; down-magnitude -4.0%->-4.3%) roughly cancelled, leaving both directions sub-breakeven or tail-blocked after costs. Panel converged to NO-TRADE. Synthesized on opus, confidence 74 (weighted toward quant's live-data-anchored reasoning; bull/bear's independent convergence toward NO-TRADE despite opposite starting priors treated as corroborating signal, not averaged). Sources: T-Mobile Q2 2026 earnings-call announcement (t-mobile.com, accessed 2026-07-13T20:41:00Z); TMUS price and historical earnings-day reactions via twelvedata time_series API.
