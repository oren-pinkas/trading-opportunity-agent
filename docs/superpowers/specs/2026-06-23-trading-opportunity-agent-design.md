# Trading Opportunity Agent — Design Spec

**Date:** 2026-06-23
**Status:** Approved (design); pending implementation plan
**Author:** Oren + Claude

> ⚠️ **PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.** This system
> generates and *simulates* hypothetical trades for research and learning. It
> never places real orders. Every generated artifact must carry this disclaimer.

---

## 1. Purpose

A team of scheduled Claude agents that continuously scouts the market for
event-driven opportunities (geopolitical, macro/rates, earnings, product/feature
launches, IPOs, etc.), researches each one through a structured multi-persona
**debate**, produces a falsifiable **hypothesis + action plan**, **simulates** the
plan against real historical price data, and runs a **post-mortem** on failures so
the system *learns over time*.

The whole system is **pure Claude Code**: agents are skills + subagents, scheduling
is Claude Code cloud `/schedule` (cron), and all state is human-readable files in
this repo. There is no server and no database — **the ledger is the state and the
queue; `git` is the audit trail.**

## 2. Core architecture

One pipeline with a shared **ledger**. Each opportunity flows through four stages,
each stage transforming the same record:

```
scout-news ──creates──▶ research-debate ──enriches──▶ simulate-plans ──appends──▶ post-mortem ──appends──▶ LESSONS.md
   (status: scouted)        (researched/scheduled)        (simulated)              (analyzed)        │
        ▲                                                                                            │
        └──────────────────────────  learning loop: lessons re-injected into research  ◀────────────┘
```

**Status is the work queue.** Each stage globs the ledger for dossiers in the
status it consumes and emits the next status. No message bus, no locks. Status is
monotonic, so a late or skipped run self-heals — the next run picks up whatever sits
in the right status.

### Three orthogonal axes of pluggability (the modularity requirement)

The "discussion method" must be modular — strategy-pattern, but with skills. Three
independent, hot-swappable slots:

1. **Personas — the *who*.** Pure character specs (expertise, worldview, biases,
   what they look for). A persona file **never names a model** and **never encodes
   the debate protocol**. Model-agnostic, protocol-agnostic.
2. **Strategy — the *how*.** The debate/post-mortem protocol lives behind a fixed
   **contract** as an interchangeable skill (default debate: `three-round-panel`;
   default post-mortem: `investigator-critic`). The orchestrator calls the contract,
   not a specific strategy.
3. **Model assignment — the *with what*.** Which model each persona/role runs on is
   **injected as live context at spawn time** from a run-config, never baked into the
   persona. The same "Bear" can run on Haiku in a cheap pass or Opus in a deep pass.

The discipline that makes this hold: **contracts** (see `contracts/`). As long as a
strategy consumes the agreed inputs and emits the agreed artifact shape, strategies,
personas, and model maps are all swappable without touching the rest of the pipeline.

## 3. The ledger (backbone)

One folder per opportunity:

```
opportunities/<id>/
  dossier.md       ← YAML frontmatter (queryable machine state) + narrative body
  transcript.md    ← full debate log: every persona position, rebuttal, citations
  simulation.md    ← simulator's fill-by-fill log with cited prices
  postmortem.md    ← post-mortem analysis (only if it gets one)
```

**Rules:**
- **Frontmatter = machine state; body = human narrative.** Stages read frontmatter
  to decide *what to do*; they append to the body to record *what they did*.
- **Frontmatter is mutable; the body is append-only.** Re-runs append a new
  timestamped revision block and bump `last_updated` — they never overwrite history,
  so the post-mortem can see what the team believed and when.
- One folder per opportunity = natural isolation; the four logs never collide.

### `dossier.md` frontmatter schema

```yaml
id: 2026-06-22-oil-iran-talks
title: "US–Iran talks resume → oil downside"
status: scouted        # scouted → researched → scheduled → simulated → analyzed
created: 2026-06-22T09:00:00Z

event:
  type: geopolitical   # geopolitical|economic|earnings|product|macro|regulatory|ipo
  summary: "..."
  impact_window: 2026-07-10              # when the market reaction is expected
tickers: [BNO, XOM, USO]
sources: [{title, url, accessed_at}]      # filled by scout

hypothesis:                               # filled by research team
  statement: "..."
  direction: short                        # long|short
  confidence: 65                          # 0–100
plan:
  ticker: USO
  action: short                           # buy|sell|short
  entry: {time: 2026-07-10T13:00:00Z, target_price: 78.50}
  exit:  {time: 2026-07-10T13:12:00Z, target_price: 77.10}
  expected_profit_pct: 1.8
research:
  strategy: three-round-panel             # which debate strategy produced this
  models: {bull: sonnet, bear: sonnet, quant: opus, synthesizer: opus}
  dissent: "Quant flagged thin liquidity..."   # unresolved disagreement
  last_updated: 2026-06-22T11:00:00Z

simulation:                               # filled by simulator
  ran_at: 2026-07-11T06:00:00Z
  fills:
    - {leg: entry, planned_price: 78.50, actual_price: 78.62, source: "...", fetched_at: ...}
    - {leg: exit,  planned_price: 77.10, actual_price: 77.95, source: "...", fetched_at: ...}
  realized_profit_pct: 0.85
  outcome: win                            # win|loss|neutral
  matched_hypothesis: partial             # yes|no|partial

postmortem:                               # filled by post-mortem (losers + flukes only)
  ran_at: ...
  root_cause: timing                      # wrong-assumption|missing-info|timing|data|priced-in
  lessons: ["..."]
```

Plus two repo-root artifacts:
- **`INDEX.md`** — generated dashboard of every opportunity + status + outcome.
- **`LESSONS.md`** — accumulated, tagged post-mortem lessons (the learning loop).

## 4. The four stages

Every stage follows the same shape: *wake → query ledger frontmatter for work →
spawn subagents → write results back → update status.*

### ① `scout-news` — Haiku, 3×/day
Searches news (WebSearch/WebFetch) for **forward-looking, market-moving** events.
Scout breadth is **open-ended** for v1 (no fixed beats; `scout.json` `source_hints[]`
left empty). For each: extracts event, expected impact window, candidate tickers;
**dedupes** against open opportunities in `INDEX.md` (dedupe window: **14 days** — a
scouted event is not re-created within 14 days of its last sighting). Writes new
`opportunities/<id>/dossier.md`
at status `scouted` with cited sources. Cheap model on purpose — filtering, not
judgement.

### ② `research-debate` — 1×/day
The heart. Consumes `scouted` (fresh) **and** `researched` (revise on new info).
For each opportunity:
1. Reads `config/research.json` → picks the **debate strategy skill**, the
   **persona set**, and the **model map**.
2. Injects relevant `LESSONS.md` entries (filtered by event-type + ticker) as live
   context — institutional memory, not persona edits.
3. Runs the strategy. Default `three-round-panel`:
   - **R1 Independent research (parallel):** each persona researches alone and writes
     an opening position (read, evidence, proposed action). No cross-visibility.
   - **R2 Rebuttal (parallel):** each persona sees the *other two* positions and
     rebuts — disagreements, gaps, what would change their mind.
   - **R3 Convergence:** a **neutral synthesizer** writes the final artifact:
     hypothesis, plan (action, entry time+price, exit time+price, expected_profit_pct),
     confidence, and a **dissent note** (unresolved disagreement — gold for the
     post-mortem).
4. Writes hypothesis/plan/research blocks to the dossier + full `transcript.md` with
   citations. On revisits, only re-runs if new sources appeared since `last_updated`;
   appends a timestamped revision. Status → `researched`, or `scheduled` once the
   plan has future action times.

### ③ `simulate-plans` — light model, 1×/day
Consumes `scheduled` where `plan.exit.time` is in the past and no `simulation` block
exists. Calls the **`market-data` skill** (stubbed for now) for the price at each
planned timestamp; computes fills, realized P/L, `outcome`, `matched_hypothesis`.
Writes the `simulation` block + cited `simulation.md`. Status → `simulated`. Mostly
deterministic.

### ④ `post-mortem` — Sonnet/Opus, 1×/day
Consumes `simulated`, not yet `analyzed`, where `outcome: loss` **or** a *fluke*
(`win` but `matched_hypothesis: no`). Clean wins get a one-line note, no full
post-mortem. Modular **team behind a strategy slot** (same pattern as the debate);
default `investigator-critic`:
- **Investigator** — reconstructs what actually happened from the price path +
  simulation log.
- **Critic** — compares against the debate transcript and assigns a `root_cause`,
  asking *was the error knowable at research time?*
- **Synthesizer** — writes structured, tagged `lessons[]`.

Status → `analyzed`. Lessons appended to `LESSONS.md`.

### The learning loop
Post-mortem appends tagged lessons to `LESSONS.md`. The research orchestrator injects
the *relevant* lessons (by event-type + ticker) into each persona's context at spawn
time. Persona *character* stays fixed; its *briefing* gains hard-won memory. This
closes the cycle: predict → act → measure → diagnose → adjust priors → predict better.

## 5. Scheduling

Four thin cloud-scheduled triggers (Claude Code `/schedule`/cron); each only invokes
its skill, so schedules never change when logic changes. **Pinned to the
`America/New_York` timezone** so they track the US session through DST automatically
(open 09:30, close 16:00 ET). UTC shown for the current EDT season.

| Stage | Cadence | Time (ET) | UTC (EDT) | Rationale |
|---|---|---|---|---|
| `scout-news` | 3×/day | 07:00 | 11:00 | Pre-market — overnight + futures news |
| | | 12:30 | 16:30 | Midday — intraday developments |
| | | 17:00 | 21:00 | Post-close — after-the-bell earnings & wrap |
| `research-debate` | 1×/day | 08:00 | 12:00 | After dawn scout, before open — time to build plans |
| `simulate-plans` | 1×/day | 18:30 | 22:30 | 2.5h after close — minute bars settled |
| `post-mortem` | 1×/day | 19:30 | 23:30 | After simulator writes the night's results |

Intra-day flow: 07:00 scout → 08:00 research/plan → [market 09:30–16:00, plans
execute] → 12:30 & 17:00 scouts → 18:30 simulate → 19:30 post-mortem. Happens-before
ordering is preserved by the time gaps; missed runs self-heal via status-queue.

## 6. Repo layout

```
trading-opportunity-agent/
  README.md           ← purpose + bold PAPER-TRADING / NOT-ADVICE disclaimer
  INDEX.md            ← generated dashboard: every opportunity + status + outcome
  LESSONS.md          ← accumulated, tagged post-mortem lessons (learning loop)

  .claude/skills/                       ← executable agents (Claude Code discovers these)
    scout-news/                         ← stage ①
    research-debate/                    ← stage ② orchestrator (reads config, runs a strategy)
    simulate-plans/                     ← stage ③
    post-mortem/                        ← stage ④ orchestrator
    market-data/                        ← STUBBED price provider (one fixed contract)
    debate-three-round-panel/           ← a debate strategy  (swappable)
    pm-investigator-critic/             ← a post-mortem strategy (swappable)

  config/                               ← live context, edited freely, no code changes
    research.json     ← { strategy, personas[], models{bull,bear,quant,synthesizer} }
    postmortem.json   ← { strategy, roles[], models{investigator,critic,synth} }
    scout.json        ← { model, source_hints[], dedupe_window_days }

  personas/                             ← CHARACTER ONLY — never names a model
    bull.md  bear.md  quant.md  investigator.md  critic.md

  contracts/                            ← the interfaces everything agrees on (the "headers")
    dossier-schema.md   debate-contract.md   postmortem-contract.md   market-data-contract.md

  opportunities/<id>/
    dossier.md  transcript.md  simulation.md  postmortem.md
```

The **`contracts/` folder is the load-bearing wall** — the written-down interfaces
(dossier frontmatter shape, what a strategy accepts/returns, what `market-data`
promises). Every skill reads its relevant contract at the top of its prompt, so
swapping a strategy or wiring the real data provider can't silently break a neighbor.

## 7. The three personas (default debate)

- **Bull / Catalyst-hunter** — momentum/narrative-driven; why this event *moves* the
  stock and how to ride it.
- **Bear / Skeptic** — risk/disconfirmation-driven; why the thesis is wrong, what's
  priced in, what blows it up.
- **Quant / Pragmatist** — data/probability-driven; base rates, historical analogues,
  expected value after costs, position sizing.

## 7a. Market data provider — Twelve Data (free tier)

`market-data` calls **Twelve Data** (`api.twelvedata.com/time_series`,
`interval=1min`) on its **free tier**: 800 requests/day, 8 requests/min, US equities
intraday included, **$0, no credit card**. Our access pattern is batch-and-historical
(daily simulator run, ~2 reads per plan leg), which fits free quotas with wide margin
— a few hundred simulated plans/day before paid tiers ($29+/mo) would ever apply.

- The `market-data` skill still hides the provider behind the fixed contract
  `(ticker, timestamp) → {price, source, fetched_at}`, so the provider remains a
  one-file swap. **Build order:** a deterministic **stub** implements the contract
  first so the whole pipeline can be validated end-to-end; the live Twelve Data call
  drops in behind the same contract.
- The skill must **throttle to ≤8 req/min** and cache fetched bars per
  `(ticker, date)` under the opportunity folder so re-runs don't re-spend quota.
- Requires a free API key in an env var (e.g. `TWELVEDATA_API_KEY`); never committed.
- Granularity: **intraday minute/hourly** so plans can express "buy 13:00 → sell
  13:12 UTC".

**Sufficiency for our needs (verified June 2026):**
- *Granularity:* free tier provides **1-minute OHLC** for US equities (from
  2020-02-10). Plans are minute-resolution, so this is an exact match. **Minute is the
  resolution floor** — plans must not require sub-minute precision (no "13:12:30").
- *Freshness:* free tier realtime is **15-min delayed**, but this is **irrelevant to
  us** — the simulator runs at T+1 (18:30 ET, ~2.5h after close) and queries *settled
  historical* bars, never live quotes.
- *Invariant — simulate promptly:* free-tier intraday history retention is finite
  (months, not years). The daily simulator cadence ensures every plan is priced while
  still inside the retention window. Plans must **not** be left un-simulated for
  months. The simulator should warn if a plan's exit time is older than the safe
  retention horizon (treat ~30 days as a conservative bound; tune if needed).
- *Out of scope (would require a paid feed):* sub-minute precision, and simulating a
  fill live *during* the session.

## 8. Deferred / out of scope for v1

- Real order execution — **never**; this is simulation only.
- Portfolio-level accounting, position sizing across plans, risk budgeting — later.
- Alternative strategies beyond the two defaults — additive, drop-in later.

## 9. Open decisions (resolved)

- Substrate: **pure Claude Code**. ✅
- Granularity: **intraday minute/hourly**. ✅
- Data provider: **Twelve Data free tier** (stub first, live behind same contract). ✅
- Scout breadth: **open-ended**; dedup window **14 days**. ✅
- Debate: **3 independent persona subagents, 3 rounds, neutral synthesizer**. ✅
- Modularity: **personas / strategy / model-map as three swappable slots via contracts**. ✅
- Post-mortem: **modular 2-role team (Investigator + Critic + synth); losers + flukes only**. ✅
- Learning loop: **in v1** — lessons re-injected into research. ✅
- Scheduling: **ET-anchored, `America/New_York` pinned**. ✅
```
