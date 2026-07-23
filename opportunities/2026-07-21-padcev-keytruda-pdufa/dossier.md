---
id: 2026-07-21-padcev-keytruda-pdufa
title: Padcev plus Keytruda bladder cancer PDUFA decision
status: researched
created: '2026-07-21T15:25:19Z'
event:
  type: regulatory
  summary: FDA PDUFA action date August 17 2026 for enfortumab vedotin plus pembrolizumab
    in perioperative muscle invasive bladder cancer
  impact_window: '2026-08-17'
tickers:
- PFE
- MRK
sources:
- title: 'FDA drug approval decisions: July and August 2026 - Life Science Daily'
  url: https://lifesciencedaily.news/fda-drug-approval-decisions-to-watch-july-and-august-2026/
  accessed_at: '2026-07-21T15:25:19Z'
hypothesis:
  statement: 'All three panelists converged on NO TRADE for the equity directional
    bet. The PDUFA is a telegraphed formality on an already-approved Padcev+Keytruda
    combo with year-old EV-302 Phase 3 data, so P(favorable surprise) collapses to
    ~0.135 -- gated not by approval odds (~0.90) but by P(not already priced in)
    ~0.15 -- while the expected favorable move (~0.6% PFE / 0.3% MRK) sits well
    below daily ATR (~1.7%/1.6%), yielding negative EV after transaction costs and
    no-surprise noise-fade; signal/noise ~0.05, below the 0.15 institutional
    durability floor. The one genuinely asymmetric idea the panel surfaced was a
    CRL/delay tail (P~0.10, plausible -3% to -6% gap), but it was explicitly
    declined as a paper trade -- it is a structured cheap-OTM-put expression rather
    than a clean delta-short equity trade, hard to time, and likely already bid
    into event options vol.'
  direction: none
  confidence: 17
plan:
  ticker: PFE
  action: no-trade
  entry:
    time: '2026-08-14T19:50:00Z'
    target_price: null
  exit:
    time: '2026-08-18T13:45:00Z'
    target_price: null
  expected_profit_pct: 0
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
  dissent: 'The sharpest unresolved thread is the CRL/delay tail. Bear and Quant
    agreed it is the only structurally asymmetric setup in the debate -- roughly
    +0.45% gross EV to a downside holder on a ~10% chance of a -3% to -6% gap --
    yet both declined to size or execute it. The disagreement is left implicit and
    unactioned: it is a real edge only through a cheap OTM put, not the equity leg
    this simulation trades, and the panel could not establish that the tail is
    currently mispriced, so a genuinely interesting idea was identified but never
    resolved into a trade.'
  last_updated: '2026-07-23T01:07:42Z'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-23T01:07:42Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Bull opened
long PFE small (35 confidence) on the "cleaner Seagen/Padcev exposure" read, but
conceded to NO TRADE (confidence 12) once the quant's EV math held under
stress-testing -- the combo's Phase 3 data (EV-302) is over a year old and already
approved in the metastatic setting, so this perioperative-MIBC label expansion has
near-zero informational surprise despite a high (~90%) approval base rate. Bear
(78->76) and quant (78->80) both held NO TRADE throughout, converging on negative
EV after transaction costs once P(not-already-priced-in)~0.15 and expected
magnitude (~0.6% PFE / 0.3% MRK) are weighed against ATR (~1.7%/1.6%). The panel
did surface one asymmetric idea -- a CRL/delay tail risk, ~10% probability of a
-3% to -6% gap-down -- but explicitly declined to size it as a paper trade (it
wants a cheap OTM put, not the equity leg this simulation trades, and is hard to
time). Verdict: NO-TRADE (not scheduled, not simulated). Full debate with citations
in `transcript.md`.
