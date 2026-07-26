---
id: 2026-07-23-spyre-skyline-phase2-readout
title: Spyre Therapeutics SKYLINE Part A Phase 2 IBD/UC Topline Data
status: researched
created: '2026-07-23T05:29:18Z'
event:
  type: product
  summary: Spyre's SPY003 Phase 2 SKYLINE Part A topline data in inflammatory bowel
    disease and ulcerative colitis due late July 2026
  impact_window: '2026-07-31'
tickers:
- SYRE
sources:
- title: Biotech Catalyst Calendar - July 2026 - ClinicalInvestor
  url: https://www.clinicalinvestor.com/catalyst/2026-07
  accessed_at: '2026-07-23T05:29:18Z'
hypothesis:
  statement: >-
    The SYRE/SPY003 SKYLINE Part A "catalyst" fails on two independent grounds
    before direction ever matters: the 2026-07-31 date is unconfirmed (sourced
    only from a third-party catalyst-calendar aggregator, not a Spyre IR
    release, 8-K, or clinicaltrials.gov update), and the tape does not
    corroborate an imminent binary event -- SYRE printed USD 99.89-102.90
    across 2026-07-22 to 2026-07-24 at roughly 1 pct per day realized vol, with
    no pre-event vol or volume ramp of the kind names five sessions from a
    Phase 2 topline normally show. Applying the panel's agreed distribution
    (P(readout lands by 07-31) revised 0.55 to 0.45; conditional P(positive)
    0.35 at plus 35 pct, P(mixed) 0.35 at minus 12 pct after an IBD/UC
    crowding adjustment, P(negative) 0.30 at minus 35 pct) gives conditional
    EV of roughly minus 2.45 pct and unconditional EV of roughly minus 1.65
    pct gross, minus 2.25 pct net of about 0.6 pct round-trip costs.
    Break-even requires P(positive) near 0.39-0.40 versus the 0.35 nobody
    could source from SPY001/SPY002 precedent. A cash-equity position is only
    paid the signed mean, not the gross expected absolute move, so the bull's
    wide-tail framing does not rescue the trade.
  direction: none
  confidence: 78
plan:
  ticker: SYRE
  action: no-trade
  entry:
    time: '2026-07-31T13:29:00Z'
    target_price: null
  exit:
    time: '2026-07-31T20:00:00Z'
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
  dissent: >-
    The strongest unresolved split is how to read the flat pre-event tape.
    Bear and quant treat SYRE's roughly 1 pct per day realized vol as evidence
    the calendar date is soft and used it to revise P(lands by 07-31) down
    from 0.55 to 0.45. Bull reads the identical tape as normal vol compression
    into a date-certain binary catalyst, not a signal the date is wrong, and
    argues a "no positioning" inference from equity vol alone is unfounded
    without options data -- which nobody in the panel could fetch. The verdict
    does not flip on this (even at P(lands)=0.55 conditional EV is still
    negative), but the stated confidence does depend on it. Post-mortem test:
    did Spyre publish SPY003 SKYLINE Part A topline on or before 2026-07-31?
    If yes, the panel over-weighted an absence-of-evidence signal into a
    probability revision -- a bias worth flagging for every calendar-sourced
    biotech dossier. If no, promote "third-party-calendar date plus no
    pre-event vol build equals downgrade before debating direction" to a
    standing scout-time filter.
  last_updated: '2026-07-26T02:41:58Z'
---

## Scouted 2026-07-23T05:29:18Z

## Researched 2026-07-26T02:41:58Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). SPY003 SKYLINE
Part A IBD/UC topline is calendar-sourced only (ClinicalInvestor aggregator, not a
Spyre primary release) with impact window 2026-07-31. Price checks (twelvedata):
SYRE traded USD 99.89-102.90 across 2026-07-22 to 2026-07-24, ~1 pct/day realized
vol -- flat for a name supposedly five sessions from a binary Phase 2 readout. The
QUANT's EV calibration was decisive: assumed P(readout lands)=0.45 (revised down
from 0.55 on the flat-tape signal), conditional P(positive)=0.35 (+35 pct),
P(mixed)=0.35 (-12 pct), P(negative)=0.30 (-35 pct) gives conditional EV ~-2.45 pct,
unconditional ~-2.25 pct net of costs; break-even needs P(positive) ~0.39-0.40,
unsupported by any cited SPY001/SPY002 precedent. BULL's wide-implied-move argument
(E|move| ~14.5 pct) does not rescue a cash-equity long, which is only paid the
signed mean. BEAR's provenance and crowding concerns were adopted into the numbers
rather than left qualitative. Verdict: NO-TRADE pre-catalyst, watchlist only. A
post-print reaction trade is gated on (1) primary-source (IR/8-K/clinicaltrials.gov)
date+data confirmation, (2) disclosed efficacy substance (endpoint, Part A n,
remission rate vs. comparator), (3) toa price --provider twelvedata resolving
cleanly at 2026-07-31T13:29Z, 13:35Z, and 20:00Z, and (4) a stated non-gap drift
thesis, capped at 25 pct of normal unit size. Flips to a pre-catalyst long only on
company-issued date confirmation (P(lands) >= 0.85), SPY001/SPY002 precedent
supporting P(positive) >= 0.40, and pre-event realized vol > 3 pct/day. Full debate
with citations in `transcript.md`.
