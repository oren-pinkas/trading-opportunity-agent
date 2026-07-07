# Post-mortem — 2026-07-07-lime-ipo

Analyzed 2026-07-06T23:30:00Z. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Outcome:** neutral, 0.0% (fills: [], matched_hypothesis: no). **Root cause:** data.

## Reconstruction
LONG LIME planned at the Jul 1 listing-day open (13:35:00Z, target $28.00), exit
mid-morning (15:30:00Z, target $30.24) for an ~8% pop, at a deliberately low confidence
of 52. The trade never executed: on the 2026-07-06 run, twelvedata returned no 1-minute
bar for LIME at the entry minute (`market data unavailable: 'no 1min bar for 2026-07-01
13:35:00'`), so both legs were unfillable — `fills: []`, `realized_profit_pct: 0.0`,
`outcome: neutral`.

## Root cause: data
Pure data-availability failure, foreseeable in two ways the transcript itself hinted at.
First, the listing time was a derived guess: the dossier described the event only as a
"late June/early July 2026" window and the synthesis flagged that "the date could slip,"
yet the plan pinned entry to one exact UTC minute. Second, price providers routinely lack
clean minute bars for a ticker in its very first trading minutes — even a correctly
guessed listing time would likely have hit sparse/absent day-one data. The plan absorbed
all of that binary risk into a single hard-coded timestamp with no fallback and no
pre-trade data check. ("wrong-assumption" is a close secondary — the listing time was
guessed from an imprecise window — but "data" is the more useful label because even a
correct listing time would likely have hit missing first-minute bars.) The debate's
dissent, aimed at a market-structure concern (thin residual gain post-open), never got
tested; the failure was mechanical.

## Lessons
1. For IPO plans, don't hard-code entry to the raw listing-day open minute — day-one
   minute-bar coverage for a fresh ticker is unreliable. Delay entry to a later liquid
   window (30-60 min after the first print) or add a pre-trade data-availability probe
   that confirms a fillable bar exists before scheduling both legs.
2. Never convert an imprecise listing window ("late June/early July") into a single exact
   timestamp. Gate IPO opportunities on a confirmed exchange listing date/time verified
   present in the price provider; treat unconfirmed listings as non-schedulable.
