---
id: 2026-07-23-intel-q2-fy26
title: Intel Q2 FY26 earnings
status: researched
created: '2026-07-07T20:34:02Z'
event:
  type: earnings
  summary: INTC reports Q2 FY26 after close July 23; foundry losses, DCAI momentum
    and gross-margin trajectory in focus
  impact_window: '2026-07-23'
tickers:
- INTC
sources:
- title: Intel to Report Second-Quarter 2026 Financial Results
  url: https://www.intc.com/news-events/press-releases/detail/1774/intel-to-report-second-quarter-2026-financial-results
  accessed_at: '2026-07-07T20:34:02Z'
hypothesis:
  statement: INTC Q2 FY26 (2026-07-23 after close) is a well-worn sentiment-battleground
    earnings print with no fresh, sourced, non-consensus catalyst in the dossier.
    The turnaround narrative (DCAI recovery, foundry breakeven timeline, margin
    scoreboard, 18A/14A ramp) is already priced, and Intel's credibility deficit
    from a prior breakeven walkback argues if anything for negative skew. In an
    equity-only sim with no options, no structure clears both the 2% net-EV bar
    and the no-trade/un-hedgeable-tail filter -- hold-through-print is negative
    EV at the base 45/55 skew, post-earnings momentum (long or short) prices to
    ~0-0.03% net (noise below the actionable threshold), and a naked hold-through
    short, though it pencils positive at a narrative-derived 40/60 skew, is
    categorically blocked by the un-hedgeable binary-event tail. Stand aside.
  direction: none
  confidence: 70
plan:
  ticker: INTC
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  rationale: All three personas converged on NO-TRADE by Round 2, via different
    mechanisms -- bull conceded no edge survives losing the options instrument
    and having no sourced catalyst; bear found no specific pre-print signal
    (yield disclosure, customer pause, guidance pushout) to justify a short beyond
    generic caution; quant showed no equity-only structure clears the 2% net-EV
    bar while also passing the un-hedgeable-tail filter. Stand aside; revisit if
    a sourced, non-consensus catalyst surfaces before 2026-07-22 close.
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
  dissent: 'The sharpest unresolved tension is the quant''s rejected-but-positive-EV
    short. Applying the bear''s credibility-deficit argument to shift skew from
    45/55 to 40/60 with asymmetric magnitudes (disappointment ~12%, relief ~11%),
    a hold-through short pencils to ~+2.5% net EV -- above the 2% actionable bar.
    It was rejected on two grounds the panel never reconciled: (a) the 40/60 skew
    is narrative-derived and unsourced, not data-derived -- the entire positive
    point estimate rests on an assumption no one could source this quarter; and
    (b) a naked short through a binary earnings event carries an un-hedgeable,
    theoretically unbounded adverse tail (beat-and-raise squeeze gap), a lesson-1
    violation that in an options-less sim is a categorical block, not a size-down.
    If INTC delivers a merely not-worse-than-feared print and gaps up on relief,
    the stood-aside book leaves defined-risk money on the table; if it gaps down
    as the skew implies, the rejected short would have paid -- but the panel''s
    discipline is that a positive point estimate built on an unsourced skew behind
    an unbounded tail is not a tradable edge. Post-mortem thread: was the 40/60
    skew directionally right, and did the tail-risk filter correctly veto a trade
    that would have profited?'
  last_updated: '2026-07-08T14:44:33Z'
---

## Scouted 2026-07-07T20:34:02Z

## Researched 2026-07-08T14:44:33Z — NO-TRADE

Three-round panel (bull/bear/quant, synthesized on opus) converged on NO-TRADE.
Reference price: INTC $316.42 @ 2026-07-08T14:44Z (stub deterministic provider).

Bull's opening thesis (foundry-loss-narrowing re-rating on a confirming beat, via
a long call spread/straddle targeting $350-365) collapsed once the equity-only
sim constraint removed the options instrument entirely, and bull admitted no
sourced, non-consensus catalyst exists in the dossier -- only pattern-matching
on Intel's history of outsized earnings-day moves. Confidence fell 40 -> 20.

Bear held that the DCAI/foundry/margin narrative is already fully priced, that
Intel's guidance has been optimistic before (a prior foundry-breakeven timeline
walkback), and that AMD/Nvidia/TSMC competitive erosion is structural, not new
information -- but could not name a fresh, sourced pre-print signal (yield
disclosure, customer pause, guidance pushout) specific enough to justify an
active short rather than pure caution. Confidence in no-trade rose 70 -> 75.

Quant's EV math anchored the panel: hold-through-print at a base 45/55 skew is
-1.0% gross / ~-1.1% net (fails the no-trade filter outright, infinite adverse-
tail-to-edge ratio); the only equity-only structures that avoid gap exposure
(pre- or post-earnings momentum) price to ~0-0.03% net -- noise below the 2%
actionable threshold. Shifting skew to 40/60 per bear's credibility-deficit
argument makes a hold-through short pencil to ~+2.5% net EV, but quant explicitly
rejected trading it: the skew is narrative-derived, not sourced, and a naked
short through a binary earnings event has an unbounded, un-hedgeable adverse
tail (squeeze/beat-and-raise gap) -- a categorical block in an options-less sim,
not a size-down. Confidence in NO-TRADE rose 35 -> 62.

Synthesis: stand aside. No structure clears both the 2% net-EV bar and the
no-trade/tail-risk filter simultaneously. Confidence in NO-TRADE: 70/100.
Reconsideration trigger: a sourced, non-consensus catalyst (foundry customer
win/loss, capex signal, leaked guidance) surfacing before 2026-07-22 close.
