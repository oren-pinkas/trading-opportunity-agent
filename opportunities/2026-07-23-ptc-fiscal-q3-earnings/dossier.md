---
id: 2026-07-23-ptc-fiscal-q3-earnings
title: PTC Inc fiscal Q3 2026 earnings, July 29
status: researched
created: '2026-07-23T16:29:19Z'
event:
  type: earnings
  summary: PTC reports fiscal Q3 2026 results after market close Wednesday July 29
    2026, following its AI product platform expansion announcements
  impact_window: '2026-07-29'
tickers:
- PTC
sources:
- title: PTC sets July 29 webcast for fiscal Q3'26 results - StockTitan
  url: https://www.stocktitan.net/news/PTC/ptc-to-announce-fiscal-q3-26-results-on-wednesday-july-29-apxvr4swz0bb.html
  accessed_at: '2026-07-23T16:29:19Z'
- title: PTC to Announce Fiscal Q3'26 Results - investor.ptc.com
  url: https://investor.ptc.com/resources/news/news-details/2026/PTC-to-Announce-Fiscal-Q326-Results-on-Wednesday-July-29-2026/default.aspx
  accessed_at: '2026-07-25T22:10:00Z'
- title: PTC Unveils a Wave of Product Innovations - ptc.com
  url: https://www.ptc.com/en/news/2026/ptc-unveils-a-wave-of-product-innovations
  accessed_at: '2026-07-25T22:10:00Z'
- title: PTC stock forecast and analyst price targets - stockanalysis.com
  url: https://stockanalysis.com/stocks/ptc/forecast/
  accessed_at: '2026-07-25T22:10:00Z'
- title: PTC earnings history - Investing.com
  url: https://www.investing.com/equities/ptc-earnings
  accessed_at: '2026-07-25T22:10:00Z'
hypothesis:
  statement: >-
    PTC's FQ3 2026 print (AMC 2026-07-29) offers no exploitable directional edge.
    The stock trades on forward guidance rather than the print (8/8 EPS beats over
    the last two years with the stock ~46% below its 52-week high; the May 6 2026
    beat+raise+buyback still saw the stock down ~6% over the following month), and
    the bear's deferred-ARR-reliance finding from the Q2 call (H2 growth described
    as "much more" the already-banked deferred ARR, with new-business ARR
    ex-deferral only "approximately" flat YoY) — the debate's best qualitative
    contribution — is ~12-week-old public information already absorbed into a
    -15.49% consensus EPS-estimate cut and a ~9th-percentile-of-52-week-range
    price, worth a likelihood ratio of roughly 1.1-1.2 (implying P(down) ~0.51-0.53),
    not the ~1.63 that would be needed to justify a short. The bull's AI-platform
    catalyst case (PTC Orbit/Jetstream, Onshape Labs) cannot appear in the FQ3 print
    at all — PTC's fiscal year ends Sept 30, so FQ3 = Apr-Jun, and Onshape Labs
    (launched July 14) falls in FQ4 — so it can only enter via forward guidance,
    the same channel that has punished this stock twice running. Net EV is
    approximately -0.23% after ~0.27% round-trip costs and stays negative across
    P(up) 0.47-0.56 and under a widened move-magnitude scenario. Independently,
    the price anchor is unresolved: `toa price PTC --provider twelvedata` returned
    HTTP 429 seven times across all three personas, and the two web-sourced quotes
    used as fallback differ by 4.23% (USD 118.52 vs USD 123.54) - about 18x the
    modeled gross edge - so any P/L sign would be set by an unverifiable input.
  direction: none
  confidence: 72
plan:
  ticker: PTC
  action: no-trade
  entry:
    time: '2026-07-29T19:50:00Z'
    target_price: null
  exit:
    time: '2026-07-30T13:45:00Z'
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
    Whether the bear's deferred-ARR finding is priced in, and the debate had no
    way to settle it. Bear holds that management's own Q2 transcript admission
    ("Approximately" flat new-business ARR ex-deferred) is an under-appreciated
    weakness that makes a propped-up beat likely to be sold. Quant holds the same
    fact is 12 weeks old, public, and already reflected in a -15.49% consensus cut
    and a 9th-percentile price, worth only LR ~1.1-1.2 - not enough for a short.
    Bull, having conceded the flag is real, argues the guidance raise was issued
    with full knowledge of the mix and that constant-currency ARR is cash-collectable
    regardless of composition. Nobody could measure absorption: no T+1 return series
    for the last 8 prints was produced, no options-implied move was found, and the
    price anchor itself failed verification seven times (twelvedata HTTP 429, a
    recurring infrastructure constraint - see project memory). Secondary unresolved
    item: quant's structural claim that n=8 earnings observations (SE ~17.7pp)
    cannot statistically distinguish P=0.50 from P=0.68, implying single-name
    earnings-direction betting is underpowered by construction - a standing
    argument for NO-TRADE as the default prior for this class of setup generally,
    not just PTC.
  last_updated: '2026-07-25T22:15:00Z'
---

## Scouted 2026-07-23T16:29:19Z

## Researched 2026-07-25T22:15:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three personas
converged on no executable directional position, though for different reasons and with
diverging confidence trajectories: quant held ZERO/NO-TRADE throughout and *raised*
confidence 62->66 (the only persona whose confidence moved toward its own conclusion);
bull fell 55->45 after conceding the deferred-ARR flag was real, that PTC "trades on
guidance not the print" was the single strongest point made by anyone, and that a
fiscal-calendar error undercut the AI-catalyst timing case (Onshape Labs is FQ4, not
FQ3); bear rose only 35->38 and never escalated to an active short, cautioning against
chasing an already-absorbed story at the 9th percentile of the 52-week range. KEY
FINDING: PTC has beaten EPS estimates 8/8 of the last 8 quarters yet sits ~46% below
its 52-week high - it trades on guidance, not the beat. QUANT EV: net ~-0.23% after
costs, robust negative across P(up) 0.47-0.56, short side nets only ~+0.02% (still
below the 2% hurdle). OPERATIONAL BLOCKER: toa price 429'd seven times across all three
personas (twelvedata rate limit, not a coverage gap - matches the known POOL-corp
pattern); the two unverified web-sourced price fallbacks disagree by 4.23% (USD 118.52
vs USD 123.54), ~18x the modeled gross edge, making any P/L sign unverifiable even if
the thesis had merit. Verdict: NO-TRADE. Flips only on a verified price anchor plus
either (a) an options-implied move <=5% against a >=7% realized median, enabling a
non-directional long-vol structure, or (b) a hard new datapoint (not the stale
deferred-ARR story) pushing P(down) to ~0.60+. Full debate in `transcript.md`.
