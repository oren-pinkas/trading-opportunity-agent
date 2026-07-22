---
id: 2026-07-16-fomc-july-decision
title: FOMC July rate decision
status: researched
created: '2026-07-16T03:59:59Z'
event:
  type: macro
  summary: Fed announces its rate decision on 2026-07-29 with markets expecting a
    hold amid persistent inflation
  impact_window: '2026-07-29'
tickers:
- SPY
- TLT
sources:
- title: FedRateCalc FOMC Meeting Schedule
  url: https://fedratecalc.com/fomc-meeting-schedule/
  accessed_at: '2026-07-16T03:59:59Z'
hypothesis:
  statement: A July HOLD (about 88% base rate) is fully telegraphed and already
    in the tape - SPY's chop to 748.38 and TLT's steady bleed to 83.69 show duration
    and equities have already repriced the "higher-for-longer" view, leaving no
    positive expected edge net of costs and a fat negative hike-tail.
  direction: none
  confidence: 78
plan:
  ticker: SPY
  action: none
  entry: null
  exit: null
  expected_profit_pct: 0
  reasoning: Quant's own EV math is the deciding evidence - long SPY nets only about
    plus 0.17 percent on a plus 0.30 percent drift assumption and falls to about
    plus 0.04 percent (below the cost and noise floor) on a plus 0.15 percent assumption;
    the entire edge is one soft assumption away from zero, while carrying a 7 percent
    hike-tail of minus 2.0 percent. Bear's tape-reading (net 7/16-7/21 drift is
    actually minus 0.77 percent) and quant's EV math converged independently on
    no-trade, and reaction-trading was shown to be negative-EV, not a better fallback.
  reassess_trigger: CPI or PCE surprise before 2026-07-29 that breaks SPY's range,
    TLT stabilizing or bouncing, a dot-plot leak or Fed-speaker signal, or options-implied
    vol showing the market is not priced for a non-event.
research:
  last_updated: '2026-07-22T10:05:00Z'
  dissent: The strongest unresolved disagreement is the hold-day SPY drift magnitude.
    Bull claims plus 0.30 percent is defensible from recent hold-decision comps
    (unverified in this debate); quant argues the flat/negative realized drift over
    7/16-7/21 argues for revising down to plus 0.15 percent, which pushes net EV
    below the noise floor. If plus 0.30 percent verifies against past telegraphed-hold
    FOMC days, a tiny long-SPY starter becomes marginally positive-EV and the no-trade
    verdict weakens.
  transcript: transcript.md
---

## Scouted 2026-07-16T03:59:59Z

## Researched 2026-07-22T10:05:00Z

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) converged
on NO TRADE. See `transcript.md` for the full debate. Quant's EV for a long-SPY
"hold = relief rally" trade is only about +0.17% net of costs on an optimistic
drift assumption, and collapses to about +0.04% (below the noise floor) under a
more conservative but still-defensible drift assumption - while carrying a 7%
probability of a hawkish-hold/hike surprise worth about -2.0%. Bear independently
reached the same no-trade conclusion via tape-reading (net SPY drift 2026-07-16 to
2026-07-21 is actually -0.77%, so the apparent "V-recovery" is round-trip noise,
not a trend). Bull retreated from full conviction to a 0.5-0.75%-of-book starter
size, an implicit concession the edge is thin. No trade recorded; reassess if a
CPI/PCE surprise, dot-plot leak, or options-implied vol shift changes the picture
before 2026-07-29.
