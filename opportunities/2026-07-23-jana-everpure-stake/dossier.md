---
id: 2026-07-23-jana-everpure-stake
title: Jana Partners Builds Activist Stake in Everpure
status: researched
created: '2026-07-23T04:24:42Z'
event:
  type: economic
  summary: Jana Partners built a new position of over one million shares in Everpure
    (formerly Pure Storage) in Q1 2026, with imminent public disclosure expected to
    shift sentiment
  impact_window: '2026-08-15'
tickers:
- P
sources:
- title: Exclusive-Activist Jana Partners has new stake in Everpure, sources - Reuters
    via Yahoo Finance
  url: https://finance.yahoo.com/markets/stocks/articles/exclusive-activist-jana-partners-stake-193258851.html
  accessed_at: '2026-07-23T04:24:42Z'
hypothesis:
  statement: 'Stand-aside: ticker "P" has zero market-data coverage in this system
    (twelvedata HTTP 400/404 on P, P.US, PSTG, PSTG.US, EVERPURE, EVRP) so the trade
    cannot be anchored, filled, or marked. Independently of that, the catalyst itself
    is a two-day-old unconfirmed "sources say" leak of a stake built in Q1 2026 with
    no stated activist ask, so most of any announcement-day edge is already stale;
    modeled net EV is marginally negative even setting the data gap aside.'
  direction: neutral
  confidence: 30
plan:
  ticker: P
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-25T15:20:00Z'
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
  confidence: 30
  lessons_applied:
  - '2026-07-02-june-jobs: skip trades whose only positive-EV path cannot be filled
    by the harness — here there is no fill mechanism at all for ticker P'
  - '2026-07-01-ism-mfg: catalyst already priced in before the event should be faded
    or shrunk, not chased'
  dissent: Bull initially argued the Reuters leak is correctly-timed for the disclosure
    catalyst rather than stale, and withdrew the buy call only after conceding the
    tradability gap and negative-EV math were unrebuttable; bear framed the thesis
    itself (not just the data gap) as moot given no confirmed 13D/13G and no stated
    activist ask.
  transcript: transcript.md
  untradeable: true
  untradeable_reason: No twelvedata coverage for ticker P or any plausible variant
    (P.US, PSTG, PSTG.US, EVERPURE, EVRP) — HTTP 400/404 on all, matching the known
    structural NSE/Euronext coverage-gap pattern rather than a transient outage.
---

## Scouted 2026-07-23T04:24:42Z

## Researched 2026-07-25T15:20:00Z
Verdict: NO-TRADE (neutral, confidence 30). Three-round panel unanimously converged
on stand-aside via two independent, sufficient kills: (1) zero market-data coverage
for ticker P and every plausible variant — the trade cannot be entered, marked, or
exited in this system; (2) even setting the data gap aside, the "disclosure" is a
2-day-old unconfirmed press leak of a stake built a full two quarters earlier with
no stated activist ask, and modeled net EV comes out marginally negative after costs.
Bull initially proposed a buy but withdrew after conceding both points were
unrebuttable. Full debate with citations in `transcript.md`.
