---
name: pm-investigator-critic
description: A post-mortem strategy. Two roles — an investigator reconstructs what happened, a critic assigns a root cause by comparing reality to the debate transcript — then a synthesizer writes the lessons. Swappable via config.
---

# pm-investigator-critic

Inputs (from the post-mortem orchestrator): the dossier, its `transcript.md`,
`simulation.md`, the roles, and the model map. Output: a `root_cause` and a list of
`lessons`. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Protocol

- **Investigator (on its configured model).** Using `personas/investigator.md`,
  reconstruct what actually happened from the simulation fills and price path. State
  the realized result vs the plan's expectation, and exactly where reality diverged.
- **Critic (on its configured model).** Using `personas/critic.md`, compare that
  reconstruction to the debate `transcript.md` and the recorded `dissent`. Decide
  whether the error was knowable at research time and classify the `root_cause` as one
  of: wrong-assumption, missing-info, timing, data, priced-in.
- **Synthesizer.** Distil one or two crisp, reusable `lessons` (each tagged implicitly
  by the dossier's event type and tickers when recorded). A good lesson is specific
  and actionable for a future similar setup, e.g. "diplomacy headlines on oil are
  largely priced within the first 3 minutes — avoid same-minute entries."
