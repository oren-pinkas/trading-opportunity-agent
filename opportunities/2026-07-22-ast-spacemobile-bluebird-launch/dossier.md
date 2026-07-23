---
id: 2026-07-22-ast-spacemobile-bluebird-launch
title: AST SpaceMobile BlueBirds 11-13 Orbital Launch
status: researched
created: '2026-07-22T20:01:24Z'
event:
  type: product
  summary: AST SpaceMobile targets a first-half-August orbital rideshare launch of
    BlueBirds 11, 12 and 13, expanding its direct-to-cell satellite constellation.
  impact_window: '2026-08-15'
tickers:
- ASTS
sources:
- title: 'BusinessWire: AST SpaceMobile Announces BlueBirds 11, 12, and 13 Orbital
    Launch in the First Half of August'
  url: https://www.businesswire.com/news/home/20260623653685/en/AST-SpaceMobile-Announces-BlueBirds-11-12-and-13-Orbital-Launch-in-the-First-Half-of-August
  accessed_at: '2026-07-22T20:01:24Z'
hypothesis:
  statement: "ASTS's BlueBirds 11/12/13 rideshare launch is a real but unconfirmed-date,
    low-edge catalyst; the impact window through 2026-08-15 captures at most a launch
    pop-then-fade, not deployment/commissioning value, and corrected EV is slightly
    negative pre-confirmation."
  direction: no-trade
  confidence: 70
plan:
  ticker: ASTS
  action: no-trade
  entry:
    time: conditional-pending-confirmation
    target_price: 62.00
    trigger: "Confirmed firm launch date (specific day, not 'first half of August')
      plus a stable primary-payload manifest; entry USD 61-63 on any pullback."
  exit:
    time: '2026-08-15T20:00:00Z'
    target_price: 56.00
    trigger: "Scale out at/into confirmed orbital insertion; hard stop below USD
      56; exit no later than 2026-08-15T20:00:00Z if activated."
  expected_profit_pct: null
research:
  strategy: debate-three-round-panel
  personas:
    bull: {model: sonnet, confidence: 52}
    bear: {model: sonnet, confidence: 20}
    quant: {model: opus, confidence: 71}
  dissent: "Is the event 'materially priced in' (bear) or a 're-rate on confirmation'
    catalyst (bull)? Quant's Round 2 self-correction (rideshare insertion is not
    commissioning) flipped the up-leg from +12% to +7% and EV from +1.3% to -0.9%
    net-negative. Bull remains the only persona net long-biased after both others
    self-corrected, and never revised the up-move probability quant flagged as too
    high (~65% implied vs ~35% base rate)."
  last_updated: '2026-07-23T04:44:18Z'
---

## Scouted 2026-07-22T20:01:24Z

## Researched 2026-07-23T04:44:18Z

Three-round panel debate (bull/bear/quant) converged on **no-trade**: the BlueBirds
11-13 launch announcement (2026-06-23) is a month old and largely priced in at USD
61.67 (2026-07-22T19:30Z ref print). Quant's Round 2 self-correction — recognizing
the 2026-08-15 impact window captures only a launch pop-then-fade, not deployment/
commissioning — flipped modeled EV from +1.3% to -0.9% net. Bull remained long-biased
(52/100) but conceded the EV haircut and dilution risk without rebutting quant's
probability critique. Plan stays inactive pending a confirmed firm launch date; see
`transcript.md` for the full debate.
