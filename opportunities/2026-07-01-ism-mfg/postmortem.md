# Post-mortem — 2026-07-01-ism-mfg

Analyzed 2026-07-06T23:30:00Z. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Outcome:** neutral, -0.0054% (matched_hypothesis: no). **Root cause:** data.

## Reconstruction
LONG XLI (confidence 58) betting a June ISM Manufacturing print at/above ~51 would
surprise a skeptical consensus and drive XLI ~1% intraday. Plan: entry 180.81 at 14:05Z,
exit 182.62 at 17:00Z, +1.0% target. Actual: entry filled 184.63, exit 184.62 — a
one-cent round-trip over three hours, flat, well inside noise. The ~1% post-print
repricing never occurred during the hold. The decisive divergence is not the intraday
tape but the entry anchor: XLI opened the window ~2.1% ($~4) above the plan's assumed
180.81, and above the $182.92 52-week high the transcript had cited as the ceiling.

## Root cause: data
The plan hard-coded `entry.target_price: 180.81`, which was verbatim the research-time
quote captured 2026-06-24 ("XLI ~$180.81 (52wk high $182.92)"). By the 2026-07-01 event
window that anchor was seven days stale and the level was gone. The plan never
re-validated the entry reference against the event-day tape, so a stale price — not any
market reaction — drove `matched_hypothesis=no`. This was knowable at simulation time:
any pre-entry price refresh would have shown the anchor was a week old. The flat print
reaction (a priced-in non-event, exactly the "within ~1.2% of 52wk high" risk the dissent
flagged) meant there was little to capture regardless, but the reason the trade never
resembled the plan is mechanical: it was benchmarked to a dead price. Bad process, not
bad luck.

## Lessons
1. Anchor entry to a live pre-event quote, not the research-day price. For a
   multi-day-old dossier, resolve `entry.target_price` from a fresh read at/near the
   entry timestamp; if the live price has drifted >~0.5-1% from the plan anchor,
   re-derive the exit target and EV or void the trade rather than filling blind.
2. When the thesis is "catalyst reprices X higher" and X has already rallied to its
   52-week high before the event, treat the move as largely priced-in — fade or shrink,
   don't chase the entry.
