---
id: 2026-07-07-apple-fiscalq3-earnings
title: Apple fiscal Q3 2026 earnings
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: earnings
  summary: Apple reports Jul 30; iPhone demand and services growth drive the print.
  impact_window: '2026-07-30'
tickers:
- AAPL
sources:
- title: EarningsWhispers calendar
  url: https://www.earningswhispers.com/calendar
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: AAPL FQ3-2026 is a priced-in beat near the 52-wk high (~$317); weekly
    implied ~6% vs realized ~1.8-2.6% and an un-hedgeable Cook-succession/margin tail
    leave direction a slight-down coin-flip with no exploitable edge.
  direction: short
  confidence: 44
plan:
  ticker: AAPL
  action: no-trade
  entry:
    time: '2026-07-31T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-31T19:59:00Z'
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
  dissent: 'Bull holds symmetric magnitude flips EV positive and Cook''s telegraphed
    last call de-risks a key-man overhang; Quant/Bear counter that IV at 62nd pctile
    plus the succession tail keep net EV negative. Unresolved: is the move symmetric
    or down-skewed?'
  last_updated: '2026-07-07T22:05:35Z'
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:05:35Z — NO-TRADE

Bull argued a China iPhone-17 supercycle (FQ2 China +38%, Services $30.98B +16.3%, total rev $111.2B) and PT hikes (Citi $330, MS $315) drive momentum continuation. Bear and Quant showed the beat is already consensus (EPS $1.89 +20.4%): P/E ~37x, IV ~27% at the 62nd pctile pricing a ~6% weekly move vs ~1.8-2.6% realized, with forward China deceleration (UBS -19% by May) already priced. Quant's EV math is decisive: directional gap gross ~+0.13% minus 0.3-0.5% costs = net negative, adverse-tail-to-edge >>7-8x amplified by the un-hedgeable Cook-succession tail (reportedly his last call). Confidence ~44 with negative net EV and an un-hedgeable tail trips the institutional no-trade filter. VERDICT: NO-TRADE, nominal slight-down lean; the only positive-EV alternative (short-vega iron condor harvesting implied-over-realized) is not initiated because the vol is expensive for a reason this quarter.
