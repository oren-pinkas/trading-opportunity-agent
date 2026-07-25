# Research debate transcript — 2026-07-23-bmy-cobenfy-alzheimers-psychosis-data

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant
(opus). Synthesizer: opus. Run at 2026-07-25T05:03:19Z.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Dossier under review

- Title: Bristol Myers Squibb tests Cobenfy in Alzheimer's psychosis
- Event summary: BMY's Karuna-acquired Cobenfy is being tested in Alzheimer's-related
  psychosis, with a positive readout seen adding USD 2-4B peak sales and validating
  the Karuna acquisition thesis.
- impact_window: 2026-08-15
- Ticker: BMY
- Source: "This Small-Cap Biotech Is Turning Heads on Wall Street" —
  https://pro.thestreet.com/trade-ideas/this-small-cap-biotech-is-turning-heads-on-wall-street
  (accessed 2026-07-23T11:19:21Z)
- Reference price: BMY closed ~USD 62.055 as of 2026-07-24T19:59Z (source:
  twelvedata via `toa price`).

## Institutional-memory lessons injected (event.type=earnings, ticker=BMY)

- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
  ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express via
  defined-risk options, never a naked position. (source: 2026-07-02-levi-q2-fy26 /
  2026-06-25-nike-q4-fy26 lineage)
- Discount post-earnings negative base rates when the name is already at/near its
  52-week low: most of the drawdown may already be priced in. (2026-06-25-nike-q4-fy26)
- Set intraday exits at least one minute inside the session boundary (19:59:00Z);
  1-minute-bar providers have no bar stamped exactly at the close. (2026-07-02-tesla-deliveries)
- A catalyst that already drove a large multi-week run to a 52-week high above the
  Street mean target is priced in — don't re-bet the same fundamental as a fresh
  trigger. (2026-06-26-delta-q2-fy26)
- When the quant's EV math and the strongest dissent both point to near-zero edge,
  synthesize to NO-TRADE rather than a token directional position.
  (2026-06-26-delta-q2-fy26 / 2026-07-02-levi-q2-fy26)
- Anchor entry prices to a live quote fetched at the actual entry timestamp; validate
  the planned entry is within tolerance of current price before filling.
  (2026-07-02-levi-q2-fy26)

---

## Round 1 — Independent research

### Bull (sonnet)

BMY sits near a 52-week trough after Karuna-thesis skepticism; the stock has priced
in almost nothing for Cobenfy beyond schizophrenia. Any signal that Cobenfy's
mechanism (muscarinic agonism, not dopamine blockade) extends into Alzheimer's-related
psychosis reframes the whole acquisition — from "expensive schizophrenia bet" to
"platform play across a dementia-psychosis population that dwarfs the current
label." Alzheimer's psychosis affects a materially larger patient pool than
schizophrenia, and a clean safety/efficacy signal removes the biggest overhang bears
have used against the deal. The dossier's own framing — "positive readout adding
USD 2-4B peak sales" — is exactly the kind of re-rating catalyst that moves biopharma
names 5-15% on data-flow headlines alone, even ahead of a formal readout, because
momentum/algo desks front-run trial chatter once it hits the tape.

What's actually known vs. inferred: Known — this is a single small-cap-biotech
commentary source (thestreet.com trade-ideas piece, accessed 2026-07-23), no
confirmed trial name, no phase, no PDUFA or readout date; impact_window of
2026-08-15 appears to be an editorial/analytical marker, not a confirmed data-drop
date. Inferred — that "being tested" implies active News flow between now and 8/15
that can move sentiment even without a formal readout. This is thin — a
narrative/momentum trade on flow, not a binary-event trade on a locked catalyst date.

Proposed action: Long BMY. Instrument: modest common-stock long or a call option
expiring shortly after 2026-08-15 (e.g., Aug 21 expiry). Entry: near USD 62.06
(validate live quote at fill), scaled small given source thinness. Exit: scale out
into strength ahead of 8/15 if the stock runs 5%+, or hold through the window with a
hard stop below USD 58 (~6.5% risk) if no news materializes. Target: USD 66-68
(6-10% move).

### Bear (sonnet)

This dossier does not clear the bar for a tradeable catalyst. The source is a single
retail-oriented article titled "This Small-Cap Biotech Is Turning Heads on Wall
Street" — applied to BMY, a >USD 100B large-cap pharma. That mismatch is a red
flag: either the source is a low-quality aggregator mislabeling names, or BMY is
being swept into a listicle with no dedicated diligence. There is no named trial, no
confirmed phase, no cited data-readout or conference date. "impact_window:
2026-08-15" reads as an arbitrary placeholder, not a PDUFA date or an AAIC
presentation slot. Trading a specific date against an unconfirmed catalyst is
trading noise, not signal.

What's already priced in: BMY completed the Karuna acquisition to get Cobenfy, and
expansion into Alzheimer's-related psychosis is the obvious, widely-anticipated next
indication for a novel schizophrenia mechanism — every sell-side analyst covering
BMY has this in their model already. The dossier's own USD 2-4B peak-sales figure is
the bull case already known to the Street, not new information.

Concrete risks: (1) No confirmed date means 2026-08-15 could simply pass with no
news — decay/theta cost, no resolution. (2) Even if some data trickles out,
early-stage psychosis data in Alzheimer's is not registrational — it moves a stock
<1% typically for a name with BMY's diversification (oncology, cardiovascular,
immunology dwarf Cobenfy in P&L terms). A USD 2-4B peak-sales estimate is immaterial
against BMY's ~45B total revenue base. (3) If the "data" is a poster/early cohort
update rather than a defined readout, the asymmetric downside is a sold-the-news
fade on a hyped small position.

Proposed action: NO TRADE. If a bull case survives synthesis at all, it should only
be expressed as a small, defined-risk options structure with a strike/expiry padded
well past 2026-08-15 to survive date slippage — never a naked equity position sized
to an unconfirmed binary.

### Quant (opus)

BMY market cap ~USD 135B; price USD 62.06 (2026-07-24T19:59Z, twelvedata). Peak
sales USD 2-4B (midpoint 3B) at a 3.5x multiple for a de-risked indication =
undiscounted equity value ~USD 10.5B = ~7.8% of market cap. Discounting 6 years to
peak sales at 9% (~0.60x) = ~USD 6.3B = ~4.7% of cap. Probability-weighting at
10-15% ultimate approval from an early/unconfirmed signal (historical Phase
2→approval in CNS/neuropsych) = risk-adjusted value ~USD 0.6-0.9B = **0.5-0.7% of
market cap**. Diversification dampener: BMY has 10+ meaningful revenue lines —
single-indication label expansions in diversified large-cap pharma historically move
the stock 1-3% on a genuine positive readout, 0-1% on ambiguity; 8-15% moves belong
to single-asset small caps.

Explicit probabilities: P(confirmed, tradeable readout on/before 2026-08-15) = 15%
(no trial ID, no guided date, promotional third-party article; sub-4-week windows
with no scheduled catalyst usually resolve empty). P(positive | readout occurs) =
55%. P(positive readout in window) = 15% × 55% = **8.3%**. Expected move if positive:
+2.5%. If negative: -2.0%. No event (85%): 0% drift, pure beta with ~4-5% three-week
sigma.

EV calculation (directional long): Positive 0.083 × +2.5% = +0.21%. Negative 0.15 ×
0.45 = 6.75% × -2.0% = -0.14%. No event 0.85 × 0% = 0%. Gross EV = +0.07%. Costs
(commission/spread/slippage round trip) ≈ -0.10%. **Net EV = -0.03%.**

Filter check: confidence ~20% (well under the 45% threshold); net EV -0.03% (far
under 2%); adverse tail (-2% event leg plus ~4-5% three-week beta sigma against a
+0.21% edge) is a >20x tail-to-edge ratio, worse than the 7-8x rejection bar. All
three no-trade conditions trip simultaneously.

Recommendation: **NO TRADE.** Would need P(readout in window) above 60% AND expected
positive move above 6% to clear a 2% net EV bar — neither remotely supported. Even a
defined-risk call spread fails: 8.3% probability of a 2.5% move won't cover premium
on a 3-week option. Size: zero.

---

## Round 2 — Rebuttal

### Bull (sonnet)

Bear/Quant's core points land, and I won't pretend otherwise.

1. "Already priced in": partially concede. Sell-side has modeled Cobenfy-into-
   Alzheimer's-psychosis as a pipeline line item since the Karuna deal closed — fair.
   But priced-in-as-optionality is not the same as priced-in-as-confirmed-signal. My
   thesis was "a confirmatory signal compresses the discount rate on an
   already-known option" — a real but narrower edge than my Round 1 framing implied.
   Concede on magnitude, not direction.
2. Quant's EV math: don't dispute the 15%/55% inputs — no better numbers, and Bear's
   point about the arbitrary 08-15 window is legitimate. Slight pushback on
   magnitude: if the "readout" is a positive early cohort/poster update, the market
   reaction on a large-cap could show up as elevated call volume/IV pop rather than
   a clean spot move — a secondary, options-microstructure argument, not strong
   enough to overturn -0.03% net EV alone.
3. Strongest point I can't rebut: the source itself — a "Small-Cap Biotech" headline
   applied to a >USD 100B name is a real credibility flag glossed over in Round 1.
   Combined with no named trial/phase/date, I can't construct a defensible edge
   estimate independent of the Quant's number.
4. Revised action: withdraw the common-stock/near-dated-call proposal. Cannot defend
   a directional trade against a 92% no-event probability and negative net EV.
   **Recommendation: NO TRADE, concur with Bear/Quant.**

### Bear (sonnet)

Quant's numbers vindicate the NO TRADE thesis directly: 8.3% joint probability of a
real, positive readout, net EV of -0.03% after costs, tail-to-edge over 20x — an
arithmetic confirmation that the base rate on an unconfirmed trial with no named
phase or date can't clear transaction costs, let alone justify sizing.

On the Bull's "52-week trough, priced in almost nothing" framing: this cuts against
the Bull, not for them. A stock at a trough after Karuna-thesis skepticism means the
market has already relitigated the Cobenfy bet and concluded the risk/reward on
unconfirmed pipeline extensions is poor — efficient pricing of a soft signal, not an
oversight waiting to be corrected. Trough + thin catalyst is not a coiled spring;
it's a stock where the market has already done the Quant's math.

The risk the Bull ignores: the 08-15 impact_window may not map to any real
corporate/conference event at all. Nothing in the source names a trial ID, phase, or
data-cutoff/readout date — the window looks like an analyst-assigned placeholder.
Anyone taking the Bull's "call option expiring shortly after 08-15" trade is
underwriting date risk on a date that might be fictional — a bet that decays to zero
on no news at all, with no informational payoff either way.

**Recommendation: sharpened NO TRADE, size zero.**

### Quant (opus)

1. Stress-testing the Bull's 5-15% magnitude claim: real but drawn from single-asset
   biotechs where the asset is 60-100% of enterprise value; does not transfer.
   Cobenfy-in-AD-psychosis is risk-adjusted 0.5-0.7% of BMY's ~USD 135B cap, at most
   ~8% of cap at full un-discounted 100%-probability credit. BMY has ~2B shares,
   USD 400-600M daily dollar volume, deep listed options, mechanical index/dividend
   ownership — float absorbs headline flow instead of gapping. BMY 30-day IV runs in
   the 20s with mild put skew (vs. 80-120% IV for single-asset names) — the options
   market itself is pricing the absence of a binary. The Bull's 6-10% target is a
   category error, not a conservative estimate.
2. Double-counting with Bear: partly yes. "Already priced in" and "low P(readout)"
   are largely the same effect (efficient discounting of a known pipeline
   extension). But not fully identical — mine is event-timing risk (nothing happens
   by 08-15), Bear's is information risk (something happens but is pre-discounted).
   Independent conditional layers; Bear compounds the negative case modestly, not
   doubly.
3. Sensitivity: net EV +2% needs P(readout) ≈ 75% at +2.5% move, or an expected
   positive move of ~+45% at P=15%. Both absurd given zero supporting evidence in the
   dossier (no trial name, no phase, no registered readout date, retail small-cap
   source).
4. **Recommendation: HELD. NO TRADE, size zero. Confidence ~20%.**

---

## Round 3 — Convergence (synthesizer, opus)

**hypothesis**
- statement: Cobenfy-in-Alzheimer's-psychosis is a real but immaterial and largely
  pre-discounted optionality for BMY; the dossier's 2026-08-15 impact_window is not
  tied to any confirmed trial, phase, readout, or conference event, and the sourcing
  (a small-cap-biotech headline applied to a ~USD 135B large-cap) fails the
  credibility bar. No tradeable edge exists at current evidence quality.
- direction: none
- confidence: 22

**plan**
- action: no trade
- ticker: BMY
- rationale: Unanimous across all three personas by round 2 (Bull explicitly
  withdrew). All three no-trade filter conditions trip: (1) confidence ~20% vs. 45%
  threshold; (2) net EV after costs -0.03%; (3) tail-to-edge ratio >20x vs. 7-8x
  rejection bar. Joint probability of a positive tradeable readout by 2026-08-15 is
  8.3% (15% readout × 55% positive); risk-adjusted equity value of the full
  indication is only 0.5-0.7% of market cap even before probability weighting,
  against 4-5% three-week beta sigma. A dated option position carries pure theta
  decay with no informational payoff if the window maps to no real event.
- entry/exit: none (monitoring only)
- expected_profit_pct: 0
- position_size: 0

**dissent**

Strongest unresolved disagreement: the Bull's surviving secondary claim that an
options-microstructure edge (implied-vol expansion into a rumored catalyst window)
can exist even when spot EV is ~zero. The Quant did not model IV separately — he
rebutted on spot-move magnitude and noted BMY's ~20s IV regime dampens gaps, but
never priced a long-vega structure. If the vega path were real, the panel's
spot-based -0.03% EV would be the wrong test. Preserve for post-mortem: did BMY
3-week IV actually expand into 08-15?

What would flip the call to a trade:
- A named trial (NCT ID), phase, and a confirmed readout or conference presentation
  date inside the window — this alone would move P(readout) from 15% toward the
  Quant's ~75% flip threshold.
- Corroboration from a tier-1 source or BMY IR/investor-day guidance, replacing the
  mismatched small-cap article.
- Evidence the indication is materially larger than USD 2-4B peak sales, or a BMY
  drawdown large enough that the same optionality becomes a meaningful share of
  value.
- Sell-side revision activity showing the indication is NOT already in consensus
  (Bear's core premise is an assumption, not a verified fact — nobody checked
  consensus models).

What to watch: (1) any BMY/Cobenfy AD-psychosis trial registration or
dose-expansion disclosure; (2) whether 2026-08-15 corresponds to any real
corporate/conference event at all — if not, treat this dossier's impact_window as an
editorial artifact and flag the scout pipeline for generating unanchored dates; (3)
source-quality gate: this dossier passed research with a small-cap-framed article on
a large-cap, which should have been caught upstream.

Post-mortem calibration note: an outcome where BMY moves >5% on unrelated news
through 08-15 does NOT invalidate this NO TRADE — judge the call on whether a
Cobenfy AD-psychosis readout actually occurred in-window, not on realized BMY drift.
