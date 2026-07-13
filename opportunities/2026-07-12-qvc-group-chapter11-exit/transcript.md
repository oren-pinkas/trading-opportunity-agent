# Research Debate Transcript — 2026-07-12-qvc-group-chapter11-exit

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel` (bull/bear/quant, synthesizer). Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.

Isolation note: this debate was run in isolation — no other opportunity dossier in this repo was consulted; judgment formed strictly from this opportunity's own dossier plus independently gathered market/news research.

Institutional lessons injected (from `toa lessons-relevant --type regulatory --tickers QVCGA`):
1. "Before finalizing any plan, validate that every entry and exit timestamp falls within an open trading session (not a weekend or exchange holiday) for the specific instrument, and roll non-trading exit dates forward to the next open session." (CZR case, 2026-07-12)
2. "Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines) directly onto an execution timestamp — treat such dates as catalysts and derive the fill time from the nearest valid trading session." (CZR case, 2026-07-12)

---

## Round 1 — Independent research (parallel, no cross-visibility)

### Bull (sonnet)

Frames this as a litigation-arbitrage catalyst play on residual equity value at the QVCG parent level, not a "buy the turnaround" story. Key evidence:

- Petition date April 16, 2026, S.D. Texas, Judge Alfredo R. Pérez; debt cut ~$6.6B → ~$1.3B. ([Bondoro case summary](https://bondoro.com/qvc-group/), [elevenflo](https://elevenflo.com/blog/qvc-group-chapter-11-bankruptcy))
- Second Amended Plan (June 2, 2026) reversed the original full-cancellation treatment: QVCG preferred (Class A6) and common (Class A7) now get a pro rata share of "QVCG Equity Consideration." ([elevenflo](https://elevenflo.com/blog/qvc-group-chapter-11-bankruptcy))
- Objecting preferred holders argue QVCG is solvent standalone (~$195M cash + 62% stake in Cornerstone Brands); blocking the $400M intercompany settlement would preserve >$160M for QVCG equity classes. ([vista.today](https://vista.today/2026/06/qvc-group-bankruptcy-shareholder-challenge/), [ION Analytics/Debtwire](https://ionanalytics.com/insights/debtwire/qvc-preferred-equity-trades-up-as-shareholders-abandon-request-for-equity-committee-usd-400m-value-stripping-settlement-still-subject-to-scrutiny-legal-analysis/))
- Confirmation trial ran June 4–5 and June 8–9, 2026; RSA plan-effectiveness deadline ~July 15, 2026. ([Law360](https://www.law360.com/articles/2488247/qvc-seeks-ch-11-plan-ok-over-shareholder-complaints))
- **Ticker reality check:** Nasdaq delisting effective April 24, 2026; QVCGA → OTC successor QVCAQ. Real OTC quote ~$0.06 as of July 1, 2026 (52-week range $0.06–$0.40) — vs. the dossier/tool's stub price of $126.40, a ~2000x gap. Flags the stub as untethered to reality. ([TipRanks](https://www.tipranks.com/news/company-announcements/qvc-group-faces-nasdaq-delisting-after-chapter-11-filing), [stockanalysis.com](https://stockanalysis.com/quote/otc/QVCAQ/history/))

Proposed (conditional on price-feed reconciliation): small speculative long QVCAQ, entry now, exit at confirmation ruling / rolled to Monday 2026-07-27 (dossier's July 25 is a Saturday). Invalidation: close if the $400M settlement is approved as-is or equity consideration prices near zero.

### Bear (sonnet)

Frames the dossier's "targets exit by late July" framing as understating live legal risk. Key evidence:

- Original Disclosure Statement (filed with the April 16, 2026 petition) contemplated cancelling QVCG preferred/common for **no consideration**. Second Amended Plan (June 2, 2026) added an undisclosed "pro rata share of QVCG Equity Consideration" — no dollar figure found in any source.
- Case still contested: combined disclosure/confirmation trial ran June 4–9, 2026; **no confirmation order entered as of June 9**. Objectors: preferred holders (sought emergency equity committee), U.S. Trustee (third-party releases), individual shareholders. ([Octus](https://octus.com/resources/articles/qvc-preferred-shareholders-seek-emergency-appointment-of-equity-committee/), [PETITION](https://www.petition11.com/p/qvc-c-for-confirmation))
- Central fight: a $400M intercompany claim by QVC Inc. against parent QVCG that did not appear in QVCG's own 10-K filed one day before the petition — preferred holders argue this strips value from an otherwise-solvent parent.
- Found real QVCGA traded **$3–$7.36** in the May–June 2026 window (high $7.36 on May 11; market pricing ~85% probability of total wipeout at ~$3/share, ~$24M market cap) — a different, higher range than the bull's $0.06 finding, flagged as unresolved. ([strxstk Substack](https://strxstk.substack.com/p/qvcga-is-it-worth-0-or-34))
- RSA ~90-day effectiveness deadline ~July 15; dossier's own impact_window (2026-07-25) falls on a **Saturday** — not a trading session.

Recommends no long without: (a) a confirmed favorable ruling, (b) a disclosed non-trivial equity %, (c) a confirmed real price.

### Quant (opus)

Bottom line up front: **not a tradeable edge**. Base rate for old common recovering materially in an ~80% debt-cut prepack is well under 10%; historical analogues (GM, Lehman, Sears, Revlon, Bed Bath & Beyond, WeWork) show near-total wipeout as the norm. The debtor itself originally stated interests would be "cancelled ... for no consideration."

Explicit terminal-value distribution: 85% chance $0, 10% chance ~$10, 5% chance ~$60/share → EV ≈ $4/share. Against the $126.40 stub: long EV ≈ **-97%**. Short would be EV-positive (~+97%) but unborrowable/no locate on a delisted, suspended security — uncapturable. Flags that QVCGA has had **no open trading session since the April 24, 2026 suspension**, which breaks any "roll exit to next open session" logic since there is no session to roll into.

Recommends **PASS, size = 0**.

---

## Round 2 — Rebuttal (parallel, full cross-visibility)

### Bull rebuttal

Concedes the tail-probability sizing gap to the quant (can't size 10%/5% better). Cannot reconcile the $3–$7.36 vs $0.06 discrepancy from available information; downgrades own $0.06 print from "verified proxy" to "unverified" and **retracts the immediacy of "enter now."** Concedes the "no open session since April 24" point is the strongest argument against him — if true, there's no clean entry or exit mechanism regardless of the fundamental thesis, and treats the quant's claim as controlling for execution feasibility. Notes neither peer addressed the A6-preferred vs A7-common priority split, or that "plan confirmed" and "plan effective" are distinct risk events. **Moves from "small speculative long, enter now" to "no position, watch-only"** pending: (1) a timestamped executed trade print (not quote) post-April-24 on the correct symbol/CUSIP, (2) a disclosed numeric equity-consideration %, (3) resolution of the $400M settlement dispute, (4) clarity on A6 vs A7 relative treatment. States that if no executed session exists, the position is uninvestable "full stop," siding with the quant's size=0.

### Bear rebuttal

Pushes back that "fighting for >$160M" is a claim in litigation, not an allowed claim — the bull's own invalidation trigger concedes the base case is the bad one. Agrees with the quant's EV/base-rate direction but cautions the 85/10/5 distribution is calibrated off analogues, not this case's disclosed terms, and that the 10-K omission of the $400M claim is a fact pattern a bankruptcy judge takes seriously (could fatten the tail, doesn't flip the recommendation). Flags that nobody addressed the solvency dispute on the merits, or that a lapsed RSA deadline could mean delay/renegotiation rather than resolution. On the price discrepancy: attributes it to a likely ticker/symbol mismatch (stale pre-delisting QVCGA prints vs. current QVCAQ) or a stale/thin/erroneous print; now weights $0.06 as the more likely current figure, but treats the >100x disagreement between two independent research passes as itself disqualifying. Upgrades own bar from "wait for better information" to "wait for a tradeable market to even exist." Final: no position, size 0.

### Quant rebuttal

Ran the actual fill engine: the stub provider deterministically returns ~$126–131 for QVCGA — **confirmed synthetic, not a real quote**. Resolves the bull/bear discrepancy: QVCAQ (Q-suffix = standard OTC bankruptcy convention) is the live post-suspension ticker; the bear's $3–$7.36 QVCGA range is almost certainly stale pre-April-24 data, making $0.06 the more credible current anchor. But identifies a gap neither peer modeled: **Class A6 (preferred) is senior to A7 (common)** with a liquidation preference — if the disputed ~$160M is preserved, preferred's senior claim likely absorbs most/all of it before common sees anything, so "pro rata share of $160M" could still net to ~zero for common even in the "win" scenario. Separately, checked actual data feeds: twelvedata returns HTTP 400 for QVCGA on every date probed and has no 1-min bars for QVCAQ — **neither real price is fillable in this harness**, so simulated P/L would be meaningless regardless of direction. Re-anchors EV by price: at $126 (stub) EV ≈ -97%; at $3–7 (stale) EV roughly breakeven but the anchor is invalid; at $0.06 (live) EV is near breakeven-to-modestly-positive if there's a 10–15% chance of $0.15–0.40/share recovery — a genuinely different conclusion than at $126. Downgrades own framing from "confident -97%, obvious PASS" to **"PASS on execution/integrity grounds, EV indeterminate."** Short thesis declared dead regardless (no borrow/locate, no fillable feed).

---

## Round 3 — Synthesis (opus)

**Hypothesis:** QVC Group parent-level residual equity (Class A7 common, tracked via delisted QVCGA / OTC successor QVCAQ) is uninvestable in this harness. All three personas converged on PASS/size-0 across two separable failure modes: an integrity/execution failure (synthetic $126.40 stub, no post-suspension trading session, no fillable feed for either candidate real price) and a fundamental uncertainty (unresolved A6/A7 liquidation-preference waterfall plus undisclosed equity-consideration %).
**Direction:** no_trade
**Confidence:** 88/100

**Plan:** No position. Ticker QVCAQ noted as the correct real-world successor instrument (QVCGA suspended since 2026-04-24), but no entry/exit timestamp can be derived — there is no open trading session to anchor a fill to, and the harness cannot fill either candidate real price. Per institutional lesson, no legal-calendar date (RSA ~July 15, confirmation, dossier's July 25 which is a Saturday) may be mapped directly onto an execution timestamp regardless.

**What would make this actionable (all required):**
1. A timestamped executed trade print (not a quote) on QVCAQ after 2026-04-24, fillable through a real data feed.
2. A filed, disclosed numeric equity-consideration figure for the QVCG equity classes.
3. Resolution of the ~$160M dispute in favor of preservation (intercompany settlement rejected/reduced/carved).
4. Explicit clarity that A7 common receives value after A6 preferred's liquidation preference is satisfied.

**Dissent (strongest unresolved disagreement, gold for post-mortem):** In the bull's own "win" scenario, does Class A7 common recover anything, or does Class A6 preferred's liquidation preference consume the entire disputed ~$160M first, leaving common at ~$0 even when the equity thesis "works"? Raised only in the final round by the quant and never rebutted — the entire fundamental case hinges on this priority-stack question, and the debate closed without resolving it.
