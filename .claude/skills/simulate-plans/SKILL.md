---
name: simulate-plans
description: Once-daily simulation of due trade plans. Finds scheduled dossiers whose exit time has passed, fills them against real prices, computes P/L, and records the outcome. Run after the US close.
---

# simulate-plans

You simulate — you never trade. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

All arithmetic and price-fetching is done by tested code via the `toa` CLI. Your job
is orchestration and narrative, not computation.

## Procedure

1. Find the plans due for simulation (exit time now in the past, not yet simulated):

   ```bash
   toa simulatable --now <CURRENT-ISO-UTC>
   # -> {"ids": ["2026-06-22-oil-iran-talks", ...]}
   ```

2. For each id, run the deterministic simulation against the dossier. Use
   `--provider twelvedata` if `TWELVEDATA_API_KEY` is set, else `--provider stub`:

   ```bash
   toa simulate opportunities/<id>/dossier.md --now <CURRENT-ISO-UTC> --provider twelvedata
   # -> {"id": "...", "outcome": "win", "realized_profit_pct": 0.85, "matched_hypothesis": "partial"}
   ```

   This writes the `simulation` block into the dossier and flips its status to
   `simulated`. Do NOT compute P/L or edit the block yourself. If a plan's date had no
   market data (holiday/weekend), the command records a `neutral` outcome with an
   explanatory note rather than failing the run.

3. Append a short, human-readable narrative to `opportunities/<id>/simulation.md`:
   what the plan intended, the entry/exit prices actually used and their cited
   `source`, the realized result, and whether reality matched the hypothesis. Read
   the dossier's `simulation.fills` for the exact prices and sources to cite.

4. Regenerate the dashboard:

   ```bash
   toa reindex
   ```

5. Report a one-line summary per simulated plan (id, outcome, realized %).

If `toa simulatable` returns no ids, there is nothing due — report that and stop.
