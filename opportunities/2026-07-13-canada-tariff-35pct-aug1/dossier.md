---
id: 2026-07-13-canada-tariff-35pct-aug1
title: Trump threatens 35% tariff on Canada effective Aug 1
status: researched
created: '2026-07-13T03:25:44Z'
event:
  type: geopolitical
  summary: Trump threatened a 35% tariff on Canadian goods taking effect Aug 1, 2026,
    pressuring cross-border auto supply chains.
  impact_window: '2026-08-01'
tickers:
- GM
sources:
- title: Trump Tariff Tracker – July 2, 2026
  url: https://ourtake.bakerbotts.com/post/102n7tq/trump-tariff-tracker-july-2-2026
  accessed_at: '2026-07-13T03:25:44Z'
hypothesis:
  statement: 'The dossier''s ''35% Canada tariff, Aug 1'' catalyst is a recycled 2025
    headline whose teeth have been pulled: the IEEPA legal basis was struck down by
    SCOTUS (Feb 2026), auto-specific costs are governed by a separate, already-guided-in
    Section 232 regime, and the live 2026 story (USMCA joint-review / non-renewal)
    is a slow negotiation, not a binary Aug-1 cliff. The return distribution is thin
    and mildly left-skewed (modest grind-up base case ~+3% vs a legally-fragile ~-6%
    tail), with a probability-weighted expected move near flat (~+0.9%). No verified
    live GM price exists. There is no clean, positive-EV standing trade in either
    direction on the dossier as written.'
  direction: long
  confidence: 20
plan:
  ticker: GM
  action: no-trade
  entry:
    time: '2026-08-01T00:00:00Z'
    target_price: null
    trigger_condition: 'Data gate: require a verified, citable live GM price (toa
      price GM <ts> --provider twelvedata with a real bar) before any action. Trigger
      A (higher-EV): a genuinely fresh tariff headline drives a verified >=3-6% intraday
      GM drop with NO confirmed new statutory tariff filing -> small reactive LONG,
      size <=0.5% of book, time-stop 5-7 trading days (mean-reversion/relief fade).
      Trigger B: a confirmed filing establishes a NEW statutory hook reviving genuine
      enactment risk -> small defined-risk bearish put spread, size <=0.25-0.5% of
      book. Absent either trigger by ~Aug 1-5 2026, let the event pass with no position.'
  exit:
    time: '2026-08-07T00:00:00Z'
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
  dissent: 'Strongest unresolved disagreement: whether the tradeable dip will ever
    print. Bull retains a residual belief the headline-driven overreaction dynamic
    is real -- a fresh 35%-tariff headline can still spook the tape into a shortable-then-buyable
    3%+ air-pocket, and his entire contingent-long playbook depends on that dip existing.
    Bear counters with a ''boy who cried tariff'' thesis: markets already watched
    this exact headline resolve benignly via USMCA carve-out once, training under-reaction,
    so the dip Bull awaits may never materialize, making even the contingent long
    a phantom setup. Quant leans toward Bear on tradeability but concedes Bull''s
    mean-reversion framing enough to flip the point estimate mildly positive. Unfalsifiable
    until a fresh headline actually hits the tape -- the fork a post-mortem should
    judge. Also material: toa price GM <ts> without --provider twelvedata returns
    fake/uncitable stub data ($421.57); twelvedata had no bar for the queried timestamp.
    Any activation of the contingent plan is blocked until citable price data is available.'
  last_updated: '2026-07-13T13:59:02Z'
---

## Scouted 2026-07-13T03:25:44Z

## Researched 2026-07-13T13:59:02Z — NO-TRADE

Three-round bull/bear/quant debate on the recycled 'Trump 35% Canada tariff, Aug 1' headline and GM. All three personas independently converged that this is a rerun of the July 2025 threat: the IEEPA legal basis was struck down by SCOTUS on 2026-02-20, autos are governed by a separate, already-guided Section 232 tariff regime ($2.5-4B baked into GM's 2026 guidance), and the live 2026 catalyst is actually the slow-moving USMCA joint-review/non-renewal (declined 2026-07-01), not a binary Aug-1 cliff. Quant's probability-weighted expected GM move converged near flat/mildly positive (~+0.9%) after two rounds of revision, with a thin, legally-fragile left tail. Verdict: NO STANDING TRADE. The panel instead sets a trigger-based watchlist: (A) a verified >=3-6% headline-only selloff with no new legal filing -> small reactive long (relief fade, <=0.5% book, 5-7 day time-stop); (B) a confirmed new statutory tariff filing -> small defined-risk put spread (<=0.25-0.5% book). Both triggers require a citable live GM price first -- toa's default price command returned fake stub data throughout this debate and twelvedata had no bar for the target timestamp, so no side had a verified price. See transcript.md for full three-round detail and citations.
