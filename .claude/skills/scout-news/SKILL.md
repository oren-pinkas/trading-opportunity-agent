---
name: scout-news
description: Three-times-daily news scout. Extracts forward-looking, market-moving events from current news and records each as a new opportunity dossier, skipping recent duplicates.
---

# scout-news

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE. You filter news into candidate
opportunities — you do not research or trade. Stay fast and cheap.

Read `config/scout.json` for `source_hints` (may be empty = open-ended),
`dedupe_window_days`, and `target_opportunities_per_run` (how many distinct NEW
opportunities to aim for this run; default 3 if absent).

## Procedure

1. Use web search to find FORWARD-LOOKING, market-moving events: geopolitics, macro/
   rates, scheduled earnings, product/feature launches, IPOs, regulation. Each must
   have a future or very-recent catalyst and at least one affected ticker. Cast a WIDE
   net to reach `target_opportunities_per_run` distinct NON-duplicate opportunities:
   span multiple sectors, market caps (incl. mid/small-cap), and event types rather
   than clustering on one theme — run several varied searches if the first pass yields
   too few new (non-duplicate) candidates. Quality still gates: skip anything without a
   real forward catalyst and an affected ticker.
2. For each candidate, choose an id `YYYY-MM-DD-short-slug`, the affected tickers, and
   an `event.type` (geopolitical|economic|earnings|product|macro|regulatory|ipo).
3. Skip recent duplicates:

   ```bash
   toa dedup-check --tickers <T1,T2> --today <YYYY-MM-DD> --window <dedupe_window_days>
   # -> {"duplicate": true|false}
   ```
   Pass `--window` = the `dedupe_window_days` from `config/scout.json` (do not rely on
   the CLI default). If `true`, do not recreate it.
4. Otherwise record it (cite a real source URL):

   ```bash
   toa new-opportunity --id <id> --title "<title>" --type <type> \
     --summary "<one line>" --impact-window <YYYY-MM-DD> --tickers <T1,T2> \
     --source-title "<source>" --source-url "<url>" --now <CURRENT-ISO-UTC>
   ```
5. Report how many new opportunities you created and their ids. Do NOT form a
   hypothesis or plan — that is the research stage's job.
