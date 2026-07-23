---
id: 2026-07-22-avanos-medical-merger-close
title: Avanos Medical take-private merger targeted to close July 27
status: researched
created: '2026-07-22T13:34:47Z'
event:
  type: regulatory
  summary: Avanos Medical stockholders approved AIP take-private deal at July 22 special
    meeting; close expected no later than July 27
  impact_window: '2026-07-27'
tickers:
- AVNS
sources:
- title: Avanos merger clears regulators, with stockholder vote set for July 22
  url: https://www.stocktitan.net/news/AVNS/avanos-medical-inc-and-american-industrial-partners-receive-required-7pjk02dt2cvy.html
  accessed_at: '2026-07-22T13:34:47Z'
hypothesis:
  statement: "AVNS is an approved, regulator-cleared cash take-private (AIP) pinned dead-flat at approximately USD 24.98 across three sessions into a July 27 close. The residual spread is thinner than round-trip costs, so no long merger-arb edge exists; the break tail makes the risk-adjusted setup strictly negative. No credible evidence supports a competing bid or an unpriced blocker."
  direction: no_trade
  confidence: 88
plan:
  ticker: AVNS
  action: no_action
  entry: null
  exit: null
  expected_profit_pct: 0.0
  retrigger_condition: "Reopen only if a sourced cash consideration price implies a live spread clearing round-trip cost (about 0.10 pct) plus a risk-adjusted break hurdle (gross spread materially above about 0.9 pct with low break probability), or if the tape breaks off the USD 24.98 pin."
research:
  last_updated: '2026-07-23T05:30:04Z'
  dissent: "No genuine persona disagreement; all three personas converged on pass. The only unresolved item is a research gap (unverified cash deal price), and sensitivity analysis showed the verdict is robust to that gap resolving either way."
  research_gap: "Dossier omitted the deal cash consideration price; panel inferred approximately USD 25.00 from the flat price pin rather than sourcing it directly."
---

## Scouted 2026-07-22T13:34:47Z

## Researched 2026-07-23T05:30:04Z

Three-round panel (bull/bear/quant, debate-three-round-panel strategy) converged unanimously on no_trade. Bull's initial conditional long (based on an unverified recalled deal price of USD 22.00/share) was refuted when the real price tape (toa price, twelvedata) showed AVNS pinned dead-flat near USD 24.98 across three sessions -- consistent with an already-fully-arbed deal, not one still trading below terms. Quant's EV calculation, using an inferred deal price near USD 25.00, found the trade EV-negative (~-0.83% at P(break)=0.03; still negative even at P(break)=0, since the raw spread is smaller than round-trip transaction costs alone) -- a frictions problem, not a probability problem. Bear independently flagged the asymmetric tail risk of a deal break (potential 20-30% reversion toward standalone value) against a residual spread of a few cents. Full transcript: `transcript.md`.
