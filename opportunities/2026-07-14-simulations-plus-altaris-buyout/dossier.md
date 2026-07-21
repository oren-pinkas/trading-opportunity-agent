---
id: 2026-07-14-simulations-plus-altaris-buyout
title: Simulations Plus shareholder vote pending on Altaris buyout
status: researched
created: '2026-07-14T04:02:05Z'
event:
  type: regulatory
  summary: SLP shareholders must approve the USD 375 million, USD 18.50/share all-cash
    Altaris acquisition; deal expected to close Q4 2026.
  impact_window: '2026-12-31'
tickers:
- SLP
sources:
- title: Simulations Plus to Be Acquired by Altaris For Approximately $375 Million
  url: https://www.businesswire.com/news/home/20260616126655/en/Simulations-Plus-to-Be-Acquired-by-Altaris-For-Approximately-$375-Million
  accessed_at: '2026-07-14T04:02:05Z'
hypothesis:
  statement: SLP trades at USD 18.225 versus the USD 18.50 all-cash Altaris offer
    (spot 2026-07-20 session, twelvedata), a gross spread of roughly plus 1.51
    percent, annualizing to about plus 4.7 percent gross into a Q4 2026 close
    — barely above the risk-free rate before costs. At an assumed 94 percent
    completion probability and an estimated break price near USD 14.00 (about
    minus 23 percent), net expected value after roughly 15bps round-trip costs
    is approximately minus 0.12 percent, breakeven to slightly negative. Topping-bid
    optionality (healthcare-focused sponsor, capital-light software target,
    low antitrust friction) is real but unconfirmed — go-shop window status
    and termination fee were never sourced — and even the optimistic case (10
    percent topping probability) only pushes annualized excess return to about
    1.7 percent, still trailing T-bills. No positive-expectancy edge in the
    spread, the topping-bid lottery, or a naked short.
  direction: none
  confidence: 78
plan:
  ticker: SLP
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: null
  note: Zero excess carry paid to wait against a fat left tail (roughly minus
    23 to minus 30 percent on deal break) and an unconfirmed topping-bid catalyst.
    The dossier's 2026-12-31 impact window is a corporate-calendar reference
    point, not an execution timestamp, so no valid-session entry or exit is
    defined since there is no trade to place. Revisit only if SLP trades at or
    below approximately USD 17.80 (spread widens past about 3.9 percent, annualized
    above about 12 percent), or an 8-K/proxy confirms an active go-shop with a
    sub-3 percent termination fee, or evidence emerges of Altaris financing
    trouble, a contested vote, or an antitrust second request — either would
    warrant a fresh debate.
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
  dissent: The sharpest unresolved disagreement is the weight of topping-bid
    optionality, which hinges on a fact the panel never obtained — go-shop
    window status and termination-fee size. Bull argues the healthcare-focused
    sponsor and capital-light, low-antitrust-friction target make a competing
    bid materially more likely than a generic deal, potentially worth several
    dollars of upside. Bear and quant counter that without deal-protection
    confirmation, any topping probability large enough to matter is unsupported
    speculation, and opportunity cost against T-bills kills even the optimistic
    case. All three converged on no_trade for structurally different reasons —
    quant on excess-EV/opportunity cost, bear on asymmetric break risk, bull
    reluctantly on missing information rather than absent opportunity. If a
    subsequent filing reveals an active go-shop with a low break fee, bull's
    thesis reactivates and the consensus fractures — the primary post-mortem
    watch item.
  lessons_applied:
  - Sourced a real, dated spot price (twelvedata, SLP USD 18.225, 2026-07-20
    session) rather than trading on the announcement-date deal terms alone,
    resolving round-1's price-blind bull case into a determinate spread
    calculation.
  - Treated the dossier's 2026-12-31 impact window as a corporate-calendar
    checkpoint, not an execution timestamp; no entry/exit timestamps were set
    since the verdict is no_trade.
  last_updated: '2026-07-21T10:46:00Z'
---

## Scouted 2026-07-14T04:02:05Z

## Researched 2026-07-21T10:46:00Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 78/100
confidence. Bull opened long (55/100) on a topping-bid-optionality thesis but
had no live price (API rate-limited); after bear and quant sourced spot
(USD 18.225 vs USD 18.50 deal, 2026-07-20), bull conceded the static-spread
case and fell back to 30/100. Bear held near-flat (20 to 15/100 long spread),
flagging a roughly 1:15 risk/reward if the deal breaks (downside to USD 12-14).
Quant's EV model showed gross spread capture at breakeven-to-negative after
costs (94 percent completion assumption, USD 14.00 break price), rising only
to 25/100 after crediting a modest topping-bid tail that still trails T-bill
yield on an annualized basis. Full transcript: `transcript.md`.
