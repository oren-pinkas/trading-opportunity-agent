# Research debate transcript — 2026-07-13-spgi-mobility-global-spinoff

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Debate run: 2026-07-14T05:12:26Z.

Anchor price used throughout: **SPGI USD 438.415 at 2026-07-13T19:00:00Z**
(source: `https://api.twelvedata.com/time_series?symbol=SPGI&interval=1min&date=2026-07-13&timezone=UTC`,
fetched via `toa price SPGI 2026-07-13T19:00:00Z --provider twelvedata`).

Institutional lessons injected (via `toa lessons-relevant --type economic --tickers SPGI`):

1. Anchor entry to a live pre-event quote, not the research-day price; if the live price
   has drifted >~0.5-1% from the plan anchor, re-derive targets/EV or void the trade
   rather than filling blind. (`2026-07-01-ism-mfg`)
2. When the thesis is "catalyst reprices X higher" and X has already rallied to its
   52-week high before the event, treat the move as priced-in: fade or shrink, don't
   chase the entry. (`2026-07-01-ism-mfg`)
3. Skip trades whose only positive-EV path is a pre-market conditional entry the harness
   cannot fill; if the executable cash-open leg's EV is ~0, don't record the trade.
   (`2026-07-02-june-jobs`)
4. After a known regime shift, require a differentiated surprise vs consensus before
   shorting duration into a data print: an in-line print is already in the curve and
   gets faded by duration buyers. (`2026-07-02-june-jobs`)

---

## Round 1 — Independent research

### Bull (Catalyst-hunter), confidence 62/100

READ: Classic RemainCo pure-play re-rating trade, already in motion but not finished —
the next leg is the Q2 2026 earnings/first-clean-guidance catalyst (~2026-07-28),
landing just before the 2026-07-31 window close. Long SPGI, riding the second half of
a re-rating that started on the spin date.

Evidence: spin completed 2026-07-01 (record date 2026-06-15); MBGL carries USD 2B new
debt (cleaner balance sheet left with SPGI). SPGI opened USD 412.14 on 7/1 post-
distribution, rose to USD 437.19 by 7/2 (+5.35%, attributed to post-separation
repricing, index rebalancing flows, and a Q1 beat), then held/consolidated at USD
438.42 through 7/13 — read as consolidation, not a fade. Analyst consensus Buy, 24
buys/4 holds, median price target USD 548-550 (~25% upside from anchor). Huber
Research upgraded citing pure-play re-rating logic ("cleaner stories often get
cleaner valuations"). JPMorgan trimmed target to USD 535 (from 550) and BofA to USD
550 (from 575) on guidance-recast, but both kept Buy/Overweight. Sum-of-parts:
pre-spin modeling put SPGI stub fair value at USD 385-393; current USD 438 confirms
the re-rating is real and in progress, with room left to the USD 548-550 consensus.
MBGL trades ~40% below its own analyst target — read as capital rotating to the
cleaner RemainCo. Lesson #2 (fade if at 52-week high) argued not to bind because the
pre-spin 52-week high (~USD 574-579) included Mobility's value, since carved out.

Action: Long SPGI common at ~USD 438.42; optional small OTM call sleeve (August
expiry, USD 460-470 strike) for convexity around 7/28 earnings. Hold through the 7/28
print into the 7/31 window. Soft invalidation: close below ~USD 412 (post-spin open).

### Bear (Skeptic), confidence 72/100

READ: This is stale news dressed as a fresh catalyst. The spin-off was announced
2025-04-29 and completed 2026-07-01 — thirteen days before "today." Completion, NYSE
debut, and the initial re-rating pop are done deals; there is no forward catalyst
left in "the spin-off completed."

Evidence: SPGI closed up 7.99% on 7/1 (completion day) — that IS the re-rate, already
priced. Stock ran to ~USD 447 post-completion then eased to USD 430.50 by 7/10, a
2-4% pullback within the same week — consistent with a sell-the-news unwind. Goldman
cut its price target from USD 539 to 490 on 7/1 (day of completion); Baird cut to USD
520 "on Mobility spin" — sell-side sum-of-parts trimmed down, undercutting the
"leaner = higher multiple" narrative. SPGI sits 24% below its August-2025 all-time
high of USD 579 — an 11-month structural downtrend the spin alone is unlikely to
reverse in 2.5 weeks. Q2 earnings land 7/28, three days before window close — an
in-line print gets faded (lesson #4 analog), and this earnings binary dwarfs the
already-consumed spin "catalyst" as a risk to any position. Spin-offs generate
valuation-insensitive index/passive selling for weeks after separation — mechanical
overhang risk isn't fully cleared. Standalone dis-synergy costs (SG&A, lost
shared-services scale) are a known 12-24 month margin headwind likely understated by
the "leaner business" story.

Action: No trade / avoid a long SPGI position keyed to "the spin re-rates it higher."
If forced to take a stance: fade any further rally toward the stale USD 543
consensus rather than chase; flag 7/28 earnings as the dominant, underpriced risk.

### Quant (Pragmatist), confidence 72/100 — SKIP

VERDICT: Skip. The catalyst is stale — SPGI closed USD 439.89 on 7/2 and sits at USD
438.415 on 7/13, i.e. flat (-0.3%) for ~12 trading sessions since going ex-Mobility.
No forced-selling dislocation remains in the parent: SPGI stays in the S&P 500,
while spin-off passive/index selling pressure lands on the small SpinCo (MBGL), not
the large-cap parent.

Base rates: academic spin-off literature (Cusatis/Miles/Woolridge 1993; McConnell/
Ovtchinnikov 2004) shows parent abnormal returns of +16-18%, but concentrated over
**three years** and in names later acquired — irrelevant to a 12-day hold.
Documented short-horizon spin-off underperformance (-2.3% to -3.7%) applies to the
SpinCo in its first ~5 trading days, which have already elapsed. No robust base rate
supports parent RemainCo outperformance in a 2-week window.

The only live catalyst in the window is Q2 earnings on 7/28 (consensus USD 4.94 EPS,
+11.5% YoY, already priced in) — a symmetric coin-flip with no differentiated edge.
Explicit EV table: Beat (30%, +4.0%) / Flat (40%, +0.25%) / In-line mild fade (20%,
-2.0%) / Miss (10%, -5.0%) → gross EV ≈ +0.40%, net of ~0.05-0.10% slippage ≈
+0.30-0.35% over two weeks against ±3-4% earnings-day volatility — a ~0.1
reward-to-variance ratio, not an edge. Valuation sanity check: P/E ~22.7, Buy/~USD
520 consensus target, ~20% below 52-week high (not extended, so lesson #2 doesn't
bind either way — but also no coiled-spring re-rating fuel left since the spin is
already digested). Caveat: no live 2026-07-14 quote obtainable (`toa price` returned
HTTP 400 for intraday minutes not yet available); only the 7/13 anchor is
confirmable, which is itself a reason to void rather than fill blind (lesson #1).

Action: Skip / no directional trade. If forced to express a view, the only honest
structure is a small defined-risk earnings-vol play (e.g. a long straddle into
7/28), not a directional cash-equity position.

---

## Round 2 — Rebuttal

### Bull rebuttal — confidence revised 62 → 55/100

Concedes the core diagnostic point Bear and Quant both make: the spin-completion
pop is a realized, past event, not a live catalyst. Drops reliance on "re-rating
already in progress, more room to run" — flat (-0.3%) over 12 sessions is digestion,
not momentum, and that framing does not survive scrutiny. Also drops the base-rate
literature framing since neither counterparty's citations support a 2-week parent
re-rating tailwind.

Still argues: (1) the Goldman/Baird/JPM/BofA price-target cuts are being read as
more bearish than they are — a sum-of-parts PT *mechanically* comes down when a
division is removed, and all four analysts kept Buy/Overweight/Buy ratings despite
the cuts, which is the more informative signal; neither side has shown the cuts
exceed the value of the spun-off Mobility unit (the actual test of a fundamental
downgrade vs. arithmetic). (2) The USD 430.50 (7/10) → USD 438.42 (7/13) bounce
(+1.8%) reads as stabilization, not continued unwind — a clean unwind in motion
would show continued bleed. (3) Quant's own EV table nets positive (+0.30-0.35%),
just below Quant's personal bar; it also treats 7/28 as a single EPS beat/miss
variable when it's actually the first standalone operating guide (margin
framework, capital-return/buyback plans, segment mix) with independent re-rating
power that a bare "40% flat, +0.25%" bucket underprices. (4) Never claimed a
round-trip to the USD 579 all-time high — the thesis is a partial catch-up toward
the revised ~USD 520-535 consensus (still ~19-22% above spot), so the "24% below
ATH" framing argues against a thesis not actually held.

Revised action: a smaller directional common-share position, tighten the soft
invalidation trigger to ~USD 430 (the recent demonstrated low) rather than ~USD
412, and keep the small OTM call sleeve into 7/28 as the primary vehicle for the
"new guide re-rates the multiple" thesis rather than overweighting the coin-flip
EPS outcome.

### Bear rebuttal — confidence revised 72 → 75/100

Bull's "consolidation not a fade" framing is undercut by Bull's own numbers: flat
for ~2 weeks after a one-day 5.35% pop is exactly what a completed, priced-in move
looks like before the next data point (earnings), not unfinished business — if the
catalyst were still unresolved and worth 25% upside, the market would not have done
nothing with the stock for two straight weeks.

The MBGL-rotation argument ("MBGL trades 40% below its own target, so capital
rotated to the cleaner RemainCo") is a non-sequitur: SpinCo mispricing has a
simpler, well-documented explanation — forced index-fund/small-cap-mandate selling
of a newly spun, sub-scale, debt-loaded entity that doesn't fit institutional
mandates — a mechanism Quant's own Round 1 (passive selling lands on MBGL, not the
large-cap parent) already flags. That says nothing about whether SPGI itself still
has upside; it is the weakest plank in Bull's case.

Concessions: (1) JPM/BofA rating retention despite target cuts is fair pushback,
underweighted in Round 1 — but a stock still flat despite bullish targets is itself
informative (the market isn't rushing to underwrite the re-rating thesis, or
analyst SOTP models haven't been fully rebuilt post-spin). (2) The sum-of-parts stub
math (USD 385-393 pre-spin fair value vs. USD 438 now) is real and was underweighted
in Round 1 — but it actually cuts *against* Bull: current price already sits ~12-14%
above the modeled stub fair value, meaning much of the re-rate may already be more
than fully captured, not "in progress with room left." (3) The Huber Research
upgrade is single-shop, uncorroborated, and contradicted by the base-rate work
already in the transcript — doesn't need more weight.

Notes that Quant's EV table converts the qualitative "stale catalyst" claim into a
quantified near-zero/negative-skew edge — corroboration from an uncorrelated,
quantitative angle. Where Bear and Quant would differ if forced: Bear leans toward
fading rallies toward the trimmed USD 490-520 cluster (not the stale USD 543).

Revised confidence to 75/100 on the strength of Quant's independent convergence;
capped below 80 because Bull's rating-retention and stub-math pushback are real,
if modest, and the actual invalidation trigger (a strong 7/28 print with a genuine
guidance upgrade) remains three-sided and unresolved.

### Quant rebuttal — confidence revised 72 → 76/100

Bull's sum-of-parts stub math reinforces the skip case rather than the bull thesis:
price (USD 438.42) already sits ~12-14% *above* its own modeled fair-value anchor
(USD 389 midpoint) — the tradeable dislocation is gone. Converting the USD 548-550
consensus target (a ~12-month figure) to the trade window: ~25% over ~250 trading
days implies roughly +1.7% over 17 sessions if linear and front-loaded — neither of
which holds for a stock flat for 12 days — and that magnitude is already inside the
existing "Flat"/"Beat" buckets, not a new source of edge.

Bear's evidence reinforces "no upside edge" but overstates directional downside:
Goldman (USD 490), JPMorgan (USD 535), and Baird (USD 520) targets, even after
cuts, all remain *above* the USD 438 spot — a PT cut is not a sell signal, it's
sell-side sum-of-parts recalibration; it does compress the upside tail, however,
which matters for the Beat-scenario magnitude. Also flags an unreconciled data
point: Bear's unconfirmed USD 447 intraday peak / USD 430.50 trough (implying a
-3.8% swing) does not reconcile against the flat USD 438-440 closes Quant and Bull
both independently cite; Quant does not credit the larger magnitude.

Bear and Quant share the "skip" headline but would take opposite forced trades:
Bear leans short-delta (fade rallies), while Quant's own EV table — with a 40%-
weighted "Flat" scenario — implies long-vol (a straddle) is negative carry, so
Quant would actually prefer short-gamma/short-premium (e.g. an iron condor) into
the de-risked 7/28 print rather than a long straddle. Genuine disagreement beneath
a shared headline.

Sharpened EV table (incorporating the stub-overshoot and PT-cut evidence): Beat &
hold 28% at +3.0% (upside capped by broker cuts) → +0.84%; Flat/drift 40% at
+0.10% (12-day consolidation persists) → +0.04%; In-line fade 22% at -2.5% (a
stock 13% over fair value fades a no-surprise print harder) → -0.55%; Miss 10% at
-5.5% (more air beneath an over-anchored price) → -0.55%. Gross EV ≈ -0.22%, net of
costs ≈ -0.27% to -0.32% — flipped from Round 1's +0.40% to marginally negative.
Not enough magnitude to justify an outright short, but enough to make this a
cleaner skip than in Round 1.

Revised confidence to 76/100: both counterparties' fresh evidence, read
arithmetically, converges on "the re-rate is priced" (Bull's own stub implies price
above fair value; Bear's own price targets sit above spot); neither surfaced a
mechanism that moves the tape inside 17 days. Capped at 76 rather than higher
because the price-anchor discrepancy across personas and the still-missing live
2026-07-14 quote mean pre-event drift can't be fully verified.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** The Mobility spin-off is a completed, already-priced catalyst
(distribution closed 2026-07-01; SPGI flat ~-0.3% over the ~12 sessions since going
ex-Mobility), leaving no differentiated edge before the 2026-07-31 window closes.
Current price (~USD 438) already sits an estimated 12-14% above the modeled
sum-of-parts stub fair value; analyst price-target cuts have compressed the upside
tail even as ratings held Buy; and the only live catalyst in the window — 7/28 Q2
earnings/first standalone guide — is a near-symmetric event whose probability-
weighted EV does not clear execution/variance costs.

**Direction:** no_trade. **Confidence:** 74/100.

**Plan:** SPGI, action = no_trade. No entry, no exit, no position sized. Expected
profit ≈ -0.3% (i.e., inside the range where the edge does not clear costs) —
recorded, not filled.

**Dissent (preserved for post-mortem, not resolved):** Bull argues the 2026-07-28
print is not a coin-flip EPS variable but the first clean standalone guide (margin
framework, capital-return/buyback plans) carrying independent re-rating power that
the quant's 40%-weighted "flat" bucket underprices. Bear and the quant treat that
same guidance event as already discounted, folding it into a near-zero/negative-
skew EV. This is unresolved and load-bearing: if the standalone guide surprises to
the upside, the panel's no_trade call is wrong in the bullish direction. Secondary
unresolved item: an unreconciled price-anchor discrepancy across personas (an
unconfirmed USD 447 intraday peak / USD 430.50 swing cited by the bear versus the
flat USD 438-440 closes the others cite), which prevents fully verifying pre-event
drift.

**Rationale for confidence level:** Two of three personas (bear, quant)
independently converged on skip and *raised* confidence after rebuttal (75, 76);
the quant's own quantitative EV flipped from +0.40% to roughly -0.27% to -0.32%
once it absorbed the bull's best evidence, and the bull conceded the core
"re-rating still in progress" claim, cutting confidence to 55 and retreating to a
smaller, hedged structure. The panel-level conclusion — "no differentiated edge
that clears costs" — is corroborated from both qualitative and uncorrelated
quantitative angles, warranting a synthesis confidence (74) above any single
persona's directional confidence, while pricing expected profit near zero/slightly
negative to reflect that the edge does not clear costs.
