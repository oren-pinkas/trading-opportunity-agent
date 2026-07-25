# Debate transcript — 2026-07-23-peco-exelon-strike (EXC)

Strategy: `three-round-panel`. Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Institutional lessons injected (via `toa lessons-relevant --type economic --tickers EXC`):
1. Anchor entry to a live pre-event quote, not the research-day price; if the live price has drifted >~0.5-1% from the plan anchor, re-derive targets/EV or void the trade rather than filling blind. (2026-07-01-ism-mfg)
2. When the thesis is "catalyst reprices X higher" and X has already rallied to its 52-week high before the event, treat the move as priced-in: fade or shrink, don't chase the entry. (2026-07-01-ism-mfg)
3. Skip trades whose only positive-EV path is a pre-market conditional entry the harness cannot fill; if the executable cash-open leg's EV is ~0, don't record the trade. (2026-07-02-june-jobs)
4. After a known regime shift, require a differentiated surprise vs consensus before shorting duration into a data print: an in-line print is already in the curve and gets faded by duration buyers. (2026-07-02-june-jobs)

## Round 1 — Independent research

### BULL
Data provider is rate-limited right now (twelvedata returning HTTP 429 on repeated attempts) — flagging this as a live caveat per institutional lesson #1: no fresh quote to anchor entry to, so any numbers below are indicative and must be re-verified against a live print before any fill.

**Read on the event:** first strike in PECO's 145-year history (WHYY, accessed 2026-07-23) is a headline-grabbing rarity that generates outsized sentiment noise a bull should fade. PECO is a *regulated* T&D utility; a short strike does not reprice the regulated asset base or capex plan driving EXC's EPS growth. The strike is already public/dated (started July 4, ~3 weeks old); any initial negative reaction should already be in the tape. The forward catalyst per the dossier is resolution timing into 2026-08-15 — i.e. the tradeable edge is the eventual *settlement* (a positive, de-risking event).

**Thesis:** contrarian long into resolution. Labor strikes at regulated utilities typically end in negotiated contracts passed through via O&M cost recovery — a bounded, market-discounted hit. Settlement near 8/15 should produce a modest relief pop.

**Evidence:** WHYY article (strike start, 1,600 workers, first-ever in 145yr history); dossier impact_window 2026-08-15. Live price check via `toa price EXC <ts> --provider twelvedata` returned HTTP 429 twice — no fresh quote available.

**Proposed action:** small long EXC common (or small call/call-spread past 8/15); entry gated on confirming price hasn't already run up (lesson #2); exit at/after settlement news or by 8/15.

**Caveats:** no live quote this session; escalation/adverse-PUC-action risk would weaken the case; low-conviction, low-magnitude trade; avoid unfillable conditional entries (lesson #3).

### BEAR
Rate-limited on live quote (429 x2). Proceeding on fundamentals/public record.

**Bottom line: pass.** Scale mismatch — Exelon is a 6-utility holding company (ComEd, PECO, Atlantic City Electric, Delmarva, BGE, Pepco), ~USD 24B consolidated revenue, ~19,000 employees. 1,600 striking PECO workers over wages/benefits is a rounding error against that base, not a company-wide event.

**What's priced in:** regulated utilities recover incremental storm/labor O&M costs through rate mechanisms (PA cost-recovery riders) — largely a *timing* issue, not a permanent hit, subject to PUC prudency review. The dossier's own framing ("resolution timing... are a forward catalyst") is speculative and conditional on an outcome that hasn't happened. No 8-K, analyst EPS cut, rating action, or PUC filing is cited — only a single local-news (WHYY) source.

**Risk to the bull trade:** most likely outcome is the strike settles quietly before 8/15 with a standard CBA, Exelon absorbs it as budgeted labor cost, PA regulators allow pass-through, EXC re-rates on nothing having changed. Utilities also use contractor/mutual-aid crews to cap reliability/financial tail risk.

**Proposed action:** no trade. Minimum bar before any entry: live quote, corroborating source beyond WHYY, confirmation market hasn't already re-priced the strike.

### QUANT
Data blocker up front: 7 attempts across ~5 minutes (25s/70s backoff) on `toa price EXC <ts> --provider twelvedata` (including strike-start context bars 2026-07-02/06) all returned HTTP 429 — a provider quota wall, not a coverage gap. No live anchor obtainable; reasoning in percentage space per Lesson 1.

**Base rate:** PECO is ~11% of EXC consolidated revenue, ~15-18% of parent net income; 1,600 workers is ~8% of EXC's ~20,000 headcount, 0% of nuclear/other five utilities. Incremental strike O&M ≈ USD 2-5M/week; a 6-week strike ≈ USD 12-30M pre-tax ≈ 0.4-0.8% of one year's EPS ≈ 0.1-0.3% of enterprise value — and this is a rate-regulated entity where prudently-incurred O&M is routinely deferred/recovered.

Historical analogues (National Grid/USW MA gas lockout 2018-19, ~1,250 workers, ~6mo; Con Edison/UWUA lockouts 2016/2012): parent stock not identifiable from the labor action absent a safety incident, PUC penalty docket, or spread to nuclear/bulk power — none present here.

Base-rate estimates: P(attributable parent move ≥3%) ~3-5%; P(≥2%) ~8%; P(≥0.75%, above noise floor) ~15-20%. EXC beta ~0.5, annualized vol ~18-20% → σ_daily ≈1.1-1.25%. The event's entire fundamental content (0.1-0.3% of EV) is smaller than a quarter of one day's σ.

**Fatal confounder:** EXC reports Q2 earnings ~2026-07-30/31, inside the 2026-08-15 impact window — will dominate/obscure any strike-driven move.

**EV calc:** P(favorable resolution move ≥0.75%|resolution before 8/15)=55%×20%=11% at +1.0%; P(adverse)=8% at -1.5%; friction=0.12%. EV_long = 0.11%-0.12%-0.12% ≈ -0.13%. EV_short ≈ -0.11%. Gross edge (±0.01%) is ~1/12th of friction.

**Recommendation:** PASS. Would change mind: safety/reliability incident, PUC docket with penalty exposure, spread to other subsidiaries/generation, or visible narrative pricing (EXC underperforming XLU peer set with strike cited).

## Round 2 — Rebuttal

### BULL
Concedes Quant's Q2-earnings confounder is the strongest point raised — can't isolate a settlement-driven move from an earnings-driven move pre-print. Restructures: no new entry before the 7/30-31 print; any position must survive earnings on its own merits or enter post-earnings with a shorter window to 8/15.

Agrees with Bear's fact pattern (scale mismatch, single-source sourcing) but had never claimed a fundamental EPS story — the thesis was sentiment/overhang removal. Concedes, however, that Bear is right there's no evidence of any priced-in negative to fade, which symmetrically means there's no confirmable overhang to remove either — closer to "nothing happened, nothing will happen."

Flags that Quant's EV math shows a favorable probability skew (11% vs 8%) that the magnitude assumptions (+1.0%/-1.5%) invert — can't independently verify those magnitudes either, but doesn't dispute the mechanics.

**Net position:** downsizes from "small long, entry pre-earnings" to "no new entry before earnings; conditional small long only post-earnings if a clean, separable reaction to actual settlement news appears with a live quote confirming no pre-run." Effectively converges to no trade now.

### BEAR
Bull's "already priced in / settlement is the catalyst" is wishful, not evidenced — no baseline print exists to show any reaction was priced in, and if the strike start was never going to move the stock (scale mismatch), there's no de-risking dividend to harvest at settlement either. Two unfalsifiable assumptions stacked in opposite directions.

Quant's independent quantitative build converges with Bear's qualitative case via a different route: sub-noise sizing (0.1-0.3% of EV vs ~1.1-1.25% σ) backs the scale-mismatch intuition numerically; the Q2 earnings confounder further kills Bull's setup since any post-8/15 entry would also be contaminated by the print.

**Would change mind:** an 8-K/PUC filing showing financial materiality, strike scope expanding beyond PECO, or a live quote showing an outsized (>2x normal σ) move at strike-start. None exists.

**Final position:** unchanged, PASS — conviction higher after this round.

### QUANT — critical new fact
Discovered via in-repo check that this dossier is a **stale duplicate** of an already-researched, already-closed opportunity: `2026-07-08-peco-ibew-strike` (status: researched, verdict NO-TRADE, confidence 78, researched 2026-07-10). Same 1,600 IBEW Local 614 workers, same 2026-07-04 strike start, same EXC ticker. That dossier documents: tentative agreement 2026-07-06/07, workers back 2026-07-08/09, ordinary 5-year terms (4%/4.5% raises linemen/gas techs, 3%/yr call-center, restored pensions/retiree medical), PECO stating no immediate rate impact, and EXC trading USD 46.54-47.43 on 2026-07-09 (first post-settlement session) — mid-range of 52-week band, zero discernible reaction, no volume/analyst signature. Prior panel's independent EV calc: -0.12% to -0.24%.

*[Orchestrator note: this finding was independently verified by directly reading `/Users/oren/Oren/lab/trading-oppurtonity-agent/opportunities/2026-07-08-peco-ibew-strike/dossier.md`, which confirms status, settlement dates/terms, EXC's flat post-settlement range, and the NO-TRADE verdict.]*

Recomputes Bull's decomposition with settlement as a known fact: P(settlement in window) ≈ 1.0 (already occurred) but E[move|settlement] ≈ 0 (measured, not modeled) — product ≈ 0; after friction, EV ≈ -0.12%. Bull's own efficiency premise ("already priced in") and "settlement is a catalyst" are shown to be mutually exclusive: if the strike-start reaction was fully priced (no reaction to price), settlement carries no incremental information to de-risk.

Sensitivities: P(favorable) would need to rise from 11% to >24% for EV_long to turn positive holding magnitudes fixed — the posterior, conditioned on zero disclosure events over 20 days, is actually *lower* (4-6%), not higher. Even granting 0% adverse probability, EV_long is still -0.01% — friction alone kills the trade regardless of risk management or sizing. With the strike term now ≈0, Q2 earnings (σ ~2-3%) is the only live variance driver in the window — SNR ≈ 0.

**Confidence upgraded to 92, PASS** — reason changed from "sub-noise/confounded" to "event already resolved flatly, no residual catalyst exists."

**Process finding:** dossier should be marked resolved-stale/duplicate of `2026-07-08-peco-ibew-strike`, not merely no-trade. Root cause: scout dedup (`lib/dedup.py`) uses a 14-day ticker-overlap window; these two dossiers were created 15 days apart (2026-07-08 → 2026-07-23) — one day past the window — despite describing the identical event.

**Falsifiable flip condition:** a PA PUC docket opened before 2026-08-08 seeking a *going-forward* regulatory disallowance/ROE reduction on PECO ≥ USD 100M annualized pre-tax (~1.5-2% of EXC equity value), confirmed by ≥2 independent sources including the primary filing, landing on a non-earnings session, with a live quote obtainable to set entry/stop. Absent that, asserts EXC's cumulative strike-attributable move through 2026-08-15 will be statistically indistinguishable from zero (|residual vs XLU-hedged benchmark| < 0.5σ ≈ 0.6%).

## Round 3 — Synthesis

**hypothesis:**
- statement: No tradeable edge exists. The event this dossier framed as a forward catalyst had already resolved before the dossier was created: the same 1,600 IBEW Local 614 PECO workers who struck 2026-07-04 reached a tentative agreement 2026-07-06/07 and returned 2026-07-08/09 on ordinary terms, with PECO stating no immediate rate impact. EXC's first post-settlement session (2026-07-09) traded USD 46.54-47.43 — mid-range of its 52-week band, with no volume/analyst/rating signature. The market reaction is a measured zero, not a modeled unknown. P(settlement in window)≈1.0 but E[move|settlement]≈0, so the product is ≈0; after friction (~0.12% round-trip), EV_long/EV_short are both negative, and even granting a 0%-adverse branch EV_long is still -0.01%. Independently, scale caps upside (PECO ~1 of 6 subsidiaries, regulated cost-recovery mutes O&M shocks, incremental cost sub-noise vs EXC's daily σ). EXC's Q2 earnings (~2026-07-30/31) sits inside the impact window and would dominate any residual signal. No live quote was obtainable in any round (twelvedata HTTP 429 throughout).
- direction: neutral
- confidence: 94

**plan:** ticker EXC, action none, no entry/exit, expected_profit_pct 0. Not "wait for a better price" — there is no residual catalyst to wait for.

**dissent (strongest unresolved disagreement, carried forward for post-mortem):**
Does "no measurable move on the settlement session" prove "no edge existed," or only that the daily-bar instrument couldn't resolve a real-but-sub-noise reaction? Bear and Quant both reach PASS but for different reasons — Bear says signal is absent, Quant says signal is present but smaller than friction. These imply different things for whether this class of event (single-subsidiary utility labor action) is worth scouting again, and whether a cheaper execution path/leveraged instrument could ever harvest it. Secondary dissent: nobody in the panel actually checked the PA PUC docket record — Quant's own stated falsifiable flip condition was never tested, only asserted. If EXC moves materially by 2026-08-15, the likely failure mode is "we correctly killed a stale thesis and then stopped looking," not "we mispriced the strike." Also logged: all three personas failed to obtain a live quote (provider 429 throughout) — the panel reached a confident PASS with zero live market data, which is only the right call here because the dossier was stale; a live catalyst under the same data outage should have produced "cannot research — data unavailable," not a directional verdict.

**process note (orchestrator action taken):** Dossier marked `status: researched`, `duplicate_of: 2026-07-08-peco-ibew-strike` added to frontmatter so post-mortem/base-rate tooling does not double-count this as an independent strike-event data point. Root cause for project memory: `lib/dedup.py` uses a 14-day ticker-overlap window (`window_days=14`); these two dossiers were created 15 days apart despite describing the identical event — one day past the window. Recommend widening the dedup window (or adding a ticker+event-type match independent of `last_seen` recency) for `event.type: economic` labor-action stories, which can remain "current news" for weeks after the underlying event resolves.
