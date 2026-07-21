---
id: 2026-07-15-kinder-morgan-q2-fy26
title: Kinder Morgan Q2 FY26 earnings
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: earnings
  summary: Kinder Morgan reports Q2 2026 results Wed Jul 15, a read on natural gas
    pipeline demand and capex plans.
  impact_window: '2026-07-15'
tickers:
- KMI
sources:
- title: 'Stock market next week: Outlook for July 13-17, 2026 - CNBC'
  url: https://www.cnbc.com/2026/07/10/stock-market-next-week-outlook-for-july-13-17-2026.html
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: >-
    KMI Q2 FY26 earnings offered no exploitable event-day edge. The good-news
    narrative (LNG/data-center gas demand backlog) was already discounted by a
    2.4% pre-print run-up (USD 31.85 to USD 32.60 over the prior two weeks); the
    fee-based/take-or-pay toll-taker model structurally caps EPS surprise
    magnitude; and the realized print-day path (open USD 32.50, close USD 32.20,
    a -0.92% fade) landed within historical noise, confirming the priced-in
    read rather than rewarding a momentum continuation or punishing a
    disappointment.
  direction: none
  confidence: 80
plan:
  ticker: KMI
  action: no-trade
  entry:
    time: '2026-07-15T13:31:00Z'
    target_price: null
  exit:
    time: '2026-07-15T19:59:00Z'
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
    The convergence is genuine but setup-dependent, not KMI-dependent: all
    three personas would revisit this only under a standing gate (implied move
    at least ~2x the historical realized 1.5-2.5% band, or a genuine unpriced
    catalyst, with gross EV required to exceed 2x round-trip cost). Open
    caveats for the post-mortem: (1) the bull's multi-quarter uptrend (+16.4%
    trailing year) is a valid position-trade signal even though it carries no
    event-day edge -- the debate should not be read as bearish on KMI broadly;
    (2) the bear's un-hedgeable bond-proxy rate-sensitivity overlay did not
    fire this cycle but remains a live risk on future prints; (3) the quant's
    null-EV conclusion assumes KMI realizes at or below implied vol -- a
    quarter with a genuine unpriced backlog/contract disclosure would
    invalidate the gate, so the trigger to watch is the dislocation, not the
    ticker.
  last_updated: '2026-07-21T14:12:54Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-21T14:12:54Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). KMI reported Q2
FY26 Wednesday 2026-07-15. All three personas independently converged on NO TRADE:
the BEAR flagged the pre-print run-up (USD 31.85 to USD 32.60) as already pricing the
LNG-export/data-center-gas-demand narrative, with a fee-based take-or-pay model
capping surprise magnitude and a bond-proxy rate overlay as an un-hedgeable risk. The
QUANT's EV math was decisive: base-rate move ~1.5-2.5%, P(up)/P(down) 0.52/0.48,
gross EV +0.08%, net EV -0.04% after ~0.12% round-trip costs -- with no positive-EV
options structure since KMI historically realizes at or below implied vol. The BULL's
own price research surfaced the realized print-day path (open USD 32.50, close USD
32.20, -0.92%), which it conceded was disconfirming evidence for its momentum thesis
rather than noise, and revised down to NO TRADE. Re-running the quant's EV on the
realized 0.92% move (vs the 2.0% assumed) worsened net EV to -0.08%, and the move hit
neither a hypothetical profit target nor a stop-loss -- the signature of a no-edge
setup. Verdict: NO-TRADE (not scheduled, not simulated; window already past). Standing
lesson: for fee-based midstream toll-takers with a pre-print narrative already run
into the tape, treat earnings as non-events unless implied move is at least ~2x
historical realized or a genuine unpriced catalyst exists. Full debate with citations
in `transcript.md`.
