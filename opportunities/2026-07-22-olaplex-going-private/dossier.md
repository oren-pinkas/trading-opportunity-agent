---
id: 2026-07-22-olaplex-going-private
title: Olaplex going-private merger vote pending
status: researched
created: '2026-07-22T14:43:29Z'
event:
  type: regulatory
  summary: Olaplex Holdings filed DEFM14C for a going-private merger; shareholder
    consent/closing timeline is a near-term catalyst for OLPX.
  impact_window: '2026-09-15'
tickers:
- OLPX
sources:
- title: OLAPLEX HOLDINGS, INC. - Form DEFM14C - FY2026
  url: https://www.sec.gov/Archives/edgar/data/0001868726/000119312526202411/d544500ddefm14c.htm
  accessed_at: '2026-07-22T14:43:29Z'
hypothesis:
  statement: >-
    OLPX is in a going-private merger (DEFM14C filed 2026-07-22, expected close
    ~2026-09-15). Shareholder-vote risk is already retired via majority written
    consent, so the residual break distribution is dominated by regulatory,
    financing, MAC-repricing, litigation, and controlling-holder governance
    risk. The directional thesis (spread likely closes at original terms) is
    probably correct in reality, but is NOT actionable here - the deal-price
    consideration figure is missing and the OLPX price feed returns HTTP 400
    on the relevant dates, so no real entry/exit spread can be computed or
    simulated.
  direction: no-trade
  confidence: 82
plan:
  ticker: OLPX
  action: stand_aside
  position_size: 0
  entry: null
  exit: null
  expected_profit_pct: null
  blocking_conditions:
  - unpriceable feed - "toa price OLPX --provider twelvedata" returns HTTP 400
    on 2026-07-22 and 2026-07-23 while AAPL prices fine same dates; no usable
    price series means simulate-plans has nothing to diff.
  - missing deal price - per-share merger consideration not available from the
    dossier/filing read; without it spread, EV, and break-downside are
    unquantifiable. Illustrative EV with an unconfirmed 2 percent spread came
    out negative (-0.7 percent gross) even before this gap.
  reopen_criteria:
  - working OLPX price feed (HTTP 400 resolved, verified sane)
  - confirmed per-share deal price from the DEFM14C
  - observable market spread to deal price at a real timestamp
  - merger-agreement financing-out/reverse-termination-fee and HSR/regulatory
    clearance status read
  - EV recomputed with real spread and real downside, requiring positive EV
    net of costs
research:
  last_updated: '2026-07-23T21:30:06Z'
  strategy: three-round-panel
  personas:
    bull: sonnet
    bear: sonnet
    quant: opus
  synthesizer: opus
  dissent: >-
    Whether the OLPX HTTP 400 pricing failure is an incidental data-plumbing
    gap (bull/quant view - blocks execution only, doesn't change thesis
    confidence) or a material adverse signal about the instrument itself
    (bear view - AAPL prices fine same dates, so the failure may reflect
    thinning float, delisting-in-progress, or impaired live quoting, which
    should lower thesis confidence too). No diagnostic was run to resolve
    which reading is correct. Secondary: whether quant's P(break-or-reprice)
    bump to 0.15 adequately prices Olaplex's guidance-cut history as a MAC
    vector, or whether bear's fatter reprice tail is warranted.
  transcript: opportunities/2026-07-22-olaplex-going-private/transcript.md
---

## Scouted 2026-07-22T14:43:29Z

## Researched 2026-07-23T21:30:06Z

Three-round panel debate (bull/bear/quant) converged on **no-trade / stand-aside**. The
DEFM14C filing retires shareholder-vote risk (majority written consent already secured),
giving a high thesis confidence (~82/100) that the deal closes near original terms by
2026-09-15. However, two independent blockers make this non-actionable in this system:
(1) OLPX is currently unpriceable via the house real-data provider (`toa price OLPX
--provider twelvedata` returns HTTP 400 while AAPL prices fine same dates), and (2) the
actual per-share deal consideration was not available, so no real spread/EV could be
computed - an illustrative EV using an unconfirmed 2% spread came out negative (-0.7%
gross). See full transcript for the round-by-round debate and reopen criteria.
