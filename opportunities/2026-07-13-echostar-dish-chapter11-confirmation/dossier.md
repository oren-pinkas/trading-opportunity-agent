---
id: 2026-07-13-echostar-dish-chapter11-confirmation
title: EchoStar's DISH DBS prepackaged Chapter 11 confirmation hearing set for Aug
  17
status: researched
created: '2026-07-13T14:08:35Z'
event:
  type: regulatory
  summary: DISH DBS filed prepackaged Chapter 11 after AT&T spectrum sale delay; combined
    confirmation/sale hearing set for Aug 17, 2026, resolving note maturities and
    wireless business transition.
  impact_window: '2026-08-17'
tickers:
- SATS
sources:
- title: EchoStar's Dish files Chapter 11 after spectrum sale to AT&T is delayed -
    Yahoo Finance
  url: https://finance.yahoo.com/markets/stocks/articles/echostars-dish-files-chapter-11-143224999.html
  accessed_at: '2026-07-13T14:08:35Z'
hypothesis:
  statement: The Aug 17, 2026 combined confirmation/sale hearing for DISH DBS's prepackaged
    Chapter 11 is a de-risking event for DBS creditors, but no plan-of-reorganization
    language has been cited establishing that value flows to EchoStar (SATS) common
    equity. The 88%+ pre-filing support and hard court calendar are evidence about
    the DBS creditor outcome, not the SATS equity outcome. With the parent-equity
    transmission mechanism unconfirmed, the terms already negotiated pre-filing,
    and dilution risk unquantified, the trade has negative expected value and no
    defensible directional edge.
  direction: no_trade
  confidence: 78
plan:
  direction: no_trade
  position: none
  size: 0
  rationale: Bear and quant personas converged independently on NO TRADE for the
    same root reason — the unconfirmed DISH-DBS-subsidiary-to-EchoStar-parent equity
    transmission mechanism. Quant's revised net EV is ~-1.5% after costs. Bull did
    not refute the core objection; bull's Round 2 revision (cut size, add precondition
    to pull the plan of reorganization first) is itself a restatement of the bear/quant
    objection. No compromise half-position is warranted.
  reopen_conditions:
    document_to_pull: The actual DISH DBS plan of reorganization, disclosure statement,
      and any plan supplement filed on the docket.
    conditions_all_required:
    - Plan language explicitly preserves or provides recovery to EchoStar/SATS common
      equity.
    - AT&T ~$23B spectrum-sale proceeds are contractually earmarked to benefit parent
      shareholders rather than being absorbed by creditor claims first.
    - SATS is named as a distribution vehicle, or the transmission path to parent
      equity is otherwise documented.
    - A market-implied signal (e.g. SATS/DBS debt-basis divergence) suggesting the
      market already prices a linkage.
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: Bull maintains "expected" does not equal "fully priced in" 34 days ahead
    of a hard court-calendared catalyst, and that quant's 3% derailment tail is too
    high given 88%+ pre-filing support — implying a residual resolution-pop edge
    if the parent-equity mechanism is confirmed. The unresolved crux across all three
    personas is whether any positive DBS confirmation outcome mechanically transmits
    to SATS common equity at all; nobody cited plan language settling this.
  last_updated: '2026-07-13T14:58:16Z'
---

## Scouted 2026-07-13T14:08:35Z

## Researched 2026-07-13T14:58:16Z

Three-round debate (bull/bear/quant) converged on **NO TRADE**. Bear and quant
independently flagged the same decisive gap: DISH DBS (the Chapter 11 filer) is a
subsidiary of EchoStar Corp (SATS, the listed parent), and no plan-of-reorganization
language was found establishing that value from the prepackaged plan flows to SATS
common equity. The 88%+ noteholder support and Aug 17 confirmation date are evidence
about creditor recovery at the subsidiary level, already priced in given the
prepackaged structure — not evidence about parent-equity impact. Quant's EV calc
came out net negative (~-1.5% after costs) once the unsupported upside leg was
zeroed out per bear's dilution critique. Bull held a diluted long thesis but never
refuted the core objection. See `transcript.md` for the full debate.

**No live price sanity check was available this run** — `toa price SATS ... --provider
twelvedata` returned HTTP 400.
