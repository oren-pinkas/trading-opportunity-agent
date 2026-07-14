---
id: 2026-07-13-sanofi-sarclisa-subq-pdufa
title: Sanofi Sarclisa subcutaneous PDUFA decision
status: researched
created: '2026-07-13T03:25:44Z'
event:
  type: regulatory
  summary: FDA PDUFA date July 23, 2026 for subcutaneous isatuximab (Sarclisa) in
    multiple myeloma.
  impact_window: '2026-07-23'
tickers:
- SNY
sources:
- title: 'FDA drug approval decisions: July and August 2026'
  url: https://lifesciencedaily.news/fda-drug-approval-decisions-to-watch-july-and-august-2026/
  accessed_at: '2026-07-13T03:25:44Z'
hypothesis:
  statement: The scouted premise is stale. FDA approved subcutaneous isatuximab-irfc
    (Sarclisa Escena) on 2026-07-09, roughly two weeks ahead of the dossier's stated
    2026-07-23 PDUFA date, per FDA.gov and Sanofi's own 2026-07-10 press release,
    with no CRL history and a clean Phase 3 IRAKLIA non-inferiority basis (ORR 71.1
    percent SC vs 70.5 percent IV). The binary resolved to P(approval) equals 1.0
    before research began, collapsing forward expected value on the original event
    trade to roughly zero, net-of-costs negative. A fallback thesis (long SNY into
    Sanofi's 2026-07-30 Q2 earnings on first Escena launch commentary) does not
    survive scrutiny either - Escena launched nine days into Q3, so Q2 financials
    contain zero Escena revenue, and Sarclisa is only about 1.1 to 1.3 percent of
    Sanofi's revenue against a roughly USD 117 to 120 billion market cap dominated
    by Dupixent, vaccines, FX, and guidance. Even a blowout Sarclisa surprise moves
    group revenue by only about 0.2 to 0.25 percent. All three personas independently
    discovered the stale-catalyst fact in Round 1 and unanimously converged on no-trade
    by Round 2.
  direction: no-trade
  confidence: 82
plan:
  ticker: SNY
  action: no-trade
  entry:
    time: null
    target_price: null
    trigger: Monitor only. The only structurally coherent residual idea raised (a
      tiny defined-risk implied-vol fade if the option chain shows stale elevated
      IV for the now-resolved approval) was never confirmed - no panelist pulled
      option-chain data - so there is no green light for any position. Re-open only
      on a new, independently-sized catalyst (e.g. a surprise competitive or label
      development in anti-CD38 myeloma), not on the 2026-07-30 earnings print itself.
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: Two unresolved items preserved for post-mortem. First, a three-way price-data
    discrepancy in the approval-window reaction - bull read plus 0.6 percent over
    two sessions, bear read minus 0.82 percent on approval day (Benzinga/Seeking
    Alpha), quant read plus 2.0 percent on approval day fading to roughly flat by
    Jul 13 (twelvedata) - never resolved to one canonical sourced number, though
    all three versions sit inside SNY's approximately 1.1 to 1.5 percent daily vol
    band so the no-trade conclusion is robust regardless. This is a recurring price-provenance
    weakness in this system worth a standing fix (single canonical price source
    plus exact UTC timestamp per dossier), related to the standing lesson that toa
    price silently returns stub data without the twelvedata provider flag. Second,
    a process tell - the bull persona pivoted to a manufactured Q2-earnings binary
    immediately after conceding the original PDUFA thesis was dead, rather than defaulting
    to pass, and only downgraded to watch-only under bear/quant pressure once the
    zero-Escena-revenue-in-Q2 arithmetic was shown. Worth flagging as a bias pattern
    distinct from the trade outcome itself.
  last_updated: '2026-07-14T04:35:00Z'
---

## Scouted 2026-07-13T03:25:44Z

## Researched 2026-07-14T04:35:00Z

Debate converged unanimously on no-trade. The dossier's scouted PDUFA date (2026-07-23)
was already stale by the time of research: FDA approved subcutaneous Sarclisa
(Sarclisa Escena) on 2026-07-09, ahead of schedule, with a muted market reaction.
Full three-round transcript: [transcript.md](transcript.md).
