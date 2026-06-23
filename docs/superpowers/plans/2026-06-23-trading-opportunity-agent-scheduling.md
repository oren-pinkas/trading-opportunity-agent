# Trading Opportunity Agent — Plan 4: Scheduling & Ops

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce the scheduling artifacts — a validated `config/schedules.json`, a `bin/run-stage.sh` stage-runner that loads the API key and invokes a stage's skill, and a `SCHEDULES.md` runbook — so the four pipeline stages can be registered as recurring jobs; actual activation is a documented, opt-in manual step.

**Architecture:** Pure Claude Code. Scheduling is config + a thin shell wrapper, not code logic. Each scheduled job invokes one stage skill via the wrapper, which loads `.env` (the Twelve Data key) and runs Claude Code headless. Times are pinned to `America/New_York` so they track the US session through DST. No live cron jobs are created by this plan.

**Tech Stack:** Python 3.11+ (`pytest`, `PyYAML` already present), Bash, JSON. Cron expressions in `America/New_York`.

## Global Constraints

- **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.** Present in `SCHEDULES.md`.
- **Conventional commits, no scope:** `feat:`/`fix:` only. **Branch:** `feat/trading-opportunity-agent-scheduling`.
- **Timezone:** all schedules pinned to `America/New_York`.
- **Schedule (ET):** scout-news 07:00, 12:30, 17:00; research-debate 08:00; simulate-plans 18:30; post-mortem 19:30. (From the spec §5.)
- **Secret:** the stage runner loads `TWELVEDATA_API_KEY` from `.env`; never committed.
- **No auto-activation:** creating live recurring agents is an explicit, separately-confirmed step (cost + requires the repo reachable by the runtime). This plan only produces the artifacts.

---

## File Structure

```
config/schedules.json   ← NEW: timezone + the six cron jobs (machine-readable schedule)
bin/run-stage.sh        ← NEW: load .env, invoke a stage's skill headless
SCHEDULES.md            ← NEW: runbook — how to register (cloud /schedule or local crontab), env, rationale
README.md               ← MODIFY: link to SCHEDULES.md
tests/test_schedules.py ← NEW: validates schedules.json shape/times + run-stage.sh contract
```

---

### Task 1: `config/schedules.json` + validation test

**Files:** Create `config/schedules.json`; Test `tests/test_schedules.py`.

**Interfaces:**
- Produces: a JSON object `{timezone: "America/New_York", jobs: [{name, skill, cron}]}` with exactly the six jobs from the spec. `cron` is standard 5-field `m h dom mon dow`.

- [ ] **Step 1: Write the failing test** — `tests/test_schedules.py`

```python
import json
from pathlib import Path

SCHED = json.loads(Path("config/schedules.json").read_text()) if Path("config/schedules.json").exists() else {}


def test_timezone_is_new_york():
    assert SCHED.get("timezone") == "America/New_York"


def test_six_jobs_match_spec():
    jobs = {(j["skill"], j["cron"]) for j in SCHED.get("jobs", [])}
    expected = {
        ("scout-news", "0 7 * * *"),
        ("scout-news", "30 12 * * *"),
        ("scout-news", "0 17 * * *"),
        ("research-debate", "0 8 * * *"),
        ("simulate-plans", "30 18 * * *"),
        ("post-mortem", "30 19 * * *"),
    }
    assert jobs == expected


def test_job_names_unique():
    names = [j["name"] for j in SCHED.get("jobs", [])]
    assert len(names) == len(set(names)) == 6
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_schedules.py -v` → FAIL (file missing / empty dict).

- [ ] **Step 3: Create `config/schedules.json`**

```json
{
  "timezone": "America/New_York",
  "jobs": [
    {"name": "scout-news-am",  "skill": "scout-news",      "cron": "0 7 * * *"},
    {"name": "scout-news-mid", "skill": "scout-news",      "cron": "30 12 * * *"},
    {"name": "scout-news-pm",  "skill": "scout-news",      "cron": "0 17 * * *"},
    {"name": "research-debate","skill": "research-debate",  "cron": "0 8 * * *"},
    {"name": "simulate-plans", "skill": "simulate-plans",   "cron": "30 18 * * *"},
    {"name": "post-mortem",    "skill": "post-mortem",      "cron": "30 19 * * *"}
  ]
}
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_schedules.py -v` → PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add config/schedules.json tests/test_schedules.py
git commit -m "feat: add schedules config pinned to America/New_York"
```

---

### Task 2: `bin/run-stage.sh` stage runner + contract test

**Files:** Create `bin/run-stage.sh`; Test `tests/test_schedules.py` (add cases).

**Interfaces:**
- Produces: an executable `bin/run-stage.sh <skill-name>` that (1) cds to repo root, (2) loads `.env` if present, (3) invokes Claude Code headless asking it to use the named skill. The exact `claude` invocation is isolated to this one file so it can be adjusted to the local CLI without touching anything else.

- [ ] **Step 1: Write the failing test** — append to `tests/test_schedules.py`

```python
import os
import subprocess


def test_run_stage_script_exists_and_executable():
    p = "bin/run-stage.sh"
    assert os.path.isfile(p)
    assert os.access(p, os.X_OK), "run-stage.sh must be executable"


def test_run_stage_loads_env_and_takes_stage_arg():
    text = open("bin/run-stage.sh").read()
    assert ".env" in text                      # loads the API key
    assert "$1" in text or "${1" in text        # takes the stage name
    assert "claude" in text                      # invokes Claude Code


def test_run_stage_is_valid_bash():
    # `bash -n` parses without executing
    r = subprocess.run(["bash", "-n", "bin/run-stage.sh"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_schedules.py -k run_stage -v` → FAIL.

- [ ] **Step 3: Create `bin/run-stage.sh`**

```bash
#!/usr/bin/env bash
# Run one pipeline stage by invoking its Claude Code skill, headless.
# Usage: bin/run-stage.sh <skill-name>   e.g. bin/run-stage.sh simulate-plans
set -euo pipefail

STAGE="${1:?usage: run-stage.sh <skill-name>}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Load secrets (TWELVEDATA_API_KEY) if present; never required for stub runs.
if [ -f .env ]; then
  set -a; source .env; set +a
fi

# Invoke Claude Code headless and ask it to run the stage's skill.
# (Confirm the exact flags against your local `claude` CLI before activating.)
exec claude -p "Use the ${STAGE} skill. Today is $(date -u +%Y-%m-%dT%H:%MZ)."
```

- [ ] **Step 4: Make executable** — `chmod +x bin/run-stage.sh`

- [ ] **Step 5: Run to verify pass** — `python3 -m pytest tests/test_schedules.py -v` → PASS (6 passed).

- [ ] **Step 6: Commit**

```bash
git add bin/run-stage.sh tests/test_schedules.py
git commit -m "feat: add stage runner that loads env and invokes a skill"
```

---

### Task 3: `SCHEDULES.md` runbook + README link

**Files:** Create `SCHEDULES.md`; Modify `README.md`; Test `tests/test_schedules.py` (add a case).

**Interfaces:** human runbook. Conformance test: mentions all four stage skills, the timezone, the disclaimer, and the env var.

- [ ] **Step 1: Write the failing test** — append to `tests/test_schedules.py`

```python
def test_runbook_covers_stages_env_and_disclaimer():
    text = open("SCHEDULES.md").read()
    for token in ["scout-news", "research-debate", "simulate-plans", "post-mortem",
                  "America/New_York", "TWELVEDATA_API_KEY", "NOT FINANCIAL ADVICE"]:
        assert token in text, f"runbook missing {token}"
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_schedules.py -k runbook -v` → FAIL.

- [ ] **Step 3: Create `SCHEDULES.md`**

```markdown
# Schedules & Operations Runbook

> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

The pipeline runs as four scheduled stages, pinned to **America/New_York** so they
track the US trading session (open 09:30, close 16:00 ET) across DST automatically.
The canonical machine-readable schedule is `config/schedules.json`.

| Time (ET) | Job | Skill | Why then |
|-----------|-----|-------|----------|
| 07:00 | scout-news-am  | `scout-news`      | Pre-market — overnight news |
| 08:00 | research-debate| `research-debate` | After dawn scout, before open — build plans |
| 12:30 | scout-news-mid | `scout-news`      | Midday developments |
| 17:00 | scout-news-pm  | `scout-news`      | Post-close — after-the-bell earnings |
| 18:30 | simulate-plans | `simulate-plans`  | 2.5h after close — minute bars settled |
| 19:30 | post-mortem    | `post-mortem`     | After the simulator writes results |

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
# m h dom mon dow   (set crontab TZ to America/New_York: `CRON_TZ=America/New_York`)
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
```

- [ ] **Step 4: Link from `README.md`** — append a line:

```markdown

## Operations
See `SCHEDULES.md` for the scheduled-stage runbook and how to activate it.
```

- [ ] **Step 5: Run to verify pass** — `python3 -m pytest tests/test_schedules.py -v` → PASS (7 passed).

- [ ] **Step 6: Commit**

```bash
git add SCHEDULES.md README.md tests/test_schedules.py
git commit -m "feat: add scheduling runbook and README link"
```

---

### Task 4: Final verification

**Files:** none.

- [ ] **Step 1: Full suite** — `python3 -m pytest -q` → all green.

- [ ] **Step 2: Sanity-check the runner against the stub** (does not need the API key or live LLM — just confirms the script parses and the stage name flows). Dry parse only:

```bash
bash -n bin/run-stage.sh && echo "run-stage.sh parses OK"
```
Expected: `run-stage.sh parses OK`.

- [ ] **Step 3: Confirm schedules.json is internally consistent with the skills that exist**

```bash
python3 - <<'PY'
import json, os
sched = json.load(open("config/schedules.json"))
for j in sched["jobs"]:
    assert os.path.isfile(f".claude/skills/{j['skill']}/SKILL.md"), j["skill"]
print("all", len(sched["jobs"]), "jobs map to existing skills")
PY
```
Expected: `all 6 jobs map to existing skills`.

- [ ] **Step 4: Commit (if anything regenerated)**

```bash
git add -A && git commit -m "feat: verify scheduling artifacts" || echo "nothing to commit"
```

---

## Self-Review notes (author)

- **Spec coverage:** scheduling §5 — four stages, exact ET times, `America/New_York` pinning (Task 1); env carrying `TWELVEDATA_API_KEY` (Task 2 + runbook Task 3); self-healing-via-status rationale documented (Task 3). Activation deliberately left as opt-in (Global Constraint), consistent with not taking costly outward actions unprompted.
- **Placeholders:** none — all artifacts complete; the one "confirm flags against your local CLI" note concerns an environment-specific value (the `claude` headless invocation), isolated to a single file by design.
- **Type consistency:** the six `(skill, cron)` pairs in `schedules.json` (Task 1) exactly match the runbook table (Task 3) and Task 4's skill-existence check; skill names match the directories created in Plan 3.
- **Cross-plan check:** every `skill` named here (`scout-news`, `research-debate`, `simulate-plans`, `post-mortem`) exists as a `.claude/skills/<name>/SKILL.md` from Plans 2–3.
