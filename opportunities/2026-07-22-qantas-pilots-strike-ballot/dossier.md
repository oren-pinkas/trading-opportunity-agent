---
id: 2026-07-22-qantas-pilots-strike-ballot
title: Qantas long-haul pilot strike ballot opens July 27
status: scouted
created: '2026-07-22T17:49:00Z'
event:
  type: geopolitical
  summary: Australia's Fair Work Commission approved a strike ballot for Qantas's
    1,700 long-haul pilots, voting opens July 27, 2026; pilots are pushing for better
    work-life balance and pay above Qantas's 3% offer, raising risk of long-haul flight
    disruption.
  impact_window: '2026-07-27'
tickers:
- QAN.AX
sources:
- title: Qantas Faces Potential Long-haul Pilot Strike - LoyaltyLobby
  url: https://loyaltylobby.com/2026/07/20/qantas-faces-potential-long-haul-pilot-strike/
  accessed_at: '2026-07-22T17:49:00Z'
hypothesis:
  statement: 'The Jul 27 ballot-open is informationally empty (news public since
    Jul 20-22, results dont land until ~Aug 3, protected action then needs a 3
    business-day notice period before any stoppage), so it falls outside every
    persona proposed impact window and carries no fresh catalyst. Base-rate math
    (roughly 90 percent ballot passes times 40 percent any protected action times
    30 percent that action is a material long-haul strike, about 11 percent
    overall) plus the 2011 precedent (a far more severe full grounding that cost
    under 0.5 percent of revenue and saw the stock rise 5.5 percent on
    resolution) argue disruption risk is small and cheap for Qantas to defuse
    (roughly a 1 percent pay-offer gap). No persona could obtain real QAN.AX
    price data (toa price with twelvedata returned HTTP 404 at every tested
    timestamp), so no confirmed dislocation exists to trade. The only
    structurally sound edge is a conditional mean-reversion long on a verified
    over-reaction to the Aug 3 ballot result, armed but not active.'
  direction: no_trade
  confidence: 72
plan:
  ticker: QAN.AX
  action: no_trade
  entry:
    time: '2026-08-03T00:00:00Z'
    target_price: null
  exit:
    time: '2026-08-12T00:00:00Z'
    target_price: null
  expected_profit_pct: 0
  notes: 'Armed conditional only, not a live position. If ballot result confirms
    PASS on or around Aug 3 2026 AND QAN.AX prints a verified same-session move
    of 3 percent or more down versus prior close (real market data required, no
    stub) AND no protected-action strike notice specifying an actual stoppage
    date has been filed, then enter half-unit long QAN.AX at that verified
    dislocation. Exit at plus 3 percent from entry or by Aug 12 2026, whichever
    first. Invalidation: a strike notice specifying a stoppage date filed at any
    time (exit immediately or do not enter), OR minus 3 percent from entry
    (hard stop), OR entry price unverifiable via real market data (void the
    trade), OR no qualifying dislocation by Aug 7 2026 close (expires, remains
    no trade).'
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
  dissent: 'Direction of the armed Aug 3 conditional trade is unresolved. Bear
    conceded on timing and magnitude but never fully retracted the directional
    call: if the ballot passes by a wide margin and the union signals intent to
    file notice, a same-session drop is not an over-reaction to fade but the
    start of a real repricing, and the armed long would be buying into a falling
    knife. The "no strike notice filed" entry guard is thin, since notice can
    follow entry by days, inside the holding period, leaving the minus 3 percent
    stop as the only backstop. Post-mortem test: if the Aug 3 trigger fires,
    check whether a strike notice followed within the 8-day hold and whether the
    stop or the profit target hit first.'
  last_updated: '2026-07-24T01:10:00Z'
---

## Scouted 2026-07-22T17:49:00Z

## Researched 2026-07-24T01:10:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). No persona
could obtain real QAN.AX price data (toa price with twelvedata returned HTTP 404
at every tested timestamp for this ticker), a material unresolved gap flagged
throughout. Panel converged on NO TRADE for the Jul 27 ballot-open (confidence
72): Quant (78, then 74) held NO TRADE from base-rate and magnitude reasoning
that the ballot-open date is informationally empty and disruption risk is small;
Bull (35, then 30) and Bear (35, then 25) both opened with directional Jul 27
trades but conceded the timing flaw and retreated toward NO TRADE, converging
instead on an armed, data-contingent, half-size mean-reversion long staged for
the Aug 3 ballot-result window that self-voids if the price feed stays broken.
Full debate with citations in `transcript.md`.
