---
id: 2026-07-12-deere-ftc-right-to-repair-settlement
title: FTC secures right-to-repair antitrust settlement with Deere
status: researched
created: '2026-07-12T08:53:04Z'
event:
  type: regulatory
  summary: FTC and five states settled an antitrust suit against Deere & Company,
    forcing it to open tractor/farm-equipment repair access to farmers and independent
    shops.
  impact_window: '2026-09-01'
tickers:
- DE
sources:
- title: Looking Ahead on US Antitrust Enforcement and Tech | TechPolicy.Press
  url: https://www.techpolicy.press/looking-ahead-on-us-antitrust-enforcement-and-tech-will-2026-deliver-more-of-the-same/
  accessed_at: '2026-07-12T08:53:04Z'
hypothesis:
  statement: The July 8, 2026 FTC + 5-state right-to-repair settlement is a
    fully-telegraphed, twice-precedented (Jan 2023 Farm Bureau MOU; April 2026
    $99M farmer class action) formalization that was priced at ~zero. The
    observed ~7% DE decline around July 7-8 is macro/tariff-confounded (CAT and
    CMI fell in the same window on CAT's own tariff-cost guidance), leaving an
    idiosyncratic settlement residual of only ~-0.5% to -2% that had already
    printed days before this dossier was even opened. There is no unpriced,
    tradeable edge on the stated 2026-09-01 impact window.
  direction: no_trade
  confidence: 80
plan:
  ticker: DE
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: Bull surfaced a separate, unrelated thesis — long DE into the Aug 16
    2026 Q3 earnings print on raised FY2026 guidance ($4.5-5.0B) — which
    quant and bear both ruled out of scope for this dossier ("must not be
    laundered through this event"; "smuggling in a generic industrial-earnings
    thesis"). Whether that earnings idea deserves independent research standing
    of its own was never resolved, only declared off-topic. Secondary and
    smaller residual — quant treats the macro-decomposed price-move residual as
    confirming a small negative settlement effect, while bear treats the whole
    July 7-8 move as pure macro noise with no extractable settlement signal —
    neither view changes the no-trade verdict.
  last_updated: '2026-07-12T19:17:00Z'
---

## Scouted 2026-07-12T08:53:04Z

## Researched 2026-07-12T19:17:00Z — NO-TRADE

Three-round panel debate (bull/bear sonnet, quant/synthesizer opus). All three
personas converged on no-trade, with the bull conceding fully in Round 2:

- **Bear (decisive, live-verified):** Fetched the settlement directly — announced
  July 8, 2026 (FTC + IL/AZ/MI/MN/WI), suit filed Jan 15, 2025, $1M to state legal
  costs, no admission of wrongdoing, 10-year repair-tool-parity mandate (Deere
  retains the right to charge fees). This is Deere's *second* right-to-repair
  settlement in 2026 (also a $99M farmer class action in April) and is largely an
  incremental formalization of the Jan 2023 American Farm Bureau MOU — not a new
  business-model shock. DE fell ~6.6-7.7% around July 7-8, but CAT and CMI fell in
  the same window, with CAT's move independently explained by CAT's own
  $2.2-2.4B FY26 tariff/import-compliance guidance — the DE drop is very likely
  macro/tariff-confounded, not idiosyncratic to the settlement. Confidence in
  no-edge: 85/100.
- **Quant:** No live web access in Round 1 (base-rate reasoning only, explicit
  confidence haircut); base rate says behavioral consent decrees on telegraphed
  suits are modally non-events or mild relief rallies (Microsoft 2001-02, Apple
  2021-22, Deere's own 2023 MOU). After bear's data, decomposed the confounded
  ~7% move: backing out CAT/CMI-implied macro beta leaves an idiosyncratic
  residual of only ~-0.5% to -2%, confirming (not refuting) Round 1's bound but
  worsening signal-to-noise — "the move already happened July 7-8; trading now is
  a macro bet wearing a settlement costume." Final EV: expected excess move
  ≈ +0.08%, sigma ≈ 0.94%, net EV ≈ -0.12% after ~15-25bps round-trip costs,
  EV/sigma ≈ 0.08 (negligible), implied Kelly ≈ 0. Recommendation: PASS, zero
  size. Confidence: directional 78/100.
- **Bull:** Opened long DE (3-8% upside over ~5 weeks) on a "de-risking, not
  re-rating" framing, targeting a hold through the Aug 16 Q3 earnings print.
  Conceded in Round 2 that (a) the CAT/CMI confound undercuts the
  "settlement-driven dip" framing, (b) quant's EV takedown of trading the
  settlement itself is correct, and (c) the Aug 16 earnings/guidance thesis is a
  *separate* trade not actually backed by this dossier's event. Lowered
  confidence from 55 to 42/100.

**Data-quality flags (process issues, independent of the trade verdict):**
1. The dossier's only cited source (TechPolicy.Press, "Looking Ahead on US
   Antitrust Enforcement and Tech") is exclusively about Google/Meta/Apple/Amazon
   antitrust cases and **never mentions Deere, tractors, or right-to-repair
   anywhere** — a citation/provenance error in the scouting pipeline. The
   underlying event (the actual FTC/Deere settlement) is real and was
   independently re-verified by bull and bear via WebSearch/WebFetch, but the
   dossier's own sourcing chain does not support it.
2. The `toa price DE` feed returned an incoherent series (e.g. $270.67 on 7/11
   vs $106.08 on 7/12, vs $399.72 quoted for 7/8 by web search — real DE trades
   materially higher than any of these) and was assigned zero weight by all
   three personas.
3. The 2026-09-01 impact_window has no identified supporting event (no
   compliance deadline, no court date, no earnings call — Deere's Q3 FY26
   earnings is Aug 16, not Sept 1) and appears arbitrary.

**What would need to change to revisit:** (1) sourcing/citation fixed so the
dossier actually documents the Deere-specific event; (2) a clean beta-decomposition
showing DE's July 7-8 residual materially exceeds the CAT/CMI-implied sector move
(would indicate genuine idiosyncratic mispricing); (3) a sourced hard event
actually tied to the Sept 1 window; (4) a quantified guidance/margin channel
showing the repair mandate moves EPS by more than a rounding error. The
Aug 16 Q3 FY26 earnings idea bull raised should be evaluated as its own,
separately-scoped opportunity, not folded into this one.

Full transcript: see `transcript.md`.
