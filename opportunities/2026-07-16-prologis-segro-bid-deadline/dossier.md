---
id: 2026-07-16-prologis-segro-bid-deadline
title: Prologis formal-offer deadline for Segro bid
status: researched
created: '2026-07-16T03:59:59Z'
event:
  type: regulatory
  summary: Prologis must make a formal offer for Segro by 2026-07-22 under UK takeover
    rules or walk away from its USD 16.9B bid
  impact_window: '2026-07-22'
tickers:
- PLD
sources:
- title: Yahoo Finance - Prologis Pushes for Talks on Segro Bid
  url: https://finance.yahoo.com/real-estate/articles/prologis-pushes-talks-16-9-113500480.html
  accessed_at: '2026-07-16T03:59:59Z'
hypothesis:
  statement: The Prologis-Segro USD 16.9B PUSU deadline is a Segro-side (target)
    catalyst, not a Prologis-side one. After correcting PLD's deal size down to
    roughly 12 percent of equity market cap and reweighting toward "extension as
    base case," the direction-agnostic long thesis on PLD collapses to essentially
    zero net expected value.
  direction: no-trade
  confidence: 78
plan:
  ticker: PLD
  action: none
  note: No position recommended - corrected net EV (roughly 0 to +5bps) sits an
    order of magnitude below the 50bps net-EV hurdle and is swamped by PLD's 1.5-2
    percent daily idiosyncratic volatility. Preferred vehicle for actual catalyst
    exposure, if any, is Segro (SGRO.L), not PLD.
  hypothetical_record_only:
    entry:
      time: '2026-07-22T14:00:00Z'
      target_price: 147.70
    exit:
      time: '2026-07-23T13:35:00Z'
      target_price: 148.60
    expected_profit_pct: 0.13
    size_cap_pct_of_book: 0.25
research:
  last_updated: '2026-07-22T13:57:00Z'
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  dissent: The strongest unresolved disagreement is the sign and magnitude of the
    walk-away scenario. Quant weighted it at 25 percent probability with a +0.85
    percent impact; bear argues even that is too generous given the asymmetry
    versus the formal-offer scenario, and would lean toward a de-minimis tactical
    short/fade into any formal-offer headline spike rather than a flat pass; bull
    still leans marginally long. All three converge on "no material long edge" but
    disagree on the sign of the residual tail.
  lessons_applied:
  - 'Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines)
    directly onto an execution timestamp - treat such dates as catalysts and derive
    the fill time from the nearest valid trading session.'
  - 'Before finalizing any plan, validate that every entry and exit timestamp falls
    within an open trading session for the specific instrument.'
---

## Scouted 2026-07-16T03:59:59Z

## Researched 2026-07-22T13:57:00Z

Three-round bull/bear/quant panel concluded **no-trade / pass** on PLD (confidence
78). Deal-size correction (USD 16.9B is roughly 12 percent of Prologis's actual
~USD 137B equity market cap, not the initially assumed 15-17 percent) plus
reweighting toward "PUSU extension is the base case, not the tail" collapsed net
expected value on a directional PLD trade to roughly zero, well below the 50bps
hurdle, and swamped by PLD's 1.5-2 percent daily idiosyncratic volatility.
Structurally this is a Segro (SGRO.L, the target) catalyst, not a Prologis
(acquirer) one. Full debate transcript: `transcript.md`.
