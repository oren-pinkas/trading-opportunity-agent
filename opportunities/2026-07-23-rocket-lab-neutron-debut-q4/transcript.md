# Research Debate Transcript — 2026-07-23-rocket-lab-neutron-debut-q4

Strategy: three-round-panel (debate-three-round-panel). Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
Run: 2026-07-26. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Institutional lesson injected as context: freshly-listed/IPO tickers are a distinct data-risk category — verify `toa price` coverage before scheduling any plan (source: 2026-07-12-spacex-starship-flight13, SPCX). RKLB is an established listing; coverage was pre-verified clean (`toa price RKLB 2026-07-24T15:00:00Z --provider twelvedata` -> USD 65.55).

## Round 1 — Independent research

### Bull (opening)
Neutron is Rocket Lab's ticket out of small-launch into medium-lift, Falcon-9-adjacent market — reusable, backlog-conversion catalyst (NSSL Phase 3, SDA). Jan 2026 test-stand accident pushed first flight to NET Q4 2026 (source: "Rocket Lab's Neutron slips to 2026", https://www.theregister.com/2025/11/11/rocket_labs_neutron_slips_2026/, accessed 2026-07-23). Slips are normal for novel reusable rockets (Falcon 9, New Glenn, Starship precedent) and don't kill the equity story. The catalyst isn't "did it slip" (priced in) — it's the actual Q4 2026 debut launch itself, a major re-rating event.

Proposed action: LONG, two-stage — anticipation leg entering ~2026-10-01 (equity), event leg via calls if a firm date is announced, exit on first launch or by 2026-12-31.

Price checks: `toa price RKLB 2026-07-24T15:00:00Z --provider twelvedata` = USD 65.55 (clean). `toa price RKLB 2026-09-15T13:30:00Z` and `2026-10-01T13:30:00Z` -> HTTP 400 (future dates not yet in twelvedata's range — expected, not a coverage gap).

### Bear (opening)
The delay IS the signal, not noise — Neutron has never flown; this is a repeat slip. By 2026-07-23 this is 8+ month stale news, likely fully priced. Flagged an internal date inconsistency: the dossier's accident is dated Jan 2026 but its only cited source is dated 2025-11-11 — a Nov-2025 article cannot report a Jan-2026 accident; sourcing may be muddled or the wrong source is attached.

Risks named: repeated-delay base rate for novel launch vehicles, cash burn/dilution from extended development, competitive erosion (SpaceX Starship / Blue Origin New Glenn banking flight heritage every month Neutron slips), backlog ATTRITION (not conversion) risk, and first-flight day being the point of MAXIMUM technical risk, not a de-risking event.

Proposed action: NO-TRADE; would lean toward a modest short/put hedge absent a fresher, dated, verifiable pre-window catalyst (e.g. a scheduled static fire/stage test before Oct 1).

### Quant (opening)
Base rate for novel orbital vehicles hitting an announced NET date: ~10-15%; P(slips 2+ quarters) 60%+; P(actual launch before the 2026-10-01 impact window) ~5%. Independently flagged the same date inconsistency as bear (uncorroborated by its own citation).

Pulled realized price path showing RKLB round-tripped ~45% twice already in 2026: 2026-01-15 USD 88.99 -> 2026-02-02 USD 75.49 -> 2026-04-15 USD 73.17 -> 2026-06-15 USD 106.55 -> 2026-07-17 USD 67.96 -> 2026-07-24 USD 65.55. Argues no unpriced information remains in the stale Nov-2025 article given repeated repricing.

Explicit EV (67-day horizon, initial ~30% sigma assumption): EV(long) ≈ -0.71% net of costs under a bearish direction tilt (45/55), only +0.37% even under the most bull-favorable tilt (55/45) — Sharpe ~0.01, indistinguishable from noise. Recommended NO TRADE, honest Kelly ≈ 0% once parameter uncertainty on direction is priced in. Would reconsider given: a source dated within 7 days confirming/revising the target, a specific dated launch attempt inside the window, or cheap implied vol enabling a long-convexity structure instead of picking a direction. Data coverage confirmed clean throughout (2026-01-15 through 2026-07-24, no provider errors) — the SPCX-derived data-risk lesson does not bite here.

## Round 2 — Rebuttal

### Bull (rebuttal)
Concedes the date-inconsistency is a real sourcing defect but argues the underlying NET-Q4-2026 guidance is likely independently corroborated elsewhere (earnings calls), so the defect doesn't kill the core thesis even though it undermines this specific citation. Argues the realized ~45% round-trips prove RKLB has a large reaction function to Neutron news, which is evidence a *successful debut* (categorically different from a slip announcement) could still re-rate the stock, not evidence the debut itself is priced. Concedes quant's flat-EV math is fair criticism of an undated anticipation leg.

Revision: drops the pure-equity anticipation leg; proposes no equity entry until a company-confirmed static-fire/dated launch-attempt lands inside the window; if confirmed, prefers a long-call/call-spread (convexity) over shares, sized small given bear's cash-burn/dilution and repeated-delay risks. Net: conditional long, convexity-first, gated on dated confirmation.

### Bear (rebuttal)
Notes quant's base-rate/EV work and the realized-vol evidence independently confirm bear's Round 1 thesis (three independent angles converging without cross-contamination). Grants the categorical point that a slip announcement and an actual debut are different events, but denies it's actionable off this dossier/timeline given quant's ~5% in-window launch probability and the absence of any firm date. Reaffirms the first-flight-day-max-risk point applies whenever the real event eventually happens.

Concedes quant's EV math kills bear's own short/hedge idea too — a short has the same near-zero raw edge as a long, so holding onto "small hedge" was motivated reasoning. Drops the hedge.

Updated recommendation: NO TRADE, full stop — no long, no short, no hedge. Revisit only on a genuinely fresh (<7-day), dated, specific pre-window catalyst.

### Quant (rebuttal)
Notes the date-inconsistency flag is an audit-checkable property of the artifact (not weak blackout-agreement) — the Q4 2026 target is an unverified input, and every EV calculation downstream inherits that. Revises own sigma upward: realized vol implies ~65-70% annualized (not the initial 30% assumption), giving a 67-day sigma of ~36% — raises the raw magnitude of any edge but Sharpe stays ~0.08, still statistically indistinguishable from zero on n=1.

Shows a naive long-convexity (ATM straddle) into the launch is ALSO -EV at ~70% IV: breakeven ~16% move vs. ~12-14% probability-weighted expected move on historical first-flight-day reactions. Proposes the only defensible structure: once a firm dated attempt exists, buy vol weeks out and sell into the pre-launch IV ramp — harvesting event-date IV concentration, not betting on outcome, no directional view required.

Shows bear's short hedge is arithmetically the mirror of the long (same near-zero edge) and strictly worse after borrow/financing drag (~0.2-0.6%), cutting bear's best case to ~0-2bps.

Final recommendation: NO-TRADE-NOW, CONDITIONALLY REVISIT. Size stays exactly zero until all of: (1) a launch date confirmed by a source <7 days fresh, ideally primary (FAA licence / RKLB IR); (2) that date falls in a tradeable window with ≥3 weeks runway; (3) an option chain exists on an expiry straddling the date with ATM IV below ~55%; (4) the pre-event IV ramp is observable and the entry-to-ramp spread clears frictions. Concrete trigger: re-run this analysis early-to-mid September 2026, or immediately on a dated launch-attempt announcement, whichever comes first. Final numeric confidence a directional trade taken today is +EV: 12/100.

## Round 3 — Synthesis

**Hypothesis:** The "Neutron debut slips to NET Q4 2026" item carries no tradeable edge as of 2026-07-26. The dossier's core claim is internally unsupported — its single cited source (theregister.com, 2025-11-11) predates the "Jan 2026 test accident" it is cited for, so the accident and the NET-Q4-2026 target are unverified inputs. Even granting the target, the news is 8+ months stale and has been repeatedly repriced (RKLB round-tripped ~45% twice in 2026; last verified quote USD 65.55 at 2026-07-24T15:00Z). Base rates give ~10-15% odds of hitting an announced NET date and ~5% odds any launch falls inside the 2026-10-01 impact window, with no firm date in existence. Both directional legs price out near zero (EV(long) approx -0.71% to +0.37% net of costs; the mirror short is the same edge minus borrow/financing drag). A naive long-convexity substitute is also -EV at prevailing implied vol. All three personas independently converged on no-trade; bull withdrew its equity anticipation leg and bear withdrew its short hedge.

- direction: no-trade
- confidence: 88 (in the no-trade conclusion; the panel's own stated confidence that a directional trade taken today is +EV was 12/100)

**Plan:** ticker RKLB, action no-trade, no entry/exit, expected_profit_pct 0.0. Conditional re-trigger (all four required before any position is considered): (1) a specific dated Neutron launch/static-fire milestone confirmed by a source less than 7 days fresh, ideally primary (RKLB IR / FAA licence / earnings call) — this also cures the dossier's date-attribution defect; (2) that date falls in a tradeable window with at least 3 weeks runway; (3) a listed option chain exists on an expiry straddling the date with ATM IV below approximately 55%; (4) a pre-event IV ramp is observable and the entry-to-ramp vega spread clears frictions. If triggered, the only structure judged defensible is buying vol weeks ahead of a confirmed date and selling into the pre-launch IV ramp (event-date IV concentration, not a bet on launch outcome) — explicitly not a hold-through-launch straddle and explicitly not long equity into the event itself. Concrete review date: early-to-mid September 2026, or immediately on a dated launch-attempt announcement, whichever comes first.

**Dissent (strongest unresolved disagreement):** Whether a successful Neutron debut is a genuinely unpriced, categorically different event, or already in the tape. Bull's surviving argument was never refuted, only ruled non-actionable: a slip announcement and a first successful orbital flight are different events, and the ~45% round-trips prove RKLB has real event sensitivity to Neutron news — not proof the debut itself is priced. Bear and quant answered on timing and dossier quality (no firm date, ~5% in-window probability, stale unverified source), not on magnitude. The panel's convergence rests on "not yet / not from this dossier," not on "the debut is priced." If Neutron flies successfully and RKLB re-rates 30%+ on the day, this synthesis will look like a process-correct miss — the post-mortem question is whether the freshness/date gates were calibrated or a way to avoid a hard call.

Secondary notes: both directional personas abandoned their own book (bull dropped the equity leg, bear dropped the hedge and named its own motivated reasoning) — healthy, but it leaves the final answer driven almost entirely by the quant's EV/vol arithmetic, a single unreplicated model whose own sigma revision (30% -> ~65-70% annualized) shows how sensitive the conclusion is to one input. Unlike the pool-corp precedent (agreement partly on facts later retracted), this convergence rests on an audit-checkable, confirmed defect: the dossier's own frontmatter cites a 2025-11-11 URL for a Jan-2026 accident. Price data was clean throughout — future-dated `toa price` HTTP 400s were expected range errors, not a coverage gap. Process note for the scout: an event whose accident date postdates its only source should be caught before it reaches debate.
