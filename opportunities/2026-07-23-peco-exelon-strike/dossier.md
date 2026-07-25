---
id: 2026-07-23-peco-exelon-strike
title: PECO workers' first-ever strike pressures Exelon utility earnings
status: researched
created: '2026-07-23T19:57:39Z'
event:
  type: economic
  summary: 1,600 unionized PECO (Exelon) workers began the utility's first strike
    in its 145-year history on July 4 over wages and benefits; resolution timing and
    any service disruption are a forward catalyst for EXC.
  impact_window: '2026-08-15'
tickers:
- EXC
sources:
- title: 'WHYY: PECO workers strike starts amid Fourth of July heat wave'
  url: https://whyy.org/articles/peco-workers-strike-july-fourth-philadelphia/
  accessed_at: '2026-07-23T19:57:39Z'
duplicate_of: 2026-07-08-peco-ibew-strike
hypothesis:
  statement: "No tradeable edge exists. The event this dossier framed as a forward catalyst (\"resolution timing ... a forward catalyst\", impact_window 2026-08-15) had already resolved before this dossier was created: the same 1,600 IBEW Local 614 PECO workers who struck on 2026-07-04 reached a tentative agreement 2026-07-06/07 and returned 2026-07-08/09 on ordinary 5-year terms (4%/4.5% raises for linemen and gas techs, 3%/yr for call-center staff, restored pensions/retiree medical), with PECO stating no immediate rate impact. EXC's first post-settlement session (2026-07-09) traded USD 46.54-47.43, mid-range of its 52-week band, with no volume, analyst, or rating signature. The market reaction is a measured zero, not a modeled unknown. Decomposing the bull case, P(settlement in window) is ~1.0 (already occurred) but E[move | settlement] is ~0 (observed), so the product is ~0; after friction (~0.12% round-trip) EV_long/EV_short are both negative (-0.11% to -0.13%), and even granting a 0% adverse branch EV_long is still -0.01%. Independently, scale caps any upside: PECO is 1 of 6 EXC utility subsidiaries, 1,600 workers is ~8% of headcount against ~USD 24B consolidated revenue, and regulated cost-recovery mutes O&M shocks -- incremental strike cost is ~0.1-0.3% of EV versus EXC daily sigma of ~1.1-1.25%, i.e. sub-noise. EXC also reports Q2 earnings ~2026-07-30/31, inside the stated impact window, which would dominate and contaminate any residual strike signal even if one existed. No live quote was obtainable across all three personas (twelvedata HTTP 429), so entry/stop could not be priced even if a thesis survived."
  direction: neutral
  confidence: 94
plan:
  ticker: EXC
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-25T21:30:03Z'
---

## Scouted 2026-07-23T19:57:39Z

## Researched 2026-07-25T21:30:03Z

**Verdict: NO-TRADE (neutral, confidence 94).** Three-round bull/bear/quant panel.
This dossier turned out to be a stale duplicate of `2026-07-08-peco-ibew-strike`
(same ticker, same 1,600 IBEW Local 614 workers, same 2026-07-04 strike start,
15 days apart -- just outside the scout dedup window's 14-day ticker-overlap
check). That prior dossier (status: researched, confidence 78, NO-TRADE) already
documented the strike settling 2026-07-06/07 on ordinary terms with EXC trading
flat (USD 46.54-47.43, mid-52-week-band) on its first post-settlement session,
2026-07-09 -- 14 days before this dossier was even scouted. Quant discovered this
in Round 2 and recomputed the bull thesis with the settlement treated as a known
fact rather than a forward catalyst: P(settlement)~1.0 but E[move|settlement]~0
(measured), so the product is ~0, and friction alone (~0.12% round-trip) makes
even a friction-only EV_long negative (-0.01%). Bear's independent scale-mismatch
argument (PECO is 1 of 6 EXC subsidiaries, 1,600 of ~19,000 employees, regulated
cost recovery) and Quant's base-rate/EV model converged on the same PASS from two
different methodologies. A further confound: EXC's Q2 earnings print (~2026-07-30
to 07-31) sits inside the 2026-08-15 impact window and would dominate any residual
signal even if one existed. No live EXC quote was obtainable in any round
(twelvedata HTTP 429 throughout). Full debate in `transcript.md`.

**Process note:** this opportunity should be treated as a duplicate of
`2026-07-08-peco-ibew-strike` for post-mortem/base-rate purposes (do not
double-count). Root cause: the scout dedup window (`lib/dedup.py`,
`window_days=14`) missed this pair because the two dossiers were created 15 days
apart -- one day past the window -- despite describing the identical event. Worth
widening the dedup window or adding a ticker+event-type match independent of
`last_seen` recency for `event.type: economic` labor-action stories, which can
stay "current news" for weeks after the underlying event resolves.

**Dissent (carried forward for post-mortem):** whether "no measurable move on the
settlement session" proves "no edge existed" or only that the daily-bar
instrument couldn't resolve a sub-noise but real reaction -- Bear and Quant reach
the same PASS for different reasons (signal absent vs. signal present-but-smaller-
than-friction), which matters if a cheaper execution path or leveraged instrument
is ever considered for this class of event. Also unresolved: nobody in the panel
checked whether a PA PUC docket exists that would flip the verdict (Quant's stated
falsifiable condition); the PASS is correct on the strike thesis alone but was
never tested against that specific condition.
