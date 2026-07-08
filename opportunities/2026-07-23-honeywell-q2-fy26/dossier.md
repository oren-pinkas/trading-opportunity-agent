---
id: 2026-07-23-honeywell-q2-fy26
title: Honeywell Q2 FY26 earnings
status: researched
created: '2026-07-07T22:42:46Z'
event:
  type: earnings
  summary: Honeywell Technologies (post-Aerospace-spin pure-play automation entity)
    reports its first standalone Q2 2026 results July 23, before market open, with
    an updated 2026 outlook. The breakup is already complete (Solstice spun Oct 2025,
    Aerospace/HONA spun Jun 29 2026 with a 1-for-2 reverse split), not upcoming.
  impact_window: '2026-07-23'
tickers:
- HON
sources:
- title: StockTitan HON earnings
  url: https://www.stocktitan.net/news/HON/honeywell-technologies-to-release-second-quarter-financial-results-59jvz8t45sma.html
  accessed_at: '2026-07-07T22:42:46Z'
- title: Honeywell Completes Spin-Off of Solstice Advanced Materials
  url: https://investor.honeywell.com/news-releases/news-release-details/honeywell-completes-spin-solstice-advanced-materials
  accessed_at: '2026-07-08T14:30:06Z'
- title: Honeywell Technologies Launches As Independent, Pure-Play Automation Company
  url: https://www.honeywell.com/us/en/news/press-releases/2026/06/honeywell-technologies-launches-independent-pure-play-automation-company-following-honeywell-aerospace-spin-off
  accessed_at: '2026-07-08T14:30:06Z'
- title: Honeywell International's Q2 2026 Earnings — What to Expect (Barchart)
  url: https://www.barchart.com/story/news/3098477/honeywell-international-s-q2-2026-earnings-what-to-expect
  accessed_at: '2026-07-08T14:30:06Z'
- title: Is Honeywell Stock a Buy After Its Latest Structural Overhaul? (Motley Fool)
  url: https://www.fool.com/investing/2026/07/03/is-honeywell-stock-a-buy-after-its-latest-structur/
  accessed_at: '2026-07-08T14:30:06Z'
- title: Honeywell Stock Falls After Q1 2026 Earnings Miss (TIKR)
  url: https://www.tikr.com/blog/honeywell-stock-falls-after-q1-2026-earnings-miss-what-the-june-29-aerospace-spin-means-for-investors
  accessed_at: '2026-07-08T14:30:06Z'
hypothesis:
  statement: HON's first standalone quarterly print as pure-play "Honeywell Technologies"
    on 2026-07-23 is a genuine binary event whose true outcome dispersion is wider
    than the ~4% implied move suggests, because no earnings history exists for the
    stub entity, two irreconcilable guidance bases (legacy combined-company $10.35-10.65
    FY26 EPS vs new stub-only $3.95-4.15) contaminate every circulating consensus
    figure, and live Middle East/Process Automation drag plus spin dis-synergies land
    in this exact quarter. Directional edge is indistinguishable from zero after costs,
    and event tail risk is plausibly underpriced by 91st-99th-percentile IV rather
    than overpriced, so no structure (long, short, or short-vol) clears its adverse-tail-to-edge
    ratio.
  direction: none
  confidence: 80
plan:
  ticker: HON
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  rationale: Two of three personas (bear, quant) independently converged on NO-TRADE
    after explicitly modeling costs and tail risk; a symmetric iron condor nets ~$0.00-0.05/spread
    against a $4.80 max loss (60-100:1 adverse-tail ratio), and directional debit
    structures run negative EV (~-$0.78) from overpaying 91st-percentile IV. Bull's
    one-sided put credit spread ($205P/$195P) was the most disciplined bullish idea
    but rests on two unvalidated assumptions -- that the old combined-entity
    -7.6% worst-case base rate transfers to a zero-history stub, and that elevated
    IV is harvestable premium rather than fair compensation for genuine first-print/guidance-reconciliation
    gap risk. Stand aside; revisit post-print once the RemainCo base is established.
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
  dissent: 'The unresolved crux is whether elevated IV (Rank 91.75, percentile 99)
    is a mispricing to harvest or fair compensation for a genuinely unmeasured tail.
    Bull argues a $205/$195 put credit spread with a -6.9% breakeven sits beyond
    the -7.6% historical worst case and monetizes rich premium one-sidedly -- defensible
    if that historical base rate transfers and if management sandbagged the Day-1
    stub guide to beat-and-raise. Bear and quant counter that the base rate belongs
    to a now-defunct combined entity and that sparse modeling on the new stub base
    widens true dispersion beyond the quoted 4% implied move, so the -7.6% "floor"
    is not a floor at all. If HON beats-and-reconciles cleanly and compresses the
    uncertainty discount toward the ~$240 average analyst target, the stood-aside
    book leaves real, defined-risk money on the table -- the thread a post-mortem
    should pull if HON prints a large positive move on Jul 23.'
  last_updated: '2026-07-08T14:30:06Z'
---

## Scouted 2026-07-07T22:42:46Z

## Researched 2026-07-08T14:30:06Z — NO-TRADE

Three-round panel (bull/bear/quant) converged on NO-TRADE, with a critical mid-debate
correction: the dossier's synthetic reference price ($312.47) was wrong by ~42%;
bear and quant independently flagged the discrepancy in Round 1 from web research,
confirmed in-session via `toa price HON 2026-07-08T14:30:00Z --provider twelvedata`
= $220.24 (real feed). All subsequent analysis re-anchored to $220.24.

Honeywell's breakup is complete, not upcoming (Solstice spun Oct 2025, Aerospace/HONA
spun Jun 29 2026 with a 1-for-2 reverse split of the parent, now "Honeywell Technologies").
July 23 is the first-ever standalone print for this entity — zero earnings history,
and two irreconcilable guidance bases in circulation (legacy combined $10.35-10.65
FY26 EPS vs new stub-only $3.95-4.15) that make most circulating "consensus" figures
(e.g. $4.83 Q2 EPS / -12.2% YoY) likely stale artifacts rather than a clean read —
bull and quant both converged on this independently in Round 2.

Q1 FY26 (Apr 23) previewed the risk pattern: beat adj EPS (+5.6%) but missed revenue,
guided Q2 below Street, and the stock fell -2.6% despite the beat (beat-and-fade),
with Middle East drag (~0.5%→~1% in Q2, concentrated in Process Automation) still
live inside the automation-only stub. Options are priced at IV Rank 91.75 / percentile
99 (~4% implied 1-day move) — quant modeled every structure (long, short, and a
short-vol iron condor) as EV-indistinguishable-from-zero to negative after costs
against large adverse-tail ratios (60-100:1 on the condor). Bear independently argued
elevated IV likely reflects real, underpriced first-print/guidance-reconciliation
gap risk rather than overpriced premium to harvest.

Bull's best idea — a one-sided $205P/$195P put credit spread (breakeven beyond the
-7.6% historical worst case) — was the most disciplined bullish structure raised,
but rests on assumptions (old-entity base-rate transferability; IV as harvestable
premium) that bear and quant's cost/tail accounting undercut. Two independent
NO-TRADE conclusions (~80-82% confidence) via different mechanisms override the
single conditional bullish structure. Reconsideration triggers before Jul 23: (1)
pre-earnings 8-K reconciling the two guidance bases onto a single continuing-ops
basis; (2) confirmation the $4.83 Q2 consensus figure is real vs. a stale-basis
artifact; (3) IV Rank dropping materially below ~50; (4) disclosure on whether
Middle East softness is order cancellation (structural) vs. timing delay (recoverable).
Confidence in NO-TRADE: 80/100. Anchor HON $220.24 @ 2026-07-08T14:30Z (twelvedata).
