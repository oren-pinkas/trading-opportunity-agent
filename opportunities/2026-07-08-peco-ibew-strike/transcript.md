# Debate transcript — PECO/IBEW Local 614 strike (EXC)

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Context fetched before the debate:
- `toa lessons-relevant --type economic --tickers EXC` → 4 lessons on anchoring entries
  to live quotes, treating priced-in moves as faded, skipping trades with no
  executable positive-EV leg, and requiring a differentiated surprise vs. consensus.
- Live quote: EXC = $46.68 @ 2026-07-10T15:13Z
  (source: `https://api.twelvedata.com/time_series?symbol=EXC&interval=1min&date=2026-07-10&timezone=UTC`).

## Round 1 — independent research

### Bull (catalyst-hunter, sonnet)
Bottom line: the catalyst is dead. Web research found the strike actually ended
July 6/7, 2026 — a tentative agreement was reached, workers returned to the job
July 8/9 — three days before this dossier's stated impact window (2026-07-10).
Settlement: 5-year deal, 4%/4.5% raises for linemen/gas techs, 3%/yr for call-center
staff, restored cash-balance pensions, full retiree medical for newer hires — ordinary
terms, not a cost shock. EXC printed $47.28 flat on both Jul 7 and Jul 8 (no reaction
to the settlement news); today's $46.68 reads as routine drift, not strike-related.
Per lesson #4 (need a differentiated surprise vs. consensus to trade a known
development), there is none left. Floated a residual idea — a small, non-event
fundamentals long toward the ~$49 analyst mean target (5% gap, mid-52-week-range
valuation, tail-risk removed by the 5-yr deal) — but explicitly flagged it as weak
and not clearing the bar as an event trade.
Sources: [Inquirer Jul 4](https://www.inquirer.com/business/peco-strike-ibew-union-electricity-power-outage-20260704.html),
[Inquirer Jul 7](https://www.inquirer.com/business/peco-strike-linemen-call-center-workers-20260707.html),
[WHYY](https://whyy.org/articles/peco-strike-ends-tentative-agreement/),
[FOX 29](https://www.fox29.com/news/peco-worker-strike-ends-ibew-local-614-wins-pensions-retirement-medical-wage-hikes),
[NBC10](https://www.nbcphiladelphia.com/news/local/peco-and-union-reach-tentative-deal-to-end-strike-both-sides-say/4429279/),
[TIKR valuation](https://www.tikr.com/blog/exelon-stock-trades-at-48-is-wall-streets-49-target-missing-the-real-story).

### Bear (skeptic, sonnet)
Same core finding independently confirmed: strike settled Jul 6/7 (tentative
agreement), workers back Jul 8/9 — 2-3 sessions before the stated impact window.
EXC traded $46.54-$47.43 on Jul 9 (post-settlement session), squarely mid-range of
its 52-week band ($42.47-$50.65) — no discernible reaction, positive or negative.
Scale check: PECO's 1,600 strikers are ~7.8% of Exelon's ~20,571 group headcount,
across one of six distribution utilities; PECO itself said the settlement "will not
result in any immediate change to customer rates" — i.e. management confirms no
guidance risk. No sell-side analyst coverage found tying the strike to earnings; only
labor/local press covered it. Current EXC narrative is data-center demand growth, not
this strike. Recommends zero size / full pass. Only a fresh surprise (failed
ratification with real escalation, a rating-agency/PUC cost action, or unusual
EXC-specific divergence vs. utility peers) would change the call.
Sources: [Inquirer Jul 7](https://www.inquirer.com/business/peco-strike-linemen-call-center-workers-20260707.html),
[AFL-CIO](https://aflcio.org/2026/7/8/service-solidarity-spotlight-ibew-reaches-tentative-agreement-end-peco-strike),
[WHYY](https://whyy.org/articles/peco-strike-ends-tentative-agreement/),
[6abc](https://6abc.com/post/workers-expected-return-jobs-wednesday-tentative-deal-reached-end-peco-strike/19462945/),
[NBC10](https://www.nbcphiladelphia.com/news/local/peco-and-union-reach-tentative-deal-to-end-strike-both-sides-say/4429279/),
[Keystone Newsroom](https://keystonenewsroom.com/newsletter/archive/keystone-labor-report/peco-workers-win-wage-and-benefit-increases-after-historic-strike/),
[Philadelphia Weekly](https://philadelphiaweekly.com/peco-workers-head-back-after-historic-three-day-strike/),
[stockanalysis.com](https://stockanalysis.com/stocks/exc/).

### Quant (pragmatist, opus)
No live web access this round; worked from prior knowledge of Exelon's scale plus the
given live quote. Exelon ≈ $46-47B market cap, ~$22-23B revenue, ~19,000 employees;
PECO ≈ 15-20% of Exelon net income. A 1,600-worker strike at one segment, even a
prolonged one, plausibly costs $5-70M in incremental overtime/contractor spend —
under 2% of Exelon's consolidated net income and ~0.1% of market cap, often
rate-case-recoverable. Base rate: regulated-utility equities (low beta, rate/yield
driven) essentially never show idiosyncratic reaction to sub-segment labor strikes of
this scale. Scenario-weighted EV of a directional bet ≈ **-0.24%**, versus ~0.8-1.2%
daily realized vol — signal is ~1/4 of one day's noise. Recommendation: **no trade**,
size 0. Triggers to revisit: confirmed major outage/reliability failure, a PUC
prudence proceeding, a live gap >1-1.5% on strike news, or escalation to a
multi-month/$100M+ cost strike.

## Round 2 — rebuttal

### Bull
Fully concedes to **no trade**. Acknowledges the residual "value long toward $49"
idea isn't actually an event thesis — it's a generic regulated-utility valuation
argument that would be equally true on any day of the year and has no causal link to
the strike; keeping it in this debate would be borrowing catalyst-hunter framing to
justify an unrelated position. Found nothing bear/quant missed (ratification vote has
no scheduled date or real rejection-probability signal; no evidence of EXC decoupling
from utility peers). Converges fully with bear and quant.

### Bear
Rejects bull's residual long as out of scope: no timing, no causal link to the
settlement (stock was flat throughout, so there's no "overhang" to have been removed),
and it smuggles in an unrelated regulated-utility-valuation risk factor. On the
ratification vote: fails all three tests for a real catalyst — implausible rejection
odds (workers already back under agreed terms), nothing left to reprice against
(company already said no rate impact), and no clean, dateable reaction window. No
daylight versus quant's EV call — the flat tape (Jul 9: $46.54-47.43, no peer
divergence) corroborates the base-rate model rather than contradicting it.

### Quant
Reinforces and slightly *improves* (less negative) the EV once the tree is rebuilt
around a confirmed-resolved strike rather than an assumed-ongoing one: removing the
escalation/prolonged-strike tail also removes the downside variance. Revised EV ≈
**-0.12%** (near-zero dispersion, effectively zero risk-adjusted return) after
transaction costs and opportunity cost of capital. Rejects bull's residual long as
thesis drift outside this dossier's scope. Final call unchanged: **no trade**, size 0.

## Round 3 — synthesis

All three personas independently converged, and after rebuttal fully agree, on
**NO TRADE**. The stated event (an ongoing PECO strike as of the 2026-07-10 impact
window) had already resolved on 2026-07-06/07 — three days before the window — with
workers back on the job 2026-07-08/09 under an ordinary 5-year settlement. The market
had 2+ full sessions to react and did not: EXC traded mid-range within its 52-week
band both on the settlement day and since, with no analyst commentary tying the event
to earnings/guidance. Quant's base-rate/scale analysis (PECO ≈ 15-20% of Exelon
income, strikers ≈ 8% of group headcount, worst-case cost <2% of Exelon net income)
independently corroborates the flat tape. Bull's residual "value long to $49" was
unanimously rejected by round 2 (including by bull itself) as an unrelated,
un-timed thesis wearing this dossier's name tag — it belongs in its own opportunity
with its own catalyst, not here.

**Hypothesis:** No tradeable edge remains in this dossier. The strike is a resolved,
sub-material, already-priced non-event for a $46-47B regulated utility.
**Direction:** neutral. **Confidence:** 78 (high confidence in "no trade," not in a
directional call).

**Plan:** no action. ticker EXC, action none, no entry/exit, expected_profit_pct 0.

**Dissent:** none substantive survives Round 2 — bull's initial residual long was the
only points of daylight, and bull itself withdrew it as out-of-scope thesis drift
rather than a genuine disagreement about this event's tradeability. The one open
question all three flag: the union ratification vote has no announced date, so a
tail scenario (vote fails, strike resumes during continued heat-wave load) can't be
fully priced out — but all three agree it's not a differentiated, currently-tradeable
catalyst.
