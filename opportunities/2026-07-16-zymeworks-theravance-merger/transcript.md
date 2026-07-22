# Research debate — 2026-07-16-zymeworks-theravance-merger

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus.

## Context

Zymeworks (ZYME) agreed to acquire Theravance Biopharma (TBPH) for USD 17.00/share
cash plus a CVR, announced 2026-07-16. Adds Yupelri (COPD drug) to Zymeworks'
portfolio. Deal requires a two-thirds TBPH shareholder vote and HSR clearance.
Targeted close H2 2026; dossier impact_window 2026-09-30.
Source: https://investor.theravance.com/news-releases/news-release-details/theravance-biopharma-enters-definitive-agreement-be-acquired

Prices (toa price, twelvedata):
- TBPH: 16.93 @ 2026-07-16T13:30Z (announcement day) → 16.875 @ 2026-07-22T14:00Z/17:00Z
- ZYME: 24.75 @ 2026-07-16T13:30Z → 24.075 @ 2026-07-22T13:30Z

Relevant lessons injected: (1) validate entry/exit timestamps fall within an open
trading session, rolling non-trading exit dates forward; (2) never map a
corporate/legal calendar date directly onto an execution timestamp — derive fill
time from the nearest valid trading session.

## Round 1 — Independent research

### Bull
Long TBPH merger-arb. Gross spread (17.00−16.875)/16.875 = 0.741%, annualized
~3.9% over ~70 days to 2026-09-30. TBPH stable 16.93→16.875 over 6 days — no
rumor of trouble, no topping bid. Handicaps HSR as routine (no antitrust overlap
flagged). CVR framed as free optionality (zero cost basis). ZYME itself not an
attractive bull vehicle (down 24.75→24.075, market pricing dilution). Recommends
long TBPH, entry ~16.875, exit at first valid session on/after 2026-09-30.

### Bear
0.74% spread annualizes to only ~4% before costs — too thin for a professional
risk-arb desk unless rock-solid, implying real break-risk is priced in already.
Risks: (1) two-thirds shareholder vote is a genuine hurdle, not paperwork; (2)
HSR could draw a second request given possible respiratory/COPD portfolio
overlap; (3) CVR likely worth near-zero — counting it as free upside is
optimistic accounting; (4) ZYME (smaller-cap acquirer) carries financing/
balance-sheet/MAC-clause risk. Asymmetry: ~0.74% capped upside vs. 10-15%+
downside on a break. Recommends skip, or token-size only, pending vote-date/HSR
news.

### Quant
Spread 0.741%. Assumed close 2026-10-15 (85 days out), annualized ~3.18%/yr.
P(close)=0.92, P(break)=0.08 (base rate for signed cash deal, 2/3 vote, no
antitrust overlap flagged). Downside on break ≈ −20% (flagged as a real data
gap — no clean pre-announcement price anchor in the dossier). EV = 0.92×0.741%
+ 0.08×(−20%) = −0.918%, worse after ~0.1-0.3% slippage. Break-even P(close)
needed = 96.4%, above the 92% assumed base rate. Verdict: negative EV, PASS as
standalone; only rational inside a diversified 20+ name risk-arb book at ≤1%
sizing. CVR terms unknown — the one thing that could flip the call. Conditional
execution if forced: entry 2026-07-22T15:00Z, exit 2026-10-15T15:00Z (both valid
NYSE sessions).

## Round 2 — Rebuttal

### Bull (revised)
Concedes −20% downside is a plausible upper bound, not a base case — absent a
stated breakup fee, a blended −12% to −15% is more realistic. Concedes the
92%/8% split is roughly defensible; won't claim it should be higher without
vote-date/HSR data. Concedes the CVR should be modeled near-zero, not "free
upside" — overclaimed originally. Cites the quant's break-even-probability
framing (96.4% needed vs. 92% assumed) as the strongest point against the
original call. Revised call: back off from full-size long; recommend a
reduced/token position (≤1% of book) only inside a diversified book, not
standalone; treat any HSR second-request or vote-date delay news as an
immediate exit trigger.

### Bear (revised)
Argues 8% break-probability may be understated — three correlated risk vectors
(2/3 vote, possible HSR second request, ZYME financing/MAC risk) could push
true break-probability to 10-12%. Rejects "6 days calm = safe" as recency bias:
pre-catalyst calm is uninformative about post-catalyst outcome, and 6 days is
under 10% of the ~70-85 day timeline. Revises own downside estimate up from
−15% to align with the quant's −20%, calling it the more defensible
conservative assumption absent a clean pre-deal price anchor. Agrees the CVR is
an unresolved variable, not upside. Final call: EV math settles this decisively
as a pass; no legitimate position size turns a −0.92% to −1.2% net EV into a
winner; at most a fractional-percent informational tracking position.

### Quant (revised)
On raising P(close): moves it from 0.92 to at most 0.93 — six calm days is thin
evidence for an 85-day process; most deal breaks are back-loaded near
vote/HSR milestones, none of which have occurred yet. On lowering P(close):
directionally fair but evidentially empty — no dissenting holder, no
proxy-advisor flag, no second-request precedent cited in the dossier; holds
P(close)=0.92, effectively unchanged. Sensitivity: at −20% downside, EV=−0.918%
(break-even P=96.4%); at −10% downside (optimistic), EV=−0.118% (break-even
P=93.1%) — still negative before slippage in both cases, negative after in
both. Trade only turns EV-positive if downside ≤~−8% AND P(close)≥0.93
simultaneously — a corner not justified by the dossier. CVR: correct
conservative default is $0; it's the one documented catalyst that could flip
the call but cannot be banked. Final numbers: P(close)=0.92, downside −20%
base/−10% optimistic (unresolved, biggest gap), EV −0.92% to −0.12% (negative
after slippage in both), verdict PASS as standalone, token size only (≤1% of a
20+ name arb book) if forced, instrument long TBPH, do not initiate
single-name absent CVR terms or a clean downside anchor.

## Round 3 — Synthesis

**Hypothesis:** The TBPH/ZYME merger-arb spread (~0.74% gross, ~3.2%/yr
annualized) does not compensate for asymmetric break risk; expected value is
negative before slippage under every downside/probability combination the
panel could defend from the dossier. This is a no-trade absent CVR terms or a
clean pre-announcement price anchor.
- direction: no-trade
- confidence: 78

**Plan:**
- ticker: TBPH
- action: pass (no standalone position)
- if forced to a token/tracking position only: buy, entry 2026-07-22T15:00:00Z
  @ 16.875, exit 2026-10-15T15:00:00Z @ 17.00 (exit derived from the ~85-day
  assumed close catalyst, not the naive 2026-09-30 impact-window date; both
  timestamps are valid NYSE trading sessions)
- expected_profit_pct: +0.74% gross best case; blended EV −0.92% (−20%
  downside case) to −0.12% (−10% downside case), negative after slippage in
  both
- sizing: standalone PASS; only defensible as ≤1% of a diversified 20+ name
  arb book as an informational tracker, not a real position

**Dissent (strongest unresolved disagreement):** All three converged on PASS
but for irreconcilable reasons:
- Bull: downside is overstated — −20% is an upper bound; absent a stated
  breakup fee, true break loss is likely −12% to −15%, closer to break-even
  than the headline EV implies.
- Bear: break-probability is understated — three correlated failure vectors
  (2/3 vote, possible HSR second request, ZYME small-cap financing/MAC risk)
  argue for 10-12% break probability, not 8%.
- Quant/synthesizer: both revisions are evidentially empty; the real
  unresolved variable is the missing clean pre-announcement price anchor.
  Downside magnitude — not probability — is the single largest data gap and
  alone determines whether this deal could ever be EV-positive. Resolve the
  anchor and the CVR terms before revisiting.
