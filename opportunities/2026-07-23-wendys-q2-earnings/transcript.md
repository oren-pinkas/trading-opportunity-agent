# Debate Transcript: WEN Q2 2026 Earnings (2026-08-07 BMO)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.

Isolation note: this debate was run for `2026-07-23-wendys-q2-earnings` ONLY. No other opportunity dossier was read or referenced.

## Pre-flight

- `toa price WEN 2026-07-23T16:29:19Z --provider twelvedata` -> USD 7.205 (source: twelvedata time_series, fetched 2026-07-23T16:29Z). Coverage confirmed live/tradeable before burning rounds.
- Institutional-memory lessons pulled via `toa lessons-relevant --type earnings --tickers WEN` (8 lessons from NKE/TSLA/DAL/LEVI debates injected as context — see below).

### Lessons injected as context

1. (NKE) Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short.
2. (NKE) Discount post-earnings negative base rates when the name is already at/near its 52-week low: most of the drawdown is priced in and a benign or one-time-beat print flips the reaction positive.
3. (TSLA) Set intraday exits at least one minute inside the session boundary (19:59:00Z / 15:59 ET, not 20:00:00Z): a 1-minute-bar provider has no bar stamped exactly at the close.
4. (TSLA) Add a pre-simulation timestamp guard that validates both legs map to available US-equity bars (13:30Z-19:59Z) and snaps to the nearest valid bar instead of voiding an untested thesis to NEUTRAL.
5. (DAL) A catalyst that already drove a large multi-week run to a 52-week high above the Street mean target is priced in — do not re-bet the same fundamental as a fresh gap trigger for the print.
6. (DAL) When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size directional position.
7. (LEVI) When the highest-confidence panelist (the quant) says directional EV is ~0 and the only positive-EV structure is out of mandate, log NO TRADE — do not manufacture a minimal directional position "for the learning loop."
8. (LEVI) Anchor entry prices to a live quote fetched at the actual entry timestamp, not a stale pre-move reference — validate the planned entry is still within a small tolerance of the current price before filling, and re-price or abort if the stock has already run away from the modeled entry.

---

## Round 1 — Independent research (parallel, no cross-visibility)

### Bull (sonnet) — opening position

**Read:** Wendy's reports Q2 2026 BMO Aug 7 2026, into a QSR tape defined by consumer bifurcation — Wendy's running an aggressive value-menu counter-offensive to defend traffic share. WEN is a low-dollar, high-dividend-yield stock (~USD 7.20) that trades on comps/unit-economics narrative more than headline EPS; stock near multi-year lows means the bar for "good enough" is low — a stabilization-in-comps story can trigger a relief rally (citing Lesson 2: discount negative base rates when a name is already depressed).

**Evidence:** Report date confirmed via 2026-07-23 press release, BMO Aug 7 (source: irwendys.com). Live quote USD 7.205 (2026-07-23T16:29Z, twelvedata). WEN in a multi-year downtrend from a ~USD 12-20 band toward single digits. QSR value-menu wars (MCD USD 5 meal deal era) as sector context. Dividend creates structural bid/support (income-holder base). Flagged as unverified: current consensus EPS/SSS estimates, exact dividend rate.

**Proposed action:** Long WEN via defined-risk call (or shares if options illiquid). Entry 2026-08-06T19:55:00Z at a re-checked live price (per Lesson 8). Exit 2026-08-07 between 13:35Z-14:30Z, hard exit by 19:59:00Z (per Lesson 3). Target: 5-8% move to USD 7.60-7.80. Stop: abandon if pre-market shows accelerating negative SSS or a dividend-cut signal.

**Confidence:** 42

### Bear (sonnet) — opening position

**Read:** WEN is a low-priced, mature-cap QSR name; post-earnings moves historically cluster 3-6%; the dossier is just an earnings-date announcement with no differentiated information edge — a coin-flip binary on a low-beta, income-oriented stock.

**Evidence:** WEN has guided/cut full-year SSS guidance in 2023/2024 amid QSR value-war pressure (MCD USD 5 meal deal, Taco Bell value pushes). Dividend yield historically ~6-7% at this price, dampening speculative pre-earnings positioning. Sector-wide "consumer bifurcation" theme is common across QSR (MCD/YUM/SBUX), meaning any WEN move is likely correlated with peer reactions rather than WEN-specific edge. No consensus EPS/SSS/IV/short-interest data present in the dossier.

**Proposed action:** NO-TRADE at this stage. Would need live verification of: options-implied move vs. historical realized move, position within the 52-week range, consensus SSS/EPS estimates and guidance trend, and peer QSR earnings reactions this cycle — before considering any position. If a bull case emerges, defined-risk options only (per Lesson 1).

**Confidence (skeptical view):** 72

### Quant (opus) — opening position

**Read:** A 12-days-out, zero-information dossier — an IR date announcement, no consensus EPS, whisper, SSS estimate, or IV. Magnitude without a direction estimate is variance, not edge. Live-data pull shows WEN is not a sleepy dividend QSR: it is a ~USD 7 stock in a ~30% twelve-month downtrend with episodic double-digit daily moves unrelated to earnings.

**Evidence (live `toa price WEN --provider twelvedata` pulls):**
- Dossier anchor (USD 7.205, 2026-07-23T16:29Z) is **stale**. Actual closes: Jul 20 USD 7.855 -> Jul 21 USD 7.625 -> Jul 23 USD 7.175 -> Jul 24 USD 6.995 — down 11.0% in four sessions, 2.9% below the dossier anchor.
- 12-month trend: 2025-08-07 USD 9.935 -> 2025-11-06 USD 8.795 -> 2026-01-15 USD 8.58 -> 2026-04-15 USD 6.905 -> 2026-06-15 USD 6.91 -> now USD 6.995. Roughly -30% y/y; current price ~7% above the 12-month low (~USD 6.535, May 4).
- Inferred (not confirmed against a verified earnings calendar) prior four earnings-day 1-day moves: 2025-08-08 +1.61%, 2025-11-07 +2.05%, 2026-02-26 +3.20%, 2026-05-08 +5.24%. Mean |move| ≈ 3.0%. Day-2 follow-through is negative noise, not drift: Nov 10 -5.63%, May 11 -7.78%.
- Ambient non-earnings daily vol ≈ 2.3%/day (~36% annualized); May 12 2026 alone was +16.95% with no earnings attached.
- Costs on a USD 7 stock: 1-cent spread = 14.3bps; round-trip crossing ≈ 28.6bps; add slippage on a post-BMO gap open -> assume ~50bps round-trip friction. Options are uneconomic: weekly USD 7-strike premium ~USD 0.20-0.30 with nickel-wide markets = 15-25% of premium consumed by spread alone.

**EV calculation:** Break-even hurdle at 3.0% magnitude, 50bps costs: p* = 58.3%. Coin-flip prior: EV = 0.5(+3.0%) + 0.5(-3.0%) - 0.5% = **-0.50%**. Most-generous case (Jeffreys-smoothed p≈0.83 from the 4-for-4 record): EV = 0.83(+3.0%) - 0.17(-3.0%) - 0.5% = **+1.50%**, but n=4, dates inferred not confirmed, 95% credible interval on p runs down to ~0.47 (below the hurdle), and Kelly swings from 67% to 0% depending on estimator. Adverse tail on a bad print: -8% to -12%, giving a 6-8x tail-to-edge ratio against the best-case EV — matching the Lesson-1 no-trade filter profile.

**Proposed action:** NO TRADE (zero position, not sized down). Waiting is free — consensus, whisper, and franchisee/comp commentary arrive before Aug 7. Re-open trigger, not a position: revisit 2026-08-05/06 with a live quote, consensus EPS/SSS, and the implied move from the Aug-7 weekly straddle.

**Confidence:** 74

---

## Round 2 — Rebuttal (parallel; each persona shown the other two's Round-1 openings)

### Bull rebuttal

Concedes the Quant's stale-price finding is "the single most damaging fact on the table" — the true anchor is USD 6.995, an unexplained 11% four-session slide, not a resting/stabilized level. Pushes back partially on the ambient-vol point: a single +16.95% non-earnings gap shows fat-tailed idiosyncratic risk but doesn't necessarily contaminate the *scheduled* earnings-day distribution. Argues the Quant's own EV math (coin-flip -0.50%, best-case +1.50%) is "mild negative drift," not a screaming loser — a weak argument against options (agreed uneconomic) but a much weaker argument against a small, tightly-stopped share position. Sets a binding condition: no entry unless a live peer-QSR check (MCD/YUM/JACK) confirms the slide is sector-wide, not WEN-specific distress, plus a dividend-safety check. Downgrades structure from calls to shares-only, cuts size, moves target to USD 7.35-7.50 (5-7% off USD 6.995).

**Revised confidence: 30** (down from 42).

### Bear rebuttal

Argues the Quant's live data upgrades caution from "no edge" to "negative-expectancy trap." The 4-for-4 record (n=4, unconfirmed dates) is a small-sample artifact per the Quant's own 95% CI (down to ~47%); the day-2 reversals (-5.6%, -7.8%) reinforce the priced-in/fade thesis — even the bull scenario doesn't hold past the print session. Argues the Bull's "stabilization = relief rally" framing is now directly contradicted, not just unverified: the tape shows an accelerating -11% slide this week with no stated cause, i.e. unexplained live event risk, not a coiled spring waiting for good news. Reframes the trade as "we don't understand the current selloff, and options are uneconomic to hedge that uncertainty" — a stronger NO-TRADE, not a weaker one.

**Revised confidence: 78** (up from 72).

### Quant rebuttal

Confirms the Bull's target is now mechanically harder (+8.6% to +11.5% from USD 6.995, not +5-8%) and that the Bull's own stop condition (accelerating negative signal pre-print) may already be triggered by the unexplained slide. Concedes the Bull's relief-rally-at-lows asymmetry is directionally plausible but explicitly **unmeasurable** with the current information set (no implied move, no consensus, no options surface) — "an unquantified asymmetry is a story about an edge, not an edge." Flags the dividend "structural bid" argument as double-edged: a 6-7% yield on a 30%-drawdown name usually signals the market pricing cut risk, not providing support — and notes the Bull's own stop condition (dividend cut) concedes this. Corrects the Bear's "3-6% historical move" claim to the measured ~3.0% mean (Bear's range biased ~1pt high, which if anything strengthens the no-trade case by raising the break-even hurdle). Corrects the Bear's "sleepy low-beta" framing: ambient vol (~2.3%/day, one +16.95% non-earnings print) means earnings is *not* the dominant variance source in this name — this is a high-vol microcap trade with a print attached, not a clean binary catalyst. Explicitly flags that panel convergence (Bear and Quant both landing on NO-TRADE) is weak corroboration since the two reached it via incompatible models of the stock (sleepy income name vs. high-ambient-vol downtrend).

**Revised confidence: 79** (up from 74). Re-open trigger reaffirmed: 2026-08-05/06, live quote + confirmed consensus EPS/SSS + implied move from the Aug-7 weekly straddle + verified (not inferred) historical earnings dates.

---

## Round 3 — Synthesis (opus, neutral)

### hypothesis

**Statement:** There is no measurable, positionable edge in WEN into the Aug 7 2026 BMO print at this time. The Bull's "depressed-name relief rally" asymmetry is directionally coherent but unquantified: the dossier anchor (USD 7.205) was stale, the true anchor is USD 6.995 after an unexplained ~11% four-session slide (Jul 20 USD 7.855 -> Jul 24 USD 6.995), and no consensus EPS, comp/SSS estimate, implied move, or short-interest data exists yet. Measured earnings-day magnitude (~3.0% mean, n=4, dates inferred not confirmed) sits below the ~58.3% break-even hit-rate hurdle once ~50bps round-trip friction on a sub-USD-7 stock is applied, while ambient non-earnings volatility (~2.3%/day, including a +16.95% non-earnings session on 2026-05-12) means the print is not even the dominant variance source. The adverse tail (-8% to -12%) is 6-8x the best-case measured edge (+1.50% under the most generous 4-for-4 assumption, whose 95% CI falls to ~47% hit rate). Direction is unknowable; magnitude alone is variance, not edge.

**Direction:** none

**Confidence:** 76 (in the NO-TRADE conclusion, not a directional view — set slightly below the Bear/Quant pair of 78/79 because those two reached the same verdict via mutually incompatible models of the stock, which is weak corroboration, not independent confirmation; the Bull's Round-2 concession collapsed one side of the debate rather than resolving it)

### plan

**Ticker:** WEN
**Action:** no_trade
**Entry:** none — no position is to be opened
**Exit:** none — not applicable
**Expected profit:** 0.00% (zero position). For the record: best modeled alternative was +1.50% EV under assumptions judged non-investable (n=4, unconfirmed dates, Kelly swinging 67%->0% across the CI), against a -8% to -12% adverse tail; coin-flip assumption yields -0.50%.

Explicitly rejected structures (for the post-mortem record):
- Bull's Round-1 long calls: withdrawn by the Bull itself — weekly USD 7-strike premium ~USD 0.20-0.30 with nickel-wide spreads = 15-25% friction; uneconomic.
- Bull's Round-2 reduced-size shares-only long to USD 7.35-7.50: requires +5.0% to +7.2% from USD 6.995 (2-4x the measured ~3.0% mean move); the Bull's own stop condition is arguably already pre-triggered by the unexplained slide.

### dissent

**Strongest unresolved disagreement: is the unexplained four-session -11% slide a discount or a warning?**

The Bull's surviving claim — never refuted, only deferred — is that a name down ~30% y/y, ~7% off its 12-month low, carrying a 6-7% dividend yield, has a genuinely low bar for a "good enough" print, and stabilization can produce an outsized relief move. The Quant conceded this asymmetry is directionally plausible and refused it only on measurability grounds, which is an epistemic objection, not a substantive rebuttal. Against that: the Bear's fade evidence (day-2 follow-through negative in both observed cases) suggests even a correct relief-rally call may not survive to a next-session exit, and the Quant's inversion of the dividend argument (high yield on a large drawdown more plausibly prices cut risk than support) turns the Bull's floor into a possible trapdoor. The disagreement is unresolved because the deciding fact is missing: nobody established the cause of the 11% four-session decline. If sector-wide QSR repricing, the Bull's read strengthens materially; if WEN-specific (cut risk, leak, franchisee/unit-economics headline), the Bear's read is correct. The panel converged on NO TRADE without answering this — right for the current information state, but convergence under a data blackout, not a validated call (cf. the pool-corp precedent in institutional memory of false consensus under a blackout).

Secondary dissent: the Bear and Quant agree on the verdict via incompatible models of WEN (low-beta income stock vs. high-ambient-vol downtrend) — which one is correct determines whether a future position should ever be sized as an earnings trade at all, or only as a volatility trade with a print attached.

### Re-open trigger (this is a live opportunity, not closed)

**Re-open window: 2026-08-05 / 2026-08-06** (T-2/T-1 to the BMO print). NO TRADE is a decision about the current information state, expected to change materially before the print. Required before any position is reconsidered (all six, not a subset):

1. Live quote and 52-week-range position on the re-open date (fresh anchor mandatory — the stale-USD-7.205 anchor was the largest process failure in this debate).
2. Cause of the Jul 20-24 ~11% decline, resolved via peer-QSR price action (MCD, YUM, QSR, JACK) over the identical window — sector beta vs. WEN-specific distress.
3. Confirmed consensus EPS and SSS estimate, plus whisper number if obtainable.
4. Implied move from the Aug-7-expiry weekly straddle vs. the measured ~3.0% realized mean (non-negotiable gate — no implied move, no trade).
5. Verified (not inferred) historical earnings dates and corresponding day-1/day-2 moves.
6. Dividend-safety check (payout ratio, FCF coverage, any pre-announcement/board commentary).

**Escalation gate:** if favorable, reconsidered position is shares-only, reduced size, same-session hold with a hard close before the Aug 7 US close — never overnight, given the observed day-2 fade. Options remain rejected regardless of data, on friction grounds alone.

**Default:** if the re-open check is not performed, or items 2/3/4 remain unresolved by 2026-08-06, NO TRADE stands automatically through the print.
