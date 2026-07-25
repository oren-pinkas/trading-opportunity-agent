---
id: 2026-07-23-houthi-red-sea-saudi-blockade
title: Houthi blockade of Saudi Red Sea ports widens Iran war
status: researched
created: '2026-07-23T22:07:07Z'
event:
  type: geopolitical
  summary: Houthis attacked two Saudi oil tankers in the Red Sea and announced a naval
    blockade of Saudi ports, opening a new front beyond the Strait of Hormuz and pushing
    oil above USD 100/bbl.
  impact_window: '2026-08-15'
tickers:
- STNG
- BNO
sources:
- title: Trump says U.S. will hold Iran responsible for Houthi attacks after oil tankers
    targeted in Red Sea - CNBC
  url: https://www.cnbc.com/2026/07/23/iran-war-us-trump-houthis-red-sea-oil.html
  accessed_at: '2026-07-23T22:07:07Z'
hypothesis:
  statement: >-
    The Houthi blockade of Saudi Red Sea ports is, on currently available
    information, a priced-and-faded headline rather than a tradable tanker-rate
    catalyst. STNG's day-one round trip (79.25 pre-event close to 79.99 open to
    79.36 close, +0.14% net, ~85% of the pop given back) and BNO's wrong-signed
    -1.73% match the false-positive signature of the single-headline chokepoint
    reference class (Gulf of Oman 2019, Abqaiq 2019, Soleimani 2020, April 2024
    Iran-Israel, June 2025 Hormuz scare), all of which mean-reverted in 24-72h. The
    one durable precedent (Dec 2023 Red Sea diversion) re-rated tanker equities only
    weeks after confirmed rerouting, meaning the bull mechanism (port-of-call
    war-risk at Saudi terminals lifting day-rates) is not yet observable and cannot
    be distinguished from noise today. P(durable to 2026-08-15) is approximately
    0.22 against a break-even of 25.9%; the stop required to bound risk over a
    three-week hold consumes the entire edge.
  direction: none
  confidence: 78
plan:
  ticker: STNG
  action: no-trade
  entry:
    time: '2026-07-23T22:07:07Z'
    target_price: null
  exit:
    time: '2026-08-15T00:00:00Z'
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
    Whether the freight/port-risk transmission channel bull argues for is the
    correct reference class, or whether quant's supply-shock base rate (Gulf of
    Oman, Abqaiq, Soleimani, Iran-Israel, Hormuz 2025 - all faded in 24-72h) governs
    instead. Bull distinguishes bear's 2024 US Navy escort precedent (protects
    transit lanes) from this event (port-of-call risk at Saudi terminals, which
    escorts do not cover) and calls this falsifiable; bear/quant counter that "give
    it three weeks" is unfalsifiable in real time and, per quant, structurally
    untestable inside simulate-plans specifically, since it has no path-dependent
    monitoring and "wait for confirmation" collapses into holding naked risk to
    expiry. Unresolved because the deciding evidence (war-risk insurance quotes for
    Saudi port calls, Kpler/AIS berth-level rerouting data) was not obtainable
    inside the panel. Quant's own confidence that no-trade beats a trigger-conditional
    entry was only 25%, so the recorded flat verdict is a harness limitation, not a
    settled analytical preference. Testable post-mortem: did any of the four named
    triggers (STNG 3 consecutive closes >79.99; TC2/TC5 rate print +15% w/w;
    sustained Brent backwardation; documented war-risk premium repricing or Kpler/AIS
    Saudi port avoidance) print before 2026-08-15, and if so did STNG re-rate on the
    multi-week lag the bull's Dec 2023 analogy predicts?
  last_updated: '2026-07-25T12:04:51Z'
---

## Scouted 2026-07-23T22:07:07Z

## Researched 2026-07-25T12:04:51Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), researched in
isolation from all other opportunities. STNG round-tripped on the headline (79.25
pre-event close, +0.9% pop to 79.99 open, faded to 79.36 close, +0.14% net) and BNO
moved the wrong sign entirely versus the dossier's "oil above USD 100/bbl" claim
(53.42 to 52.495, -1.73%) — the false-positive signature of prior single-headline
chokepoint shocks (Abqaiq, Soleimani, the April 2024 Iran-Israel exchange, the June
2025 Hormuz scare), none of which sustained beyond 24-72h except the Dec 2023 Red Sea
diversion, which only re-rated tanker equities weeks after confirmed rerouting data.
The QUANT's EV calibration was decisive: P(durable continuation to 2026-08-15) = 0.22
against a break-even of 25.9%, and the hard stop required to bound loss over a
three-week hold (per the lesson that simulate-plans has no path-dependent monitoring)
consumes essentially the entire edge. The BULL conceded the EV math and narrowed to a
falsifiable 5-7 session confirmation test; the BEAR held no-trade throughout and
rejected any capped probe as a certain transaction cost on a coin-flip-or-worse
thesis. Verdict: NO-TRADE (not scheduled, not simulated). Reopen as a new dossier only
if STNG posts 3 consecutive closes above 79.99, a TC2/TC5 rate print rises >=15% w/w,
Brent shows sustained backwardation, or war-risk insurance/Kpler-AIS data confirms
Saudi port avoidance — otherwise close as a dead headline after 5-7 sessions of no
confirmation. Full debate with citations in `transcript.md`.
