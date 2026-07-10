---
id: 2026-07-08-boj-july-policy-meeting
title: Bank of Japan July policy meeting
status: researched
created: '2026-07-08T17:21:22Z'
event:
  type: macro
  summary: BOJ meets July 30-31 with the policy rate already at a 31-year high (1.00%)
    after June's hike; the Outlook for Economic Activity and Prices report is due
    July 31, a key signal for the yen and Japanese financials.
  impact_window: '2026-07-31'
tickers:
- 8306.T
sources:
- title: 'Rising sun, rising rates: Bank of Japan lifts rates to 31-year high - EFG
    International'
  url: https://www.efginternational.com/insights/2026/rising_sun_rising_rates_bank_of_japan_lifts_rates_to_31-year_high.html
  accessed_at: '2026-07-08T17:21:22Z'
hypothesis:
  statement: >-
    A long in 8306.T timed to the July 31 BOJ decision carries negative expected
    value: the hold-hawkish base case (~46-52% probability, the most likely path)
    does not pay enough (+1.0-1.2% modeled vs a +1.73% breakeven) to clear round-trip
    costs and the -2.0% hold-dovish tail, with no offsetting asymmetry. Bear and
    quant independently converged on NO-TRADE for the BOJ-day event; quant reached
    that verdict even after conceding ground to the bull's tone-vs-headline framing.
    The one bull point that survived cross-examination and won quant's explicit
    agreement is that any real edge in this dossier is idiosyncratic to MUFG's
    Aug 3-4 Q1 FY26 earnings print (NIM trajectory 0.80%->0.89%, +30% profit growth),
    not to reading BOJ tone -- but that is a separate, not-yet-actionable trade, not
    a reason to go long into July 31 at ~485, near the stock's all-time high.
  direction: none
  confidence: 34
plan:
  ticker: 8306.T
  action: no-trade
  entry:
    time: '2026-07-31T02:00:00Z'
    target_price: null
  exit:
    time: '2026-07-31T06:00:00Z'
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
    The strongest unresolved disagreement is the magnitude and existence of the
    hold-dovish downside tail (-2.0%) and its probability (bull implies it is
    over-weighted with no clean precedent; bear argues it should be ~50% and the
    tail could be worse than -8% in a disorderly case, citing the 2024 carry-unwind's
    Nikkei -12.4% single session). The bull's strongest evidence is that the only
    clean, *observed* analogue is the +3.13% pop on a realized hike (June 17); no
    precedent exists for a comparable move driven by tone alone absent action. The
    bear's strongest evidence is a Cabinet Office push (in the June Summary of
    Opinions) for the BOJ to "align with Takaichi's growth agenda" plus reporting
    that the dovish dissent count could double at the next meeting. Both cannot be
    fully right; the debate never reconciled them against a shared dataset. A future
    post-mortem should check what 8306.T actually did on 2026-07-31 relative to the
    modeled -2.0% hold-dovish assumption, and whether the driver was policy tone or
    an unrelated factor (overvaluation unwind, FX, carry trade).
  last_updated: '2026-07-10T07:30:06Z'
---

## Scouted 2026-07-08T17:21:22Z

## Researched 2026-07-10T07:30:06Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). No lessons found
(toa lessons-relevant, type=macro, ticker=8306.T). Reference price 8306.T = 485.08 as
of 2026-07-10T07:30Z. BULL opened long on a two-catalyst thesis (BOJ Outlook Report
July 31 + MUFG Q1 FY26 earnings Aug 3-4), arguing the real catalyst is hawkish
tone/guidance (yen still 160-162 post-June-hike, "insufficient to defend the
currency") rather than the ~9% priced headline hike odds, backed by NIM expansion
(0.80%->0.89%), +30% profit growth, and a +3.13% pop the day after June's hike was
confirmed. BEAR countered that a fully-expected June hike produced a muted broad-market
reaction (buy-rumor-sell-news), that Takaichi is stacking dovish board appointees
(Cabinet Office pushed alignment with the growth agenda per the June SOO; dovish
dissent count could double), and that MUFG is already extended (ATH ¥3,305 June 10,
-3% June 23, GuruFocus "overvalued" GF Score 63/100). QUANT modeled Hike 10% (+0.6%
tail-adjusted) / Hold-hawkish 52% (+1.0-1.2%) / Hold-dovish 38% (-2.0%), yielding a net
EV of -0.09% to -0.56% after ~20bps round-trip costs -- the hold-hawkish path would
need to deliver >=+1.73% to break even, a gap the bull's own evidence (a confounded,
realized-hike comp) couldn't close. Bear and quant converged on NO-TRADE for the
BOJ-day event; the bull conceded from a full naked long to a smaller structured
position but never closed the breakeven gap. Consensus finding: if an edge exists in
this dossier, it is earnings-anchored (MUFG's Aug 3-4 NIM/profit print), not a BOJ-tone
bet -- flagged as a separate, not-yet-actionable opportunity, not a reason to trade
into July 31. Re-entry watch conditions (any one flips the call): implied July hike
probability >25% (currently ~9.2%), hold-hawkish repricing implying >=+1.73% (currently
modeled ~+1.2%), or 8306.T selling off >=4% into the meeting (~466 from ~485) -- the
bear cautions such a selloff could be the start of a carry-unwind rather than a
discount entry, so any resulting position needs a hard stop. Full debate in
`transcript.md`.
