---
id: 2026-07-12-jersey-mikes-ipo
title: Jersey Mike's files S-1 for NYSE IPO
status: researched
created: '2026-07-12T06:44:59Z'
event:
  type: ipo
  summary: Jersey Mike's Subs filed S-1 for NYSE listing under ticker JMKE, seeking
    B+ valuation and B+ raise.
  impact_window: '2026-08-15'
tickers:
- JMKE
sources:
- title: Jersey Mike's files for IPO, plans NYSE listing under ticker JMKE - StreetInsider
  url: https://www.streetinsider.com/Equity+Offerings/Jersey+Mikes+files+for+IPO,+plans+NYSE+listing+under+ticker+JMKE/26725601.html
  accessed_at: '2026-07-12T06:44:59Z'
hypothesis:
  statement: JMKE is not yet a tradeable security (no confirmed price range, share
    count, or exchange listing date/time as of 2026-07-12). The debate concluded
    that the well-known IPO "pop" (comps CAVA +99%, Dutch Bros +70% offer-to-close)
    accrues to allocated investors, which a retail/systematic account cannot obtain
    on a hot Blackstone-led deal. The only fillable leg (buy the first liquid print
    at listing, exit day-1 close) is an open-to-close residual-momentum trade that
    both the Quant's EV model and the Bull's own arithmetic on his own comps (CAVA
    +4.2%, Sweetgreen -5.2% open-to-close) converge on as negative expected value
    after slippage. Any multi-day or post-lockup hold is worse once leverage ($2.1B
    long-term debt vs $232M cash), the Blackstone dividend-recap/cash-out structure,
    controlled-company overhang, and decelerating same-store sales (3.6% to 2.3%)
    are priced in. No action is warranted today; only a small, strictly gated
    conditional long survives the debate.
  direction: long
  confidence: 30
plan:
  ticker: JMKE
  action: buy
  entry:
    time: Unconfirmed - gated on all of (1) an amended S-1/424B setting a real price
      range and share count, (2) a confirmed NYSE listing date/time verified present
      in the price provider, (3) an observed liquid opening print on listing day
      showing a "hot-deal" pop signature (not a Smith-Douglas-style +12-15% print).
      Do NOT hard-code to the 2026-08-15 impact_window placeholder. If triggered,
      enter after the opening auction clears and a liquid bar forms - the offer-to-close
      pop is already gone by the time a retail account can fill, so entry is a
      discretionary momentum read, not a scheduled clock-based leg.
    target_price: TBD - no price range set in the S-1 as of 2026-07-12; do not estimate
  exit:
    time: Day-1 close only if a conditional position is ever taken (no multi-day
      hold - lockup/controlled-company overhang and post-IPO fade risk argue against
      extending past close).
    target_price: Hard intraday stop-loss at -3%; otherwise exit at day-1 close
      regardless of price.
  expected_profit_pct: 0
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-12T22:55:42Z'
---

## Scouted 2026-07-12T06:44:59Z

## Researched 2026-07-12T22:55:42Z

No trade today. JMKE has no confirmed listing date, price range, or share count as
of the S-1 filing (2026-07-02) - nothing is schedulable. The three-persona debate
(bull/bear/quant, three rounds) converged near-unanimously on holding at zero size:
the Bull conceded the IPO-price-to-open "pop" is captured entirely by allocated
investors and is inaccessible to a retail/systematic fill; the retail-accessible
open-to-close leg is negative EV per both the Quant's model (~-2.6% per unit risked)
and the Bull's own independently-derived comp arithmetic. Bear's leverage/dividend-
recap/decelerating-SSS case was conceded by the Bull and reinforces negative EV on
any hold longer than intraday. A small, strictly gated conditional long survives
(low single-digit % sizing, entered only after a confirmed listing + a "hot-deal"
opening signature, exited at day-1 close with a -3% stop), but is not endorsed as
an edge - see dissent below and full transcript in `transcript.md`.

**Dissent (gold for post-mortem):** the one live disagreement is whether a "hot-deal"
opening signature (large first print + deep bulge-bracket syndicate) raises the
retail-accessible open-to-close P(up) above the ~0.43 base rate enough to flip EV
positive (Bull's unproven hypothesis, n=2 comp sample), or whether a hot open is
itself the marker of maximum overpricing (Quant/Bear's view, with the only EV-flipping
path being a deal priced *below* the $10-12B target instead). This is falsifiable
only once JMKE actually lists.

**Revisit trigger:** amended S-1/424B with a real price range AND a confirmed NYSE
listing date/time verifiable in the price provider - re-run research once both exist.
