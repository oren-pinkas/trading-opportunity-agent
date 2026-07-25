# Research Debate Transcript — AIG Q2 2026 Earnings

Strategy: three-round-panel. Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
Generated: 2026-07-25T00:55:57Z (event impact window 2026-08-06).
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Event:** American International Group (AIG) reports Q2 2026 results 2026-08-06 after market
close. Analysts forecast adjusted EPS of USD 1.93, up 6.6% YoY, with AIG having beaten estimates
each of the last four quarters. Source: Yahoo Finance, "American International's Q2 2026
Earnings: What to Expect" (accessed 2026-07-23T19:57:39Z).

**Reference price:** USD 79.14 at 2026-07-24T19:59Z close (source: `toa price AIG
2026-07-24T19:59:00Z --provider twelvedata`, twelvedata 1min series). Note the 20:00:00Z bar
does not exist for a 1-min provider; snapped to 19:59Z per institutional lesson from the TSLA
post-mortem.

**Institutional lessons applied (from `toa lessons-relevant --type earnings --tickers AIG`):**
- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x
  adverse-tail-to-edge ratio is a no-trade filter, not a size-down (NKE).
- A catalyst that already drove a large run/is well-telegraphed is priced in — don't re-bet the
  same fundamental as a fresh gap trigger (DAL).
- When the strongest unrebutted dissent aligns with the quant's own EV math showing
  near-zero/marginal edge, synthesize to NO-TRADE rather than a quarter-size directional
  position (DAL, LEVI).
- If directional EV is ~0 and the only positive-EV structure is out of mandate (e.g. straddle),
  log NO TRADE — don't manufacture a minimal directional position "for the learning loop" (LEVI).
- Anchor entry prices to a live quote at the actual entry timestamp (LEVI).

---

## Round 1 — Independent Research

### Bull (sonnet)

This is a positive-drift setup into a known catalyst. AIG has a hard binary event with real
historical asymmetry: four straight beats plus consensus modeling +6.6% YoY EPS growth signals
analysts are extrapolating genuine operational momentum (pricing, reserve releases, buyback-driven
EPS accretion). The stock likely drifts up modestly into the print, then the real move comes from
the magnitude of the beat and management commentary on capital return pace and combined ratio
trends.

Evidence vs. inference: consensus USD 1.93 (+6.6% YoY), 4 consecutive beats, ref price USD 79.14
are given facts. AIG's multi-year de-risking of legacy long-tail reserves and buyback program is
general knowledge, not confirmed for this specific quarter — flagged as inference. No data given
on options IV, expected move, or 52-week range positioning, so the "already priced in near 52-wk
high" lesson can't be confirmed or denied here.

Beat-streak analysis: four consecutive beats is a real operational signal but by now the market
prices a "beat" as the base case — the tradeable edge isn't "will they beat" but "will they beat
by enough, and will guidance/commentary exceed the embedded expectation." A beat-and-raise with
buyback acceleration is the outsized-upside scenario; an in-line beat with no incremental catalyst
likely produces a muted or fade reaction.

Proposed action: Long shares (avoids IV-crush noise given no visibility into current implied
move). Entry ~30-60 min before the 2026-08-06 close (anchored to live quote at actual entry time,
not the stale 07-24 reference). Exit: scale out 2026-08-07 (partial at open if gap-up, hold
remainder to 1 min inside session close, full exit by EOD 08-07). Target +2% to +4% one-day
reaction on a clean beat-and-raise; treat <1% as priced-in and exit flat/small loss.

**Confidence: 55/100.**

### Bear (sonnet)

A four-quarter beat streak against Street estimate $1.93 is table stakes — already learned by the
market, already reflected in the price. The tradeable surprise isn't the number, it's the
qualitative commentary: reserve development in long-tail casualty lines, pace/size of the next
buyback authorization, investment income trajectory, and catastrophe-loss framing for the back
half of the year (the print lands mid-Atlantic-hurricane-season).

Specific risks that break a naive "buy the beat" trade:
- **Catastrophe timing** — Aug 6 print sits mid-hurricane-season; commentary on July/early-Q3
  storm activity and reinsurance retention could overhang guidance regardless of the printed Q2
  number.
- **Reserve development in long-tail lines** — any signal of adverse development creeping back
  into general liability/excess casualty/professional lines undermines the "clean book" narrative
  central to the bull case.
- **Buyback pace disappointment** — slower repurchase cadence or pivot to M&A over buybacks could
  trigger sell-the-news even alongside a beat.
- **Investment portfolio / rate sensitivity** — dovish macro shift or credit-spread widening is a
  read-through risk.
- **Life & Retirement (Corebridge-linked) segment noise** — variable annuity/spread compression
  dynamics, a recurring wildcard.

What would change my mind: a quantified guidance upgrade + explicit reserve releases + a buyback
authorization increase, all three together.

**Confidence a naive long-the-beat trade has edge: 30/100.**

### Quant (opus)

Base rate (stated as assumptions, not measured facts): median 1-day post-earnings move for a
large-cap, low-beta P&C insurer ~1.5-2.0%; ~70% of outcomes inside ±3%; right tail (clean
beat+raise) +3% to +5%; left tail (adverse reserve/cat/investment miss) -5% to -8%, structurally
fatter than the right tail because bad news is balance-sheet news (reserves) that re-rates book
value, not just one quarter's EPS. A 4-quarter beat streak is public — beat #5 is roughly modal
expectation, carrying little marginal surprise value (expectations-treadmill asymmetry).

EV arithmetic — naive long-the-beat: P(headline beat) ≈ 0.75; P(up | beat) ≈ 0.62; P(up | miss) ≈
0.20 → P(up) ≈ 0.75×0.62 + 0.25×0.20 ≈ 0.52. E[up] ≈ +1.9%, E[down] ≈ -2.3% (fatter left tail).
Gross EV = 0.52×1.9 + 0.48×(-2.3) = 0.988 - 1.104 = **-0.12%**. Costs (spread/slippage ~0.08% +
gap-fill risk ~0.10%) → **net EV ≈ -0.30%**. Even charitable inputs (P(up)=0.58, symmetric
±2.1%) give gross +0.34%, net ≈ **+0.16%** — inside the ±0.5% own-parameter-error band.

Adverse-tail-to-edge ratio ≈ 20:1 or worse at |net EV| < 0.35% against a 6-8% left tail — fails
the no-trade filter outright, not a size-down candidate. No measured IV/expected-move data, so no
volatility mispricing claim can be made either (and a straddle would be out of mandate regardless).

**Recommendation: NO TRADE.** Confidence in the EV-ambiguity conclusion: 62/100.

---

## Round 2 — Rebuttal

### Bull rebuttal

Disagrees with bear's "table stakes = no drift" framing — a known catalyst with consistent
historical beats still generates pre-earnings positioning flows even when anticipated; that's the
mechanism, not a contradiction. Bear's qualitative risks are real but get resolved in the print,
not before it — the plan already scales exit around the reaction rather than betting blind.

Engaging the quant's EV math directly: pushes back that the -5%/-8% left tail is overstated for
AIG specifically — three years of de-risking (Corebridge separation, reinsurance actions) reduced
that tail. If the true left tail is -4%/-5% instead, EV flips positive even at P(up)=0.52.
**Concedes**: the parameter-uncertainty band (±0.5%) genuinely swamps a naive long-and-hold EV
calculation, and this isn't a 55-confidence "lean in" trade — it's a smaller/tighter-stop trade or
a wait-for-confirmation-post-print trade.

**Confidence: 55 → 44.**

### Bear rebuttal

Disagrees with both, and notes they cancel out in a way that should worry, not comfort. Vs. bull:
the real tail risk isn't an underwhelming beat, it's a qualitatively clean-looking beat hiding
adverse reserve development — a distinct, worse failure mode bull doesn't model at all, and bull
doesn't engage with cat-framing risk. Vs. quant: the EV math (net -0.30% base case, only +0.16%
charitable, inside ±0.5% error) reinforces bear's caution rather than undercutting it — describes
a coin flip with fee drag. Pushes back that quant's "adverse-tail-to-edge ~20:1" may be understated
for reserve development specifically: lower-frequency, higher-severity, clusters with book-value
re-rating that extends past day one.

Notes: all three, tellingly, agree nobody wants to be long into this print without a specific
information edge on reserves/buybacks/cat commentary that none of us has.

What would change my mind: same three conditions as R1, plus quant's EV turning clearly positive
(not parameter-ambiguous) paired with credible evidence the reserve overhang is a non-issue (e.g.
no casualty-line reserve strengthening in the last 2 quarters).

**Confidence: 30 → 25.**

### Quant rebuttal

Bull's "beat by enough" reframe is directional, not distributional — an unspecified conditional
does not move the prior. One input does move, the wrong way for bull: if 4 straight beats have
conditioned positioning, the beat is in the price and E[up] revises down 1.9% → 1.8% (holds
P(up)=0.52). Revised gross EV = 0.52(1.8) + 0.48(-2.4) = **-0.216%**, net ≈ **-0.42%** — worse, not
better.

On bear's qualitative risks: partly already priced into the generic -5%/-8% left tail, but bear
supplies the *mechanism* the quant's R1 tail asserted without proof — reserve charges re-rate book
value permanently vs. an EPS beat re-rating one quarter, and bear's four independent trigger
channels (reserves, cat framing, buyback pace, portfolio rate-sensitivity) raise P(tail) even
holding magnitude fixed. Widens E[down] 2.3% → 2.4%; notes the tail's left edge may extend past
-8% if reserve development and cat framing land together.

**Recommendation: NO TRADE, reinforced.** Adverse-tail-to-edge ratio worsens ~20:1 → ~26:1. Notes
bear and quant "disagree only on whether to express negative edge as a short" — declines: a
negative-EV long does not imply a positive-EV short; it implies no position.

**Confidence: 62 → 71.**

---

## Round 3 — Synthesis (opus)

### Hypothesis

**Statement:** AIG's Q2 2026 print (2026-08-06 AMC) is a well-telegraphed catalyst with no
identified information edge. The beat itself is table stakes — four consecutive beats and +6.6%
YoY consensus EPS growth are already in the USD 79.14 reference price — so a naive long expresses
no view beyond "the known thing happens." The variables that would actually move the stock
(magnitude of beat, long-tail casualty reserve development, buyback pace, cat-loss framing
mid-hurricane-season, investment-portfolio rate sensitivity) are unknowable pre-print, and are
asymmetric in kind, not just magnitude: an EPS beat re-rates one quarter, an adverse reserve
charge re-rates book value and persists past day one. The quant's EV work is negative and got
worse under rebuttal (gross -0.216%, net ≈ -0.42%, adverse-tail-to-edge ratio ≈ 26:1), and the
bull conceded down to 44 while admitting parameter uncertainty swamps the naive EV. All three
personas converge on the same operative sentence: nobody wants to be long without a specific
information edge on reserves, buybacks, or cat commentary — an edge this panel does not have.

**Direction:** no-trade
**Confidence:** 74

Applying the institutional lesson: the strongest unrebutted dissent (bear's clean-beat-hiding-
adverse-reserve-development failure mode) aligns with the quant's own EV math showing
negative-to-marginal edge, so this synthesizes to NO-TRADE rather than a quarter-size long.
Directional EV is at or below zero; the only structure that would express the panel's real view
(long volatility / defined-risk straddle around the print) is out of mandate, and the quant
explicitly rejected converting a negative-EV long into a short. No minimal directional position is
manufactured for the learning loop.

### Plan

**No position.** Nothing entered, nothing exited, no ticker action taken on AIG for the
2026-08-06 event.
- ticker: AIG (monitored only, not traded)
- action: none
- entry: none
- exit: none
- expected_profit_pct: 0.00

Conditions that would make this tradeable (for future revisit, not acted on now):
1. A quantified information edge on long-tail casualty reserve development ahead of the print.
2. A pre-announced buyback authorization increase / explicit capital-return step-up, converting
   the bull's "beat by enough" from an unspecified conditional into a distribution.
3. A defined-risk long-volatility structure being brought into mandate — the panel's real
   consensus is "wide distribution, unknown sign," a volatility view, not a directional one.
4. Post-print confirmation trading on 2026-08-07 once reserve/cat/buyback commentary is known —
   the bull's own fallback, and the only surviving path to a directional position, but a
   different, later setup not authorized here.

### Dissent

The single strongest unresolved disagreement is the direction and size of the left tail, and it
was never settled — asserted in opposite directions with no evidence adjudicating between them.

The bull argues the -5%/-8% left tail is overstated for AIG specifically: three years of
de-risking and the Corebridge separation have structurally shrunk the downside; if the true left
tail is -4%/-5%, EV flips positive even at P(up)=0.52. That is a real, load-bearing, falsifiable
claim — the no-trade verdict rests on a tail parameter, not a disputed fact.

The bear argues the opposite with equal force: the tail is understated, because reserve
development is low-frequency/high-severity, does not mean-revert within a day, and can hide
inside a headline that looks like a clean beat. The bull's Round 2 rebuttal never actually answers
this "good-looking beat, bad reserve triangle" scenario, nor engages with cat-loss framing for an
August print.

The quant sided with the bear on mechanism (reserve charges re-rate book value permanently vs. EPS
beats re-rating one quarter) and widened E[down] accordingly, raising its own confidence 62 → 71 —
but that is a reason the tail is asymmetric in kind, not a measurement of its width. Neither side
produced AIG's actual post-earnings return distribution, its prior-development history, or a
decomposition of the last four prints. The decisive number in the debate — the width of the left
tail — remains an assertion on both sides.

Confidence is 74, not higher, because the verdict is robust in sign (negative-to-zero EV under
every parameterization except the bull's most charitable one) but was resolved by declining to
take risk rather than by measuring the parameter. Post-mortem should test the bull's structural
claim against what actually prints 08-06/08-07 — specifically whether the realized move falls
inside -4%/-5% or extends past -5%/-8%, and whether any adverse development surfaces beneath a
headline beat.
