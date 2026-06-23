# Trading Opportunity Agent — Plan 1: Deterministic Core & Contracts

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the tested, deterministic foundation — the written contracts plus a small pure-function Python library — that every agent skill in later plans will rely on for arithmetic, parsing, validation, and file I/O.

**Architecture:** Pure Claude Code system (skills + file ledger + cron). This plan delivers ONLY the non-LLM, deterministic substrate: a `lib/` of pure functions and one `toa` CLI that wraps them, so that later agent-skills can shell out (e.g. `toa pnl ...`, `toa price ...`, `toa validate ...`) instead of doing math or JSON-parsing in a prompt. No skills, no scheduling, no LLM calls here — those are Plans 2 and 3.

**Tech Stack:** Python 3.11+ (stdlib only at runtime — `urllib` for HTTP, no `requests`), `PyYAML` for dossier frontmatter, `pytest` for tests. The live market-data provider is **Twelve Data** (free tier).

## Global Constraints

- **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.** This string (or a clear equivalent) must appear in `README.md` and is asserted by a test.
- **Conventional commits, no scope:** only `feat:` / `fix:` prefixes (CLAUDE.md rule). Every commit on the branch validated.
- **Branch:** all work on `feat/trading-opportunity-agent-foundation` (never commit to a default branch).
- **Secrets:** the Twelve Data key lives in env var `TWELVEDATA_API_KEY`, never committed; `.gitignore` must exclude `.env`.
- **Provider seam:** all price access goes through `lib/marketdata.get_price(...)`; no other module hardcodes a provider URL.
- **Granularity floor:** minute resolution; no sub-minute logic anywhere.
- **Timestamps:** all dossier/contract timestamps are ISO-8601 UTC (`...Z`). Twelve Data requests pass `timezone=UTC` so returned bar datetimes are UTC.
- **Dossier statuses (ordered):** `scouted → researched → scheduled → simulated → analyzed`.

---

## File Structure

```
trading-opportunity-agent/
  README.md                         ← purpose + disclaimer (Task 1)
  pyproject.toml                    ← project + pytest config (Task 1)
  .gitignore                        ← excludes .env, __pycache__ (Task 1)
  contracts/
    dossier-schema.md               ← written frontmatter contract (Task 2)
    market-data-contract.md         ← written price contract (Task 5)
  lib/
    __init__.py
    dossier.py                      ← validate / load / save / append_revision (Tasks 2,3)
    pnl.py                          ← realized P/L + outcome (Task 4)
    marketdata.py                   ← get_price: stub + Twelve Data (Tasks 5,6,7)
    dedup.py                        ← duplicate detection (Task 8)
    lessons.py                      ← relevance filter for learning loop (Task 9)
    index.py                        ← render INDEX.md (Task 10)
    cli.py                          ← `toa` argparse entrypoint (Task 11)
  tests/
    fixtures/twelvedata_nvda_1min.json   ← captured sample response (Task 6)
    test_dossier.py  test_pnl.py  test_marketdata.py
    test_dedup.py  test_lessons.py  test_index.py  test_cli.py
```

Each `lib/` module has one responsibility and is independently testable. The CLI is the only integration seam later skills touch.

---

### Task 1: Project scaffold

**Files:**
- Create: `README.md`, `pyproject.toml`, `.gitignore`, `lib/__init__.py`, `tests/__init__.py`
- Test: `tests/test_readme.py`

**Interfaces:**
- Consumes: nothing.
- Produces: a runnable `pytest`; package `lib` importable; the disclaimer string present in `README.md`.

- [ ] **Step 1: Create the branch**

```bash
cd /Users/oren/Oren/trading-oppurtonity-agent
git checkout -b feat/trading-opportunity-agent-foundation
```

- [ ] **Step 2: Write `pyproject.toml`**

```toml
[project]
name = "trading-opportunity-agent"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["PyYAML>=6.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0"]

[project.scripts]
toa = "lib.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 3: Write `.gitignore`**

```gitignore
.env
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
```

- [ ] **Step 4: Write `README.md`** (must contain the disclaimer verbatim)

```markdown
# Trading Opportunity Agent

A team of scheduled Claude agents that scouts event-driven market opportunities,
debates each through opposed personas, simulates the resulting plan against real
historical prices, and runs post-mortems that feed a learning loop.

> ⚠️ **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.**
> This system never places real orders. All trades are hypothetical and simulated
> for research and learning purposes only.

See `docs/superpowers/specs/2026-06-23-trading-opportunity-agent-design.md` for the design.
```

- [ ] **Step 5: Create empty packages**

```bash
mkdir -p lib tests contracts
touch lib/__init__.py tests/__init__.py
```

- [ ] **Step 6: Write the failing test** — `tests/test_readme.py`

```python
from pathlib import Path

def test_readme_has_disclaimer():
    text = Path("README.md").read_text()
    assert "PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE." in text
```

- [ ] **Step 7: Install dev deps and run the test**

Run: `pip install -e ".[dev]" && pytest tests/test_readme.py -v`
Expected: PASS (1 passed).

- [ ] **Step 8: Commit**

```bash
git add README.md pyproject.toml .gitignore lib/ tests/
git commit -m "feat: scaffold project with disclaimer and pytest"
```

---

### Task 2: Dossier contract + frontmatter validation

**Files:**
- Create: `contracts/dossier-schema.md`, `lib/dossier.py`
- Test: `tests/test_dossier.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `validate_frontmatter(fm: dict) -> list[str]` — returns a list of human-readable error strings (empty list == valid). Validation is **status-aware**: each status requires its own blocks plus all earlier ones.

- [ ] **Step 1: Write `contracts/dossier-schema.md`** — the written contract (the canonical field list copied from the spec §3, plus this rule):

```markdown
# Dossier frontmatter contract

A `dossier.md` begins with a YAML frontmatter block (between `---` fences) and a
free-form Markdown body. Frontmatter is the queryable machine state; the body is
append-only narrative.

## Required fields by status
- `scouted`: id, title, status, created, event{type,summary,impact_window}, tickers, sources
- `researched`: all of the above + hypothesis{statement,direction,confidence}, plan{ticker,action,entry{time,target_price},exit{time,target_price},expected_profit_pct}, research{strategy,models,last_updated}
- `scheduled`: same fields as researched (status flips once plan times are in the future)
- `simulated`: all research fields + simulation{ran_at,fills,realized_profit_pct,outcome,matched_hypothesis}
- `analyzed`: all simulated fields + postmortem{ran_at,root_cause,lessons}

## Enums
- status: scouted|researched|scheduled|simulated|analyzed
- event.type: geopolitical|economic|earnings|product|macro|regulatory|ipo
- hypothesis.direction: long|short
- plan.action: buy|sell|short
- simulation.outcome: win|loss|neutral
- simulation.matched_hypothesis: yes|no|partial
- postmortem.root_cause: wrong-assumption|missing-info|timing|data|priced-in

All timestamps are ISO-8601 UTC (suffix `Z`).
```

- [ ] **Step 2: Write the failing test** — `tests/test_dossier.py`

```python
from lib.dossier import validate_frontmatter

def _scouted():
    return {
        "id": "2026-06-22-oil", "title": "t", "status": "scouted",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"], "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
    }

def test_valid_scouted_has_no_errors():
    assert validate_frontmatter(_scouted()) == []

def test_missing_field_is_reported():
    fm = _scouted(); del fm["tickers"]
    errs = validate_frontmatter(fm)
    assert any("tickers" in e for e in errs)

def test_bad_status_enum_is_reported():
    fm = _scouted(); fm["status"] = "bogus"
    assert any("status" in e for e in validate_frontmatter(fm))

def test_researched_requires_plan():
    fm = _scouted(); fm["status"] = "researched"
    assert any("plan" in e for e in validate_frontmatter(fm))
```

- [ ] **Step 3: Run to verify failure**

Run: `pytest tests/test_dossier.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.dossier'`.

- [ ] **Step 4: Implement `lib/dossier.py`** (validation only)

```python
"""Dossier frontmatter validation and I/O."""

STATUSES = ["scouted", "researched", "scheduled", "simulated", "analyzed"]
EVENT_TYPES = {"geopolitical", "economic", "earnings", "product", "macro", "regulatory", "ipo"}

# Required top-level keys introduced at each status (cumulative).
_REQUIRED_AT = {
    "scouted": ["id", "title", "status", "created", "event", "tickers", "sources"],
    "researched": ["hypothesis", "plan", "research"],
    "scheduled": [],
    "simulated": ["simulation"],
    "analyzed": ["postmortem"],
}


def _required_keys(status: str) -> list[str]:
    keys: list[str] = []
    for s in STATUSES:
        keys += _REQUIRED_AT[s]
        if s == status:
            break
    return keys


def validate_frontmatter(fm: dict) -> list[str]:
    errors: list[str] = []
    status = fm.get("status")
    if status not in STATUSES:
        errors.append(f"status: must be one of {STATUSES}, got {status!r}")
        return errors  # can't check requirements without a valid status
    for key in _required_keys(status):
        if key not in fm or fm[key] in (None, "", [], {}):
            errors.append(f"{key}: required at status '{status}' but missing/empty")
    ev = fm.get("event")
    if isinstance(ev, dict) and ev.get("type") not in EVENT_TYPES:
        errors.append(f"event.type: must be one of {sorted(EVENT_TYPES)}")
    return errors
```

- [ ] **Step 5: Run to verify pass**

Run: `pytest tests/test_dossier.py -v`
Expected: PASS (4 passed).

- [ ] **Step 6: Commit**

```bash
git add contracts/dossier-schema.md lib/dossier.py tests/test_dossier.py
git commit -m "feat: add dossier contract and status-aware validation"
```

---

### Task 3: Dossier load / save / append-revision

**Files:**
- Modify: `lib/dossier.py`
- Test: `tests/test_dossier.py` (add cases)

**Interfaces:**
- Consumes: `validate_frontmatter`.
- Produces:
  - `load(path) -> tuple[dict, str]` — returns `(frontmatter_dict, body_str)`.
  - `save(path, fm: dict, body: str) -> None` — writes `---\n<yaml>---\n<body>`.
  - `append_revision(path, fm_updates: dict, note: str, ts: str) -> None` — merges `fm_updates` into frontmatter (mutable) and appends a timestamped block to the body (append-only). Must keep history intact.

- [ ] **Step 1: Write the failing test** — append to `tests/test_dossier.py`

```python
from lib.dossier import load, save, append_revision

def test_save_then_load_roundtrips(tmp_path):
    p = tmp_path / "dossier.md"
    fm = _scouted(); body = "## Scouted\nfound it\n"
    save(str(p), fm, body)
    fm2, body2 = load(str(p))
    assert fm2["id"] == fm["id"]
    assert "found it" in body2

def test_append_revision_keeps_history_and_updates_fm(tmp_path):
    p = tmp_path / "dossier.md"
    save(str(p), _scouted(), "## Scouted\nfirst\n")
    append_revision(str(p), {"status": "researched"}, "added hypothesis",
                    ts="2026-06-23T08:00:00Z")
    fm, body = load(str(p))
    assert fm["status"] == "researched"
    assert "first" in body                       # history preserved
    assert "2026-06-23T08:00:00Z" in body        # revision timestamp recorded
    assert "added hypothesis" in body
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_dossier.py -k "roundtrip or history" -v`
Expected: FAIL with `ImportError: cannot import name 'load'`.

- [ ] **Step 3: Implement** — append to `lib/dossier.py`

```python
import yaml

def load(path: str) -> tuple[dict, str]:
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing frontmatter fence")
    _, fm_block, body = text.split("---", 2)
    return yaml.safe_load(fm_block) or {}, body.lstrip("\n")


def save(path: str, fm: dict, body: str) -> None:
    fm_block = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{fm_block}---\n\n{body}")


def append_revision(path: str, fm_updates: dict, note: str, ts: str) -> None:
    fm, body = load(path)
    fm.update(fm_updates)
    body = body.rstrip() + f"\n\n---\n### Revision {ts}\n{note}\n"
    save(path, fm, body)
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_dossier.py -v`
Expected: PASS (6 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/dossier.py tests/test_dossier.py
git commit -m "feat: add dossier load/save/append-revision"
```

---

### Task 4: P/L computation

**Files:**
- Create: `lib/pnl.py`
- Test: `tests/test_pnl.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `compute_pnl(action: str, entry_price: float, exit_price: float, neutral_band_pct: float = 0.1) -> dict` returning `{"realized_profit_pct": float, "outcome": "win"|"loss"|"neutral"}`. `action` is `buy`/`sell`/`short`; `buy` is long, `sell`/`short` are short. Result rounded to 4 dp. `neutral` when `|pct| <= neutral_band_pct`.

- [ ] **Step 1: Write the failing test** — `tests/test_pnl.py`

```python
import pytest
from lib.pnl import compute_pnl

def test_long_gain_is_win():
    r = compute_pnl("buy", 100.0, 110.0)
    assert r["realized_profit_pct"] == 10.0
    assert r["outcome"] == "win"

def test_short_gain_when_price_falls():
    r = compute_pnl("short", 100.0, 90.0)
    assert r["realized_profit_pct"] == 10.0
    assert r["outcome"] == "win"

def test_long_loss():
    r = compute_pnl("buy", 100.0, 95.0)
    assert r["realized_profit_pct"] == -5.0
    assert r["outcome"] == "loss"

def test_tiny_move_is_neutral():
    assert compute_pnl("buy", 100.0, 100.05)["outcome"] == "neutral"

def test_invalid_action_raises():
    with pytest.raises(ValueError):
        compute_pnl("hold", 100.0, 110.0)
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_pnl.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.pnl'`.

- [ ] **Step 3: Implement `lib/pnl.py`**

```python
"""Deterministic realized P/L for a simulated round-trip."""

_LONG = {"buy"}
_SHORT = {"sell", "short"}


def compute_pnl(action: str, entry_price: float, exit_price: float,
                neutral_band_pct: float = 0.1) -> dict:
    if action in _LONG:
        pct = (exit_price - entry_price) / entry_price * 100.0
    elif action in _SHORT:
        pct = (entry_price - exit_price) / entry_price * 100.0
    else:
        raise ValueError(f"unknown action: {action!r}")
    pct = round(pct, 4)
    if abs(pct) <= neutral_band_pct:
        outcome = "neutral"
    else:
        outcome = "win" if pct > 0 else "loss"
    return {"realized_profit_pct": pct, "outcome": outcome}
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_pnl.py -v`
Expected: PASS (5 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/pnl.py tests/test_pnl.py
git commit -m "feat: add deterministic P/L computation"
```

---

### Task 5: Market-data contract + deterministic stub

**Files:**
- Create: `contracts/market-data-contract.md`, `lib/marketdata.py`
- Test: `tests/test_marketdata.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `get_price(ticker: str, timestamp: str, provider: str = "stub") -> dict` returning `{"price": float, "source": str, "fetched_at": str|None, "timestamp": str}`. The `stub` provider is **deterministic**: the same `(ticker, timestamp)` always yields the same price in a plausible range (10–500), with `source="stub:deterministic"`.

- [ ] **Step 1: Write `contracts/market-data-contract.md`**

```markdown
# Market-data contract

`get_price(ticker, timestamp, provider) -> {price, source, fetched_at, timestamp}`

- `ticker`: e.g. "NVDA". `timestamp`: ISO-8601 UTC of a minute (seconds ignored).
- Returns the price for that minute bar. `source` cites where the number came from
  (a stub label or a provider URL). `fetched_at` is when it was retrieved (UTC) or
  None for the stub.
- Providers: `stub` (deterministic, offline) and `twelvedata` (live, free tier).
- All providers honor the same return shape so the provider is a one-arg swap.
- Minute resolution only; seconds in `timestamp` are truncated.
```

- [ ] **Step 2: Write the failing test** — `tests/test_marketdata.py`

```python
from lib.marketdata import get_price

def test_stub_is_deterministic():
    a = get_price("NVDA", "2026-07-10T13:00:00Z")
    b = get_price("NVDA", "2026-07-10T13:00:00Z")
    assert a["price"] == b["price"]
    assert a["source"] == "stub:deterministic"

def test_stub_varies_by_minute():
    a = get_price("NVDA", "2026-07-10T13:00:00Z")
    b = get_price("NVDA", "2026-07-10T13:12:00Z")
    assert a["price"] != b["price"]

def test_stub_price_in_plausible_range():
    p = get_price("AAPL", "2026-07-10T14:30:00Z")["price"]
    assert 10.0 <= p <= 500.0
```

- [ ] **Step 3: Run to verify failure**

Run: `pytest tests/test_marketdata.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.marketdata'`.

- [ ] **Step 4: Implement `lib/marketdata.py`** (stub + dispatcher only)

```python
"""Price access behind a single provider-swappable contract."""
import hashlib


def _truncate_to_minute(timestamp: str) -> str:
    # "2026-07-10T13:00:45Z" -> "2026-07-10T13:00Z"
    base = timestamp.replace("Z", "")
    return base[:16] + "Z"


def _stub_price(ticker: str, minute: str) -> float:
    h = hashlib.sha256(f"{ticker}|{minute}".encode()).hexdigest()
    return round(10.0 + (int(h[:8], 16) % 49000) / 100.0, 2)  # 10.00–500.00


def get_price(ticker: str, timestamp: str, provider: str = "stub") -> dict:
    minute = _truncate_to_minute(timestamp)
    if provider == "stub":
        return {"price": _stub_price(ticker, minute),
                "source": "stub:deterministic", "fetched_at": None,
                "timestamp": minute}
    raise ValueError(f"unknown provider: {provider!r}")
```

- [ ] **Step 5: Run to verify pass**

Run: `pytest tests/test_marketdata.py -v`
Expected: PASS (3 passed).

- [ ] **Step 6: Commit**

```bash
git add contracts/market-data-contract.md lib/marketdata.py tests/test_marketdata.py
git commit -m "feat: add market-data contract and deterministic stub"
```

---

### Task 6: Twelve Data response parser

**Files:**
- Create: `tests/fixtures/twelvedata_nvda_1min.json`
- Modify: `lib/marketdata.py`
- Test: `tests/test_marketdata.py` (add cases)

**Interfaces:**
- Consumes: `_truncate_to_minute`.
- Produces: `parse_twelvedata(payload: dict, timestamp: str) -> float` — given a Twelve Data `time_series` JSON payload (UTC datetimes, `"YYYY-MM-DD HH:MM:SS"`) and a target ISO-UTC timestamp, returns the **open** of the matching minute bar. Raises `KeyError` if that minute is absent; raises `ValueError` if `payload["status"] != "ok"`.

- [ ] **Step 1: Create the fixture** — `tests/fixtures/twelvedata_nvda_1min.json`

```json
{
  "meta": {"symbol": "NVDA", "interval": "1min", "exchange_timezone": "UTC"},
  "values": [
    {"datetime": "2026-07-10 13:12:00", "open": "120.50", "high": "120.80", "low": "120.40", "close": "120.75"},
    {"datetime": "2026-07-10 13:00:00", "open": "118.20", "high": "118.60", "low": "118.10", "close": "118.55"}
  ],
  "status": "ok"
}
```

- [ ] **Step 2: Write the failing test** — append to `tests/test_marketdata.py`

```python
import json
from pathlib import Path
import pytest
from lib.marketdata import parse_twelvedata

def _payload():
    return json.loads(Path("tests/fixtures/twelvedata_nvda_1min.json").read_text())

def test_parse_returns_open_of_matching_minute():
    assert parse_twelvedata(_payload(), "2026-07-10T13:00:00Z") == 118.20

def test_parse_ignores_seconds():
    assert parse_twelvedata(_payload(), "2026-07-10T13:12:45Z") == 120.50

def test_parse_missing_minute_raises():
    with pytest.raises(KeyError):
        parse_twelvedata(_payload(), "2026-07-10T15:00:00Z")

def test_parse_error_status_raises():
    with pytest.raises(ValueError):
        parse_twelvedata({"status": "error", "message": "bad key"}, "2026-07-10T13:00:00Z")
```

- [ ] **Step 3: Run to verify failure**

Run: `pytest tests/test_marketdata.py -k parse -v`
Expected: FAIL with `ImportError: cannot import name 'parse_twelvedata'`.

- [ ] **Step 4: Implement** — append to `lib/marketdata.py`

```python
def parse_twelvedata(payload: dict, timestamp: str) -> float:
    if payload.get("status") != "ok":
        raise ValueError(f"twelvedata error: {payload.get('message', payload.get('status'))}")
    minute = _truncate_to_minute(timestamp)          # "2026-07-10T13:00Z"
    want = minute[:-1].replace("T", " ") + ":00"     # "2026-07-10 13:00:00"
    for bar in payload.get("values", []):
        if bar["datetime"] == want:
            return float(bar["open"])
    raise KeyError(f"no 1min bar for {want}")
```

- [ ] **Step 5: Run to verify pass**

Run: `pytest tests/test_marketdata.py -v`
Expected: PASS (7 passed).

- [ ] **Step 6: Commit**

```bash
git add tests/fixtures/twelvedata_nvda_1min.json lib/marketdata.py tests/test_marketdata.py
git commit -m "feat: parse Twelve Data 1min response to a minute price"
```

---

### Task 7: Live Twelve Data provider (fetch + cache + throttle)

**Files:**
- Modify: `lib/marketdata.py`
- Test: `tests/test_marketdata.py` (add cases)

**Interfaces:**
- Consumes: `parse_twelvedata`, `get_price` dispatcher.
- Produces:
  - `_fetch_twelvedata(ticker, date, api_key) -> dict` — HTTP GET via `urllib`, returns parsed JSON. (Network — exercised only via monkeypatch in tests.)
  - `get_price(..., provider="twelvedata")` wired to fetch (cached per `(ticker,date)` in module-level dict) then `parse_twelvedata`; `source` set to the request URL; reads key from `TWELVEDATA_API_KEY`; raises `RuntimeError` if key missing.

- [ ] **Step 1: Write the failing test** — append to `tests/test_marketdata.py`

```python
import lib.marketdata as md

def test_twelvedata_provider_uses_fetch_and_parse(monkeypatch):
    calls = {"n": 0}
    def fake_fetch(ticker, date, api_key):
        calls["n"] += 1
        return _payload()
    monkeypatch.setattr(md, "_fetch_twelvedata", fake_fetch)
    monkeypatch.setenv("TWELVEDATA_API_KEY", "test-key")
    md._CACHE.clear()
    r1 = md.get_price("NVDA", "2026-07-10T13:00:00Z", provider="twelvedata")
    r2 = md.get_price("NVDA", "2026-07-10T13:12:00Z", provider="twelvedata")
    assert r1["price"] == 118.20 and r2["price"] == 120.50
    assert calls["n"] == 1                       # same (ticker,date) cached
    assert "twelvedata.com" in r1["source"]

def test_twelvedata_missing_key_raises(monkeypatch):
    monkeypatch.delenv("TWELVEDATA_API_KEY", raising=False)
    md._CACHE.clear()
    import pytest
    with pytest.raises(RuntimeError):
        md.get_price("NVDA", "2026-07-10T13:00:00Z", provider="twelvedata")
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_marketdata.py -k twelvedata_provider -v`
Expected: FAIL (`_CACHE` / provider branch absent).

- [ ] **Step 3: Implement** — edit the top and `get_price` of `lib/marketdata.py`

```python
import json
import os
import time
import urllib.parse
import urllib.request

_CACHE: dict[tuple[str, str], dict] = {}
_BASE = "https://api.twelvedata.com/time_series"


def _fetch_twelvedata(ticker: str, date: str, api_key: str) -> dict:
    params = urllib.parse.urlencode({
        "symbol": ticker, "interval": "1min", "date": date,
        "timezone": "UTC", "outputsize": 5000, "apikey": api_key,
    })
    time.sleep(8)  # throttle: free tier is 8 req/min
    with urllib.request.urlopen(f"{_BASE}?{params}", timeout=30) as resp:
        return json.loads(resp.read().decode())
```

Then replace `get_price` with:

```python
def get_price(ticker: str, timestamp: str, provider: str = "stub") -> dict:
    minute = _truncate_to_minute(timestamp)
    if provider == "stub":
        return {"price": _stub_price(ticker, minute),
                "source": "stub:deterministic", "fetched_at": None, "timestamp": minute}
    if provider == "twelvedata":
        key = os.environ.get("TWELVEDATA_API_KEY")
        if not key:
            raise RuntimeError("TWELVEDATA_API_KEY not set")
        date = minute[:10]
        cache_key = (ticker, date)
        if cache_key not in _CACHE:
            _CACHE[cache_key] = _fetch_twelvedata(ticker, date, key)
        price = parse_twelvedata(_CACHE[cache_key], timestamp)
        url = f"{_BASE}?symbol={ticker}&interval=1min&date={date}&timezone=UTC"
        return {"price": price, "source": url,
                "fetched_at": minute, "timestamp": minute}
    raise ValueError(f"unknown provider: {provider!r}")
```

- [ ] **Step 4: Run to verify pass** (no network — fetch is monkeypatched)

Run: `pytest tests/test_marketdata.py -v`
Expected: PASS (9 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/marketdata.py tests/test_marketdata.py
git commit -m "feat: add live Twelve Data provider with cache and throttle"
```

---

### Task 8: Duplicate detection (scout dedup)

**Files:**
- Create: `lib/dedup.py`
- Test: `tests/test_dedup.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `is_duplicate(candidate: dict, existing: list[dict], window_days: int = 14, today: str) -> bool`. `candidate`/`existing` items have `tickers: list[str]` and `last_seen: str` (ISO-UTC date). A candidate is a duplicate iff some existing entry shares ≥1 ticker AND `last_seen` is within `window_days` of `today`.

- [ ] **Step 1: Write the failing test** — `tests/test_dedup.py`

```python
from lib.dedup import is_duplicate

EXISTING = [{"tickers": ["USO", "BNO"], "last_seen": "2026-06-20"}]

def test_recent_shared_ticker_is_duplicate():
    cand = {"tickers": ["USO"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-06-23") is True

def test_old_entry_not_duplicate():
    cand = {"tickers": ["USO"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-07-30") is False

def test_no_ticker_overlap_not_duplicate():
    cand = {"tickers": ["NVDA"]}
    assert is_duplicate(cand, EXISTING, window_days=14, today="2026-06-23") is False
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_dedup.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.dedup'`.

- [ ] **Step 3: Implement `lib/dedup.py`**

```python
"""Scout duplicate detection within a rolling window."""
from datetime import date


def _d(s: str) -> date:
    return date.fromisoformat(s)


def is_duplicate(candidate: dict, existing: list[dict], today: str,
                 window_days: int = 14) -> bool:
    cand_tickers = set(candidate.get("tickers", []))
    cutoff_days = window_days
    for e in existing:
        if cand_tickers & set(e.get("tickers", [])):
            age = (_d(today) - _d(e["last_seen"])).days
            if 0 <= age <= cutoff_days:
                return True
    return False
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_dedup.py -v`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/dedup.py tests/test_dedup.py
git commit -m "feat: add scout duplicate detection within rolling window"
```

---

### Task 9: Lessons relevance filter (learning loop)

**Files:**
- Create: `lib/lessons.py`
- Test: `tests/test_lessons.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `filter_relevant(lessons: list[dict], event_type: str, tickers: list[str]) -> list[dict]`. A lesson has `event_type: str`, `tickers: list[str]`, `text: str`. A lesson is relevant if its `event_type` matches OR it shares ≥1 ticker. Results de-duplicated by `text`, preserving input order.

- [ ] **Step 1: Write the failing test** — `tests/test_lessons.py`

```python
from lib.lessons import filter_relevant

LESSONS = [
    {"event_type": "geopolitical", "tickers": ["USO"], "text": "oil prices in fast"},
    {"event_type": "earnings", "tickers": ["NVDA"], "text": "earnings already priced"},
    {"event_type": "geopolitical", "tickers": ["XOM"], "text": "oil prices in fast"},  # dup text
]

def test_matches_by_event_type():
    out = filter_relevant(LESSONS, "geopolitical", ["TSLA"])
    assert [l["text"] for l in out] == ["oil prices in fast"]   # deduped

def test_matches_by_ticker():
    out = filter_relevant(LESSONS, "macro", ["NVDA"])
    assert out[0]["text"] == "earnings already priced"

def test_no_match_returns_empty():
    assert filter_relevant(LESSONS, "macro", ["TSLA"]) == []
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_lessons.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.lessons'`.

- [ ] **Step 3: Implement `lib/lessons.py`**

```python
"""Select post-mortem lessons relevant to an opportunity (learning loop)."""


def filter_relevant(lessons: list[dict], event_type: str, tickers: list[str]) -> list[dict]:
    want = set(tickers)
    out, seen = [], set()
    for l in lessons:
        hit = l.get("event_type") == event_type or (set(l.get("tickers", [])) & want)
        if hit and l["text"] not in seen:
            out.append(l)
            seen.add(l["text"])
    return out
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_lessons.py -v`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/lessons.py tests/test_lessons.py
git commit -m "feat: add lessons relevance filter for learning loop"
```

---

### Task 10: INDEX.md renderer

**Files:**
- Create: `lib/index.py`
- Test: `tests/test_index.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `render_index(rows: list[dict]) -> str` — given dossier summaries (`id, title, status, outcome` where `outcome` may be `None`), returns a Markdown document with the disclaimer header and one table row per opportunity, sorted by `id`. Missing `outcome` renders as `—`.

- [ ] **Step 1: Write the failing test** — `tests/test_index.py`

```python
from lib.index import render_index

ROWS = [
    {"id": "2026-06-22-oil", "title": "Oil down", "status": "simulated", "outcome": "win"},
    {"id": "2026-06-21-nvda", "title": "NVDA up", "status": "scouted", "outcome": None},
]

def test_index_has_disclaimer_and_sorted_rows():
    out = render_index(ROWS)
    assert "NOT FINANCIAL ADVICE" in out
    assert out.index("2026-06-21-nvda") < out.index("2026-06-22-oil")  # sorted by id

def test_index_renders_missing_outcome_as_dash():
    out = render_index(ROWS)
    assert "| — |" in out or "| —" in out
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_index.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'lib.index'`.

- [ ] **Step 3: Implement `lib/index.py`**

```python
"""Render the INDEX.md dashboard from dossier summaries."""

_HEADER = (
    "# Opportunity Index\n\n"
    "> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.\n\n"
    "| ID | Title | Status | Outcome |\n"
    "|----|-------|--------|---------|\n"
)


def render_index(rows: list[dict]) -> str:
    body = ""
    for r in sorted(rows, key=lambda r: r["id"]):
        outcome = r.get("outcome") or "—"
        body += f"| {r['id']} | {r['title']} | {r['status']} | {outcome} |\n"
    return _HEADER + body
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_index.py -v`
Expected: PASS (2 passed).

- [ ] **Step 5: Commit**

```bash
git add lib/index.py tests/test_index.py
git commit -m "feat: add INDEX.md renderer"
```

---

### Task 11: `toa` CLI (the skill-facing seam)

**Files:**
- Create: `lib/cli.py`
- Test: `tests/test_cli.py`

**Interfaces:**
- Consumes: `marketdata.get_price`, `pnl.compute_pnl`, `dossier.validate_frontmatter`, `dossier.load`.
- Produces: a `main(argv=None)` argparse entrypoint with subcommands that print JSON to stdout:
  - `toa price <ticker> <timestamp> [--provider stub|twelvedata]`
  - `toa pnl <action> <entry_price> <exit_price>`
  - `toa validate <dossier_path>` (exit code 1 + JSON errors if invalid)

- [ ] **Step 1: Write the failing test** — `tests/test_cli.py`

```python
import json, subprocess, sys

def _run(*args):
    return subprocess.run([sys.executable, "-m", "lib.cli", *args],
                          capture_output=True, text=True)

def test_cli_price_stub():
    r = _run("price", "NVDA", "2026-07-10T13:00:00Z")
    assert r.returncode == 0
    assert json.loads(r.stdout)["source"] == "stub:deterministic"

def test_cli_pnl():
    r = _run("pnl", "buy", "100", "110")
    assert json.loads(r.stdout)["outcome"] == "win"
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_cli.py -v`
Expected: FAIL (`No module named lib.cli`).

- [ ] **Step 3: Implement `lib/cli.py`**

```python
"""`toa` CLI — the deterministic seam that agent skills shell out to."""
import argparse
import json
import sys

from lib import dossier, marketdata, pnl


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="toa")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("price")
    sp.add_argument("ticker"); sp.add_argument("timestamp")
    sp.add_argument("--provider", default="stub")

    pl = sub.add_parser("pnl")
    pl.add_argument("action"); pl.add_argument("entry", type=float)
    pl.add_argument("exit", type=float)

    va = sub.add_parser("validate")
    va.add_argument("path")

    args = p.parse_args(argv)
    if args.cmd == "price":
        print(json.dumps(marketdata.get_price(args.ticker, args.timestamp, args.provider)))
        return 0
    if args.cmd == "pnl":
        print(json.dumps(pnl.compute_pnl(args.action, args.entry, args.exit)))
        return 0
    if args.cmd == "validate":
        fm, _ = dossier.load(args.path)
        errs = dossier.validate_frontmatter(fm)
        print(json.dumps({"valid": not errs, "errors": errs}))
        return 1 if errs else 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_cli.py -v && pytest -q`
Expected: `test_cli.py` PASS (2 passed); full suite all green.

- [ ] **Step 5: Commit**

```bash
git add lib/cli.py tests/test_cli.py
git commit -m "feat: add toa CLI wrapping deterministic helpers"
```

---

## Self-Review notes (author)

- **Spec coverage (Plan 1 scope):** dossier schema §3 → Tasks 2–3; P/L + outcome §4③ → Task 4; market-data contract + stub-first + live Twelve Data + throttle/cache §7a → Tasks 5–7; dedup window 14d §4① → Task 8; learning-loop relevance §4 → Task 9; INDEX.md §3 → Task 10; disclaimer global constraint → Tasks 1 & 10. **Deferred to later plans (by design):** the four agent skills, personas, debate/post-mortem strategies, config files, and cron schedules (Plans 2–3).
- **Placeholders:** none — every code/test step is complete and runnable.
- **Type consistency:** `get_price` shape `{price,source,fetched_at,timestamp}` consistent across Tasks 5/7 and CLI; `compute_pnl` keys consistent across Task 4 and CLI; `is_duplicate(candidate, existing, today, window_days)` signature consistent.
