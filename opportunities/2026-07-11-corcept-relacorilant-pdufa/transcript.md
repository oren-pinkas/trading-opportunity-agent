# Debate transcript — 2026-07-11-corcept-relacorilant-pdufa

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- Strategy: `three-round-panel` (debate-three-round-panel)
- Personas / models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus
- Run: 2026-07-07T19:30:04Z
- Reference price: CORT 268.38 @ 2026-07-07T19:00Z (`toa price`, deterministic stub)
- Relevant lessons injected: none on record (`toa lessons-relevant --type regulatory --tickers CORT` → `[]`)

**Verdict: NO-TRADE (unanimous).** The dossier's July 11 2026 PDUFA is a stale
catalyst — the FDA already approved relacorilant + nab-paclitaxel (Lifyorli) for
platinum-resistant ovarian cancer on **2026-03-25**, ~3.5 months before the dossier
date. The binary is resolved; there is no live event to trade on 7/11.

---

## Round 1 — Independent research

### Bull (sonnet)
Long lean, but flagged this as a **probable stale catalyst**. Independent research
surfaced that the FDA approved relacorilant + nab-paclitaxel (brand: Lifyorli) for
platinum-resistant epithelial ovarian/fallopian/primary-peritoneal cancer on
2026-03-25 — "more than 3 months ahead of its planned July 11, 2026 action date."

Evidence (cited):
- ROSELLA (GOG-3073/ENGOT-ov72) Ph3: OS HR 0.65, p=0.0004; mOS 16.0 vs 11.9 mo;
  mPFS 6.5 vs 5.5 mo. [Lancet PIIS0140-6736(26)00462-9; ir.corcept.com]
- FDA approval 2026-03-25 [fda.gov/drugs/resources-information-approved-drugs/...;
  FiercePharma; OncLive; Drugs.com/history/lifyorli].
- Real stock reaction: sharp gap-up +13% to +40% on 2026-03-25/26
  [FinancialContent MarketMinute +19.66%; MEXC +40%; Simply Wall St +13%].
- Prior CRL 2025-12-31 was a **different** indication (hypercortisolism/Cushing's,
  GRACE trial), stock −50% that day — not the oncology file
  [businesswire 20251231309474; PRNewswire].
- Analyst PTs raised post-approval: H.C. Wainwright $75 (from $60), Piper $88
  (from $73); FY26 revenue guide raised to $950M–$1.05B.

Proposed (Round 1): long common, enter ~2026-07-07T20:00Z, exit by 2026-07-14,
base +8–15%, sized for the −20/−50% tail. Key uncertainty: is 7/11 a live event or a
stale calendar artifact? Also flagged the 268.38 sim price vs ~$77–91 real-world gap.

### Bear (sonnet)
Thesis **dead on arrival**, not merely risky. The binary already resolved (approved
2026-03-25); the "BiopharmaWatch PDUFA Calendar" cites the original target date the
FDA beat. No live catalyst on 7/11; the market has had 3.5 months to digest — a buyer
today has **no information edge**.

Evidence (cited): fda.gov approval notice; Corcept IR release; BusinessWire
20260325948774 (URL-dated 2026-03-25); StockTwits "+35% after early FDA nod";
Q1'26 revenue $164.9M, FY26 guide raised to $950M–$1.05B "citing the successful
launch of Lifyorli"; Lancet OS data (solid — not the weak point); Cushing's CRL
2025-12-31 (same molecule/sponsor/division rejected a significant readout weeks
earlier → outcome was genuinely uncertain, not a rubber stamp); Elahere
(mirvetuximab, AbbVie) entrenched + crowded pipeline [Nature d41573-026-00077-7];
price levels irreconcilable ($61–91 real vs 268.38 sim); short interest noisy
(9.7–21%). Real live question = **commercial execution vs Elahere**, reported ~early
August, not 7/11. Action: **no trade; correct the dossier.**

### Quant (opus)
Long at **P(approval)=0.90 / P(CRL)=0.10**; approval +10%→295.2, CRL −30%→187.9;
hold-through net EV ≈ **+5.6%**. Critical caveat: EV sign depends **entirely** on the
gap between 0.90 and the market-implied P — break-even at P_mkt≈0.89, edge =
(0.90 − P_mkt) × ~40%. Flagged "already-approved" web signals (NCCN preferred, ASCO,
FDA pages) as either genuine early approval (→ P≈0.97, clean long) or forward-index
contamination. Base rate for Ph3-OS-positive oncology → approval ~85–92%
[PMC8196526]. Prior CRL was Cushing's, limited read-through. Sizing: tail-capped
≤6% of book. Biggest numerical uncertainty: the market-implied P embedded in 268.38.

---

## Round 2 — Rebuttal

### Bull (sonnet)
Concedes the fact pattern, then **retracts the long**. Three independent research
paths landing on the 2026-03-25 approval is convergent evidence, not coincidence. His
only rescue — an OS-data/label-conversion event, or (the one he'd chase) a **Cushing's
resubmission PDUFA landing ~6 months after the Q4'25 CRL** — is a hypothesis, not a
confirmed 7/11 event; none verified. Adds that the 268.38-vs-$61–91 gap is a "broken
ruler" that invalidates any sizing math regardless of the catalyst. **Concedes
no-trade**; retracts the Round 1 long.

### Bear (sonnet)
Holds **no-trade** and dismantles the quant's EV formula: with a resolved catalyst,
there is **no market-implied P for a 7/11 approval embedded in the tape** — 268.38 is
the real post-approval print 4+ months later. Holding through 7/11 marks against real
historical drift/noise, not catalyst resolution, so any positive P/L is
uninterpretable and would corrupt the post-mortem/lessons pipeline. Concrete downside:
tail-sized exposure into a non-event window (sell-the-news-late, profit-taking,
beta/macro contamination misattributed to a "CRL scenario"). Change-my-mind: a
verified distinct still-pending 7/11 action, or pre-7/11 news showing the market
anticipates an event.

### Quant (opus)
**Concedes no-trade** and corrects his own Round 1: with a public approval, market
P(app) ≈ 0.99 > his 0.90, so by his own equation the long has **negative edge** and
the move term ≈ 0. Models 7/11 as a **non-event**. Branch A (sim fills vs real prices,
P≈0.85): EV ≈ −0.15% (costs). Branch B (sim injects synthetic move, P≈0.15): EV ≈
+0.5% but sign unknowable. **Blended EV ≈ −0.05%, Sharpe ≈ 0.** Final: FLAT / size 0.
Flip triggers: (1) 7/11 is a *different* still-pending decision (separate
indication/label/EMA), (2) options show a fat 7/11 event-vol term (market P << 0.99),
(3) confirmed the sim injects a synthetic move with known direction.

---

## Round 3 — Synthesis (opus)

**hypothesis** — statement: The 7/11/2026 PDUFA in the dossier is a **stale catalyst**;
the FDA already approved relacorilant + nab-paclitaxel (Lifyorli) for platinum-resistant
ovarian cancer on 2026-03-25 (ROSELLA: OS HR 0.65, p=0.0004), so the binary resolved
~3.5 months before the dossier date and is fully digested. The prior 2025-12-31 CRL was
a different indication (Cushing's) and does not revive a 7/11 oncology event. Residual
fundamental lean is long, but there is **no tradable edge** at the dossier's event
window — the actionable verdict is **NO-TRADE**. direction: **long** (residual lean
only). confidence: **12**.

**plan** — CORT, action buy (NOMINAL — zero-size placeholder; verdict is no-trade),
entry 2026-07-11T13:30:00Z @ 268.38, exit 2026-07-11T20:00:00Z @ 268.38,
expected_profit_pct 0.0. Entry == exit == 268.38 and 0.0% encode a do-not-execute
placeholder; no capital deployed. Dossier held at `researched` (deliberately **not**
promoted to `scheduled`) so `simulate-plans` never fills a position.

**dissent** — The strongest unresolved disagreement: whether a **distinct, still-pending
FDA/EMA action** sits near 7/11 that would re-arm the trade — the Bull's proposed rescue
(a Cushing's resubmission PDUFA ~6 months after the Q4'25 CRL, or an OS-data/
label-conversion event). The panel could neither confirm nor refute it; if verified it
flips the verdict from no-trade to a live binary. Coupled to this is the Quant's Branch-B
uncertainty about simulator mechanics: if the sim injects a synthetic move at the dossier
event rather than filling against the real post-approval tape, a positive P/L would be a
harness artifact of unknowable sign. Both must be resolved before any lesson is drawn
from this dossier's simulated outcome.
