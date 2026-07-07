# Post-mortem — 2026-07-02-tesla-deliveries

Analyzed 2026-07-06T23:30:00Z. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Outcome:** neutral, 0.0% (fills: [], matched_hypothesis: no). **Root cause:** data.

## Reconstruction
LONG TSLA planned at $380.00 on the 2026-07-02 open (13:30:00Z), exit $418.00 near the
close (20:00:00Z), +2.33% target — the synthesizer lifted P(beat) from the quant's 0.35
to 0.40 on "observed" EU registration data (+85-90% YoY), tipping EV across the +2% bar.
None of that was tested. The simulator (twelvedata, run 2026-07-06) recorded `fills: []`,
`realized_profit_pct: 0.0`, `outcome: neutral`, with the note `market data unavailable:
'no 1min bar for 2026-07-02 20:00:00'`. The exit timestamp landed on the 16:00 ET close
boundary, a minute the 1-minute feed does not publish, so the exit leg could not be
priced and the whole trade voided.

## Root cause: data
Pure data-availability/execution failure, not a market-thesis error. The 1-minute series
runs through 19:59Z (15:59 ET); 20:00:00Z falls in the closing-auction gap with no bar,
so the leg silently no-filled. The thesis was never exercised, so the bear's
sell-the-news dissent is irrelevant to why this returned 0.0% NEUTRAL. This is a fluke on
the outcome axis but a *defect* on the process axis: choosing 20:00:00Z as an exit is a
boundary off-by-one that is fully knowable at planning time. Every future intraday plan
carries the same latent bug until the exit is pulled inside the session or the simulator
snaps to the nearest valid bar.

## Lessons
1. Set intraday exits at least one minute inside the session boundary (19:59:00Z / 15:59
   ET, not 20:00:00Z). A 1-minute-bar provider has no bar stamped exactly at the close,
   so any leg timed to the close silently no-fills and voids the whole trade regardless
   of thesis quality.
2. Add a pre-simulation timestamp guard that validates both legs map to available
   US-equity bars (13:30Z-19:59Z) and falls back to the nearest valid bar rather than
   voiding an expensive, untested thesis to NEUTRAL.
