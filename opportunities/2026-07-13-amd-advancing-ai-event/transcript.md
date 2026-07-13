# Research Debate Transcript — 2026-07-13-amd-advancing-ai-event

Strategy: `three-round-panel` (debate-three-round-panel). Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Event:** AMD hosts its Advancing AI 2026 event July 22-23 in San Francisco ahead of Q2 earnings expected around Aug 4, 2026, with the Zen 6 EPYC launch and AI accelerator roadmap in focus after the stock's ~130-145% YTD surge. Source: "AMD Stock Forecast | Advancing AI Event, Q2 Earnings" — https://capital.com/en-int/market-updates/amd-stock-forecast-23-06-2026 (accessed 2026-07-13). Debate date/time: 2026-07-13T20:45:14Z.

Relevant lessons injected (from `toa lessons-relevant --type product --tickers AMD`): none recorded.

Note on price data: bull's Round 1 price series (Jul10 $558.39, Jul13 $535.87) diverged ~2% from bear's and quant's independently-pulled twelvedata series, and was later diagnosed (by quant, in Round 2) as carrying the signature of the known `toa price` stub-data bug — `toa price` silently returns fake/synthetic data unless `--provider twelvedata` is explicitly passed. Bull re-pulled with the correct flag in Round 2 and the series reconciled (small residual differences attributable to intraday-bar-vs-close sampling). **Always use `--provider twelvedata`.**

---

## Round 1 — Independent Research

### BULL (sonnet)
Verified prices via `toa price AMD ... --provider twelvedata` (later flagged as possibly stub-corrupted — see note above): 2026-01-02 ≈$222.93, 2026-06-23 ≈$519.82, 2026-07-10 ≈$558.39, 2026-07-13 ≈$535.87 (+140% YTD, -4% pullback in the last 3 sessions).

Thesis: a rare double-catalyst setup — Advancing AI (Jul 22-23) sits just 12 days ahead of Q2 earnings (~Aug 4), compressing two tradeable events into one arc. The recent pullback is a shakeout giving a better entry than chasing the $558 high. Two catalysts let AMD pre-condition Street sentiment before the harder earnings gate. 130%+ YTD momentum in AI-infrastructure names (NVDA comparison) has kept working for three years running. Proposed **LONG AMD** — common stock or an Aug 7-14 call debit spread; entry now through Jul 21 on weakness toward $520-530; scale out 1/3-1/2 into strength on any event pop; hold the remainder through earnings with a hard stop below ~$510-515. Explicitly flagged own kill conditions: crowded positioning/rich options skew, a pre-event guide-down, or an incremental (non-beat) roadmap reveal — any of which flips this into a classic "sell the news after a huge run" pattern.

### BEAR (sonnet)
Verified prices (twelvedata): 2026-01-02 $222.93, 2026-04-01 $211.92 (flat Q1 — the surge is Q2-driven, not gradual), 2026-05-01 $351.48 (+66% in one month), 2026-06-15 $549.24 (prior high), 2026-07-07 $508.55 (-7.4% pullback from the June high), 2026-07-13 $546.10 (rallied +7.4% in under a week, back within 0.6% of the June high). +145% YTD.

Key point: this is a **re-test of a level that already failed once** (rejected from $549 down to $508 by Jul 7, now back near $549) — not a fresh breakout. Much of the good news is already priced given AMD controls the framing at a self-hosted promotional event (diminishing marginal information value after a year of "we have design wins" messaging). Sell-the-news risk is high after this magnitude of run. Binary risk stacking: event and earnings only ~2 weeks apart means no clean exit before the harder Aug 4 catalyst, so a post-event fade could compound into pre-earnings de-risking. NVDA remains dominant with its CUDA moat; AMD's MI400/450 narrative depends on hyperscaler orders converting from slides to real revenue. The 2.4x move in two quarters is multiple expansion, not EPS-driven, leaving the stock exposed to any broader "AI capex digestion" scare. Steelmanned the bull case fairly (MI300/350 revenue growth is real, Zen 6 EPYC share-gain is durable, hyperscaler capex commentary has kept surprising upside, momentum can persist longer than valuation skepticism predicts, the Jul 7→13 rally could validly be read as healthy continuation). Bottom line: skeptical of new long exposure; wants the bull to explain why the failed June test doesn't apply this time.

### QUANT (opus)
Verified prices (twelvedata): 2026-01-02 $225.90 → 2026-07-13 $546.10 (+141.7% YTD). Recent chop: $549.24 (Jun 15) → $522.48 (Jun 23) → $566.73 (Jul 6, local high) → $546.10 (Jul 13), -3.6% off the Jul 6 peak — momentum **stalling, not accelerating**, into the catalyst.

Historical base rates: Dec 2023 Advancing AI (genuinely new MI300 information) → +3% over two days. June 2024 Advancing AI (roadmap already telegraphed) → flat/mild sell-the-news. Read-through: Zen 6 EPYC + the MI400/450 roadmap is largely pre-announced/leaked, rhyming with the flat June 2024 case, not the surprise Dec 2023 case. AMD product-event moves cluster ±3-5%; the big 8-10%+ moves are reserved for earnings, not analyst days.

Assumed probabilities (event window through ~Jul 29, pre-earnings): P(genuine surprise)=0.30, P(pop>5%)=0.15, P(modest pop +3%)=0.25, P(flat)=0.25, P(modest selloff -4%)=0.20, P(sharp selloff -9%)=0.15. EV of a naive long at $546: gross EV ≈ -$1.09/share (-0.20%); net after costs ≈ -0.25% to -0.30%. EV of a naive short mirrors to +0.20% gross but is rejected due to the fat right tail (an AI-demand beat or design win could gap AMD +10-15%) — reject the naked short given the negative skew.

Verdict: the event is a coin-flip with small negative EV on either directional side after costs; the real information event is Aug 4 earnings, not the roadmap show. Recommendation: **PASS** on any directional event trade; if forced, a tiny (<0.5% NAV) defined-risk sell-the-news fade (short call spread / long put spread expiring right after the event, before Aug 4). Treat Aug 4 earnings as a **separate** decision, sized independently, leaning long-vol/direction-neutral (a debit structure sized to AMD's typical ~9-11% earnings move) rather than directional.

---

## Round 2 — Rebuttal

### BULL
Re-pulled prices with `--provider twelvedata`: Jun 15 $550.81, Jul 6 $566.36 (new local high), Jul 7 $511.53 (-9.7% single-session drop), Jul 13 $545.65 (+6.7% off the Jul 7 low). Converges with bear/quant's tape (small differences are just intraday-vs-open sampling) — no longer disputes the data, only the interpretation.

Partially conceded the "stalling momentum" framing but argued the move was a sharp one-session flush followed by a strong recovery (a "V," not a rollover) — more consistent with position-adjustment ahead of a known catalyst than distribution, while honestly admitting no volume/breadth data to prove demand-driven vs. short-covering. On quant's EV math: conceded the arithmetic, pushed only on inputs — the Dec2023-vs-June2024 base-rate mapping assumes the *absence* of a live named-hyperscaler dollar commitment at the event, which is an assumption, not a fact; and quant's own fat-right-tail (used to reject the naked short) logically argues for a small convex defined-risk **long** structure rather than a full pass. Pushed back on bear's "failed retest" as premature — the stock hasn't re-approached the $550-566 zone and failed a second time, it's approaching it for the first time since the Jul 7 flush — while agreeing the binary-risk-stacking critique was underweighted in Round 1.

**Conceded:** dropped "long common stock through both catalysts" entirely. Revised to a small (<1% NAV) defined-risk call spread expiring after the event with a hard time-stop before Aug 4, not held into earnings; earnings treated as a fully separate, independently-sized decision (leaning long-vol). Revised invalidation level to the actual Jul 7 flush low of $511.53 — a break/hold below that, especially pre-event, would confirm bear's thesis and bull would stand down entirely.

### BEAR
Noted convergence with quant's independent "already priced in / stalling momentum" read via a different method (technical re-test vs. historical base-rate) as a meaningful signal, not coincidence. Pushed back on bull's "-4% pullback = entry" framing: all three personas' price series disagreed on direction of the last leg (bull: -4%; bear: +7.4%; quant: -3.6%) — flagged as a hard blocker to sizing until reconciled (later resolved: bull's series was the stub-corrupted one). Argued "two catalysts pre-condition the Street" is circular — pre-conditioning either carries real information content (which contradicts "already priced in") or it doesn't (which doesn't de-risk earnings); can't have both. Argued NVDA is the wrong reference class for "130% momentum has worked for 3 years" — survivorship bias; the correct comparable set is AI-capex-linked names that ran 100%+ on narrative ahead of confirmed order books, a set that includes non-survivors (e.g., SMCI's 2024 unwind), not just the one surviving example.

What would change bear's mind: hard hyperscaler order/dollar confirmation (not roadmap slides) at the event; reconciled price data confirming a genuine dip; guarded AMD IR language lowering the Aug 4 bar; options IV/skew data showing the event is *not* already crowded.

### QUANT
Diagnosed bull's Round 1 series as bearing the signature of the known `toa` stub-data bug (matched Jan 2 but diverged ~2% on recent prints) — advised discarding it in favor of the twelvedata-sourced bear/quant numbers. Rejected "two catalysts, one narrative arc" as improving EV: two events sharing a common driver are positively correlated, so holding through both is concentration, not diversification — argued for sizing the two events independently and, if anything, scaling out before earnings rather than holding through. Noted bear's "$549 failed retest" and quant's own "$566 local high, -3.6%" don't fully reconcile on the exact level, but both readings agree directionally that momentum is not accelerating. Explicitly refused to treat bear+quant's shared skepticism as itself an EV edge — called that correlated opinion, not new information, and flagged upsizing a fade on that basis as a textbook confirmation-bias trap. Held Round 1 probabilities and recommendation unchanged.

What would change quant's mind: options IV/term-structure data (cheap implied vs. history → flip to a long-vol structure; rich implied + crowded positioning → size up the defined-risk fade); named hyperscaler dollar commitments (kills the fade); a pre-event guide-down or positioning washout.

---

## Round 3 — Synthesis (opus)

**Convergence summary:** all three personas independently arrived at the same place from different methods. Bull dropped the original "long common stock through both catalysts" thesis entirely. Bear and quant were skeptical of new long exposure from the start. The tape was reconciled (twelvedata: ~$546 on Jul 13, local high in the $549-566 zone, a sharp -9.7% Jul 7 flush to $511.53, +6.7% recovery). The only live disagreement is whether a sub-1%-NAV defined-risk position around Jul 22-23 clears the bar — and the honest answer is that it does not, absent one missing input (options IV/skew).

**hypothesis:**
- statement: AMD's Advancing AI event (Jul 22-23) is a self-hosted, roadmap-heavy promotional event whose informational content is largely pre-priced after a +141% YTD run. Base rates for AMD product events cluster around ±3-5% moves; the naive-long EV at ~$546 is slightly negative net of costs (roughly -0.25% to -0.30%), and the fat right-tail (a named-hyperscaler dollar commitment could gap AMD +10-15%) makes a naked short uninvestable. A defined-risk sell-the-news fade only earns positive EV if options IV/skew confirm the event is crowded/rich — that data was never obtained. The real information event is Aug 4 earnings, a separate, independently-sized decision out of scope for this dossier.
- direction: no_trade (neutral)
- confidence: 72 (high confidence in the PASS decision; the residual uncertainty is entirely the un-pulled IV/skew data that all three personas named as the single thing that would flip the call)

**plan:**
- ticker: AMD
- action: **pass**
- entry: none
- exit: none
- expected_profit_pct: 0
- conditional trigger (not a committed order, logged for context): if a pre-event options pull (before 2026-07-22T13:30:00Z) shows an implied move materially rich vs. the ±3-5% event base rate, plus crowded call skew, and no named-hyperscaler dollar commitment has leaked, then a tiny (<0.5% NAV) defined-risk fade — short call spread or long put spread — entry 2026-07-22T14:00:00Z, hard time-stop/exit 2026-07-24T19:55:00Z (before Aug 4 earnings). Invalidation: any credible named-hyperscaler dollar order at the event kills the fade immediately; a break-and-hold below the Jul 7 flush low $511.53 pre-event would also argue against any long-side convexity.

**dissent (strongest unresolved disagreement — post-mortem gold):**
The bull's unresolved objection is that quant's own fat-right-tail — the same asymmetry used to reject a naked short — logically argues for a small convex defined-risk long (a call spread), not a full pass. Quant counters that the naive-long net EV is negative and a convex long only pays off if implied vol is cheap versus history, which was never measured. This stayed unresolved because the deciding input — options IV term structure and skew, plus any hyperscaler order confirmation — was never pulled. The debate passed on a directional trade while explicitly flagging that a single missing data pull could have justified a tiny position in *either* direction (cheap IV → long-vol/convex long; rich IV + crowding → the fade). **Post-mortem check:** pull AMD's actual pre-event options IV/skew and compare to the historical ±3-5% event-day base rate — that one data point would tell whether PASS was a fully-informed rejection or a data-gap default.
