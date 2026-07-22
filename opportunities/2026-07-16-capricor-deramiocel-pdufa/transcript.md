# Research Debate Transcript — 2026-07-16-capricor-deramiocel-pdufa

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Run date: 2026-07-22.

---

## Round 1 — Independent Research

### Bull

Bull Case: CAPR — Deramiocel PDUFA (Aug 22 2026)

**1. Read of the situation**

This is a binary regulatory catalyst that the market has already de-risked to the downside — which is exactly the setup a catalyst-hunter wants. CAPR stock traded around $30.01 on 2026-06-25 (verified via `toa price CAPR 2026-06-25T15:35:00Z --provider twelvedata` → $30.01) and has since fallen to $19.46 as of 2026-07-21 (verified via `toa price CAPR 2026-07-21T15:35:00Z --provider twelvedata` → $19.46) — a ~35% drawdown. That drop tracks the market's reaction to the FDA scheduling a CTGTAC advisory committee meeting for July 29, 2026 (announced via 8-K, June 26, 2026), which stock commentary attributed to a ~13% single-day decline plus two analyst downgrades in the trailing month. Investors read "extra AdCom step" as incremental regulatory risk.

But the underlying clinical package hasn't gotten worse — it's gotten stronger, and the AdCom is procedural, not a rejection signal. Deramiocel already has:
- A positive pivotal Phase 3 HOPE-3 result: met primary skeletal endpoint (PUL 2.0, p=0.03) and key secondary cardiac endpoint (LVEF%, p=0.04), plus all other type-1-error-controlled secondary endpoints, with ~54% slowing of skeletal muscle disease progression vs. placebo.
- Five-year HOPE-2 open-label extension durability data presented at PPMD 2026.
- FDA's own December 2025 guidance that HOPE-3 results "should be sufficient to support regulatory approval" once the CSR was submitted.
- A BLA resubmission classified as Class 2, with the July 29 AdCom (CTGTAC) issuing a non-binding recommendation ahead of the Aug 22 PDUFA date.

This is a company that already survived a Complete Response Letter (July 2025) and got the FDA to reopen review on the strength of the resubmitted data — a meaningfully de-risked path relative to a first-cycle review. The stock sold off on process news (an AdCom being scheduled), not new negative science. Sell-side has not capitulated — Oppenheimer raised its price target from $15 to $43, with a broader analyst range of $41–$63 (blended ~$53.60) — implying >170% upside from the current ~$19.46 print if approval occurs.

**2. Concrete evidence**

- FDA PDUFA target action date: Aug 22, 2026.
- CTGTAC advisory committee meeting: July 29, 2026 (Capricor 8-K, GlobeNewswire 6/26/2026).
- HOPE-3 topline: primary endpoint PUL 2.0 p=0.03, key secondary LVEF% p=0.04, ~54% slower skeletal disease progression vs. placebo.
- Stock: $30.01 on 2026-06-25 vs. $19.46 on 2026-07-21 (twelvedata via `toa price`), a ~35% pullback.
- Oppenheimer price target raised $15 → $43.
- Consensus/narrative target range $41–$63, blended ~$53.60.
- Prior regulatory history: FDA issued a CRL in July 2025; agency reopened review after resubmission incorporating the HOPE-3 CSR, with FDA guidance (Dec 2025) that HOPE-3 data should support approval.

**3. Proposed action**

Long CAPR common (or calls expiring past Aug 22 to avoid IV crush) at current levels (~$19-20). Hold through the July 29 AdCom as an interim catalyst; reassess/trim immediately after the vote. Small, defined-risk position sizing given the binary nature of the catalyst.

**4. Confidence and what would prove me wrong**

Confidence: Moderate (55-60%). Biggest risk: I have not been able to independently verify the content/tone of the July 29 AdCom (it hasn't happened yet) — FDA convening an AdCom for a resubmitted BLA can signal unresolved reviewer concerns rather than being purely routine. A negative or split panel vote would be the single biggest thing that could prove me wrong.

Sources: Parent Project Muscular Dystrophy (PDUFA date), GlobeNewswire (3/10/2026, 6/26/2026), SEC 8-K Exhibit, TradingView, CGTlive (HOPE-3 data), Capricor PR (HOPE-3 topline, regulatory update), AAII, Benzinga, TipRanks/The Fly (Oppenheimer PT), SimplyWall.st (analyst target narrative).

---

### Bear

Bear Position — CAPR / Deramiocel PDUFA (Aug 22, 2026)

**1. What's priced in / consensus**

CAPR stock has already run hard on de-risking events: HOPE-3 Phase 3 "positive topline" (Dec 2025), FDA lifting the CRL and granting a Class 2 resubmission with an Aug 22, 2026 PDUFA date (Mar 10, 2026), and continued Priority Review Voucher eligibility on approval. Sell-side consensus is "Strong Buy" with an average target near $44.63, some houses trimming to $38 (Roth Capital) — the Street has largely underwritten an approval scenario. CAPR closed around $20.13 as of 2026-07-21 19:30 UTC (verified via `toa price CAPR --provider twelvedata`).

**2. Specific risks that blow up the long thesis**

- **A.** This is Capricor's SECOND bite at the apple — the first rejection (July 9, 2025 CRL) was efficacy-based: "does not meet the statutory requirement for substantial evidence of effectiveness," alongside CMC clarification asks. An efficacy-based CRL is a materially harder bar to clear than a manufacturing-only CRL.
- **B.** FDA scheduled an Advisory Committee for July 29, 2026 — 3.5 weeks BEFORE the PDUFA date, a new, unplanned step. Announced June 26, 2026, the stock dropped ~12% intraday. CEO Linda Marbán stated the company had received no indication of specific concerns and was "surprised," offering only speculative explanations. An unrequested, unexplained adcom scheduled just before a resubmission PDUFA — after an efficacy-based CRL — is a textbook signal the agency wants public/expert cover on a genuinely close call. This event sits inside the trade window and is arguably the real catalyst, not Aug 22.
- **C.** The "positive" HOPE-3 data is thinner than press releases suggest: primary endpoint PUL 2.0 p=0.03, key secondary LVEF p=0.04, n=106. Independent commentary (Seeking Alpha, Alpha Talon) flags marginal p-values (0.029–0.041), small sample size, and framing that leans on composite/subgroup emphasis rather than the pre-specified primary analysis FDA actually adjudicates on.
- **D.** Sector-wide regulatory chill in the DMD cell/gene-therapy space: Sarepta's Elevidys (different modality — AAV gene therapy) has seen three patient deaths since March 2025, a shipment suspension, boxed warning, and label restriction, plus revocation of its platform technology designation — raising the bar for benefit-risk framing.
- **E.** Small-cap, high-beta, event-driven stock — the 12% single-day move on the adcom announcement alone demonstrates binary sensitivity.
- **F.** Dilution risk: cash and marketable securities ~$278.6M as of March 31, 2026 (down from ~$318.1M at Dec 31, 2025), Q1 2026 net loss ~$34M against $9.4M revenue, opex up to $36.8M from $25M YoY — a burn rate assuming on-schedule approval. If Aug 22 slips, runway assumptions get re-rated and capital raises become more likely on worse terms.

**3. What the bull is ignoring**

The bull narrative ("FDA identified no review issues in March, so this is basically a formality") ignores that FDA's posture changed materially between March and June 2026, and nobody at Capricor can explain why. The bull likely treats "met primary endpoint" as equivalent to "cleared the effectiveness bar the CRL demanded," when marginal p-values on a modest-n trial reviewed by an agency that already once said "not enough evidence" is higher-variance than press-release framing implies. The bull is also likely under-weighting the adcom (July 29) as a distinct, earlier, and possibly more informative catalyst than the PDUFA.

**4. Proposed action and confidence**

No long entry ahead of the July 29, 2026 adcom. If forced to take a position, flat or modestly short/short-vol into the adcom given the CRL history + unexplained adcom scheduling + marginal statistics, sized very small given squeeze-risk on a clean positive vote.

Confidence: Low-to-moderate conviction bearish (~55-60%) that the path to Aug 22 is rockier than consensus prices in, primarily driven by the adcom being a genuine unknown-unknown. Not a high-conviction "the drug fails" call.

What would change my mind: FDA briefing documents showing no substantive effectiveness concerns; a strong, non-split adcom vote in favor; clarity from Capricor on why FDA added the adcom; independent statistical re-analysis showing the effect size is stronger than raw p-values suggest.

Sources: GlobeNewswire (3/10/2026, 9/9/2025 CRL response), Parent Project Muscular Dystrophy (CRL), BioSpace ("Capricor thrown for another loop," HOPE-3 topline), GuruFocus (12% decline), Stocktwits, Seeking Alpha ("A Detailed Examination of HOPE-3"), Alpha Talon Substack, Capricor Q1 2026 financial results PR, NeurologyLive (Sarepta Elevidys), CAPR price $20.13 at 2026-07-21T19:30Z (twelvedata).

---

### Quant

QUANT — Round 1 Opening Position: CAPR (Deramiocel PDUFA, Aug 22 2026)

**0. The setup that actually matters (two catalysts, not one)**

This is not a single-event trade. There are two discrete catalysts between now (2026-07-22) and the decision: (1) FDA Advisory Committee — July 29, 2026 (7 days out), the near-term swing factor since a clear panel vote largely pre-determines the outcome; (2) PDUFA target action date — Aug 22, 2026, which is a **Saturday** (verified). Per institutional lessons from CZR post-mortems, a regulatory calendar date must not be mapped directly onto an execution timestamp — the tradeable reaction lands Friday Aug 21 (if FDA acts early) or Monday Aug 24 (if dated on/over the weekend).

**1. Base rates — assumed approval probability**

Case-specific facts: prior CRL (July 2025) was efficacy-driven plus outstanding CMC items — the hard kind to cure. But the efficacy gap was directly addressed: HOPE-3 met its primary endpoint (p=0.03) and key secondary cardiac endpoint (p=0.04), with all type-1-error-controlled secondaries also significant. FDA lifted the CRL, resumed review as Class 2 resubmission, and indicated HOPE-3 should be sufficient to support approval. High unmet need, first-in-class cell therapy, PRV eligibility. Countervailing risk: DMD/rare-disease FDA panels are historically contentious, and cell-therapy CMC is a recurring stumbling block.

Base rates applied: FDA drug adcoms recommend approval ~76% of the time; FDA aligns with the panel vote ~88% of the time (2010–2021 dataset).

Assumed conditional tree: P(positive adcom July 29) = 0.60; P(approval | positive adcom) = 0.85; P(approval | negative/mixed adcom) = 0.35. Unconditional P(approval) = 0.60×0.85 + 0.40×0.35 = 0.51 + 0.14 = ~0.65. Carrying P(approval) ≈ 0.62–0.65, central 0.63.

**2. Expected magnitude**

Reference price: CAPR $19.76 at 2026-07-21 15:59 ET (verified). Market cap ~$1.23B. Short interest reported 9.8%-30% of float (crowded, adds squeeze convexity both directions). Analyst targets bimodal — cluster near $21.50 (range $12–$29) and stale pre-CRL bulls up to ~$53.

Terminal move estimates from ~$19.76: clean approval +85%; second CRL −65%. The straddle-implied move (estimated, not directly observed) is roughly ±55-75%, i.e. the market is pricing close to a coin flip — the edge is entirely in believing approval odds (~63%) exceed the implied (~50%).

**3. Explicit EV (long common, held through both catalysts)**

Four-state decomposition:
- A. Positive adcom → approval: p=0.51, +85%
- B. Positive adcom → CRL: p=0.09, −55%
- C. Negative adcom → eventual approval: p=0.14, −10%
- D. Negative adcom → CRL: p=0.26, −65%

EV_gross = 0.51(85) + 0.09(−55) + 0.14(−10) + 0.26(−65) = 43.35 − 4.95 − 1.40 − 16.90 = +20.1% gross. Costs/slippage ~0.4–0.6% (liquid $1.2B name, no borrow needed). EV_net ≈ +19.5%.

Break-even check: p* = 65/150 = 0.433. Assumed 0.63, a ~20-point cushion. Stress test at pure 50/50: EV = +10% gross — stays positive down to ~43% approval odds.

**4. Does the edge survive costs and timing — confidence**

Costs: comfortably survived. Timing: the real hazard — Saturday PDUFA reaction trades Fri 8/21 or Mon 8/24, and a position opened now eats the July 29 adcom (±40% possible gap) before the PDUFA — a 4-week hold through two binaries.

Variance/sizing: −65% at ~37% probability is a brutal left tail. Fractional-Kelly argues for a small position (~1–2% of book max). Prefer a defined-risk structure (call spread or collar) over naked common given the severe downside.

Confidence: MEDIUM. EV sign is robust (positive down to ~43% approval odds vs. estimated ~63%), but the whole edge rests on adcom/approval probabilities exceeding market-implied, in a disease area where FDA panels have surprised before.

Sources: Parent Project Muscular Dystrophy, GlobeNewswire (3/10/2026), FierceBiotech, BioSpace (HOPE-3 topline), NeurologyLive (HOPE-3 primary endpoint, original CRL), StockTitan (AdCom announcement), NCBI/PMC (adcom-FDA alignment base rate), MarketBeat (analyst targets), StockAnalysis (market cap/statistics), Benzinga (short interest), toa price CAPR 2026-07-21T19:59Z → $19.76.

---

## Round 2 — Rebuttal

### Bull

On the Bear's core claim — that the July 29 AdCom is "unrequested, unexplained" — I grant the observation but reject the inference. Marbán's surprise is consistent with two very different worlds: (a) FDA wants public cover on a genuinely close call, or (b) FDA is following its own post-Sarepta institutional reflex to route any DMD cell/gene therapy through public review regardless of file strength. The Bear treats "unexplained" as evidence of "problem" with no differential evidence discriminating between the two.

On the efficacy-based CRL point: this is the Bear's strongest fact, but the Bear elides that HOPE-3 is the resubmission trial specifically designed to address that CRL, with pre-specified endpoints hit. A second efficacy-based rejection of new confirmatory data is a harder position for FDA to hold than the original CRL was.

On the Quant's numbers: I don't disagree with the arithmetic, I disagree with how it's being buried — an EV of +19.5% with a 43% breakeven against a 63% assumed approval probability is a 20-point margin of safety, unusually favorable for a binary biotech catalyst trade. That should lead the recommendation, not be qualified down. The −65% left tail is a reason to use a defined-risk structure (shrink structure), not a reason to shrink conviction.

**What they got right:** Both Bear and Quant are right that I under-weighted the AdCom as its own catalyst rather than a mere staging post — I now agree it should be modeled as a discrete, high-variance event with its own P&L consequence inside my hold window. I also accept the Quant's disaggregated conditional probabilities as a more rigorous replacement for my vague confidence range.

**What would change my mind:** A negative or split AdCom vote on July 29 (cuts P(approval) roughly in half per Quant's math) — I'd exit or flip to Bear's flat/small-short stance immediately. FDA briefing documents re-raising the primary pre-specified endpoint concern from the original CRL. Any for-cause/expanded-safety discussion tying Sarepta's Elevidys deaths to Deramiocel's mechanism specifically. A dilutive capital raise announced before Aug 22.

**Updated position:** Still long — the Quant's EV math is the strongest objective evidence in the room. Revising structure/sequencing: treat July 29 as a live decision point; downsize to a small (1-2% book) defined-risk structure (call spread/collar); hard rule — negative/split AdCom vote = exit or flip to flat/small-short before Aug 22, no averaging down on hope. Confidence: ~55% (down slightly from 55-60%), now explicitly conditioned on AdCom outcome.

---

### Bear

**1. Where I disagree.** The Bull treats the AdCom-scheduling sell-off as pure "sentiment noise divorced from science," but that's the weakest link. An FDA-initiated, company-unrequested AdCom for a product the agency's own Dec 2025 guidance said "should be sufficient to support approval" is new information, not noise. The Bull's $15→$43 Oppenheimer re-rate and $41-63 consensus range all predate this scheduling news — stale priors, circular to cite as evidence the AdCom is non-substantive.

On the Quant's inputs: P(positive AdCom) = 0.60 and P(approval | positive AdCom) = 0.85 read like generic historical base rates without conditioning on: (i) the original CRL was efficacy-based — a selected, adverse sub-population of the "generic AdCom" reference class, since this panel specifically relitigates whether the data clear the bar; (ii) the unexplained/unrequested nature of this AdCom is itself informative and should lower P(positive AdCom) further; (iii) the Sarepta Elevidys chill represents a regime shift in the review division's posture, not captured in pre-2025 base rates.

Combining these, I'd put P(positive AdCom) closer to 0.40-0.50, and P(approval | positive AdCom) closer to 0.70-0.75. That moves the Quant's unconditional P(approval) from ~0.63 down toward ~0.30-0.38 — below the Quant's own 43% break-even, flipping the framework's conclusion to negative EV using their identical structure.

**2. What they got right.** The Quant's EV structure — not their inputs — is the most useful contribution: framing this as an asymmetric four-state payoff with an explicit break-even threshold sharpens my case rather than weakening it. I credit the Bull that the last hard scientific data point (HOPE-3 topline) was indeed positive — my thesis rests on regulatory-process risk, not a claim the science got worse.

**3. What would change my mind.** Any leaked/reported detail on why FDA scheduled the AdCom suggesting it's procedural/manufacturing rather than efficacy-related. A pre-AdCom briefing document showing FDA staff analysis is neutral-to-positive on pre-specified primary endpoints. Evidence the AdCom was industry/advocacy-driven rather than agency-driven. A clean, decisive AdCom vote (e.g. 12-2 or better).

**4. Updated position.** Confidence: unchanged to slightly more bearish, 60-65% (up from 55-60%). Still no long entry ahead of July 29. Goes further than Round 1: if participating at all, a small defined-risk short or put-based structure into July 29 (limited premium risk vs. a plausible -30-40% single-day drop on negative/split vote), sized like the Quant's 1-2% but directionally inverted. Absent a defined-risk structure, flat remains the default.

---

### Quant

**1. Does the bear change my inputs? Yes — mostly the adcom node, not the conditional.**

Taking the Bear's points one at a time:
- **Efficacy-based CRL:** the strongest point, conceded. But a CTGTAC panel votes precisely on the efficacy/benefit-risk question. A *positive* vote is unusually informative because it directly addresses the exact deficiency that generated the CRL. This should lower P(positive adcom) and crush P(approval | negative adcom), but only modestly dent P(approval | positive adcom). Moving P(app|pos) 0.85 → 0.80, P(app|neg) 0.35 → 0.22.
- **Unrequested/unexplained adcom + "surprised" CEO:** I buy this as a negative signal on the vote. Main driver for cutting P(positive adcom) 0.60 → 0.50.
- **Marginal p-values, composite/subgroup framing:** reinforces the same cut, keeping P(positive adcom) at 0.50 or lower.

I do NOT accept the Bear's "consensus already prices approval" claim at face value — in direct tension with a stock that just fell 35%.

**2. Does the bull add anything quantitative?** Only on magnitude, not probability. Analyst PTs are conditional-on-approval price objectives, not odds — they validate/slightly understate my up-leg (+85% terminal maps to ~$36, below the $41-63 consensus range). The 35% drawdown from $30→$19.5 means the market is NOT pricing 65% optimism, undercutting the Bear's "already priced in" claim; also flags the CRL-tail may be partly pre-loaded (realized left tail closer to -50% than -65%, not formally rebased).

**3. Re-running the numbers — bear-adjusted set.** New assumptions: P(positive adcom)=0.50, P(approval|positive adcom)=0.80, P(approval|negative adcom)=0.22. Unconditional P(approval) = 0.50×0.80 + 0.50×0.22 = 0.525 (down from 0.63; well above Bear's 0.30-0.38 — I do not fully accept the Bear's stacking of all three factors onto the same parameter as this risks double-counting).

Break-even unchanged at 43.3%. EV_gross = 0.525×85 − 0.475×65 = +13.75%; EV_net ≈ +13.3%. Cushion narrows from ~20 points to ~9 points.

Stress test (P(pos)=0.48, P(app|pos)=0.78, P(app|neg)=0.20 → P(approval)=0.478): EV_net ≈ +6.2%. Cushion ~4.5 points — sign stays positive even under punitive stress.

Kelly: full Kelly ~16% at p=0.525 (~10% at stress case); recommend staying well below quarter-Kelly given binary variance, parameter uncertainty, and the fat left tail.

**4. Updated position.** Still long, still positive EV, but confidence downgraded MEDIUM → MEDIUM-LOW. Size trimmed to 1-1.5% of book (from 1-2%). Defined-risk structure now non-negotiable (call spread/collar). Adopts a STAGED entry: roughly half intended size now, remainder contingent on a positive July 29 AdCom vote — buying confirmation lowers EV/dollar but sharply raises risk-adjusted return, since a positive vote lifts P(approval) from 0.525 toward ~0.80. Execution reminder stands: Aug 22 PDUFA is a Saturday — any hold-to-decision exit rolls to Fri 8/21 or Mon 8/24, never the calendar date itself.

---

## Round 3 — Synthesis

### hypothesis

**Statement:** The ~35% drawdown from $30 to ~$19.5 has repriced CAPR from a "priced-for-approval" name to something closer to a coin-flip, while the underlying HOPE-3 dataset (pre-specified primary PUL 2.0 p=0.03, secondary LVEF p=0.04) remains a genuine positive data point that neither bear nor quant disputes on the science. The trade is a positive-expected-value, event-driven long: the quant's bear-adjusted framework still clears its own break-even with a modest cushion (unconditional P(approval) ≈ 0.50–0.525 vs a 43.3% break-even; EV_net ≈ +6% to +13%). The edge is thin and rests on parameter estimates that are honestly contested, so this is a small, defined-risk, staged expression — not a conviction long.

**Direction:** long
**Confidence:** 54

(Rationale: I weight the quant's decomposition as the correct lens and accept its rejection of the bear's parameter-stacking as partial double-counting — the same three factors cannot each be loaded onto every node independently. But the bear is right that an agency-initiated, unrequested AdCom for a file the FDA's own Dec-2025 guidance called sufficient is information, not noise, and it plausibly pulls P(positive AdCom) toward 0.45–0.50. Net: EV is positive but the margin of safety is single-digit points, not the 20 the bull leaned on. That maps to a confidence just above a coin-flip.)

### plan

Single cleanest actionable variant = a two-leg staged long anchored to the AdCom node, kept as one plan since both legs share one direction, one instrument thesis, and one hard stop; the contingency is a size trigger, not a direction change.

- **ticker:** CAPR
- **action:** buy (defined-risk structure — call spread or stock-plus-protective-put collar, NOT naked common, to cap the −50%/−65% left tail)
- **entry:**
  - time: 2026-07-22T14:00:00Z (initial leg — ~half of intended size, ~0.75% of book)
  - target_price: USD 19.60
  - *Contingent second leg (~0.75% of book) added at 2026-07-30T14:00:00Z ONLY if the July 29 AdCom returns a clearly positive panel vote; a positive vote lifts P(approval) from ~0.525 toward ~0.80. Total capped at ~1.5% of book.*
- **exit:**
  - time: 2026-08-24T14:00:00Z (Aug 22 PDUFA is a Saturday — per the CZR post-mortem lesson, do not map the calendar date to an execution timestamp; the tradeable reaction lands Fri 2026-08-21 or Mon 2026-08-24. Monday's open captures the decision regardless of when FDA acts.)
  - target_price: USD 22.30 (EV-weighted expectation, ~+13%; the real outcome distribution is bimodal — ~$36 on clean approval vs ~$7–10 on a second CRL — not a point landing near $22)
- **expected_profit_pct:** +13% (bear-adjusted base case; degrades to ~+6% under punitive stress; turns negative if the bear's P(approval) ≈ 0.30–0.38 is correct)

**Hard rule (non-negotiable):** a negative or split July 29 AdCom vote = exit the initial leg / flip to flat before Aug 22 and do NOT deploy the second leg or average down into the PDUFA. The AdCom is a discrete decision node inside the hold window, not a waypoint.

### dissent

The strongest unresolved disagreement is the value of two probability inputs feeding P(approval): P(positive AdCom) and P(approval | positive AdCom) — and, underneath them, whether the efficacy-based CRL + unrequested-AdCom + Sarepta-chill factors are three independent negatives or largely one correlated negative counted three times.

- The bear stacks all three and lands at P(approval) ≈ 0.30–0.38 — below the quant's own 43.3% break-even, flipping the framework's conclusion to negative EV and arguing for flat or a small defined-risk short.
- The quant revises to P(positive AdCom) = 0.50 and P(approval | positive AdCom) = 0.80, yielding P(approval) ≈ 0.525, and explicitly rejects the bear's combined math as double-counting the same adverse signal across multiple nodes.

I lean toward the quant's ~0.50–0.525, which is why the synthesis is (barely) long. The decisive reason: a CTGTAC panel votes precisely on the efficacy question the original CRL turned on, so a positive vote is unusually dispositive of exactly the bear's strongest fact — that structural feature genuinely dampens how far the efficacy-CRL history can depress P(approval | positive AdCom). The bear is also right that the analyst targets are stale (pre-AdCom) and that "something changed FDA's calculus between Dec 2025 and July 2026."

What remains genuinely unresolved (preserved for post-mortem): neither side has the one piece of differential evidence that would break the tie — the FDA briefing document / AdCom materials, which had not published as of this debate. The entire bull-vs-bear gap reduces to whether the unrequested AdCom reflects (a) a post-Sarepta institutional reflex to route all DMD cell/gene therapies through public review regardless of file strength (bull/quant reading, EV-positive), or (b) undisclosed internal reviewer disagreement the sponsor wasn't told about (bear reading, EV-negative). If this trade loses, the most likely reason is that (b) was true and P(positive AdCom) was really ~0.40 or below — i.e. the market's "surprise AdCom = bad omen" instinct was signal, and the quant's rejection of the bear's stacking was itself the error.
