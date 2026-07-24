## Post-mortem 2026-07-24T23:40:00Z

**Strategy:** investigator-critic (investigator sonnet, critic opus, synthesizer opus).

### Reconstruction (Investigator)

Plan: short STLD, entry 2026-07-22T14:00:00Z @ target USD 233.67, exit
2026-07-24T19:45:00Z @ target USD 232.97 (expected +0.3%), a minimal confidence-18
contrarian fade recorded mainly to keep the Section 122/STLD sign question in the
learning loop (see `transcript.md` Round 3 synthesis and dissent).

Calendar check: 2026-07-22 is a Wednesday, no US market holiday nearby — a normal
trading day. 14:00:00Z is 10:00 EDT, squarely inside NYSE regular hours (13:30-20:00
UTC), well past the open. This is not a calendar-mapping error (a legal/corporate
date mapped onto a non-trading timestamp) — it's a genuinely liquid large-cap minute.

Data gap: `simulation.md` and the dossier frontmatter both record, verbatim, `market
data unavailable: 'no 1min bar for 2026-07-22 14:00:00'`, with no HTTP error code, no
retry log, and no adjacent-timestamp fallback attempted or cited. The same
transcript's Round 1/2 research successfully pulled twelvedata STLD bars at other
timestamps in the 2026-07-08 to 2026-07-15 window (14:30Z, 15:30Z, 19:00Z), so general
coverage exists — this reads as an isolated provider data hole or fetch-boundary issue
at that exact minute, not systemic illiquidity.

Realized result vs. plan: no position was ever opened. `realized_profit_pct: 0.0`,
`outcome: neutral`. There is no entry/exit price pair, so the STLD sign-inversion
question the panel debated (mildly bearish vs. bullish for STLD from the July 24
Section 122 expiry) was never actually tested by this trade.

### Diagnosis (Critic)

**root_cause: `data`**

None of the panel's substantive research disputes (Section 122/232 overlap, sign
inversion, extension tail risk) caused this outcome — the trade never touched the
market, so those remain exactly as unresolved as they were at research time. The
failure is entirely in the execution/data layer: twelvedata had no 1-minute bar for
the exact entry timestamp, and the simulator treated that single missing bar as a
terminal skip with no retry or fallback.

This was knowable and preventable at the plan/harness level, not the thesis level. A
one-bar gap in intraday data is a routine provider characteristic; the plan specified
a point-in-time fill with zero tolerance window and no secondary provider — a single
point of failure with no redundancy. Note the asymmetry: the expected edge was only
0.3%, smaller than plausible price drift across a few minutes of tolerance, yet the
plan demanded minute-exact precision it didn't economically need, and paid for that
precision with total execution failure.

Also worth flagging: this dossier's dissent list was unusually strong (no primary
source for the hard sunset date, unresolved sign, extension tail risk), and the data
failure deferred rather than resolved it. `outcome: neutral` should not be read as
"the short thesis was fine" — it's untested, not validated.

### Lessons recorded

- Never treat a single missing minute-bar as a terminal skip: exhaust a fallback
  ladder (retry, then adjacent minutes within a stated tolerance e.g. ±5 min same
  session, then a second provider) before recording market-data-unavailable, and log
  which rung filled.
- Size fill-precision to the size of the edge: when expected_profit_pct is under
  ~0.5% and confidence is under 30, use a tolerance window (VWAP over N minutes, or
  nearest available bar within ±X min) instead of an exact-minute target price —
  low-conviction learning-loop trades should be the most execution-robust plans, not
  the most fragile, since their whole purpose is to generate an observation.
