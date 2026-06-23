---
name: research-debate
description: Once-daily deep research. For each scouted or researched opportunity, runs the configured debate strategy with the configured personas and model map, producing a hypothesis, an action plan, a confidence level, and a cited transcript.
---

# research-debate

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

You are the orchestrator. You do not hold opinions; you run a configured debate and
record its result. The three pluggable slots come from config, never hardcoded.

## Procedure

1. Read `config/research.json`: `strategy`, `personas`, `models` (the model each
   persona/synthesizer runs on — injected, not baked into persona files).
2. Find work:

   ```bash
   toa ls --status scouted     # new
   toa ls --status researched  # revisit only if materially new info since research.last_updated
   ```
3. For each opportunity, gather institutional memory:

   ```bash
   toa lessons-relevant --type <event.type> --tickers <tickers>
   # -> {"lessons": [...]}  # inject these as context to each persona
   ```
4. Invoke the debate strategy named by `config.strategy` (default
   `debate-three-round-panel`), passing: the dossier, the persona set, the model map,
   and the relevant lessons. Spawn each persona as a subagent on its configured model
   (load the persona text from `personas/<name>.md`; the persona file is the character,
   the model is the injected runtime).
5. The strategy returns hypothesis + plan + confidence + dissent + a transcript. Write
   the `hypothesis`, `plan`, and `research` blocks into the dossier frontmatter, write
   the full debate to `opportunities/<id>/transcript.md` (with citations), set
   `research.last_updated` to now, and set status to `researched` (or `scheduled` if
   the plan's entry/exit times are in the future). On a revisit, append a timestamped
   revision rather than overwriting.
6. Validate every dossier you touched:

   ```bash
   toa validate opportunities/<id>/dossier.md   # must be {"valid": true}
   ```
7. Report the opportunities researched and their hypotheses one-line each.
