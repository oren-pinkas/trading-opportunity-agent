---
name: debate-three-round-panel
description: A debate strategy. Runs three independent persona subagents through three rounds (independent research, rebuttal, synthesis) to produce a hypothesis, action plan, confidence, and dissent note. Swappable with other strategies via config.
---

# debate-three-round-panel

Inputs (from the research-debate orchestrator): the dossier, the persona set, the
model map, and the relevant lessons. Output: hypothesis + plan + confidence + dissent
+ transcript. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Protocol

- **Round 1 — Independent research (parallel).** Spawn each persona as its own subagent
  on its configured model, given the event, sources, and relevant lessons — but NOT
  each other's views. Each writes an opening position: their read, their evidence
  (cited), and a proposed action.
- **Round 2 — Rebuttal (parallel).** Show each persona the other two opening positions.
  Each writes a rebuttal: disagreements, what the others missed, what would change
  their mind.
- **Round 3 — Convergence.** A neutral synthesizer (on its configured model) reads the
  full transcript and produces:
  - `hypothesis`: {statement, direction (long|short), confidence 0–100}
  - `plan`: {ticker, action (buy|sell|short), entry {time, target_price},
    exit {time, target_price}, expected_profit_pct}
  - `dissent`: the strongest unresolved disagreement (gold for the post-mortem).

Record every position, rebuttal, and the synthesis in `transcript.md` with source
citations. Prices referenced for targets should be sanity-checked with
`toa price <ticker> <ts>` where useful. Entry/exit times must be specific ISO-8601
UTC minutes.
