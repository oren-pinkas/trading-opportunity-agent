---
id: 2026-07-13-sk-hynix-samsung-memory-selloff
title: SK Hynix and Samsung Electronics drop over 10% in memory stock selloff
status: researched
created: '2026-07-13T16:16:37Z'
event:
  type: economic
  summary: SK Hynix and Samsung Electronics each fell more than 10%, dragging tech
    indexes lower, as investors reassess the memory/DRAM pricing cycle heading into
    upcoming earnings.
  impact_window: '2026-07-24'
tickers:
- HXSCF
sources:
- title: 'Market Update Into July 13th: Memory Stock Mayhem'
  url: https://trendspider.com/blog/market-update-into-july-13th-2026/
  accessed_at: '2026-07-13T16:16:37Z'
hypothesis:
  statement: 'The panel converges on no-trade because the opportunity is unexecutable
    and under-specified before it is even directionally wrong. The harness cannot
    price, mark, or fill either instrument -- both HXSCF and the new SKHY ADR return
    HTTP 404 on Twelve Data, the latter only days old and not yet in the provider
    universe -- so the only positive-EV path the harness could fill does not exist
    today. The earnings catalyst date is in three-way conflict across sources (dossier
    says 2026-07-24, one source set says 2026-07-22, another says 2026-07-29) and
    must be pinned to a primary source such as SK Hynix IR or an SEC filing before
    any entry, exit, or hold window can be trusted. The setup also sits behind a
    priced-for-perfection precedent -- Samsung sold off on 2026-07-07 despite a record
    profit -- meaning a mere beat of a still-extreme consensus bar (Street modeling
    600+ percent YoY profit growth) does not reliably produce a relief rally, while
    the SKHY line already drifted roughly 8 percent in a single session, well beyond
    anchor-drift tolerance, voiding any plan anchored to a research-day price.'
  direction: no-trade
  confidence: 88
plan:
  ticker: HXSCF
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  monitor_conditions:
  - SKHY becomes quotable and fillable by the price provider (Twelve Data no longer
    404s), giving a live cash-open anchor to re-derive targets against
  - True Q2 earnings date confirmed from a primary source (SK Hynix IR or an SEC
    filing), resolving the 2026-07-22 vs 2026-07-24 vs 2026-07-29 conflict
  - Clarity on whether the reported miss is against median consensus (roughly 82
    trillion won revenue, 63-66 trillion won operating profit) rather than only
    the most aggressive bull-case outlier
  - Evidence the drawdown is over 80 percent memory-name-specific rather than driven
    by broad macro risk-off (SanDisk, ARM, Intel, Nasdaq all down the same session)
    or mechanical ADR-rotation and index-inclusion flows
  - Fresh live quote re-anchored within 0.5-1 percent anchor-drift tolerance at the
    moment of any re-underwrite, with realistic thin-ADR slippage (roughly 100-300
    bps) still leaving positive net EV
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
  dissent: 'All three converged on no-trade, but their reasoning diverges on one
    unresolved point worth tracking for a future post-mortem. The bull persona held
    that the flagged miss is measured against the most aggressive bull-case estimate
    (600+ percent YoY profit growth), not the median consensus -- so if the median
    revenue and operating-profit bar is still met or beaten, the priced-for-perfection
    unwind could be refuted by the print itself and a genuine long (coiled-spring
    relief re-rating) may still exist once the instrument is fillable. The bear and
    quant personas treated this as already settled against the long, using Samsung''s
    2026-07-07 sell-off on a record profit as load-bearing proof that even a median
    beat will not generate a relief rally in a name this extended (SK Hynix up 341.9
    percent YTD). This gap -- whether a median beat is sufficient to rally the stock,
    or whether the market has moved to grading only against the marginal optimistic
    estimate -- is genuinely unresolvable before the print and before the instrument
    is priceable, and is the fork most likely to be judged wrong in hindsight. Secondary
    preserved tension: the bear persona also flagged that shorting is separately
    dangerous (still-bullish sell-side with above-spot targets), so the no-trade
    is a two-sided abstention rather than a disguised short.'
  last_updated: '2026-07-14T05:01:56Z'
---

## Scouted 2026-07-13T16:16:37Z

## Researched 2026-07-14T05:01:56Z -- NO-TRADE

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesizer opus). Round
1: bull read the selloff as a valuation air-pocket into a binary earnings catalyst,
proposing to switch the traded instrument from the dossier's HXSCF to the newly
listed Nasdaq ADR SKHY. Bear read it as a multi-week priced-for-perfection unwind
(SK Hynix +341.9% YTD, Samsung +197.7% YTD before the crashes), with the "miss"
catalyst measured against an extreme Street bar and a meaningful share of the move
being macro/mechanical rather than memory-specific. Quant independently ran `toa
price` against both HXSCF and SKHY and got HTTP 404 on both -- no fillable instrument
exists in the harness at all -- and separately flagged the dossier's 2026-07-24
impact window likely conflicts with the true earnings date. Round 2: bull fully
conceded the executability hard stop and softened the directional case after weighing
Bear's priced-for-perfection framing and the Samsung sell-the-news precedent; bear
and quant reinforced NO TRADE from independent angles, noting that a bull and a
bear who disagree on direction both hit the same liquidity wall unprompted. Round
3 synthesis: high-confidence (88/100) NO TRADE given unanimous convergence on both
the executability gate and the earnings-date conflict, with the deepest reasoning
disagreement (whether a median, not just bull-case, beat could still flip the setup
bullish once tradeable) preserved as dissent for a future post-mortem. Monitor-only
pending: SKHY becoming fillable, primary-source confirmation of the true earnings
date, clarity on median-vs-bull-case consensus risk, isolation of memory-specific
vs macro/mechanical drawdown, and a fresh live anchor with acceptable net EV after
realistic thin-ADR slippage.
