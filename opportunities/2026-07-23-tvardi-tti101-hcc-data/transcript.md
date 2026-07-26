# Research debate transcript — 2026-07-23-tvardi-tti101-hcc-data

Strategy: `three-round-panel` (config/research.json). Personas: bull (sonnet), bear
(sonnet), quant (opus). Synthesizer: opus.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Judged strictly on its own merits — no comparison to any other opportunity.

## Dossier facts at time of debate

- id: 2026-07-23-tvardi-tti101-hcc-data
- Tvardi Therapeutics (TVRD), Phase 1b/2 REVERT LIVER CANCER trial of TTI-101
  (STAT3 inhibitor) in hepatocellular carcinoma; topline data guided "on track"
  for 2H 2026 per company Q1 2026 update.
  Source: https://ir.tvarditherapeutics.com/news-releases/news-release-details/tvardi-therapeutics-announces-first-quarter-2026-results-and
  (accessed 2026-07-23T00:14:58Z)
- dossier impact_window: 2026-09-30 (scout-assigned placeholder, not a
  company-confirmed date)
- Confirmed live price: TVRD $2.60 at 2026-07-23T14:30:00Z (twelvedata 1-min,
  fetched 2026-07-23T14:30Z) — pre-flight verified before the debate began.

## Round 1 — Independent research

### Bull (sonnet)

Long TVRD, small speculative/lottery-ticket sizing, entering now near $2.60,
plan to harvest a pre-catalyst momentum runup and treat the actual 2H 2026 data
print as a hard exit decision point rather than holding through it blindly.

Rationale: STAT3 is a differentiated oncology target (implicated in tumor
immune evasion and inflammation-driven hepatocarcinogenesis); HCC is starved
for new mechanisms beyond checkpoint inhibitors and TKIs; TVRD trades near
cash-value with the HCC program apparently unpriced; small-cap biotechs on
binary Ph1b/2 oncology readouts routinely see 50-150%+ single-day moves on a
clean positive signal due to thin float and scarce pre-print interest.
Proposed instrument: common equity (no meaningful options market expected at
this microcap size). Explicit acknowledgment this is genuinely binary — sizing
must be small, venture-style.

### Bear (sonnet)

NO TRADE.

1. "2H 2026" is vague PR language, not a real trigger date — the dossier's
   2026-09-30 impact_window is an assumption, not a fact from the source.
   Nothing forces a print by that date.
2. STAT3 inhibition in HCC is a historically hard target/indication combo — a
   difficult-to-drug target, no approved STAT3-inhibitor precedent, and HCC is
   a graveyard for failed Ph1b/2 readouts (refractory, heterogeneous disease,
   immune-suppressive liver microenvironment).
3. Dilution/cash-runway risk is standard for a pre-catalyst microcap biotech
   and totally unaddressed by the dossier — no cash balance, share count, or
   offering history given.
4. A same-company "on track" reaffirmation in an IR release carries near-zero
   incremental information (companies disclose delays reluctantly and
   reactively; no independent clinicaltrials.gov check or third-party
   disclosure cited).
5. TVRD already shows ~4% single-day swings on thin trading with intermittent
   twelvedata rate-limiting/missing bars, consistent with the documented
   microcap coverage-quality pattern.

Test-priced TVRD at 2026-07-24T15:00Z = $2.495 (twelvedata), confirming the
name is priceable but fragile (rate-limited on subsequent lookups).

### Quant (opus)

NO TRADE, size 0.

Verified twelvedata price series (1-min bars, various UTC timestamps):

| date (UTC) | price |
|---|---|
| 2026-07-10T19:55 | 3.275 |
| 2026-07-17T19:55 | 3.12 |
| 2026-07-20T13:35 | 2.955 |
| 2026-07-21T13:35 | 2.92 |
| 2026-07-23T14:30 | 2.60 |
| 2026-07-24T19:55 | 2.52 |
| 2026-07-24T19:59 | 2.515 |

Steady ~23% decline over 11 sessions, monotonic, no offsetting news — the
opposite of an anticipation runup. Minute-bar coverage partial (19:55Z bars
resolve every date tried; 13:35Z resolved 2 of 5 attempts) — pricable via a
fallback ladder, but corroborates thin liquidity.

Explicit EV assumptions:

- P(topline reported by 2026-09-30) = 0.28 (guidance is "2H 2026", not a date;
  we are 26 of 184 days into the window)
- P(positive | reported) = 0.25 (Ph1b/2 oncology base rate ~10-30%; STAT3 has
  no approved precedent)
- Upside on clear positive = +90%; downside on negative/ambiguous = -50%
- P(dilutive raise before 2026-09-30) = 0.40, impact -20%
- Baseline drift if nothing happens = -8% (heavily decayed vs. the observed
  ~-2%/week trend)
- Round-trip transaction cost = 2.5%

EV(long) = 0.070×(+90%) + 0.210×(-50%) + 0.432×(-8%) + 0.288×(-20%) =
-13.5% gross, ≈ -16% net of costs. Rejected.

Mirror-image short: gross EV ≈ +13.5%, net of costs and borrow (~3%) ≈ +8%.
Signal-to-noise: realized daily vol ~5.5%, 47-session horizon → σ≈37.7%,
S/N = 8/37.7 ≈ 0.21 (above the 0.15 floor nominally) — but perturbing
P(raise) 0.40→0.20 drops net to ≈+4% (S/N≈0.11); perturbing drift -8%→-2%
drops net to ≈+5% (S/N≈0.13); both together ≈+1% (S/N≈0.03). The edge is
smaller than the uncertainty in its own inputs. Positive-readout tail is an
un-stoppable overnight gap (+100% to +300% on the 7% branch), making even a
small Kelly-sized short unattractive.

Verdict: NO TRADE, size 0. Confidence 0.8.

## Round 2 — Rebuttal

### Bull rebuttal

Concedes the momentum thesis is falsified by the -23% bleed with no offsetting
news — retracts "riding pre-catalyst momentum" entirely; a steady unexplained
decline into a binary catalyst is not unpriced upside, and there's no way from
here to distinguish informed selling, forced liquidity exit, or dilution
pricing.

Pushes back: (1) Bear's date-uncertainty critique cuts both ways — argues for
wider/cheaper sizing, not necessarily zero position; (2) Quant's EV is built
on unverifiable assumptions whose own stated fragility (S/N~0.21) should
discount the long-side rejection symmetrically with the short's rejection, not
just kill the short.

Revised position: NO ENTRY TODAY. Would only take a much smaller starter
position on clear stabilization (2-3 sessions without new lows, or a clear
volume/price exhaustion signal). Would move to full NO TRADE alongside
Bear/Quant if the bleed continues into September with no stabilization. What
would restore conviction: price stabilization/reversal, a company update
narrowing "2H 2026" to a specific date, or confirmed cash runway past the
catalyst.

### Bear rebuttal

Notes the Bear's qualitative case (vague catalyst, hard target/indication,
dilution overhang, non-informative reaffirmation) and the Quant's quantitative
case (negative EV, failed short robustness) are independent evidence streams
— disjoint inputs (narrative risk vs. realized price action) reaching the same
NO TRADE, which is genuine corroboration.

Pushes on Quant's specific numbers: argues P(raise)=0.40 may be conservative
given the bleed plus a 2+-month runway to the catalyst; argues -8% baseline
drift may understate the realized trend, though agrees killing the short
holds regardless of drift assumption given the un-hedgeable gap tail.

Directly refutes Bull's "unpriced optionality": the market has had the
STAT3/HCC thesis available the whole time TVRD was falling and has
consistently chosen to sell into it — "unpriced" is not the same as
"un-bought." Bull's own stated exit plan (treat the print as a hard exit)
implicitly concedes there is no run-up to harvest.

Verdict: NO TRADE stands, confidence 0.8, aligned with Quant.

### Quant rebuttal

Steelmans the Bull's strongest possible counter: a falling price against a
fixed absolute post-data target is mechanically convex (upside multiple
widens as entry falls, downside compressed by a cash floor) — i.e. the
decline could be exogenous flow, not information.

Tests it: TVRD -23.1% (07-10 to 07-24) vs. XBI (biotech sector benchmark)
-5.3% over the identical window
(https://api.twelvedata.com/time_series?symbol=TVRD&interval=1min&date=2026-07-24
and same endpoint for XBI). Even at an aggressive 1.8 beta, sector explains
only ~-9.5%, leaving ~-13pp of idiosyncratic, name-specific decline. The
contrarian read is quantitatively refuted — TVRD fell ~4x its sector; the
market is pricing something specific to this name, not generic micro-cap
softness. Notes the "cash floor" claim (Bull) and the "dilution forces a raise"
claim (Bear) are opposite readings of the same unsourced balance-sheet line —
neither persona produced the actual number, so neither is credited.

Separately measures minute-bar coverage on the most recent session
(2026-07-24): 5 of 12 sampled RTH minutes had bars (~42%), including gaps one
and five minutes after the open — the same coverage-quality failure mode
logged for other microcaps in this project. This makes the Bull's "harvest
strength intraday" exit plan structurally unexecutable independent of any EV
argument.

On dilution: flags that Bear's agreement on P(raise)=0.40 is a correlated
generic base-rate prior, not independent corroboration — refuses to harden
the input on agreement alone (per this project's own false-consensus lesson).
Notes the long-side rejection doesn't depend on this input: zeroing dilution
entirely still leaves EV(long) at roughly -6% to -10% gross, still rejected.
The short's nominal edge, by contrast, depends heavily on this same weak
input, making the short's case worse under scrutiny, not better.

Re-runs the S/N robustness check with all context on the table: signal side
unchanged or weaker (P(raise) downgraded to unverified generic prior); noise
side worse (coverage gap raises realized slippage, adds borrow/recall risk);
long-side signal tested against the strongest available counter-hypothesis
(XBI comparison) and survives. S/N conclusion holds below the 0.15 floor in
both directions.

Verdict: NO TRADE, size 0, unchanged. Confidence raised to 0.85 — driven
specifically by the two new verified facts this round (XBI relative-strength
refutation, minute-bar coverage-gap finding), explicitly not by persona
headcount/agreement (flags the risk of false consensus from correlated
priors).

## Round 3 — Synthesis

**hypothesis**
- statement: TVRD offers no exploitable edge into its TTI-101 HCC Phase 1b/2
  readout. The catalyst is not date-certain ("2H 2026" is company PR language;
  the dossier's 2026-09-30 impact_window is an assumption, not a scheduled
  event), so the probability the print even lands inside the trade window is
  low (~0.28). The bull's original entry rationale, a pre-catalyst
  anticipation runup, is empirically falsified: verified twelvedata prints
  show $3.275 (07-10) to $2.515 (07-24), ~-23% over 11 sessions, against XBI
  -5.3%, leaving ~-13pp of idiosyncratic, name-specific decline that even a
  1.8 beta cannot explain. The market has had the STAT3/HCC thesis available
  throughout that decline and sold into it, so "unpriced optionality" is not
  supported. Long-side EV is negative (~-13.5% gross, ~-16% net) and remains
  negative (~-6% to -10% gross) even if dilution risk is zeroed out entirely.
  The mirror-image short shows only a nominal +8% net EV, fails the
  robustness floor (S/N ~0.21 vs. 0.15 threshold under small perturbations of
  P(raise) and drift), depends most heavily on the single weakest unverified
  input (an unsourced P(raise)=0.40), and carries an un-hedgeable
  positive-readout gap tail. Execution is separately impaired: sampled live
  minute-bar coverage on TVRD is only ~42%, making any intraday "harvest
  strength" exit structurally unexecutable.
- direction: none
- confidence: 85

**plan**: no trade — no directional position survives: the long is
negative-EV even with dilution risk zeroed, and the short's positive nominal
EV fails the robustness floor while carrying an un-hedgeable positive-readout
gap tail. No entry, no exit, no timestamps proposed; ~42% minute-bar density
would also make any exact-minute fill assumption unreliable. Bull's
conditional re-entry trigger (a smaller starter position only on 2-3 sessions
without new lows, plus either a company update narrowing "2H 2026" to a
specific date or verified cash runway past the catalyst) is recorded as a
watch condition, not an authorized plan — none of those conditions is met as
of 2026-07-24.

**dissent**: Does the ~-13pp idiosyncratic decline make the position worse or
better? All three personas treated the bleed as bearish information, but
nobody resolved the mechanism, and the mechanism flips the sign. If it is the
market front-running a dilutive financing or leaking a negative read on the
program, the decline is informative and NO TRADE is right for the reason
given. If it is indiscriminate microcap tax-loss/liquidity bleed, then a
fixed-absolute-value binary catalyst just got materially cheaper and the
long's convexity is rising as price falls — the quant steelmanned this read
but refuted it only with relative-strength evidence, which establishes the
decline is name-specific, not that it is outcome-predictive. The debate could
not settle it because the one fact that would arbitrate — an actual
cash-and-burn figure from filings establishing whether runway extends past
the readout — was never sourced by any persona. Bear's agreement on
P(raise)=0.40 was a correlated generic base-rate prior rather than
independent corroboration, and Bull's symmetry objection (that the EV
model's admitted input fragility should discount the long-side rejection too,
not just kill the short) was never directly answered. Post-mortem check: pull
TVRD's cash/burn and any financing announced between 2026-07-24 and the
actual readout date. If a raise came, the consensus was right for the right
reason; if runway was already funded past the catalyst and the stock re-rated
on the print, this was a correctly-reasoned NO TRADE reached on an unverified
premise.
