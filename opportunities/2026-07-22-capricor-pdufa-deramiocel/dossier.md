---
id: 2026-07-22-capricor-pdufa-deramiocel
title: Capricor Deramiocel PDUFA decision
status: scheduled
created: '2026-07-22T07:00:28Z'
event:
  type: regulatory
  summary: FDA PDUFA target action date Aug 22 2026 for Capricor's Deramiocel BLA
    in Duchenne muscular dystrophy
  impact_window: '2026-08-22'
tickers:
- CAPR
sources:
- title: SEC 8-K - Capricor Therapeutics
  url: https://www.sec.gov/Archives/edgar/data/0001133869/000110465926078327/capr-20260626x8k.htm
  accessed_at: '2026-07-22T07:00:28Z'
- title: Twelve Data 1min bar, CAPR 2026-07-22 (price anchor)
  url: https://api.twelvedata.com/time_series?symbol=CAPR&interval=1min&date=2026-07-22&timezone=UTC
  accessed_at: '2026-07-23T10:35:29Z'
hypothesis:
  statement: >-
    CAPR's Aug 22 2026 Deramiocel PDUFA is a fair-priced binary whose gap outcome
    carries no analyzable edge in this dossier (no volume, skew, short-interest, or
    AdCom data; the panel's 55/45 approval prior is an unverified assumption and EV
    collapses toward zero at a coin flip). All three personas independently rejected
    holding a naked position through the binary itself. The only defensible exposure
    is a small, gated long that captures pre-catalyst sentiment drift and is fully
    closed out before the Saturday PDUFA date, hard-gated to stand down if CAPR has
    already run up materially (>10-15%) versus the USD 18.8225 anchor by entry.
  direction: long
  confidence: 33
plan:
  ticker: CAPR
  action: buy
  entry:
    time: '2026-08-11T13:30:00Z'
    target_price: 18.85
  exit:
    time: '2026-08-21T19:55:00Z'
    target_price: 19.65
  expected_profit_pct: 4.0
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
    Bear's crowding objection is unresolved and is the strongest live threat: "buy
    before the date, sell before the print" is the most-faded biotech setup, so the
    drift may already be priced in, and the Aug 11 entry can fill into an already
    extended tape while elevated implied vol crushes the very run-up the trade means
    to harvest -- meaning pre-PDUFA de-risking or a leak could compress a CRL-like
    slide into the exact Aug 21 exit window, converting a "safe" drift exit into a
    small realized loss. Bear would only accept this as a strict tiny stop-defined
    trade and argues no-trade (avoid) is correct; the synthesis overrides that to a
    gated long because the setup is still marginally EV-positive, but the drift-EV
    estimate is fragile and the hard stand-down gate is doing most of the risk
    control.
  last_updated: '2026-07-23T10:35:29Z'
---

## Scouted 2026-07-22T07:00:28Z

## Researched 2026-07-23T10:35:29Z — SMALL GATED LONG (drift-only, no hold-through-binary)

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). CAPR PDUFA for
Deramiocel (DMD cell therapy BLA) lands Sat 2026-08-22 -- a non-tradeable calendar
date, so all execution timestamps are anchored to the nearest valid session per
institutional lesson from the CZR debate. Price anchor: USD 18.8225 at
2026-07-22T19:30Z (twelvedata), down ~4% intraday from USD 19.62 at 15:00Z same
session.

BULL opened long (55-60% confidence), reading the intraday fade as noise and the
setup (first-in-class DMD cell therapy, orphan/rare-pediatric FDA flexibility, no
disclosed negative signal) as favoring a small defined-risk long held through the
catalyst. BEAR opened AVOID (65% confidence), arguing binary FDA catalysts are
structurally asymmetric, the named PDUFA means implied vol is already elevated and
the trade is common-knowledge/crowded, and the 4% fade is a caution flag, not an
entry signal -- with no trial/AdCom/label data in the dossier to break the tie.
QUANT opened with explicit EV math: P(approval)=0.55/P(CRL)=0.45, EV holding through
the gap ~+7.8% gross / ~+4.5-5.5% net -- positive but thin and collapsing to ~0 at
P=0.50 (does not clear a durable signal-to-noise bar). Quant favored DRIFT-ONLY
(capture pre-catalyst run-up, exit before the binary) over the naked into-event
hold, sized at 0.5% (half book).

In rebuttal, BULL conceded the 4% fade is a real data gap (not pure noise) and
downsized to quant's 0.5% half-size, but kept direction and hold-through-catalyst
timing. BEAR held firm, arguing quant's drift-only "relocates" the risk into a
discretionary Aug-21 exit rather than eliminating it, and that quant's own P=0.50
sensitivity concedes the point. QUANT sided with bear's crowding argument enough to
cut confidence to 3/10 and explicitly REJECTED holding through the gap, converging
on a small, mechanical, hard-gated drift trade with a stand-down condition.

VERDICT: all three personas independently rejected a naked hold-through-the-gap
position. Plan: small gated long, entry 2026-08-11T13:30Z (~USD 18.85, US session
open) exit 2026-08-21T19:55Z (~USD 19.65, last valid session before the Sat Aug 22
PDUFA) -- fully closed before the binary prints. Expected profit ~4.0%, confidence
33/100 (thin, fragile edge). Hard stand-down gate: if CAPR has already run up >10-15%
vs the USD 18.8225 anchor by the entry check, skip the trade entirely. Strongest
dissent: bear's crowding argument that the drift itself may already be priced in,
making the Aug 21 exit vulnerable to the same de-risking slide the trade is trying to
avoid. Full debate in `transcript.md`.
