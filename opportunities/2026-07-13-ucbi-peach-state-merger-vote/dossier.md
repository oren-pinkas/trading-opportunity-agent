---
id: 2026-07-13-ucbi-peach-state-merger-vote
title: United Community Banks / Peach State Bancshares merger election deadline
status: scheduled
created: '2026-07-13T03:25:44Z'
event:
  type: economic
  summary: Peach State shareholders face a July 20, 2026 deadline to elect merger
    consideration form ahead of an Aug 3 expected close with United Community Banks.
  impact_window: '2026-07-20'
tickers:
- UCBI
sources:
- title: United Community Banks and Peach State Bancshares Announce Election Deadline
  url: https://www.globenewswire.com/news-release/2026/07/10/3325540/34434/en/United-Community-Banks-Inc-and-Peach-State-Bancshares-Inc-Announce-Election-Deadline-for-Peach-State-Shareholders-to-Elect-Form-of-Merger-Consideration-and-Expected-Closing-Date.html
  accessed_at: '2026-07-13T03:25:44Z'
hypothesis:
  statement: "The July 20 shareholder consideration-election deadline and expected Aug 3 close are administrative deal-mechanics steps fixed at signing, not new information or a catalyst for acquirer UCBI. No merger-arb spread exists (no evidence Peach State is separately exchange-listed). Panel consensus is a HARD STRUCTURAL NO TRADE: quant's EV math is negative (~-0.16% of notional) even before accounting for direction, which is unsignable (a coin flip) since no persona identified a real directional lean. UCBI also closed 2026-07-14 at USD 35.61, near its 52-week high (USD 36.77), consistent with the deal being already priced in. The nominal long direction and near-zero size below reflect only a schema-forced formality, not conviction."
  direction: long
  confidence: 5
plan:
  ticker: UCBI
  action: buy
  entry:
    time: '2026-07-16T13:35:00Z'
    target_price: 35.61
  exit:
    time: '2026-08-03T20:00:00Z'
    target_price: 35.55
  expected_profit_pct: -0.16
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-16T05:30:00Z'
---

## Scouted 2026-07-13T03:25:44Z

## Researched 2026-07-16T05:30:00Z

Three-round panel debate (bull/bear/quant, synthesized by opus) converged
independently and then collaboratively on a HARD STRUCTURAL NO TRADE. All three
personas separately concluded the July 20 election-form deadline is pure
deal-mechanics plumbing fixed at signing, carrying no new information for acquirer
UCBI: bull found no tradeable target on the Peach State side (likely unlisted, no
classic arb spread), bear called it administrative noise with no precedent for
moving an acquirer's stock, and quant computed a negative EV (~-0.16% of notional)
from a ~2-4% base rate of a >2% event-driven move with unsignable (coin-flip)
direction. `toa price UCBI --provider twelvedata` returned HTTP 400 on every 1-minute
lookup tested (2026-07-14/15/16) — twelvedata's free tier does not carry 1-min
intraday bars for UCBI, though its daily-bar and quote endpoints do: UCBI closed
USD 35.61 on 2026-07-14 (source: https://api.twelvedata.com/quote?symbol=UCBI),
near its 52-week high of USD 36.77, reinforcing that the deal is already priced in.
The recorded buy/long, near-zero-confidence plan is a schema-forced formality (the
dossier contract requires a directional action even for a no-trade call) — see
transcript.md for the full debate and dissent. Bear's residual risk: Peach State's
listing status was never independently verified; if it turns out to be thinly but
technically exchange-listed, a target-side merger-arb spread could reopen and
warrant a revisit.
