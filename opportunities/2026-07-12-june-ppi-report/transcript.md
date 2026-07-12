# Research Debate Transcript — June PPI report due July 15

**Opportunity:** 2026-07-12-june-ppi-report
**Strategy:** three-round-panel (bull/bear sonnet, quant/synthesizer opus)
**Run:** 2026-07-12T23:17:45Z
**Disclaimer:** Paper-trading simulation only. Not financial advice.

Event: BLS releases the June 2026 Producer Price Index on 2026-07-15 8:30am ET
(2026-07-15T12:30Z), ahead of the July 29 FOMC decision. Tickers: SPY, TLT.
Simulation reference prices as of 2026-07-12T20:00Z: SPY = $85.08, TLT = $365.04
(internal sim-stub prices — not live real-world quotes).
Source: [BLS Schedule of Releases for the Producer Price Index](https://www.bls.gov/schedule/news_release/ppi.htm), accessed 2026-07-12.

Institutional lessons injected (via `toa lessons-relevant --type economic --tickers SPY,TLT`):
1. Anchor entry to a live pre-event quote, not the research-day price; re-derive or void if drift >0.5-1%. (2026-07-06, ISM mfg)
2. When the thesis is "catalyst reprices X higher" and X already rallied to its 52-week high pre-event, treat the move as priced-in — fade or shrink, don't chase. (2026-07-06, ISM mfg)
3. Skip trades whose only positive-EV path is a pre-market conditional entry the harness cannot fill. (2026-07-06, June jobs)
4. After a known regime shift, require a differentiated surprise vs. consensus before shorting duration into a data print — an in-line print is already in the curve and gets faded. (2026-07-06, June jobs)

---

## Round 1 — Independent opening positions

### Bull (sonnet) — confidence 55/100

June PPI is the last major inflation data point before the July 29 FOMC. Fed reaction
function is genuinely live to a hike, not a cut — CME FedWatch (via Investing.com Fed
Rate Monitor / MacroMicro FedWatch series, accessed 2026-07-12) prices ~70-75% hold at
3.50-3.75%, ~25-30% hike, ~0% cut. This is an active, unresolved hawkish regime, not a
stale one (distinguishing it from lesson #2/#4's "already-faded" concern).

Mechanism: May 2026 PPI (BLS) came in hot — final demand +1.1% MoM, +6.5% YoY, goods
+2.8% MoM. A sharp acceleration, not noise. If June extends the trend, it reinforces
"Fed can't cut, may hike" → TLT sells off, and equities are more likely to de-rate on
rate-shock in a hot-inflation regime than shrug it off. If June cools sharply, relief
rally in both. An in-line print is the least tradeable outcome (lesson #4).

Gap acknowledged: no specific Street/survey consensus estimate for the June print — a
real constraint on sizing the surprise.

**Proposed action:** Short TLT (or a short-dated slightly-OTM TLT put). Entry at the
live quote near close **2026-07-14T20:00:00Z** (day before print, anchored to the
actual close, re-derive size/target if drifted >0.5-1% from $365.04 per lesson #1).
Exit **2026-07-15T20:00:00Z** (same-day close, full session digestion — avoids the
pre-market fill problem in lesson #3). Void/flip immediately at the open if June PPI
undershoots May's pace materially.

### Bear (sonnet) — confidence 74/100 (in the bear case)

A "trade the PPI print" thesis on SPY/TLT is weak on its face. PPI is a second-tier
release in the Fed's reaction function — not part of the dual mandate directly, feeds
core PCE only partially and with a lag (June PCE won't print before July 29 FOMC), and
historically moves rates/equities less than CPI or the jobs report. Absent a large
surprise, SPY/TLT chop and mean-revert intra-session. With FOMC two weeks out, any
one-day repricing has ample time to be overwritten by more data before the Fed meets.

Sequencing issue: CPI for the same reference month typically releases before PPI, so
the market's primary inflation read has likely already happened by July 15 — PPI is
confirmatory, not a fresh catalyst, exactly the profile lesson #4 warns about ("an
in-line print is already in the curve and gets faded"). Gap acknowledged: doesn't have
the actual June CPI date/result in hand.

Additional evidence: mid-July is earnings season for SPY-index constituents — a
confound diluting any PPI-specific signal in SPY. No hard data on implied vol, PPI
consensus vs. whisper, or dealer positioning.

**Specific risks:** (a) in-line print → no reaction, position bleeds on time/opportunity
cost; (b) execution/timing — print lands 8:30am ET, well before cash open; if the plan
can only fill at/after 9:30am ET, the tradeable move has likely already reverted
(lessons #1/#3); (c) gap risk if entry is anchored to the 7/12 stub price rather than a
live 7/15 pre-print quote.

### Quant (opus) — verdict SKIP, confidence 82/100

**Base rates:** PPI is a second-order mover. Ranking by realized SPY reaction: CPI >
NFP > PPI. Typical same-day absolute SPY move on a PPI print ~0.2-0.4% vs. ~0.8-1.2%
for CPI, ~0.7-1.0% for NFP. TLT marginally more sensitive but still only ~0.3-0.6%
absent a surprise. Scenario probabilities (estimates, no live consensus/whisper in
hand): Hot 25% (SPY -0.5%, TLT -0.8%), In-line 50% (SPY ±0.15%, TLT ±0.2% noise), Cool
25% (SPY +0.4%, TLT +0.6%) — roughly symmetric, no directional edge without a
differentiated view (lesson #4).

**EV calc:** No options leg (cash SPY/TLT only) — a true straddle isn't constructible.
Long SPY open→close 7/15: EV = 0.25(-0.5%) + 0.5(0%) + 0.25(0.4%) = -0.025%, minus
~3bps costs → net ≈ **-0.055%**. Long TLT open→close: EV = 0.25(-0.8%) + 0.5(0%) +
0.25(0.6%) = -0.05%, minus ~5bps costs → net ≈ **-0.10%**. Both negative.

**Executable trade:** Print at 2026-07-15T12:30Z. Harness cannot fill pre-market
conditionals. Earliest executable entry = cash open **2026-07-15T13:30Z** (one hour
after the print — captures only residual drift, not the initial repricing). Exit =
same-day close **2026-07-15T20:00Z** or next open.

**Verdict: SKIP.** The only positive-EV path (front-running the 12:30Z print) is
precisely the unfillable pre-market leg — a textbook lesson-#3 void. Would flip to a
small directional bet only if bull/bear surface a concrete, differentiated
consensus-vs-whisper gap before Round 3.

---

## Round 2 — Rebuttals (each persona sees the other two's Round 1)

### Bull rebuttal — confidence 42/100 (down from 55)

Bear and quant's generic base rates (0.2-0.4% typical SPY move) don't account for the
conditional setup: May's print was already a +1.1% MoM/+6.5% YoY outlier with live hike
odds priced. But **concedes** bear's CPI-sequencing point as a real, unresolved hit —
a shared gap, not resolved in bull's favor.

On the day-before entry: **concedes**, with explicit intellectual honesty, that
entering 2026-07-14T20:00Z fixes the fill-mechanics problem (lesson #3) but does NOT
resolve quant's deeper point — bull has zero informational edge on the print outcome,
so this is an overnight event-risk bet on an unknown binary (a coin-flip with a
trend-following lean), not a high-conviction edge. Quant's symmetric-distribution /
negative-EV argument applies just as much to this entry as to a post-print one.

Would flip to skip if June CPI is confirmed to have already printed (making PPI fully
anticipated) or if consensus-vs-whisper numbers show low surprise probability.

### Bear rebuttal — confidence 78/100 (up from 74)

Bull's evidence doesn't move the needle: a hot May print without a June consensus
number is trend extrapolation, not a surprise thesis — surprise vs. consensus moves
markets, not level. Quant's base rates stand unrefuted.

The day-before entry is the **weakest** part of bull's case, not the strongest: it
deletes the information edge, converting an execution constraint into pure variance —
worse than a post-print entry, which at least captures directional confirmation before
committing capital.

Quant's negative-EV math reinforces bear's case as a second independent nail. Would
change mind given: (a) an actual June consensus figure showing a real whisper-number
gap, (b) confirmation June CPI already printed cool/in-line (making PPI the freshest
hawkish read), (c) a fill mechanism within the first 30 minutes post-print.

### Quant rebuttal — confidence 78/100 in SKIP (down from 82)

Night-before entry fixes the executability objection (credit given — the trade is now
constructible) but not the EV problem. Re-run on bull's short-TLT overnight structure:
EV = 0.25(+0.8%) + 0.5(0%) + 0.25(-0.6%) = +0.05% gross, minus ~5bps costs + ~1bp
overnight financing ≈ **-0.01% net** — essentially zero, with added overnight gap
variance for no premium. Symmetry, not entry timing, was always the real objection.

Grants a payoff-convexity point (in a live-hike regime, a hot surprise may move TLT
more than a symmetric cool surprise reverts) but this is a payoff skew, not a
probability skew — without a June consensus number the distribution's center can't be
located, so scenario probabilities stay 25/50/25.

Rates bear's CPI-sequencing point as the single strongest point raised in any round —
reinforces SKIP. Would flip to TAKE given: a consensus-vs-whisper gap, an options leg
to monetize the convexity, or a cheap implied move.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** June PPI is a second-tier catalyst with no locatable surprise vector —
no June consensus estimate exists to gauge surprise magnitude, only a hot May level to
trend-extrapolate from. The one positive-EV expression (a pre-print reaction leg) is
unfillable by the harness; the fillable expressions (cash-open-after-print or
day-before-close entry) are symmetric coin-flips that go net-negative after costs and
(for the overnight variant) financing.
Direction: **no-trade**. Confidence: **80/100**.

**Plan:** Skip. All three seats converged: quant's re-run puts short-TLT overnight at
≈-0.01% net (essentially zero, with added gap variance for no premium); long SPY/TLT
both negative after costs. Bull's own day-before entry fixes fill mechanics but, by his
own concession, deletes the information edge, leaving pure variance (bull confidence
fell 55→42). Nothing positive-EV is fillable; nothing fillable is positive-EV.

**Dissent (for the post-mortem):** The sharpest unresolved thread is the
**CPI-sequencing question** — rated by quant as the single strongest point in the
debate, conceded by bull as an unresolved shared gap. If same-month June CPI already
printed cool/in-line before July 15, PPI becomes the freshest hawkish data point ahead
of a live-hike FOMC (CME FedWatch ~25-30% hike / ~0% cut priced as of 2026-07-08) —
inverting it from "confirmatory/fade-prone" to a genuine catalyst. Nobody in the panel
had the June CPI date or result in hand. Secondary: quant granted a real
payoff-convexity skew (a hot TLT surprise plausibly moves price more than a symmetric
cool surprise reverts, in a live-hike regime) but no cash-only vehicle exists to harvest
it.

Evidence that would flip the verdict to TAKE: (a) a published June PPI consensus/whisper
number showing meaningful surprise probability; (b) confirmation June CPI already
printed cool/in-line; (c) an options leg or cheap implied move to monetize the
convexity; (d) a fill mechanism within ~30 minutes of the 12:30Z print.
