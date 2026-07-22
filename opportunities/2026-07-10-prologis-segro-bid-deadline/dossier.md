---
id: 2026-07-10-prologis-segro-bid-deadline
title: Prologis faces July 22 deadline on Segro takeover bid
status: analyzed
created: '2026-07-10T07:38:15Z'
event:
  type: regulatory
  summary: UK takeover rules require Prologis to announce a firm offer for Segro or
    walk away by 5pm London time July 22, 2026, after Segro's board rejected the ~GBP12.6B
    all-share proposal.
  impact_window: '2026-07-22'
tickers:
- PLD
sources:
- title: Prologis Pushes Segro For Talks On GBP12.6B Takeover Bid
  url: https://www.law360.com/articles/2498898/prologis-pushes-segro-for-talks-on-12-6b-takeover-bid
  accessed_at: '2026-07-10T07:38:15Z'
hypothesis:
  statement: PLD is the acquirer in a rejected, all-share bid facing a hard UK Takeover
    Panel PUSU deadline (5pm London, 2026-07-22). The acquirer-dilution discount is
    only partially in the price (-0.9% net on news day, not a full recovery -- the
    bull conceded its "V-shaped recovery" framing was overstated). Two bear structural
    points survived rebuttal unrefuted -- (1) a Rule 2.8 "no firm intention" walk-away
    imposes a ~6-month standstill and removes the catalyst premium rather than restoring
    the pre-news baseline, so walk-away is flat-to-slightly-positive at best, not
    a relief rally; (2) "pushing for talks" is procedurally required to avoid an automatic
    Rule 2.8 bar and carries no bullish information content. On the quant's revised
    scenario tree -- firm offer 25% (-3.0%, more dilutive post-rejection), extension
    20% (-0.5%, harder to get target consent post-rejection), walk-away 55% (+0.75%,
    standstill caps the re-rate) -- gross EV(long) = -0.44%, giving a short a thin
    but real net edge of ~+0.36% after ~8bps costs. Signal-to-noise is only ~0.12
    (edge small relative to ~4% dispersion), so this is a low-conviction, small-size
    tactical fade of the acquirer, not a high-conviction directional call.
  direction: short
  confidence: 57
plan:
  ticker: PLD
  action: short
  entry:
    time: '2026-07-13T14:00:00Z'
    target_price: 140.75
  exit:
    time: '2026-07-22T19:55:00Z'
    target_price: 140.15
  expected_profit_pct: 0.36
  note: Small tactical short, ~0.25x normal size (thin edge, high dispersion). Entry
    band $140.50-141.00. Hard exit/cover immediately on any resolution headline --
    a firm-offer announcement (favorable, take the gain) OR an extension announcement
    (catalyst deferred, stand down) -- do not hold residual exposure through unpredictable
    post-event drift. Hard stop above $143 (caps the walk-away/relief-rally adverse
    scenario, the 55%-probability path that goes against the short). This is a linear-EV
    fade only; it deliberately does not capture the bull's convexity thesis (short-dated
    OTM calls) -- see dissent.
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
  dissent: The strongest unresolved disagreement is the linear short vs. the bull's
    convex long-optionality structure -- genuinely different bets on the same event,
    never reconciled. The bear/quant case prices the linear expected value and lands
    on a small fade. The bull's surviving argument (after conceding the recovery narrative
    and the standstill economics) is that short-dated slightly-OTM PLD calls have
    a convex payoff the linear EV framework understates -- if a firm offer lands (25%,
    plausibly more aggressive/dilutive post-rejection), the adverse move for PLD could
    exceed the modeled -3.0%, and a long-option structure would monetize that tail
    asymmetrically while risking only premium on the 55% walk-away path. This hinges
    on an unpriced question -- is the firm-offer downside tail fatter than modeled
    (favoring long convexity), or is walk-away flat-to-negative rather than +0.75%
    (favoring the linear short)? Post-mortem should check the realized distribution
    -- if PLD gapped hard on a firm offer, the linear short under-captured the move
    a convex structure would have caught; if PLD drifted flat-to-up into a walk-away,
    both the short's thin edge and the bull's premium were the wrong bet.
  last_updated: '2026-07-12T12:53:24Z'
simulation:
  ran_at: '2026-07-22T22:30:04Z'
  fills:
  - leg: entry
    planned_price: 140.75
    actual_price: 142.36501
    source: https://api.twelvedata.com/time_series?symbol=PLD&interval=1min&date=2026-07-13&timezone=UTC
    fetched_at: 2026-07-13T14:00Z
  - leg: exit
    planned_price: 140.15
    actual_price: 144.23
    source: https://api.twelvedata.com/time_series?symbol=PLD&interval=1min&date=2026-07-22&timezone=UTC
    fetched_at: 2026-07-22T19:55Z
  realized_profit_pct: -1.31
  outcome: loss
  matched_hypothesis: 'no'
postmortem:
  ran_at: '2026-07-22T23:30:01Z'
  root_cause: wrong-assumption
  lessons:
  - A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge,
    and simulate-plans has no path-dependent stop-loss/invalidation enforcement --
    it only diffs the plan's fixed entry/exit prices, so a plan's stated hard stop
    or entry band is not actually enforced during simulation.
  - When the actual entry fill prints outside the planned entry band, treat that as
    an early falsification signal -- the market has already moved past the thesis
    before the position opened.
---

## Scouted 2026-07-10T07:38:15Z

## Researched 2026-07-12T12:53:24Z — SHORT (scheduled)

Three-round panel (bull/sonnet, bear/sonnet, quant/opus) independently researched, then
rebutted, then synthesized (opus). PLD is the acquirer in a ~GBP12.6B all-share bid for
Segro rejected by Segro's board, now on a UK Takeover Panel PUSU clock to 2026-07-22.
Bull opened long (V-shaped recovery, PUSU as forcing function) but retreated materially
in rebuttal after conceding the recovery read was overstated and the standstill economics
undercut the walk-away upside; bear held that the acquirer-dilution discount is only
partially priced and "pushing for talks" carries no bullish signal; quant's fully
recomputed scenario tree, after incorporating the bear's Rule 2.8 corrections, produced
a thin but positive net short edge (~+36bps after costs, signal-to-noise ~0.12).
Synthesizer sided with the bear+quant lean: small tactical short (~0.25x size), entry
2026-07-13, hard exit at the 2026-07-22 PUSU resolution. See transcript.md for full
rounds.

---
### Revision 2026-07-22T22:30:04Z
Simulated PLD short: -1.31% (loss, matched=no)

---
### Revision 2026-07-22T23:30:01Z
Post-mortem: wrong-assumption
