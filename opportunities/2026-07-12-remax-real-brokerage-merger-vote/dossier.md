---
id: 2026-07-12-remax-real-brokerage-merger-vote
title: RE/MAX and Real Brokerage shareholder votes on merger set for Aug 14
status: researched
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: RMAX and REAX holders vote Aug 14, 2026 on forming Real REMAX Group; RMAX
    holders can elect stock or $13.80 cash.
  impact_window: '2026-08-14'
tickers:
- RMAX
- REAX
sources:
- title: Real and RE/MAX to Combine into Real REMAX Group Inc. (StockTitan)
  url: https://www.stocktitan.net/sec-filings/RMAX/defm14a-re-max-holdings-inc-merger-proxy-statement-82f7e6b8ed81.html
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: The RMAX/REAX merger is a genuine, board-negotiated, single-bidder deal
    with high vote-passage odds, but it is NOT a tradeable merger-arb setup right
    now. The bull case rests on a measurable spread to the $13.80 cash election
    that (a) is contingent on unconfirmed cash-pool proration mechanics -- making
    the true deliverable a cash + REAX-linked-stock blend rather than a clean cash
    floor -- and (b) cannot be observed because the price feed available this
    session is broken/stubbed (returned impossible prints like RMAX $249-400+
    against a $13.80 cash election), not merely unchecked. The debate converged
    on P(deal completes) ~0.89 (+/- 0.05, down from an initial 0.96/0.93 estimate
    once the dual-key vote -- both RMAX and REAX shareholders must independently
    approve -- was properly modeled as a joint probability), with a breakeven
    spread of ~4% net of costs. The edge is unmeasurable, not merely thin.
  direction: no-trade
  confidence: 78
plan:
  ticker: RMAX
  action: no-trade
  entry:
    time: null
    condition: Do not enter this session. Gated on ALL of -- (1) a live two-sided
      RMAX quote from a validated feed (current toa price feed is confirmed
      broken, a hard blocker); (2) observed spread to consideration >= 4.0% to
      $13.80 if the cash pool is uncapped, or >= 3.5% to blended consideration
      (~$13.30-13.60 est.) if capped, sustained across >= 2 sessions and net of
      ~0.6% costs; (3) filed RIHI (RMAX controlling holder) and Poleg (REAX)
      voting/support agreements; (4) confirmed S-4 cash-pool cap/proration
      formula; (5) ISS and Glass Lewis FOR recommendations on BOTH the RMAX and
      REAX proxies with no organized opposition; (6) no adjournment/postponement
      filing and no pending appraisal-demand or injunction litigation.
  exit:
    time: '2026-08-17T13:30:00Z'
    condition: N/A while flat. If and only if all entry gates clear in a future
      session, base-case exit is the first valid trading session after
      vote-result disclosure. Aug 14, 2026 is a Friday (valid session) but
      disclosure is expected after Friday close per merger-vote precedent, so
      exit rolls forward to Monday 2026-08-17 13:30 UTC market open -- same-day
      Aug 14 exit is rejected as unrealistic.
  expected_profit_pct: 0.0
research:
  last_updated: '2026-07-13T08:15:26Z'
  strategy: three-round-panel
  dissent: The strongest unresolved disagreement is whether the -25% break
    scenario is symmetric-conservative or optimistic. Bull argued a failed
    first vote likely triggers re-solicitation with sweetened terms (shallower,
    less probable left tail) but had no data to support it. Bear argued RMAX's
    deteriorating standalone fundamentals (NAR commission-litigation overhang,
    leverage, shrinking agent count) mean a break reverts to below the pre-deal
    price, making -25% an understatement. Quant noted the whole thesis is
    negative-EV at any reasonable spread once P(complete) drops to 0.85, i.e.
    the trade is fragile to a +/-0.05 swing in an unresolvable probability.
    This question is only observable if the deal actually fails, so it is not
    resolved by verifying the pre-vote data gates.
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-13T08:15:26Z

Three-round debate panel (bull/bear/quant, synthesized by a neutral opus
synthesizer) converged on **no-trade**. Full transcript with citations in
`transcript.md`. Summary: this is a real, board-negotiated, single-bidder
merger with structurally high vote-passage odds, but the tradeable edge (a
spread to the $13.80 RMAX cash election) could not be measured this session
because (a) the price feed was confirmed broken/stubbed rather than merely
unchecked, and (b) the cash-election "floor" is likely capped/prorated,
meaning realized deliverable value is contingent on unconfirmed proration
mechanics and correlated to REAX's price at close, not a clean fixed value.
P(deal completes) was revised from an initial 0.93 to ~0.89 once the dual-key
vote (both RMAX and REAX shareholders must independently approve) was modeled
as a joint probability, pushing the breakeven spread from ~3% to ~4% net of
costs. No position taken; re-evaluate if a validated live quote and the S-4
proration/voting-agreement terms become available ahead of the Aug 14, 2026
vote.
