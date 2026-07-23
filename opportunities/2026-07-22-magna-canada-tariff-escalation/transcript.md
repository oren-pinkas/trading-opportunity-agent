# Research Debate Transcript: Magna Canada auto tariff escalation (MGA)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel (bull/bear sonnet, quant/synthesizer opus)
Run: 2026-07-23T19:36:19Z

Event: US tariffs on non-USMCA-compliant Canadian goods rise from 25pct to 35pct
effective 2026-08-01 (a Saturday — nearest trading sessions: Fri 2026-07-31 close
or Mon 2026-08-03 open), hitting the auto parts supply chain. Ticker: MGA (Magna
International). Reference price: USD 68.45 at 2026-07-22T14:30Z (source:
twelvedata via `toa price`).

Source: WardsAuto — "Canada auto sector faces existential challenges in 2026"
(https://www.wardsauto.com/news/usmca-canada-auto-sector-faces-challenges-2026-tariffs-evs/810028/),
accessed 2026-07-22T07:00:28Z.

Relevant institutional lessons applied:
- Validate entry/exit timestamps fall within an open trading session; roll
  non-trading dates forward (source: 2026-07-08-caesars-icahn-fertitta-bidding-war).
- Never map a corporate/legal calendar date directly onto an execution timestamp
  (source: 2026-07-08-caesars-icahn-fertitta-bidding-war).
- S/N below ~0.15 on a linear-EV fade is not a durable edge; simulate-plans has no
  path-dependent stop enforcement (source: 2026-07-10-prologis-segro-bid-deadline).
- A fill outside the planned entry band is an early falsification signal
  (source: 2026-07-10-prologis-segro-bid-deadline).
- Test-query the real price provider for exact timestamps during research
  (source: 2026-07-12-nayax-cyber-breach-ultimatum).

## Round 1 — Independent research (parallel)

### Bull (sonnet)

Short MGA (or puts). Enter Thu 7/30 or Fri 7/31 near USD 68.45, target USD 64-66 by
early the following week, stop above ~70. Confidence 55-60%.

Reasoning: the 10-point tariff step-up (25pct->35pct) is a real, dated, scheduled
cost-margin shock, not a rumor. Magna runs one of the largest Canadian
manufacturing footprints in auto parts (stamping, seating, powertrain), and even
largely-compliant parts carry non-compliant sub-assemblies/inputs that fall into
rules-of-origin gaps — exactly what WardsAuto flags as an "existential challenge."
Explicitly flagged Magna's exact non-USMCA-compliant content % as unsourced
inference — the single biggest unknown. Would strengthen on analyst notes
quantifying tariff cost exposure in $/EPS; would weaken on evidence this was
already flagged/priced in, or that most Canadian output is already compliant.

### Bear (sonnet)

No trade. Confidence only ~30% that any tradeable edge exists at all.

Reasoning: this is a long-telegraphed USMCA compliance dispute, not a surprise —
markets price known dates well in advance. WardsAuto trade-press coverage is
downstream, not primary; sell-side has had compliance %/tariff schedules modeled
for over a year. Magna is a diversified global supplier that can pass costs
through to OEMs (Ford/GM/Stellantis) via existing industry levers. Single-name
event shorts around binary regulatory dates risk violent short-covering rallies.
Signal-to-noise likely below the ~0.15 durability bar. Would change mind on:
evidence of large undisclosed non-compliant COGS share, a still-flat price days
before the date (no anticipation pricing), or a primary-source (10-Q/8-K)
compliance percentage.

### Quant (opus)

No trade. Confidence 80%.

Reasoning: base rate for a telegraphed, calendar-fixed tariff step-up producing a
clean discrete move (attributable to the step itself, not noise) is ~15-20%.
Magnitude: Magna's footprint is predominantly US/Mexico/Europe; non-USMCA-compliant
Canadian revenue is likely a low-single-digit slice of a ~USD19B-cap company — a
rounding error against consolidated earnings. Explicit EV calc for a short from Fri
7/31 close to Mon 8/3 (weighted across adverse/flat/relief scenarios): ~-USD0.10/share
gross, ~-USD0.25/share after slippage/commission. Signal-to-noise well under the
0.15 durability bar once the pre-priced and symmetric-relief-tail mass is weighted
in. Weekend-gap entry also means any off-band fill is an immediate falsification
with no path-dependent stop to save it.

## Round 2 — Rebuttal (parallel)

### Bull (sonnet)

Still holds the short thesis but weakens/adjusts it materially. Disputes quant's
"rounding error" framing: the marginal non-compliant slice hits gross margin
dollar-for-dollar, and OEM cost pass-through isn't instantaneous (contracts have
negotiated cost-share clauses with lag, not automatic pass-through on a Saturday
deadline) — so the outcome distribution is wider than quant's point estimate
implies. Grants bear's "telegraphed dispute, sell-side has modeled this for a
year" objection is real and dangerous — trading a calendar date is not the same
as trading new information. Adjustment: cut size ~40-50% vs Round 1, switch from
outright short to a defined-risk put spread (caps loss on a short-covering
squeeze), enter Fri 7/31 close only (not Thu), require a pre-market
IV/skew check confirming the move isn't already priced before sizing up. Would
flip to no-trade on: rich put skew already priced into 8/1, a recent sell-side
note calling the non-compliant content immaterial, or evidence of pass-through
mechanisms.

### Bear (sonnet)

Converges further toward no-trade; revises "edge exists" estimate DOWN from ~30%
to ~20-25%. Notes quant's magnitude analysis strengthens (not just parallels)
bear's priced-in argument: even if nothing is priced in, the shock is objectively
too small to matter for a diversified ~USD19B supplier — a stronger, more
falsifiable objection than "it's stale." Bull's own admission that the
non-compliant-content % is "inference, not sourced" is itself evidence there's no
primary-source edge here — everyone, including bull, is reading the same
consensus trade-press signal. Final: NO TRADE. Revisit only if a sourced
non-compliant-revenue % surfaces via 10-K/10-Q disclosure or a cited sell-side
note.

### Quant (opus)

Grants the tariff step is real/dated but reiterates tier-1 USMCA-compliant
suppliers typically run 75-90%+ compliance, so the incremental hit lands on a thin
non-compliant residual — ballpark single-digit millions to low tens of millions of
EBIT impact, sub-1% of earnings. Nudges clean-discrete-move probability up
slightly (15%->18%) but leaves magnitude estimate unchanged. Frames bear's and its
own arguments as reinforcing, not redundant: bear's is conditional (no edge if
priced in), quant's is unconditional (shock too small regardless of pricing).
Stress test: for bull's short to have positive EV after costs, the joint
probability of (right magnitude AND right direction AND right timing) needs to be
~5-8%; quant estimates the actual joint probability at ~5% — right at breakeven,
no margin of safety. Final: NO TRADE, confidence raised to 82%.

## Round 3 — Convergence (synthesizer, opus)

**Hypothesis:** The 25%->35% tariff step on non-USMCA-compliant Canadian goods
(effective 2026-08-01) is real and dated, but it is both long-telegraphed (likely
priced-in) AND objectively too small to move MGA — a ~USD19B diversified global
supplier whose Canadian non-compliant revenue is, by every persona's own estimate,
a low-single-digit residual after 75-90%+ tier-1 USMCA compliance. The one
variable that could justify a trade (true non-compliant Canadian revenue %) is
admitted-inference by the bull itself — no participant holds a primary-source
edge. Direction: neutral / no-trade. Confidence: 80.

**Plan:** No position. No actionable entry or exit.
- ticker: MGA
- action: no-trade
- entry: none
- exit: none
- expected_profit_pct: 0

Re-open only if a sourced non-USMCA-compliant Canadian revenue figure surfaces
(10-K/10-Q segment disclosure, guidance cut, or a cited sell-side note) AND a
pre-market options-skew check on Fri 2026-07-31 shows the Street has not already
priced it. Absent both, there is no trade here.

**Dissent (strongest unresolved disagreement):** The true size of MGA's
non-USMCA-compliant Canadian revenue exposure is unsourced across all three
personas — bull flagged it as inference, bear used that admission to argue no one
has an edge, quant assumed 75-90%+ compliance to derive a sub-1%-of-earnings
impact. All three numbers are estimates, not disclosures. The no-trade call is
robust to this uncertainty in the "priced-in" direction, but the tail risk is
asymmetric: if the actual non-compliant Canadian exposure were materially higher
than assumed (e.g. a concentrated product line/plant plus OEM pass-through
contractual lag, which bull correctly noted is not instant), the short thesis
could revive with real edge. For the post-mortem: if this event did move MGA, the
failure would be that no one pulled the segment/compliance data that would have
converted three guesses into one fact.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
