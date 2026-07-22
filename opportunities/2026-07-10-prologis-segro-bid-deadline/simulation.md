## Simulated 2026-07-22T22:30:04Z

**Plan:** small tactical short of PLD (~0.25x size), entry band $140.50-141.00,
hard exit/cover at the 2026-07-22 19:55 UTC PUSU resolution deadline. Thesis: the
acquirer-dilution discount was only partially priced in, and the bear+quant scenario
tree gave a thin (~+0.36% net) edge to fading PLD into the UK Takeover Panel deadline.

**Fills (twelvedata):**
- Entry: 2026-07-13T14:00Z, actual $142.365 (planned $140.75) —
  [source](https://api.twelvedata.com/time_series?symbol=PLD&interval=1min&date=2026-07-13&timezone=UTC)
- Exit: 2026-07-22T19:55Z, actual $144.23 (planned $140.15) —
  [source](https://api.twelvedata.com/time_series?symbol=PLD&interval=1min&date=2026-07-22&timezone=UTC)

**Result:** loss, realized -1.31%. Hypothesis did not match reality (matched_hypothesis: no).

**Read:** PLD drifted up roughly 1.3% net short over the holding window rather than
the flat-to-slightly-positive walk-away path the quant modeled as the dominant
(55%-probability) scenario. The short's thin edge (~36bps expected) was swamped by
real-world dispersion in the opposite direction — a bigger move than the ~4% modeled
dispersion would suggest is unusual, but this was already flagged as a low
signal-to-noise (~0.12) trade. Per the dissent note: PLD did not gap hard on a firm
offer (which would have favored the bull's convex long-calls structure); it simply
drifted up through the PUSU window, which is bad for the linear short but doesn't
clearly validate the bull's convexity thesis either — no visible catalyst-driven
option payoff, just adverse grind against a thin-edge short.
