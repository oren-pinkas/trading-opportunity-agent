# Research Debate Transcript: FTC antitrust case against Zillow and Redfin

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` (bull/sonnet, bear/sonnet, quant/opus, synthesizer/opus)
Opportunity: `2026-07-22-zillow-redfin-ftc-antitrust`
Debate run: 2026-07-25

## Institutional memory injected

- [regulatory/CZR] Validate entry/exit timestamps fall within open trading sessions; roll non-trading exit dates forward.
- [regulatory/CZR] Never map a legal-calendar date directly onto an execution timestamp — treat it as a catalyst and derive fill time from the nearest valid session.
- [regulatory/PLD] A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge; simulate-plans has no path-dependent stop enforcement.
- [regulatory/PLD] When actual entry fill prints outside the planned entry band, treat that as an early falsification signal.
- [regulatory/NYAX] Test-query the real price provider (`toa price <ticker> <ts> --provider twelvedata`) for exact entry/exit timestamps during research before finalizing a plan.
- [regulatory/PG,STLD] Never treat a single missing minute-bar as terminal; exhaust a fallback ladder before recording market-data-unavailable.
- [regulatory/PG,STLD] Size fill-precision to the size of the edge; sub-0.5%-expected-profit, sub-30-confidence trades should use tolerance windows, not exact-minute targets.

## Round 1 — Independent research

### Bull (sonnet)

The FTC's May 7, 2026 denial of Zillow/Redfin's motion to dismiss lets the antitrust suit over real-estate listing practices proceed to discovery. Verified via `toa price --provider twelvedata`: Z closed near USD 44.13 intraday on 2026-05-07 (ruling day), then drifted to USD 41.76 by 2026-05-08, continuing to USD 40.73 (5/11), USD 37.80 (5/15), USD 33.69 (7/1), USD 33.07 (7/20), USD 30.87 (7/24) — a cumulative ~30% decline. RDFN returned consistent 404s from the price provider across all tested dates — could not confirm liveness.

Thesis: this is a "sell the overhang, buy the capitulation" setup — 11 weeks to price in "case proceeds to discovery" is a large de-rating for a procedural motion-to-dismiss denial (not a liability finding or verdict). Antitrust survival-of-MTD rulings against dominant platforms historically produce a sharp initial gap followed by stabilization once the market absorbs that trial/remedy risk is years away.

Catalyst timing: believed the 2026-09-15 impact_window likely marks a case-management/scheduling-order milestone (12–18 months out from any real trial), not a trial date itself; flagged settlement chatter as a live wildcard.

Proposed action: LONG Z only (RDFN untradeable). Entry ~USD 30.50–31.50, scaled in the week of 2026-07-27. Target USD 34–36 by/before 2026-09-15 (~12–17% bounce). Stop below USD 28. Modest sizing given contrarian-against-downtrend nature.

### Bear (sonnet)

RDFN does not exist as a tradeable equity: Rocket Companies completed its acquisition of Redfin on 2025-07-01; Redfin was delisted from Nasdaq (former holders now hold RKT at a 0.7926 RKT/share ratio). Any plan referencing RDFN is proposing a fill in a dead ticker.

The May 2026 ruling is stale relative to the 2026-07-22 scout date (2.5 months), and price action (Z: USD 45.03 on 2026-05-06 → USD 32.68 on 2026-07-09, ~27% decline) shows the market already digested it — some of that decline reportedly followed Zillow's Q4 2025 earnings call, confounding attribution.

**New catalyst found, absent from the dossier:** on 2026-07-08/09 the judge denied the FTC's motion for partial summary judgment and set a two-week trial starting **2026-08-24** — landing inside/near the 2026-09-15 impact window. Sources: RISMedia, The Real Deal, Seeking Alpha, Bloomberg, Multifamily Dive. This is the real dated catalyst, not the stale May MTD ruling; the dossier was scouted against the wrong anchor event.

Risks flagged: settlement/consent decree pre-trial (bullish relief), trial delay/continuance past 2026-09-15 (window expires unresolved), Q2 earnings noise, RKT-side dilution if forced to substitute for RDFN (Redfin economics immaterial inside Rocket's mortgage book), broader real-estate/rate-sensitive sector moves.

Recommendation: avoid the dossier as constructed (RDFN leg must be dropped or rewritten to RKT before entry/exit timestamps are even discussed); if trading at all, a small fade/vol position narrowly around 2026-08-24 trial start, Z only. Base case: no trade.

Sources:
- https://www.rismedia.com/2026/05/07/ftc-zillow-redfin-may-ruling-case-proceeds/
- https://www.rismedia.com/2026/07/09/zillow-ftc-redfin-judge-denies-motion-partial-summary-judgment/
- https://therealdeal.com/national/2026/07/08/ftc-challenge-to-zillow-redfin-partnership-headed-to-trial/
- https://seekingalpha.com/news/4612377-zillow-and-rockets-redfin-set-to-face-ftc-trial-next-month---report
- https://www.bloomberg.com/news/articles/2026-07-08/zillow-rocket-to-face-august-ftc-trial-over-rental-listing-deal
- https://www.multifamilydive.com/news/zillow-investor-lawsuit-redfin-partnership/824014/
- https://www.rocketcompanies.com/press-release/rocket-companies-completes-acquisition-of-redfin/
- https://www.investing.com/news/sec-filings/redfin-completes-merger-with-rocket-companies-delisting-from-nasdaq-93CH-4120173

### Quant (opus)

**Bottom line: NO-TRADE.** Gross event edge ~4.5 bps against ~25 bps round-trip friction; signal-to-noise ratio well below the 0.15 durable-edge threshold from institutional memory.

Base rate: "motion to dismiss denied" is a weak node in the litigation event tree — surviving Rule 12(b)(6) is the modal outcome in government antitrust suits (low surprise), and abnormal returns in antitrust litigation cluster at complaint-announcement and verdict/settlement, not interlocutory rulings. Median MTD-to-resolution time in civil antitrust is measured in years.

Verified prices via `toa price Z <ts> --provider twelvedata`:

| Date | Z (approx, UTC) |
|---|---|
| 2026-05-05 | 43.515 |
| 2026-05-07 (ruling) close | 43.77 |
| 2026-05-08 | 41.25 |
| 2026-05-11 | 40.78 |
| 2026-06-15 | 32.275 |
| 2026-07-16 | 34.07 |
| 2026-07-21 | 31.89 |
| 2026-07-22 | 31.68 |
| 2026-07-23 | 29.62 |
| 2026-07-24 | 30.97 |

**Ruling-day move was +0.6% — zero abnormal return, i.e. noise.** The -5.8% move the following session overlaps Zillow's Q1 earnings window (confounded, not attributable to the docket). The -28.8% decline from 05-05 to 07-24 has no docket catalysts inside it and is not measurably this event.

Realized daily sigma ≈ 4.45%/day (~70% annualized). Horizon to 2026-09-15 = 37 trading days → sigma_horizon ≈ ±27.1%. Plausible event-attributable magnitude ~3%. Signal/noise ≈ 0.11, below the PLD-lesson 0.15 threshold.

`toa price RDFN <ts> --provider twelvedata` returned 404 across three tested dates (2026-05-06, 2026-05-07, 2026-07-24) — exhausted the PG/STLD fallback ladder; this is a permanent symbol-not-found failure, not a missing-bar gap. RDFN resolves as uninformative-neutral; 50% of the dossier's tickers are untradeable in this harness.

EV calculation: P(price-forming news in window) = 0.15, E[|move| | news] = 3.0%, P(correct direction | news) = 0.55, friction = 0.25% round-trip → gross edge = 0.15 × 3.0% × 0.10 = +0.045%; net EV = -0.205%. Even stressing assumptions maximally favorable (P=0.30, magnitude 5%, direction 0.60): net EV = +0.05%, IR ≈ 0.002 against 27% sigma.

Flagged: Zillow's Q2 2026 earnings almost certainly print inside this window — the dominant, uncompensated risk ("any Z position held to 9/15 is a levered bet on Q2 earnings wearing an antitrust costume").

Recommendation: NO-TRADE, high confidence. If overridden: Z only (drop RDFN), ≤0.25% notional, confidence ≤15, tolerance-window fill not exact-minute.

## Round 2 — Rebuttal

### Bull rebuttal

Concedes RDFN dead outright (two independent confirmations decisive). Concedes quant's "zero abnormal return on ruling day" fully undercuts the original bounce thesis — no longer defends a directional long. Adopts bear's 2026-08-24 trial-start catalyst as the primary event going forward. Concedes the earnings-confound risk is real and unrebutted, and has no counter to the 4.5bps-edge-vs-25bps-friction math.

Narrows recommendation to: Z only, a short-dated vol/fade play strictly bracketing 2026-08-24 (entry ~1–2 trading days pre-trial-start, exit ~3–5 trading days post-start, avoiding the Q2 earnings print entirely), sizing ≤0.25% notional, confidence ≤15. States explicitly: will drop to full NO-TRADE if the position can't cleanly dodge the earnings date.

### Bear rebuttal

Reinforces that the bull's "capitulation" thesis has no event to capitulate from — a market that didn't react to the ruling (+0.6%) can't be said to be "oversold" because of it; the subsequent -29% drift is an unexplained move coinciding with, not caused by, the litigation calendar.

Corrects quant's Round-1 "arbitrary date" claim: the 2026-08-24 trial start is a real, dated, high-probability-of-some-news event (~70-90% probability of price-relevant headlines around trial opening), materially higher than quant's assumed 15%. But argues this raises P(news), not P(directionally forecastable news) — trial openings historically move stocks in low single digits, not double digits (verdicts move stocks, openings don't) — so the revised probability doesn't flip the EV conclusion, only changes the reasoning from "no catalyst" to "small catalyst still dominated by noise."

Both the earnings confound and vol-swamping (±27% horizon sigma vs. 3-5% plausible event magnitude) remain fully intact and untouched by the correction.

Updated recommendation: grudging allowance for, at most, a narrow tactical structure around 2026-08-24 — sized ≤0.4-0.5% notional, entered just ahead of 8/24 (not scaled in from 7/27 as bull proposed, which re-exposes to the earnings print and macro vol), closed within days of trial-opening headlines, ideally expressed as a defined-risk long-vol structure (straddle/strangle) rather than a naked directional long, since the actual edge is "something happens," not "it goes up." Does not support adding RDFN exposure; if a second leg is required, RKT is the only viable proxy but should be treated as a separate, independently-underwritten position, not a hedge or amplifier — Rocket's mortgage-origination fundamentals dominate any residual Redfin antitrust signal.

### Quant rebuttal

**Concedes and retracts** the Round-1 "arbitrary date, no docket milestone" claim — verified independently: Judge Anthony J. Trenga (E.D. Va.) denied the FTC's motion for partial summary judgment on 2026-07-08, finding genuine disputes of material fact on market definition; trial set for 2026-08-24, running two weeks (closing ~2026-09-04). Underlying conduct: Zillow's February 2025 payment of USD 100 million for exclusive multifamily rental-listing rights on Redfin's rental sites.

**Critical counter-correction: this is a BENCH trial, not a jury trial** as both bull and bear assumed. The judge alone decides market definition, market power, and legality — there is no discrete "verdict day"; a written opinion typically follows weeks-to-months after trial closes, often after post-trial briefing. This revises P(merits resolution lands before 2026-09-15) down to ~0.10-0.15, versus the ~0.35-0.45 a jury-trial framing would imply.

**Verified: Zillow reports Q2 2026 results after the close on Wednesday, 2026-08-05** (StockTitan, Yahoo Finance) — this does not overlap the 8/24 trial window, but does sit squarely inside bull's original 7/27→9/15 hold window as a serious, unhedged risk (Z's typical earnings-day move is high single digits, unforecastable sign, capable of gapping through a stop).

Revised EV via full branch tree (using Z reference price USD 30.81 @ 2026-07-24T19:59Z, 50% annualized vol, sigma_window ≈16.1% to 9/15):

| Branch | P | Conditional E[move] | Contribution |
|---|---|---|---|
| Merits decision issued by 9/15 | 0.15 | +3.0% (0.60×+15% + 0.40×-15%) | +0.45% |
| Mid-trial settlement/consent decree | 0.12 | -0.5% | -0.06% |
| Trial runs, no resolution by 9/15 | 0.67 | 0.0% (headline noise, sign unforecastable) | 0.00% |
| Trial slips/continued | 0.06 | ~0% | 0.00% |
| **Total** | | | **+0.39%** |

Information ratio ≈ 0.024 against 16.1% sigma — not distinguishable from zero. Sensitivity on the single load-bearing assumption (P(favorable) in Branch A) swings the total EV across [-0.24%, +1.07%] — **the sign of the edge is not statistically identified.**

Priced bull's specific structure (entry USD 30.81, stop USD 28, target USD 34-36) as a barrier race against 16.1% sigma: P(touch stop) ≈ 0.57, P(touch target) ≈ 0.50, stop nearer than target → win probability ≈ 0.44 → EV ≈ -0.26% before commissions/slippage. **Bull's specific structure loses money in expectation even ignoring earnings risk.**

Shortening the horizon to a 6-day bracket around 2026-08-24 (8/21→8/28 close) cuts noise sigma to ~7.7% and excludes the 8/5 earnings gap, but also excludes Branch A (the only branch with a directional expectation) — bracket EV/sigma ratio (~0.006) is worse than the full-window ratio (~0.024). Concludes: "the correct read from the new fact is not 'trade a shorter window,' it's 'this dossier's window is mis-specified relative to its own catalyst'" — the tradeable version of this idea has a horizon around Nov-Dec 2026 (expected written opinion), outside this dossier's scope.

Confirms RDFN unrecoverable (not merely impaired) and the RKT substitute analytically hopeless — Redfin's rental-listing economics are immaterial inside Rocket's mortgage-origination business, rendering any trial outcome unobservable in RKT's price.

Final recommendation: **NO-TRADE held**, on materially revised but ultimately unchanged grounds — moderate-to-high confidence (downgraded from Round 1's "high" since the central "arbitrary date" claim was factually wrong, though the conclusion survives revision). If forced to size anything: max 0.25% NAV on Z only, tagged explicitly as a lottery ticket, not a position.

Recommends dossier corrections: `impact_window` should move to 2026-08-24 (trial start, the only verifiable docket milestone) with a secondary marker for the expected written opinion (~Nov-Dec 2026, outside any reasonable trading window here); `tickers` should become `[Z]` only.

Sources:
- https://www.realestatenews.com/2026/07/09/judge-denies-ftc-request-to-presume-zillow-redfin-deal-unlawful
- https://www.housingwire.com/articles/ftc-zillow-redfin-lawsuit/
- https://www.rismedia.com/2026/07/09/zillow-ftc-redfin-judge-denies-motion-partial-summary-judgment/
- https://propmodo.com/ftc-takes-zillow-and-redfin-rental-partnership-to-august-trial/
- https://www.bloomberg.com/news/articles/2026-07-08/zillow-rocket-to-face-august-ftc-trial-over-rental-listing-deal
- https://finance.yahoo.com/real-estate/articles/zillow-group-announce-second-quarter-200500425.html
- https://www.stocktitan.net/news/Z/zillow-group-to-announce-second-quarter-2026-results-aug-i2ce520pobh8.html
- Z price USD 30.81 @ 2026-07-24T19:59Z — https://api.twelvedata.com/time_series?symbol=Z&interval=1min&date=2026-07-24&timezone=UTC

## Round 3 — Convergence (Synthesizer, opus)

### Hypothesis

- **Statement:** The dossier's premise is broken on two independent axes. (a) One of two tickers does not exist: Redfin (RDFN) was acquired by Rocket Companies on 2025-07-01 and delisted from Nasdaq — twelvedata 404s are permanent, and RKT is not a usable proxy (Redfin economics are immaterial inside Rocket's mortgage-origination business). (b) The named catalyst carries no measurable information: on the 2026-05-07 MTD-denial day Z closed +0.6% (zero abnormal return), so the subsequent -28.8% drift to USD 30.97 by 7/24 is unattributable to the docket and is confounded with Q1 results and housing fundamentals. The only real dated docket event in range is the two-week BENCH trial starting 2026-08-24 — bench, not jury, so there is no discrete verdict day, and the written opinion is expected weeks-to-months after close (~Nov-Dec 2026), putting P(merits resolution before 2026-09-15) at only ~0.10-0.15. Against ~4.45% daily vol (~27% horizon sigma to 9/15), plausible event magnitude of ~3-5% is not extractable: branch-tree EV is +0.39% with a CI of [-0.24%, +1.07%] (sign indistinguishable from zero, IR ~0.024), and the specific bull structure (entry ~30.50-31.50, stop 28, target 34-36) is a losing barrier race (~57% chance of touching the stop first, EV ~-0.26% before costs). Z Q2 earnings on 2026-08-05 after close sits inside the original hold window as an uncompensated confound.
- **Direction:** no-trade
- **Confidence:** 82

### Plan

**NO-TRADE.** No entry, no exit, no sizing, no ticker. All three personas converged: quant held flat NO-TRADE across both rounds; bull voluntarily downgraded from a directional long to a ≤0.25%-notional, ≤15-confidence lottery ticket conditional on dodging earnings; bear moved only to a "grudging allowance" for a ≤0.4-0.5% vol structure. No persona defends the dossier as constructed, and no persona produced a positive-expectancy directional structure. A sub-0.5%-notional structure with an EV sign indistinguishable from zero is not a plan.

### Dissent (gold for the post-mortem)

Bear vs. quant on whether a long-volatility structure tightly boxed around 2026-08-24 is tradeable. Bear argues high P(some news) justifies buying vol/gamma; quant argues high P(news) without high P(directional/magnitude-sufficient news) yields nothing, and the bench-trial finding removes the discrete resolution event a vol buyer would pay for. **Never settled** — no option chain, implied vol, term structure, or IV-vs-realized comparison around 8/24 was ever pulled; both sides argued from priors on an unmeasured number.

Runner-up (resolved, but notable): both bull and bear built a full round of reasoning on a **jury**-trial framing that was factually wrong; quant's bench-trial correction cut P(resolution before 9/15) from ~35-45% to ~0.10-0.15.

### Recommended dossier corrections

1. `tickers`: `[Z, RDFN]` → `[Z]`. RDFN delisted 2025-07-01 (Rocket Companies acquisition); 404 is permanent. Do not substitute RKT.
2. `event.impact_window`: consider moving to `2026-08-24` (trial start, the only real dated docket milestone), noting the expected written opinion lands ~Nov-Dec 2026, outside any reasonable trading window for this event.
3. Process note for scouting: a headline catalyst with zero ruling-day price reaction, and a ticker delisted for over a year at scout time, are both cheap pre-debate checks that would have reframed this item before three rounds of persona time were spent on it.
