# Debate transcript: PTC Inc fiscal Q3 2026 earnings (2026-07-23-ptc-fiscal-q3-earnings)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Event: PTC reports fiscal Q3 2026 results after market close
Wednesday July 29, 2026.

Institutional lessons injected as context (general applicability, not PTC-specific):
1. Confidence <=45 with an un-hedgeable positive tail and net EV <2% against a
   ~7-8x adverse-tail ratio is a no-trade filter, not a size-down.
2. Discount post-earnings negative base rates when the name is already near its
   52-week low.
3. Set intraday exits at least 1 minute inside the session boundary (19:59:00Z not
   20:00:00Z) since 1-min-bar providers have no bar exactly at the close.
4. A catalyst already priced into a large run to 52-week highs above Street mean
   target should not be re-bet as a fresh gap trigger.
5. When the strongest dissent aligns with the quant's own EV math showing
   near-zero edge, synthesize to NO-TRADE.
6. Anchor entry prices to a live quote at the actual entry timestamp; validate
   against current price before filling.

Note on data integrity: `toa price PTC <ts> --provider twelvedata` returned HTTP 429
on every attempt across all three personas and both rounds (bull: 3 attempts,
bear: multiple, quant: 6 then a 7th on rebuttal) - a rate-limit ceiling, not a venue
coverage gap (PTC is a covered Nasdaq large-cap). All price figures below are
web-sourced and explicitly flagged as unverified where used.

---

## Round 1 — Independent research

### Bull (sonnet)

PTC price/news research was rate-limited on `toa price` (twelvedata HTTP 429 on
every attempt across three separate calls); the numbers below marked "web-sourced,
unverified via toa" are flagged as such.

**Why this moves the stock:**

1. The stock has been de-risked into the print, not run up into it. Web-sourced
   quote: PTC trading ~$123.54 (-2.35% intraday), down roughly 15% since March 31,
   2026, and sitting well below its 52-week high of $219.69 (implied 52-week range
   ~$108.50-$219.69). BMO cut its target from $231->$219, and even that reduced
   target implies ~75% upside from spot.
2. Last quarter's actual execution was strong, and the stock still sold off - a
   sentiment/multiple problem, not a fundamentals problem. Q2 FY26: non-GAAP EPS
   $2.69 vs ~$2.10 consensus, cc-ARR +8.5% YoY to $2.388B (high end of guide), FCF
   +14% YoY, and management raised FY revenue guidance to $2.58B-$2.82B and
   non-GAAP EPS guidance to $6.65-$8.90.
3. Fresh AI-platform catalysts are stacking up right into the print: June 10, 2026
   PTC unveiled PTC Orbit and PTC Jetstream plus a new AI platform, 12 new AI
   agents, 10 new integrations, and 100+ enhancements; July 14, 2026 PTC launched
   Onshape Labs. Management has guided to 14 new AI features in FY26 including its
   first fully AI-native product.
4. Binary, well-flagged catalyst with a clean historical base rate of large
   post-earnings moves - good risk/reward structure for a defined-window trade.

**Proposed action:** Long PTC (or a long-biased options structure - call/call
spread expiring the Friday after earnings). Entry during regular session July 29,
final hour before close (~19:00-19:30Z), anchored to a live twelvedata quote at
fill time (not obtained this round). Exit at 19:59:00Z July 30 (1 minute inside the
20:00Z close, per lesson #3). Instrument: common stock preferred for clean fill/exit
math; if options, short tenor only.

**Confidence: 55/100.** Real fundamentals-vs-price disconnect and stacked
AI-platform news flow, but capped because: (a) no toa-verified live price this
round; (b) Windchill CVE / "software budget rotating to AI infra" are real live
bear risks; (c) above the lesson-#1 no-trade threshold but not comfortably so.

Sources: [PTC IR - FQ3'26 date](https://investor.ptc.com/resources/news/news-details/2026/PTC-to-Announce-Fiscal-Q326-Results-on-Wednesday-July-29-2026/default.aspx),
[PTC Unveils a Wave of Product Innovations](https://www.ptc.com/en/news/2026/ptc-unveils-a-wave-of-product-innovations),
[PTC Launches Onshape Labs - gurufocus.com](https://www.gurufocus.com/news/8958172/ptc-launches-onshape-labs-to-integrate-ai-in-product-development),
[PTC Q2 2026 earnings beat forecasts, stock dips - investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-ptc-inc-q2-2026-earnings-beat-forecasts-stock-dips-93CH-4665973),
[PTC Q2 Earnings & Revenues Beat on AI-Led ARR Strength - Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/ptc-q2-earnings-revenues-beat-144900886.html),
[PTC Falls as Investors Weigh Upcoming Earnings - quiverquant.com](https://www.quiverquant.com/news/PTC+Falls+as+Investors+Weigh+Upcoming+Earnings+and+Ongoing+Software+Sector+Pressure),
[PTC Stock Forecast & Analyst Price Targets - stockanalysis.com](https://stockanalysis.com/stocks/ptc/forecast/)

### Bear (sonnet)

Still rate-limited on `toa price` (matches the known twelvedata-rate-limit pattern
- not a coverage gap, a request ceiling). Proceeding on cited web sources with the
live price explicitly flagged as an assumption.

**What's priced in / setup:** PTC is a broken-momentum name - down ~30.7% YTD and
~39.3% over the trailing year as of July 21, 2026, already ~31.8% below its 52-week
high by mid-2026. 52-week range cited at $133.38-$219.69 in one source; another
(post-selloff) puts spot near $114.75 against a 25-analyst average target of
$189.09 - a spread wide enough to flag the exact current quote as unverified.
Analyst sentiment is split: Citi cut its target by $11, BNP Paribas initiated at
Neutral with a $130 target, while others raised 2026 EPS estimates from $5.93 to
$8.40. This divergence signals the Street hasn't converged on what "good" looks
like Wednesday.

**Key red flag - the deferred-ARR mechanic:** On the Q2 call, management confirmed
the expected H2 growth step-up is "much more around the deferred ARR we already
have banked" rather than new bookings, and when pressed on whether underlying
new-business ARR (ex-deferred recognition) was flat YoY, the answer was
"Approximately." That is a company pulling forward already-signed backlog into
revenue recognition to hit a guide, while genuinely new demand generation stalls.
Q2 ARR growth of 8.5% (9% ex-IoT) beat guidance, but if that beat is substantially
deferred-revenue recognition rather than new logo/expansion activity, it's a
lower-quality beat the market may not keep rewarding a second consecutive quarter.

**Structural headwind - the divestiture:** PTC completed the divestiture of
Kepware and ThingWorx (its IoT stack) on March 13, 2026, narrowing the growth story
to core CAD/PLM plus the AI platform narrative - removing a business line that
flattered the "ex-IoT" growth math and raising the bar since the AI narrative now
has to carry the whole story alone.

**Valuation still not cheap despite the pullback:** Forward P/E estimates range
mid-20s to mid-40s depending on the EPS base used - not a build-in-the-worst-case
multiple.

**Specific risk:** Management repeats reliance on deferred-ARR recognition or
explicitly flags decelerating net-new ARR ex-backlog on the call - a very plausible
outcome given execs already conceded new business was "approximately" flat. A
repeat of "beat on backlog recognition, miss on new-business quality" (echoing the
Q2 reaction, where the stock fell ~6.2% post-earnings despite the beat) is a
specific, high-probability disconfirming path for any bull thesis.

**Institutional lesson check:** Lesson #2 (discount negative base rates near
52-week lows) cuts against a *fresh* short here, since much bad news may already be
reflected in the ~30-40% YTD decline - but it doesn't neutralize the deferred-ARR
and post-divestiture growth-concentration concerns, which are genuinely
not-yet-fully-tested risks into this specific print.

**Proposed action:** No fresh long entry into this print. Lean toward a small
tactical short / long-put structure only if implied move and options pricing offer
favorable asymmetry - not yet checked, toa rate-limited. Absent a verified live
quote, actionable recommendation is **NO-TRADE going into earnings**, or at most a
very small hedged short sized only after a live price/IV check clears.

**Confidence: 35/100.** Real, cited evidence of a bookings-quality problem
supports caution, but no verified current price, no options/IV check, and the
large YTD decline means much bad news may already be priced (working against a
fresh short). Given the un-hedgeable binary nature of an earnings gap and missing
live-price verification, this sits below the no-trade threshold for a confident
directional bet.

Sources: [Weiss Ratings](https://weissratings.com/en/instant-news-alerts/ptc-inc-ptc-down-6-2-time-to-execute-the-exit-plan),
[GuruFocus](https://www.gurufocus.com/news/8970358/ptc-inc-ptc-stock-down-32-now-undervalued-gf-score-81100),
[WallStreetZen](https://www.wallstreetzen.com/stocks/us/nasdaq/ptc/stock-forecast),
[SimplyWall.st](https://simplywall.st/community/narratives/us/software/nasdaq-ptc/ptc/vvpel1ib-ai-capabilities-and-nvidia-partnership-will-modernize-manufacturing-processes-r0bu/updates/19-analysts-have-trimmed-their-price-target-on-ptc-by-about-dollar11),
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/ptc-ptc-stock-sees-fair-211633976.html),
[SimplyWall.st - deferred ARR quote](https://simplywall.st/stocks/us/software/nasdaq-ptc/ptc/news/ptc-ptc-on-new-ai-and-partnership-moves-with-an-undervalued/amp),
[Investing.com - ARR/cash flow beat](https://www.investing.com/news/company-news/ptc-q2-2026-slides-arr-cash-flow-beat-guidance-amid-ai-push-93CH-4666029)

### Quant (opus)

**Data integrity flags:** `toa price PTC --provider twelvedata` failed with HTTP
429 on all six attempts (spaced retries across two dates, including a background
run) - no citable minute-bar anchor. Per lesson 6, any plan built on web quotes
must re-anchor to a live quote before filling and abort on divergence. Second flag:
web sources materially contradict each other on fiscal-quarter labels, trailing
52-week performance (-5.3% vs -30.8% vs -43.3% market-cap change), analyst mean
target ($177.50 vs $216.24), and even the sign of the May 6 reaction (+7.34%
after-hours per one source, -8% the next day per another). Only figures that
survive cross-source corroboration are used below.

**Price and range context** (corroborated by two independent sources, both
quoting $118.52):

| Metric | Value |
|---|---|
| Last (2026-07-24) | $118.52 (+4.84% on the day) |
| 52-week range | $108.50 - $219.69 |
| Position in range | ~9th percentile (9.2% above low, 46% below high) |
| Market cap | $13.69B |
| Beta | 0.99 |
| ADV | ~1.42M sh, ~$168M/day notional (liquid) |
| Forward P/E | 15.4 |
| Analyst mean target | $177.50-$216.24 - far above spot either way |

This is the inverse of "already-priced-in run to 52-week highs" (lesson #4);
PTC is at the *bottom* of its range with a Street target 50%+ above spot -
lesson #2 (discount the negative base rate near a 52-week low) applies.

**Base rate - and why it's weaker than it looks:** The beat rate is exceptional;
the reaction rate is not. Last eight quarters of EPS actual-vs-estimate: +6.2%,
+22.2%, +27.9%, +35.5%, +52.9%, +23.9%, +28.1% - **8 for 8, every one a beat, most
by >20%.** And the stock is down ~46% from its high. **A 100% beat rate has
produced a 46% drawdown.** PTC is not being traded on the print. Two sourced
reactions: Nov 5, 2025 - beat revenue and EPS, stock -1.1% on soft forward revenue
guidance. May 6, 2026 - EPS $2.69 vs $2.10 (+30.6%), revenue $774M (+8.5%), raised
FY guidance, and a $1.225-1.325B buyback - stock is -6% in the month since, with
consensus estimates cut -15.49% after the print.

Could not source a clean 8-quarter 1-day move distribution or PTC's current
options-implied earnings move.

- **Assumption A1:** conditional absolute 1-day move ~7% (from the two observed
  reactions plus the mid-cap enterprise-software 6-9% norm). Wide error bars.
- **Assumption A2:** downside conditional magnitude slightly larger (7.5% vs 7.0%),
  since the May episode showed an after-hours pop fully round-tripping.

**EV calculation:** Bull side: 8/8 beats, 9th-percentile range position, 15.4x
forward, targets 50% above spot, large buyback bid. Bear side: guidance - not the
print - is what has moved this stock the last two quarters, both times down;
estimates already cut 15%; the AI-platform catalysts are already announced and
already rejected by the tape - not a fresh gap trigger. These roughly offset:
P(up) = 0.52, P(down) = 0.48.

```
Gross EV: 0.52 x (+7.0%) + 0.48 x (-7.5%) = +0.04%
Costs (round trip): entry slippage/spread 0.05% + exit into gapped open 0.20%
  + commission/fees 0.02% = 0.27%
NET EV = +0.04% - 0.27% = -0.23%
```

Net EV is negative. Break-even probability: P(up) must exceed 53.6%; clearing a 2%
net-EV hurdle needs P(up) ~66% - nothing in the record supports that. Robust across
P(up) 0.45-0.60. Tail check: plausible worst gap ~-18%, plausible best ~+15%,
ratio ~1.2x - not the 7-8x adverse-tail case from the lesson library; this fails on
EV magnitude, not tail risk.

**Recommendation: ZERO, NO TRADE.** Sizing cannot rescue negative expectancy. If
the panel insists on expression: defined-risk options only, never naked equity over
the gap, and only with (a) an implied-move quote below the 7% assumption and (b) a
working live price anchor - neither obtained.

**Confidence: 62/100** (in the NO-TRADE recommendation, not a direction). Not
higher because: no citable entry anchor, unsourced move-magnitude assumption, no
implied vol, source contradictions on quarter labels/performance/targets. Not lower
because the core finding doesn't depend on any of the shaky inputs - gross EV
(+0.04%) is inside the noise of its own assumptions and turns negative on realistic
costs alone; independently, PTC has beaten estimates 8 consecutive times and lost
nearly half its value, and betting on beat #9 producing an up-gap bets on a
mechanism that has demonstrably stopped working.

Sources: [PTC IR - FQ3'26 date](https://investor.ptc.com/resources/news/news-details/2026/PTC-to-Announce-Fiscal-Q326-Results-on-Wednesday-July-29-2026/default.aspx),
[stockanalysis.com - price/range/cap](https://stockanalysis.com/stocks/ptc/),
[Investing.com - earnings history](https://www.investing.com/equities/ptc-earnings),
[Yahoo/Zacks - down 6% since last report, -15.5% estimate revision](https://finance.yahoo.com/markets/stocks/articles/why-ptc-inc-ptc-down-153013320.html),
[Barchart - Nov 5 -1.1%, preview](https://www.barchart.com/story/news/36923991/what-to-expect-from-ptc-inc-s-next-quarterly-earnings-report),
[ChartMill - FQ2'26 beat](https://www.chartmill.com/news/PTC/Chartmill-47389-PTC-Inc-NASDAQPTC-Shares-Surge-on-FQ2-2026-Earnings-Beat)

---

## Round 2 — Rebuttal

### Bull rebuttal

On the bear's deferred-ARR concern - taken seriously, not disqualifying. cc-ARR of
$2.388B is real, cash-collectable revenue regardless of composition; the FY
guidance raise happened after management had this deferred-vs-new-business
conversation on the same call, so raising guidance with full knowledge of the mix
is a data point in favor of durability, not against it - though the bull concedes
this is a weaker counter than it sounds. Wants Q3 to explicitly break out
new-logo/expansion/renewal ARR; absent that disclosure or with further
deceleration, would flip to no-trade.

On the quant's "trades on guidance, not the print" finding - the single strongest
point either persona made; changes sizing, not direction. Note the mechanism: PTC
has been punished on guidance, not the EPS beat itself. The AI-platform catalyst
case is explicitly a forward-guidance argument - designed to give management
something concrete to point to, the exact lever missing the last two prints. If
the AI narrative doesn't get quantified in guidance language, the base rate wins
again regardless of the beat.

On the EV math - no rebuttal, an assumption to fix. Wants the 7.0%/7.5% guess
replaced with real implied-vol data before backing any directional trade at any
size.

**What would change my mind (toward no-trade):** Q3 new-business ARR ex-deferred
continues flat-to-negative with no disclosure improvement; guidance commentary
vague/hedged on AI monetization; implied move turns out small (sub-5%), shrinking
room for a guidance-driven upside surprise to clear costs.

**What would strengthen the thesis:** verified live price near the 52-week low
combined with implied vol pricing in less downside than the 8/8-beat history
would suggest, plus Q3 disclosure isolating healthy new-logo/expansion ARR growth.

**Revised stance:** confidence lowered 55 -> 45; now agrees naked equity is the
wrong instrument - only a small, defined-risk call/call-spread contingent on a
real implied-move number would be defended, once toa is unblocked.

### Bear rebuttal

Quant's math supports the bear's case, doesn't sit neutral. "Trades on guidance,
not the print" is precisely the mechanism behind the bear's thesis: if the market
already discounts beats-that-aren't-clean, a Q3 beat propped up by banked deferred
ARR is the kind most likely to get sold, not bought. Quant's -0.23% net EV and the
May 6 precedent (beat +30.6% EPS, raised guidance, buyback - stock still -6% over
the next month) is a direct analog to what's expected if Q3 repeats the
H2-is-mostly-deferred-ARR story.

Bull's "beat-and-raise still sold off = macro/multiple compression, not
fundamentals" framing doesn't hold up against the transcript evidence: management
explicitly attributed H2 growth to already-banked deferred ARR and conceded
("approximately") new-business ARR ex-deferral was roughly flat YoY - that's not
macro noise, it's a specific, sourced, disclosed weakness. The bull's Round 1
leaned entirely on beat magnitude and AI-platform catalysts without engaging the
bookings-composition question at all.

**Where bull/quant do complicate the bear's case:** the ~9th-percentile 52-week
position and analyst targets far above spot represent a lot of already-priced-in
pessimism - lesson #2's discount against shorting near 52-week lows still applies
with force. If the sell-off already reflects the deferred-ARR concern, a fresh
short into earnings is chasing a story the market has largely absorbed - the
strongest thing keeping the bear from converting to an active short.

**What would change my mind:** a disclosed Q3 new-business/net-new ARR figure
showing re-acceleration ex-deferral -> neutral-to-bullish. Confirmation the
guide-raise embeds durable expansion/new-logo growth -> same direction.
Conversely, explicit Q3/Q4 guidance language repeating "much of the growth is from
ARR already on the books" -> hardens conviction for a small tactical short/put.

**Bottom line unchanged:** default NO-TRADE (aligned with quant's negative EV),
open to a small tactical short/long-put only if the print or options pricing
corroborates the bookings-quality red flag. **Confidence: 38/100** (up slightly -
quant's guidance-driven pattern reinforces the bear's mechanism, but the
already-depressed valuation argues against escalating size).

### Quant rebuttal

Price re-check attempted (`toa price PTC 2026-07-24T19:59:00Z --provider
twelvedata`) - HTTP 429 again, 7th consecutive failure. Still no citable anchor.

**Price discrepancy - flagged explicitly, material:** quant's $118.52 vs bull's
$123.54, gap = $5.02 = 4.23% - roughly 56-60% of one entire assumed event-day move,
and ~18x the modeled gross edge (+0.04%). Both cannot be right for the same
timestamp; neither is verified after seven 429s. A plan whose entry price is
ambiguous by 4.2% is unsimulatable - the P/L sign is determined by the anchor, not
the analysis. Secondary: the bull's "$219 target = ~75% upside" is
horizon-mismatched - a 12-month sell-side target contributes ~0.2%/trading-day of
drift if realized linearly, noise inside a ~24h window; don't let a 12-month number
underwrite a 1-day trade.

**Bear's deferred-ARR finding tightens the range, doesn't support a short:** to
justify a short, P(down) must rise from 0.48 to ~0.60, requiring a likelihood ratio
of (0.60/0.40)/(0.48/0.52) = 1.63. An LR of 1.63 from a management hedge-word on a
call held 12 weeks / ~55 trading sessions ago, already chewed over by sell-side?
No - the -15.49% post-print consensus estimate cut *is* the repricing of ARR
quality. Realistic LR ~1.1-1.2 -> P(down) ~0.51-0.53. Short EV at P(down)=0.52,
symmetric 7.25% move: gross = 0.52(7.25) - 0.48(7.25) = +0.29%, minus 0.27%
round-trip cost = **+0.02% net** - rounding, not an edge; 2% hurdle needs P(down)
~0.66. Worse, the short carries the wrong tail: shorting an 8/8-beat name at the
9th percentile with targets 50-85% above spot is selling a washed-out name into a
possible relief bid - conditional on bad news being priced, P(down) arguably goes
down, not up. **Net effect: P(up) range narrows from [0.45, 0.60] to [0.47, 0.56]**
- tightening around zero-EV, making NO-TRADE more robust, not less.

**Bull's AI catalysts: no change to move magnitude, plus a fiscal-calendar
error:** PTC's FY ends Sept 30, so fiscal Q3 = Apr-Jun. The June 10 AI platform
launch has ~3 weeks of possible in-quarter revenue contribution; Onshape Labs
(July 14) is fiscal Q4 and cannot appear in the Q3 print at all. These catalysts
can only enter through forward commentary - exactly the guidance channel where
this stock has repeatedly been punished; the bull's own best evidence reinforces
the regime rather than breaking it. Granting a quantified AI number in guidance and
widening to 7.5%/8.0%: gross = 0.52(7.5) - 0.48(8.0) = +0.06%, net = -0.21% -
essentially unchanged. Zero gross edge scaled by more vol is still zero.

**What both sides missed:** the actual T+1 return series for the last 8 earnings
prints - everything rests on an unsourced 7.0/7.5% move assumption. Structural
point: n=8, SE on a proportion ~ sqrt(0.25/8) = 17.7pp; break-even needs P(up) >
53.6%, but an 8-observation sample cannot distinguish 0.50 from 0.68 at any usable
confidence (n~780 needed to detect a 5pp edge at 80% power). Single-name
earnings-event direction betting is underpowered by construction - a general
argument for NO-TRADE as the default for this whole class of setup, not just PTC.

**What would change my mind (falsifiable, thresholded):** (1) a citable
options-implied move - if implied <=5.0% against realized median >=7% -> long
straddle/strangle (non-directional, doesn't require resolving bull/bear at all); if
implied >=10% against realized <=7% -> defined-risk short premium. (2) directional
short requires P(down) >= 0.60 - a negative pre-announcement, a hard third-party Q3
ARR datapoint, or a T+1 series showing >=6/8 down prints with median <=-4%. (3)
directional long requires the mirror image plus a resolved price anchor. (4) any
trade requires `toa price` to resolve - non-negotiable.

**Position: ZERO, NO TRADE, size 0 both directions. Confidence: 66/100** (up from
62) - the bear supplied a downside mechanism that turns out to be already priced
(tightening, not shifting, the range); the bull supplied only pre-print public
information that cannot enter the Q3 numbers; the price-anchor failure is now
confirmed seven times. Would flip to a long straddle on one verified input: an
implied move <=5%.

---

## Round 3 — Synthesis (opus)

**Where the debate actually converged:** all three personas ended in the same
place on action, differing only in reasoning and residual enthusiasm. Quant held
ZERO/NO-TRADE both directions and *raised* confidence 62 -> 66 - the highest-
confidence position in the debate, and the only one whose confidence moved toward
its own conclusion. Bull fell 55 -> 45, conceded the deferred-ARR flag was real,
conceded "trades on guidance not the print" was the strongest point made by
anyone, conceded the EV math needs real implied vol, and abandoned naked equity
entirely - retreating to a small defined-risk call spread contingent on
implied-move data that was never obtained (an unmet contingency is a no-trade).
Bear moved 35 -> 38 but never escalated to an active short, explicitly cautioning
against chasing an absorbed story at the 9th percentile with targets 50-85% above
spot. No persona ends the debate defending an executable directional position -
NO-TRADE by convergence, not tie-break.

**Why the substantive case fails:** the bear's deferred-ARR finding is the best
qualitative work in the debate and supplies a real mechanism for the
guidance-punishment regime the base rates show (8/8 EPS beats, stock -46% from
high; Nov 5 2025 beat-then--1.1% on soft guidance; May 6 2026 beat +30.6% + raise +
buyback, still -6% over the following month). But it's 12-week-old public
information already absorbed into a -15.49% consensus estimate cut and a
9th-percentile price. Quant's likelihood-ratio treatment is decisive: the LR needed
to move P(down) 0.48 -> 0.60 is 1.63; a realistic 1.1-1.2 yields P(down) ~0.51-0.53.
The effect of the debate's best insight is to *narrow* P(up) from [0.45, 0.60] to
[0.47, 0.56] - tightening around zero edge, strengthening NO-TRADE rather than
enabling a short. The bull's AI-catalyst leg was materially damaged by the
fiscal-calendar correction: PTC's FY ends Sept 30, FQ3 = Apr-Jun; the June 10
Orbit/Jetstream launch has ~3 weeks in-quarter and Onshape Labs (July 14) falls in
FQ4 and cannot appear in the print at all - the catalyst can only enter through
forward guidance, the exact channel that has punished this stock twice running.
Arithmetic across every variant offered: gross EV +0.04%, round-trip cost ~0.27%,
net EV ~-0.23%; widened distribution gives ~-0.21%; the short side nets only
~+0.02% and still misses the 2% hurdle (needs P(down) ~0.66). Break-even long needs
P(up) > 53.6%; the 2% hurdle needs ~66%. Nothing in three rounds supports either.

**The operational blocker (independent of thesis):** `toa price` returned HTTP 429
seven times across all three personas. The only price anchors are unverified web
quotes that disagree: $118.52 (quant, corroborated 2 sources) vs $123.54 (bull) - a
4.23% gap, ~18x the modeled gross edge. With edge this thin, the sign of the P/L is
decided by which unverifiable anchor you pick - disqualifying execution even if the
thesis had merit, and combined with no options-implied move, the bull's own
defined-risk structure cannot be priced and its stated precondition is unmet.
Quant's structural point generalizes beyond this name: n=8 earnings observations
has SE ~17.7pp and cannot distinguish P=0.50 from P=0.68 - single-name
earnings-direction betting is underpowered by construction, an argument for
NO-TRADE as the prior for this class of setup generally.

**Hypothesis:** direction none, confidence 72 (above quant's 66 because quant's
EV result is corroborated by the bull's abandonment of naked equity and the bear's
refusal to escalate to a short, and is reinforced by an operational blocker the
quant's EV model doesn't price).

**Plan:** NO TRADE. No position opened in either direction, in equity or options.
Conditions that would reopen the setup: a verified `toa price` anchor; an
options-implied move <=5% against a >=7% realized median (non-directional long-vol
structure); a hard new datapoint or 6/8+ down-print T+1 track record pushing
P(down) >= 0.60; post-print Q3 disclosure explicitly breaking out new-logo vs
expansion vs renewal ARR.

**Dissent (strongest unresolved disagreement):** whether the bear's deferred-ARR
finding is priced in - the debate had no way to settle it because nobody produced
the actual T+1 return series for the last 8 prints, no options-implied move was
found, and the price anchor itself failed verification seven times. Both sides are
arguing priors, not evidence. Secondary unresolved item: quant's n=8
statistical-power claim went uncontested by bull or bear and, if accepted, argues
for NO-TRADE as a strategy-level default for single-name earnings-direction bets,
not a per-name judgment call.

**Post-mortem watch items:** (a) if PTC moves sharply on July 30, verify whether
the move was attributable to the print or to guidance language, to test the
guidance-punishment regime claim; (b) log the `toa price` 429 as a repeated
infrastructure failure across debates (see project memory
`feedback_twelvedata_rate_limit_covered_ticker.md`) - escalating from an incident
to a systemic constraint; (c) record the fiscal-calendar error in the bull's
Round 1 as an avoidable research defect - fiscal-quarter boundaries should be
verified before any catalyst is assigned to a print.
