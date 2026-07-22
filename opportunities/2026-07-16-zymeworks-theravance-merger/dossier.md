---
id: 2026-07-16-zymeworks-theravance-merger
title: Zymeworks to acquire Theravance Biopharma for USD 929M cash-plus-CVR
status: scouted
created: '2026-07-16T07:53:17Z'
event:
  type: regulatory
  summary: Zymeworks agreed to buy Theravance Biopharma for USD 17.00 per share cash
    plus a CVR, adding COPD drug Yupelri; deal needs a two-thirds Theravance shareholder
    vote and HSR clearance, targeted to close H2 2026.
  impact_window: '2026-09-30'
tickers:
- ZYME
- TBPH
sources:
- title: Theravance Biopharma Enters Into Definitive Agreement to Be Acquired by Zymeworks
  url: https://investor.theravance.com/news-releases/news-release-details/theravance-biopharma-enters-definitive-agreement-be-acquired
  accessed_at: '2026-07-16T07:53:17Z'
hypothesis:
  statement: "The TBPH/ZYME merger-arb spread (gross USD 0.125/share, 0.741 percent
    of the USD 17.00 cash consideration versus TBPH at USD 16.875 on 2026-07-22,
    annualizing to roughly 3.2 percent per year over an assumed ~85-day path to
    close) does not compensate for asymmetric break risk. Expected value is negative
    before slippage under every downside/probability combination the panel could
    defend from the dossier -- P(close) approx 92 percent, downside on a break of
    -10 to -20 percent, EV -0.12 to -0.92 percent -- versus a 96.4 percent close
    probability needed to break even at the -20 percent downside case. This is a
    no-trade absent disclosed CVR terms or a clean pre-announcement price anchor
    for TBPH."
  direction: none
  confidence: 78
plan:
  ticker: TBPH
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
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
  dissent: "All three personas converged on PASS but for irreconcilable reasons.
    The bull argued downside is overstated -- the quant's -20 percent estimate is
    a plausible upper bound only, and absent a disclosed breakup fee the true
    break-loss is likely -12 to -15 percent, putting the trade closer to breakeven
    than the headline EV implies. The bear argued break-probability is understated
    -- three correlated failure vectors (the two-thirds shareholder vote, a
    possible HSR second request given unconfirmed respiratory/COPD portfolio
    overlap, and ZYME's smaller-cap acquirer financing/MAC-clause risk) argue for
    a 10-12 percent break probability, not the quant's 8 percent. The quant held
    both revisions to be evidentially empty -- neither is supported by concrete
    dossier evidence (no dissenting holder, no proxy-advisor flag, no breakup-fee
    disclosure) -- and identified the missing clean pre-announcement TBPH price
    anchor as the single largest data gap in the whole analysis: downside
    magnitude, not close probability, is what actually determines whether this
    deal could ever be EV-positive. Resolving it needs the definitive merger
    agreement's breakup-fee terms, the CVR's trigger/milestone terms, and a clean
    unaffected pre-announcement TBPH print -- none of which are in this dossier."
  last_updated: '2026-07-22T21:04:00Z'
---

## Scouted 2026-07-16T07:53:17Z

## Researched 2026-07-22T21:04:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), judged strictly
on this opportunity's own merits. Zymeworks agreed to acquire Theravance Biopharma
for USD 17.00/share cash plus a CVR (announced 2026-07-16), adding the COPD drug
Yupelri to Zymeworks' portfolio; the deal needs a two-thirds TBPH shareholder vote
and HSR clearance, targeted to close H2 2026. TBPH traded at USD 16.93 on
announcement day (2026-07-16T13:30Z) and USD 16.875 as of 2026-07-22 -- a gross
merger-arb spread of only 0.741 percent to the USD 17.00 cash price, annualizing to
roughly 3.2 percent per year over an assumed ~85-day path to an assumed 2026-10-15
close. The bull opened long on a clean-arb thesis (calm six-day tape, CVR framed as
free optionality, HSR treated as routine), but conceded in rebuttal that the CVR
should be modeled near-zero and that the quant's break-even-probability framing (a
96.4 percent close probability needed to break even at a -20 percent downside,
versus a 92 percent assumed base rate) was the decisive counterpoint. The bear
argued the spread is too thin for the deal-break tail risk and that the CVR is an
unresolved variable, not upside. The quant's EV arithmetic -- P(close) 0.92,
P(break) 0.08, downside on break -10 to -20 percent (flagged as the biggest data
gap: no clean pre-announcement TBPH price in the dossier) -- produced an EV of
-0.12 to -0.92 percent, negative before and after slippage across the full
sensitivity range. Synthesis: no standalone trade; the deal itself likely closes
(P approx 92 percent) but the arb spread does not pay for the tail risk. See
transcript.md for the full three-round debate.
