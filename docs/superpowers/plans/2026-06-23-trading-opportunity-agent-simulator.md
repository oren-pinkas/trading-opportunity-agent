# Trading Opportunity Agent — Plan 2: Ledger Glue & Simulator (Deterministic Keystone)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the deterministic ledger-navigation layer plus a fully-tested `simulate-plans` stage that reads `scheduled` dossiers, fills them against real (stub or Twelve Data) prices, computes P/L, and writes back a valid `simulated` dossier — all reachable from one `toa simulate` command that an LLM skill thinly wraps.

**Architecture:** Pure Claude Code system (skills + file ledger + cron). Plan 1 delivered the pure primitives (`pnl`, `marketdata`, `dossier`, `index`). This plan adds `lib/ledger.py` (navigation + simulation orchestration over the `opportunities/` tree), extends the `toa` CLI with ledger subcommands, and authors the first two agent skills (`market-data`, `simulate-plans`) which are *thin* — they call `toa`, not LLM arithmetic. The simulator is built before the LLM producers (scout/research) because, as the deterministic *consumer* of `scheduled` dossiers, it pins down exactly what those producers must emit.

**Tech Stack:** Python 3.11+ (stdlib + `PyYAML`), `pytest`. Skills are `SKILL.md` prompt files under `.claude/skills/`. Market data via `lib.marketdata` (stub default, Twelve Data when `TWELVEDATA_API_KEY` is set).

## Global Constraints

- **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.** Present in `README.md` and `INDEX.md` (asserted by existing Plan 1 tests).
- **Conventional commits, no scope:** only `feat:` / `fix:` prefixes. **Branch:** all work on `feat/trading-opportunity-agent-simulator`.
- **Provider seam:** price access only via `lib.marketdata.get_price`; `lib/ledger.py` accepts an injectable `get_price` so tests never touch the network.
- **Timestamps:** ISO-8601 UTC (`...Z`). `lib.ledger` parses them by converting `Z`→`+00:00`.
- **Dossier statuses (ordered):** `scouted → researched → scheduled → simulated → analyzed`. The simulator consumes `scheduled` and produces `simulated`.
- **Ledger root:** `opportunities/` (each opportunity is `opportunities/<id>/dossier.md`). All `lib/ledger.py` functions take a `base` parameter defaulting to `"opportunities"` so tests use `tmp_path`.
- **Determinism rule for `matched_hypothesis`:** compare realized vs the plan's `expected_profit_pct` — `no` if realized ≤ 0; `yes` if realized ≥ 50% of expected; `partial` otherwise. (A deterministic baseline; later judgement stages may refine it.)

---

## File Structure

```
lib/
  ledger.py          ← NEW: list_by_status, find_simulatable, build_simulation_block,
                       simulate_dossier, regenerate_index
  cli.py             ← MODIFY: add `ls`, `simulatable`, `simulate`, `reindex` subcommands
tests/
  test_ledger.py     ← NEW
  test_cli.py        ← MODIFY: add simulate/simulatable cases
.claude/skills/
  market-data/SKILL.md     ← NEW: thin doc — "to get a price, run `toa price ...`"
  simulate-plans/SKILL.md  ← NEW: orchestration prompt wrapping `toa simulatable`/`simulate`/`reindex`
tests/
  test_skills_present.py   ← NEW: conformance — skill files exist with valid frontmatter
opportunities/             ← (created by manual verification task; not a code dir)
```

`lib/ledger.py` is the only new module; it composes Plan 1 primitives and owns all `opportunities/`-tree I/O so the skills stay thin.

---

### Task 1: `list_by_status` + `find_simulatable`

**Files:**
- Create: `lib/ledger.py`
- Test: `tests/test_ledger.py`

**Interfaces:**
- Consumes: `lib.dossier.load`, `lib.dossier.save`.
- Produces:
  - `list_by_status(status: str, base: str = "opportunities") -> list[dict]` — each item `{"id", "path", "fm"}`, sorted by directory name. Missing `base` dir → `[]`.
  - `find_simulatable(now: str, base: str = "opportunities") -> list[dict]` — items at status `scheduled` whose `plan.exit.time <= now` and that have no truthy `simulation` block.

- [ ] **Step 1: Write the failing test** — `tests/test_ledger.py`

```python
from lib import dossier, ledger


def _scheduled_fm(oid, exit_time):
    return {
        "id": oid, "title": "t", "status": "scheduled",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"],
        "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
        "hypothesis": {"statement": "h", "direction": "short", "confidence": 65},
        "plan": {"ticker": "USO", "action": "short",
                 "entry": {"time": "2026-07-10T13:00:00Z", "target_price": 100.0},
                 "exit": {"time": exit_time, "target_price": 90.0},
                 "expected_profit_pct": 2.0},
        "research": {"strategy": "three-round-panel",
                     "models": {"bull": "sonnet"}, "last_updated": "2026-06-22T11:00:00Z"},
    }


def _seed(base, oid, fm):
    import os
    d = base / oid
    d.mkdir(parents=True)
    dossier.save(str(d / "dossier.md"), fm, "## Seed\n")


def test_list_by_status_filters(tmp_path):
    _seed(tmp_path, "a", _scheduled_fm("a", "2026-07-10T13:12:00Z"))
    fm_other = _scheduled_fm("b", "2026-07-10T13:12:00Z"); fm_other["status"] = "scouted"
    _seed(tmp_path, "b", fm_other)
    got = ledger.list_by_status("scheduled", base=str(tmp_path))
    assert [i["id"] for i in got] == ["a"]


def test_find_simulatable_respects_exit_time(tmp_path):
    _seed(tmp_path, "past", _scheduled_fm("past", "2026-07-10T13:12:00Z"))
    _seed(tmp_path, "future", _scheduled_fm("future", "2026-12-31T13:12:00Z"))
    got = ledger.find_simulatable("2026-07-11T00:00:00Z", base=str(tmp_path))
    assert [i["id"] for i in got] == ["past"]


def test_missing_base_returns_empty():
    assert ledger.list_by_status("scheduled", base="/nonexistent/path") == []
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_ledger.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'lib.ledger'`.

- [ ] **Step 3: Implement** — `lib/ledger.py`

```python
"""Ledger navigation and deterministic simulation over the opportunities tree."""
import os
from datetime import datetime

from lib import dossier as _dossier

LEDGER_DIR = "opportunities"


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def list_by_status(status: str, base: str = LEDGER_DIR) -> list[dict]:
    out: list[dict] = []
    if not os.path.isdir(base):
        return out
    for entry in sorted(os.listdir(base)):
        path = os.path.join(base, entry, "dossier.md")
        if not os.path.isfile(path):
            continue
        fm, _ = _dossier.load(path)
        if fm.get("status") == status:
            out.append({"id": fm.get("id", entry), "path": path, "fm": fm})
    return out


def find_simulatable(now: str, base: str = LEDGER_DIR) -> list[dict]:
    now_dt = _parse_iso(now)
    out: list[dict] = []
    for item in list_by_status("scheduled", base):
        fm = item["fm"]
        if fm.get("simulation"):
            continue
        exit_time = fm.get("plan", {}).get("exit", {}).get("time")
        if exit_time and _parse_iso(exit_time) <= now_dt:
            out.append(item)
    return out
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_ledger.py -v`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add ledger status listing and simulatable selection"
```

---

### Task 2: `matched_hypothesis` + `build_simulation_block`

**Files:**
- Modify: `lib/ledger.py`
- Test: `tests/test_ledger.py` (add cases)

**Interfaces:**
- Consumes: `lib.pnl.compute_pnl`, an injectable `get_price` (defaults to `lib.marketdata.get_price`).
- Produces:
  - `matched_hypothesis(expected_pct: float, realized_pct: float) -> str` — `no` if `realized_pct <= 0`; `yes` if `realized_pct >= 0.5 * expected_pct`; else `partial`.
  - `build_simulation_block(plan: dict, now: str, provider: str = "stub", get_price=...) -> dict` — returns `{ran_at, fills, realized_profit_pct, outcome, matched_hypothesis}` where `fills` is a 2-item list (`entry`, `exit`) each `{leg, planned_price, actual_price, source, fetched_at}`.

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import matched_hypothesis, build_simulation_block


def test_matched_hypothesis_rule():
    assert matched_hypothesis(2.0, -1.0) == "no"
    assert matched_hypothesis(2.0, 1.5) == "yes"
    assert matched_hypothesis(2.0, 0.5) == "partial"


def test_build_simulation_block_uses_injected_prices():
    plan = _scheduled_fm("x", "2026-07-10T13:12:00Z")["plan"]

    def fake_price(ticker, ts, provider):
        price = 100.0 if "13:00" in ts else 90.0   # short 100->90 = +10%
        return {"price": price, "source": f"test:{ticker}", "fetched_at": ts}

    block = build_simulation_block(plan, "2026-07-11T00:00:00Z",
                                   get_price=fake_price)
    assert block["realized_profit_pct"] == 10.0
    assert block["outcome"] == "win"
    assert block["matched_hypothesis"] == "yes"      # 10 >= 0.5*2.0
    assert block["fills"][0]["leg"] == "entry"
    assert block["fills"][0]["actual_price"] == 100.0
    assert block["fills"][1]["actual_price"] == 90.0
    assert block["fills"][0]["source"] == "test:USO"
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_ledger.py -k "matched or build_simulation" -v`
Expected: FAIL — `ImportError: cannot import name 'matched_hypothesis'`.

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
from lib import pnl as _pnl
from lib import marketdata as _marketdata


def matched_hypothesis(expected_pct: float, realized_pct: float) -> str:
    if realized_pct <= 0:
        return "no"
    if realized_pct >= 0.5 * expected_pct:
        return "yes"
    return "partial"


def build_simulation_block(plan: dict, now: str, provider: str = "stub",
                           get_price=_marketdata.get_price) -> dict:
    ticker = plan["ticker"]
    entry = get_price(ticker, plan["entry"]["time"], provider)
    exit_ = get_price(ticker, plan["exit"]["time"], provider)
    pl = _pnl.compute_pnl(plan["action"], entry["price"], exit_["price"])
    fills = [
        {"leg": "entry", "planned_price": plan["entry"].get("target_price"),
         "actual_price": entry["price"], "source": entry["source"],
         "fetched_at": entry["fetched_at"]},
        {"leg": "exit", "planned_price": plan["exit"].get("target_price"),
         "actual_price": exit_["price"], "source": exit_["source"],
         "fetched_at": exit_["fetched_at"]},
    ]
    return {
        "ran_at": now, "fills": fills,
        "realized_profit_pct": pl["realized_profit_pct"],
        "outcome": pl["outcome"],
        "matched_hypothesis": matched_hypothesis(
            plan.get("expected_profit_pct", 0.0), pl["realized_profit_pct"]),
    }
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_ledger.py -v`
Expected: PASS (5 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add simulation block assembly with matched-hypothesis rule"
```

---

### Task 3: `simulate_dossier` (end-to-end write-back)

**Files:**
- Modify: `lib/ledger.py`
- Test: `tests/test_ledger.py` (add cases)

**Interfaces:**
- Consumes: `lib.dossier.load`, `lib.dossier.append_revision`, `build_simulation_block`, `lib.dossier.validate_frontmatter`.
- Produces: `simulate_dossier(path: str, now: str, provider: str = "stub", get_price=...) -> dict` — loads the dossier, builds the simulation block, appends a revision setting `status="simulated"` and the `simulation` block, and returns `{"id", "outcome", "realized_profit_pct", "matched_hypothesis"}`. The written dossier must pass `validate_frontmatter`.

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import simulate_dossier


def test_simulate_dossier_writes_valid_simulated(tmp_path):
    _seed(tmp_path, "x", _scheduled_fm("x", "2026-07-10T13:12:00Z"))
    path = str(tmp_path / "x" / "dossier.md")
    summary = simulate_dossier(path, "2026-07-11T00:00:00Z", provider="stub")
    assert summary["id"] == "x"
    assert summary["outcome"] in {"win", "loss", "neutral"}
    fm, body = dossier.load(path)
    assert fm["status"] == "simulated"
    assert fm["simulation"]["ran_at"] == "2026-07-11T00:00:00Z"
    assert dossier.validate_frontmatter(fm) == []     # conforms at new status
    assert "Simulated" in body                        # narrative revision appended
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_ledger.py -k simulate_dossier -v`
Expected: FAIL — `ImportError: cannot import name 'simulate_dossier'`.

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
def simulate_dossier(path: str, now: str, provider: str = "stub",
                     get_price=_marketdata.get_price) -> dict:
    fm, _ = _dossier.load(path)
    block = build_simulation_block(fm["plan"], now, provider, get_price)
    note = (f"Simulated {fm['plan']['ticker']} {fm['plan']['action']}: "
            f"{block['realized_profit_pct']}% "
            f"({block['outcome']}, matched={block['matched_hypothesis']})")
    _dossier.append_revision(path, {"status": "simulated", "simulation": block},
                             note, ts=now)
    return {"id": fm.get("id"), "outcome": block["outcome"],
            "realized_profit_pct": block["realized_profit_pct"],
            "matched_hypothesis": block["matched_hypothesis"]}
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_ledger.py -v`
Expected: PASS (6 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add simulate_dossier end-to-end write-back"
```

---

### Task 4: `regenerate_index`

**Files:**
- Modify: `lib/ledger.py`
- Test: `tests/test_ledger.py` (add cases)

**Interfaces:**
- Consumes: `lib.dossier.load`, `lib.index.render_index`.
- Produces: `regenerate_index(base: str = "opportunities", out_path: str = "INDEX.md") -> str` — scans every `<base>/<id>/dossier.md`, builds rows `{id, title, status, outcome}` (outcome from `simulation.outcome` or None), writes the rendered table to `out_path`, and returns the text.

- [ ] **Step 1: Write the failing test** — append to `tests/test_ledger.py`

```python
from lib.ledger import regenerate_index


def test_regenerate_index_writes_rows(tmp_path):
    _seed(tmp_path, "a", _scheduled_fm("a", "2026-07-10T13:12:00Z"))
    out = tmp_path / "INDEX.md"
    text = regenerate_index(base=str(tmp_path), out_path=str(out))
    assert "NOT FINANCIAL ADVICE" in text
    assert "| a |" in text
    assert out.read_text() == text
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_ledger.py -k regenerate_index -v`
Expected: FAIL — `ImportError: cannot import name 'regenerate_index'`.

- [ ] **Step 3: Implement** — append to `lib/ledger.py`

```python
from lib import index as _index


def regenerate_index(base: str = LEDGER_DIR, out_path: str = "INDEX.md") -> str:
    rows: list[dict] = []
    if os.path.isdir(base):
        for entry in sorted(os.listdir(base)):
            p = os.path.join(base, entry, "dossier.md")
            if not os.path.isfile(p):
                continue
            fm, _ = _dossier.load(p)
            rows.append({"id": fm.get("id", entry), "title": fm.get("title", ""),
                         "status": fm.get("status", ""),
                         "outcome": (fm.get("simulation") or {}).get("outcome")})
    text = _index.render_index(rows)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return text
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_ledger.py -v`
Expected: PASS (7 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/ledger.py tests/test_ledger.py
git commit -m "feat: add INDEX regeneration from the ledger"
```

---

### Task 5: `toa` CLI ledger subcommands

**Files:**
- Modify: `lib/cli.py`
- Test: `tests/test_cli.py` (add cases)

**Interfaces:**
- Consumes: `lib.ledger.find_simulatable`, `lib.ledger.simulate_dossier`, `lib.ledger.regenerate_index`, `lib.ledger.list_by_status`.
- Produces CLI subcommands (all print JSON to stdout):
  - `toa ls --status <s> [--base DIR]` → `{"ids": [...]}`
  - `toa simulatable --now <ISO> [--base DIR]` → `{"ids": [...]}`
  - `toa simulate <dossier_path> --now <ISO> [--provider stub|twelvedata]` → the `simulate_dossier` summary dict
  - `toa reindex [--base DIR] [--out PATH]` → `{"written": <out_path>}`

- [ ] **Step 1: Write the failing test** — append to `tests/test_cli.py`

```python
from lib import dossier, ledger  # noqa: F401  (ledger import ensures module present)


def _seed_scheduled(tmp_path, oid):
    fm = {
        "id": oid, "title": "t", "status": "scheduled",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"], "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
        "hypothesis": {"statement": "h", "direction": "short", "confidence": 65},
        "plan": {"ticker": "USO", "action": "short",
                 "entry": {"time": "2026-07-10T13:00:00Z", "target_price": 100.0},
                 "exit": {"time": "2026-07-10T13:12:00Z", "target_price": 90.0},
                 "expected_profit_pct": 2.0},
        "research": {"strategy": "three-round-panel", "models": {"bull": "sonnet"},
                     "last_updated": "2026-06-22T11:00:00Z"},
    }
    d = tmp_path / oid; d.mkdir(parents=True)
    path = str(d / "dossier.md")
    dossier.save(path, fm, "## Seed\n")
    return path


def test_cli_simulate_writes_outcome(tmp_path):
    path = _seed_scheduled(tmp_path, "x")
    r = _run("simulate", path, "--now", "2026-07-11T00:00:00Z")
    assert r.returncode == 0
    out = json.loads(r.stdout)
    assert out["id"] == "x"
    assert out["outcome"] in {"win", "loss", "neutral"}


def test_cli_simulatable_lists_due(tmp_path):
    _seed_scheduled(tmp_path, "x")
    r = _run("simulatable", "--now", "2026-07-11T00:00:00Z", "--base", str(tmp_path))
    assert json.loads(r.stdout)["ids"] == ["x"]
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_cli.py -k "simulate or simulatable" -v`
Expected: FAIL — argparse error / unknown command `simulate`.

- [ ] **Step 3: Implement** — edit `lib/cli.py`: add `from lib import ledger`, register the subparsers, and handle them. Insert the new parsers after the existing `validate` parser:

```python
    ls = sub.add_parser("ls")
    ls.add_argument("--status", required=True); ls.add_argument("--base", default="opportunities")

    si = sub.add_parser("simulatable")
    si.add_argument("--now", required=True); si.add_argument("--base", default="opportunities")

    sm = sub.add_parser("simulate")
    sm.add_argument("path"); sm.add_argument("--now", required=True)
    sm.add_argument("--provider", default="stub")

    ri = sub.add_parser("reindex")
    ri.add_argument("--base", default="opportunities"); ri.add_argument("--out", default="INDEX.md")
```

and add these branches before the final `return 2`:

```python
    if args.cmd == "ls":
        ids = [i["id"] for i in ledger.list_by_status(args.status, base=args.base)]
        print(json.dumps({"ids": ids}))
        return 0
    if args.cmd == "simulatable":
        ids = [i["id"] for i in ledger.find_simulatable(args.now, base=args.base)]
        print(json.dumps({"ids": ids}))
        return 0
    if args.cmd == "simulate":
        print(json.dumps(ledger.simulate_dossier(args.path, args.now, args.provider)))
        return 0
    if args.cmd == "reindex":
        ledger.regenerate_index(base=args.base, out_path=args.out)
        print(json.dumps({"written": args.out}))
        return 0
```

Add the import near the top:

```python
from lib import dossier, ledger, marketdata, pnl
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_cli.py -v`
Expected: PASS (all CLI tests, including the 2 new ones).

- [ ] **Step 5: Commit**

```bash
git add lib/cli.py tests/test_cli.py
git commit -m "feat: add ledger subcommands to toa CLI"
```

---

### Task 6: Author `market-data` and `simulate-plans` skills

**Files:**
- Create: `.claude/skills/market-data/SKILL.md`, `.claude/skills/simulate-plans/SKILL.md`
- Test: `tests/test_skills_present.py`

**Interfaces:**
- Consumes: the `toa` CLI subcommands from Tasks 1–5.
- Produces: two `SKILL.md` files, each with YAML frontmatter containing `name` and `description`. Conformance test asserts presence + frontmatter keys.

- [ ] **Step 1: Write the failing test** — `tests/test_skills_present.py`

```python
from pathlib import Path
import yaml

SKILLS = ["market-data", "simulate-plans"]


def _frontmatter(path):
    text = path.read_text()
    assert text.startswith("---"), f"{path} missing frontmatter"
    _, fm_block, _ = text.split("---", 2)
    return yaml.safe_load(fm_block)


def test_skill_files_exist_with_frontmatter():
    for name in SKILLS:
        p = Path(f".claude/skills/{name}/SKILL.md")
        assert p.is_file(), f"missing {p}"
        fm = _frontmatter(p)
        assert fm.get("name") == name
        assert fm.get("description")


def test_simulate_skill_references_toa():
    text = Path(".claude/skills/simulate-plans/SKILL.md").read_text()
    assert "toa simulatable" in text and "toa simulate" in text and "toa reindex" in text
```

- [ ] **Step 2: Run to verify failure**

Run: `python3 -m pytest tests/test_skills_present.py -v`
Expected: FAIL — files missing.

- [ ] **Step 3a: Create `.claude/skills/market-data/SKILL.md`**

```markdown
---
name: market-data
description: Fetch a citable historical price for a ticker at a UTC minute. Use whenever a skill needs a real price; never estimate prices yourself.
---

# market-data

Prices come from tested code, never from your own estimate. To get the price of a
ticker at a specific UTC minute, run:

```bash
toa price <TICKER> <ISO-8601-UTC> [--provider stub|twelvedata]
```

Example:

```bash
toa price USO 2026-07-10T13:00:00Z --provider twelvedata
# -> {"price": 78.62, "source": "https://api.twelvedata.com/...", "fetched_at": "...", "timestamp": "..."}
```

Use `--provider stub` for offline/dry runs (deterministic fake prices). Use
`--provider twelvedata` for real data (requires `TWELVEDATA_API_KEY` in the
environment). Always record the returned `source` when you cite a price.
```

- [ ] **Step 3b: Create `.claude/skills/simulate-plans/SKILL.md`**

```markdown
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
   `simulated`. Do NOT compute P/L or edit the block yourself.

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
```

- [ ] **Step 4: Run to verify pass**

Run: `python3 -m pytest tests/test_skills_present.py -v`
Expected: PASS (2 passed).

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/market-data/SKILL.md .claude/skills/simulate-plans/SKILL.md tests/test_skills_present.py
git commit -m "feat: add market-data and simulate-plans skills"
```

---

### Task 7: Manual end-to-end verification (seeded opportunity)

**Files:**
- Create (temporary, committed as a worked example): `opportunities/2026-06-22-oil-iran-talks/dossier.md`

**Interfaces:** none new — exercises the whole Plan 2 path via `toa`.

- [ ] **Step 1: Seed a scheduled opportunity** — create `opportunities/2026-06-22-oil-iran-talks/dossier.md`

```markdown
---
id: 2026-06-22-oil-iran-talks
title: "US–Iran talks resume → oil downside"
status: scheduled
created: 2026-06-22T09:00:00Z
event:
  type: geopolitical
  summary: "Resumption of US–Iran talks pressures crude."
  impact_window: 2026-07-10
tickers: [USO]
sources:
  - {title: "Example wire", url: "https://example.com/oil", accessed_at: "2026-06-22T09:00:00Z"}
hypothesis:
  statement: "Diplomatic thaw eases supply fears; USO dips intraday."
  direction: short
  confidence: 60
plan:
  ticker: USO
  action: short
  entry: {time: 2026-07-10T13:00:00Z, target_price: 78.50}
  exit: {time: 2026-07-10T13:12:00Z, target_price: 77.10}
  expected_profit_pct: 1.8
research:
  strategy: three-round-panel
  models: {bull: sonnet, bear: sonnet, quant: opus, synthesizer: opus}
  last_updated: 2026-06-22T11:00:00Z
---

## Seeded example
Hand-authored to exercise the simulator before the research stage exists.
```

- [ ] **Step 2: Confirm it is selected as due**

Run: `toa simulatable --now 2026-07-11T00:00:00Z`
Expected: `{"ids": ["2026-06-22-oil-iran-talks"]}`.

- [ ] **Step 3: Simulate it (stub provider — offline, deterministic)**

Run: `toa simulate opportunities/2026-06-22-oil-iran-talks/dossier.md --now 2026-07-11T00:00:00Z --provider stub`
Expected: JSON like `{"id": "2026-06-22-oil-iran-talks", "outcome": "win"|"loss"|"neutral", "realized_profit_pct": <number>, "matched_hypothesis": "yes"|"no"|"partial"}`.

- [ ] **Step 4: Verify the dossier is now valid `simulated`**

Run: `toa validate opportunities/2026-06-22-oil-iran-talks/dossier.md`
Expected: `{"valid": true, "errors": []}`.

- [ ] **Step 5: Regenerate and inspect the index**

Run: `toa reindex && cat INDEX.md`
Expected: a table row for `2026-06-22-oil-iran-talks` at status `simulated` with its outcome, under the disclaimer header.

- [ ] **Step 6: Run the full suite**

Run: `python3 -m pytest -q`
Expected: all green.

- [ ] **Step 7: Commit**

```bash
git add opportunities/2026-06-22-oil-iran-talks/ INDEX.md
git commit -m "feat: add worked example opportunity and generated index"
```

---

## Self-Review notes (author)

- **Spec coverage (Plan 2 scope):** simulate-plans §4③ — consume `scheduled` past-exit + no simulation (Task 1), fetch prices via market-data seam (Task 2), compute P/L + outcome + matched_hypothesis (Tasks 2–3), write `simulation` block + flip status + cite sources (Tasks 3, 6), INDEX dashboard §3 (Task 4), market-data skill §7a (Task 6). **Deferred to Plan 3 (by design):** scout-news, research-debate + personas + strategies, post-mortem + learning loop, config files. **Plan 4:** scheduling.
- **Determinism note:** `matched_hypothesis` is a deterministic baseline (realized vs expected). The spec frames it as partly judgemental; Plan 3's stages may overwrite it with reasoning. Recorded as a Global Constraint so it is not mistaken for the final word.
- **Placeholders:** none — every code/test/command step is complete and runnable.
- **Type consistency:** `get_price` return shape `{price, source, fetched_at, timestamp}` matches Plan 1; `simulate_dossier` summary keys (`id, outcome, realized_profit_pct, matched_hypothesis`) consistent across Tasks 3, 5, 6; `simulation` block keys match the dossier schema in `contracts/dossier-schema.md`.
