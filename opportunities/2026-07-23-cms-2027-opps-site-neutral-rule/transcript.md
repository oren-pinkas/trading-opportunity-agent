# Debate transcript — 2026-07-23-cms-2027-opps-site-neutral-rule

Strategy: debate-three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: CMS's proposed CY2027 Hospital OPPS rule expands site-neutral payment policy,
cutting Medicare hospital-outpatient reimbursement; dossier names SGRY (Surgery
Partners) and UHS (Universal Health Services), impact_window 2026-09-30. Source: CMS
Issues Sweeping CY 2027 Hospital OPPS/ASC Proposed Rule — Holland & Knight
(https://www.hklaw.com/en/insights/publications/2026/07/cms-issues-sweeping-cy-2027-hospital-opps),
accessed 2026-07-23T22:07:07Z.

Institutional lessons injected (regulatory-type, via `toa lessons-relevant --type
regulatory --tickers SGRY,UHS`): validate entry/exit fall on open trading sessions;
never map a legal/calendar date directly onto an execution timestamp; SNR below ~0.15
on a linear-EV fade is not durable edge; an entry fill outside the planned band is an
early falsification signal; test-query the real price provider before finalizing a
plan; exhaust a fallback ladder before recording market-data-unavailable; size
fill-precision to the size of the edge.

---

## Round 1 — Independent research

### BULL (opening position)

CMS's CY2027 OPPS/ASC proposed rule (released 2026-07-02) proposes a 2.4% base
payment-rate increase for hospital outpatient services overall, and separately expands
site-neutral payment narrowly — adding "imaging without contrast" services furnished
in off-campus provider-based departments, reimbursed at 40% of the OPPS rate
(non-budget-neutral), projected ~USD 260M in Medicare savings. This is not a broad cut
to surgical procedures or ASC facility fees — ASC rates sit on a separate, lower CMS
fee schedule untouched by this rule. The dossier's framing ("pressuring off-campus and
ASC-heavy providers") overstates the read-through to a pure-play ASC operator like
SGRY.

Comment period runs through 2026-08-31; final rule typically drops ~November 1 for a
2027-01-01 effective date. Initial tape reaction: UHS reported up ~5.3% on release day
(2.4% base increase read as the dominant story), fading back to roughly flat three
weeks later. Priced via `toa price --provider twelvedata`: SGRY 2026-07-02 15:00Z =
USD 16.95 → 2026-07-24 15:00Z = USD 16.10 (≈ -5.0%); UHS 2026-07-02 15:00Z = USD 158.82
→ 2026-07-24 15:00Z = USD 159.73 (≈ +0.6%). SGRY's drift looks like a mispricing: a
~5% drawdown in a name whose core revenue (ASC facility fees) isn't the rule's target,
during a comment period that doesn't even close for five more weeks. Prior
site-neutral proposals (CY2019 clinic-visit, drug-administration) produced only
modest, short-lived reactions in HOPD-heavy names, absorbed via payer-mix
diversification — no precedent for a durable ASC-operator selloff.

**Proposed action:** LONG SGRY. Entry ~2026-07-27 (next valid session,
14:30–15:00 UTC). Exit ~2026-09-30 19:30–20:00 UTC (tied to dossier impact_window).
**Confidence: ~35%** (moderate-low — thin S/N, biggest evidence gap is SGRY's exact
off-campus billing mix, unverified).

### BEAR (opening position)

The naive "short SGRY/UHS on site-neutral cuts" trade conflates proposed with
finalized policy, and may have SGRY's direction backwards. Comment period closes ~Sept
(the dossier's 2026-09-30 is the comment-period close, not a decision point — no vote,
no binding action). Site-neutral expansion is not new information: MedPAC/CMS have
pushed this direction since the Bipartisan Budget Act of 2015 grandfathered
pre-existing off-campus HOPDs, recommended in nearly every MedPAC annual report since
2016 — a proposed-rule reiteration of a well-telegraphed direction is close to zero
incremental information. Litigation precedent (*AHA v. Azar*, CY2019 clinic-visit
expansion; CMS ultimately prevailed at the D.C. Circuit in 2020, but only after a
multi-year fight) means hospitals will sue again, guaranteeing a drawn-out process
rather than a clean near-term cut.

**Ticker/exposure mismatch — the biggest hole:** SGRY is overwhelmingly an ASC
operator, not an off-campus HOPD operator. Site-neutral policy cuts HOPD reimbursement
down toward physician-office/ASC-equivalent rates — narrowing the HOPD premium
mechanically makes ASCs more cost-competitive, pushing volume toward ASCs, not away.
A short on SGRY may have the sign backwards; SGRY could be a relative beneficiary of
the gap closing. UHS is a diversified acute-care and behavioral-health operator
(~half revenue behavioral health, largely inpatient/residential, entirely outside
OPPS/HOPD site-neutral policy); its off-campus HOPD footprint is a fraction of total
revenue — diluted dollar sensitivity. The two tickers chosen look like a generic
"hospital-adjacent names" screen rather than a rule-specific exposure map.

**What would flip this:** rule watered down/narrowed during comment period (likely,
given lobbying and historical CMS pattern); AHA/state hospital-association suit
post-finalization (near-certain if the final rule meaningfully expands cuts);
congressional intervention; no differential stock reaction vs. peers on the actual
publication day (direct evidence of already-priced-in); analyst confirmation that
site-neutral narrowing is ASC-volume-accretive for SGRY.

**Confidence in a tradeable bearish thesis: ~15-20%.** Default: no-trade/neutral on
both names.

### QUANT (opening position)

**Verdict: NO TRADE.** Comment-period close is a calendar artifact, not a
price-forming event. Base rates: proposed-rule release ~25-40% P(rule-attributable
>2σ move); comment-period close ~3-6%; final-rule release ~35-50%. The 3-6% figure is
not above SGRY's unconditional base rate (SGRY prints >3% moves on ~30% of all days
anyway) — zero incremental directional information from conditioning on Sept 30.
Dossier is also 3+ days stale as a fresh catalyst; whatever repricing the July 23
headline caused is already in the tape (priced SGRY USD 15.16, UHS USD 148.95 at
2026-07-23T14:30Z via twelvedata).

**Exposure:** UHS revenue-at-risk estimated ~0.2-0.6% of total revenue (behavioral
health, ~half of revenue, sits under IPF PPS entirely outside OPPS; acute-care Medicare
FFS outpatient is a modest slice; UHS runs comparatively few off-campus PBDs) — real
but not a thesis. SGRY likely the wrong direction: ASCs are reimbursed under a separate
ASC payment system (Addenda AA/BB), not OPPS; site-neutral cuts HOPD down toward
PFS/ASC level, narrowing the HOPD-vs-ASC premium — competitively favorable to a
pure-play ASC operator. Unresolved sign ambiguity (untested: does the rule also cut
the ASC conversion factor?) is itself disqualifying for a directional trade.

**EV calc**, short-biased, entry ~2026-09-30, 3-day hold: P(comment close produces a
discrete rule-attributable move) = 0.05; conditional direction split 60% down/40% up;
conditional magnitude SGRY 3.5%, UHS 2.0%; non-event branch (0.95) ≈ -0.15% drift
against a short. SGRY short: EV_gross ≈ +0.035% - 0.1425% = -0.108%; costs (spread +
slippage + borrow) ≈ 0.29%; **EV_net ≈ -0.40%** (worse, -0.6% to -0.8%, if SGRY sign is
inverted). UHS short: EV_net ≈ -0.20%. Breakeven test (SGRY): need p ≥ 41% that a
comment-period close is a discrete rule-driven event; assumed probability is 5% — fails
by an order of magnitude. SNR ≈ 0.006 for both, vs. institutional threshold ~0.15 (25x
below).

**Is Sept 30 the real catalyst?** No. A July 23 publication with a standard 60-day
comment window closes ~Sept 21, not Sept 30 — a second red flag on dossier date
provenance. The real catalyst is the CY2027 OPPS/ASC **final rule**, historically
landing ~Oct 30-Nov 2, 2026, not yet published/dated. Per institutional lesson, a
legal/regulatory calendar date must never be mapped onto an execution timestamp before
it is actually dated.

**Confidence in no-trade call: 85. Confidence in short-as-written: 10. Sizing: 0%.**
Conditions to reopen: firm CY2027 final-rule date; confirmation the proposal cuts the
ASC conversion factor/CPL directly; a quantified revenue-at-risk disclosure >~2% of
revenue from either issuer.

---

## Round 2 — Rebuttal

### BULL rebuttal

Concedes: Sept 30 is not a price-forming catalyst — anchored to a comment-period-close
date without verifying mechanical linkage to price discovery; own process failure.
Concedes the quant's date math (60-day window from July 23 lands ~Sept 21, not
Sept 30 — a legitimate provenance flag). Concedes the real catalyst is the final rule
(~Oct 30-Nov 2), not anything in Q3. Concedes SGRY is more likely a beneficiary than a
victim of a narrower HOPD-ASC spread — arrived at via a different route (overreaction)
than the bear/quant (wrong-sign mechanism), but now prefers the structural framing as
stronger/more falsifiable.

Still tries: if SGRY is a structural beneficiary and the market has treated
"site-neutral" as a blanket negative, that mispricing doesn't need Sept 30 or even the
Nov final rule to close — it could unwind whenever generalist flows catch up, a
different (weaker, harder-to-time) edge than a rule-driven catalyst.

**Revised timing:** drops Sept 30 entirely; would use either a time-based window
(60-90 days, no date dependency) or anchor to the actual final-rule window
(~Oct 30-Nov 2); no strong reason to insist on July 27 entry; drops UHS entirely
(concedes bear/quant's diluted-exposure read).

**Final:** concedes no-trade. Confidence 15%, size 0%. Bar to revisit: confirmation the
~5% SGRY drawdown is attributable to this rule specifically (vs. sector beta or an
unrelated event — not yet isolated), plus evidence of analyst mischaracterization of
SGRY as a site-neutral casualty.

### BEAR rebuttal

Agrees fully with the quant's no-trade verdict; no residual bear case, not defending a
short. Strongest objection to the bull's long-SGRY overreaction thesis: the bull's own
framing is in tension — it says the rule barely touches SGRY, then attributes a 5%
drift to that same rule and treats it as tradeable reversion; the causal link (SGRY's
off-campus billing mix) was never verified, so this is pattern-matching a price chart
to a coincident headline. Three weeks is a long, noisy window for a single ASC-name
move — sector rotation, rates, elective-volume data, or company-specific news could
fully explain it. Even granting the sign-inversion logic, that implies a slow,
multi-month fundamental re-rating, not a 2-month swing timed to an artifact date —
anchoring exit to Sept 30 borrows the same flawed calendar logic already rejected for
the short side.

Confidence in no-trade firms up (does not weaken): two independent reads (bear,
quant) converged on both the timing flaw and the sign flaw without coordinating; the
bull's pivot reuses the panel's own objections as raw material for a different
directional bet rather than surfacing a new, independent information edge — one shaky,
uncaused data point wearing two different trade wrappers.

**Final:** no-trade, confidence 85%, matching the quant. If forced to rank residual
interest: a long-SGRY re-rating thesis is "least-bad" (correct sign, plausible
mechanism) but only as a slow, fundamentals-driven position sized after verifying the
off-campus/ASC billing mix and identifying the actual driver of the 5% move — not a
Sept-30-timed trade.

### QUANT rebuttal

Pulled the actual SGRY tape via `toa price --provider twelvedata` (19:00Z daily
closes). The bull's price data was wrong: SGRY **rose** +1.71% on release day
(07-02: 16.84 → 17.13), continued to a peak on 07-07 (+2.1% cumulative), and only
began declining 07-08 — six calendar days after release, temporally disconnected from
the rule under standard event-study attribution (t=0/t+1). The two largest down-days
are 07-22/07-23, three weeks out. "16.10" (bull's cited recent price) was the 07-20
print, not current; latest is 15.705 — true peak-to-now is -8.96%, not the bull's
stated -5%. UHS verified: 159.73 (07-02) → 155.81 (07-24) = -2.45% (could not retrieve
UHS pre-release prints to confirm the bull's "+5.3% release day" claim). Cross-section
is backwards: UHS (the direct OPPS payee) is roughly flat-to-down while SGRY (minimal
OPPS exposure) is down ~9% — no single coherent rule-driven mechanism explains this;
simplest reading is neither move is rule-driven.

**Statistical significance:** measured realized daily log-return vol 2026-06-24 to
2026-07-24 (n=21): σ_daily 3.78% full sample, 2.60% excluding a suspected bad tick
(07-14) and its rebound (conservative, generous to the bull). Testing the actual
15-day move (07-02→07-24, -8.68% log): t = -0.86 (generous case, p≈0.39), t = -0.59
(full sample, p≈0.55). The bull's own stated -5% is even weaker (t=-0.50, p≈0.62).
For the move to clear 2σ would require annualized vol ≤17.8%; SGRY realizes 41-60%.
Conclusion is robust across the entire feasible vol range, and uses a zero-beta
assumption most favorable to the bull (any market/sector-beta adjustment shrinks the
residual further). Upper bound on the rule-attributable mispricing: total program
savings USD 260M across all OPPS; SGRY market cap ≈ USD 2.0B; even granting SGRY an
absurdly generous 1% capture of the entire savings pool, capitalized at 12x ≈ USD 31M
≈ ~1.5% of market cap — ~6x smaller than the 9% move being attributed to it, and with
the wrong sign by the panel's own mechanism reasoning. Documented short-horizon
reversal is a 1-5 day phenomenon; at a 3-4 week lookback the standard prior is
momentum, not reversal — "it fell over three weeks, buy it" has at best zero
unconditional edge.

**Sept 30 as exit:** inherits the identical flaw as entry (a comment-period close
produces no CMS output — nothing published at the deadline), plus two new problems:
(1) the bull's stated mechanism ("rule is immaterial to SGRY") is logically
self-cancelling with a regulatory-milestone exit — if the rule doesn't matter, no
regulatory event can force a re-rating; (2) the exit sits before the only real event
(final rule ~Oct 30-Nov 2). SGRY historically reports Q2 in the first week of August —
inside the proposed July 27→Sept 30 hold; at measured vol and typical earnings-day
multiples (2-3x), earnings-day distribution is ~±8-12%, making an unhedged earnings
print the dominant variance driver, not the rule.

**Sizing math:** at the bull's own inputs (p=0.35, target +5%), SNR = edge/σ_45d =
1.75%/17.4% = 0.10 — below the 0.15 institutional gate using the bull's own numbers.
At the quant's inputs (P≤10%), SNR = 0.029. After 0.10-0.15% round-trip frictions and
nine weeks of capital lockup, EV_net ≈ -0.15% to -0.30%, before unhedged earnings
variance. No stop/target structure produces positive EV (driftless 45-day EV = 0 at
any symmetric stop/target by construction).

**Final:** NO TRADE, confidence 88 (up from 85). Short-as-written: 6 (down from 10).
Long-SGRY-per-bull: 8. Short-UHS: 5. All sizing 0%. Conditions to reopen: confirmed
final-rule publication date + Federal-Register-verified comment deadline; quantified
SGRY OPPS/off-campus-PBD revenue share; a proper event study vs. a healthcare-facility
peer basket; options-implied vol around the final-rule date; SGRY Q2 report date and
result, outside or hedged against any holding window.

---

## Round 3 — Synthesis

**hypothesis:**
- statement: The CMS CY2027 OPPS proposed rule's site-neutral expansion is not a
  tradable catalyst for SGRY or UHS on the dossier's stated horizon. All three
  personas converged on this via three independently sufficient reasons: (1) no
  price-forming event falls in the window — 2026-09-30 is a comment-period artifact,
  not the final rule (~Oct 30-Nov 2, 2026), which lands after any proposed exit; (2)
  the observed SGRY price action is not attributable to the rule — verified tape shows
  SGRY rose on release day and only began declining six days later, with the
  cross-section (UHS flat-to-down, SGRY down ~9%) backwards from any single coherent
  mechanism; (3) the move is statistically indistinguishable from noise (t = -0.86 to
  -0.59) under any plausible realized-vol assumption, and the maximum rule-attributable
  mispricing under generous assumptions is ~6x smaller than the realized move. The
  bull conceded all three points in Round 2 and dropped UHS entirely.
- direction: none
- confidence: 88 (no-trade). Residual directional confidences: short-SGRY-as-written 6,
  long-SGRY-per-bull 8, short-UHS 5.

**Dossier impact_window (2026-09-30) — explicitly rejected**, on three grounds: (1)
provenance error — a 60-day comment window from a July 23 reference closes ~Sept 21,
not Sept 30; (2) wrong event even if the date were right — comment-period close
carries no payment-rate decision, the decisive event is the final rule (~Oct 30-
Nov 2), outside and after the window; (3) self-cancelling with the bull's own
thesis — if the rule is immaterial to SGRY (the bull's core premise), no regulatory
milestone can force a re-rating. SGRY Q2 earnings likely fall inside the proposed
holding window and would be the dominant unhedged variance driver, not CMS.

**plan:** NO TRADE. No entry, no exit, no target prices. ticker: SGRY (primary), UHS
(dropped by bull in Round 2). action: no-trade. expected_profit_pct: 0.00 (size 0%).
Modelled alternatives were all negative: EV_net short-SGRY ≈ -0.40% to -0.8%,
short-UHS ≈ -0.20%; SNR ≈ 0.006-0.10 depending on whose inputs are used, all below the
0.15 institutional threshold; no stop/target structure produced positive EV.

Conditions to reopen (union of all three personas): confirmed final-rule publication
date; quantified SGRY OPPS/off-campus-HOPD revenue share; a proper event study vs. a
healthcare-facility peer basket isolating the cause of the 07-08-onward drawdown;
options-implied vol to price the event; SGRY Q2 date/result; hard evidence sell-side is
mischaracterizing the rule's mechanism for SGRY.

**dissent:** The strongest unresolved disagreement is the sign, not the size — every
persona ended at no-trade, so the surviving dispute is which direction the rule points
if it ever prices in, and that was never settled with evidence, only reasoning. The
bear (R1) and the bull (R2, conceding) both argued site-neutral expansion narrows the
HOPD-vs-ASC payment premium and is therefore structurally favorable to SGRY — making
the dossier's implied short a sign-inverted trade, and long-SGRY-on-re-rating the
"least-bad residual idea." The quant agreed the sign is "likely inverted" but refused
to underwrite the long either, since no one quantified SGRY's actual OPPS/off-campus
revenue share — the beneficiary claim rests on a mechanism story with no exposure
denominator, and the timing is unbounded. The panel never resolved whether this
dossier is a non-event (the 9% SGRY move is noise plus idiosyncratic/earnings drift) or
a correctly-identified event with the sign flipped (a real structural tailwind the
market and dossier both read backwards) — those two diagnoses imply opposite
corrective actions upstream. If SGRY re-rates upward into or after the final rule, the
no-trade call was correct on timing but the dossier's short-side framing was wrong on
substance — that is the failure worth logging in a future post-mortem. Secondary
unresolved point: the bull's original ~5% SGRY drawdown figure was stale/wrong
(verified true peak-to-now is -8.96%); the panel never established what did cause the
07-08→07-23 decline — the mispricing thesis was abandoned for lack of a verified causal
link, not because a competing cause was identified, so the drawdown remains
unexplained.
