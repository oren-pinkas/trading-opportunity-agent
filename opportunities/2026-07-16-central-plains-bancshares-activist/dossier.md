---
id: 2026-07-16-central-plains-bancshares-activist
title: Stilwell presses Central Plains Bancshares over buybacks
status: researched
created: '2026-07-16T10:24:00Z'
event:
  type: regulatory
  summary: Stilwell Activist Investments disclosed a ~9.73pct stake in Central Plains
    Bancshares and sent a letter criticizing weak share repurchase activity despite
    trading below book value
  impact_window: '2026-09-01'
tickers:
- CPBI
sources:
- title: Central Plains Bancshares, Inc. - Form DFAN14A
  url: https://www.sec.gov/Archives/edgar/data/0001979332/000092189526001807/dfan14a10318031_07142026.htm
  accessed_at: '2026-07-16T10:24:00Z'
hypothesis:
  statement: >-
    Stilwell's 9.73pct stake and public DFAN14A letter demanding buybacks
    against a below-book valuation is a directionally plausible re-rating
    thesis on a 3-6 month horizon, but has no dated forcing mechanism inside
    the scoped 6-week impact window (2026-09-01). CPBI is a sub-USD 300
    million microcap thrift trading at USD 20.48 (twelvedata, 2026-07-21T19:45Z)
    with mostly-empty 1-minute bars, confirming thin liquidity and wide
    spreads. The quant's EV math (gross plus 0.98 to plus 1.49 percent,
    depending on floor assumptions) is erased by realistic round-trip
    execution cost of roughly 2 percent, and even optimistic limit-order
    execution only reaches a razor-thin plus 0.19 percent net EV that does
    not survive a single bad exit print in a name this illiquid. The initial
    disclosure pop (2026-07-16) is five trading days old by the quant's
    reference price and is likely already reflected in the quote. No
    position clears the bar within this window.
  direction: none
  confidence: 72
plan:
  ticker: CPBI
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: -1.0
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
    Whether the positive-catalyst probability is correctly about 18 percent
    (quant's generic small-cap activism base rate) or materially higher at
    roughly 25 to 28 percent (bull's claim it should be conditioned on
    Stilwell's specific campaign history at prior thrift targets). This
    single input is the pivot: at 18 percent net EV is negative; near 25 to
    28 percent net EV flips positive even after costs. It stayed unresolved
    because nobody pulled the two pieces of evidence that would settle it -
    an actual pre/post price series to test the contested "already priced
    in" assumption, and a Stilwell-specific 6-week catalyst conversion rate.
    Both quant and bull stated they would flip to a small long given a
    documented pre-catalyst price dislocation or a dated forcing event
    inside the window; neither exists today.
  last_updated: '2026-07-22T08:59:54Z'
---

## Scouted 2026-07-16T10:24:00Z

## Researched 2026-07-22T08:59:54Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Bear
(fundamental/timing case: no forcing mechanism inside the 6-week window,
Stilwell's 30-50pct quarter-plus discount-closure base rate exceeds the
scoped horizon) and quant (execution-cost case: gross EV of plus 0.98 to
plus 1.49 percent erased by a roughly 2 percent round-trip cost on an
illiquid microcap that doesn't print every minute) converged independently
on PASS by Round 2, via two different methodologies. The bull moved from a
full-conviction long to a much smaller, conditional starter position and
conceded the timing/forcing-mechanism gap. See `transcript.md` for the full
debate with citations. Operational flag: 2026-09-01 is a US exchange
holiday (Labor Day) - any future exit would need to roll to 2026-09-02.
