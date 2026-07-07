---
id: 2026-07-07-delta-q2-earnings
title: Delta Air Lines Q2 2026 earnings
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: earnings
  summary: Delta reports before Fri Jul 10 open, unofficial kickoff of airline earnings;
    demand/fares guide read-through.
  impact_window: '2026-07-10'
tickers:
- DAL
sources:
- title: Kiplinger earnings calendar
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: 'Stand-aside: DAL near 52-wk highs prices a beat-vs-Street that is really
    a beat-vs-lowered-guide; edge ~0, adverse-tail/edge ~65x, spot/IV data unverifiable.'
  direction: neutral
  confidence: 40
plan:
  ticker: DAL
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-07T22:07:00Z'
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
  verdict: no-trade
  confidence: 40
  lessons_applied:
  - '2026-06-25-nike-q4-fy26: no-trade filter when conf<=45 + net EV<2% + tail/edge>>7-8x'
  - '2026-06-25-nike-q4-fy26: discount negative base rates near 52-wk low (did NOT
    apply — DAL near highs)'
  - '2026-07-02-tesla-deliveries: intraday exit >=1min inside session boundary'
  dissent: Whether faint sell-side edge exists (premium-selling into IV crush at highs)
    or whether the guide-vs-Street gap makes direction unmeasurable given contradictory
    spot/IV data.
  transcript: transcript.md
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:07:00Z
Verdict: NO-TRADE (neutral, confidence 40). Three-round panel converged on stand-aside — net EV ~flat, ~65x adverse-tail-to-edge, unverifiable spot/IV, simulator price is per-minute noise. Full debate in transcript.md.
