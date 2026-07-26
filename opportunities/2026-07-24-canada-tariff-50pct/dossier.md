---
id: 2026-07-24-canada-tariff-50pct
title: 50% US tariff on Canadian imports takes effect Aug 19
status: researched
created: '2026-07-24T00:13:06Z'
event:
  type: geopolitical
  summary: Section 338 tariff action imposes 50% duties on certain Canadian imports
    starting Aug 19, 2026, pressuring Canada-exposed equities
  impact_window: '2026-08-19'
tickers:
- EWC
sources:
- title: 'Blakes: U.S.-Canada Tariffs Timeline'
  url: https://www.blakes.com/insights/us-canada-tariffs-timeline-of-key-dates-and-documents/
  accessed_at: '2026-07-24T00:13:06Z'
hypothesis:
  statement: 'Section 338''s 50% duties on roughly USD 20B of Canadian goods effective
    2026-08-19 are not tradeable through EWC. Covered categories (dairy, alcohol,
    motor vehicles, cement, furniture, textiles) map to an estimated 1-2% of fund
    revenue exposure, while EWC''s top-5 weights (RBC 8.24%, TD 5.93%, Shopify 4.99%,
    Enbridge 3.91%, BMO 3.53% = 26.6%) contain no tariffed name and energy/potash/fish/critical
    minerals/Section-232 goods are explicitly excluded. The market has already expressed
    this: the verified move from the Jul 17 pre-proclamation close (59.305) to the
    Jul 24 anchor (59.01) is -0.50%, only 0.34 sigma against 0.654% daily realized
    vol -- statistically indistinguishable from noise. After correcting for roughly
    6%/yr generic equity drift (+0.43% over 18 trading days), both directions collapse
    to flat: short EV -0.23% (below its own breakeven), long EV +0.04% (equity risk
    premium, not event edge). Both sit inside +/-25bp against a ~2.9% terminal sigma,
    an edge ratio under 0.02.'
  direction: no-trade
  confidence: 88
plan:
  ticker: EWC
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0
  rationale: No positive-EV trade in either direction. Short EV -0.23% net of ~11bps
    costs after the drift correction (below its own breakeven); long EV +0.04% is
    equity risk premium unrelated to the Section 338 catalyst. Edge ratio under 0.02
    against ~2.9% terminal sigma to the Aug 19 impact window.
  revisit_triggers:
  - EWC Aug-expiry options IV/skew becomes available -- single most decisive missing
    input, never obtained in either round
  - CIT (Court of International Trade) docket shows a filed challenge to the Section
    338 proclamations
  - 'Official confirmation resolving IMPOSED vs PROPOSED legal status (sources conflict:
    Baker McKenzie says proposed, GHY/Crane Worldwide/Mohawk Global say imposed)'
  - Canadian retaliation list or announcement (unexamined by any persona)
  - A single-session EWC move exceeding ~1.3% (2 sigma) on tariff-specific news --
    max observed in sample is 0.96%
  known_data_hazard: Monday 2026-08-03 is the Canadian Civic Holiday (TSX closed,
    NYSE open) -- EWC would trade against a stale underlying that session, inside
    the Aug 19 holding window.
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
  dissent: 'P(suspension/carve-back/injunction before Aug 19): Quant estimated 0.30
    (deriving a 13pp cushion against his stated short breakeven of P(slip) < 43%);
    Bull argued for 0.40-0.45 (citing the same proclamation already carving out 4
    categories by name as revealed willingness to narrow scope), which would erase
    Quant''s cushion to ~0-3pp; Bear argued the opposite direction, weighting USTR
    Greer''s public no-exemption signal as the central threat to any relief-rally
    leg. Bear separately attacked the estimate''s epistemics as false precision drawn
    from a single noisy 4-day (0.34-sigma) price path, which Quant never rebutted.
    Unresolved because the three inputs that could arbitrate it -- options-implied
    probability, the CIT docket, and imposed-vs-proposed status -- were flagged missing
    in Round 1 and still missing at the end of Round 2. The dispute does not change
    the call (both EVs are flat regardless of whether P(slip) is 0.30 or 0.45, since
    the payoff spread across buckets is only ~5.3pp wide), but it is the live methodological
    gap: two rounds were spent refining a probability no available data could discipline,
    while the actually decisive error -- an omitted ~0.43% equity-drift term in Quant''s
    own EV baseline -- went unnoticed until Quant caught it himself in Round 2. Secondary
    unresolved thread: CAD/USDCAD was flagged by all three personas as material (EWC
    is unhedged) and never quantified by any of them.'
  last_updated: '2026-07-26T09:06:55Z'
---

## Scouted 2026-07-24T00:13:06Z

## Researched 2026-07-26T09:06:55Z — NO-TRADE

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) converged on NO TRADE for EWC against the Aug 19, 2026 Section 338 tariff deadline.

Key verified facts (via `toa price EWC --provider twelvedata`): EWC printed 59.305 on 2026-07-17 (last pre-proclamation close), 58.81 on 2026-07-20 (proclamation day), and 59.01 on 2026-07-24 (anchor) -- a cumulative post-proclamation move of -0.50%, or 0.34 sigma against a realized daily sigma of 0.654% (~10.4% annualized). No single session in the sampled window exceeded a 0.96% move. The bull's Round 1 claim of an unverified "~57.06 in late June" baseline was shown in Round 2 to be a mis-cited trough (actual closest print: 57.145 on 2026-06-24, the three-month low), and decomposing the bull's cited rally showed +3.78% occurred *before* the July 20 proclamation versus -0.50% *after* it -- his evidence for a bullish post-announcement drift did not survive verification.

Independently confirmed (GHY, Crane Worldwide, Troutman, Baker McKenzie trade advisories) that Section 338's exclusion list covers energy, potash, fish/seafood, critical minerals, and anything already under Section 232 -- meaning EWC's two largest cyclical blocks (energy, financials) are structurally insulated from the tariff's direct mechanism. Direct revenue-at-risk inside EWC from covered categories (dairy, alcohol, autos, cement, furniture, textiles) was estimated at only ~1-2% of the fund.

The decisive step came in Round 2 when Quant corrected his own Round 1 EV calculation by adding a previously-omitted ~6%/yr generic equity drift (+0.43% over the 18 remaining trading days to Aug 19): the short's net EV fell from +0.20% to -0.23% (moving it below its own breakeven), while the long's net EV rose only from -0.39% to +0.04% (attributable to equity risk premium, not tariff-event edge). Both results sit inside +/-25bp against a ~2.9% terminal sigma -- an edge ratio under 0.02.

The dossier's own cited source (Blakes tariff-timeline page) was found by Quant not to contain the Aug 19/50%/exclusion-list content when fetched directly; all substantive facts in this debate were sourced independently from other trade-law advisories. The proclamations were signed 2026-07-20 (not the 2026-07-23/24 date implied by the dossier's `accessed_at`).

No trade taken. See revisit_triggers in the plan frontmatter for what would reopen this call.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
