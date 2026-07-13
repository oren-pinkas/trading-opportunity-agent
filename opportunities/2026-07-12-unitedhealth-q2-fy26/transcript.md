# Research Debate Transcript — UNH Q2 2026 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` | Personas: bull (sonnet), bear (sonnet), quant (opus) | Synthesizer: opus
Run date: 2026-07-13 | Event: UNH reports Q2 2026 earnings 2026-07-16 pre-market
Reference price: $424.12 (close 2026-07-10T19:00Z, last session before this weekend)

Relevant institutional lessons injected (general earnings-trade discipline, `toa lessons-relevant --type earnings --tickers UNH`):
- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express via defined-risk options, never a naked short. (NKE, 2026-07-06)
- Discount post-earnings negative base rates when the name is already at/near its 52-week low. (NKE, 2026-07-06)
- Set intraday exits at least one minute inside the session boundary (19:59:00Z, not 20:00:00Z). (TSLA, 2026-07-06)
- A catalyst that already drove a large multi-week run to a 52-week high is priced in — don't re-bet it as a fresh trigger. (DAL, 2026-07-12)
- When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size directional position. (DAL, 2026-07-12)
- When the highest-confidence panelist says directional EV is ~0 and the only positive-EV structure is out of mandate, log NO TRADE. (LEVI, 2026-07-12)
- Anchor entry prices to a live quote fetched at the actual entry timestamp, not a stale pre-move reference. (LEVI, 2026-07-12)

---

## Round 1 — Independent Research

### Bull (opening)

Bull's read: UNH's stock reaction is driven by guidance, not just the beat. Jan 27 2026 Q4'25 print fell -14.6% vs 5.5% implied (FY26 guide read as too cautious). Apr 21 2026 Q1'26 print jumped +10.5% vs 5.4% implied (EPS beat ~9.7% ahead of consensus, FY26 guide raised to >$18.25 adj EPS, 30% cut to prior-auth requirements). Stock +33%/90d, +20%/30d, ~$424, 2.3% below 52-wk high $434.30. Q1'26 MCR 83.9%, down 90bps YoY. FY26 guide 88.8%±50bps is a normal seasonal step-up (Q1 always seasonally lowest MCR). Optum margin guided to ~5.1% from 3.5%; MA margin to ~7.5% from 6.2%. Morgan Stanley raised PT $453→$468 days before print; consensus Strong Buy (19/3/1); average Street target ~$397-413 (argued as room to re-rate as analysts catch up). Consensus Q2 adj EPS ~$4.84 (+18.6% YoY), revenue ~$110.9-111B. Implied move 6.1-6.6%, IV30 38.37 above median; stock exceeded implied move in 4/8 last prints. DOJ investigation called "year-old overhang already absorbed," not a fresh catalyst.

Sources: [Hudson Labs Q2 2026 Preview](https://www.hudson-labs.com/research/unitedhealth-group-unh-q2-2026-earnings-preview), [BusinessWire/Nasdaq FY26 outlook](https://www.nasdaq.com/press-release/unitedhealth-group-reports-2025-results-and-issues-2026-outlook-2026-01-27), [ad-hoc-news.de Q1 2026 beat](https://www.ad-hoc-news.de/boerse/news/ueberblick/unitedhealth-group-stock-us91324p1021-q1-2026-earnings-beat-and-outlook/69369364), [Investing.com implied move](https://www.investing.com/news/stock-market-news/unitedhealth-shares-may-move-61-on-july-16-earnings-report-93CH-4784480), [Healthcare Dive DOJ probe](https://www.healthcaredive.com/news/unitedhealth-grassley-medicare-advantage-investigation/809377/), [ainvest.com MA bid strategy](https://www.ainvest.com/news/unitedhealth-2026-medicare-bids-signal-turnaround-healthcare-giant-2505/)

Proposed (R1): Long via bull call debit spread (~5% OTM long / ~12-15% OTM short) + small core equity sized to survive full adverse move. Entry Mon 7/13-Wed 7/15 close (live quote, not stale reference). Targets: retest $434.30 then $450-460. Stop below $410. Exit by 19:59:00Z.

**Confidence: 58/100**

### Bear (opening)

Bear's read: the entire re-rating rests on ONE fundamental (MCR normalizing) that already drove the stock from a $234.60 low (Mar 2026) to near its 52-wk high — a catalyst that already drove a big run into a high is priced in, not a fresh trigger. Pre-print PT hikes (MS $468, Bernstein $492) and 71% prediction-market beat odds mean the "surprise" is already consensus → reaction skews sell-the-news on anything short of a blowout. Mechanical risk: FY26 MCR guide 88.8%±50bps with H1 >250bps below full-year midpoint; consensus Q2 EPS quoted at $4.54, down 27.7% QoQ from Q1's $6.28 — optically weak even under the "good" scenario. Options imply 6.1-6.63% move; stock blew through implied in 4/8 prints including -14.6% Jan 27 2026 vs 5.5% implied. Peer read-through double-edged: Humana FY26 EPS guidance collapsed 47%, Elevance posted a benefit-ratio segment loss — sector cost pressure hasn't disappeared, "we're different" already disproven once. Unresolved DOJ criminal/civil MA-upcoding investigation plus a new May 2026 Massachusetts suit (>$100M fraudulent Medicaid overbilling) — binary, un-hedgeable tail that could surface via call commentary.

Sources: [Hudson Labs Q2 2026 Preview](https://www.hudson-labs.com/research/unitedhealth-group-unh-q2-2026-earnings-preview), [TIKR — fallen 54% from high](https://www.tikr.com/blog/unitedhealth-has-fallen-54-from-its-high-is-2026-finally-the-turning-point), [TIKR — DOJ problem](https://www.tikr.com/blog/unitedhealths-doj-problem-isnt-going-away-neither-is-the-16-billion-in-free-cash-flow), [Yahoo Finance DOJ](https://finance.yahoo.com/news/unitedhealth-under-doj-investigation-buy-110002685.html), [247wallst.com](https://247wallst.com/investing/2026/07/10/the-main-reason-behind-buying-unitedhealth-before-july-16/), [Investing.com MS PT raise](https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-unitedhealth-stock-price-target-on-utilization-93CH-4767498), [ad-hoc-news.de Q1'26 52-wk high](https://www.ad-hoc-news.de/boerse/news/ueberblick/unitedhealth-group-stock-us91324p1021-q1-2026-earnings-beat-pushes/69344519), [Investing.com implied move](https://www.investing.com/news/stock-market-news/unitedhealth-shares-may-move-61-on-july-16-earnings-report-93CH-4784480), [optionslam.com straddle history](https://www.optionslam.com/earnings/straddle/UNH), [stockanalysis.com forecast](https://stockanalysis.com/stocks/unh/forecast/)

Proposed (R1): Not a high-conviction naked short; small defined-risk put debit spread (~5-7% OTM) if forced, or NO TRADE if the quant's EV comes back near zero.

**Confidence: 35/100** standalone bear thesis; **~75/100** confidence that fresh-long risk/reward is poor.

### Quant (opening)

Base rate: violent gaps — Jan 27 2026 -14.6% (vs 5.5% implied), Apr 21 2026 (Q1'26) ~+7%, Jul 29 2025 (Q2'25) ~-7%, Apr 17 2025 ~-20%. Average absolute move ~10-12%, well above a normal mega-cap. Implied move for July 16 ~6.1-6.6%, IV30 ~38 above median; UNH exceeded implied move in 4/8 prints — coin flip on the vol trade. Consensus EPS $4.84 (+18.6% YoY); Strong Buy; MS PT $468; prediction markets ~71% beat probability. Stock $424.62 (Jul 10), within 2.3% of 52-wk high $434.30, +80% off Aug 2025 low — turnaround largely priced in near the 52-wk high.

P(up)=0.55, P(down)=0.45, downside fatter (avg up 6.5%, avg down 7.5%) given near-high positioning + tail history.

EV_gross = 0.55×6.5% − 0.45×7.5% = +0.20%. Costs/slippage ~0.5% round-trip. EV_net ≈ −0.3%. Directional EV ~0 before costs, negative after. Adverse-tail-to-edge ratio ~7-8x — textbook no-trade filter. Vol play (straddle) also no edge: 6.1% implied already elevated, UNH clears implied only ~50% of the time.

Sources: [Investing.com implied move](https://www.investing.com/news/stock-market-news/unitedhealth-shares-may-move-61-on-july-16-earnings-report-93CH-4784480), [OptionsLam UNH](https://www.optionslam.com/earnings/stocks/UNH), [CNBC Q2'25 report](https://www.cnbc.com/2025/07/29/unitedhealth-group-unh-earnings-report-q2-2025.html), [Simply Wall St Q1'26](https://simplywall.st/stocks/us/healthcare/nyse-unh/unitedhealth-group/news/unitedhealth-group-unh-valuation-check-after-strong-q1-2026), [Yahoo Q2 preview](https://finance.yahoo.com/healthcare/articles/expect-unitedhealth-groups-q2-2026-093554304.html), [stockanalysis.com](https://stockanalysis.com/stocks/unh/), [247wallst.com](https://247wallst.com/investing/2026/07/10/the-main-reason-behind-buying-unitedhealth-before-july-16/)

Proposed (R1): Leans NO TRADE. If forced, the only defensible expression is a small defined-risk bullish call spread riding the beat base rate.

**Confidence: 35/100**

---

## Round 2 — Rebuttal

### Bull (rebuttal)

Disagrees with bear's "priced in" framing: the last time this exact setup occurred (Q1'26 print), the stock still moved +7% on the print itself — not a sell-the-news reversal — so the MCR-normalization thesis wasn't fully discounted then either. Backloaded EPS is guided seasonality, not fresh risk. Peer read-through is selectively applied: UNH's Optum segment (health services + Rx, ~half of earnings) is structurally less correlated to MA MCR swings than Humana (pure-play MA) or Elevance (ACA/Medicaid-weighted) — the segment-mix difference is real. DOJ overhang is old/slow-moving; the Massachusetts suit is immaterial (~$100M vs ~$30B+ annual profit) absent a NEW indictment timed to the call. Partially concedes the quant's EV math and fat-tail point, but notes a call debit spread caps downside regardless of tail size, and the 7.5% avg-down figure is skewed by two outlier prints while a right tail (+7%, +10.5%) exists in the same sample.

What would change mind: new DOJ charges/new state suit at print; MCR >89.3%; guidance reiterated-not-raised; heavy OTM put skew pre-print.

Revised (R2): Long but smaller/more defensive — bullish call debit spread ~5% OTM long/~10-12% OTM short, max loss = premium. Entry July 15 close or July 16 pre-market (not earlier). Exit within 1-2 sessions post-print regardless of direction; don't hold through DOJ-related call commentary.

**Confidence: 45/100** (down from 58)

### Bear (rebuttal)

Disagrees with bull: analyst targets below spot means the sell-side hasn't validated the move, not a coiled spring; MS/Bernstein PT hikes days before the print are crowded-momentum markers, not fresh catalysts — a classic sell-the-news setup after an +80%-off-lows run. The MCR "normal seasonal step-up" argument is too clean: a ~490bp sequential step is large even by UNH's own pattern, and Jan's -14.6% was specifically triggered by the market re-pricing a "too cautious" guide once already; the 30% prior-auth cut carries real utilization-uptick risk the bull never quantifies. DOJ dismissal is unearned — it doesn't address the NEW May 2026 Massachusetts suit.

On the quant: agrees EV_net≈-0.3%/no directional edge, but reframes the tail — 3 of the last 4 prints were down, and the two largest moves (-14.6%, -20%) are BOTH downside, not a symmetric distribution but a negatively skewed one sitting at 97.7% of the 52-wk high, where negative skew resolves violently (more stacked long profit to unwind than short-covering fuel). Argues the quant's "if forced, take the bull call spread" concedes directional bias without justification — the driver of the last two double-digit gaps was MCR/guide commentary, not the EPS beat itself.

What would change mind: signal FY26 MCR guide walked to the low end or held flat; confirmation prior-auth relaxation hasn't shown up in early-Q2 utilization; broad risk-on tape.

Revised (R2): Bearish tilt / defined-risk short, not outright long, not fully flat. Put debit spread ~5% OTM long/~12-15% OTM short (mirrors bull's structure inverted). Entry Wed 7/15 close. Targets $390-400 (disappoint), stretch $360-370 (repeat of -14.6%/-20% tail). Max loss if stock holds above $434.30. Exit by 19:59:00Z day-of.

**Confidence: 40/100**

### Quant (rebuttal)

Corrects the bull: "Street targets below spot" is BEARISH (stock trading above consensus fair value), not bullish room-to-run — the bull has the sign backwards. Fresh PT hikes into the print mark local sentiment tops, not tailwinds. Corrects the bull's DOJ dismissal: the 2025 crash absorbed the existence of the investigation, not the NEW May 2026 Massachusetts suit.

Corrects the bear: the QoQ EPS-decline optics argument is a sentiment assertion, not a quantifiable edge — if real, it would already be in the 6.3% implied. The bear's proposed put debit spread is ALSO negative EV: it fights both rich IV (IV30 38.37 above median) AND the 71% beat odds simultaneously.

Flags an unresolved input both sides skated past: consensus Q2 adj EPS quoted as $4.84 (bull) vs $4.54 (bear) — a ~7% gap, likely adjusted-vs-reported/estimate-vintage drift, not reconciled by either side, and it materially changes the beat/miss bar.

Reaction-distribution estimate: big up >8% ~20%, mod up ~20%, flat ~20%, mod down ~22%, big down >8% ~18%. Mean reaction ≈ -0.5% to -1%. EV checks: fresh long/call spread = negative EV, reject. Bear's put debit spread (~$402 long/~$374 short, ~$6.5 debit): ~13% full profit/~17% partial/~70% worthless, EV ≈ -$0.4/share, slightly negative against rich IV. No trade: EV=0, wins by default.

Revised (R2): Primary = NO TRADE (both directional structures price negative-to-breakeven against rich IV). Contingent: IF spot pushes to a fresh 52-wk high into 7/15 close AND put skew richens vs upside, take a small (≤0.5% risk budget) put debit spread ~5% OTM long/~12% OTM short, exit by 19:59:00Z reaction day.

**Confidence: ~70/100** that a fresh long is poor R/R; **~40/100** on an actual bearish bet; net conviction to act directionally is LOW.

---

## Round 3 — Synthesis

### Hypothesis
UNH enters its July 16 print sitting at ~97.7% of its 52-week high after an +80%-off-lows run, with the MCR-normalization thesis that fueled that run largely priced in. All three personas independently converged toward caution (bull 58→45, bear 35→40, quant "leans no-trade"→~70/100 that a fresh long is poor R/R). The quant's reaction distribution centers on a mean of roughly -0.5% to -1% with a fat, negatively-skewed downside tail, while implied vol (IV30 ~38, ~6.1-6.6% implied move) is rich and beat odds (~71%) are already consensus. Both directional structures (bull call spread, bear put spread) price out negative-to-breakeven against that rich IV. There is no positive-expectancy expression; the edge does not clear costs or the adverse-tail-to-edge ratio (~7-8x).

- **Direction:** no_trade
- **Confidence:** 68/100 (confidence in the no-trade verdict itself; directional conviction in either direction is low by construction)

### Plan
- **Ticker:** UNH
- **Action:** no_trade
- **Entry:** none
- **Exit:** none
- **Expected profit:** 0% (flat). Both live directional structures modeled negative EV: fresh long/call spread negative after ~0.5% round-trip costs; put debit spread (~$402 long/~$374 short, ~$6.5 debit) EV ≈ -$0.4/share against rich IV.

**Contingent triggers (must resolve before 2026-07-15 close):**
- Toward a small defined-risk SHORT (put debit spread, ≤0.5% risk budget, ~5% OTM long/~12% OTM short, exit by 2026-07-16T19:59:00Z): UNH prints a fresh 52-wk high into the 7/15 close on thin breadth AND put skew richens materially vs. upside skew; OR a new DOJ charge/new state headline lands pre-print.
- Toward a small defined-risk LONG (call debit spread, entry 7/15 close or 7/16 pre-market, exit within 1-2 sessions): the Q2 EPS bar is confirmed at the lower ~$4.54 figure AND IV compresses into the print. Stops: $410 hard stop, targets $434.30 then $450-460.
- Hard veto (stay flat): FY26 MCR guide reiterated-not-raised or walked above ~89.3%, evidence prior-auth relaxation is driving early-Q2 utilization uptick, or fresh DOJ/state legal action at the print.

### Dissent (strongest unresolved disagreement)
Two unreconciled inputs drive the residual uncertainty:

1. **The EPS bar is not agreed upon.** Consensus Q2 adj EPS is quoted as $4.84 (bull/quant R1) vs $4.54 (bear) — a ~7% gap the quant flagged as likely adjusted-vs-reported/estimate-vintage drift, never reconciled by either side. This directly moves the beat/miss line the market judges on July 16.
2. **Is the fat tail symmetric or negatively skewed?** The bull argues the 7.5% average-down is distorted by two outlier prints and a real right tail exists in the same sample (justifying a downside-capped call spread). The bear argues the opposite reading of the same data: 3 of the last 4 prints were down, the two largest moves (-14.6%, -20%) are both downside, and a negatively-skewed distribution at a 52-wk high resolves violently down. The quant sides directionally with the bear on mean reaction but still concludes no expression clears rich IV. If the panel is wrong about skew direction, the no-trade default is correct in expectancy but a missed directional move (in whichever direction the skew truly points) is the most likely regret.
