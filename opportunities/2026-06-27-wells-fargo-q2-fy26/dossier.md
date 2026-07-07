---
id: 2026-06-27-wells-fargo-q2-fy26
title: Wells Fargo Q2 FY2026 earnings (report July 14 BMO)
status: researched
created: '2026-06-27T11:00:05Z'
event:
  type: earnings
  summary: Wells Fargo reports Q2 results pre-open July 14, leading off Q2 bank earnings
    season; consumer-credit and NII read-through.
  impact_window: '2026-07-14'
tickers:
- WFC
sources:
- title: Wells Fargo Updates 2026 Earnings Release Date Information
  url: https://newsroom.wf.com/news-releases/news-details/2026/Wells-Fargo-Updates-2026-Earnings-Release-Date-Information/default.aspx
  accessed_at: '2026-06-27T11:00:05Z'
- title: Wells Fargo Q1 2026 — EPS beat, revenue miss, ~4.92% pre-market drop (Investing.com)
  url: https://ca.investing.com/news/company-news/wells-fargo-q1-2026-slides-earnings-beat-offset-by-revenue-miss-93CH-4564385
  accessed_at: '2026-06-27T12:18:00Z'
hypothesis:
  statement: >-
    Unlike the sibling JPM case, WFC's recent negative earnings reactions ARE
    open-gap-capturable: Q1 2026 (Apr 14) gapped down ~4.92% PRE-MARKET to ~$83.30 on
    the revenue miss (then partially recovered intraday), and the Q4 2025 -3.4%
    landed in early trading — both at/near the open, exactly what a gap-hold
    harvests. This validates the structure the JPM debate killed. The quant
    established a genuine but THIN positive-EV short (P(down) ~0.62; +0.57% net after
    slippage) that holds ONLY if the live straddle is <=2.5% AND the move is gap-form;
    with realized avg ~4%, a ~9.7% 30-day run-up, and CFO-scheduled NIM compression,
    the live implied move is more likely 3-4%+, where the quant's own rule says SKIP.
  direction: none
  confidence: 33
plan:
  ticker: WFC
  action: no-trade
  entry:
    time: '2026-07-13T19:50:00Z'
    target_price: null
  exit:
    time: '2026-07-14T13:45:00Z'
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
    The bull's "spent-driver asymmetry" vs the quant/bear "scheduled-downside"
    framing. The bull argues the 4-of-5-down pattern was always one line (NII) now
    reset three quarters running, so a contrarian long has asymmetry; the quant
    counters the lone up-move was the non-repeating asset-cap catalyst and four
    straight beats still fell. Unresolved because we cannot know today whether the
    full-year ~$50B NII guide is REAFFIRMED (bull's long) or the CFO's pre-guided
    3-4bps NIM compression headlines fresh (bear/quant short) — that single guidance
    line, not the EPS print, determines direction and whether the move clears the
    2.5% implied-move gate.
  last_updated: '2026-06-27T12:20:00Z'
---

## Scouted 2026-06-27T11:00:05Z

## Researched 2026-06-27T12:20:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). WFC reports Q2
FY2026 BMO Tuesday 2026-07-14 (leads bank season with JPM/GS same morning). Gap-hold
structure: enter ~19:50Z 7/13, exit ~13:45Z 7/14. KEY FINDING vs the JPM NO-TRADE: WFC's
drops ARE open-gap-capturable — Q1 2026 gapped down ~4.92% pre-market on the revenue
miss; Q4 2025 -3.4% landed in early trading. So the structure is valid here, unlike JPM.
But this is the only name in the batch where a panelist found a conditional positive-EV
edge: the QUANT moved P(down) to ~0.62 and computed a small short at +0.57% net — yet
ONLY if the live straddle is <=2.5%; at >=4.0% the quant's own rule flips to SKIP, and
history (~4% realized) plus the ~9.7% run-up make a <=2.5% implied move unlikely. The
BEAR conceded the EV is "real but thin, does not survive costs at meaningful size"
(skip beats long decisively; small-short beats skip only marginally); the BULL conceded
"coin-flip-plus." Verdict: NO-TRADE — the thin edge does not survive its own
unconfirmable contingency today. Re-checkable when the live straddle and NII guide are
known. Full debate in `transcript.md`.
