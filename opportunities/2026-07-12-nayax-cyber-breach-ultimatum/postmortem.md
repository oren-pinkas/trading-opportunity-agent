# Post-mortem — 2026-07-12-nayax-cyber-breach-ultimatum

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Investigator (reconstruction)

Plan: long NYAX, entry 2026-07-13T13:30:00Z (next valid NASDAQ open) target $292.08,
exit 2026-07-17T20:00:00Z (Friday close, clearing the weekend gap ahead of the
2026-07-21 extortion deadline) target $300.84. Expected profit +3.0%.

Simulation result: `fills: []`, `realized_profit_pct: 0.0`, `outcome: neutral`,
`matched_hypothesis: no`, note: **"market data unavailable: 'no 1min bar for
2026-07-13 13:30:00'"**. No trade was actually filled — the real-provider
(twelvedata) lookup for the planned entry timestamp simply returned no data.

Notably, the transcript's own "Data-integrity note for any future post-mortem"
(written at research time) anticipated exactly this class of failure and warned
explicitly: *"If `simulate-plans` later books a large loss (or an outsized gain) on
this dossier, that outcome reflects hash-driven stub noise... P&L on this opportunity
is non-informative and must not be used to grade the debate's reasoning."* In the
event, the simulator behaved correctly — it did NOT fall back to the fake stub price
and instead reported a clean data-unavailable neutral, which is the right behavior.

## Critic (root cause)

This is not a trading loss or a fluke win — it is a data-coverage gap. Was it
knowable at research time? Partially: twelvedata's real-time/near-real-time coverage
gaps for the specific instrument and timestamp were not checked before the plan was
finalized — the panel verified NYAX's historical reaction (the -8.7% Nasdaq print) but
never test-queried `toa price NYAX 2026-07-13T13:30:00Z --provider twelvedata` to
confirm a bar would exist at the planned entry moment.

**Root cause: data** — the simulator had no priceable bar at the planned entry
timestamp, so the plan never actually executed; the qualitative thesis (extortion
claims quantitatively implausible vs. Nayax's real scale) remains untested and should
not be scored as won or lost.

## Lessons

1. Before finalizing a plan's entry/exit timestamps, test-query the real price
   provider (`toa price <ticker> <timestamp> --provider twelvedata`) for those exact
   timestamps during research, not just for a generic reference spot a few days
   prior — a plan whose entry/exit can't be priced by the real provider will resolve
   as an uninformative neutral, silently wasting the debate's qualitative work.
2. When a dossier's own transcript pre-flags a data-integrity risk (as this one did),
   surface that flag directly in `postmortem-targets`/reporting rather than requiring
   a human to re-discover it by reading the transcript — the informational content is
   "not tested," not "tested and neutral."
