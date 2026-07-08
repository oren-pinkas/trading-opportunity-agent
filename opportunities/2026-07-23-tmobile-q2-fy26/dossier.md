---
id: 2026-07-23-tmobile-q2-fy26
title: T-Mobile Q2 FY26 earnings
status: researched
created: '2026-07-07T22:42:46Z'
event:
  type: earnings
  summary: T-Mobile hosts Q2 2026 call July 23; postpaid net adds and fiber/broadband
    traction in focus.
  impact_window: '2026-07-23'
tickers:
- TMUS
sources:
- title: Businesswire TMUS earnings
  url: https://www.businesswire.com/news/home/20260625543544/en/T-Mobile-to-Host-Q2-2026-Earnings-Call-on-July-23-2026
  accessed_at: '2026-07-07T22:42:46Z'
hypothesis:
  statement: There is no executable positive-expected-value trade in TMUS around
    the Q2 FY26 print that clears the panel's risk bar as of today. The known July
    23 earnings date carries no differentiated edge (no cited options-implied move,
    no whisper delta, no historical TMUS post-earnings distribution, no guidance
    catalyst in the dossier). Every pre-print directional bet expressible in this
    equity-only simulator (a naked hold through the gap) carries an adverse-tail-to-edge
    ratio far worse than the panel's threshold and, after the bear-driven skew
    revision, a negative point EV. The only idea with a plausibly acceptable
    structure is a post-print intraday continuation trade, but its edge rests
    entirely on an unverified, memory-based continuation-rate assumption and cannot
    be committed to today.
  direction: none
  confidence: 80
plan:
  ticker: TMUS
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  rationale: Bull opened long via a call debit spread but conceded in Round 2 that
    (a) options are not executable in this equity-only, 1-minute-bar simulator, and
    (b) the equity-only fallback (naked hold through the print) fails the
    adverse-tail-to-edge bar the quant computed (~35-40x against a ~2% no-trade
    threshold). Bear and quant independently converged on NO-TRADE via different
    methods (priced-for-perfection/sell-the-news narrative vs. explicit EV math),
    and quant's confidence hardened from 72 to 78 after revising its directional
    skew from 55/45 positive to 48/52 negative on the bear's argument, flipping
    pre-print EV from +0.20% to -0.29%. Stand aside; the only surviving idea is a
    contingent, unverified post-print opening-range continuation trade to be
    re-evaluated cold on 2026-07-24 (see transcript) -- not a commitment today.
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
  dissent: 'The unresolved crux is whether a post-print opening-range continuation
    trade (structure B) has any real edge at all. Its entire case rests on the
    quant''s single unsourced assumption -- a 55% intraday continuation win rate --
    that nobody validated against TMUS''s actual historical post-earnings
    gap-and-continue vs. gap-and-fade distribution. If TMUS earnings gaps
    historically mean-revert intraday (plausible for a liquid, well-covered
    mega-cap where the gap is efficiently priced pre-market), structure B''s EV
    flips negative and it is just another no-trade with a trigger attached. Bull
    conceded this dependency explicitly; quant deferred it to post-print; neither
    resolved it. Secondary open question: the adverse-tail magnitude was pushed
    from -7/-8% to -8/-9% by the bear and adopted by the quant, also uncited --
    the no-trade direction is robust to this number, but confidence in the
    hardening partly rests on it. If TMUS prints a large, clean beat-and-hold move
    with no reversal, this is the thread a post-mortem should pull.'
  last_updated: '2026-07-08T15:04:17Z'
---

## Scouted 2026-07-07T22:42:46Z

## Researched 2026-07-08T15:04:17Z — NO-TRADE

Three-round panel (bull/bear/quant) converged on NO-TRADE. Bull opened long via a
call debit spread (285/300C) on T-Mobile's structural postpaid/FWA-fiber growth
story; bear opened NO-TRADE on priced-for-perfection grounds (postpaid leadership
is baseline expectation, not a surprise, and TMUS sits near highs with no
drawdown cushion); quant opened NO-TRADE on explicit EV math (~+0.20% net EV
under a soft 55/45 skew against a ~35-40x adverse-tail-to-edge ratio on a
possible -7/-8% guide-cut tail).

In Round 2, the quant flagged a mechanical dealbreaker neither other persona had
caught: this simulator fills only US-equity 1-minute bars (13:30Z-19:59Z) with no
options chain at all, so the bull's call debit spread is not executable. Bull
conceded fully, and further conceded that the equity-only fallback (a naked
pre-earnings hold through the print) does not clear the tail-to-edge bar either --
withdrawing any pre-print directional trade. Bull's only remaining idea was a
conditional post-print opening-range continuation trade (enter next session only
if the gap confirms >=2% and holds, hard stop at the opening-range extreme, exit
by 19:59Z same session), explicitly framed as unproven and contingent on base-rate
evidence nobody in the debate had produced. Bear, given the mechanical
confirmation, hardened its qualitative case, pushing the quant's directional skew
from 55/45 positive to 48/52 negative (shrinking room to surprise vs. undiminished
room to disappoint on a name that has already beaten for years) and the adverse
tail from -7/-8% to -8/-9%. Quant accepted both revisions, which flipped pre-print
EV from Round 1's marginal +0.20% to Round 2's -0.29%, and raised its own
confidence in NO-TRADE from 72 to 78.

Net verdict: NO-TRADE on any capital committed today. Confidence 80/100. The one
surviving idea -- a post-print intraday continuation/fade trade with a defined
opening-range trigger and stop -- is recorded as a documented contingency to be
evaluated cold on 2026-07-24, not a plan executed now; its ~+0.30% modeled EV rests
on an explicitly unsourced 55% continuation-rate assumption. Reconsideration
triggers before Jul 23: a cited options-implied move showing a materially smaller
expected move than the -8/-9% tail assumed here; a cited prior-quarter net-add or
estimate-revision trend confirming or denying the priced-for-perfection read; or a
pre-print selloff that repairs the risk/reward on a naked equity entry. Anchor
TMUS $279.85 @ 2026-07-08T15:04Z.
