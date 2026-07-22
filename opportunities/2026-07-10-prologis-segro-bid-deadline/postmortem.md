# Post-mortem — 2026-07-10-prologis-segro-bid-deadline

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Investigator (reconstruction)

Plan: small tactical short (~0.25x), entry band $140.50-141.00 targeting $140.75 at
2026-07-13T14:00:00Z, hard cover at 2026-07-22T19:55:00Z (post-PUSU) targeting $140.15.
Expected profit ~+0.36% net.

Actual fills (twelvedata):
- Entry 2026-07-13T14:00Z: **$142.365** (vs. planned $140.75 — already +1.15% above the
  top of the planned entry band before the position was even opened).
- Exit 2026-07-22T19:55Z: **$144.23** (vs. planned $140.15).
- Realized: **-1.31%, loss**, matched_hypothesis: no.

PLD did not fade toward the acquirer-dilution discount the panel modeled; it drifted
steadily *up* through the entire PUSU window, including before entry was even filled.
The plan's own "hard stop above $143" (see transcript.md dissent, invalidating the
walk-away/relief path) was breached intra-window (exit printed $144.23), but
`simulate-plans`/`lib/pnl.py` has no path-dependent stop logic — it only diffs the
fixed entry and exit prices from the plan. The stop was never mechanically enforced.

## Critic (root cause)

The panel explicitly flagged this as a thin, low-conviction edge: signal-to-noise
~0.12, gross EV ~+0.36% net vs. ~4% dispersion — "a coin flip you pay a toll to enter"
in the quant's own words. The synthesizer's dissent section named the exact failure
mode in advance: *"if PLD drifted flat-to-up into a walk-away, both the short's thin
edge and the bull's premium were the wrong bet."* That is exactly what happened.

Was it knowable at research time? Partially. The direction call was a legitimate,
rigorously-argued 2-against-1 lean, not a process failure — this is the acknowledged
downside of trading a S/N≈0.12 setup. But two things *were* knowable and not acted on:
(1) the entry itself printed 1.15% outside the planned band, which should have been
a no-fill/reassess trigger rather than an automatic fill; (2) the plan's own $143
hard stop was breached mid-window with no mechanism to actually exit early — the
"hard stop" existed only as prose, not as an enforced simulation rule.

**Root cause: wrong-assumption** — the core acquirer-dilution-discount / walk-away
framing was simply wrong this cycle (PLD re-rated up, not down), compounded by a
structural gap where the plan's own risk controls (entry band, hard stop) are not
enforced by the simulator.

## Lessons

1. A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge —
   treat these as effectively no-trade in practice, and if taken, do not expect the
   stated entry band/hard-stop language to be enforced by `simulate-plans`: it only
   diffs the plan's fixed entry/exit prices against realized fills, with zero
   path-dependent stop-loss or invalidation-trigger logic. A plan that depends on an
   intra-window stop for its risk profile is currently mis-modeled by the simulator.
2. When the actual fill price on entry is already outside the planned entry band
   (here +1.15%), treat that as an early falsification signal of the thesis — the
   market has moved past the entry assumption before the position even opened.
