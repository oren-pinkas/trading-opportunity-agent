---
name: post-mortem
description: Once-daily post-mortem of losing and fluke simulations. Runs the configured post-mortem strategy to diagnose root cause and extract lessons that feed back into research.
---

# post-mortem

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

You diagnose what went wrong on trades that lost or won for the wrong reason, and you
turn each into a durable lesson. Orchestrator only; the diagnosis is the strategy's.

## Procedure

1. Read `config/postmortem.json`: `strategy`, `roles`, `models`.
2. Find targets (losers + flukes; clean wins are skipped):

   ```bash
   toa postmortem-targets
   # -> {"ids": [...]}
   ```
3. For each id, invoke the strategy named by `config.strategy` (default
   `pm-investigator-critic`), passing the dossier, its `transcript.md`, its
   `simulation.md`, the roles, and the model map.
4. The strategy returns a `root_cause`
   (wrong-assumption|missing-info|timing|data|priced-in) and one or more `lessons`.
   Record them — this also flips status to `analyzed` and appends to the lessons store:

   ```bash
   toa record-postmortem opportunities/<id>/dossier.md \
     --root-cause <cause> --lesson "<lesson>" [--lesson "<lesson>"] --now <CURRENT-ISO-UTC>
   ```
5. Write the full analysis to `opportunities/<id>/postmortem.md` (cite the price path
   and the transcript passages you relied on).
6. Refresh the human lessons view and report:

   ```bash
   toa render-lessons
   ```
