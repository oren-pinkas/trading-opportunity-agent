---
id: 2026-07-23-nasdaq-inc-q2-fy26
title: Nasdaq Inc Q2 2026 Earnings
status: researched
created: '2026-07-23T01:19:37Z'
event:
  type: earnings
  summary: Nasdaq Inc reports Q2 2026 results with consensus EPS of USD 0.98 on USD
    1.46B revenue
  impact_window: '2026-07-23'
tickers:
- NDAQ
sources:
- title: Nasdaq Q2 2026 Earnings Preview - Alphastreet
  url: https://news.alphastreet.com/nasdaq-q2-2026-earnings-preview-july-23-street-expects-0-98-eps/
  accessed_at: '2026-07-23T01:19:37Z'
hypothesis:
  statement: "No tradeable edge exists in NDAQ around its Q2 FY26 print. The catalyst\
    \ is T+2 stale by the time research ran (current time 2026-07-25T18:10:22Z vs\
    \ impact_window 2026-07-23), and every attempt to fetch a citable NDAQ price\
    \ via toa price --provider twelvedata (roughly 10 calls across 4 timestamps\
    \ and two debate rounds) returned HTTP 429. Even granting a generous p(continuation)\
    \ of 0.52 on ~2.0% 3-day sigma, net EV after costs is approximately -0.06%,\
    \ against a breakeven requirement of p > 0.545 that nothing in the record supports."
  direction: none
  confidence: 88
plan:
  ticker: NDAQ
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  note: "NO TRADE. Logged as unresolved due to data unavailability (persistent twelvedata\
    \ 429s foreclosed any anchorable entry/exit) plus an independent negative-EV\
    \ finding that would hold even with a working feed."
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-25T18:10:22Z'
---

## Scouted 2026-07-23T01:19:37Z

## Researched 2026-07-25T18:10:22Z

Three-round-panel debate (bull/bear/quant -> synthesizer) converged on **NO TRADE**.
See `transcript.md` for the full debate. Summary: the Q2 print is two trading
sessions stale by the time this research ran, and every `toa price NDAQ --provider
twelvedata` call (pre-print close, print-day close, day-after close, current;
~10 attempts across both debate rounds) returned HTTP 429 — no citable price could
be obtained for this ticker in this pass. Independently, the quant's post-earnings-
announcement-drift (PEAD) base-rate math for a large-cap, heavily-covered name at
T+2 produced a net EV of approximately -0.06% after costs against a required
breakeven hit rate of p > 0.545, which nothing in the debate supports. The bull
opened long at 40% confidence and revised down to 15% after conceding the PEAD
base-rate and thesis-creep objections; bear and quant both held NO TRADE at 90%.
Direction logged as `none` rather than `short` — the panel was explicit that taking
the other side of a weak long is not itself a thesis.
