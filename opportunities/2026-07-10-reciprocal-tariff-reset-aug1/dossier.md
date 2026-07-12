---
id: 2026-07-10-reciprocal-tariff-reset-aug1
title: Trump reciprocal tariff reset on 14 countries takes effect Aug 1
status: researched
created: '2026-07-10T15:17:34Z'
event:
  type: regulatory
  summary: New US tariff rates on 14 countries including Japan and South Korea, delayed
    from a July 9 deadline, take effect August 1, 2026, raising cost pressure on major
    auto exporters.
  impact_window: '2026-08-01'
tickers:
- TM
- HMC
sources:
- title: Trump Tariff Tracker – July 2, 2026
  url: https://ourtake.bakerbotts.com/post/102n7tq/trump-tariff-tracker-july-2-2026
  accessed_at: '2026-07-10T15:17:34Z'
hypothesis:
  statement: >-
    The Aug 1 reciprocal tariff reset on TM/HMC is a fully telegraphed policy
    binary (second slipped deadline, close-ally carve-out pressure) whose
    fundamental impact is diluted by US-assembly footprints, MSRP pass-through,
    and JPY offset. The scenario distribution skews favorable-for-long (~70%
    delay/carve-out vs ~30% hits-as-announced), so the sign of any edge is long,
    never short. But the modeled net long edge (~+0.10%) is smaller than its own
    error bar (±0.3%), single-event t-stat ~0.05, and the price feed proved
    unusable for entry/stop/exit, so the edge is un-capturable even if real.
  direction: no-trade
  confidence: 70
plan:
  ticker: TM
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
  note: >-
    No position in TM or HMC in either direction. Monitor for (1) a verifiable,
    coherent price feed and (2) confirmed pre-Aug-1 news (formal Japan/Korea auto
    carve-out, a third delay, or a negotiated rate cut) before reopening the
    debate. If both trigger, the conditional structure would be a small,
    single-name TM long only (drop HMC).
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
    Bull argues the long-favoring asymmetry is genuine and 3x in the long's favor
    (net long -0.25% obscured a real +0.10% after Quant's own cost correction),
    and that a small, feed-conditional position monetizes an edge the others
    concede exists in sign. Bear and Quant hold that a +0.10% edge riding on
    subjective probabilities (55-58/100 confidence, ±0.3% uncertainty) with
    t-stat ~0.05 is statistically indistinguishable from zero, and that trading
    it pays real costs and short-vol tail risk to harvest noise. Unresolved: if
    a clean price feed had existed, would the +0.10% edge have justified a
    minimum-size long? The feed being unusable made this moot this time without
    resolving it on the merits.
  last_updated: '2026-07-12T13:03:04Z'
---

## Scouted 2026-07-10T15:17:34Z

## Researched 2026-07-12T13:03:04Z — NO-TRADE

Three-round panel debate (bull/sonnet, bear/sonnet, quant/opus, synthesizer/opus).
All three personas converged on **direction** (long > short, never short — the
telegraphed, once-already-slipped Aug 1 deadline skews toward further delay or a
Japan/Korea auto carve-out) but split on **action**. Bull argued a small, TM-only,
feed-conditional long was worth taking given the ~70/30 favorable scenario skew.
Bear (confidence 75/100) and Quant (confidence 62/100, having corrected an initial
cost mis-specification that had understated the long-side edge) both held no-trade:
the corrected net long edge (~+0.10%) sits inside its own probability-estimate
error bar (±0.3%), giving a single-event t-stat of ~0.05 — statistically
indistinguishable from zero. Independently and decisively, all three personas (and
the synthesizer, who verified it directly via `toa price`) found the `toa price`
feed for TM/HMC incoherent — intraday swings of 40%+ from a `stub:deterministic`
source, no autocorrelation, implausible for real equity ADRs — making any modeled
edge, real or not, un-executable (no trustworthy entry, stop, or exit level).
Synthesis: no position, size 0, confidence 70/100. Monitor for a coherent price
feed or confirmed pre-Aug-1 carve-out/delay/deal news before reopening. See
`transcript.md` for the full three-round debate.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
