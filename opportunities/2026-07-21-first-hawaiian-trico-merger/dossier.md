---
id: 2026-07-21-first-hawaiian-trico-merger
title: First Hawaiian-TriCo Bancshares all-stock merger
status: researched
created: '2026-07-21T09:20:33Z'
event:
  type: regulatory
  summary: USD 2B all-stock bank merger announced July 13, pending shareholder and
    regulatory approval
  impact_window: '2026-09-30'
tickers:
- FHB
- TCBK
sources:
- title: Intellizence M&A tracker
  url: https://intellizence.com/insights/merger-and-acquisition/largest-merger-acquisition-deals/
  accessed_at: '2026-07-21T09:20:33Z'
hypothesis:
  statement: >-
    The FHB/TCBK all-stock merger (fixed ratio 2.095 FHB per TCBK) carries a real
    but thin merger-arb spread of ~1.37% (implied TCBK USD 60.81 vs actual USD
    59.98 at the 2.095 ratio on 7/21 prices). That spread has been essentially
    flat for 8 sessions, confirming deal-certainty is already priced with no
    repricing catalyst left before the dossier window. The Sep 30 date is a
    window-end, not a close date - Bank Holding Company Act / Bank Merger Act
    review of a USD 2B deal runs a median ~7 months, so the deal is only mid-review
    by then. On real inputs the position is negative EV (~-1.47% net) because the
    ~1.37% reward ceiling is dominated by the ~9% probability of a -15% break tail,
    and the ~2% annualized residual carry is roughly cash-negative after ~0.45%
    costs. This is efficient pricing of last-mile regulatory/vote risk, not
    harvestable mispricing.
  direction: no_trade
  confidence: 70
plan:
  decision: no_trade
  ticker: null
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  reopen_conditions:
  - Arb spread widens materially past ~3-4% on a regulatory scare offering real convergence
  - A firm shareholder-vote or regulatory-decision date is confirmed inside a tradeable window
  - Fed/OCC approval or a definitive close date is announced, collapsing timeline uncertainty
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
    Whether the ~1.37% residual spread is a harvestable inefficiency or fair
    compensation. The bull holds the deal is healthy and the spread is merely a
    "cost problem" - real convergence value that is simply too thin to trade at
    this size (would trade it if wider). The bear holds the identical 1.37% is
    EFFICIENT pricing of last-mile completion risk - compensation for the exact
    Fed/OCC and vote risk that is hardest to diligence, not mispricing at any size.
    Unresolvable because it turns on whether the ~9% break probability is correctly
    priced, which cannot be diligenced without a last-mile regulatory read that
    does not exist inside the window.
  last_updated: '2026-07-23T00:00:00Z'
---

## Scouted 2026-07-21T09:20:33Z

## Researched 2026-07-23 — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus) converged on
**NO-TRADE**, with all three seats ending in the low-conviction band (bull 25, bear
25, quant 16 of 100). The debate collapsed onto one number: the real merger-arb
spread is ~1.37% (implied TCBK USD 60.81 = 2.095 x FHB USD 29.025, vs actual TCBK
USD 59.98 on 7/21), not the bull's annualized "7-8%" (a one-time-event scaling
error) nor the quant's Round-1 illustrative 3% (unfetched, later retired). The bull
conceded its original thesis — "long TCBK targeting the Sep 30 resolution" — was
built on a false premise: Sep 30 is a dossier window-end, not a close date; a USD 2B
bank merger under the Bank Holding Company Act / Bank Merger Act clears in a median
~7 months, so the deal is only mid-review by the window and there is no convergence
event to harvest inside it. Rebuilt on real inputs, the quant's EV is ~-1.02% gross
/ -1.47% net (0.05 x +1.37% close + 0.86 x +0.30% pending + 0.09 x -15% break, minus
~0.45% costs) — worse than Round 1, because the reward ceiling shrank while the
-15% break tail held, worsening the risk/reward asymmetry. A spread flat for 8
sessions confirms deal-certainty is already priced; the residual ~2% annualized
carry is roughly cash-negative after costs. Verdict: NO-TRADE (not scheduled, not
simulated). Reopen only on a spread blowout past ~3-4% or a confirmed vote/regulatory
date inside a tradeable window. Full debate with citations in `transcript.md`.
