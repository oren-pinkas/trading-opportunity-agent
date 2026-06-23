# Trading Opportunity Agent — Plan 3: Judgement Stages & Learning Loop

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the three LLM-judgement stages — `scout-news`, `research-debate` (with modular personas, debate strategy, and model map), and `post-mortem` (with its own strategy) — plus the `LESSONS.md` learning loop, on top of the deterministic glue they shell out to.

**Architecture:** Skills do judgement (read news, debate, diagnose); deterministic file/arithmetic work stays in tested `lib/` reached via `toa`. This plan adds ledger glue (`create_opportunity`, `find_postmortem_targets`, `record_postmortem`, dedup helper), a lessons store (`lib/lessons.py` extended; machine store `lessons.yaml` rendered to `LESSONS.md`, mirroring the INDEX pattern), new `toa` subcommands, the persona/strategy/config files (the three pluggable slots), and the stage SKILL.md prompts.

**Tech Stack:** Python 3.11+ (stdlib + `PyYAML`), `pytest`. Skills are `SKILL.md` files under `.claude/skills/`. Personas are model-agnostic Markdown. Config is JSON under `config/`.

## Global Constraints

- **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.** Present in every generated artifact and in skill prompts.
- **Conventional commits, no scope:** `feat:`/`fix:` only. **Branch:** `feat/trading-opportunity-agent-judgement`.
- **Personas are model-agnostic:** a persona file must NEVER name a model (`haiku`/`sonnet`/`opus`). The model is injected at spawn time from `config/research.json`. Enforced by a test.
- **Three pluggable slots:** personas (who) / debate strategy skill (how) / model map in `config/*.json` (with what). Orchestrators read config; they don't hardcode strategy or model.
- **Dossier statuses (ordered):** `scouted → researched → scheduled → simulated → analyzed`. Scout creates `scouted`; research produces `researched`/`scheduled`; post-mortem consumes `simulated` and produces `analyzed`.
- **Dedup window:** 14 days (scout). **Post-mortem scope:** `outcome == loss` OR fluke (`outcome` in win/neutral AND `matched_hypothesis == no`).
- **Lessons store:** machine file `lessons.yaml` (list of `{event_type, tickers, text, date, source_id}`); human view `LESSONS.md` rendered from it. `lib.lessons.filter_relevant` (Plan 1) operates on the loaded list.
- **Timestamps:** ISO-8601 UTC; `lib` already tolerates str or datetime.

---

## File Structure

```
lib/
  ledger.py     ← MODIFY: create_opportunity, existing_for_dedup, find_postmortem_targets, record_postmortem
  lessons.py    ← MODIFY: load_lessons, append_lesson, render_lessons_md (filter_relevant already exists)
  cli.py        ← MODIFY: new-opportunity, dedup-check, postmortem-targets, lessons-relevant, record-postmortem, render-lessons
personas/       ← NEW: bull.md bear.md quant.md investigator.md critic.md   (model-agnostic)
config/         ← NEW: research.json postmortem.json scout.json
.claude/skills/
  scout-news/SKILL.md            ← NEW
  research-debate/SKILL.md       ← NEW (orchestrator)
  debate-three-round-panel/SKILL.md  ← NEW (debate strategy)
  post-mortem/SKILL.md           ← NEW (orchestrator)
  pm-investigator-critic/SKILL.md    ← NEW (post-mortem strategy)
tests/
  test_ledger.py / test_lessons.py / test_cli.py  ← MODIFY
  test_personas.py / test_config.py / test_skills_present.py ← NEW/MODIFY
```

---

### Task 1: `find_postmortem_targets`

**Files:** Modify `lib/ledger.py`; Test `tests/test_ledger.py`.

**Interfaces:**
- Consumes: `list_by_status`.
- Produces: `find_postmortem_targets(base="opportunities") -> list[dict]` — items at status `simulated` whose `simulation.outcome == "loss"` OR (`outcome` in {"win","neutral"} AND `simulation.matched_hypothesis == "no"`).

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import find_postmortem_targets


def _simulated_fm(oid, outcome, matched):
    fm = _scheduled_fm(oid, "2026-07-10T13:12:00Z")
    fm["status"] = "simulated"
    fm["simulation"] = {"ran_at": "2026-07-11T00:00:00Z", "fills": [],
                        "realized_profit_pct": -1.0, "outcome": outcome,
                        "matched_hypothesis": matched}
    return fm


def test_find_postmortem_targets_picks_losers_and_flukes(tmp_path):
    _seed(tmp_path, "loss", _simulated_fm("loss", "loss", "no"))
    _seed(tmp_path, "fluke", _simulated_fm("fluke", "win", "no"))
    _seed(tmp_path, "clean", _simulated_fm("clean", "win", "yes"))
    ids = sorted(i["id"] for i in find_postmortem_targets(base=str(tmp_path)))
    assert ids == ["fluke", "loss"]
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_ledger.py -k postmortem_targets -v` → FAIL (ImportError).

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
def find_postmortem_targets(base: str = LEDGER_DIR) -> list[dict]:
    out: list[dict] = []
    for item in list_by_status("simulated", base):
        sim = item["fm"].get("simulation") or {}
        outcome = sim.get("outcome")
        matched = sim.get("matched_hypothesis")
        if outcome == "loss" or (outcome in {"win", "neutral"} and matched == "no"):
            out.append(item)
    return out
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_ledger.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add post-mortem target selection"
```

---

### Task 2: `create_opportunity` + `existing_for_dedup`

**Files:** Modify `lib/ledger.py`; Test `tests/test_ledger.py`.

**Interfaces:**
- Consumes: `lib.dossier.save`, `lib.dossier.validate_frontmatter`.
- Produces:
  - `create_opportunity(oid, title, event, tickers, sources, now, base="opportunities") -> str` — writes `<base>/<oid>/dossier.md` at status `scouted` (`created=now`), returns the path. Result must pass `validate_frontmatter`.
  - `existing_for_dedup(base="opportunities") -> list[dict]` — `[{ "tickers": [...], "last_seen": "<YYYY-MM-DD>" }]` for every dossier, `last_seen` derived from `research.last_updated` else `created` (date portion).

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import create_opportunity, existing_for_dedup


def test_create_opportunity_writes_valid_scouted(tmp_path):
    path = create_opportunity(
        "2026-06-23-fed", "Fed holds", {"type": "macro", "summary": "s", "impact_window": "2026-07-30"},
        ["SPY"], [{"title": "t", "url": "u", "accessed_at": "2026-06-23T10:00:00Z"}],
        "2026-06-23T10:00:00Z", base=str(tmp_path))
    fm, _ = dossier.load(path)
    assert fm["status"] == "scouted"
    assert fm["id"] == "2026-06-23-fed"
    assert dossier.validate_frontmatter(fm) == []


def test_existing_for_dedup_lists_tickers_and_date(tmp_path):
    create_opportunity("2026-06-23-fed", "Fed", {"type": "macro", "summary": "s", "impact_window": "2026-07-30"},
                       ["SPY", "QQQ"], [{"title": "t", "url": "u", "accessed_at": "x"}],
                       "2026-06-23T10:00:00Z", base=str(tmp_path))
    rows = existing_for_dedup(base=str(tmp_path))
    assert rows == [{"tickers": ["SPY", "QQQ"], "last_seen": "2026-06-23"}]
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_ledger.py -k "create_opportunity or existing_for_dedup" -v` → FAIL.

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
def create_opportunity(oid: str, title: str, event: dict, tickers: list,
                       sources: list, now: str, base: str = LEDGER_DIR) -> str:
    d = os.path.join(base, oid)
    os.makedirs(d, exist_ok=True)
    fm = {"id": oid, "title": title, "status": "scouted", "created": now,
          "event": event, "tickers": tickers, "sources": sources}
    path = os.path.join(d, "dossier.md")
    _dossier.save(path, fm, f"## Scouted {now}\n")
    return path


def existing_for_dedup(base: str = LEDGER_DIR) -> list[dict]:
    rows: list[dict] = []
    if not os.path.isdir(base):
        return rows
    for entry in sorted(os.listdir(base)):
        p = os.path.join(base, entry, "dossier.md")
        if not os.path.isfile(p):
            continue
        fm, _ = _dossier.load(p)
        seen = (fm.get("research") or {}).get("last_updated") or fm.get("created", "")
        seen = str(seen)[:10]
        rows.append({"tickers": fm.get("tickers", []), "last_seen": seen})
    return rows
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_ledger.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add opportunity creation and dedup listing"
```

---

### Task 3: Lessons store (load / append / render)

**Files:** Modify `lib/lessons.py`; Test `tests/test_lessons.py`.

**Interfaces:**
- Consumes: nothing new (`filter_relevant` already present).
- Produces:
  - `load_lessons(path) -> list[dict]` — parse a YAML list file; missing file → `[]`.
  - `append_lesson(path, lesson: dict) -> None` — append and rewrite the YAML list.
  - `render_lessons_md(lessons: list[dict]) -> str` — Markdown view with the disclaimer header and one bullet per lesson (`[event_type | tickers] text`).

- [ ] **Step 1: Write the failing test** — append to `tests/test_lessons.py`

```python
from lib.lessons import load_lessons, append_lesson, render_lessons_md


def test_append_then_load_roundtrips(tmp_path):
    p = str(tmp_path / "lessons.yaml")
    assert load_lessons(p) == []
    append_lesson(p, {"event_type": "geopolitical", "tickers": ["USO"],
                      "text": "oil reacts in minutes", "date": "2026-07-11", "source_id": "x"})
    rows = load_lessons(p)
    assert rows[0]["text"] == "oil reacts in minutes"


def test_render_lessons_md_has_disclaimer_and_text():
    md = render_lessons_md([{"event_type": "macro", "tickers": ["SPY"], "text": "priced in early"}])
    assert "NOT FINANCIAL ADVICE" in md
    assert "priced in early" in md
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_lessons.py -k "roundtrips or render" -v` → FAIL.

- [ ] **Step 3: Implement** — append to `lib/lessons.py`

```python
import os
import yaml


def load_lessons(path: str) -> list[dict]:
    if not os.path.isfile(path):
        return []
    return yaml.safe_load(open(path, encoding="utf-8")) or []


def append_lesson(path: str, lesson: dict) -> None:
    rows = load_lessons(path)
    rows.append(lesson)
    with open(path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(rows, fh, sort_keys=False, allow_unicode=True)


def render_lessons_md(lessons: list[dict]) -> str:
    head = ("# Lessons\n\n> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.\n\n")
    body = ""
    for l in lessons:
        tickers = ",".join(l.get("tickers", []))
        body += f"- [{l.get('event_type','')} | {tickers}] {l['text']}\n"
    return head + body
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_lessons.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/lessons.py tests/test_lessons.py
git commit -m "feat: add lessons store load/append/render"
```

---

### Task 4: `record_postmortem` (write-back + learning loop)

**Files:** Modify `lib/ledger.py`; Test `tests/test_ledger.py`.

**Interfaces:**
- Consumes: `lib.dossier.load`, `lib.dossier.append_revision`, `lib.lessons.append_lesson`.
- Produces: `record_postmortem(path, root_cause, lessons, now, lessons_path="lessons.yaml") -> dict` — sets status `analyzed` and writes the `postmortem` block `{ran_at, root_cause, lessons}`; appends each lesson text to the lessons store tagged with the dossier's `event.type` and `tickers` and `date=now[:10]`. Returns `{"id", "root_cause", "lessons_added": <int>}`.

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import record_postmortem
from lib.lessons import load_lessons


def test_record_postmortem_writes_block_and_lessons(tmp_path):
    _seed(tmp_path, "loss", _simulated_fm("loss", "loss", "no"))
    path = str(tmp_path / "loss" / "dossier.md")
    store = str(tmp_path / "lessons.yaml")
    summary = record_postmortem(path, "priced-in", ["entered too late"],
                                "2026-07-12T00:00:00Z", lessons_path=store)
    assert summary["lessons_added"] == 1
    fm, _ = dossier.load(path)
    assert fm["status"] == "analyzed"
    assert fm["postmortem"]["root_cause"] == "priced-in"
    assert dossier.validate_frontmatter(fm) == []
    lessons = load_lessons(store)
    assert lessons[0]["text"] == "entered too late"
    assert lessons[0]["event_type"] == "geopolitical"   # from the dossier's event.type
    assert "USO" in lessons[0]["tickers"]
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_ledger.py -k record_postmortem -v` → FAIL.

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
from lib import lessons as _lessons


def record_postmortem(path: str, root_cause: str, lessons: list, now: str,
                      lessons_path: str = "lessons.yaml") -> dict:
    fm, _ = _dossier.load(path)
    block = {"ran_at": now, "root_cause": root_cause, "lessons": lessons}
    _dossier.append_revision(path, {"status": "analyzed", "postmortem": block},
                             f"Post-mortem: {root_cause}", ts=now)
    event_type = (fm.get("event") or {}).get("type")
    tickers = fm.get("tickers", [])
    for text in lessons:
        _lessons.append_lesson(lessons_path, {
            "event_type": event_type, "tickers": tickers,
            "text": text, "date": now[:10], "source_id": fm.get("id")})
    return {"id": fm.get("id"), "root_cause": root_cause, "lessons_added": len(lessons)}
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_ledger.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add post-mortem write-back feeding the lessons store"
```

---

### Task 5: `toa` subcommands for the judgement stages

**Files:** Modify `lib/cli.py`; Test `tests/test_cli.py`.

**Interfaces:**
- Consumes: `ledger.create_opportunity`, `ledger.existing_for_dedup`, `ledger.find_postmortem_targets`, `ledger.record_postmortem`, `lessons.load_lessons`, `lessons.filter_relevant`, `lessons.render_lessons_md`, `lib.dedup.is_duplicate`.
- Produces CLI subcommands (JSON to stdout):
  - `toa postmortem-targets [--base DIR]` → `{"ids": [...]}`
  - `toa dedup-check --tickers A,B --today YYYY-MM-DD [--base DIR] [--window 14]` → `{"duplicate": bool}`
  - `toa lessons-relevant --type T --tickers A,B [--store lessons.yaml]` → `{"lessons": [...]}`
  - `toa record-postmortem PATH --root-cause X --lesson "..." [--lesson "..."] --now ISO [--store lessons.yaml]` → summary dict
  - `toa render-lessons [--store lessons.yaml] [--out LESSONS.md]` → `{"written": OUT}`

- [ ] **Step 1: Write the failing test** — append to `tests/test_cli.py`

```python
def test_cli_dedup_check(tmp_path):
    _seed_scheduled(tmp_path, "x")  # tickers [USO], created 2026-06-22
    r = _run("dedup-check", "--tickers", "USO", "--today", "2026-06-23", "--base", str(tmp_path))
    assert json.loads(r.stdout)["duplicate"] is True


def test_cli_postmortem_targets_empty(tmp_path):
    r = _run("postmortem-targets", "--base", str(tmp_path))
    assert json.loads(r.stdout)["ids"] == []
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_cli.py -k "dedup_check or postmortem_targets" -v` → FAIL.

- [ ] **Step 3: Implement** — in `lib/cli.py` add `from lib import dedup, lessons as lessons_mod` to imports, register parsers after `reindex`:

```python
    pt = sub.add_parser("postmortem-targets")
    pt.add_argument("--base", default="opportunities")

    dc = sub.add_parser("dedup-check")
    dc.add_argument("--tickers", required=True); dc.add_argument("--today", required=True)
    dc.add_argument("--base", default="opportunities"); dc.add_argument("--window", type=int, default=14)

    lr = sub.add_parser("lessons-relevant")
    lr.add_argument("--type", required=True); lr.add_argument("--tickers", default="")
    lr.add_argument("--store", default="lessons.yaml")

    rp = sub.add_parser("record-postmortem")
    rp.add_argument("path"); rp.add_argument("--root-cause", required=True, dest="root_cause")
    rp.add_argument("--lesson", action="append", default=[], dest="lessons")
    rp.add_argument("--now", required=True); rp.add_argument("--store", default="lessons.yaml")

    rl = sub.add_parser("render-lessons")
    rl.add_argument("--store", default="lessons.yaml"); rl.add_argument("--out", default="LESSONS.md")
```

and branches before `return 2`:

```python
    if args.cmd == "postmortem-targets":
        print(json.dumps({"ids": [i["id"] for i in ledger.find_postmortem_targets(base=args.base)]}))
        return 0
    if args.cmd == "dedup-check":
        cand = {"tickers": [t for t in args.tickers.split(",") if t]}
        dup = dedup.is_duplicate(cand, ledger.existing_for_dedup(base=args.base),
                                 today=args.today, window_days=args.window)
        print(json.dumps({"duplicate": dup}))
        return 0
    if args.cmd == "lessons-relevant":
        rows = lessons_mod.load_lessons(args.store)
        tickers = [t for t in args.tickers.split(",") if t]
        print(json.dumps({"lessons": lessons_mod.filter_relevant(rows, args.type, tickers)}))
        return 0
    if args.cmd == "record-postmortem":
        print(json.dumps(ledger.record_postmortem(args.path, args.root_cause, args.lessons,
                                                  args.now, lessons_path=args.store)))
        return 0
    if args.cmd == "render-lessons":
        text = lessons_mod.render_lessons_md(lessons_mod.load_lessons(args.store))
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(json.dumps({"written": args.out}))
        return 0
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_cli.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/cli.py tests/test_cli.py
git commit -m "feat: add judgement-stage subcommands to toa CLI"
```

---

### Task 6: Personas (model-agnostic) + conformance test

**Files:** Create `personas/{bull,bear,quant,investigator,critic}.md`; Test `tests/test_personas.py`.

**Interfaces:** consumed by the orchestrator skills at spawn time. Each file has frontmatter `name` + `role`, and a body describing worldview/biases/what-they-look-for. NO model names anywhere.

- [ ] **Step 1: Write the failing test** — `tests/test_personas.py`

```python
from pathlib import Path
import re
import yaml

PERSONAS = ["bull", "bear", "quant", "investigator", "critic"]


def test_personas_exist_with_frontmatter():
    for name in PERSONAS:
        p = Path(f"personas/{name}.md")
        assert p.is_file(), f"missing {p}"
        _, fm_block, body = p.read_text().split("---", 2)
        fm = yaml.safe_load(fm_block)
        assert fm.get("name") == name and fm.get("role")
        assert len(body.strip()) > 50


def test_personas_are_model_agnostic():
    for name in PERSONAS:
        text = Path(f"personas/{name}.md").read_text().lower()
        assert not re.search(r"\b(haiku|sonnet|opus)\b", text), f"{name} names a model"
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_personas.py -v` → FAIL.

- [ ] **Step 3: Create the five persona files.**

`personas/bull.md`:
```markdown
---
name: bull
role: Catalyst-hunter
---
You hunt for why this event MOVES the stock and how to ride it. Momentum- and
narrative-driven, optimistic, fast. You look for the upside path, the catalyst
timing, and the cleanest instrument to express it. You argue for taking the
opportunity; you are biased toward action. Cite concrete evidence (sources, dates,
numbers), not vibes.
```

`personas/bear.md`:
```markdown
---
name: bear
role: Skeptic
---
You hunt for why the thesis is WRONG. Risk- and disconfirmation-driven. You ask what
is already priced in, what the consensus is, what could blow the trade up, and what
the bull is ignoring. You are biased toward caution and demand evidence. Cite
sources; name the specific risk and how it would play out.
```

`personas/quant.md`:
```markdown
---
name: quant
role: Pragmatist
---
You care about base rates, historical analogues, and expected value AFTER costs and
slippage. You weigh probability and magnitude, not story. You size positions and ask
whether the edge survives fees and timing. You break ties with numbers. State your
assumed probabilities and the EV calculation explicitly.
```

`personas/investigator.md`:
```markdown
---
name: investigator
role: Reconstructor
---
You reconstruct what ACTUALLY happened from the price path and the simulation log.
You compare the realized move to what the plan expected, minute by minute if needed.
You state facts: entry/exit prices used, realized result, where reality diverged from
the plan. No blame yet — just an accurate timeline grounded in the cited data.
```

`personas/critic.md`:
```markdown
---
name: critic
role: Diagnostician
---
You assign a root cause for a losing or fluke trade by comparing reality to the debate
transcript. You ask: was the error knowable at research time? Classify it as one of
wrong-assumption, missing-info, timing, data, or priced-in. You distinguish bad
process from bad luck, and you propose the single most useful lesson to carry forward.
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_personas.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add personas/ tests/test_personas.py
git commit -m "feat: add model-agnostic personas for debate and post-mortem"
```

---

### Task 7: Config files (the model-map slot) + conformance test

**Files:** Create `config/{research,postmortem,scout}.json`; Test `tests/test_config.py`.

**Interfaces:** read by the orchestrator skills at runtime. `research.json`: `{strategy, personas[], models{}}`. `postmortem.json`: `{strategy, roles[], models{}}`. `scout.json`: `{model, source_hints[], dedupe_window_days}`.

- [ ] **Step 1: Write the failing test** — `tests/test_config.py`

```python
import json
from pathlib import Path


def test_research_config_shape():
    c = json.loads(Path("config/research.json").read_text())
    assert c["strategy"] == "three-round-panel"
    assert set(c["personas"]) >= {"bull", "bear", "quant"}
    assert {"bull", "bear", "quant", "synthesizer"} <= set(c["models"])


def test_postmortem_config_shape():
    c = json.loads(Path("config/postmortem.json").read_text())
    assert c["strategy"] == "investigator-critic"
    assert {"investigator", "critic"} <= set(c["roles"])


def test_scout_config_shape():
    c = json.loads(Path("config/scout.json").read_text())
    assert c["dedupe_window_days"] == 14
    assert "source_hints" in c
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_config.py -v` → FAIL.

- [ ] **Step 3: Create the config files.**

`config/research.json`:
```json
{
  "strategy": "three-round-panel",
  "personas": ["bull", "bear", "quant"],
  "models": {"bull": "sonnet", "bear": "sonnet", "quant": "opus", "synthesizer": "opus"}
}
```

`config/postmortem.json`:
```json
{
  "strategy": "investigator-critic",
  "roles": ["investigator", "critic"],
  "models": {"investigator": "sonnet", "critic": "opus", "synthesizer": "opus"}
}
```

`config/scout.json`:
```json
{
  "model": "haiku",
  "source_hints": [],
  "dedupe_window_days": 14
}
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_config.py -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add config/ tests/test_config.py
git commit -m "feat: add research/postmortem/scout config (model-map slot)"
```

---

### Task 8: `scout-news` skill

**Files:** Create `.claude/skills/scout-news/SKILL.md`; Modify `tests/test_skills_present.py`.

**Interfaces:** uses `toa dedup-check` and `toa new-opportunity` (wait — `new-opportunity` CLI is added here). NOTE: this task also adds the `new-opportunity` subcommand the scout needs.

- [ ] **Step 1: Add `new-opportunity` test** — append to `tests/test_cli.py`

```python
def test_cli_new_opportunity(tmp_path):
    r = _run("new-opportunity", "--id", "2026-06-23-fed", "--title", "Fed holds",
             "--type", "macro", "--summary", "s", "--impact-window", "2026-07-30",
             "--tickers", "SPY", "--source-title", "wire", "--source-url", "https://x",
             "--now", "2026-06-23T10:00:00Z", "--base", str(tmp_path))
    assert json.loads(r.stdout)["status"] == "scouted"
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest tests/test_cli.py -k new_opportunity -v` → FAIL.

- [ ] **Step 3: Implement `new-opportunity`** — in `lib/cli.py` register parser after `render-lessons`:

```python
    no = sub.add_parser("new-opportunity")
    no.add_argument("--id", required=True, dest="oid"); no.add_argument("--title", required=True)
    no.add_argument("--type", required=True, dest="etype"); no.add_argument("--summary", required=True)
    no.add_argument("--impact-window", required=True, dest="impact_window")
    no.add_argument("--tickers", required=True); no.add_argument("--source-title", required=True, dest="stitle")
    no.add_argument("--source-url", required=True, dest="surl"); no.add_argument("--now", required=True)
    no.add_argument("--base", default="opportunities")
```

and branch:

```python
    if args.cmd == "new-opportunity":
        event = {"type": args.etype, "summary": args.summary, "impact_window": args.impact_window}
        sources = [{"title": args.stitle, "url": args.surl, "accessed_at": args.now}]
        path = ledger.create_opportunity(args.oid, args.title, event,
                                         args.tickers.split(","), sources, args.now, base=args.base)
        fm, _ = dossier.load(path)
        print(json.dumps({"path": path, "status": fm["status"]}))
        return 0
```

- [ ] **Step 4: Run to verify pass** — `python3 -m pytest tests/test_cli.py -v` → PASS.

- [ ] **Step 5: Create `.claude/skills/scout-news/SKILL.md`**

```markdown
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
```

- [ ] **Step 6: Update `tests/test_skills_present.py`** — extend the `SKILLS` list:

```python
SKILLS = ["market-data", "simulate-plans", "scout-news",
          "research-debate", "debate-three-round-panel",
          "post-mortem", "pm-investigator-critic"]
```

(The two research/post-mortem skills are created in Tasks 9–10; run this test at the end of Task 10.)

- [ ] **Step 7: Commit**

```bash
git add lib/cli.py .claude/skills/scout-news/SKILL.md tests/test_cli.py tests/test_skills_present.py
git commit -m "feat: add scout-news skill and new-opportunity command"
```

---

### Task 9: `research-debate` orchestrator + `debate-three-round-panel` strategy

**Files:** Create `.claude/skills/research-debate/SKILL.md`, `.claude/skills/debate-three-round-panel/SKILL.md`.

**Interfaces:** orchestrator reads `config/research.json`, `toa ls --status scouted`/`researched`, `toa lessons-relevant`; strategy runs the 3-round panel and writes the dossier via dossier edits + records the plan. Plan/hypothesis are written by the synthesizer directly into the dossier frontmatter (validated with `toa validate`).

- [ ] **Step 1: Create `.claude/skills/research-debate/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Create `.claude/skills/debate-three-round-panel/SKILL.md`**

```markdown
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
```

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/research-debate/SKILL.md .claude/skills/debate-three-round-panel/SKILL.md
git commit -m "feat: add research-debate orchestrator and three-round-panel strategy"
```

---

### Task 10: `post-mortem` orchestrator + `pm-investigator-critic` strategy

**Files:** Create `.claude/skills/post-mortem/SKILL.md`, `.claude/skills/pm-investigator-critic/SKILL.md`; run `tests/test_skills_present.py`.

- [ ] **Step 1: Create `.claude/skills/post-mortem/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Create `.claude/skills/pm-investigator-critic/SKILL.md`**

```markdown
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
```

- [ ] **Step 3: Run the skills conformance test** — `python3 -m pytest tests/test_skills_present.py -v` → PASS (all 7 skills present with frontmatter).

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/post-mortem/SKILL.md .claude/skills/pm-investigator-critic/SKILL.md
git commit -m "feat: add post-mortem orchestrator and investigator-critic strategy"
```

---

### Task 11: Manual end-to-end verification of the deterministic loop

**Files:** none committed beyond regenerated `LESSONS.md` (optional).

- [ ] **Step 1: Full suite** — `python3 -m pytest -q` → all green.

- [ ] **Step 2: Exercise the post-mortem learning loop on a temp ledger** (no LLM needed):

```bash
python3 - <<'PY'
import tempfile, os, json
from lib import ledger, dossier
base = tempfile.mkdtemp()
# seed a losing simulated dossier
from tests.test_ledger import _simulated_fm, _seed
import pathlib
_seed(pathlib.Path(base), "loss", _simulated_fm("loss", "loss", "no"))
store = os.path.join(base, "lessons.yaml")
print("targets:", [i["id"] for i in ledger.find_postmortem_targets(base=base)])
print(ledger.record_postmortem(os.path.join(base, "loss", "dossier.md"),
      "priced-in", ["oil headlines price in within minutes"],
      "2026-07-12T00:00:00Z", lessons_path=store))
from lib.lessons import load_lessons, filter_relevant
rel = filter_relevant(load_lessons(store), "geopolitical", ["USO"])
print("relevant lessons:", [l["text"] for l in rel])
PY
```
Expected: targets `['loss']`; record summary `lessons_added: 1`; relevant lessons lists the oil lesson. Confirms target-selection → write-back → store → relevance-filter (the full loop) works.

- [ ] **Step 3: Confirm personas are model-agnostic and configs valid** — `python3 -m pytest tests/test_personas.py tests/test_config.py tests/test_skills_present.py -q` → all green.

- [ ] **Step 4: Commit any regenerated artifact** (only if changed):

```bash
git add -A && git commit -m "feat: verify judgement-stage deterministic loop end-to-end" || echo "nothing to commit"
```

---

## Self-Review notes (author)

- **Spec coverage:** scout §4① (Task 8 + dedup Tasks 2,5 + scout.json Task 7); research-debate §4② orchestrator + 3-round strategy + personas + model map + lessons injection (Tasks 6,7,9 + lessons-relevant Tasks 3,5); post-mortem §4④ losers+flukes + investigator-critic + write-back (Tasks 1,4,6,7,10); learning loop §4 (Tasks 3,4 + render Task 5); modular slots Global Constraint (personas Task 6, config Task 7, strategy skills Tasks 9–10). **Deferred to Plan 4:** cron scheduling.
- **Placeholders:** none — all code/test/prompt content is complete.
- **Type consistency:** `find_postmortem_targets`/`create_opportunity`/`existing_for_dedup`/`record_postmortem` signatures consistent across ledger Tasks 1,2,4 and CLI Tasks 5,8; lessons store dict shape `{event_type,tickers,text,date,source_id}` consistent across Tasks 3,4,5; `filter_relevant` reused from Plan 1 unchanged.
