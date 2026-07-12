# Debate transcript — 2026-07-12-airbus-spain-strike-deliveries

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Institutional lessons queried for event type `geopolitical` +
ticker `EADSY`: none found. Debate run: 2026-07-12, current time at kickoff
2026-07-12T18:30:05Z.

Reference prices (`toa price EADSY <ts>`) — flagged by all three personas as an
incoherent stub/testing artifact, not used for sizing:
- 2026-07-08T14:00Z: $175.83
- 2026-07-09T14:00Z: $494.84
- 2026-07-12T18:00Z: $79.87

Source: Bloomberg, "Airbus Employees in Spain Go on Strike Over Working
Conditions", https://www.bloomberg.com/news/articles/2026-07-09/airbus-employees-in-spain-go-on-strike-over-working-conditions,
accessed 2026-07-12T18:06:04Z.

---

## Round 1 — Independent research

### Bull (Catalyst-hunter)

Read of the event: ~3,000-worker strike at Airbus's Getafe plant, confirmed by
Bloomberg 2026-07-09, running through end of July, chokes off the
inspection/engineering-check step that gates delivery completion. Airbus's
delivery cadence is back-loaded within the month/half, so a strike eating the
back half of July hits exactly the window the company needs maximum throughput.
Airbus's H1 print typically lands right around 2026-07-31 — the same date as
the dossier's impact window — giving this a hard, dated resolution point.

Proposed action: short EADSY (or downside puts if available). Entry now/within
1-2 sessions (2026-07-12 to 2026-07-14); exit by 2026-07-31 timed to the H1
print or an interim delivery-miss headline.

Confidence: MODERATE. What breaks the thesis: strike settles early; Airbus
reroutes inspection/engineering-check work to Toulouse/Hamburg; deliveries are
merely deferred a few days and shrugged off as noise; broader sector tailwind
swamps the story. Explicitly flagged the price feed ($175.83 → $494.84 → $79.87
over 4 days) as an incoherent stub not usable for sizing/stops, and did not use
it for the recommendation above.

### Bear (Skeptic)

Doesn't doubt the strike is real; doubts it's a trade. Six points:

1. **Stale news.** Bloomberg dated 2026-07-09; debate is 2026-07-12, 18:30 UTC —
   three trading days later. Whatever repricing was coming from the headline has
   likely already happened.
2. **Scale/scope mismatch.** Getafe is one site among Toulouse, Hamburg, Mobile
   (AL), Tianjin, in a ~145k-employee company. The dossier asserts but never
   quantifies that Getafe inspections gate the bulk of monthly commercial
   deliveries (dominated by A320-family output from Toulouse/Hamburg).
3. **Backlog cushion.** Airbus's backlog is in the thousands of aircraft; a
   one-month slip from one plant is a timing issue (revenue recognition shifts),
   not a demand or margin issue, absent explicit guidance language (not
   present here) confirming quarter/year risk.
4. **Resolution risk cuts against a stale short.** European strikes commonly
   settle before their announced end date; that reversal risk isn't
   discoverable in this feed.
5. **Price feed is unusable.** +181% then -84% over 4 trading days is not a
   coherent path for a large-cap aerospace ADR absent a split/rights
   issue/data error, none of which are mentioned. Flags this as a likely
   stub/test artifact; cannot mark entry, stop, or target against it.
6. **ADR-specific liquidity risk.** EADSY is a Level-1 OTC ADR of Paris-listed
   AIR.PA — thinner, wider spreads, can dislocate from the ordinary shares for
   reasons unrelated to fundamentals.

Confidence: LOW confidence in any tradeable edge, bordering on a pass. Base
case: a plant-level labor dispute the market largely priced on 2026-07-09,
wrapped in a broken price feed that makes the "opportunity" impossible to
evaluate honestly.

### Quant (Pragmatist)

Base rates (labeled assumptions, not fabricated precedents): single-plant,
partial-workforce strikes rarely move a diversified mega-cap OEM; this is a
delivery-*timing* bottleneck, not a production halt — a materially smaller
category; delivery slips are revenue-recognition timing given deep backlog, not
lost value; the news is already public and mega-cap labor headlines are
typically priced within days.

Probabilities for the window to 2026-07-31: 20% escalation/guidance-warning,
55% noise, 25% favorable resolution.

EV calc (hypothetical short, generic magnitudes since the price feed is
unusable for calibration): escalation +3%, noise 0%, favorable resolution -2%.
Gross EV = 0.20(+3%) + 0.55(0%) + 0.25(-2%) = +0.10%. Round-trip
transaction/slippage cost ~0.30-0.50% (ADR frictions) + borrow ~0.03-0.05%.
Net EV ≈ -0.30%. **Edge does not survive costs.**

Confidence: directional "stand aside" conclusion MODERATE-HIGH (~70-75%),
robust and independent of the price feed. Point-estimate/magnitude confidence:
LOW — the price feed is a stub/testing artifact, generic priors are not
measured, no reliable price feed means any magnitude/sizing claim in this
debate should be treated as uncalibrated.

---

## Round 2 — Rebuttal

### Bull rebuttal

Concedes the bear's staleness point is the strongest hit — no volume/price data
proves the market hasn't already moved. Concedes the quant's framing
(delivery-*timing* vs. production-halt) was conflated in Round 1; the backlog
converts a slip into H2/Q3 revenue recognition rather than destroyed value, so
the real bet is narrower: "the 2026-07-31 print surprises negatively vs.
consensus," not "Airbus is hurt."

Reframes: the edge, if any, is in trading the delivery-count/guidance
disclosure at the 2026-07-31 print itself — a fresh, not-yet-occurred event —
not in trading the stale 2026-07-09 headline. But concedes this doesn't rescue
the trade: Getafe's bottleneck role is asserted, not sourced (no data on what
fraction of deliveries route through it); the quant's EV math "cannot be argued
around" — a 0.10% gross edge cannot survive 0.30-0.50% costs, "the most
damaging point in the whole debate... regardless of who's right about
mechanism"; and the ADR mechanics (thin Level-1 OTC + broken price feed) make
the instrument currently untradeable regardless of direction.

Updated position: downgraded from "moderate confidence short" to "low
confidence / speculative watch, no size until the 2026-07-31 print window,"
contingent on the price feed being fixed and confirmation that Getafe's
inspection step is non-reroutable.

### Bear rebuttal

Raises confidence in "pass" to ~80-85%. Argues the quant's EV math and the
staleness argument are *independent* failure modes, not redundant — the bull
would need both the market to be wrong on the odds AND the execution costs to
be wrong. That's a taller bar than either objection alone.

Partially concedes the bull's dated-catalyst point: the 2026-07-09 headline is
stale, but the 2026-07-31 print/resolution is a genuinely fresh, not-yet-priced
information event — calendar-anchored disclosures do move stocks even when the
underlying issue has been public for weeks. Real mechanism, credited as the
most credible part of the bull case.

But argues it still doesn't rescue the trade: (1) sign ambiguity — the quant's
own probability split cuts both ways at the print, and early settlement or
inspection-rerouting could make the print land favorably, a "fresh event" that
resolves against a short; (2) the surprise bar is high — Airbus's deep backlog
and history of absorbing single-site disruptions without guidance cuts means
analysts likely already build in cushion for exactly this kind of noise, and
Getafe's hard-gate status remains unproven; (3) even a real catalyst is
untradeable on this specific broken instrument — the coherent expression would
be an event-vol structure on the liquid primary listing (AIR.PA) dated to the
print, not a linear "short EADSY now through 7/31," which nobody actually
proposed in a tradeable form.

### Quant rebuttal

On the bull's dated-catalyst point: concentrating resolution in time raises
*variance*, not the *mean* — irrelevant to a linear EV-negative short; would
only matter for a convex options structure (long puts / put spread), which
doesn't exist for EADSY (illiquid/nonexistent listed options). Probability
weights unchanged (20/55/25); a known, scheduled catalyst date, if anything,
shrinks the surprise component via pre-positioning.

On the bear's ADR-liquidity point: agrees, and revises round-trip friction
upward from 0.30-0.50% to ~0.80-1.50% (midpoint ~1.1%) given Level-1 OTC
thinness, FX overlay, and hard-to-borrow risk on a small foreign-name ADR.

Revised EV: gross +0.10% (unchanged), net ≈ -1.0% (range -0.7% to -1.4%) — worse
than Round 1. Break-even stress test: escalation probability would need to
roughly triple to ~55% at the same magnitudes to clear the cost hurdle — not
supported by base rates for a single-plant inspection bottleneck at a
~150k-employee OEM with a multi-year backlog. Kelly-fraction on negative EV is
negative → size zero.

Confidence: directional "stand aside" raised to ~80% (from 70-75%); point
estimates remain LOW confidence (price feed unusable, borrow/spread are
estimated not observed) — but that uncertainty errs toward strengthening,
not weakening, no-trade.

---

## Round 3 — Synthesis (final)

By Round 2 all three personas converged, for independent reasons — the
strongest form of agreement. No persona finished advocating for the trade.

**Hypothesis:** The Getafe strike is a delivery-timing bottleneck at one site
of a diversified, deep-backlog OEM, not a production halt — most likely
absorbed as revenue deferral or resolved before month-end. Any residual edge
tied to the ~2026-07-31 H1 print is (a) sign-ambiguous, (b) at best a
variance/convexity play with no liquid options vehicle on EADSY, and (c)
EV-negative once ADR execution costs are applied to the proposed linear short.

- Direction: **no_trade**
- Confidence: **82/100** — high confidence in *standing aside*; robust to the
  broken price feed and independent of any point-estimate of magnitude.

**Plan:** ticker EADSY, action **no-trade**. Rationale: gross edge (~+0.10%) is
an order of magnitude smaller than round-trip friction (~0.8-1.5%) on a thin
Level-1 OTC ADR with FX overlay and borrow risk; the price feed is incoherent
so no entry/stop/target can be set; the delivery-slip thesis is timing, not
value, and Getafe's gate role is unproven.

What would need to change to revisit: (1) price feed repaired and coherent;
(2) concrete evidence Getafe performs a non-reroutable inspection gate for a
material share of H1 deliveries; (3) signs of escalation past end-July rather
than early settlement; (4) a liquid convex vehicle (event-vol options on the
primary AIR.PA listing) to express the dated-catalyst idea — a linear EADSY
short stays off the table even if (1)-(3) improve, given the cost structure.

**Dissent (for post-mortem):** whether the 2026-07-31 H1 print is a real,
exploitable dated catalyst or merely noise. Bull and bear grant the print
concentrates a genuine information event in time; quant counters that
time-concentration raises variance, not mean, and is therefore irrelevant to a
linear EV-negative position, mattering only for a convex structure that
doesn't exist for EADSY. This was dismissed on tradeability/instrument grounds
(no liquid EADSY options, broken price feed), not settled on merit — nobody
established whether a properly-structured AIR.PA event-vol trade around
2026-07-31 would carry positive EV. Post-mortem should check the actual print
outcome (delivery count / guidance and realized move) against this: if the
print produced a large move, the miss was one of vehicle selection, not a
wrong read on the catalyst's existence.
