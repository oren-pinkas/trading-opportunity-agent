---
id: 2026-06-26-jpmorgan-q2-fy26
title: JPMorgan Chase Q2 FY2026 earnings (report July 14, kicks off bank season)
status: researched
created: '2026-06-26T11:00:05Z'
event:
  type: earnings
  summary: JPMorgan releases Q2 results ~6:45-7:00am ET July 14 (before the open), the
    unofficial start of large-bank earnings season; read-through to financials broadly.
  impact_window: '2026-07-14'
tickers:
- JPM
sources:
- title: JPMorganChase announces Q2 2026 earnings conference call
  url: https://www.jpmorganchase.com/ir/news/2025/jpmc-announces-conference-calls-to-review-first-quarter-second-quarter-third-quarter-and-fourth-quarter-2026-earnings
  accessed_at: '2026-06-26T11:00:05Z'
- title: JPMorgan Q2 2026 Earnings — What to Expect (Barchart)
  url: https://www.barchart.com/story/news/2644246/jpmorgan-chases-q2-2026-earnings-what-to-expect
  accessed_at: '2026-06-26T12:05:00Z'
- title: JPM Q1 2026 earnings — beat then faded on NII guide (public.com / CNBC)
  url: https://public.com/stocks/jpm/earnings
  accessed_at: '2026-06-26T12:05:00Z'
- title: NYSE 2026 Trading Calendar (July 13 Mon, July 14 Tue both open)
  url: https://www.nyse.com/publicdocs/nyse/ICE_NYSE_2026_Yearly_Trading_Calendar.pdf
  accessed_at: '2026-06-26T12:05:00Z'
hypothesis:
  statement: The gap-hold structure cannot harvest any edge on JPM Q2 earnings because
    the only repeatable move is an intraday fade that lands AFTER the 9:45am structural
    exit. The historical OPEN gaps are ~zero (Q1 2026 +9.2% EPS beat opened −0.31%;
    Q4 2025 +7.6% beat opened +0.25%), with the −2.5% damage materializing later on
    the 8:30am Dimon call. The classic fade-on-NII-guidance mechanism is mechanically
    spent (NII cut twice, now Street-modeled) and the $50B buyback is only a ~0.06%/day
    drip that cannot move an earnings open gap. Net EV is negative (~−0.17 to −0.22%)
    after costs.
  direction: none
  confidence: 22
plan:
  ticker: JPM
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
  dissent: "The bull argues two genuinely new, un-priced factors — the fade-on-NII-cut
    mechanism is mechanically spent (NII already cut to ~$103B twice and held flat in
    Q1, so the Street now models it) and the live $50B buyback plus 10% dividend hike
    is a fresh positive catalyst neither opponent weighed — which could break the
    historical pattern to the upside. The quant rebuts that the OPEN-gap record (what
    a 9:45am exit captures) was ~zero (−0.31% / +0.25%) regardless of the EPS surprise,
    and a $50B buyback is only a ~0.06%/day drip. Unresolved: whether 'this time' the
    spent-catalyst + buyback combo produces a positive open gap large enough to clear
    costs. Quant's open-gap calibration prevails on weight."
  last_updated: '2026-06-26T12:10:39Z'
---

## Scouted 2026-06-26T11:00:05Z

## Researched 2026-06-26T12:10:39Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). JPM releases
~6:45-7:00am ET July 14 (Tuesday; July 13 Monday — both normal sessions, after one
panelist's "Sunday" calendar error was corrected). The structurally valid trade is a
gap-hold: enter 7/13 close (~19:50Z), exit ~9:45am ET 7/14 (13:45Z). The QUANT's
open-gap analysis was decisive: JPM's last two prints beat EPS (Q1 +9.2%, Q4 +7.6%)
yet the OPEN gaps were −0.31% and +0.25% (~zero); the recurring −2.5% "fade" happens
intraday on the 8:30am call, AFTER a gap-hold exits. So the structure cannot capture
the bear's edge and the bull's "beat pop" doesn't exist at the open. The BEAR conceded
from short to NO-TRADE on exactly this point; the BULL was reduced to a half-size
~+1.2% trade. Net EV negative after costs. Verdict: NO-TRADE (not scheduled, not
simulated). Full debate with citations in `transcript.md`.
