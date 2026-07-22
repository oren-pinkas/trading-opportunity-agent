# Debate transcript — 2026-07-16-eli-lilly-q2-earnings

Strategy: `debate-three-round-panel`. Personas/models: bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus).
Paper-trading simulation only. Not financial advice.

Price anchor: `toa price LLY 2026-07-16T13:35:00Z --provider twelvedata` = USD 1147.00.

Relevant institutional lessons injected (via `toa lessons-relevant --type earnings --tickers LLY`):
- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short. (NKE, 2026-07-06)
- Discount post-earnings negative base rates when the name is already at/near its 52-week low. (NKE, 2026-07-06)
- A catalyst that already drove a large multi-week run to a 52-week high above the Street mean target is priced in — do not re-bet the same fundamental as a fresh gap trigger. (DAL, 2026-07-12)
- When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size directional position. (DAL, 2026-07-12)
- A no-edge coin-flip still books real losses — do not manufacture a minimal directional position "for the learning loop" when the quant says directional EV is ~0. (LEVI, 2026-07-12)
- Anchor entry prices to a live quote fetched at the actual entry timestamp, not a stale pre-move reference. (LEVI, 2026-07-12)

## Round 1 — Independent research

### Bull (confidence 58/100)

Eli Lilly reports Q2 2026 earnings on 2026-08-05 — the first full quarter of data since Medicare Part D began covering GLP-1 weight-loss drugs on 2026-07-01 (per dossier). This is a structural TAM-expansion event: Medicare covers 65M+ enrollees, and even a low-single-digit attach rate on Zepbound/Mounjaro is a step-change in addressable market. The print is the first data point management can point to for utilization trends, formulary uptake, and channel dynamics under the new coverage regime.

The dossier also flags an "oral-obesity-drug race with Novo Nordisk" (CNBC, 2026-06-08). Lilly's oral candidate orforglipron (general knowledge, not in dossier) has been the biggest swing factor in LLY's re-rating; Q2 commentary on regulatory timeline, manufacturing scale-up, or head-to-head data versus Novo's oral semaglutide gives the market a fresh anchor to extrapolate peak-sales estimates.

Evidence: dossier event date and Medicare-coverage-start facts; CNBC 2026-06-08 sourcing; price anchor USD 1147.00 (toa price, 2026-07-16T13:35Z). General knowledge (labeled): LLY's incretin franchise has driven 6 consecutive quarterly beats through 2025; Novo has ceded U.S. obesity share amid Wegovy execution issues.

Proposed structure: long call spread (~5% OTM buy / ~12-15% OTM sell) entered 3-5 sessions pre-earnings, exit 1-2 sessions post-print, re-anchored to a fresh quote at entry (not the stale USD 1147 reference). Avoids long equity (capital-inefficient at $1000+/share) and naked calls/straddles (IV-crush exposure).

Confidence 58/100 — real, dateable catalyst, not a stale rehash, but capped by lack of options-pricing/IV data and no confirmed 52-week-range context in the dossier.

### Bear (confidence 35/100 for a short-side edge)

The Medicare Part D GLP-1 coverage start was telegraphed months in advance — the CNBC piece (2026-06-08) reports on a rollout already in motion, not breaking news. Sell-side models almost certainly already embed a Medicare-driven demand ramp. LLY has beaten and guided up repeatedly through the GLP-1 cycle, raising the bar each quarter — an in-line-to-good print risks a "sell the news" reaction near record levels (price anchor USD 1147, 2026-07-16T13:35Z).

The oral race with Novo (orforglipron vs. oral semaglutide) is a multi-year regulatory/commercial story; nothing in the dossier suggests a decisive readout falls inside this specific earnings window — treating it as a Q2 catalyst conflates a slow-moving theme with an event-driven trade.

Specific risks: rollout friction (prior authorization, plan-level formulary lag) understating Medicare contribution; CMS/IRA drug-price-negotiation pressure on net pricing/rebates for exactly this drug class; orforglipron regulatory/safety-signal risk (GI tolerability is a class-wide issue); Novo share gains via its own oral candidate; stretched valuation at a premium multiple with a crowded, widely-owned long consensus; no confirmed data-drop inside the window.

Proposed action: NO TRADE, or at most a small defined-risk put spread (never naked short) if cheap convexity is available. Confidence 35/100 — below the institutional no-trade threshold; per the lesson, sub-45 confidence without a decisive asymmetric edge should not be sized as a directional bet.

### Quant (confidence 40/100)

Critical structural point: Q2 2026 (Apr-Jun) is reported 2026-08-05 but the quarter itself ends 2026-06-30 — **before** Medicare coverage started 2026-07-01. The printed quarter contains **zero** Medicare-coverage revenue. This is purely a guidance/commentary event, not a results event, which raises variance on the call (framing, early data) while the underlying Q2 numbers are a known-ish base.

Assumed (general-knowledge/labeled) LLY earnings-day move distribution: mean absolute ~6%, IQR 5-9%, tails to ±12-15%. Direction assumed ~50/50 (slight bias toward "beat is expected" given premium multiple). Widened tail estimate for this event to IQR ~5-9%, tails ±15%, given the two-sided oral-race commentary risk.

EV math (anchor USD 1147.00, 2026-07-16T13:35Z): assumed implied move ~7% vs. expected realized ~6% →
- Long ATM straddle: EV ≈ -1% to -1.5% of notional (IV crush kills the losing leg).
- Long ATM calls: EV ≈ -1.5% (paying vol on a coin-flip direction).
- Call spread (ATM buy / +7% OTM sell, ~2.2% net debit): EV ≈ ~0% pre-cost, negative after ~0.3-0.5% two-leg slippage.

Adverse-tail-to-edge ratio ≈ 5-7x; confidence 40 < 45 threshold; positive tail is un-hedgeable cheaply. All three institutional no-trade conditions met (sub-45 confidence, negative-to-zero net EV, high adverse-tail-to-edge ratio).

Proposed action: NO TRADE. Confidence 40/100. Flip trigger: implied move compresses to ≤4.5% while realized estimate holds ~6%.

## Round 2 — Rebuttal

### Bull (revised confidence 48/100)

Concedes the calendar fact: Q2 revenue is 100% pre-Medicare-coverage, so a "Q2 revenue beats on Medicare units" thesis is dead on arrival. Reframes: the tradeable event is management's forward framing 35 days into the rollout — real, non-consensus early data (PA approval rates, script volumes, payer mix) that sell-side is currently guessing at. Downgrades thesis from "TAM-expansion results event" to "first-look forward-guidance event."

Concedes "coverage exists" is stale (per bear) but argues "coverage is working" is not priced: early enrollment/utilization numbers, PA friction rates (two-sided unknown), Q3 guidance cadence (front- vs. back-loaded Medicare ramp), and orforglipron regulatory-timeline language are all distinct, unpriced, idiosyncratic catalysts.

On quant's EV math: concedes straddles/naked calls are negative EV given the vol arithmetic. Pushes back that a capped call spread is a directional-skew bet, not a vol bet — max loss is the net debit, so the 5-7x adverse-tail-to-edge ratio (a tail-risk metric) doesn't directly transfer. Estimates direction closer to 55/45 (not 50/50) given management's track record of not self-inflicting bad news on a lobbied-for tailwind, and because the bad-news case is already consensus — but explicitly flags this as a "soft, non-rigorous" estimate.

Flip conditions: implied move ≥7.5% at entry (confirms rich vol, no offsetting skew) → drop to no-trade; evidence Medicare enrollment/PA data already leaked pre-print → drop to no-trade; no scheduled orforglipron regulatory update in this window → thesis weakens to "hope for good vibes," insufficient alone.

Revised: still favors the call spread but frames it as a cheap, capped-risk bet on a modest positive skew, confidence 58 → 48 (barely above the 45 threshold).

### Bear (revised confidence 25/100)

Explicitly agrees the quant's "zero Medicare revenue in the reported quarter" point strengthens the priced-in thesis — same fact, two angles: no fresh numeric surprise means any Aug-5 move is a tone/framing reaction, not a fundamentals reaction, a thin basis for a directional bet.

Rebuts the bull's "commentary alone is enough" claim: the evidence bar for a commentary-only catalyst to move a mega-cap is high — needs a quantified guidance change or an unambiguous regulatory-timeline statement, not generic "reiterate confidence" language (already discounted). The bull's own framing concedes there's no confirmed data-drop in the window, making the catalyst contingent on management saying something unscripted — a low base-rate trigger.

Reconciles with quant's EV math: puts/straddles are also roughly breakeven-to-negative EV, so a naive short has the same edge problem as the bull's calls. Concedes it cannot defend a "small put spread" carve-out without confirmed put/call skew or positioning data it doesn't have — converges toward NO TRADE rather than defending the carve-out.

Flip conditions: confirmed pre-earnings put/call skew showing puts structurally cheap vs. calls at equivalent delta; a specific pre-earnings CMS/IRA pricing or Novo oral-semaglutide news item shifting competitive-share expectations; evidence of stretched positioning (elevated call OI/skew, aggressive analyst-revision clustering).

Revised: NO TRADE, confidence for a tradeable short-side edge 35 → 25.

### Quant (revised confidence 42/100)

Stress-tests own Round 1 assumption: concedes the 6% realized-move estimate may be downward-biased for this variance-widening event (first Medicare-era guidance + competitive pipeline race); re-centers realized to 7-8%.

Three-scenario EV run (anchor USD 1147.00):
- (a) implied 7% / realized 6% → net EV ≈ -1.0% to -1.5%
- (b) implied 6.5% / realized 6.5% (bear's "priced-in" logic applied symmetrically to both implied and realized) → net EV ≈ -0.4% to -0.6%
- (c) implied 7% / realized 8% → net EV ≈ +0.4% to +0.6%, but inside quant's own ±1.5-point realized-move error bar

Probability-weights these 35/40/25 → blended net EV ≈ -0.5%.

Responds to bull: agrees commentary is a real catalyst for magnitude, but notes this argument supports a long **straddle**, not the bull's capped **call spread** — if the fat right tail fires to +15%, the spread is already maxed and forfeits everything beyond, while eating two-leg slippage. "The bull has identified the right catalyst and the wrong instrument."

Responds to bear: resolves the "priced in → lower implied or lower realized?" tension numerically — telegraphing argues implied should be ~6-6.5% (cheaper, good for long vol) but also that realized stays ~6% (surprise gap compressed) — net effect is EV stays flat-to-negative (scenario b), not positive. Only the corner where implied compresses to ≤4.5-5% while realized holds ~6-6.5% would rescue the trade, and there's no evidence implied is that cheap into this print.

Final verdict: blended net EV ≈ -0.5% of spot after ~0.5% round-trip slippage; the one positive-EV scenario carries only 25% weight and sits inside the quant's own ±1.5-point realized-move error band — no cost-surviving edge with acceptable confidence. All three institutional no-trade conditions remain met.

Revised: HOLDING NO TRADE, confidence 40 → 42. Flip trigger unchanged: implied ≤5% while realized estimate holds ≥6.5%.

## Round 3 — Synthesis (convergence)

**hypothesis:**
- statement: LLY's Q2 2026 print (reported 2026-08-05) is a commentary/forward-guidance event, not a results event — the reported quarter (Apr-Jun) closed 2026-06-30, one day before Medicare Part D GLP-1 coverage began 2026-07-01, so it contains zero Medicare GLP-1 revenue. The only genuinely unpriced element is early "coverage-is-working" color (35 days of PA/utilization/enrollment data, Q3 guidance cadence, orforglipron regulatory-timeline language). That edge is real but soft, un-quantified, and too small to overcome option-vol arithmetic: implied ~7% vs. realized ~6-8% yields a blended net EV of roughly -0.5% across the panel's own probability-weighted scenarios.
- direction: neutral
- confidence: 40

**plan:**
- ticker: LLY
- action: no_trade
- entry: none
- exit: none
- expected_profit_pct: 0.0
- rationale: No instrument clears the bar. Naked calls and straddles are negative EV (implied ≥ realized); the bull's capped call spread nets ~0% pre-cost and negative after slippage; a bear put spread has no confirmed skew/positioning data to justify it. The single positive-EV corner (implied 7% / realized 8% long straddle) carries only ~25% weight and is statistically indistinguishable from noise inside the quant's own ±1.5-point realized-move error bar. Two of three panelists sit well below the 45 no-trade threshold (bear 25, quant 42); the third (bull 48) cleared it only barely and on an admittedly "soft, non-rigorous" 55/45 directional guess. Per the LEVI institutional lesson, a no-edge coin-flip books real losses — no trade is manufactured for the learning loop. Flip conditions: implied compresses to ≤5% while realized estimate holds ≥6.5%; confirmed put/call skew mispricing or elevated call OI signaling stretched positioning; a pre-earnings CMS/IRA pricing or Novo oral-semaglutide news catalyst.

**dissent:**
The sharpest unresolved disagreement is instrument-vs-catalyst. The bull argues the "coverage-is-working" early-rollout signal is genuinely unpriced and modestly positive-skewed (~55/45) because management has a track record of not self-inflicting bad news on a tailwind it lobbied for, and the bad-news case is already consensus. Quant partially concedes the bull "identified the right catalyst" but insists the bull chose the wrong instrument — if the thesis is fatter-tailed variance, a long straddle dominates a capped call spread, yet that straddle only pays in the ~25% implied-7/realized-8 world, which quant cannot distinguish from noise. Neither side resolved whether the bull's directional skew is real signal or hindsight-flavored narrative. If LLY prints a large directional move on 2026-08-05, the post-mortem should ask: was no-trade correct on EV (a straddle would have won but was un-forecastable ex-ante), or did the panel under-weight a genuinely knowable management-guidance skew that a call spread would have captured?

**Overall synthesis:** The panel converged on NO TRADE from three independent directions. Quant's foundational observation — Q2 ends 2026-06-30, before the 2026-07-01 Medicare start, so the reported quarter carries zero Medicare GLP-1 revenue — reframed the event and forced the bull to downgrade from a "TAM-expansion results event" to a "first-look forward-guidance event" (confidence 58 → 48). The bear (35 → 25) agreed this same fact strengthens the priced-in/sell-the-news thesis and conceded its put-spread carve-out was indefensible without skew data it doesn't have. Quant (40 → 42) generously re-centered realized move up to 7-8% to honor the bull's variance-widening argument, ran three probability-weighted scenarios, and still landed at a blended net EV ≈ -0.5% — negative even after conceding ground. The adverse-tail-to-edge ratio (~5-7x) and the fact that the only positive-EV instrument (long straddle) sits in the least-likely, noise-indistinguishable corner mean all three institutional no-trade conditions hold. The bull nominally cleared 45, but on its own admission the directional edge is soft and the capped call spread nets ~0% pre-cost. The panel declines the trade and records the instrument-vs-catalyst dissent for post-mortem grading.
