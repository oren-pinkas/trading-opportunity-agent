# Debate transcript — Wolfspeed v. Navitas patent suit (NVTS, WOLF)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Event:** Wolfspeed (WOLF) filed a GaN power-semiconductor patent infringement suit against Navitas Semiconductor (NVTS) in Delaware federal court; NVTS fell 7% on the filing news. Single source: [Yahoo Finance](https://finance.yahoo.com/technology/articles/navitas-semiconductor-shares-drop-wolfspeed-133256201.html), accessed 2026-07-13T19:27:39Z. impact_window: 2026-08-13 (dossier reference date, ~1 month out).
- **Strategy:** three-round-panel. **Personas/models:** bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus).
- **Price data:** twelvedata has no coverage for this event's 2026 date (beyond provider range); all price references in this debate are the deterministic `--provider stub` fake price, explicitly flagged wherever used and given zero evidentiary weight.
- **Verdict:** NO-TRADE / PASS. direction=none, confidence=74.

---

## Round 1 — Independent research

### Bull (LONG NVTS, fade-the-overreaction)
- 7% drop on a mere complaint filing (not a ruling or injunction) is a headline-risk reaction, not a fundamentals reaction. Delaware patent suits take 12-24+ months to reach claim construction or trial — nothing structurally changes NVTS's business by Aug 13.
- Reads the suit as possible incumbent FUD tactic (WOLF, the larger SiC/GaN player, pressuring a faster-growing smaller rival) rather than necessarily a strong claim.
- **Action:** buy NVTS, entry ~2026-07-17 to 07-21 (after initial vol settles), exit ~2026-08-10 to 08-12 (ahead of impact window, avoiding incremental filing/injunction risk).
- Risks acknowledged up front: injunction/ITC risk (second leg down), customer-confidence contagion (design-win pauses = fundamental hit), thin single-source evidence.

### Bear (NO TRADE)
- The 7% move already priced the headline shock; patent suits don't resolve in a month, so there is no fundamental catalyst inside the impact window.
- Risks: timeframe mismatch, single-source problem (only one wire item, no docket detail), relief-rally risk, litigation base rates favor defendants, WOLF's own balance-sheet distress/prior restructuring history caps any long-WOLF thesis, motive-to-litigate-as-settlement-signal (a distressed plaintiff may want a licensing deal, not judgment), liquidity/crowding risk.
- What would change mind: evidence of a preliminary injunction motion (CAN be adjudicated within weeks — a genuine near-term catalyst), confirmation the suit seeks a sales injunction.
- **Action:** no trade as framed; if forced, only a small contrarian long-NVTS fade on clear overshoot evidence, never long WOLF.

### Quant (NO STATISTICAL EDGE)
- Base rates, 1-month horizon after a defendant-side patent-suit drop: P(partial reversion) ~45% (+3-4%), P(flat) ~30% (~0%), P(further decline) ~25% (-6 to -8%).
- Base-case gross EV ≈ -0.025% (essentially zero); net EV after ~40-50bps round-trip costs ≈ -0.48% (negative). Optimistic flex (P_up 50%, +4%; P_down 20%, -6%): gross +0.95%, net +0.50% — thin, within parameter uncertainty.
- Kelly sizing ~0. **Conclusion:** no statistical edge — catalyst/timeline mismatch (zero legal catalysts inside the window), EV≈0 gross and negative after costs, asymmetric tail the wrong way (down-case bigger than up-case).
- If forced: small long-NVTS reversion tilt ≤0.25% of book, only on evidence of panic-volume overshoot.

---

## Round 2 — Rebuttal

### Bull
- Concedes: no discrete legal catalyst inside the window; quant's arithmetic basically right (near-zero to negative base case); single-source problem stands; WOLF's distress raises the odds the suit is a leverage/licensing play rather than a fight to judgment.
- Pushes back: "no legal catalyst" ≠ "no tradeable edge" — the thesis is flow/sentiment (panic sellers finishing), not litigation-timeline-dependent. Notes quant's own -6 to -8% down-tail is itself uncatalyzed and arguably inconsistent with the "nothing happens in a month" logic. Flags unchecked volume data (light gap-down vs. heavy distribution) as the real discriminator.
- **Revised action:** folds partway — small conditional long NVTS, sized 0.25-0.4% of book (down from full size), entry compressed to ~7/17-18, exit moved earlier to ~7/24-28 (not 8/10-12, since the impact-window date itself carries no informational content). Conditional on (a) no PI motion on file, (b) no second source expanding the suit's scope. Folds to no trade if either check fails.

### Bear
- Bull's staggered timing doesn't resolve the catalyst problem, it relocates it — with no dated event, this is drift/pattern trading dressed in litigation language.
- Argues quant's 45/30/25 distribution is closer to arbitrary than derived: the tails are asymmetric (-6 to -8% vs +3-4%) but the probabilities aren't skewed to match, and the "optimistic" +0.50% branch is the same soft prior nudged, not new data. True edge reads as centered at zero-to-negative.
- Sharpens single-source risk (trading a headline about a headline; suit's requested relief unknown) and notes WOLF's distress cuts both ways — could mean the NVTS reaction was rational compression of expected settlement/royalty cost, not overreaction, and a settlement headline (positive or negative) could land any day, unscheduled.
- **Holds the line:** no trade. If forced, only the smallest possible contrarian NVTS long on clear panic-volume-overshoot evidence, ≤ quant's 0.25% ceiling, hard stop below the post-headline low.

### Quant
- Direction is settled across all three (long-NVTS-if-anything, never WOLF); the real disagreement is whether bull's timing structure moves the probability mass or is cosmetic.
- Entry filter (waiting for volume confirmation) is real but modest — raises conditional P(reversion) to ~50-52% in the subset where it triggers. Exit timing is mostly cosmetic: 2026-08-13 is a dossier artifact, not a scheduled legal date, so exiting early doesn't structurally truncate the down-tail (injunction/contagion news can hit any day in the window).
- Re-run with conditional entry: gross EV ≈ +0.21%, net ≈ -0.20% to -0.30% (still negative).
- Concedes bear's preliminary-injunction point numerically — prices an explicit discrete left-tail: P(PI-driven gap) ≈ 8% at -18% magnitude, separate from the diffuse -7% tail. With this added: P_up 0.48 (+3.5%), P_flat 0.26 (0%), P_mild_down 0.18 (-7%), P_PI_gap 0.08 (-18%) → gross EV ≈ -1.02%, net ≈ -1.45% to -1.55%.
- **Final:** PASS (no position), confidence 72%. Escalation trigger: PI/sales-injunction evidence surfacing → downgrade further (candidate short-into-strength); damages-only + panic-volume-exhaustion confirmed → fade-long becomes a ≤0.25%-of-book tactical position, still low-conviction.

---

## Round 3 — Synthesis (NO-TRADE, confidence 74)

**Hypothesis:** The 7% NVTS drop is a headline-driven reaction to a patent-suit filing whose earliest possible legal catalyst (ruling, injunction) falls well outside the impact window, leaving no dated, tradeable event by 2026-08-13. The modest mean-reversion edge is fully consumed by transaction costs and dominated by an uncatalyzed left-tail (preliminary-injunction / sales-injunction / settlement headline risk that can land any day). Direction: none.

**Plan:** NVTS, no-trade. WOLF excluded entirely (never long, given balance-sheet distress). Quant's fully-costed EV is negative in both the no-PI-aware case (net ≈ -0.20% to -0.30%) and the PI-aware case (net ≈ -1.45% to -1.55%). Bull's own conditional fade requires two unconfirmed facts (no PI motion on file; suit's scope not expanded by a second source) — since neither is verified against this single-source dossier, the default outcome is no trade. expected_profit_pct = 0.

**Dissent:** Is there a tradeable edge in the absence of a dated legal catalyst? BULL argued yes (flow/sentiment thesis, panic-seller exhaustion doesn't need a litigation-timeline catalyst; the down-tail is itself uncatalyzed). BEAR, joined substantively by QUANT, argued no (with no dated catalyst this is drift/pattern trading mislabeled as a lawsuit thesis; true edge is zero-to-negative; unscheduled settlement/PI headlines make the tail genuinely asymmetric against a long). Unresolved because the volume signature (light gap-down vs. heavy distribution) that would confirm or kill the panic-exhaustion premise was flagged by both Bull and Bear as unchecked — the key variable for a future post-mortem or revisit.

**Rationale:** Weighted the quant position most heavily since it was the only one to fully cost the disagreement into expected value, and both of its scenarios netted negative — decisive, since a positive gross EV that dies after costs is not a trade. Bear's contribution correctly identified the risk as asymmetric (unscheduled settlement/PI headlines, litigation base rates favoring defendants, single-source fragility), invalidating a symmetric mean-reversion framing. Bull made the strongest case for some edge but conceded the core points and voluntarily downsized to a conditional position gated on two unverified facts — so even the bull case resolves to no trade under current evidence. All three agreed WOLF is un-longable and that 2026-08-13 is a dossier artifact, not a real legal date, so exit-timing games cannot truncate the tail.
