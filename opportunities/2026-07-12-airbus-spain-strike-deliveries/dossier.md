---
id: 2026-07-12-airbus-spain-strike-deliveries
title: Airbus Spain strike threatens July aircraft deliveries
status: researched
created: '2026-07-12T18:06:04Z'
event:
  type: geopolitical
  summary: A strike by ~3,000 Airbus Getafe-plant workers in Spain, running through
    end of July 2026, is delaying aircraft inspections/engineering checks needed to
    complete deliveries.
  impact_window: '2026-07-31'
tickers:
- EADSY
sources:
- title: Airbus Employees in Spain Go on Strike Over Working Conditions
  url: https://www.bloomberg.com/news/articles/2026-07-09/airbus-employees-in-spain-go-on-strike-over-working-conditions
  accessed_at: '2026-07-12T18:06:04Z'
hypothesis:
  statement: The Getafe strike is a delivery-timing bottleneck at one site of a
    diversified, deep-backlog OEM, not a production halt — most likely absorbed
    as revenue deferral or resolved before month-end. Any residual edge tied to
    the ~2026-07-31 H1 print is sign-ambiguous, at best a variance/convexity play
    with no liquid EADSY options to express it, and EV-negative once ADR execution
    costs are applied to the proposed linear short.
  direction: no_trade
  confidence: 82
plan:
  ticker: EADSY
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
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
  dissent: Whether the ~2026-07-31 H1 print is a real, exploitable dated catalyst
    or merely noise. Bull/Bear grant the print concentrates a genuine information
    event in time; Quant counters that time-concentration raises variance, not
    mean, so it's irrelevant to a linear EV-negative position and only matters for
    a convex options structure that doesn't exist for EADSY. Unresolved because it
    was dismissed on tradeability/instrument grounds (no liquid EADSY options,
    broken price feed) rather than settled on merit — nobody established whether a
    properly-structured AIR.PA event-vol trade around 2026-07-31 would carry
    positive EV. Post-mortem should check the actual print outcome against this.
  last_updated: '2026-07-12T18:30:05Z'
---

## Scouted 2026-07-12T18:06:04Z

## Researched 2026-07-12T18:30:05Z — NO-TRADE

Three-round panel debate (bull/bear sonnet, quant/synthesizer opus). All three
personas converged independently on no-trade by Round 2:

- **Quant (decisive):** gross EV on a hypothetical EADSY short ≈ +0.10%, but
  realistic Level-1 OTC ADR round-trip friction (spread + FX overlay + hard-to-borrow)
  runs ~0.8–1.5%, giving net EV ≈ -1.0% (range -0.7% to -1.4%). Escalation
  probability would need to roughly triple (to ~55%) to clear costs — unsupported
  by base rates for a single-plant delivery-timing bottleneck at a ~150k-employee
  OEM with a multi-year backlog. Confidence in "stand aside": ~80%.
- **Bear:** News was 3 days stale at debate time (Bloomberg 2026-07-09 vs.
  debate on 2026-07-12); Getafe's role as a hard, non-reroutable delivery gate is
  asserted, not proven (Airbus has redundant final-assembly capacity at
  Toulouse/Hamburg); deep backlog converts a one-month slip into revenue timing,
  not lost value; strikes often settle before their stated end date. Confidence
  in "pass": ~80-85%.
- **Bull:** Opened short EADSY at moderate confidence on a dated-catalyst thesis
  (strike bottleneck resolves near Airbus's 2026-07-31 H1 print), but conceded in
  rebuttal that the quant's EV-after-costs math "stands regardless of who's right
  about mechanism" and downgraded to low-confidence speculative watch, no size.

**Cross-cutting issue:** the `toa price EADSY` feed returned an incoherent series
($175.83 on 7/8 → $494.84 on 7/9 → $79.87 on 7/12 — a +181% then -84% swing with
no news to justify it). All three personas flagged this as an unusable stub/testing
artifact and did not use it for entry/exit/sizing; the hypothesis above rests on
the fundamental mechanism and cost structure, not on these price points.

**What would need to change to revisit:** (1) price feed repaired; (2) concrete
evidence Getafe performs a non-reroutable inspection gate for a material share of
H1 deliveries; (3) signs of escalation past end-July rather than early settlement;
(4) a liquid convex vehicle (e.g., event-vol options on the primary AIR.PA
listing) to express the dated-catalyst idea, since the residual edge — if any —
lives in variance around the print, not direction, and a linear EADSY short
cannot capture it.

Full transcript: see `transcript.md`.
