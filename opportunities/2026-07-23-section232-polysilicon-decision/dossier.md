---
id: 2026-07-23-section232-polysilicon-decision
title: Section 232 polysilicon tariff proclamation expected early August
status: researched
created: '2026-07-23T17:49:00Z'
event:
  type: regulatory
  summary: White House proclamation on Section 232 polysilicon/solar supply chain
    tariffs, delayed from late June, now expected early August 2026; would hit imported
    polysilicon, wafers, cells and modules
  impact_window: '2026-08-07'
tickers:
- FSLR
- SEDG
- CSIQ
- ENPH
sources:
- title: 'pv magazine USA: U.S. polysilicon 232 decision delayed to August'
  url: https://pv-magazine-usa.com/2026/06/22/u-s-polysilicon-232-decision-delayed-to-august-while-45x-extension-draft-pushes-past-midterms-says-roth-capital-partners/
  accessed_at: '2026-07-23T17:49:00Z'
hypothesis:
  statement: "A Section 232 polysilicon/solar proclamation reported by a single outlet as expected in early August 2026 is not a specifiable trade in FSLR or any of SEDG, CSIQ, ENPH before 2026-08-07; the catalyst has no published clock-time anywhere (the impact_window date is a harness artifact, not a sourced event time), the direction has had roughly six weeks of public lead time since 2026-06-22 and is plausibly priced, a second delay is roughly a coin-flip after the first one, and the expected move is unsourced with no measured historical analogue, so every EV construction the panel tried lands negative even under the bull's own most favorable base-rate corrections."
  direction: none
  confidence: 88
plan:
  action: no-trade
  ticker: FSLR
  reasoning: "Two independent disqualifiers, either sufficient alone. (a) UNSPECIFIABLE: the catalyst has no date and no clock-time in any source (early August, quoting Roth Capital via one outlet); the harness requires fixed-timestamp entry/exit, so no order can be conditioned on the actual proclamation, and any executed version is undefined-duration solar-sector beta wearing an event-trade label. (b) NEGATIVE EV under every parameterization tested: P(clean tradeable surprise) about 0.18 (P(further delay) 0.45, P(substantially priced in given it lands) 0.60), FSLR long EV about -0.93 percent central, still -0.13 percent in a bull-favorable stress test; revised with magnitude down to a central 4.0 percent (no historical analogue exists), EV about -0.34 percent gross / -0.55 to -0.65 percent net, breakeven magnitude about 7.25 percent -- inside the unsourced upper half of the bull's own 5-15 percent guess; even granting the bull's full base-rate correction (P(delay) 0.30, P(clean surprise) 0.27), EV stays -0.17 percent, breakeven about 4.6 percent, the absolute floor of an unsourced range with zero margin. Structural rescues (FSLR/CSIQ pair, half-size fallback) were tested and abandoned by their own proposers -- CSIQ notional (~USD 18.4M/day) is too thin to be a hedge rather than theater. Data quality is not the binding constraint: all four tickers resolve on twelvedata with 96.7-100 percent RTH coverage; the trade fails on specifiability and EV, not on execution."
  revisit_conditions:
  - "A primary-source Federal Register or White House notice giving an actual date and time for the proclamation, replacing the manufactured 2026-08-07 window with a real clock-time the harness can condition on."
  - "At least two measured historical analogues of comparable Section 232 or solar-tariff proclamation-day moves in FSLR, establishing an empirical magnitude distribution in place of the unsourced 5-15 percent range."
  - "Evidence that FSLR is NOT already bid up over the lead-in since 2026-06-22 -- a measured FSLR return since that date showing the tariff expectation is not in the price."
  - "Independent second-source corroboration of scope (polysilicon, wafers, cells, and/or modules, and at what rate), since scope determines the sign for FSLR as easily as the magnitude."
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: "The live unresolved disagreement is estimator framing, not the verdict. Bull argued EV should be computed conditional on the clean-surprise branch and tail-weighted (buying a ~0.18-0.27 probability option on a discrete policy event); quant held the unconditional frame, since a fixed-timestamp harness position is held across all branches including the delay branch and cannot capture optionality convexity. This is a legitimate methodological fork that will recur on the next binary-policy-catalyst dossier, and is partly a harness limitation (no conditional-entry instrument) being scored as an analytical conclusion. Separately, this is a 3-0 convergence from a single pv magazine USA article quoting one broker, with zero measured historical analogues on either side -- shared-source convergence, not independent corroboration, echoing the false-consensus-under-a-data-blackout failure mode logged from the prior pool-corp debate. The panel never measured FSLR's actual return since 2026-06-22, so the load-bearing 'already priced in' claim remains an assumption, not an observation. The NO-TRADE verdict rests on the unspecifiability argument and the EV math standing independently, not on the unanimity."
  last_updated: '2026-07-26T01:48:00Z'
---

## Scouted 2026-07-23T17:49:00Z

## Researched 2026-07-26T01:48:00Z

Three-round panel debate (bull/bear/quant, synthesized by opus) concluded NO-TRADE,
confidence 88. Full transcript with citations: see `transcript.md`. The catalyst
(a Section 232 polysilicon/solar tariff proclamation "expected early August 2026")
has no confirmed date or clock-time anywhere in the single pv-magazine-USA source
(dated 2026-06-22); the dossier's 2026-08-07 impact_window is a manufactured
timestamp, not a sourced event time, making the trade unspecifiable in a
fixed-timestamp execution harness. Independently, every EV calculation the panel
ran on the cleanest expression (long FSLR, the domestic-manufacturing tariff
beneficiary among FSLR/SEDG/CSIQ/ENPH) came out negative, including under the
bull's own most favorable base-rate corrections, with the required breakeven move
sitting in the unsourced upper half of the bull's 5-15 percent magnitude guess. All
four tickers have solid twelvedata coverage (96.7-100 percent RTH); the trade fails
on thesis and timing specifiability, not on market-data plumbing.
