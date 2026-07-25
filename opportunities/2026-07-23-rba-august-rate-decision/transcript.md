# Debate transcript: 2026-07-23-rba-august-rate-decision

Strategy: debate-three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Dossier facts used

- RBA meets Aug 11, 2026. Economists split: CBA, NAB, ANZ predict hold at 4.35%; Westpac predicts a hike on persistent inflation risk.
- Impact window: 2026-08-11. Tickers: EWA, FXA.
- Source: https://www.aussie.com.au/insights/news/expert-predictions-rba-rates/ (accessed 2026-07-23)

## Institutional lessons injected

1. Anchor entry to a live pre-event quote, not the research-day price; if drifted >~0.5-1%, re-derive or void the trade.
2. When "catalyst reprices X higher" and X already rallied to its 52-week high pre-event, treat as priced-in.
3. Skip trades whose only positive-EV path is an unfillable pre-market conditional entry.
4. After a known regime shift, require a differentiated surprise vs consensus before shorting duration into a data print.

## Round 1 — Independent research

### Bull (sonnet)
Read: fractured 3-vs-1 forecaster consensus means market hasn't fully priced either outcome — the tradeable edge. Hike surprise -> AUD/FXA rallies (cleaner FX beneficiary via first-order rate-differential effect); EWA muddier (rate-sensitive equity drag partially offset by currency translation). Hold confirmed -> per lesson 4, largely priced in, fade not chase.

Proposed: Long FXA into Aug 11, sized for hawkish-surprise scenario (~30-35% probability-weighted, explicitly not the modal outcome — "paying for optionality against the minority-but-plausible view"). Entry anchored to live pre-event quote (T-1/T-0) per lesson 1, re-derive EV if drifted >0.5-1%. Exit within 1-2 sessions post-decision. Avoid EWA as primary vehicle. Confidence: moderate, minority-view bet; would insist on checking the executable entry has positive EV per lesson 3.

### Bear (sonnet)
1. The 3-1 split is not an edge — it's already priced. Majority-consensus rate calls get priced in well before the meeting. Westpac's hike call is a public, 19-day-old outlier with no fresh data in the dossier, sourced from a consumer-finance content aggregator (aussie.com.au), not primary/Bloomberg-consensus data.
2. What blows up either side: hold-with-hawkish-guidance (headline matches consensus but statement tone moves AUD/FXA regardless); a CPI/wage print before Aug 11 could flip the consensus itself.
3. Neither EWA nor FXA is a clean instrument — EWA diluted by bank/miner/property composition; FXA has tracking drag and thinner volume.
4. Binary, single-catalyst, three-weeks-out risk with zero informational edge today — dispersion alone isn't edge without a variant/fresh-data view.

Recommendation: SKIP. If forced to keep on the board, token/observation-only size, revisit only on fresh CPI print or RBA pre-meeting speech.

### Quant (opus)
P(hold)=0.78, P(hike)=0.20 — inertia-adjusted from naive 3:1 vote count (correlated forecasters, strong base-rate inertia for "no change" at scheduled meetings), explicitly flagging that forecaster consensus ≠ market-implied probability and that the dossier contains **no market-implied odds** — the critical missing input.

Magnitude assumptions (stated, not measured): surprise hike -> FXA +0.9%; consensus-matching hold -> FXA -0.15%. EWA rejected on instrument-construction grounds: unhedged equity+FX legs (rate-sensitive equities down, AUD up) roughly cancel under a hike, netting ~0 — a coin-flip-with-a-spread, not an edge.

EV math (20bp round-trip friction assumed for FXA):
- Long FXA: 0.20(0.90) + 0.78(-0.15) = +0.063% gross -> **-0.137% net** (generous case). At 25% market-priced odds framing: **-0.262% net**.
- Short FXA: **-0.263% net**; no value of p(hike) makes short FXA EV-positive — payoff asymmetry is intrinsic (small win on the likely outcome, large loss on the unlikely one).
- Breakeven for long FXA requires p(hike) > 33.3%; estimate is 20%.

Execution reality: RBA announces ~04:30 UTC Aug 11 while US cash markets are closed — the entire move arrives as an overnight gap. Any "wait for decision, then enter" plan is unfillable (lesson 3 failure mode). The only technically executable structure (enter Aug 10 US close / exit Aug 11 US open) IS the negative-EV coin flip computed above, with worse-than-normal slippage.

Gate checks: Lesson 1 unmet (no price anchor anywhere in the dossier). Lesson 4 unmet (Westpac dissent is public/stale, not a differentiated surprise — "persistent inflation risk" is consensus knowledge, not proprietary insight).

Recommendation: **NO TRADE**. Confidence 82/100 — robust across the whole plausible probability range (every EV cell negative in both directions), though magnitude-sensitive (a hypothetical +2% AUD reaction instead of +1% would flip long-FXA breakeven to p>10%).

## Round 2 — Rebuttal

### Bull rebuttal
Concedes Quant's EV arithmetic is basically right; pushes back only on the magnitude assumption (argues it could plausibly be 1.3-1.5% instead of 0.9%, but explicitly admits no dossier-grade evidence for this — "a genuine weakening of my position, not a full concession"). **Fully concedes the execution-reality point**: no revised structure survives the overnight-gap constraint; the original "exit within 1-2 sessions" plan is dead; trading spot AUD/USD directly would help but is outside the instrument scope. Credits Bear's point that the Westpac dissent's sourcing (secondary aggregator, not primary bank research) is weaker than Bull originally treated it.

**Final: converges to NO TRADE.** Would only keep a token speculative overnight-gap tail position if forced, explicitly flagged as non-evidence-based, not a real recommendation.

### Bear rebuttal
Adopts Quant's arithmetic as the harder, more robust floor versus its own "priced in" framing — the trade fails cost math even if Bear's market-efficiency claim is wrong. Notes Bull's 30-35% P(hike) is undefended versus Quant's derived 20%. Flags genuine daylight between the two NO-TRADE arguments: Bear's is informational (would soften with new data), Quant's is structural (needs concrete p>33.3%/magnitude bar to clear, independent of whether info is "priced in"). The US-market-closed execution finding hardens Bear's original hawkish-hold risk scenario into "unhedgeable overnight risk regardless of direction, carried blind."

**Final: hardens to full SKIP** — would not even keep token/observation size, given the unhedgeable overnight structure. Revisit only on fresh CPI/wage data or a market-implied-odds data point.

### Quant rebuttal
Ran Bull's own 30-35% P(hike) through the EV model: at p=0.30, net EV = -0.035%; at p=0.35, net EV = +0.018% (breakeven noise) at 20bp friction. Under realistic 30-40bp overnight-gap friction, breakeven requires p*=47.6% — near a coin flip, which Bull's range doesn't clear. Shows sizing cannot fix a negative sign (Kelly f* <= 0 on non-positive edge). Shows Bull's own drift-tolerance (0.5-1%) is 30-60x the entire computed edge (1.75bp at best), making the stated risk gate meaningless.

Confirms Bull's "exit within 1-2 sessions" collapses into the same structure already flagged: no branch escapes the ~9-hour US-market-closed window; holding a second session adds ~30x the edge in pure noise with zero incremental EV.

Distinguishes its own claim from Bear's explicitly: these are two *independent* gates that respond in **opposite directions** to a hypothetical revealed market-implied probability (e.g., a disclosed 22% would refute Bear's "priced in" claim while confirming Quant's negative verdict) — so 3-way agreement here should not be read as mutual corroboration.

Ran a 3-state model (hike / hawkish-hold / dovish-hold) deliberately built to be generous to Bull: net EV +0.030% at 20bp friction, but **-0.120% at realistic 35bp gap friction** — the trade still fails even under a model constructed to rescue it.

**Final: NO TRADE, confidence raised to 85/100.** Explicitly rejects Bear's token/observation-size fallback ("token size on a negative-EV trade is a small guaranteed cost purchasing free data — just record the outcome without capital at risk"). Lists three falsifiable conditions that would flip this to a trade in a future round: (1) revealed market-implied odds diverging widely from the 20% estimate; (2) an empirical FXA gap-distribution replacing the invented magnitudes; (3) a genuinely convex instrument.

## Round 3 — Synthesis (opus)

**Hypothesis:** The fractured 3-1 RBA forecaster split does not create a tradeable edge in EWA or FXA ahead of the Aug 11, 2026 decision. On a derived P(hike)~20% (vs a required p>33.3% at 20bp friction, p>47.6% at realistic 30-40bp gap friction) and an assumed ~0.9% FXA hike-response, every executable structure is net-negative EV, and the announcement lands ~04:30 UTC with US cash markets closed, so the move arrives as an unfillable overnight gap rather than a fillable price path. EWA is separately rejected on instrument construction. The dossier also lacks the two inputs that could overturn this (market-implied odds, live price anchor). Direction: **none**. Confidence: **84/100**.

**Plan:** No trade. Ticker FXA, action `no_trade`, no entry/exit/expected profit recorded.

**Dissent (for post-mortem):** The sharpest unresolved disagreement is Bull vs. Quant on the **magnitude input** — the single parameter the whole NO-TRADE verdict rests on, and neither side sourced it empirically. Quant assumes a hike surprise moves FXA ~+0.9% (hold ~-0.15%), giving breakeven p*=33.3% (20bp friction) / p*=47.6% (realistic gap friction) — both above Quant's own 20% estimate and above Bull's undefended 30-35%. Bull argued the true response could be 1.3-1.5%+ but explicitly conceded no dossier-grade evidence exists for it. Quant conceded the verdict is "magnitude-sensitive": a +2% move would drop breakeven to p>10%, which even Quant's own 20% clears comfortably. **The unanimity is unanimity over an invented number** — at 0.9% the trade is dead at any plausible probability; at ~2% it is live at Quant's own probability estimate. Nothing in the transcript resolves which magnitude is correct.

Secondary unresolved point: Bear's "already priced in" (informational) and Quant's "fails cost math regardless" (structural) are independent gates that would respond in *opposite* directions to a revealed market-implied probability — their apparent agreement here should not be read as corroboration, per this project's own lesson on false consensus reached under a data blackout (no market-implied odds, no live price anchor, and a 19-day-stale, secondary-sourced dissent).

**Reopen conditions:** (1) an empirical FXA overnight-gap distribution around RBA decisions showing a hike-surprise response materially above ~1.5-2%; (2) an actual market-implied hike probability (ASX 30-day interbank cash rate futures or OIS) diverging widely from ~20%; (3) a genuinely convex instrument (options) that survives the ~9-hour US-market-closed execution window instead of a delta-one ETF that can only be entered at the Aug 10 close and exited at the Aug 11 open.
