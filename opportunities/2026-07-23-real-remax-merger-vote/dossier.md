---
id: 2026-07-23-real-remax-merger-vote
title: Real Brokerage and RE/MAX shareholder votes on merger
status: researched
created: '2026-07-23T21:02:37Z'
event:
  type: earnings
  summary: The Real Brokerage and RE/MAX Holdings have shareholder votes scheduled
    for Aug 14 2026 to approve their merger combining the two real estate brands under
    a new parent, Real REMAX Group Inc
  impact_window: '2026-08-14'
tickers:
- REAX
- RMAX
sources:
- title: Real-REMAX merger heads to final shareholder votes in August - Inman
  url: https://www.inman.com/2026/07/10/real-remax-merger-shareholder-votes-august/
  accessed_at: '2026-07-23T21:02:37Z'
- title: RE/MAX Holdings, Inc. - Form DEFM14A (SEC)
  url: https://www.sec.gov/Archives/edgar/data/0001581091/000110465926082291/tm2620002-1_defm14a.htm
  accessed_at: '2026-07-26T00:31:00Z'
- title: RE/MAX Holdings, Inc. - Form 8-K, merger terms (SEC)
  url: https://www.sec.gov/Archives/edgar/data/0001581091/000110465926049628/tm2612789d1_8k.htm
  accessed_at: '2026-07-26T00:31:00Z'
- title: RE/MAX Holdings, Inc. - Form DEFA14A, Company Support Agreement (SEC)
  url: https://www.sec.gov/Archives/edgar/data/0001581091/000110465926049630/tm2612789d5_defa14a.htm
  accessed_at: '2026-07-26T00:31:00Z'
- title: Real Brokerage and RE/MAX clear US antitrust hurdle for planned merger - Globe and Mail
  url: https://www.theglobeandmail.com/investing/markets/stocks/REAX/pressreleases/3304797/real-brokerage-and-remax-clear-us-antitrust-hurdle-for-planned-merger/
  accessed_at: '2026-07-26T00:31:00Z'
- title: "RMAX Legal Alert: RE/MAX Holdings hit with investigation over USD 13.80 merger announcement - PRNewswire"
  url: https://www.prnewswire.com/news-releases/rmax-legal-alert-remax-holdings-hit-with-investigation-over-13-80-merger-announcement-302762070.html
  accessed_at: '2026-07-26T00:31:00Z'
hypothesis:
  statement: >-
    NO-TRADE. The 2026-08-14 REAX/RMAX shareholder votes are a low-information
    catalyst 19 days out: deal terms (RMAX holders elect 0.515 post-consolidation
    Real REMAX Group shares OR USD 13.80 cash, capped cash pool ~USD 60-80M) have
    been public since 2026-07-10, HSR is cleared, and ~38% of RE/MAX voting power
    is contractually locked FOR via a Company Support Agreement. RMAX closed
    USD 9.36 (2026-07-24T19:59Z) against a blended deal value of ~USD 10.01
    (~6.85% spread), but that spread only pays out at deal CLOSE (2H 2026), not at
    the vote — a pass removes only ~1pt of it while a fail implies a drop toward
    the USD 8.045 unaffected price (2026-04-24), roughly -14% to -18%. At
    P(pass) 0.90-0.95, vote-window EV on a long is approximately -0.3% to -0.34%
    before costs, adverse-tail-to-edge ratio ~15:1. Hedged arb (long
    RMAX/short REAX) only pays at close and needs uncertain REAX borrow; RMAX
    options are judged too illiquid at this ~USD 250-300M cap for defined-risk
    structuring; a protective put fails its own breakeven (needs P(fail) > ~20%,
    estimate is 5-10%). All three panelists independently converged on NO-TRADE,
    with the bull explicitly reversing in Round 2 once deal-terms/lockup research
    confirmed the vote's high pass-probability actually strengthens, not weakens,
    the no-edge case.
  direction: none
  confidence: 88
plan:
  ticker: RMAX
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
  dissent: >-
    Nobody confirmed whether the Real Brokerage (REAX) side's own shareholder
    vote has an equivalent support-agreement lockup — the only confirmed lockup
    covers ~38% of RE/MAX-side voting power against a majority-of-outstanding
    (not majority-of-votes-cast) approval standard, already short of a clean
    majority. REAX holders are being asked to approve issuing stock after a ~37%
    decline from its unaffected price since signing, with no collar found in
    available filings — precisely the profile where an acquirer-side vote is a
    real contest rather than a formality, and it is the leg with zero confirmed
    lockup. The entire NO-TRADE call rests on P(fail) = 5-10%; quant's own math
    shows a long-put expression on RMAX flips to positive EV above
    P(fail) ~20% — if the REAX-side vote is genuinely unlocked/contested, that
    threshold is plausibly crossable and the correct action would invert to
    short/put, not merely size down. Secondary: no public ISS/Glass Lewis
    recommendation was found for either meeting; and quant's Round 1 downside
    estimate (-35%) was off by roughly 2x, corrected in Round 2 to -14% to -18%
    (unaffected RMAX price USD 8.045) — the panel reached the right answer partly
    via a wrong number.
  last_updated: '2026-07-26T00:31:00Z'
---

## Scouted 2026-07-23T21:02:37Z

## Researched 2026-07-26T00:31:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Quant pulled
actual deal terms from SEC DEFM14A/425/8-K filings: RMAX holders elect 0.515
post-consolidation Real REMAX Group shares (5.150 pre-consolidation, confirmed via
signing-date price triangulation, 99% confidence) OR USD 13.80 cash, cash pool capped
at USD 60-80M (proration now pinned near maximum since cash > stock-equivalent value),
pro forma ownership ~59% Real / 41% RE/MAX, HSR cleared, both votes 2026-08-14, close
expected 2H 2026. Live prices via `toa price --provider twelvedata`: RMAX
USD 9.36, REAX USD 1.683 (2026-07-24T19:59Z); unaffected prices (2026-04-24, pre-signing)
RMAX USD 8.045, REAX USD 2.675. Blended deal value ~USD 10.01 vs RMAX USD 9.36 = ~6.85%
spread, but it pays at deal CLOSE, not at the vote. Vote-window long EV ≈ -0.3% to
-0.34% before costs (P(pass) 0.90-0.95, tail ~-14% to -18%), adverse-tail-to-edge
~15:1. A Company Support Agreement locks ~38% of RE/MAX voting power FOR the deal, but
against a majority-of-outstanding (not votes-cast) standard, leaving a real residual
vote-failure tail; no equivalent lockup was found for the separate REAX-side vote.
Hedged arb, defined-risk options, and protective puts were each checked and rejected
on their own merits (pays outside window / illiquid at this cap / breakeven not met).
All three personas converged independently on NO-TRADE; bull reversed explicitly in
Round 2 once deal-terms research showed a high pass-probability strengthens, not
weakens, the no-edge case. Full debate with citations in `transcript.md`.
