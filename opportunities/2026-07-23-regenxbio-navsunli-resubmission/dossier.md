---
id: 2026-07-23-regenxbio-navsunli-resubmission
title: REGENXBIO aligns with FDA on NAVSUNLI Hunter syndrome BLA resubmission
status: researched
created: '2026-07-23T15:22:32Z'
event:
  type: regulatory
  summary: REGENXBIO to hold Type A FDA meeting July 2026 and resubmit NAVSUNLI BLA
    in Q3 2026 for accelerated approval after Feb 2026 CRL
  impact_window: '2026-09-30'
tickers:
- RGNX
sources:
- title: REGENXBIO Announces Alignment with FDA on Path Forward for NAVSUNLI BLA Resubmission
  url: https://www.prnewswire.com/news-releases/regenxbio-announces-alignment-with-fda-on-path-forward-for-navsunli-bla-resubmission-for-accelerated-approval-first-potential-gene-therapy-for-mps-ii-302806010.html
  accessed_at: '2026-07-23T15:22:32Z'
hypothesis:
  statement: >-
    The NAVSUNLI FDA-alignment / Q3 2026 BLA-resubmission announcement is a process
    update whose only in-window resolvable event (resubmission acceptance, roughly
    a plus 3 percent move) is too small and too offset by slip and dilution risk to
    produce a tradeable edge before the 2026-09-30 impact window. The event that
    actually carries the estimated 0.60 approval probability resolves around
    Q1 to Q2 2027, entirely outside the window. Tape confirms: RGNX opened 9.91 and
    closed 10.25 (plus 0.7 percent) on announcement day 2026-07-23, then round-tripped
    to close 9.735 (minus 5.0 percent) the next session, landing 4.4 percent below
    the 10.18 pre-news close. Both long and short carry negative net expected value
    after costs.
  direction: none
  confidence: 18
plan:
  ticker: RGNX
  action: no-trade
  entry:
    time: '2026-07-27T13:30:00Z'
    target_price: null
  exit:
    time: '2026-09-30T20:00:00Z'
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
  dissent: >-
    Whether the minus 5 percent session on 2026-07-24 is informative (bear: the
    market pricing dilution risk or an efficacy-driven, harder-to-cure CRL cause) or
    is unrelated biotech-sector beta plus profit-taking with zero NAVSUNLI-specific
    content (bull, never falsified since no sector-relative or XBI-beta data was
    pulled). Quant treated bear's reading as a genuine update and moved the
    probability of a slip or dilutive raise from 0.20 to 0.28, which is the single
    change that flipped the long expected value from marginally to clearly negative
    (minus 1.17 percent gross, minus 1.87 percent net). If the move was pure beta,
    that reweighting is overfit to noise and the true long EV sits closer to round
    one's minus 1.1 percent, still negative, so the no-trade verdict survives, but
    confidence would be overstated. Secondary open item: the underlying CRL cause
    (CMC/manufacturing versus efficacy/evidentiary) remains undisclosed; that single
    fact would swing the approval prior from roughly 0.40 to roughly 0.78, but
    resolves after this dossier's window regardless. Testable post-mortem: check
    whether REGENXBIO ever discloses the CRL deficiency category, and whether RGNX
    traded with or against XBI on 2026-07-24.
  last_updated: '2026-07-26T00:43:00Z'
---

## Scouted 2026-07-23T15:22:32Z

## Researched 2026-07-26T00:43:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), isolated to this
opportunity only. BULL opened long near the 9.95 announcement-time print, framing the
FDA alignment/Type A meeting/Q3 resubmission as a de-risking catalyst that collapses
"no path forward" tail risk for a first-in-class MPS II gene therapy. BEAR called it a
process update, not de-risking — "alignment on a path forward" post-CRL is the modal
outcome, not evidence of a clean review, and the 2026-09-30 impact_window is a
resubmission target, not an FDA decision date (the real decision likely lands
~Q1-Q2 2027). QUANT pulled the live tape via `toa price RGNX <ts> --provider
twelvedata` across eight verified timestamps: pre-news close 10.18 (07-22) -> +0.7%
to 10.25 on announcement day (07-23) -> round-tripped to -5.0%/9.735 the next session
(07-24), landing -4.4% below pre-news. QUANT's base rates put the real approval
catalyst entirely outside the dossier window, with only a ~2-3% mechanical
resubmission-acceptance leg resolvable in-window; Round 1 EV was already negative
(net ~-1.1%) with S/N ~0.12 (below the 0.15 durable-edge bar).

In Round 2, BULL conceded the "hold to 09-30" framing was wrong once the only
in-window leg was identified as mechanical, and withdrew its original exit plan.
BEAR's dilution/CRL-cause-tail argument was treated by QUANT as a genuine update
(not mere restatement): reweighting P(slip/raise) from 0.20 to 0.28 pushed net long
EV to ~-1.87% and net short EV to ~-1.43% (short also carries ~1.90% borrow cost and
squeeze risk on a small-cap biotech float) — S/N degraded to ~0.035, four times below
the lesson-#3 bar in both directions. All three personas independently converged on
FLAT by Round 2. Verdict: NO-TRADE. Distinguishing note for the post-mortem: this is
convergence via new analysis on verified live tape data (eight twelvedata price
points, one correctly-diagnosed non-trading Saturday), not agreement under a data
blackout on facts later retracted. Flips only on: disclosure that the CRL was
CMC-only (approval prior ~0.40 -> ~0.78), or RGNX reclaiming/holding above the 10.18
pre-news close on volume. Full debate with citations in `transcript.md`.
