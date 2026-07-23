---
id: 2026-07-22-fanuc-q1-fy27-earnings
title: 'Fanuc earnings Jul 31: factory-automation demand read-through for global capex'
status: researched
created: '2026-07-22T23:08:41Z'
event:
  type: earnings
  summary: Fanuc reports next earnings Jul 31, 2026, a bellwether for global manufacturing
    capex and robotics/CNC demand after a record FY2025
  impact_window: '2026-07-31'
tickers:
- FANUY
sources:
- title: 'Fanuc stock: earnings update and factory automation outlook'
  url: https://www.ad-hoc-news.de/boerse/news/ueberblick/fanuc-stock-jp3802300008-earnings-update-and-factory-automation-outlook/69393758
  accessed_at: '2026-07-22T23:08:41Z'
hypothesis:
  statement: "Fanuc's Jul 31 FY27 Q1 print is a genuine global-capex/robotics bellwether, but the FANUY ADR is untradeable for this event: net expected value is negative (~USD -3.35 per USD 100 notional) after OTC round-trip costs and JST reporting-lag adverse selection, and the fundamental edge is plausibly already priced in via the China-recovery rally. The bellwether logic is sound but unexecutable and unmeasurable, so there is no fundable edge."
  direction: none
  confidence: 80
plan:
  ticker: FANUY
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: null
  rationale: "The panel converged to NO TRADE on two independent grounds. First, negative expected value: quant's gross EV was already -0.6% pre-cost, and after ~2% OTC round-trip cost plus ~0.5-1.0% stale-fill slippage from the JST reporting lag, net EV is roughly -3.35%. Second, a structural execution blocker: the thin OTC ADR has no live quote to anchor entry and no options chain / IV to build a defined-risk wrapper, while Tokyo (TSE 6954) trades through the reaction before the ADR responds, forcing fills after the information is already in the price. A defined-risk options structure would only cap downside, not create positive edge, and even the directional thesis is likely discounted by the prior China-recovery move. Bull withdrew the long in Round 2, conceding tradability is fatal. No trade."
research:
  strategy: three-round-panel
  personas: [bull, bear, quant]
  dissent: "The panel fully converged -- bull withdrew the long, and bear and quant reached the same conclusion from two non-overlapping angles (negative net EV and structural unexecutability). The single most fragile assumption underlying the consensus is the cost/slippage stack itself: the ~-3.35% net EV rests on estimated OTC round-trip cost (~2%) and JST-lag slippage (~0.5-1.0%) that were never measured against a live quote or real spread. If FANUY actually traded with tighter spreads and a usable options chain existed, the execution blocker would soften and the call would hinge entirely on the unproven 'already priced in' claim -- which no participant substantiated with the print's surprise versus current price."
  last_updated: '2026-07-23T14:52:54Z'
---

## Scouted 2026-07-22T23:08:41Z

## Researched 2026-07-23T14:52:54Z

Three-round panel (bull/bear/quant) converged unanimously on NO TRADE. FANUY (US OTC
ADR of TSE-listed Fanuc/6954) has no live quote available from the market-data
provider (twelvedata HTTP 400) and no confirmed options chain, making entry/exit
unanchorable and unmeasurable. Net expected value after OTC round-trip costs and
JST-reporting-lag adverse selection is approximately negative 3.35%, even before
weighing that the capex-bellwether thesis is plausibly already priced in via the
recent China-recovery rally. See `transcript.md` for the full debate record and
citations.
