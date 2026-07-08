---
id: 2026-07-23-union-pacific-q2-fy26
title: Union Pacific Q2 FY26 earnings
status: researched
created: '2026-07-07T22:42:46Z'
event:
  type: earnings
  summary: Union Pacific reports Q2 2026 July 23; volumes and merger-narrative commentary
    drive rails.
  impact_window: '2026-07-23'
tickers:
- UNP
sources:
- title: Businesswire UNP earnings date
  url: https://www.businesswire.com/news/home/20260625996926/en/Union-Pacific-Corporation-Announces-Second-Quarter-2026-Earnings-Release-Date
  accessed_at: '2026-07-07T22:42:46Z'
hypothesis:
  statement: UNP Q2 FY26 (reporting 2026-07-23) is a low-information, already-priced-in
    Class I rail print. Weekly AAR carload data makes volumes visible pre-release
    and guidance is typically reiterated, not reset, so there is no demonstrated directional
    forecasting edge (50/50). The distribution carries a fat, un-hedgeable tail --
    widened by the July 27 STB supplemental-filing deadline four days out, which layers
    merger-tone/regulatory-parsing risk on top of the earnings distribution -- that
    cannot be capped because the sim surface offers naked equity only (no executable
    options). Net EV sits far below the action threshold.
  direction: none
  confidence: 20
plan:
  ticker: UNP
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
  dissent: 'The sharpest unresolved tension is the epistemic status of Q1 FY26''s
    ~7% one-day move. Bull reads it as possible evidence rail prints carry more information
    than public AAR carload data captures (a repeatable positive skew), while conceding
    it might be a one-off outlier. Bear/Quant read the same data point as a single
    draw from an already-assumed 10-15% tail -- recency/small-sample overfitting,
    echoing the NKE single-print-anomaly lesson. Nobody produced the multi-quarter
    post-earnings move distribution for UNP that would adjudicate this; Quant''s tail-probability
    revision (12%->20%, mean 3.25%->3.75%) is an unfalsified judgment call. A subtler
    split: Bear implies the July 27 STB deadline makes management''s July 23 tone
    structurally cautious (a mild negative skew), while Quant insists direction stays
    strict 50/50 and the deadline only widens variance -- that latent short-lean was
    never tested. Also log: the entire no-trade outcome is contingent on one unverified
    structural assumption -- that no options are executable on this stub feed. If
    that assumption is ever falsified, the analysis does not merely re-size, it reopens,
    because a defined-risk long-call structure would neutralize the single decisive
    filter (the un-hedgeable tail).'
  last_updated: '2026-07-08T15:20:00Z'
---

## Scouted 2026-07-07T22:42:46Z

## Researched 2026-07-08T15:20:00Z — NO-TRADE

Three-round bull/bear/quant panel converged on NO-TRADE, with conviction strengthening across rounds rather than softening: directional confidence decayed monotonically (bull 62->33, bear 25->20, quant 22->20) while the quant's no-trade confidence rose (78->82). All four institutional no-trade filter conditions were met and reinforced in Round 2: (1) confidence <=45 -- every persona's terminal directional confidence landed at or below 33; (2) un-hedgeable tail -- this simulation's naked-equity-only surface cannot cap the ~10-20% probability of a >6% move, and the July 27 STB supplemental-filing deadline (a company filing obligation, not a ruling -- a point the bull explicitly retracted after initially over-coupling it to the print) adds a second, orthogonal, un-hedgeable regulatory-tone risk channel; (3) net EV <2% -- even under a generous 55/45 directional skew the quant computes net EV of roughly +0.18-0.23% after ~0.15% costs, an order of magnitude below the 2% action threshold, with gross EV at true 50/50 sitting at 0% before costs; (4) adverse-tail-to-edge ratio ~40:1+ -- the Round 2 tail-widening (legitimately motivated by UNP's Q1 FY26 ~7% one-day earnings-beat rally per Tickeron) made this ratio worse, not better, since variance rose without any accompanying directional edge. Key sourced facts: Businesswire confirmed the July 23, 2026 earnings date; STB accepted the UP-Norfolk Southern merger application May 28, 2026, held it in abeyance, and ordered supplemental information due July 27, 2026 (four days after this print). Bull's Q1 FY26 evidence (freight revenue +4% first-quarter record, Bulk segment +10% revenue on 12% volume growth, Industrial +5%, intermodal's third consecutive record quarter, operational metrics improving across velocity/dwell/productivity) was real and sourced but insufficient to establish a repeatable directional edge over a symmetric base rate. No position taken; no entry/exit window opened.
