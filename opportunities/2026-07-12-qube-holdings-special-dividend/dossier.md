---
id: 2026-07-12-qube-holdings-special-dividend
title: Qube Holdings pays special dividend
status: researched
created: '2026-07-12T11:57:54Z'
event:
  type: economic
  summary: Qube Holdings declared a special dividend of AUD 0.3465/share, ex-date
    July 13, payable July 23, 2026.
  impact_window: '2026-07-23'
tickers:
- QUB
sources:
- title: Qube Holdings Declares Special Dividend for July 2026 - TipRanks.com
  url: https://www.tipranks.com/news/company-announcements/qube-holdings-declares-special-dividend-for-july-2026
  accessed_at: '2026-07-12T11:57:54Z'
hypothesis:
  statement: There is no executable trade. QUB was suspended from ASX
    quotation on 8 July 2026 (five days before the dossier's stated 13 July
    ex-date) pending implementation of an $11.7bn scheme-of-arrangement
    takeover by Rubik Australia Pty Ltd (Macquarie Asset Management-led
    consortium with UniSuper and Pontegadea), with scheme implementation
    (~A$5.20/share cash) slated for ~14 August 2026. No market exists to
    fill either the cum-div buy (window already closed before today's open)
    or an ex-date position; the special dividend is fully-priced,
    court-approved deal mechanics carved from the scheme consideration for
    tax-efficient franking pass-through, disclosed since February 2026 -
    there is no unpriced edge. Reference stub prices (~400.94, ~92.87) are
    fabricated/garbage versus the real last print (A$5.12, 8 July close).
    This is a data-artifact "opportunity," not a tradeable event.
  direction: none
  confidence: 97
plan:
  ticker: QUB
  action: no_action
  entry: null
  exit: null
  expected_profit_pct: 0
  note: PASS/VOID. The security is suspended from ASX trading - no order
    book to execute against, and the only fillable leg (buy cum-div) needed
    entry before today's open, which is already closed. Even bracketing the
    suspension, the dividend is disclosed, court-approved deal consideration
    with no mispricing to be long of. Re-open only if the suspension is
    lifted, a live cross-checked quote becomes available, and a genuine
    cum-div entry window still exists before the true ex-date.
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
  dissent: Primary - process/data-quality defect upstream, not a
    trade-direction disagreement. The dossier was sourced with an ex-date
    (13 July) that was already impossible when generated, since the stock
    had been suspended five days earlier (8 July), and it carried
    fabricated reference prices (~25-100x off the real A$5.12). The debate
    caught this but the scout/ingestion step did not; the post-mortem
    should ask whether scout-time validation (live-quote check, price
    magnitude sanity check) could filter corporate-action-terminal names
    (suspensions, completed schemes, delistings) before they consume a
    full three-round debate. Secondary - whether flat PASS was the right
    system output versus an "informational/no-fresh-entry" tag for a
    hold-through thesis; bull argued this distinction, bear/quant correctly
    noted no pre-suspension inventory exists and the system's output space
    is enter/don't-enter, so flat PASS stands, but a system that also
    manages existing positions would need a "monitor/hold" state this run
    lacked.
  lessons_applied:
  - 2026-07-01-ism-mfg
  - 2026-07-02-june-jobs
  last_updated: '2026-07-13T07:38:59Z'
---

## Scouted 2026-07-12T11:57:54Z

## Researched 2026-07-13T07:38:59Z

Three-round panel debate (bull/bear/quant) concluded **no_action (PASS/VOID)**
at 97/100 confidence. Bull's independent research (Round 1) surfaced the
decisive fact none of the personas started with in the dossier: QUB was
suspended from ASX quotation at close of trading on 8 July 2026 - five days
before the dossier's stated 13 July ex-date - pending implementation of an
$11.7bn scheme-of-arrangement takeover (Rubik Australia Pty Ltd, a Macquarie
Asset Management-led consortium), last printing A$5.120. Bear independently
found the same facts and called it fatal/disqualifying from Round 1. Quant
found the reference price data fabricated (stub prices 25-100x off the real
last print) and the EV negative even before learning of the suspension, then
in Round 2 upgraded the verdict from "negative EV" to "EV undefined - no
market exists to fill against." Bull conceded in Round 2 that a "hold-through"
framing requires pre-suspension inventory the paper book does not hold, and
retracted its proposed entry as a modeling fiction rather than an executable
fill. All three personas converged on PASS/VOID via independent,
non-overlapping kill criteria (execution impossibility, undefined EV, and
conceded lack of standing inventory) - full transcript: `transcript.md`.
