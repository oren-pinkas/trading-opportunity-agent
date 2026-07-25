# Research Debate Transcript — NVTS Q2 2026 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- Opportunity: `2026-07-23-navitas-q2-2026-earnings`
- Strategy: `debate-three-round-panel` (bull/bear sonnet, quant/synthesizer opus)
- Debate run: 2026-07-25
- Event: NVTS reports Q2 2026 results after close Monday Jul 27 2026. Prior two prints
  averaged roughly 13.6% one-day moves. Guide: USD 10.0M revenue / 39.25% gross margin
  midpoint. Source: [Navitas Semiconductor to Report Q2 2026 Financial Results on Monday](https://www.stocktitan.net/news/NVTS/navitas-semiconductor-to-report-q2-2026-financial-results-on-monday-o9f0gizwbm89.html) (stocktitan.net, accessed 2026-07-23T18:53:42Z)

## Institutional memory injected

1. (NKE, 2026-07-06) Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short.
2. (NKE, 2026-07-06) Discount post-earnings negative base rates when the name is already at/near its 52-week low.
3. (TSLA, 2026-07-06) Set intraday exits at least one minute inside the session boundary (19:59:00Z, not 20:00:00Z) to avoid a silent no-fill on a 1-minute-bar provider.
4. (TSLA, 2026-07-06) Add a pre-simulation timestamp guard validating both legs map to available US-equity bars.
5. (DAL, 2026-07-12) A catalyst that already drove a large multi-week run is priced in — don't re-bet the same fundamental as a fresh gap trigger.
6. (DAL, 2026-07-12) When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size directional position.
7. (LEVI, 2026-07-12) When the highest-confidence panelist says directional EV is ~0 and the only positive-EV structure is out of mandate, log NO TRADE — don't manufacture a position "for the learning loop."
8. (LEVI, 2026-07-12) Anchor entry prices to a live quote fetched at the actual entry timestamp.

---

## Round 1 — Independent research

### Bull (Catalyst-hunter, sonnet)

Thesis: NVTS is a high-beta earnings mover with a proven track record of large, tradable
one-day reactions — prior two prints averaged ~13.6% one-day moves. That's a structural
volatility regime because Navitas (GaN/SiC power semis for AI datacenter power delivery
and EV) is a small-float, high-narrative story stock where guidance beats/misses get
amplified by momentum flow. Street bar of USD 10.0M revenue / 39.25% gross margin
midpoint is soft/digestible given the AI-datacenter power design-win narrative (Nvidia
800V HVDC architecture partnership). Any incremental commentary on design-win traction,
customer ramp timing, or gross-margin inflection gives room to run past the historical
average.

Proposed action: defined-risk long via a short-dated weekly call (expiring Jul 31),
entered Monday Jul 27 near close (19:59 ET-equivalent bar, per lesson 3/4), exit at
Tuesday Jul 28 open or within the first 30 minutes. Alternative: long shares, same
timing, if options liquidity/spreads are poor.

Flagged: could not confirm live price/liquidity or 52-week positioning (data provider
rate-limited on check).

### Bear (Skeptic, sonnet)

This is a volatility event, not a directional edge, and skews toward "sell the news"
risk on the long side. The AI-power narrative (Nvidia 800V HVDC) is already priced in —
the print itself (USD 10M revenue) can't confirm a multi-year TAM story; it's a
rounding error against the market cap the narrative has built. Per lesson 5, don't
re-bet an already-run narrative as a fresh gap trigger. The 13.6% base rate is about
magnitude, not direction, with no stated skew — argues for straddle-thinking, not
conviction.

Risks to a long: soft core (non-datacenter) demand hidden behind a beat; cash burn/
dilution overhang; hedged datacenter-timing language gets sold hard given how
narrative-driven the move has been. Risk to a short: a concrete Nvidia/datacenter
revenue-recognition timeline could re-ignite the speculative bid.

Net: wants the quant's EV math before committing; prior is this fails the
no-un-hedgeable-edge filter (lesson 1) unless news flow is unambiguous.

### Quant (Pragmatist, opus)

Data note: `toa price NVTS --provider twelvedata` returned HTTP 429 on both attempts —
no live anchor price, so cannot verify entry/exit map to available bars (lessons 3/4/8).

Base rate: n=2 prints, ~13.6% mean absolute one-day move — this is anecdote, not a base
rate (huge standard error), and says nothing about direction. Assumes P(up)=50%.

EV calc for an unhedged directional long:
- P(up)=0.5 at +13.6%, P(down)=0.5 at -13.6% → gross EV = 0.0%
- Costs: ~0.9% all-in (spread/slippage on close entry + gap-open exit in a fast tape)
- **Net EV = -0.9%.** Break-even requires P(up) >= 53.3%; nothing in the dossier (a
  routine date announcement and consensus-level guide) supplies that.

Adverse-tail-to-edge ratio effectively infinite (13.6%+ one-sided risk vs. 0% gross
edge).

**Recommendation: NO TRADE.** Fails the lesson-1 filter. Won't manufacture a quarter-size
position for the learning loop (lesson 7). A straddle is the only coherent structure,
but implied vol is almost certainly priced at/above 13.6%, making it EV-negative after
crush — and it's out of mandate anyway. Will only move off NO TRADE given a quantified
directional asymmetry, not narrative.

---

## Round 2 — Rebuttal

### Bull rebuttal

Quant's P(up)=50% is a hidden bearish assumption dressed as neutrality — with n=2
there's no basis to anchor at 50% either. The EV math also treats the call as if it
were a symmetric bet on the underlying, ignoring that a call's payoff is capped-loss/
uncapped-upside — restate EV with the actual instrument before declaring -0.9% net.

On break-even: NVTS management has a pattern of leading capex/design-win commentary in
the release itself, which is why prior prints moved big same-day — information content,
not vibes. To the bear's "priced in": that applies to diffuse expectations, not a
discrete binary disclosure (design win moving from pipeline to revenue) landing in 48
hours. Bear can't simultaneously call the print a "rounding error" and worry a short
gets squeezed by that same print.

Would change mind if quant can show current call IV already prices >13.6% expected
move with a real quote, not an assumption. Flags price-data unavailability as now the
binding constraint on executability.

### Bear rebuttal

Quant's math is confirmation of my caution, not a counterweight — -0.9% net EV,
break-even P(up)>=53.3%, no edge supplied. That's exactly the "unless news flow is
unambiguous" condition flagged in Round 1, and it hasn't been met.

What the bull missed: the entire case rests on magnitude with zero argument for
direction; never addressed the "sell the news" risk that the AI narrative already in
the stock gets faded absent a hard datacenter-revenue timeline. Concede NVTS is
structurally volatile and a straddle would be the coherent structure if in mandate —
but the quant already showed IV is priced at/above 13.6%, making that EV-negative too,
and it's out of mandate regardless.

Net: nothing moves off NO TRADE without a quantified directional catalyst.

### Quant rebuttal

Retried `toa price NVTS --provider twelvedata` three more times this round
(2026-07-24T19:59Z x2, 2026-07-23T19:59Z x1) — all HTTP 429. Four total failed
attempts across two rounds: no verified anchor price, no bar availability, no spread/
liquidity data. An unpriceable plan is unfillable regardless of thesis quality.

On the bull's "room to run past historical average": arithmetically backwards. With
n=2, the standard error is on the order of the spread between the two observations
themselves — 13.6% cannot be treated as a floor. The mechanism is inverted too: a
stock with a two-print history of ~13.6% moves has options already priced for that
magnitude — market makers set the bar where the narrative already is. A soft,
digestible guide is a reason the bar is low, not a reason the reaction is up.

Nothing quantified moves P(up) off 50%. The bear's "sell the news" risk, if anything,
pushes P(up) below 50%, worsening EV.

**Unchanged: NO TRADE.** The bull's weekly call is strictly worse than shares — it adds
vol crush and theta to a coin flip.

---

## Round 3 — Synthesis (opus)

### Hypothesis
- **Statement:** NVTS Q2 2026 earnings is a high-magnitude, direction-unknown
  volatility event, not a directional edge. The only quantified estimate (n=2 prior
  prints, ~13.6% mean absolute move, no directional skew) supplies magnitude with zero
  directional information; break-even for an unhedged directional long requires
  P(up) >= 53.3% after ~0.9% all-in frictions, and nothing in the research supplies
  that edge. The bull's AI-datacenter/Nvidia 800V HVDC narrative is a magnitude
  argument dressed as a direction argument, and its asymmetric-payoff rebuttal was
  never backed with actual call IV or skew quotes. Independently, live price data was
  unavailable across four `toa price NVTS --provider twelvedata` attempts (HTTP 429),
  so no anchor price, spread, or bar availability could be verified — the plan is
  unpriceable and therefore unfillable.
- **Direction:** none
- **Confidence:** 82

### Plan
- **Ticker:** NVTS
- **Action:** none (NO TRADE)
- **Entry:** none — no verified anchor price exists (4/4 HTTP 429)
- **Exit:** none
- **Expected profit:** 0% (explicit no-trade). Counterfactual EV of the bull's proposed
  structure had it been taken: ~-0.9% for long shares, worse for the Jul 31 weekly call
  once post-print IV crush and theta are added to a coin flip.

**Recommendation: do not act.**

Counterfactual only (not recommended): the only structure with a coherent EV story
would be a delta-neutral long straddle/strangle on the Jul 31 expiry, entered near the
Mon Jul 27 close and exited at/shortly after the Tue Jul 28 open — long vol to harvest
a ~13.6%-class move without taking a direction. Rejected on two independent grounds:
(1) a stock with a two-print history of ~13.6% moves likely already has options priced
at or above that level, making the structure EV-negative after crush; (2) it is out of
mandate. If forced into a directional position, shares (not the weekly call) strictly
dominate by removing vol-crush/theta from a 50/50 bet — but even this is expected to
lose ~0.9% per instance and should not be taken merely to generate a learning-loop data
point (lesson 7).

### Dissent

The strongest unresolved disagreement: whether P(up)=50% is a neutral prior or a
smuggled bearish assumption, and downstream, whether the priced IV actually exceeds the
realized-move distribution. The bull's sharpest point went unanswered on its own terms
— with n=2 there is no empirical basis for anchoring at 50% either, and a long call's
capped-loss/uncapped-upside payoff means a symmetric ±13.6% EV formula understates it.
The quant's counter (market makers price the bar where the narrative already is, so IV
is at/above 13.6%) is a mechanism argument, not a measured one — no call IV, skew, or
straddle price was ever quoted by either side. Unresolved because the evidence that
would settle it (a live option chain or spot quote) was unobtainable — 4/4 HTTP 429s.
The panel converged on NO TRADE partly by argument and partly by data starvation, and
those two causes are entangled in the record.

**Post-mortem falsifiable question:** did NVTS move >=13.6% on 2026-07-28, and if so,
was the Jul 31 straddle priced below the realized move? If yes, a real long-vol edge
existed and was declined on an unverified assumption plus a mandate that excludes the
only correct structure. If the straddle was priced at/above the realized move, the
quant's mechanism argument was correct and NO TRADE holds on the merits. Secondary
check: was the direction up (bull vindicated on P(up)>50%) or a "sell the news" fade
(bear's unaddressed risk, pushing P(up)<50%, making NO TRADE conservative-but-correct)?

Also note the recurring infrastructure theme: a research pipeline that cannot obtain a
price cannot distinguish "no edge" from "unmeasured edge" — this is (at minimum) a
repeated `toa price` data-availability failure pattern worth tracking across
opportunities.
