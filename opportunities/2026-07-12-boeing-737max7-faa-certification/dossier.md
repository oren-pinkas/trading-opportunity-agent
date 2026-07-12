---
id: 2026-07-12-boeing-737max7-faa-certification
title: Boeing 737 MAX 7 nears FAA certification
status: researched
created: '2026-07-12T11:57:54Z'
event:
  type: regulatory
  summary: FAA expected to certify the Boeing 737 MAX 7 by end of July/August 2026,
    clearing the way for Southwest to begin taking deliveries of ~24 parked jets.
  impact_window: '2026-07-31'
tickers:
- BA
- LUV
sources:
- title: Boeing 737 MAX 7 Nears FAA Certification by End of July 2026 - Aviation A2Z
  url: https://aviationa2z.com/index.php/2026/07/11/boeing-737-max-7-nears-faa-certification/
  accessed_at: '2026-07-12T11:57:54Z'
hypothesis:
  statement: FAA 737 MAX 7 certification is a long-telegraphed, single-sourced, de-risking
    milestone whose most probable resolution date (July/August, against a 4-year slippage
    pattern) falls at or beyond the stated 2026-07-31 impact_window. The 24-jet cash
    flow is immaterial to BA (~0.7% of market cap) and already largely priced; LUV
    carries larger unrelated overhangs (network overhaul, activist pressure). No panelist
    produced a verifiable positive expected value net of costs inside the tradeable
    window, and the MAX 10 / 777X read-through option value remains unsourced and
    speculative.
  direction: no_trade
  confidence: 78
plan:
  ticker:
  - BA
  - LUV
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  position_size: 0
  note: 'Panel converges on PASS. Rejected: Bull''s directional BA long and downgraded
    small-optionality call play (untimeable given wide/likely-out-of-window cert date
    distribution); Bear''s fade-the-LUV-run-up short (no verified non-stub price/volume
    evidence of a run-up). Reassess on primary-source (FAA/Boeing) confirmation of
    a cert date inside a defined tradeable window, plus verified live price data.'
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
  dissent: 'Unresolved: is the delay/negative-surprise move on LUV larger than Quant''s
    assumed ~-1.5%? Quant holds a symmetric neutral-pass EV (~0, no directional lean
    without data) and declines any LUV overlay absent evidence. Bear argues the modal
    outcome is ''delay past August'' (15-30% on-time odds vs a 4-year slippage base
    rate), making a negative LUV fleet-planning surprise the more likely non-zero
    move, and flags Quant''s -1.5% delay-move assumption as possibly uncalibrated
    against actual historical BA/LUV reactions to the 2023/2024 MAX 7 delay announcements.
    If a post-mortem finds historical delay headlines moved LUV materially more than
    -1.5%, a small defensive LUV hedge (Bear''s proposal, declined here for lack of
    evidence) would have been the correct call instead of flat no-trade.'
  last_updated: '2026-07-12T18:05:00Z'
---

## Scouted 2026-07-12T11:57:54Z

## Researched 2026-07-12T18:05:00Z — NO-TRADE

**Panel: bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus). Verdict: NO TRADE (confidence 78/100).**

Single-source catalyst (Aviation A2Z, 2026-07-11; no FAA/Boeing/wire corroboration in the dossier) reporting FAA MAX 7 certification expected by end of July/August 2026, unlocking ~24 parked jets for Southwest delivery.

**Why no trade:**
1. **Window mismatch** — the dossier's impact_window is 2026-07-31, but the source's own language hedges 'July/August', against a program history of four consecutive years of certification slippage (2022→2023→2024→2025→2026). The most probable resolution date sits at or beyond the window edge, meaning ~0.75 of probability mass inside the window is 'no resolution' — a directional long timed to this window is paying carry through a likely non-event, or exiting (per Bull's original 07-24–mid-August plan) before the actual catalyst prints.
2. **Immaterial magnitude, largely priced** — 24 jets ≈ $1.2B ≈ 0.7% of BA's ~$173B market cap; historical known-milestone BA reactions (MAX 9 ungrounding, return-to-service) were a modest 1-3% single-day and faded. The FAA's 38/month production-rate cap further limits how much of the '24 jets unlock cash flow' story can matter in any near-term window. A four-year-repriced overhang de-risks on removal; it does not re-rate.
3. **EV net of costs ≈ zero to negative** — Quant's three-state EV table (cert-in-window P=0.15 → +2.0%; delay P=0.10 → -1.5%; no-resolution P=0.75 → 0%) nets to EV_gross +0.15%, minus ~0.10% round-trip costs = EV_net ≈ +0.05%, statistically indistinguishable from zero, and turns negative under a more conservative +1% pop assumption.
4. **Sourcing floor not met** — single low-tier trade-press item, no institutional lessons on file for BA/LUV regulatory events, no primary-source (FAA/Boeing) confirmation.

**What survived rebuttal but wasn't actionable:** Bull's MAX 10 / 777X 'read-through' option-value argument (Bull correctly noted that pure 24-jet cash-flow immateriality 'proves too much' as an argument, since it would make almost no single BA catalyst ever tradeable) — but this mechanism is unsourced/speculative, and Bear noted it could plausibly cut negative given MAX 7/MAX 10 share the same engine anti-ice fix lineage.

**Reassess trigger:** primary-source (FAA docket, Boeing 8-K, or Southwest investor filing) confirmation of a cert date inside a defined tradeable window, plus verified (non-stub) live price/volume data for BA/LUV, plus options IV term structure to check whether the market is already pricing a bigger move than assumed.

Full transcript: see transcript.md.
