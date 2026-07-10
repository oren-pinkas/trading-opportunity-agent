# Debate transcript — RACE Q2 2026 earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Event:** Ferrari N.V. (NYSE/MTA: RACE) reports Q2 2026 Group results 2026-07-30 (per Ferrari's official FY2026 corporate calendar, SEC Form 6-K). Release/call historically precede the NYSE open (Q1'26 pattern: ~1:00-1:30 AM ET / ~7:00-7:30 AM CEST).
- **Strategy:** three-round-panel. **Personas/models:** bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus).
- **Spot anchor at research time (2026-07-10):** RACE ~$375 (7/9 close $375.03; range $370.98-$375.46); 52-week range $312.51-$519.10. Local `toa price` returned the offline stub ($423.86, `stub:deterministic`) — non-authoritative; persona targets used web-researched levels.
- **Platform constraint:** equity-only, buy/sell/short/no-trade, 1-minute bars 13:30Z-19:59Z. No options/vol structures executable.
- **Verdict:** NO-TRADE. direction=none, confidence=8.

---

## Round 1 — Independent research

### Bull (BUY, defined-risk, +6-10%)
- Order book extends to end-2027; FY2026 guidance (~€7.5B revenue, ~39% EBITDA margin) reaffirmed 2026-05-05 despite a deliberate delivery slowdown. [Ferrari corporate release](https://www.ferrari.com/en-EN/corporate/articles/2026-ferrari-first-quarter-results); [TIKR](https://www.tikr.com/blog/ferrari-q1-2026-e1-85b-revenue-as-order-book-extends-to-end-of-2027)
- Q1 2026: revenue ~€1.85B (beat ~€1.83B consensus), EBITDA €722M/39.1% margin; deliveries -4.4% to 3,436 units on deliberate changeover, not demand. [Investing.com transcript](https://ng.investing.com/news/stock-market-news/earnings-call-transcript-ferrari-beats-q1-2026-forecasts-stock-dips-93CH-2498707)
- Mix tailwind: F80 hypercar ramp (799 units, €3.6M) and new 12Cilindri Manuale (launched 2026-07-03, 1,499 units from €590k). BofA raised PT to $458 citing this; Morgan Stanley upgraded to Overweight, PT $438; UBS PT $497 (~6% Q2 order-book growth est.); Wolfe initiated Outperform 2026-07-07. [Benzinga](https://www.benzinga.com/news/26/07/60276279/ferrari-race-bofa-price-target-458-manual-v12-offsets-luce-ev)
- Stock ~28% below 52-week high ($519.10); consensus 11 Buy/3 Hold/0 Sell, median target ~$475. [aggregation]
- Tariffs largely pre-absorbed via US price hikes (up to 10%) on an affluent, price-inelastic client base. [Forbes](https://www.forbes.com/sites/neilwinton/2025/04/02/us-tariffs-wont-impact-ferrari-sales-profits-much/)
- Luce EV (unveiled 2026-05-25) drew design backlash but is "clocking up orders" per Electrek (unverified order data). [Electrek](https://electrek.co/2026/05/28/ferrari-luce-ceo-vigna-orders-despite-backlash/)
- Valuation flag: ~36.5x P/E vs ~25.6x luxury-peer average.
- **Action:** BUY via defined-risk call/call-spread (not naked long/short stock). Entry building 2026-07-27/29 pre-print, confirm gap direction in the first 15-30 min of NYSE trading 2026-07-30 before adding. Target +6-10% ($398-413), stretch to $438-475 over following weeks on an explicit raise. Exit same-day by 19:59Z for the reaction leg. Size ~1-2% equity or ~0.5-1% premium.
- **Unknowns:** exact Q2 consensus EPS/revenue not confirmed at research time; no verified historical earnings-day move size; Luce order volume unverified; valuation already stretched raises "sell the news" risk (echoing May 2026).

### Bear (no outright short; small defined-risk put spread or no-trade)
- Q1 2026 beat revenue/EPS yet shares fell ~4% because guidance was only reaffirmed, below buy-side whisper. [Motley Fool, "Ferrari Beat Estimates. So Why Is the Stock Down?"](https://www.fool.com/investing/2026/05/09/ferrari-beat-estimates-so-why-is-the-stock-down/)
- Unit deliveries -4.4% YoY — growth is entirely price/mix, not volume. [Substack, "Ferrari: The Scarcity Business"](https://longyield.substack.com/p/ferrari-the-scarcity-business-3436)
- EBIT margin slipped 60bps YoY to 29.7% (would be 30.9% ex-FX); full-year guidance floor is 29.5% — thin cushion. FX drag ~€200m guided for FY2026. [Alphastreet](https://news.alphastreet.com/ferrari-race-defends-39-1-ebitda-margin-and-confirms-2026-guidance-despite-middle-east-headwinds/)
- 25% US auto tariff a direct cost headwind in Ferrari's largest single market. [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/ferrari-q1-2026-earnings-beat-132427256.html)
- Analyst sentiment mixed at the margin: HSBC downgraded to Hold ("slow growth ahead"); BofA cut PT to $403.27 in a separate note. [Intellectia](https://intellectia.ai/news/stock/hsbc-downgrades-ferrari-race-to-hold-sees-slow-growth-ahead); [StreetInsider](https://www.streetinsider.com/Analyst+Comments/Ferrari+(RACE)+PT+Lowered+to+$403.27+at+BofA+Securities/26731912.html)
- P/E already de-rated to ~30-34x vs 3-10yr average 40-48x. [GuruFocus](https://www.gurufocus.com/term/pettm/RACE)
- Historical post-earnings pattern (bear's dataset): 19-quarter beat streak, average realized move only ~-0.7%, vs. options-implied ~4.2% (28.3% IV) — beats structurally not rewarded. [AskTraders](https://www.asktraders.com/analysis/ferrari-stock-race-under-pressure-with-earnings-on-deck-what-to-expect/)
- Countervailing facts acknowledged: order book extends to end-2027 with no abnormal cancellations; China now only 7% of deliveries (limited incremental downside); consensus still net bullish (11 Buy/3 Hold/0 Sell, median ~$475). [Seeking Alpha](https://seekingalpha.com/news/4586477-ferrari-confirms-full-year-guidance-as-order-book-extends-toward-end-of-2027-ahead-of-may-25)
- EV transition risk: Luce (first EV) drew backlash; second EV delayed to 2028 citing industry-wide weak demand for high-performance EVs. [Automotive World/Reuters](https://www.automotiveworld.com/articles/reuters-ferrari-delays-second-ev-to-2028-zero-demand/)
- **Action:** No outright short. At most a small defined-risk long put/put-spread (≤0.3-0.5% book) — never naked. Applying the institutional no-trade filter (confidence <=45, un-hedgeable positive tail, poor adverse-tail-to-edge ratio): confidence in a fresh incremental negative catalyst is only ~35-40%, and RACE has a demonstrated beat-driven squeeze history (+9% on Q4 2025) — default to NO-TRADE absent stronger evidence. Target if traded: -6 to -9% ($340-350). Exit same-day by 19:59Z.
- **Key unknowns:** whether Q2 guidance explicitly cuts the 29.5% EBIT floor; order intake/cancellation trends; tariff pass-through elasticity; FX path.

### Quant (short-vol preferred, not executable → conditional no-trade)
- Last 5 earnings-day realized moves (quant's dataset): Q1'26 -3.97% (beat+reaffirm, sold), Q4'25 +5% (beat+raise), Q3'25 +2.71% (miss, relief bounce), Q2'25 -10.81% (slight miss, violent), Q1'25 -3.5% (beat, sold). [OptionSlam](https://www.optionslam.com/earnings/straddle/RACE); [mlq.ai](https://mlq.ai/news/ferrari-reports-strong-2025-earnings-with-revenue-growth-and-raised-2026-outlook/); [Investing.com transcripts](https://www.investing.com/news/transcripts/earnings-call-transcript-ferrari-q2-2025-misses-forecasts-stock-dips-93CH-4163992)
- Directional base rate ~40% up / 60% down over the last 5 prints; mean |move| ~5.2%, median ~4%.
- Implied move for 2026-07-30: ~8% weekly (monthly 10.53%); May 2026 straddle buyers lost -20.45% (realized landed inside implied). [OptionSlam](https://www.optionslam.com/earnings/straddle/RACE)
- **EV:** directional edge ≈ +0.6% net (weakly bearish-leaning, variance-inclusive) — too weak/unreliable to trade directionally; naked short fails the risk filter given the un-hedgeable upside gap tail (Q4'25 +5%). Long-vol EV-negative (implied 8% > realized 5.2% → ~-2.8% gross).
- Preferred structure: short-volatility iron condor (short ~8%-wide strangle, long ~13% wings) — net EV ≈ +2% of spot, tail capped. **Not executable on this equity-only platform.**
- **Action (explicit fallback):** "if the harness can only trade equity on 1-min bars — NO-TRADE. There is no reliable directional equity edge... a naked short fails the risk filter." Size if anything: ≤0.25-0.5% book.
- **Key unknowns:** live option pricing/width (proxy used); whether harness can execute options at all; Q1'26 sign conflict (-3.97% close per OptionSlam vs. a reported +3.3% intraday figure) unresolved at Round 1; exact Q2 consensus EPS/revenue not yet pinned down; Milan (MTA) vs NYSE ADR / EUR-USD divergence on print day.

---

## Round 2 — Rebuttal

### Bull
- Disputes lumping miss-quarters into the base rate: strip the two miss-quarters (Q2'25, Q3'25) and it's 1 up (Q4'25, beat+raise, +5%) vs. 2 down (Q1'26/Q1'25, beat+reaffirm) — the real fork is raise-vs-reaffirm, not a generic coin flip.
- Q2 2026 has a richer catalyst stack than Q1: a fuller quarter of F80 contribution, Amalfi/849 Testarossa/296 Speciale ramping, and a fresh Wolfe Outperform initiation (2026-07-07, three days before this debate) — could nudge toward a "raise" outcome vs. Q1's reaffirm-only. Notes reports that Ferrari is deliberately pacing F80 deliveries "to optimize future financial results," i.e. the -4.4% unit decline is partly a scarcity/margin-management choice, not pure demand softness. [ItalPassion](https://www.italpassion.fr/en/ferrari/ferrari-may-reduce-f80-delivery-rate-to-optimize-future-financial-results/)
- **Concedes:** Q1 2026 (beat+reaffirm+sold ~4%) is the most relevant comp and is bad for bulls; implied move (8%) rich vs realized (5.2%) means any position must be small; the 5-quarter base rate does lean bearish (3-of-5 down) and n=5 is noisy; margin compression/-4.4% deliveries are real and could worsen.
- **Revised action:** BUY, but momentum-confirmation entry only — enter within the 13:30Z-19:59Z window after the first few 1-min bars confirm a positive reaction with rising volume; don't chase if the tape opens flat/down. Target +4-6% (down from +6-10%), tight stop ~-2%, exit same session, size 0.5-1% (down from 1-2%).
- **Stands down entirely if:** guidance explicitly lowers the 29.5% EBIT floor; order-book deceleration/cancellations surface; first-bar tape is flat/negative despite a beat; no clean beat.

### Bear
- 12Cilindri Manuale launched 2026-07-03, *after* Q2 close (June 30) — zero Q2 revenue impact, pure forward narrative, not a Q2 catalyst.
- Luce backlash coincided with a reported ~8% share drop around the launch event — a market-verified reaction, not just aesthetic sentiment. [EVTech.News](https://evtech.news/news/ferrari-luce-ev-backlash-2026-ferraris-first-electric-car-faces-criticism.html); [Simply Wall St](https://simplywall.st/stocks/us/automobiles/nyse-race/ferrari/news/ferrari-luce-backlash-puts-ev-design-and-brand-power-to-test)
- Wide analyst target dispersion ($382-497, ~30% spread) signals lack of conviction, not bullish alignment.
- Pushes back on quant's "symmetric" tail framing: actual downside prints (-10.81%, -3.97%, -3.5%) are all larger in magnitude than upside prints (+5%, +2.71%) — skew is downside-heavy even if the base-rate count is contested.
- **Concedes:** order book to end-2027 is the hardest fact for the bear case to overcome; consensus is genuinely net bullish; Ferrari's pricing power is plausible; the stock already being ~28% off its high reduces (does not eliminate) correction risk; mean move (~5.2%) / median (~4%) argues against oversizing a "crash" thesis.
- **Revised action:** default NO-TRADE pre-print. Conditional tactical short only if the post-open (13:30Z) tape confirms ≥2-3% gap down with an opening-range-low break on volume, or explicit negative fundamentals surface live (guidance cut, miss, weak Luce commentary). Target -4 to -6% (not the -10.81% tail), tight stop at opening-range high, exit by 19:59Z, size 0.25-0.5%.
- **Flips to an active pre-print short only on:** pre-print delivery/unit-miss evidence, a tariff-cost guidance cut, verified (non-Electrek) Luce cancellation data, a credible sell-side EPS/revenue cut pre-print, or insider-selling clusters.

### Quant
- Verified two facts: (1) the Q1'26 sign conflict resolves in the **bear's favor** — Ferrari beat both lines and reaffirmed guidance, yet closed down ~3.5-4% ("Ferrari slides 3.5% after Q1 results"); the "+3.3% intraday" figure appears to be a transient pre-market/pop artifact, not the settled close. [QuiverQuant](https://www.quiverquant.com/news/Ferrari+slides+3.5%25+after+Q1+results+as+investors+digest+deliveries,+FX+headwinds,+and+unchanged+outlook) (2) Q2 2026 consensus ≈ $2.30 EPS / ≈$1.95B revenue — sequential revenue growth is expected despite the deliberate delivery slowdown, so any beat is structurally a mix/margin story, the same "quality beat" type the market sold in Q1.
- Disagrees with bull: the pre-print upgrade cluster is a contra-indicator, not a bullish signal — it raises the bar the print must clear, mirroring the exact mechanism behind the Q1 -4% reaction; "tariffs absorbed" and "order book" are old, already-priced-in news, not incremental catalysts; at 36.5x P/E the bull needs an explicit raise, not a reaffirm, to justify a same-day pop.
- Disagrees with bear: the "~-0.7% avg realized vs ~4.2% implied" framing is a variance/vol-premium observation being misused as a directional claim; n=3-4 has enormous standard error; reconciles the quant-vs-bear historical discrepancy as small-sample noise (post-earnings reaction autocorrelation ~0 for luxury names quarter to quarter).
- **Concedes:** the Round 1 preferred short-vol structure is a category error once forced into linear equity — stripping the capping wings converts a bounded variance harvest into an unbounded directional bet; concedes the un-hedgeable short tail alone disqualifies an outright short regardless of point-estimate EV.
- **Explicit EV table:** gross short EV ≈ 0% (P(down)≈0.53 × -4.0% avg-down vs. P(up)≈0.47 × +4.5% avg-up ≈ cancel); net short EV after realistic 1-min-bar slippage/costs/borrow ≈ -0.2% to -0.4%. A buy is symmetric — gross ≈0, net also negative given costs and no volume-surprise room. **Linear-equity directional EV is negative both ways.**
- **Final:** NO-TRADE on RACE equity into the print, pre-print, full stop. Conditional PEAD-style flip after the gap only: SHORT if post-13:30Z gap down >2% + a hard fundamental trigger (EBIT margin at/through 29.5% floor, delivery/FX guidance shave) — enter on first 1-min bar failing to reclaim opening-range high, target -6 to -8% ($345-353), stop above ORH (~1.2-1.5% risk), flat by 19:59Z, size ≤1%. LONG only on a genuine guidance raise with gap up >2% holding opening-range low through the first 15 min — target +4-5%, stop under ORL, flat by 19:59Z, size ≤1%. Absent a >2% directional gap with a fundamental trigger: stay flat all session.

---

## Round 3 — Synthesis (NO-TRADE, confidence 8)

**Hypothesis:** All three personas independently converged on no reliable pre-print directional edge. The bull abandoned a static long for a momentum-confirmation entry; the bear defaulted to no-trade absent a live trigger; the quant showed linear-equity EV is negative in both directions (gross ≈0%, net ≈-0.2% to -0.4% after costs) because the only genuine edge — short volatility — is inexpressible on this equity-only platform. The dominant structural fact is a "quality beat" setup: at ~36.5x P/E with a fresh pre-print upgrade cluster raising the bar, and Q1'26's beat-and-reaffirm-then-sell-4% as the tightest comp, a mere reaffirm likely sells the news while only an explicit guidance raise justifies a pop — and the un-hedgeable beat-driven squeeze tail (Q4'25 +5%) disqualifies a naked short on the risk filter alone. The only live disagreement is what happens *after* the market reacts, which is conditional logic the flat plan schema cannot encode.

**Plan:** RACE, no-trade. (If traded reactively — not encodable in the schema — all three personas converged on entering only after a confirmed post-13:30Z gap + fundamental trigger, flat by 19:59Z.) expected_profit_pct = 0.

**Dissent:** Post-reaction directional skew — bear sees a downside-heavy tail (all historical down-moves exceed up-moves in magnitude, and reaffirm-not-raise "quality beats" sell); quant sees effectively symmetric tails with ~0 autocorrelation, making the print a coin flip whose only exploitable feature is variance; bull sees the richer Q2 catalyst stack (F80/Amalfi/849/296 ramp) as capable of flipping the fork toward a raise and an upside gap. Testable post-mortem: (1) reaffirm vs. raise, and did the 29.5% EBIT floor hold; (2) realized same-day close direction and magnitude vs. the ~8% implied straddle; (3) did day-1 direction persist (PEAD) or mean-revert into day 2-3.
