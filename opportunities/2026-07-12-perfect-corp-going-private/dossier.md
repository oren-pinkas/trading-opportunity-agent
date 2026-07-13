---
id: 2026-07-12-perfect-corp-going-private
title: Perfect Corp going-private merger with ProjectNY
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: economic
  summary: Perfect Corp signed a definitive .00/share cash going-private merger with
    ProjectNY (Alice Chang), ~48% premium, expected to close Q4 2026 pending shareholder
    vote.
  impact_window: '2026-10-15'
tickers:
- PERF
sources:
- title: Perfect Corp. Enters into a Definitive Agreement for a Going-Private Transaction
    - Morningstar
  url: https://www.morningstar.com/news/business-wire/20260710639441/perfect-corp-enters-into-a-definitive-agreement-for-a-going-private-transaction
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: PERF is a signed, definitive, all-cash management-led buyout
    (founder/CEO Alice Chang via ProjectNY) at a ~48% premium, targeting a
    Q4 2026 close subject to a shareholder vote. The deal-direction (converges
    to terms) is high-probability - panel-blended p(completion) ~= 0.82. But
    this is a merger-arb spread trade, not a directional bet, and its
    executability is fully gated by two independently broken inputs - the
    corrupted per-share deal price (missing from the dossier) and the
    incoherent, non-monotonic paper-trading price feed for PERF. Without a
    real deal price and a sane live quote the spread cannot be computed, so EV
    cannot be signed. Even after clean data, the modal expectation is that a
    2-3-day-stale, fast-arbed cash deal has already re-rated to a thin spread
    (est. 2-5%), below the p=0.82 breakeven of ~7.6% and far below the
    extended-hold hurdle of ~13-14%.
  direction: no_trade
  confidence: 84
plan:
  ticker: PERF
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: No position now. Re-open only if ALL hold simultaneously - (1) the
    actual per-share deal price is confirmed from the executed merger
    agreement/proxy, not the corrupted dossier field; (2) a cross-checked
    live quote from a real venue is available (the broken internal feed -
    $429.69/$401.80/$304.86 across 2026-07-09/10/13 - is disqualified); (3)
    the computed spread (deal price minus live price, over live price) is
    >8% and attributable to liquidity/technical dislocation rather than a
    priced-in break signal; (4) no active break trigger is present (no
    litigation escalation past routine disclosure settlement, no
    competing/go-shop bid, no opened Taiwan FSC/FTC review, no vote-delay or
    financing-failure headline). If opened, size small (~1/4 unit), model an
    extended hold (~0.45-0.55yr, not the naive 0.29yr) to account for
    MBO-driven delay, use event-based stops (not price stops), and converge
    to the deal price on a clean close. Suggested re-review on confirmation
    of the actual deal price, or sooner on any litigation/regulatory/vote
    headline.
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
  dissent: Whether the post-cleanup spread would actually clear ~8%. Bull
    holds that the no-trade call is an artifact of bad data, not a bad trade
    - once a real deal price and clean quote arrive, a defensible small long
    exists at the true convergence spread. Bear and quant hold that a
    well-covered, fast-arbed cash deal re-rates to within a few percent of
    terms almost immediately, so the likely spread is structurally thin and
    sits at or below breakeven regardless of data quality - i.e. the
    no-trade survives clean data. This is the exact quantity the post-mortem
    should measure first. Secondary unresolved fork - p(completion) itself -
    bull ~0.88 (no case-specific evidence of break risk in the record) vs.
    bear/quant ~0.80-0.85 (MBO conflict-of-interest plus unconfirmed
    financing/support agreements plus the Taiwan cross-border regulatory
    gate as genuine incremental hazards).
  lessons_applied:
  - 2026-07-01-ism-mfg
  - 2026-07-02-june-jobs
  last_updated: '2026-07-13T04:47:10Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-13T04:47:10Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 84/100
confidence. All three panelists converged from different starting points:
bull conceded that sizing a position off a corrupted deal price (the dossier
is missing the actual per-share cash price - it reads ".00/share") and an
economically incoherent price feed is indefensible, dropping confidence from
62 to 58. Bear reached no-trade on elevated MBO conflict-of-interest,
financing, Taiwan regulatory, and shareholder-vote risk stacked against an
already-thin post-announcement spread (confidence 82 -> 85). Quant reached
the same call independently via a non-computable EV (missing deal price,
broken feed) that converged on p(completion) ~= 0.82 and a breakeven spread
of ~7.6% against a likely live spread of only 2-5% (confidence 35 -> 88 in
no-trade). Full transcript: `transcript.md`.
