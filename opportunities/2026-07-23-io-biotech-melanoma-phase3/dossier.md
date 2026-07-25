---
id: 2026-07-23-io-biotech-melanoma-phase3
title: IO Biotech Phase 3 Melanoma Data Readout
status: researched
created: '2026-07-23T01:19:37Z'
event:
  type: product
  summary: IO Biotech IO102-IO103 plus Keytruda Phase 3 melanoma readout due August
    2026, narrowly missed statistical significance threshold per early reads
  impact_window: '2026-08-15'
tickers:
- IOBT
sources:
- title: 10 clinical trials to watch in H2 2026 - BioPharma Dive
  url: https://www.biopharmadive.com/news/biotech-pharma-clinical-trials-watch-2026/808255/
  accessed_at: '2026-07-23T01:19:37Z'
hypothesis:
  statement: IO Biotech's Phase 3 melanoma readout (IO102-IO103 plus pembrolizumab,
    window 2026-08-15) is not a tradeable opportunity in this harness. IOBT has no
    price coverage in the available data provider (HTTP 400 "MarketDataUnavailable"
    on three separate dates, vs a passing AAPL control), and the underlying thesis
    skews negative independent of that gate — an early "narrow miss" on statistical
    significance is a recognized precursor to primary-endpoint failure, not a coin
    flip, with modeled long EV of roughly USD -19 to -21 per 100 and no safely
    sizable short given thin microcap liquidity and no options-chain pricing in
    the harness.
  direction: none
  confidence: 87
plan:
  ticker: IOBT
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
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
  dissent: "The PASS is unanimous but over-determined by two separable routes: the
    data-coverage gate (decisive on its own) and thesis EV (independently negative).
    The thesis question itself was never fully settled between personas. Bull
    maintained an interim narrow miss is not near-certain failure and that late
    curve separation is mechanistically plausible for a T-cell vaccine plus
    checkpoint-inhibitor combo; Bear rejected this as unfalsifiable absent trial
    design specifics (interim analysis type, endpoint, margin all unknown from
    the single listicle source); Quant priced the concession at only 3 percentage
    points shifted from clear-miss to ambiguous (long EV moving from USD -20.8 to
    USD -19 per 100), calling it a non-actionable update. If IOBT prints a clear
    win on 2026-08-15, the correct lesson is that the coverage gate was right but
    the thesis EV sign was possibly wrong -- not that the panel's thesis reasoning
    was validated. No persona quantified timeline-slip risk (readout landing
    outside the 2026-08-15 window), which the bear raised in round 1 and nobody
    revisited."
  last_updated: '2026-07-25T14:42:34Z'
---

## Scouted 2026-07-23T01:19:37Z

## Researched 2026-07-25T14:42:34Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Two independent
routes converged on PASS. Route 1 (decisive): `toa price IOBT <ts> --provider
twelvedata` returned HTTP 400 MarketDataUnavailable on three separate dates
(2026-07-22/23/24) while an AAPL control resolved normally in the same run; the
default no-flag provider returned a fabricated stub price of USD 295.08 for what
is a sub-USD-5 microcap. IOBT is structurally absent from the twelvedata symbol
universe -- the same class of gap previously documented for .NS and .PA tickers,
not a transient outage -- so no fill, stop, or exit can be simulated. Route 2
(independent of coverage): the dossier's own framing that early reads "narrowly
missed statistical significance" is a recognized precursor to confirmed
primary-endpoint failure (regression to the mean, alpha-spending penalties), and
the only source is a single non-primary trade-press listicle with no
clinicaltrials.gov ID or company PR/8-K. Quant modeled P(clear win)=0.20,
P(ambiguous)=0.25-0.28, P(clear miss)=0.52-0.55, giving long EV of roughly
USD -19 to -21 per 100; the nominally positive short EV carries a fat, largely
unbounded gap tail in a thin microcap with no options-chain pricing available in
this harness. Bull withdrew his proposed small defined-risk long as unimplementable
once both findings landed. No position opened. Revisit only if BOTH: (1)
`toa price IOBT` returns a real quote with an AAPL control passing in the same
run, and (2) the listicle is replaced by a primary trial-registry source (NCT ID
or company PR/8-K) specifying the interim analysis type, endpoint, and actual
margin. Full debate with citations in `transcript.md`.
