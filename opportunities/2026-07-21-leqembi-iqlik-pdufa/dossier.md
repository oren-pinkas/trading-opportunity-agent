---
id: 2026-07-21-leqembi-iqlik-pdufa
title: Leqembi IQLIK PDUFA decision
status: researched
created: '2026-07-21T10:40:07Z'
event:
  type: regulatory
  summary: FDA PDUFA date for Leqembi IQLIK (subcutaneous formulation) extended to
    Aug 24 2026 after agency requested additional information in May
  impact_window: '2026-08-24'
tickers:
- BIIB
sources:
- title: 'BiopharmaWatch: PDUFA Calendar 2026'
  url: https://www.biopharmawatch.com/PDUFA-calendar
  accessed_at: '2026-07-21T10:40:07Z'
hypothesis:
  statement: "A directional trade on BIIB around the Leqembi IQLIK subcutaneous
    PDUFA (2026-08-24) does not carry positive expected value net of costs. This
    is a low-information-content convenience-reformulation event on an
    already-approved mechanism (lecanemab), in a diversified large-cap; approval
    is the base case (about 80 percent) but the approve-side magnitude is small
    and largely priced in (about 1.2 percent), and the CRL/delay tail (about -4.0
    percent) is real but not large enough to make either direction cheap. All
    three seats converged toward no-trade: bull cut confidence 55 to 40, bear
    raised no-edge confidence 80 to 88 percent, and quant's net expected value
    crossed to negative (-0.34 percent to -0.14 percent net of slippage), with a
    signal-to-noise ratio of about 0.07, well below the 0.15 durability floor."
  direction: none
  confidence: 12
plan:
  ticker: BIIB
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: null
research:
  strategy: three-round-panel
  personas: [bull, bear, quant]
  dissent: "No seat verified what the May 2026 'additional information' request
    actually concerns. If it is device or human-factors (combination-product)
    data for the autoinjector, P(approve) and the CRL tail both worsen
    materially; if it is clinical or CMC-only, the bull's upside case
    strengthens -- the no-trade call rests on this unverified assumption.
    Secondary and unresolved: neither bear nor quant modeled interim
    information flow -- a leaked or disclosed clean human-factors readout
    before 2026-08-24 could drive pre-decision drift, a potentially different
    tradeable setup this debate's binary-event framing does not capture.
    Post-mortem should check whether such a signal appeared and whether any
    edge existed pre-decision rather than at the PDUFA print itself."
  last_updated: '2026-07-23T00:04:13Z'
---

## Scouted 2026-07-21T10:40:07Z

## Researched 2026-07-23T00:04:13Z

Three-round panel debate (bull/bear/quant, synthesizer opus) converged on
**NO-TRADE** for the Leqembi IQLIK PDUFA (2026-08-24). Full transcript with
citations: `transcript.md`.

Verdict driver: this is a subcutaneous-formulation approval of an already-approved,
already-marketed drug (lecanemab) inside a diversified large-cap -- low information
content, magnitude largely priced in. Quant's EV sensitivity, after incorporating
bear's device/human-factors risk point, crossed to negative net of slippage
(gross signal-to-noise ~0.07, below the 0.15 durability floor). No entry/exit
timestamps were finalized; any revisit must first verify pricing via
`toa price BIIB <timestamp> --provider twelvedata` per institutional lesson,
or default back to no-trade.
