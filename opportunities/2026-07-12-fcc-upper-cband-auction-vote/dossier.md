---
id: 2026-07-12-fcc-upper-cband-auction-vote
title: FCC votes on Upper C-Band spectrum auction rules
status: researched
created: '2026-07-12T11:57:54Z'
event:
  type: regulatory
  summary: FCC will vote July 22, 2026 on an order to auction 160 MHz of Upper C-Band
    spectrum, combining with cleared Lower C-Band into a 440 MHz block for wireless
    carriers.
  impact_window: '2026-07-22'
tickers:
- T
- VZ
- SATS
sources:
- title: FCC sets July 22 vote on Upper C-Band auction, giving broadcasters a firm
    timeline
  url: https://www.newscaststudio.com/2026/06/30/fcc-sets-july-22-vote-on-upper-c-band-auction-giving-broadcasters-a-firm-timeline/
  accessed_at: '2026-07-12T11:57:54Z'
hypothesis:
  statement: >-
    The FCC's 2026-07-22 vote is a fully telegraphed, ~94%-consensus procedural
    rules order (auction itself is H1 2027, deployment is 2030/2031) with no
    tradeable directional edge in T, VZ, or SATS after transaction costs; the
    SATS ticker is additionally stale -- EchoStar rebranded to ECHO in June 2026
    after already monetizing its spectrum to SpaceX/AT&T and is not a beneficiary
    of this specific order.
  direction: none
  confidence: 82
plan:
  ticker: null
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
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
  dissent: >-
    Bull's residual live claim: vote-day flow (momentum algos + short-covering
    into removed delay-risk) could give VZ a ~55/45 skew tradeable via a tightly
    bracketed T-1/T+2 defined-risk options structure. Quant's final sensitivity
    refutes this on EV even granting Bull's best case (gross EV +0.017% vs 0.08%
    cost floor = -0.063% net), but that table does not explicitly price IV crush
    on short-dated options around a scheduled, known-date binary -- cutting even
    harder against Bull rather than for him. Deeper unresolved question: Bear/Quant
    argue any genuine surprise is net-negative for carriers (buyers/payers facing
    more future capex/clearing cost), so even Bull's momentum mechanism may point
    the wrong direction.
  last_updated: '2026-07-12T21:54:06Z'
---

## Scouted 2026-07-12T11:57:54Z

## Researched 2026-07-12T21:54:06Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation
on this opportunity alone. BULL opened with a swing long in VZ (favored over T for
torque, avoided SATS) on the thesis that the rules vote itself -- not just the later
auction -- removes multi-year regulatory uncertainty and that 160MHz vs. the 100MHz
statutory minimum is a bullish supply surprise, citing the 2020 Intelsat +25%/week
precedent around the original C-Band rules vote. BEAR called it a non-event: a
procedural rules order whose real economic impact (auction proceeds, deployment) is
1-5 years out, fully telegraphed since the 2025 OBBBA mandate/NPRM/July-1 draft
order, and flagged that EchoStar rebranded SATS to ECHO in June 2026 after already
closing ~$40B+ of spectrum sales to SpaceX/AT&T -- making the SATS leg of the thesis
stale. QUANT built an explicit EV calc (~94% pass probability, but irrelevant to
P/L since consensus; sub-0.5% attributable move for large-cap telecom around
procedural votes historically) showing net EV of roughly -0.20% on a T/VZ long
after costs and opportunity cost, and confirmed SATS has near-zero linkage to this
specific order.

Under rebuttal, BULL fully conceded the SATS leg was dead (confirmed the rebrand
and an EchoStar going-concern disclosure worse than bear had stated) and conceded
the "160MHz surprise" was 12-day-old, already-public information -- but pushed back
that Quant's 50/50 prior assumed away any edge by construction, arguing a modest
event-day momentum/short-covering skew (~55/45) was still plausible, and narrowed
to a small, tightly-bracketed VZ options structure around T-1/T+2 instead of the
original wide multi-day entry. BEAR showed the Intelsat comp was a category error:
Intelsat was the spectrum SELLER receiving direct clearing/incentive payments in
2020, while T/VZ are BUYERS in a future auction -- a structurally opposite role --
so the 2026 analogue to "Intelsat 2020" would be SES/Eutelsat, not the tickers in
this dossier. QUANT revised the SATS EV further downward (post-rebrand linkage
~0 but idiosyncratic vol still high -- worse EV profile, not neutral) and produced
a final table showing that even granting Bull's best-case sensitivity (doubled
surprise probability + a 55/45 edge for VZ), gross EV of +0.017% still falls short
of the ~0.08% cost floor, netting -0.063%.

Two independent methodologies (bear's telegraphing/category-error analysis, quant's
explicit EV) converged on NO TRADE across all three tickers, and Bull's own final,
scaled-down proposal did not survive Quant's numbers. SATS was unanimously dropped
by Round 2 as unrelated to this event following EchoStar's June 2026 rebrand to
ECHO. Verdict: NO-TRADE. Full debate with citations in `transcript.md`.
