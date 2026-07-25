---
id: 2026-07-22-zillow-redfin-ftc-antitrust
title: FTC antitrust case against Zillow and Redfin cleared to proceed
status: researched
created: '2026-07-22T13:34:47Z'
event:
  type: regulatory
  summary: Federal judge denied motion to dismiss FTC antitrust suit over real estate
    listing practices, allowing case to advance
  impact_window: '2026-09-15'
tickers:
- Z
- RDFN
sources:
- title: FTC's Antitrust Case Against Zillow and Redfin Can Proceed, Judge Rules
  url: https://www.rismedia.com/2026/05/07/ftc-zillow-redfin-may-ruling-case-proceeds/
  accessed_at: '2026-07-22T13:34:47Z'
hypothesis:
  statement: "Dossier premise is broken on two axes - RDFN was delisted 2025-07-01 (Rocket Companies acquisition, untradeable, no RKT substitute) and the named May-2026 MTD-denial catalyst produced zero abnormal return (Z closed +0.6 pct on ruling day), so the subsequent -28.8 pct drift is unattributable and confounded with Q1 earnings and housing fundamentals. The only real dated docket event is a two-week BENCH (not jury) trial starting 2026-08-24, giving only ~10-15 pct probability of a merits resolution before the 2026-09-15 impact_window; branch-tree EV is +0.39 pct with sign not distinguishable from zero (CI -0.24 pct to +1.07 pct, IR ~0.024) against ~27 pct horizon sigma, and Z Q2 earnings land 2026-08-05 inside the hold window as an uncompensated confound."
  direction: none
  confidence: 82
plan:
  ticker: Z
  action: no-trade
  entry:
    time: '2026-08-24T13:30:00Z'
    target_price: null
  exit:
    time: '2026-09-15T20:00:00Z'
    target_price: null
  expected_profit_pct: 0
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: "Bear vs quant on whether a long-volatility structure boxed around 2026-08-24 is tradeable - never settled, since no option chain or implied-vol data was ever pulled; both sides argued from priors. Runner-up: bull and bear both built a round of reasoning on a jury-trial framing that quant's bench-trial correction proved wrong."
  last_updated: '2026-07-25T00:39:57Z'
notes: "Recommended dossier corrections from debate: tickers should drop RDFN (delisted, permanent 404, no RKT substitute) to become [Z] only; impact_window could move to 2026-08-24 (trial start, the only verifiable docket milestone), with the expected written opinion landing outside any reasonable trading window (~Nov-Dec 2026)."
---

## Scouted 2026-07-22T13:34:47Z

## Researched 2026-07-25T00:39:57Z

Three-round panel debate (bull/bear/quant, synthesizer) converged on NO-TRADE, confidence 82.
Decisive findings: RDFN delisted and untradeable (Rocket Companies acquisition, 2025-07-01);
the dossier's named catalyst (May 2026 MTD denial) produced a zero abnormal return on the
ruling day; the only real forward catalyst is a BENCH trial starting 2026-08-24 (not jury,
as both bull and bear initially assumed), giving low odds of a merits resolution inside the
2026-09-15 impact_window; Z Q2 earnings on 2026-08-05 sit inside the window as an
uncompensated confound. Full transcript: `transcript.md`.
