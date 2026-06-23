# Schedules & Operations Runbook

> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

The pipeline runs as four scheduled stages, pinned to **America/New_York** so they
track the US trading session (open 09:30, close 16:00 ET) across DST automatically.
The canonical machine-readable schedule is `config/schedules.json`.

| Time (ET) | Job | Skill | Why then |
|-----------|-----|-------|----------|
| 07:00 | scout-news-am   | `scout-news`      | Pre-market — overnight news |
| 08:00 | research-debate | `research-debate` | After dawn scout, before open — build plans |
| 12:30 | scout-news-mid  | `scout-news`      | Midday developments |
| 17:00 | scout-news-pm   | `scout-news`      | Post-close — after-the-bell earnings |
| 18:30 | simulate-plans  | `simulate-plans`  | 2.5h after close — minute bars settled |
| 19:30 | post-mortem     | `post-mortem`     | After the simulator writes results |

**Why the gaps are safe:** status is the queue and is monotonic, so a late or missed
run self-heals — the next run picks up whatever sits in the right status. simulate
(18:30) always sees the day's `scheduled` plans; post-mortem (19:30) always sees what
the simulator just wrote.

## Each job runs

```bash
bin/run-stage.sh <skill-name>
```

which cds to the repo, loads `.env` (providing `TWELVEDATA_API_KEY`), and invokes the
named skill headless.

## Registering the schedule

Two options. **Neither is activated automatically — turning these on creates recurring
agents that consume tokens and (for the simulator) Twelve Data quota.**

### Option A — Claude Code cloud schedule (`/schedule`)
Register each job from `config/schedules.json` as a cloud routine that runs
`Use the <skill> skill.` on the given cron in `America/New_York`. Requires the repo to
be reachable by the cloud runtime (push to a git remote first) and the cloud
environment to provide `TWELVEDATA_API_KEY`.

### Option B — Local crontab
On a machine that stays on during US market hours, with `claude` on PATH:

```cron
CRON_TZ=America/New_York
0 7   * * *  /ABSOLUTE/PATH/bin/run-stage.sh scout-news
30 12 * * *  /ABSOLUTE/PATH/bin/run-stage.sh scout-news
0 17  * * *  /ABSOLUTE/PATH/bin/run-stage.sh scout-news
0 8   * * *  /ABSOLUTE/PATH/bin/run-stage.sh research-debate
30 18 * * *  /ABSOLUTE/PATH/bin/run-stage.sh simulate-plans
30 19 * * *  /ABSOLUTE/PATH/bin/run-stage.sh post-mortem
```

## Environment
- `TWELVEDATA_API_KEY` must be present (in `.env` for local, or the cloud env for A).
  Without it, the simulator falls back to `--provider stub` (fake prices).
