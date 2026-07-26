---
id: 2026-07-24-ag-equipment-tariff-cut
title: US cuts farm/construction equipment tariffs to 15pct, easing CNH and AGCO cost
  pressure
status: researched
created: '2026-07-24T01:19:18Z'
event:
  type: regulatory
  summary: Trump proclamation lowers ag/construction equipment tariffs from 25pct
    to 15pct, a tailwind for import-heavy CNH and AGCO into H2 2026 guidance
  impact_window: '2026-08-06'
tickers:
- CNH
- AGCO
sources:
- title: US cuts tariffs on farm and construction equipment to 15 percent
  url: https://www.farmprogress.com/farm-policy/u-s-cuts-tariffs-on-farm-and-construction-equipment-to-15-
  accessed_at: '2026-07-24T01:19:18Z'
- title: "AGCO announces second quarter 2026 earnings release and conference call - July 30"
  url: https://www.stocktitan.net/news/AGCO/agco-announces-second-quarter-2026-earnings-release-and-conference-li13ch1mtuwu.html
  accessed_at: '2026-07-26T08:09:27Z'
- title: "CNH to announce 2026 Q2 results on August 3"
  url: https://www.globenewswire.com/news-release/2026/07/20/3329906/0/en/cnh-to-announce-2026-q2-results-on-august-3.html
  accessed_at: '2026-07-26T08:09:27Z'
hypothesis:
  statement: "A 25pct to 15pct ag/construction equipment tariff cut is worth roughly
    4-6pct of EPS to AGCO and 2-4pct of EPS to CNH after realistic pass-through capture,
    but the residual unpriced drift by 2026-08-06 is only about 1.0-1.8pct and is fully
    confounded by AGCO's 2026-07-30 and CNH's 2026-08-03 Q2 earnings prints (about 6-9pct
    event-day vol each). The tariff thesis is not cleanly testable in this window."
  direction: none
  confidence: 78
plan:
  ticker: CNH, AGCO
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: null
  rationale: "Expected value is approximately zero (+0.09pct to -0.25pct per quant
    model) against event-day volatility an order of magnitude larger; the impact
    window does not isolate the tariff variable from AGCO's 2026-07-30 and CNH's
    2026-08-03 earnings prints. A post-print entry on 2026-08-04 was proposed but
    not endorsed -- by then the tariff benefit is already explicit in guidance and
    the residual edge is gone."
research:
  strategy: three-round-panel
  personas: bull, bear, quant
  dissent: "Whether the earnings prints kill the trade or make it was never fully
    resolved: bull argued a confirmed in-window earnings event gives the window
    real structure (bear agreed this would change their mind), but once quant found
    the dates, they were read as a confound rather than a catalyst -- that inversion
    was not revisited. Flag for post-mortem: check AGCO's 07-30 and CNH's 08-03
    reactions and whether tariff relief was cited in guidance."
  last_updated: '2026-07-26T08:09:27Z'
---

## Scouted 2026-07-24T01:19:18Z

## Researched 2026-07-26T08:09:27Z

Three-round-panel debate (bull/bear/quant, synthesizer opus) concluded no-trade. All
three personas converged on PASS: the 2026-08-06 impact window is confounded by
AGCO's Q2 earnings call (2026-07-30) and CNH's Q2 results (2026-08-03), both landing
inside the window with ~6-9pct event-day volatility that swamps the ~1.0-1.8pct
residual tariff-only signal (confound SNR ~0.09, below the 0.15 institutional floor).
Full transcript: `transcript.md`.
