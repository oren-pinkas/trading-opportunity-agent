---
id: 2026-07-08-paramount-wbd-eu-merger
title: Paramount Skydance/WBD EU antitrust decision
status: researched
created: '2026-07-08T15:21:00Z'
event:
  type: regulatory
  summary: European Commission's Jul 7 deadline to rule on Paramount Skydance's $111B
    Warner Bros Discovery acquisition has passed; decision imminent after other jurisdictions
    cleared the deal.
  impact_window: '2026-07-10'
tickers:
- PSKY
- WBD
sources:
- title: Paramount-Warner Bros. Discovery Merger Faces EU Decision by July 7 - Bloomberg
  url: https://www.bloomberg.com/news/articles/2026-06-02/paramount-seeks-eu-green-light-for-110-billion-warner-deal
  accessed_at: '2026-07-08T15:21:00Z'
hypothesis:
  statement: A long-WBD merger-arbitrage tilt into an imminent EC ruling on the $111B
    Paramount Skydance/WBD deal is directionally the only defensible expression identified
    (approval remains the modal outcome, ~83% combined per quant's revised distribution),
    but the trade's EV cannot be signed without the actual deal consideration and
    live WBD arb spread -- the single load-bearing input, which no persona could observe
    and which quant explicitly flagged as invented in illustrative math. With that
    input unobserved and the EC deadline already 3 days stale (a genuine, bounded
    bearish signal), there is insufficient information to responsibly initiate now.
  direction: no-trade
  confidence: 72
plan:
  ticker: WBD
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
  notes: 'PSKY rejected as a thesis leg (acquirer reaction to expected clearance is
    empirically small and sign-ambiguous). Triggers to convert to an actionable plan,
    in priority order: (1) actual deal consideration + live WBD arb spread -- decisive;
    spread >=5% supports a small put-hedged long (<=1-2% of book) entered at/just
    before the clearance headline, exiting on the post-clearance pop; spread 2-5%
    supports a smaller tilt only if procedural posture is benign; spread <2% is a
    pass. (2) EU procedural posture confirmation -- Phase I-clean or confirmed administrative/stop-the-clock
    lag supports long; confirmed Phase II opening/Statement of Objections flips negative.
    (3) Whether other-jurisdiction clearances were conditional or unconditional --
    conditional clearances elsewhere raise EU remedy odds.'
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
  dissent: 'BEAR vs BULL on the meaning of the passed/stale EC deadline (QUANT mediates
    but does not resolve it). BEAR: the deadline slip is substantive Bayesian evidence
    of remedies negotiation, stop-the-clock, or a Phase II being teed up, proposing
    weights of ~35-40% clean/~40-45% remedies/~15-20% delay. BULL: the slip is likely
    routine administrative friction, common even in eventually-clean clearances, and
    sequential clearance by other jurisdictions is affirmative evidence against a
    smoking-gun overlap. QUANT split the difference with a bounded revision (88/9/3
    -> 83/12/5), granting the slip is real information but ''a nudge, not a regime
    change.'' Unresolved because it requires external facts no persona could access
    -- the actual EU procedural posture and the reason for the deadline miss -- the
    same class of missing data as the unresolved WBD/PSKY deal consideration and live
    arb spread that quant admitted inventing ($330 illustrative takeout) to make the
    EV math run. Post-mortem should score both: which deadline-slip interpretation
    reality vindicated, and what the true arb spread actually was versus quant''s
    placeholder.'
  last_updated: '2026-07-10T15:03:42Z'
---

## Scouted 2026-07-08T15:21:00Z

## Researched 2026-07-10T15:03:42Z — NO-TRADE

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) debated the EC's imminent ruling on Paramount Skydance's $111B WBD acquisition, three days past the EC's own July 7 deadline.

Bull: last-regulator-standing after peer clearances favors a clean-ish approval; proposed long WBD (primary) + long PSKY (smaller, higher-beta). Bear: the deadline slip itself is a bearish signal (remedies negotiation or Phase II being teed up), and any approval is likely already priced in -- recommended no trade. Quant: base rates favor approval (~88% combined initially), but the EV is dominated by an unobservable input -- the actual WBD deal consideration/arb spread -- which nobody in the debate could source; revised probabilities modestly toward bear's view after rebuttal (88/9/3 -> 83/12/5) but held that the trade's sign is undetermined without the real spread.

Synthesis: converged on structure (long-WBD-only is the sole defensible expression if traded at all; PSKY rejected as a thesis leg) and on modal direction (approval more likely than not) but not on actionability. No trade initiated -- the central EV input (arb spread) is unobserved and was admittedly invented by quant for illustration, and the stale deadline is itself an unresolved warning sign. See transcript.md for the full three-round debate with citations.
