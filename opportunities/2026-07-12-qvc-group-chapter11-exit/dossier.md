---
id: 2026-07-12-qvc-group-chapter11-exit
title: QVC Group targets Chapter 11 exit by late July
status: researched
created: '2026-07-12T18:06:04Z'
event:
  type: regulatory
  summary: QVC Group's prepackaged Chapter 11 restructuring, cutting funded debt from
    ~$6.6B to $1.3B, is targeted to conclude by around July 2026 following confirmation
    hearings.
  impact_window: '2026-07-25'
tickers:
- QVCGA
sources:
- title: 'QVC Group: $5B+ Debt Cut, Preferred Equity Asset Dispute'
  url: https://elevenflo.com/blog/qvc-group-chapter-11-bankruptcy
  accessed_at: '2026-07-12T18:06:04Z'
hypothesis:
  statement: >-
    No executable trade. QVCGA was delisted/suspended from Nasdaq effective
    April 24, 2026 and has had no open trading session since; the real
    post-suspension OTC successor is QVCAQ (~$0.06 as of 1 July 2026),
    roughly 2000x below the tool's fabricated $126.40 stub price, and the
    harness's real data feed returns HTTP 400 for QVCGA and has no fillable
    bars for QVCAQ, so neither candidate real price can be executed against
    in this system. Independent of execution, the fundamental case is
    unresolved - the Second Amended Plan (2 June 2026) restored a "pro rata
    share of QVCG Equity Consideration" to Class A6 preferred and A7 common
    after originally zeroing both, but no confirmation order had been
    entered as of 9 June 2026, no dollar figure for that consideration is
    disclosed, and Class A6 preferred sits senior to A7 common, so if the
    disputed ~$160M is preserved via the $400M intercompany-claim fight, the
    preferred's liquidation preference likely absorbs most/all of it before
    common sees anything. This is a data-artifact "opportunity" layered on
    top of a still-contested, possibly-zero-recovery bankruptcy claim, not a
    tradeable event.
  direction: none
  confidence: 88
plan:
  ticker: QVCAQ
  action: no_action
  entry: null
  exit: null
  expected_profit_pct: 0
  note: >-
    PASS/VOID. QVCGA has had no open trading session since its April 24,
    2026 Nasdaq suspension, and the harness cannot fill either candidate
    real price (QVCGA feed errors; no QVCAQ bars), so the trade is
    unexecutable regardless of view. Re-open only if all of the following
    hold - a timestamped executed trade print on QVCAQ post-suspension
    becomes fillable in this harness; a disclosed numeric
    equity-consideration figure is filed; the $400M intercompany-claim
    dispute resolves in favor of preserving value at QVCG; and it is
    clarified that A7 common recovers value after A6 preferred's
    liquidation preference is satisfied.
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
    In the bull's own "win" scenario (the ~$160M disputed value is
    preserved at QVCG rather than stripped via the $400M intercompany
    settlement), does Class A7 common actually recover anything, or does
    Class A6 preferred's senior liquidation preference consume the entire
    preserved amount first, leaving common at ~$0 even when the equity
    thesis "works"? Raised only in Round 2 by the quant and never rebutted;
    every earlier bull/bear argument implicitly treated "equity
    consideration preserved" as equivalent to "common recovers," and the
    debate closed without resolving the priority-stack math.
  lessons_applied:
  - 2026-07-08-caesars-icahn-fertitta-bidding-war
  last_updated: '2026-07-13T07:48:57Z'
---

## Scouted 2026-07-12T18:06:04Z

## Researched 2026-07-13T07:48:57Z

Three-round panel debate (bull/bear/quant) concluded **no_action (PASS/VOID)**
at 88/100 confidence. All three personas independently flagged in Round 1 that
QVCGA was delisted/suspended from Nasdaq effective 24 April 2026 and that the
dossier/tool's $126.40 reference price is a fabricated stub, wildly disconnected
from any real quote. Bull and bear each independently sourced conflicting
real-world prices for the post-suspension name ($0.06 OTC successor QVCAQ vs.
$3-$7.36 stale QVCGA prints); the quant resolved this in Round 2 by confirming
QVCAQ as the correct live ticker and, separately, confirming via the actual
data feed that neither QVCGA nor QVCAQ has a fillable real price in this
harness. Bull conceded in Round 2 that its original "enter now" long was
unexecutable and retreated to watch-only; bear held PASS throughout; quant
upgraded from "confident -97% EV" to "EV indeterminate, PASS on
execution/integrity grounds." All three converged on PASS via two separable
failure modes - execution impossibility and an unresolved A6-preferred-over-
A7-common liquidation-preference question that could zero out common even in
the bull's best case. Full transcript: `transcript.md`.
