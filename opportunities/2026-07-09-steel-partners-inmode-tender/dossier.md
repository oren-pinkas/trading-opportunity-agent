---
id: 2026-07-09-steel-partners-inmode-tender
title: Steel Partners offers $16.75/share cash for InMode
status: researched
created: '2026-07-10T16:21:42Z'
event:
  type: regulatory
  summary: Steel Partners bid $16.75/share cash for InMode, topping the CEO-led buyout
    group's $16.20 offer; board decision on competing bids pending.
  impact_window: '2026-07-09'
tickers:
- INMD
sources:
- title: Steel Partners Offers to Acquire InMode for $16.75 Per Share in Cash
  url: https://www.businesswire.com/news/home/20260709185983/en/Steel-Partners-Offers-to-Acquire-InMode-for-$16.75-Per-Share-in-Cash
  accessed_at: '2026-07-10T16:21:42Z'
hypothesis:
  statement: InMode (INMD) is a live contested cash go-private - Steel Partners'
    $16.75/share tops the CEO-led group's standing $16.20/share signed deal. Some
    deal closing at >=$16.20 is highly likely (P~=0.83), with meaningful but not
    dominant upside optionality to >=$16.75 (P~=0.52 after haircutting for Steel's
    unconfirmed financing). The blended unconditional terminal (~$15.99) sits below
    both headline bids, so EV sign is entirely determined by a real, observable
    entry spread, which the corrupt price feed ($118.84 -> $169.23 -> $237.81 against
    a $16.75 cash tender) makes impossible to establish today.
  direction: long
  confidence: 35
plan:
  ticker: INMD
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
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
  dissent: 'The correct P(final >=$16.75) and the reference class for an unconfirmed
    topping bid. Bear argued quant''s 0.80-0.88 illegitimately borrowed the "2 FUNDED
    bidders" base rate when Steel''s financing is unconfirmed, haircutting to 0.55-0.70
    and weighting process/time risk (board sits on bids for months, capital ties
    up) as an independent loss scenario. Quant conceded the financing point and cut
    to 0.52, but countered that the standing $16.20 signed deal is a real floor,
    not unaffected price, giving P(some deal >=$16.20) ~=0.83. Bull''s Revlon-fiduciary-duty
    argument implies a thinner left tail than either bear or quant''s tree assumes.
    This ~15-30 point gap in P(superior outcome) is resolvable at zero cost once
    a real price series and confirmed/financed-vs-IOI status of Steel''s bid arrive
    - the post-mortem should check which reference class the actual outcome vindicated.
    Bear separately argued quant''s "verify-then-maybe" gating language is substantively
    identical to bear''s own no-trade stance, just relabeled, meaning the apparent
    three-way convergence may mask rather than resolve a real probability disagreement.'
  last_updated: '2026-07-12T07:10:24Z'
---

## Scouted 2026-07-10T16:21:42Z

## Researched 2026-07-12T07:10:24Z — NO-TRADE

Three-round panel converged on NO-TRADE despite a genuinely constructive directional
lean (structural completion probability P~=0.83 for some deal closing at >=$16.20).
Two co-sufficient blockers: (1) the internal price feed is economically incoherent
for a $16.75 cash tender ($118.84 -> $169.23 -> $237.81, +100% cumulative against
a fixed cash ceiling) and was independently flagged unusable by all three personas -
no valid spot exists to compute the real spread-to-offer, which is the single number
that determines EV sign since the unconditional blended terminal (~$15.99, quant's
three-node tree) sits below both headline bids; (2) Steel Partners' financing is
unconfirmed (an announced offer, not a demonstrated committed/financed bid), which
quant conceded cuts P(final >=$16.75) from an initial 0.80-0.88 down to 0.52. Bull's
Revlon-fiduciary-duty case for a thin left tail (floor = the still-live $16.20 signed
deal, not unaffected price) was the strongest pro-completion argument but did not
overcome the data-integrity gate; bull explicitly conceded from "enter now" to
"verified-small-or-no-trade." Re-entry gated on: a corroborated real price series,
real gross spread >=4-5% to $16.75 while trading at/above the $16.20 floor, and
on-record confirmation Steel's bid is bona fide/financed rather than an indication
of interest. Hard-pass if Steel's bid is revealed financing-contingent, the board
reaffirms $16.20 and Steel withdraws, or real price prints at/above $16.75 (no
spread left). Full transcript: transcript.md.
