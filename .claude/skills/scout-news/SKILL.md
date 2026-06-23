---
name: scout-news
description: Three-times-daily news scout. Extracts forward-looking, market-moving events from current news and records each as a new opportunity dossier, skipping recent duplicates.
---

# scout-news

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE. You filter news into candidate
opportunities — you do not research or trade. Stay fast and cheap.

Read `config/scout.json` for `source_hints` (may be empty = open-ended) and
`dedupe_window_days`.

## Procedure

1. Use web search to find FORWARD-LOOKING, market-moving events: geopolitics, macro/
   rates, scheduled earnings, product/feature launches, IPOs, regulation. Each must
   have a future or very-recent catalyst and at least one affected ticker.
2. For each candidate, choose an id `YYYY-MM-DD-short-slug`, the affected tickers, and
   an `event.type` (geopolitical|economic|earnings|product|macro|regulatory|ipo).
3. Skip recent duplicates:

   ```bash
   toa dedup-check --tickers <T1,T2> --today <YYYY-MM-DD>
   # -> {"duplicate": true|false}
   ```
   If `true`, do not recreate it.
4. Otherwise record it (cite a real source URL):

   ```bash
   toa new-opportunity --id <id> --title "<title>" --type <type> \
     --summary "<one line>" --impact-window <YYYY-MM-DD> --tickers <T1,T2> \
     --source-title "<source>" --source-url "<url>" --now <CURRENT-ISO-UTC>
   ```
5. Report how many new opportunities you created and their ids. Do NOT form a
   hypothesis or plan — that is the research stage's job.
