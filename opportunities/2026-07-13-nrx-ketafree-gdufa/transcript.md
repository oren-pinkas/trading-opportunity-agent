# Research Debate Transcript — NRXP / KETAFREE GDUFA decision

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- Opportunity: 2026-07-13-nrx-ketafree-gdufa
- Ticker: NRXP (NRx Pharmaceuticals)
- Event: GDUFA target action date 2026-07-29 for KETAFREE, a preservative-free IV ketamine reformulation
- Reference price: $4.16 as of 2026-07-13T19:59Z — source: TwelveData 1-min bar, `https://api.twelvedata.com/time_series?symbol=NRXP&interval=1min&date=2026-07-13&timezone=UTC`
- Dossier source: "Biotech Catalyst AI Scanner — July WK3", `https://www.biostockinfo.com/biotech-catalyst-ai-scanner-july-wk3/`, accessed 2026-07-13T20:42:00Z
- Strategy: debate-three-round-panel (`config/research.json`: personas bull/bear/quant on sonnet/sonnet/opus; synthesizer on opus)
- Institutional lessons applied (via `toa lessons-relevant --type regulatory --tickers NRXP`):
  1. Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward (source: 2026-07-08-caesars-icahn-fertitta-bidding-war post-mortem).
  2. Never map a corporate/legal calendar date directly onto an execution timestamp — treat it as a catalyst and derive the fill time from the nearest valid trading session (same source).
- Isolation note: each persona was explicitly instructed not to read or reference any other opportunity's dossier in this repository, and to form its view on NRXP/KETAFREE on its own merits alone.
- Tooling note: all three Round 1 personas disclosed they had no working web-search/fetch access in their sandboxed sessions. Their positions below are built from the dossier facts supplied, the reference price, and each persona's general knowledge (training-cutoff, unverified live) of NRx Pharmaceuticals — every unverified claim is flagged inline by the persona itself. This is a material caveat on evidence quality and is preserved here rather than smoothed over.

---

## Round 1 — Independent research

### Bull (sonnet)

**Disclosure on method:** No web-search or fetch tool was available. Everything beyond the two facts supplied in the prompt (reference price $4.16 on 2026-07-13, GDUFA target date 2026-07-29) is drawn from general training knowledge of NRx Pharmaceuticals through knowledge cutoff (Jan 2026), not live verification. Flagged every number that could not be independently confirmed.

**The setup.** NRXP is a sub-$5 microcap biopharma (formerly NeuroRx) with a well-documented history of FDA friction on its lead CNS asset (NRX-101, D-cycloserine/lurasidone for suicidal bipolar depression — multiple delays, a Refuse-to-File-type episode, a Nasdaq-compliance reverse split). KETAFREE is functionally different: a preservative-free reformulation of an already-approved active (ketamine hydrochloride injection, minus benzethonium chloride), routed through the ANDA/GDUFA pathway rather than PDUFA/NCE review. A reformulation of a long-approved molecule carries a materially lower clinical/safety evidentiary bar than a novel chemical entity. It addresses a recognized U.S. injectable-drug shortage (preservative-free ketamine flagged as supply-constrained for hospital/surgical and depression-clinic use), giving FDA incentive to clear it. This is the kind of asymmetric, low-market-cap, binary-date setup that catalyst-scanner flow (the dossier's own source) tends to pre-position ahead of — thin float, retail attention, hard date.

**Evidence and caveats.**
- Reference price/liquidity anchor: $4.16 as of 2026-07-13T19:59Z (TwelveData).
- Regulatory track record nuance: NRx's delays historically hit its novel CNS candidate; KETAFREE's ANDA/reformulation pathway is structurally different and generally faster. Cannot confirm from memory whether NRx has had prior ANDA-specific CRLs on this application — flagged as a gap to close before sizing.
- Dilution/cash risk: NRx has a history of ATM facilities and dilutive raises tied to going-concern disclosures; no verified current cash runway/share count/burn rate for mid-2026 — flagged for verification. A same-week dilutive raise on good news is a common playbook and could cap or reverse a post-approval pop.
- Options liquidity/short interest/analyst coverage: no verified current data; prior is thin, wide-spread options given the sub-$5 microcap size — needs confirmation before any options structure.
- Catalyst-date mechanics: GDUFA goal dates are user-fee commitment targets, not statutory deadlines, and slip routinely — higher-than-base-rate odds of delay given NRx's overall slippage pattern.
- Calendar check (applying lesson 1): 2026-07-29 is a Tuesday — [bull's own note: verify] a normal trading session, not a weekend/holiday. No rollover needed for the date itself; rollover risk is on the decision slipping past 07-29.

**Proposed action.** Long via common stock (not options, absent confirmed liquid strikes). Small starter position, capped at 1-2% of a risk book, given unverified cash/dilution risk, NRx's regulatory-slippage history, and binary gap risk a stop-loss can't protect against overnight. Entry: scale in over 2026-07-27 and 2026-07-28 rather than chasing the morning of the 29th. Exit: execute at the session open if a decision hits before the open; if it hits after-hours on 07-29 or late in the session, the exit/re-entry rolls to the next open session, 2026-07-30. On approval: ride momentum with a trailing stop over 3-5 sessions, watching for an opportunistic secondary/ATM raise that could cap the move. On CRL/delay: exit promptly, no averaging down.

**Confidence: medium.** High confidence the event moves the stock materially either way; lower confidence on direction. Would strengthen: no prior CRL/RTR on this ANDA, confirmed cash runway past 07-29, confirmed options liquidity, a sell-side note modeling approval probability. Would weaken/kill: a confirmed prior FDA deficiency letter specific to KETAFREE, a cash runway inside 1-2 months, confirmed illiquid options, any sign the GDUFA date has already informally slipped.

---

### Bear (sonnet)

**Tooling disclosure:** No working internet access in this session (network calls blocked). Everything below is either drawn from the dossier/price data supplied or training-data knowledge of NRx Pharmaceuticals' disclosed history (~Jan 2026 cutoff), flagged where it applies. Anything from H1 2026 forward could not be verified and is treated as an open information gap.

**Read of the situation.** GDUFA — not PDUFA — applies to ANDAs (generics), a meaningfully different animal than a novel-drug approval decision. GDUFA target action dates are performance-goal dates, not statutory deadlines, and slip routinely without a formal market-disclosure convention. Generic/ANDA review cycles commonly require multiple rounds; sterile injectables (preservative-free IV ketamine is a parenteral, aseptically-manufactured product) face a materially higher CMC/facility bar than an oral generic — exactly the category where site-inspection findings most often cause delay. Even in the best case, this is a generic approval, not a novel-therapy approval — commercial value hinges on captive supply for NRx's own clinic network, not standalone blockbuster economics; the market may be pricing a narrow internal-supply-chain catalyst as if it were a binary blockbuster event.

**Base rates.** Industry-wide first-cycle NDA approval runs roughly 60-70% (varies by source/year), but ANDA-specific complete-response/refuse-to-approve rates on first cycle are non-trivial, and multi-cycle review is the norm for complex sterile injectables. For a filer with NRx's specific track record, weight the base rate below industry average, not above it.

**NRx's own regulatory track record — a red flag, not a green light.** Per disclosures through training cutoff (not re-verified today): NRx's lead CNS candidate NRX-101 suffered a major setback when FDA indicated existing RECONNECT trial data was insufficient for approval and additional adequate/well-controlled trials would be needed — a disclosure that hit the stock hard. A company with this track record of over-promising regulatory outcomes needs to explain why this time is different, not just assert it.

**Financial distress signals (flagged as needing SEC/EDGAR re-verification, but directionally important):**
- Going-concern language across multiple prior annual reports, driven by continued net losses and reliance on external financing rather than product revenue. If still present, an approval-driven pop is a near-certain trigger for immediate dilutive financing.
- History of ATM programs and warrant exercises materially growing share count over time — mechanically, even good news is a high-probability trigger for the company to sell into the rally, capping upside ("sell the news").
- At least one prior reverse stock split (recalled circa 2023) specifically to regain Nasdaq minimum-bid-price compliance — a hallmark of chronic sub-$1-then-split-then-drift-lower value destruction. Needs current confirmation of listing-compliance status.
- Liquidity/volatility profile: low-priced, thinly-capitalized, high-beta name that has historically moved 20-50%+ intraday around binary news — cuts both ways, but matters for execution (wide spreads, thin depth, gaps through stops).

**Open gaps flagged:** current cash runway in months, most recent ATM capacity, any 2026 Nasdaq deficiency notices, additional reverse splits/dilutive raises since training cutoff, and — most importantly — any interim signal (inspection finding, Information Request, Type II GDUFA meeting outcome) about KETAFREE specifically ahead of 07-29. Absence of disclosed bad news for a company with this disclosure track record is weak evidence of a clean outcome, not strong evidence of one.

**Specific risks and mechanics.**
1. CRL-equivalent/Information Request (delay, not outright rejection) — could also simply manifest as no news at all on the date, which for a long holding into a binary date is a loss of optionality even without a negative headline.
2. Facility/inspection-driven delay — sterile injectable manufacturing is inspection-sensitive; any open Form 483/Warning Letter at the contract manufacturer (unverified) can push the ANDA past target regardless of clinical/BE package quality.
3. "Sell the news" via immediate dilution, given NRx's historical financing pattern and thin float/nervous retail-heavy holder base.
4. Narrow commercial magnitude mispriced either direction — actual stock reaction may be driven more by momentum/short-covering/retail flow than fundamental approval economics, favoring staying out or very small sizing over a directional fundamentals bet.
5. Execution/timing risk (applying lesson 2): 2026-07-29 is a Wednesday [bear's own note], a valid trading session, but because the GDUFA date is a target not a deadline, any plan must build in the real possibility of slippage past 07-29 with no same-day resolution; exits should tie to the actual news release and the next open session following it, not rigidly to the calendar date.

**Confidence: moderate-to-high on process/financing risk, lower on directional certainty of the FDA outcome itself.** Highest-conviction claim: the market may be treating a generic/ANDA GDUFA date with the drama of a novel-drug PDUFA date when commercial magnitude is smaller and more uncertain, and NRx's disclosed history (going concern, dilution, reverse split, a prior major regulatory setback) should lower priors on a clean, value-accretive outcome even if the ANDA is technically approved. Would change mind: confirmed cash runway >12 months without needing a raise around the catalyst; no open Form 483/Warning Letter at the relevant site; confirmed commercial offtake agreements raising the true economic magnitude; a clean recent Nasdaq compliance status; confirmation this is a first ANDA cycle with no prior CMC-flagging correspondence.

---

### Quant (opus)

**Tooling disclosure:** Bash/network access denied in this sandbox; numbers rest on regulatory base-rate literature as of Jan 2026 knowledge cutoff, flagged for live verification. No other opportunity's dossier was read.

**The single most important unresolved fact.** GDUFA is the pathway for ANDAs (generic copies); PDUFA governs NDAs/BLAs (branded/505(b)(2)). The dossier calls this a GDUFA action, yet "KETAFREE" is a branded product name for a reformulation of an already-approved molecule. These two readings imply very different base rates and could not be resolved without the application docket — priced as a blend with explicit sensitivity, since approval probability is the entire trade.

**Base rates.**
- ANDA/GDUFA first-cycle approval is low: historically only ~10-15% of ANDAs approved on first cycle; median generic takes 3-4 cycles; the goal-date action is usually a Complete Response/deficiency letter, not an approval (FDA GDUFA performance reports/OGD metrics, pre-2024).
- PDUFA/NDA first-cycle approval is higher: ~85-90% for large-sponsor standard NDAs, materially lower (~55-70%) for first-time small/microcap sponsors.
- Mitigant specific to KETAFREE: reformulation of a well-characterized, already-approved active — efficacy/clinical risk near nil, residual risk is CMC/manufacturing and pathway classification. Reformulations of known molecules approve at meaningfully higher rates than novel entities, pulling the estimate up from the naive ANDA first-cycle base rate.
- Net central: **P(approval near date) = 35%**, honest band **25-50%** depending on ANDA-vs-505(b)(2) classification and prior-CRL history.
- FDA acts by its goal date ~80-90% of the time (PDUFA VI/VII; GDUFA similar), but "acts" ≠ "approves." Most common slip: ~3-month extension (~10-15% of the time); less often the date passes with silence. ~15-25% chance the date is not a clean binary resolution.

**Expected value (long stock from $4.16).** Outcome tree: Approval 35% / +55%; CRL/rejection 45% / -45%; Delay/no-clean-action 20% / -10%. Gross EV = 0.35(55) + 0.45(-45) + 0.20(-10) = +19.25 - 20.25 - 2.0 = **-3.0%**. Breakeven P(approval) ≈ **37%**. Central estimate (35%) sits just below breakeven. Costs/slippage: NRXP near $4 likely trades with modest quoted spread (~0.2-0.5%) but real event-day execution risk (~1-2% round-trip friction). **Net EV ≈ -4% to -5%.** Sensitivity: at P=45% (optimistic reformulation read), net ~+6% (real edge); at P=25% (ANDA first-cycle read), net ~-16% (clearly avoid). The decision lives in a 20-point probability band not resolvable from available information.

**Timing/execution.** On central numbers, the edge does not survive costs for a naive buy-and-hold long. Do not establish a full position now — 16 days of holding exposes to unrelated drift/dilution risk, and microcap biotech commonly runs up into the date and sells the news. If entering at all, use defined risk (hard stop, or a debit structure if options are liquid — unverified). A naked long into a 45%-CRL scenario with -45% downside is poor risk geometry.

**Date validation (applying lessons 1 and 2).** 2026-07-29 is a **Wednesday** — a valid US equity session, no known market holiday. This is a catalyst date, not a fill timestamp: FDA action often posts after the close, so the tradeable move may print 7/29 or 7/30. Plan the exit for 7/30 if action lands after hours. No weekend/holiday roll needed for either date; do not hard-code a fill to 7/29 09:30 as if the decision is guaranteed at the open.

**Confidence: low-to-moderate.** Central read is a slightly-negative-EV coin flip → default stance: pass, or a token ≤1-2% speculative position sized by half-Kelly on a thin edge (rounds to ~0). Would change numbers, in order of impact: (1) pathway confirmation (ANDA vs 505(b)(2)); (2) prior-CRL/cycle history; (3) FDA CMC feedback/inspection status for the manufacturing site; (4) options-implied move, if liquid; (5) live microstructure (bid-ask, ADV, pending dilutive-raise signals).

---

## Round 2 — Rebuttal

### Bull rebuttal (sonnet)

**Disagreements.** Bear's "sell the news via dilution" argues for a *shorter holding period*, not for staying out — a dilutive raise typically follows a pop, it doesn't erase it intraday; if flat by 7/30-7/31 regardless of outcome, dilution risk is a post-holding-period problem. Quant's -45% CRL magnitude may be imported from novel-drug precedent rather than CMC/facility-failure precedent — GDUFA generic reviews don't carry the same binary "no efficacy signal" risk that hit NRX-101; failure modes here are almost entirely CMC/facility/manufacturing (Bear's own point), which historically produce narrower stock reactions ("fixable in 6-12 months" vs. "drug doesn't work"). If Quant re-runs with -20% to -30% instead of -45%, EV moves from clearly negative toward roughly flat-to-slightly-positive at Quant's own 35% approval probability. Concession: Bull's own pathway assumption is equally unverified — both sides lean on the same unresolved fact to justify opposite-leaning EV estimates; that ambiguity, not the models, is the actual crux.

**Incorporating.** From Bear: shortening intended holding period — scale in pre-catalyst, exit fast on the print regardless of direction, don't hold for a multi-week re-rate; treating facility/CMC risk (not clinical efficacy) as the primary failure mode reframes a negative outcome as more likely delay/Information Request than outright rejection. From Quant: accepting breakeven ≈37-38% as the bar the pathway argument needs to clear; adopting "token position, not full size" discipline pre-resolution of the ANDA-vs-reformulation ambiguity.

**Would change mind.** Confirmed true standard ANDA/GDUFA first-cycle review with a documented prior CRL/Information Request on this product — would flip to Quant's pass or explore Bear's short thesis. Cash runway <2 quarters with no recent shelf/ATM update — treat any pop as un-holdable, cut size or skip. Confirmed prior CRL/major deficiency letter on the KETAFREE ANDA specifically — flips bearish on process risk even liking the shortage-drug logic. Conversely, confirmed reformulation-type ANDA with no prior CRL — would move up in size, the scenario Quant's model most undervalues.

**Updated action.** Pathway verification is now the explicit gating condition before any size increase (first-cycle vs. resubmission, prior CRL/Information Request, recent cash runway/ATM capacity) before 7/27. If confirmed favorable: 2-3% position, 7/27-7/28. If ambiguous/unconfirmed by 7/27 (base case): cap at ≤1-2%, entered 7/28 only. If confirmed unfavorable: stand down, no position. Exit discipline: close within 1 session of the decision — same day into strength if news drops in market hours; at 7/30 open, no later, if after-hours. No holding into a second session waiting for a dilution announcement to resolve.

---

### Bear rebuttal (sonnet)

**Disagreements.** Quant's -45% CRL move is, if anything, too conservative given NRx's actual history — for a going-concern company, a CRL and the forced capital raise that follows (because the CRL kills the runway assumption embedded in the current price) compound: realistic tail closer to **-55% to -65%**, not -45%. Quant's tree likely understates left-tail severity by treating CRL as pure sentiment repricing rather than repricing-plus-financing. Conversely, Quant's approval scenario (+55%) may be overstated net of dilution — this is the core disagreement with Bull's "ride momentum 3-5 sessions" plan, which ignores that management in a going-concern-adjacent position typically raises *into* strength immediately, capping the move well before a trailing stop would trigger; a sharp reversal on a dilution 8-K/S-1 filing could give back most of the gain before the stop triggers in an illiquid small-cap.

**What they got right.** Quant is right the odds are genuinely ambiguous between generic-pathway and reformulation-of-known-molecule reads, and right to center on a 25-50% band rather than a single point — that discipline is the correct response to genuine base-rate uncertainty; the EV math coming out negative-to-flat after costs is the correct sizing signal, and a wider left tail only makes it more negative. Bull is right to flag cash runway, dilution, and options liquidity as explicit disconfirming triggers, and right to commit to no averaging down — that risk-management instinct has no quarrel; it's the clean-multi-day-ride exit assumption that's disputed.

**Active short?** Pushes back partially on Quant's "pass, not a conviction short." There is a case for a small tactical short specifically *into strength on an approval headline* — not shorting the binary event itself (too random, gamma risk real, dangerous against a +55% overnight gap) — but fading the initial pop specifically, sized small (~1% notional), with a defined stop above the post-approval high, on the thesis the dilutive raise follows within days and the market underprices that second leg down for a small-cap with this issuer's history. A distinct trade from "shorting the FDA decision," sized and labeled as such. Absent that specific setup, base case remains stay out pre-decision — binary risk is roughly symmetric in probability but asymmetric in Bear's favor on severity, arguing for avoiding the event risk entirely.

**Would change mind.** Confirmed funded cash runway (12+ months) disclosed before 7/29, removing the "raise is coming regardless of outcome" overhang — biggest single lever toward Bull's momentum-ride thesis. Evidence the ANDA rides a genuinely established RLD bioequivalence pathway with no CMC/facility deficiencies in any prior FDA correspondence — narrows the CRL tail, pulls toward Quant's higher-end 50%. Insider buying or unusual options-market skew showing informed bullish money with tight bid-ask. Any pre-announcement of a completed financing before the decision date, removing the raise-dilutes-the-pop mechanism entirely.

---

### Quant rebuttal (opus)

**On Bear's dilution mechanism.** Accepted and quantified: splits the approval scenario into "clean pop, no near-term raise" (+55%, ~40% probability) vs. "pop-then-dilution-cap" (+25% net after the raise prints, ~60% probability). Blended approval move = 0.40(55) + 0.60(25) = **+37%**, down from +55%. Re-solving breakeven with the +37% pop (delay fixed 20%/-10%): 37p + (0.80-p)(-45) - 2 = 0 → **breakeven ≈ 46%**, up sharply from ~38%. This is the single most important number from Round 2.

**On Bull's reformulation argument.** Partial credit — legitimate on the clinical/pathway axis but double-counted and ignores an orthogonal gate. Approval is a product of two independent gates: (1) clinical/pathway gate (is the molecule/indication acceptable — reformulation of approved ketamine → high, ~70-80%) and (2) CMC/facility-inspection gate (can this sponsor's sterile-injectable manufacturing pass first-cycle — orthogonal to clinical risk, ~50-60% given NRXP is not a scaled manufacturer). P(approval) ≈ 0.75 × 0.55 ≈ **41%** on the pure reformulation read, not Bull's implied ~50% — Bull gets to a high number only by implicitly setting the CMC gate to ~1.0. Shortage pressure raises FDA *motivation*, not FDA *tolerance for CMC defects* — FDA's typical response to a sterile-injectable shortage is delay/CRL with a facility fix, not a wave-through. Bull's clinical-gate point and Bear's CMC-gate point roughly offset; central P does not move toward 45-50%.

**Recomputed EV.** Synthesis-point tree: Approval 33% / +37%, CRL 47% / -45%, Delay 20% / -10%. Gross EV = 0.33(37) + 0.47(-45) + 0.20(-10) = 12.2 - 21.2 - 2.0 = **-11.0%**; net **≈ -12% to -13%** after costs/slippage — worse than Round 1's -3% gross / -4-5% net, specifically because accepting Bear's dilution mechanism caps the only positive branch, which dominates the small probability tweaks. Action does not flip to an outright short despite the negative EV firming: shorting a binary FDA catalyst carries fat right-tail gap risk (the clean-pop branch is +55%+ and un-stoppable overnight); negative EV plus unbounded gap-against ≠ short the stock. Primary: pass/no directional position. If expressing the negative view at all: defined-risk only (small long puts or a put spread), ≤1% NAV, never naked short stock. Explicitly rejects the Bull starter-long as negative-EV.

**Handling the unresolved pathway ambiguity.** Collapses the band to a point via an explicit 50/50 mixture: ANDA/GDUFA read (P=15%, first-cycle base rate nudged up for known molecule) vs. reformulation/505(b)(2) read (P=41%, the two-gate product above, not Bull's 50%). Mixture = 0.50(15) + 0.50(41) = 28%, rounded up to synthesis point **P(approval) = 33%**, band narrowed to **25-45%** (top clipped from 50% to 45% — Bull produced no hard evidence justifying the upper tail). Breakeven now required ≈46%. The gap between the 33% point and the 46% breakeven is the whole story: even the optimistic edge of the narrowed band (45%) sits below breakeven — the ambiguity changes the magnitude of the negative EV, not its sign; the trade is a pass across the entire plausible pathway distribution.

---

## Round 3 — Convergence (synthesizer, opus)

**Hypothesis.**
- Statement: NRXP at $4.16 faces a binary GDUFA decision (target 2026-07-29, a valid Wednesday session) on KETAFREE. The panel converged on P(approval) ≈ 33% (band 25-45%), below the ≈46% breakeven implied once the dilution-cap haircut is applied to the approval payoff (blended to ≈+37% instead of +55%, given NRx's going-concern/reverse-split/ATM history). Net EV of a fresh long ≈ -12% to -13%. The event is genuinely binary and directionally uncertain, so the negative EV does not convert into a conviction short either — gap risk against a naked short is unbounded for a going-concern small-cap.
- Direction: no-trade
- Confidence: 72/100 — high confidence this is not a long; residual 28% reflects the one unverified fact (first-cycle vs. resubmission/pathway status) that could move P(approval) enough to matter, plus the acknowledged three-way split on the CRL magnitude.

**Plan.**
- Ticker: NRXP; Action: no-trade / pass into the catalyst.
- Entry: none. Exit: none. Expected profit: 0% (position avoided — the modeled long's ≈-12% to -13% net EV is the loss avoided, not a target).
- Rationale against the EV math: Quant's final tree (Approval 33%/+37%, CRL 47%/-45%, Delay 20%/-10%) gives gross EV ≈ -11%, net -12% to -13%. The two Round 2 revisions that killed the long are structural, not cosmetic: (a) the dilution-cap split of the approval payoff, and (b) the orthogonal CMC/facility gate Bull implicitly set to 1.0. Even the most optimistic reformulation read the panel would credit tops out at ~41-45%, still under the ~46% breakeven. No version of the surviving numbers makes the long positive-EV.
- Revisit gates (must clear before 2026-07-27): (1) pathway confirmation of a reformulation-of-known-molecule review with a clean prior CMC/inspection record; (2) cash-runway/dilution status confirming no imminent raise; (3) confirmed options liquidity for any defined-risk expression.
- Bear's fade-the-pop idea (~1% notional, tight stop above the post-approval high) is carried forward as a conditional watch-item only — activates only if approval prints and the pop occurs on confirmable strength with liquidity to place a stop; rejected by default otherwise. If the negative view must be expressed pre-decision at all: defined-risk puts only, ≤1% NAV, never naked short stock.
- Timestamp hygiene: 2026-07-29 confirmed Wednesday/valid session; no entry/exit timestamps generated (pass); the only live tactical trigger (the fade) would derive its fill from the nearest valid session after the after-hours/pre-open catalyst — 2026-07-30T13:30:00Z (Thu 09:30 ET) if news posts after the close — never from the calendar date itself.

**Dissent (feeds post-mortem).** The magnitude and direction of the CRL-scenario move (-45% in the synthesis tree) is the largest single term in the EV math (0.47 weight) and the one number all three personas disagree on in different directions: Bull holds -20% to -30% (fixable-manufacturing failure mode, not failed efficacy); Quant holds -45%; Bear holds -55% to -65% (CRL plus forced capital raise compound). At Bull's -25%, gross EV improves by roughly +9 points and the pass thesis weakens materially; at Bear's -60% it worsens and strengthens the case for the defined-risk put/pop-fade. Whichever magnitude actually plays out on 2026-07-29 (or after), the post-mortem should check this term first — it is where the panel's true uncertainty lives and where being wrong would teach the most about pricing going-concern binary events.
