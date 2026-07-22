---
id: 2026-07-21-amazon-q2-earnings
title: Amazon Q2 2026 earnings report
status: scouted
created: '2026-07-21T15:25:19Z'
event:
  type: earnings
  summary: Amazon reports Q2 2026 financial results July 30 2026 after market close
    covering AWS and retail margins
  impact_window: '2026-07-30'
tickers:
- AMZN
sources:
- title: 'Amazon Q2 2026 Earnings: What to Expect on 30 July 2026 - Finance Calendar'
  url: https://www.financecalendar.com/event/amzn-earnings-july-2026/
  accessed_at: '2026-07-21T15:25:19Z'
status: researched
hypothesis:
  statement: 'AMZN Q2 2026 earnings (2026-07-30 AMC) present a symmetric roughly
    6.5 percent implied one-day move with mild negative skew and no confirmed
    directional edge. Bull''s AWS re-rating, retail-margin, and ad-growth thesis
    is narrative-only and unconfirmed by consensus AWS numbers or options-implied
    move data; bear''s guidance-disappointment thesis (Q3 guidance, not the Q2
    print, is the real swing factor) is equally unconfirmed. Quant''s arithmetic
    on bull''s proposed 250/265 call spread (net debit about USD 3.20, breakeven
    about USD 253.20) shows a gross EV of about negative USD 0.45 per spread,
    roughly negative 0.55 to 0.65 percent net of costs -- the debit already
    embeds the expected move. The mirrored put-spread idea fares no better since
    downside skew is already priced into elevated put implied volatility. No
    positive-EV directional structure exists; the only positive-EV play (long
    straddle or strangle) is out of directional mandate. Reference price USD
    244.69 (twelvedata, 2026-07-22T19:44Z).'
  direction: none
  confidence: 74
plan:
  ticker: AMZN
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-22T19:44:00Z'
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: 'Unresolved crux is methodological, not directional: bear flagged that
    quant''s binary NO TRADE framing conflates away the nuance of defined-risk,
    skew-aware structures. Quant''s refutation of both the call spread and a
    mirrored put spread rests on estimated priors (implied move about 6.5
    percent, leg premiums, 50/50 up/down probability), not a live options
    chain, confirmed skew surface, or consensus AWS growth and margin numbers
    -- none of which arrived before Round 3. If the actual implied move were
    materially below about 6.5 percent, or genuine skew mispricing existed, a
    defined-risk structure could flip to positive EV, a scenario the current
    verdict cannot rule out on data, only on prior. Secondary unresolved item:
    whether Q3 guidance or the Q2 print itself dominates the reaction, flagged
    by bear but never quantified. Post-mortem should check AMZN''s actual
    implied move (via options data if available) and the real Q2 print/guidance
    outcome to adjudicate whether the abstention was correct.'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-22T19:44:00Z

Three-round panel (bull/bear/quant) converged on NO TRADE. No live web or options
data was available in the agent sandboxes, so all three personas worked from
priors: an assumed roughly 6.5 percent implied one-day earnings move, 50/50
up/down probability with a mild negative skew (AMZN off its lows, full
valuation), and general knowledge of AWS capex/margin dynamics and retail
margin trends rather than confirmed consensus numbers.

Bull opened proposing a defined-risk 250/265 call spread (confidence 42/100)
citing an AWS re-rating narrative, retail margin improvement, and
underweighted advertising growth, while explicitly flagging the absence of
hard consensus or options data. Bear opened skeptical (confidence 55/100),
flagging AWS capex/monetization-lag risk, retail margin compression risk, Q3
guidance (not the Q2 print) as the true swing factor, and valuation/positioning
risk already priced into the run-up. Quant opened with an EV calculation for a
naked directional trade: gross EV about 0 percent, skew-adjusted about negative
0.5 percent, net of costs about negative 0.6 to 0.7 percent, concluding the
only positive-EV structure (a long straddle or strangle) is out of directional
mandate, and recommended NO TRADE (confidence 72/100 in the process verdict).

In rebuttal, bull conceded bear's margin-compression point as a genuine gap in
the opening case, accepted quant's 50/50 calibration as fair given no hard
data, and worked through the arithmetic to conclude the call spread's cost
already embeds the same skew quant identified -- capped loss reduces the
variance of outcomes, not the negative expectancy per unit risked. Bull walked
confidence down from 42 to about 25. Bear reinforced its skepticism, agreeing
quant's math validated the no-trade instinct while noting a nuance: quant's
NO TRADE framing conflates "no naked directional trade" with "no structure at
all." Quant priced both bull's call spread (net debit about USD 3.20 on
AMZN at USD 244.69, breakeven about USD 253.20, expected terminal value about
USD 2.75 versus USD 3.20 cost, gross EV about negative USD 0.45 per spread)
and a mirrored put spread (downside skew already priced into elevated put
implied volatility, so no free EV there either), and held NO TRADE with
confidence rising to 74/100 since neither dissent overturned the verdict.

All three personas converged on NO TRADE by Round 2. This matches the
institutional lesson that when the strongest unrebutted dissent aligns with
quant's own EV math, the panel should synthesize to NO TRADE rather than
manufacture a quarter-size directional position. Full debate transcript
recorded in `transcript.md`.
