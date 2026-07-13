# QTTB (Q32 Bio) SIGNAL-AA Part B — Three-Round Panel Transcript

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Strategy:** debate-three-round-panel
- **Personas / models:** bull (sonnet), bear (sonnet), quant (opus); synthesizer (opus)
- **Run:** 2026-07-13T07:52:00Z
- **Structure note:** Q32 Bio reports 36-week topline results from Part B of SIGNAL-AA
  (bempikibart in alopecia areata) on 2026-07-13 — confirmed a Monday, a normal open
  trading session (per institutional lesson from `2026-07-08-caesars-icahn-fertitta-bidding-war`
  on validating catalyst dates against trading sessions).
- **Reference prices** (stub/deterministic pricing source): QTTB @ 2026-07-11T20:00Z =
  $365.26; QTTB @ 2026-07-13T07:30Z = $380.06 (+4.05% pre-print drift).

---

## Round 1 — Independent positions

### BULL (sonnet)
Long QTTB common stock. A clean single-asset binary catalyst — no diversified pipeline
to obscure the read. Alopecia areata is commercially hot (Litfulo/Olumiant precedent
shows the category re-rates on good data). The pre-print tape already drifted +4.05%
over ~35 hours with no news out — reads as informed positioning, wants to be on the same
side of that flow. Acknowledges the dossier is thin (single secondary source, no trial
design/endpoint/powering detail, no analyst targets, no options-implied move, no short
interest data) — trading the setup and the tape, not a detailed clinical thesis.
**Action:** BUY, entry near US cash open 2026-07-13T13:30Z, exit by close
2026-07-13T20:00Z, hard stop below ~$365 (erases the pre-print drift). If the readout
slips past today's close, roll exit to the next session (2026-07-14). **Confidence: ~55%.**

### BEAR (sonnet)
Stand aside — no new directional position ahead of the print. Independent research
surfaced the actual trial facts absent from the dossier: Part B is **open-label,
single-arm, n=33, no placebo control**. Part A (the only real precedent) showed a **16%
mean SALT reduction vs 2% placebo at week 24, p=0.045** (barely clears significance),
with only **9-14% hitting SALT<=20 vs 0% placebo** — materially weaker than approved
competitors: ritlecitinib/Litfulo (~23% SALT<=20 at week 24) and baricitinib/Olumiant
(mid-30s% at week 36). An n=33 open-label design produces wide confidence intervals, not
a crisp tradable signal, and lacks a placebo comparator to adjust against alopecia
areata's known spontaneous-remission rate. Reads the pre-print +4% run-up in a low-float,
illiquid name as noise/chop, not informed money — meaning longs now are chasing.
**Action:** No new long; if anything, lean toward fading strength/trimming into the
run-up rather than buying it. **Confidence: ~70%** on "don't chase the long," ~50/50 on
the print's actual direction.
Sources: [Q32 Bio topline announcement (StreetInsider)](https://www.streetinsider.com/PRNewswire/Q32+Bio+to+Report+36-Week+Topline+Results+from+Part+B+of+SIGNAL-AA+Clinical+Trial+of+Bempikibart+in+Alopecia+Areata+on+July+13,+2026/26757357.html),
[Part B enrollment completion (StockTitan)](https://www.stocktitan.net/news/QTTB/q32-bio-announces-completion-of-enrollment-in-part-b-of-signal-aa-sdkggj082nrw.html),
[Part A/Part B OLE dosing (PR Newswire)](https://www.prnewswire.com/news-releases/q32-bio-doses-first-patients-in-both-part-a-open-label-extension-and-part-b-of-signal-aa-phase-2a-trial-evaluating-bempikibart-in-alopecia-areata-302429636.html),
[Part A results at AAD 2025 (Q32 Bio IR)](https://ir.q32bio.com/news-releases/news-release-details/q32-bio-presents-results-signal-aa-part-clinical-trial),
[QTTB analyst forecast (StockAnalysis.com)](https://stockanalysis.com/stocks/qttb/forecast/).

### QUANT (opus)
Reference-class (not company-specific) base rates: small-cap binary biotech topline
readouts are bimodal — roughly +40-100% on a clean win, -50-80% on a miss. Alopecia
areata is a crowded, benchmarked indication with approved JAK inhibitors already on
market; bempikibart's novel non-JAK (IL-7Ra) mechanism has a high bar to clear and skews
reception harsher than the raw endpoint alone. Assumed distribution: 35% positive (+55%),
45% negative (-60%), 20% mixed (-15%). **EV(long) = -10.75%** before costs.
**EV(short) = +10.75%** before costs, but this is illusory — inside the estimation-error
band, dies to hard-to-borrow costs, carries uncapped tail risk on a possible +100% pop,
and loses to information asymmetry (a lone headline vs. market makers/insiders pricing
the straddle). Kelly-sizes to ~0% of book given uncertain probabilities. **Action: PASS
/ NO TRADE**, or at most a defined-risk lottery ticket (small long call/straddle) sized
<=0.25% of book, explicitly labeled a variance bet, not an edge. **Confidence: LOW.**

---

## Round 2 — Rebuttals

### BULL → revised (smaller long, same direction)
Concedes the Part A numbers are genuinely weak and lag Litfulo/Olumiant on the raw
comparison — no rebuttal to the absolute efficacy gap. Counters: (1) Part B's open-label
design is a *durability/extension* readout (36wk vs Part A's 24wk) — the market's
question now is whether the effect deepened and whether safety stayed clean, not a fresh
efficacy test; (2) bempikibart is non-JAK (IL-7Ra) vs. Litfulo/Olumiant's JAK boxed
warnings (VTE, MACE, malignancy) — a clean 36-week safety readout is a real bull argument
the bear's efficacy-only framing doesn't capture; (3) concedes he cannot prove the +4%
drift is informed vs. noise, but argues one-directional drift (not two-way chop) into a
dated catalyst is at least weak-to-moderate evidence, which is why size stays modest.
**Revised:** still long QTTB, but cuts size materially vs. Round 1; same entry
(2026-07-13T13:30Z), same stop (~$365), same exit (2026-07-13T20:00Z, or next open if
delayed). Would abandon the thesis on any pre-print signal of a flat/regressing SALT
trend or a new safety signal.

### BEAR → confirmed, shaded more negative
Stance unchanged. On the bull's "informed positioning" claim: a more mundane explanation
fits better — an ~11.4M-float microcap with a known, scheduled binary catalyst reliably
produces pre-print drift from retail momentum, options market-maker delta-hedging as
gamma builds, and short-covering by anyone unwilling to hold a binary short over the
event — none of which requires informed data. No options-implied-move or unusual-volume
confirmation exists to distinguish informed flow from noise. On the quant's EV math:
agrees with the structure and conclusion, but would shade the distribution *more*
negative — roughly 25% clean win / 50% negative-or-ambiguous / 25% mixed-but-sold-off —
because the open-label, n=33, no-placebo design means the market must mentally
placebo-adjust against Part A's own 2% control rate, compounding the disappointment risk
into the "mixed" bucket. Explicitly does **not** think this makes a short attractive
either, agreeing with the quant's structural short-cost concerns (uncapped tail, borrow
cost, MM information asymmetry). **Final:** stand aside pre-print; if any exposure at
all, a small defined-risk fade of a post-print pop, not pre-positioning.
**Confidence: ~70%** on no-chase, ~60% that if forced to pick a direction it skews
negative.

### QUANT → revised (small short, up from pass)
Materially updates on the bear's fundamental data — treats an actual prior trial of the
same drug/mechanism/endpoint as the dominant signal over the Round 1 reference-class
prior. Revised distribution: 20% positive (+40%, dialed down from +55% since even a "win"
likely doesn't clear the Litfulo-level bar) / 45% negative (-60%, unchanged) / 35% mixed
(-25%, worse than Round 1's -15% since open-label ambiguity reads as "unpersuasive," not
neutral). On the pre-print drift: sides with the bear, treats it as noise, assigns it no
directional information value in the EV calc. **Updated EV: Long = -27.75%,
Short = +27.75%** — now calls this a genuine, fundamentally-grounded edge (vs. Round 1's
guesswork) since it's anchored to real Part A data. **Revised action:** a small short
(~1-2% of book, defined-risk/put preferred over naked short to cap the squeeze tail),
same-session entry 2026-07-13 (confirmed valid Monday session) — no longer PASS.
Caveats explicitly retained: borrow cost and squeeze risk on a low-float name are real
and asymmetric; n=33 open-label is still an estimate, not full trial-design detail.
**Confidence: MEDIUM** (up from LOW).

---

## Round 3 — Synthesis (opus)

**Weighing:** Two of three panelists (bear standing aside/leaning negative, quant moving
from pass to a small short) converged toward caution once real fundamental data (Part A's
weak, barely-significant precedent; Part B's open-label/no-placebo design) entered the
debate. The bull only partially conceded — cut size, held direction — and his remaining
case rests on a durability/safety narrative plus a pre-print drift he himself admits he
cannot distinguish from noise.

**Why not long:** The bull conceded the raw efficacy comparison outright. Long EV is
negative under every distribution modeled by the panel (-10.75% Round 1, -27.75% Round
2 after the bear's data updated the quant).

**Why not naked short either:** The quant's own updated short thesis carries real
structural risk he flagged himself — uncapped squeeze tail on a low-float name, hard
borrow cost, and market-maker information asymmetry. A naked pre-print short is the
mirror image of the bull's naked long: both absorb the full binary gap risk uncompensated.

**Hypothesis:** Part A precedent (16% vs 2% placebo, p=0.045, 9-14% vs 0% on SALT<=20) is
materially below the approved-competitor bar (Litfulo ~23% at week 24, Olumiant mid-30s%
at week 36). Part B's open-label, single-arm, n=33 design with no placebo control creates
a negatively-skewed, ambiguity-prone readout. The +4.05% pre-print drift carries no
reliable directional information (no confirming options-implied-move or unusual-volume
data exists). Long EV is negative on every modeled distribution; short EV is positive but
partly illusory once squeeze-tail, borrow cost, and information asymmetry are priced in.
**Direction: none (bearish lean). Confidence: 63.**

**Plan:** QTTB, action: no-trade. No pre-print entry in either direction. Sanctioned
contingency only: a small (<=1% of book), defined-risk fade of an efficacy-unsupported
post-print pop within the 2026-07-13T13:30Z-20:00Z session, hard stop above the
post-print high — otherwise stand aside entirely. Expected profit: 0% (no position taken).

**Dissent (strongest unresolved disagreement):** Does the +4.05% pre-print drift encode
informed positioning (bull) or is it directionless noise from retail momentum,
options-MM delta-hedging, and short-covering (bear + quant)? No confirming microstructure
evidence exists in the dossier to settle it — this is the pivotal post-mortem question:
if the print is positive, the drift was the tell and the caution call was wrong; if
negative/ambiguous, it was noise. Secondary unresolved fork: the bull's
safety-differentiation thesis (non-JAK IL-7Ra vs. JAK boxed warnings) was never rebutted
on the merits by the bear, who countered on efficacy only.
