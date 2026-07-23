---
id: 2026-07-22-banner-pacific-financial-merger-vote
title: Pacific Financial sets August 12 vote on Banner Corp merger
status: scheduled
created: '2026-07-22T11:19:27Z'
event:
  type: regulatory
  summary: Pacific Financial Corporation scheduled an August 12, 2026 special shareholder
    meeting to vote on its proposed merger with Banner Corporation; approval clears
    a key step toward deal close.
  impact_window: '2026-08-12'
tickers:
- BANR
sources:
- title: 'StockTitan: Banner outlines Pacific Financial merger vote process'
  url: https://www.stocktitan.net/sec-filings/BANR/425-banner-corp-business-combination-communication-2facafe02aab.html
  accessed_at: '2026-07-22T11:19:27Z'
hypothesis:
  statement: >-
    The 2026-08-12 PFC shareholder vote is a near-certain approval of a
    board-recommended bank merger in which BANR is the acquirer, not the
    target; catalyst reaction concentrates in the target (PFC, which is not
    a tracked ticker in this dossier), leaving BANR with only a tiny
    one-sided tail-removal skew (target-rejection risk going to zero) that
    sits below durable-edge size. Quant's estimated idiosyncratic move on
    BANR is roughly +10 to +25bps against ~150-250bps daily vol
    (signal-to-noise 0.05-0.10, below the ~0.15 durability threshold); the
    bull's 2-4% re-rating target is an unevidenced ~10x overshoot versus
    every quantitative estimate on the panel and no vol-term-structure
    elevation into 8/12 was observed to support it. The plan is also
    un-priceable by the real provider today (2026-08-12 has no data yet),
    which resolves as an uninformative neutral per prior lessons.
  direction: long
  confidence: 38
plan:
  ticker: BANR
  action: no-trade
  entry:
    time: '2026-07-23T13:35:00Z'
    target_price: 70.195
  exit:
    time: '2026-08-12T20:00:00Z'
    target_price: 70.31
  expected_profit_pct: 0.17
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
    Bear vs. quant, unresolved: bear holds strict NO TRADE (+/-15-40bps
    dwarfed by 150-250bps vol is noise-trading with costs attached, SNR
    0.05-0.10 explicitly below the 0.15 threshold, all views priced off a
    single 2026-07-22 print with zero data before 2026-08-12). Quant counters
    that NO TRADE understates a small real asymmetry, since tail-removal
    skew is genuinely one-sided even if tiny (+10-25bps), just below
    tradeable size. The panel never resolved whether a real-but-sub-threshold
    one-sided edge justifies token size or should be zeroed out entirely;
    both agree the only defensible expression of this catalyst is via PFC
    deal-spread convergence, which is untradeable here because PFC is not a
    tracked ticker in this dossier. All three seats concur the thesis would
    only become actionable on observable pre-vote binary-risk pricing on
    BANR (implied-vol term-structure elevation, spread widening, or abnormal
    volume), disclosed proxy-advisor "against" dissent, or an entry fill
    outside the USD 69.85-USD 70.55 band -- none of which exist in current
    data.
  last_updated: '2026-07-23T07:55:00Z'
---

## Scouted 2026-07-22T11:19:27Z

## Researched 2026-07-23T07:55:00Z — NO-TRADE (scheduled for record only)

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), single-opportunity
run per orchestrator instruction (no discovery, no cross-dossier comparison). Key
finding: BANR is the ACQUIRER in this merger, not the target -- Pacific Financial
Corporation (PFC) shareholders are the ones voting on 2026-08-12, and PFC is not a
tracked ticker in this dossier. Catalyst reaction on a board-recommended bank-merger
target vote concentrates in the target, not the acquirer; base-rate approval for such
votes is >90-95%, so this is a near-certain, largely-priced-in procedural step for
BANR specifically. Quant's estimated idiosyncratic move on BANR is +/-15-40bps versus
~150-250bps daily vol (signal-to-noise ~0.05-0.10, below the ~0.15 durability
threshold used elsewhere in this project). The bull's 2-4% re-rating target was
conceded in Round 2 as unevidenced and a ~5-10x mismatch against the panel's own
quantitative estimates once no vol-term-structure elevation into 8/12 was found. Real
price anchor: BANR = USD 70.195 at 2026-07-22T19:30Z (twelvedata, verified); no data
exists yet for 2026-07-23 (pre-market) or 2026-08-12 (future), so the exit leg cannot
be pre-validated against the real provider and this plan is filed as `scheduled` for
record-keeping rather than active execution. Verdict: NO-TRADE on BANR. Flips only on
observable pre-vote binary-risk pricing on BANR (IV elevation, spread widening,
abnormal volume), disclosed proxy-advisor opposition on the PFC side, or a future scout
adding PFC itself as a tracked ticker (where the panel agrees the real deal-spread
edge actually lives). Full debate in `transcript.md`.
