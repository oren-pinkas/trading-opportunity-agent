---
id: 2026-07-16-tsmc-q2-fy26
title: TSMC reports Q2 FY26 earnings
status: researched
created: '2026-07-12T23:20:25Z'
event:
  type: earnings
  summary: TSMC holds its Q2 2026 earnings conference on July 16; AI-chip demand and
    advanced-node capex guidance are the key catalysts for semiconductor supply-chain
    names.
  impact_window: '2026-07-16'
tickers:
- TSM
sources:
- title: 'TSMC Q2 Earnings Preview: Why Should You Buy TSM Stock Before July 16?'
  url: https://finance.yahoo.com/markets/stocks/articles/tsmc-q2-earnings-preview-why-190000466.html
  accessed_at: '2026-07-12T23:20:25Z'
hypothesis:
  statement: >-
    TSMC's Q2 FY26 fundamental bias is a beat-and-raise (AI/HPC demand is
    capacity-constrained, not demand-constrained), but the entire information
    content of the print lands in the overnight ADR gap to the Taiwan-morning
    release, which closes before the 13:30Z US cash open and is un-capturable
    under the simulator's equity-only, in-session fill constraints. Only
    approximately 0.8-1.5% of near-directionless intraday drift remains
    tradeable, at a approximately 52-56% continuation hit rate, netting
    approximately 0-0.2% EV after costs -- an order of magnitude below the 2%
    no-trade threshold, against a approximately 7-15x adverse-tail-to-edge ratio
    with no options hedge available to define the tail.
  direction: long
  confidence: 34
plan:
  ticker: TSM
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
  dissent: >-
    The bull's strongest surviving idea is a same-day in-session catalyst (a
    sell-side PT-revision cascade, or NVDA sympathy momentum with volume
    confirmation by approximately 13:45Z) that could widen the capturable
    intraday fraction enough to matter; a de-minimis, confirmation-gated TSM
    long (enter only on a green/holding opening tape, target +1.5%) is the only
    structure worth revisiting if that appears. Bear and quant hold that this
    still nets approximately 0% EV and could not be resolved without live tape --
    no persona believes a dataset exists showing >=62% continuation hit rate
    with >=2% net captured move on strong-tape TSM earnings days.
  last_updated: '2026-07-22T17:44:41Z'
---

## Scouted 2026-07-12T23:20:25Z

## Researched 2026-07-22T17:44:41Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), single opportunity,
no cross-comparison to other dossiers. All three personas converge on NO-TRADE: the
fundamental bias is genuinely long (TSMC beat-and-raise remains base case, AI demand
capacity-constrained), but the entire information content of this event lands in the
overnight ADR gap that closes before the US cash open -- un-capturable under the
equity-only, in-session fill constraints. The QUANT's base-rate/EV framing was decisive:
approximately 70-85% of the total move is realized in the overnight gap, leaving only
approximately 0.8-1.5% capturable intraday drift at a weak approximately 52-56%
continuation hit rate; every EV path (blind or confirmation-gated) nets approximately
0.0% to +0.2% after costs, an order of magnitude below the 2% threshold, against a
approximately 7-15x adverse-tail-to-edge ratio with no options hedge available. The BULL
conceded in Round 2 that its initial "+4-6%" target conflated the total event move with
the un-capturable in-session fraction, folding to a de-minimis confirmation-gated long
that still nets approximately 0% EV. NVDA as a read-through vehicle was rejected by all
three as strictly worse (second-derivative noise). Verdict: NO-TRADE (not scheduled, not
simulated). Full debate with citations in `transcript.md`.
