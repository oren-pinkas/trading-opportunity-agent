# Research Debate Transcript — DOMO/PRGS Asset Sale

Paper-trading simulation only. Not financial advice.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.

## Dossier facts

- Domo agreed to sell substantially all operating assets to Progress Software for USD 400 million cash, leaving a debt-free public shell with roughly USD 246 million net cash and over USD 900 million in tax-loss assets (NOLs); deal expected to close before Progress's fiscal year end Nov 30 2026.
- Tickers: DOMO (seller/shell), PRGS (buyer).
- Source: Benzinga, "Why Is Domo (DOMO) Stock Rallying Over 23% After Hours Today?" (2026-07-23), https://www.benzinga.com/markets/equities/26/07/60628806/why-is-domo-domo-stock-rallying-over-23-after-hours-today
- Announcement after-hours 2026-07-23 ~21:02 UTC.

## Verified market data (toa price, provider twelvedata)

- DOMO 2026-07-23 15:00 UTC (pre-announcement, regular session): **$3.875**
- DOMO 2026-07-24 13:31 UTC (next-day open): **$4.0299** (+4.0% vs pre-announcement)
- DOMO 2026-07-24 19:59 UTC (next-day close): **$3.66** (-5.5% vs pre-announcement, -9.2% off the open)
- PRGS 2026-07-23 15:00 UTC (pre-announcement): **$37.48** (no post-announcement print available via API)
- 2026-07-25 intraday data not available via API at time of research.

The headline "+23% after-hours" pop did not survive the regular session — DOMO opened only +4% and faded to a net loss on the day (a ~28-point round trip from the after-hours implied high to the session close).

## Institutional lessons consulted (`toa lessons-relevant --type earnings --tickers DOMO,PRGS`)

- Confidence <=~45 with an un-hedgeable positive tail and net EV <2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter — express via defined-risk options, never a naked short. (2026-06-25-nike-q4-fy26)
- A catalyst that already drove a large run is priced in — don't re-bet the same fundamental as a fresh gap trigger. (2026-06-26-delta-q2-fy26)
- When the quant's own EV math says directional EV is ~0, log NO TRADE rather than manufacture a minimal directional position "for the learning loop." (2026-07-02-levi-q2-fy26)
- Anchor entry prices to a live quote at the actual entry timestamp, not a stale pre-move reference. (2026-07-02-levi-q2-fy26)

---

## Round 1 — Independent research

### Bull (sonnet)

This is not a normal earnings pop — it's a corporate-action re-rating. Domo sold substantially all operating assets to Progress Software for USD 400M cash, leaving a debt-free shell with roughly USD 246M net cash and 900M+ in NOLs. That's a liquidation-value story: the market has to reprice DOMO off its former "growth software" multiple onto a cash-plus-optionality floor. The NOLs alone make this an attractive acquisition shell for any profitable company looking to shelter future income — a second catalyst on top of the cash. For PRGS, it's a bolt-on of Domo's BI/analytics assets funded from balance sheet, closing before Progress's Nov 30, 2026 fiscal year-end — a hard, dated catalyst window.

Evidence: Benzinga (2026-07-23); verified prints — DOMO pre-announcement $3.875, next-day open $4.0299 (+4.0%), next-day close $3.66 (-5.5% vs pre-announcement, -9.2% off the open); PRGS pre-announcement $37.48.

I have to be honest: the +23% after-hours print did not survive contact with the regular session — it faded hard, and DOMO closed down net on the day. That kills the "buy the gap, ride the momentum" thesis for the equity itself. I won't manufacture a re-entry on a catalyst that's already been faded once.

But the mispricing isn't in day-one momentum — it's in terminal value: USD 246M net cash + 900M NOLs against a small-cap market cap means DOMO could be trading near or below stub cash-shell value once the deal closes. Proposed action: modest DOMO long sized for a multi-week/multi-month hold into deal-close catalysts, entered at a live quote (not the stale $3.875), treating dips toward the $3.60s as accumulation against the ~$246M cash floor, targeting re-rating toward NAV-plus-NOL-optionality, exiting into closing-confirmation news or after FY-end passes. Secondary, smaller idea: a defined-risk long-dated PRGS call if accretion math checks out.

### Bear (sonnet)

The thesis that this is a clean tradeable dislocation is already refuted by the price action itself. AH printed +23%, but that quote was likely thin, wide-spread, low-volume noise. The market's actual verdict came in the regular session: DOMO opened at only +4%, then faded all day to close -5.5% vs pre-announcement and -9.2% off the open — a textbook sell-the-news/arb-fade. Whatever edge the bull thinks exists between the AH print and "fair value" was arbed out inside the first 30 minutes of trading on 7/24.

What's priced in: the USD 400M sale price, the ~USD 246M net cash, and the NOL shell narrative are all now public and reflected in a stock that's had a full day of two-sided volume to digest it. Real money looked at the net-cash math and did not bid it up.

Concrete risks the bull is likely underweighting: (1) deal-closing risk — shareholder vote and possible regulatory review over a ~4-month runway, no go-shop premium mentioned to cushion a break; (2) this is a slow, multi-quarter-to-multi-year special situation, not a fast trade — horizon mismatch risk; (3) liquidity/execution risk on a sub-$4 microcap, possible forced selling once it's no longer an "operating company" for small-cap mandates; (4) the AH print's reliability itself — anchoring entry logic to it risks manufacturing a false edge out of noise; (5) PRGS — USD 400M real cash outlay, integration risk, zero information on whether they overpaid, no confirmed post-announcement PRGS price.

Bottom line: NO TRADE, or at most a defined-risk, small-size options structure on DOMO that caps loss against deal-break risk — never a naked long chasing the stale AH print, never a short into what could still be a legitimate value unlock.

### Quant (opus)

This is an asset sale into a residual shell, not a clean cash merger — there is no fixed arb anchor. Base rate: shells trade at a 10-30% discount to stated net cash for quarters; NOLs are typically valued near 0-10 cents on the dollar (Section 382 limits, no taxable income to use them against). The reflexive pattern for a sub-$4 microcap: AH headline pop → overnight momentum buyers → regular-session supply from holders exiting an illiquid broken-growth name → fade → multi-week chop. By day 2-3 the informational edge is gone; what's left is a slow re-rating driven by disclosure (proxy, wind-down plan, distribution timing), not momentum.

EV, DOMO long (5-10 day hold): scenario-weighted gross +0.70%, all-in costs ~1.0% (spread/slippage on a sub-$4 microcap) → **net ≈ -0.3%. Fails.**

EV, DOMO short (fade the pop): gross -1.30% before costs — the adverse tail (net-cash-per-share disclosure, tender, special dividend, NOL-shell reverse-merger bid) is ~-28% in a 5% scenario; borrow cost/hard-to-borrow risk and spread push **net ≈ -1.5% to -1.7%.** Tail ratio ~14x vs the 7-8x no-trade threshold. No usable options chain on this microcap (near-zero OI, huge spreads) to express defined-risk. **Short is out.**

EV, PRGS: gross +0.06% vs ~0.08% costs → **net ≈ 0. Noise.**

Confidence: 22/100 that ANY directional expression has positive net EV. Crux: no verified diluted share count/net-cash-per-share — "trading at a discount to cash" is currently an unsupported claim in either direction. Would revise up on: (1) verified net-cash-per-share showing a real discount, (2) a committed return-of-capital mechanism vs open-ended reinvestment discretion, (3) a usable options market, (4) a quantified PRGS accretion argument.

**Round 1 position: NO TRADE.**

---

## Round 2 — Rebuttal

### Bull (sonnet)

Bear and quant both land the same punch: no verified diluted share count, so "trading below cash floor" is currently unpriced. Retracting the strong form of it. Flagged, unverified: DOMO's share count has historically run ~24-25M, which would put USD 246M net cash at roughly $10/share — if directionally right, the gap is the whole thesis, but this is an estimate, not a fact to trade on. Softening from "DOMO is trading below its cash floor" to "may be" — a hypothesis, not a position size.

Conceding the horizon-mismatch critique: R1 language smuggled in a faster re-rating expectation ("targeting re-rating," "accumulation") than the disclosure-driven mechanism (proxy, wind-down plan, distribution timing) actually supports. Correcting: this is a multi-month position that only makes sense held through a proxy filing and shareholder vote with no interim catalyst — quant's ~1% short-horizon cost drag is the wrong frame if not exiting in 5-10 days, but bid/ask and friction compounding over months on a microcap with possible forced index-fund selling (bear's point) wasn't addressed in R1.

Residual disagreement: quant's EV math is built for a short-horizon trade and correctly kills that, but a committed return-of-capital mechanism is, to the bull, an upside tail, not just a risk — a debt-free shell's loss vectors are narrower than a typical small-cap long (deal breaks before Nov 30; management burns cash on bad reinvestment; the share-count estimate is wrong).

Revised action: downsizing to a small starter position only, explicitly conditioned on getting a verified net-cash-per-share figure before adding; dropping "targeting re-rating into deal-close" in favor of "hold through disclosure catalysts with no fixed exit timeline." Dropping the PRGS call idea — deferring to quant's near-zero EV read.

### Bear (sonnet)

Quant and bear converge on NO TRADE but for different reasons, and the gap matters. Quant's is a costs/EV argument (even the modest gross edge fails after ~1.0% frictions). Bear's is a state-uncertainty argument: no verified net-cash-per-share, no deal-protection terms (breakup fee, go-shop, financing contingency), no confirmation the deal clears a shareholder vote without an activist holdout. Quant would flip on better EV inputs alone; bear needs EV *and* resolved event risk.

Pushing hard on "accumulation zone against the cash floor": as framed, it's unfalsifiable — any price drop reads as "more compelling," with no losing state. Demanding, before crediting the floor: (1) a verified, published net-cash-per-share number; (2) a specific invalidation price tied to actual cash-per-share math, not vibes; (3) confirmation of what happens to the cash — stated return-of-capital plan vs. open-ended management discretion (a shell with no capital-return commitment can trade below cash indefinitely — a governance discount, not a mispricing — and NOLs mean nothing without a monetization plan); (4) deal-break terms (breakup fee, MAC clause, antitrust/CFIUS exposure) — none surfaced by either side.

Position holds: NO TRADE. This is a multi-month event-risk bet dressed as a value trade, and neither side has produced the numbers to price the event risk.

### Quant (opus)

Bear's and quant's NO TRADE verdicts are independent gates, not the same objection restated — probabilities multiply, not average: P(clears frictions) ~0.25 × P(event/liquidity risk doesn't dominate) ~0.5 ≈ 0.12. This should raise combined confidence in NO TRADE, not blend the two views.

The bear's price path (open +4%, close -5.5%) is the one hard new number in Round 1, and it cuts against the bull: the market had a full liquid session and marked DOMO down net versus pre-announcement. That is completed price discovery, not an unnoticed NAV gap — the bull is not early, the bull is on the other side of a finished repricing.

"Accumulation zone" is not falsifiable: no losing state, every adverse price reads as more compelling — a martingale with a story attached, unbounded downside sizing. Three defects: (a) a cash floor isn't a floor without a committed distribution mechanism — the 10-30%-below-net-cash base rate exists because the market prices the risk of a bad reinvestment/reverse-merger, i.e. the discount is a fee for governance/agency risk, not an error to harvest; (b) the NOL leg is close to self-cancelling — monetizing 900M+ NOLs via reverse merger triggers a Section 382 ownership change that impairs them, so the two bull optionalities are negatively correlated; (c) USD 246M is gross stated net cash, not distributable cash — transaction tax, advisory fees, retained liabilities, severance/wind-down, ongoing public-company cost are all unquantified.

Three concrete deliverables that would convert the story into a numbered edge: (i) a verified diluted share count from the most recent filing with a stated net-cash-per-share (the implied per-share figure swings 40%+ across plausible share-count bands — wider than the entire alleged edge); (ii) a committed distribution mechanism with a date (plan of liquidation, tender, declared special dividend) — absent that, haircut to the 10-30%-below-net-cash base rate, not to NAV; (iii) a dated re-rating catalyst (proxy filing date, vote/record date, expected close date). Absent (i), the long thesis is unpriced speculation, not analysis.

Tightened EV: DOMO long, 5-10 day — unchanged, net ≈ -0.30%, fails. Steel-manning the bull's multi-month horizon: friction drag amortizes down, but the distribution turns bimodal on close/break — at a ~12% break probability and a ~-30% break-case gap, breakeven requires gain ≥ ~5.2%, and reaching a sane reward/risk for a four-month illiquid-microcap lockup needs a verified ~15-20%+ NAV gap with a known closing date. Nobody has produced that verified gap — the long horizon doesn't have negative EV, it has *uncomputable* EV, which for sizing purposes is treated as zero-or-worse. DOMO short: unchanged, tail ratio ~14x vs 7-8x threshold, no usable options chain — OUT. PRGS: unchanged, net ≈ 0, noise; "if accretion math checks out" is a conditional, not a trade.

Updated confidence: NO TRADE 88/100 (up from ~78 implied in Round 1); any directional expression clearing costs 12/100 (down from 22/100). Round 2 verdict: NO TRADE, DOMO and PRGS, not a close call.

---

## Round 3 — Synthesis (opus)

### hypothesis

- **statement:** Domo's sale of its operating assets to Progress Software for USD 400M cash converts DOMO into a debt-free cash shell (~USD 246M stated net cash, 900M+ NOLs), but the panel could not verify the one number the thesis depends on — diluted net-cash-per-share — so no mispricing was ever established. The market had a full liquid session to price the deal and marked DOMO *down* net (open +4.0% to $4.0299, close -5.5% to $3.66 vs the $3.875 pre-announcement print), which is completed price discovery, not an unnoticed NAV gap. Shell base rates (10-30% discounts to net cash persisting for quarters, NOLs worth ~0-10 cents/dollar under Section 382, unquantified wind-down/tax/public-company costs against gross stated cash) plus unresolved deal-completion risk (shareholder vote, possible regulatory review, no disclosed breakup fee or MAC terms, ~4-month runway to Progress's Nov 30 2026 FY-end) mean neither a computable edge nor a defined-risk expression exists. The long fails on cost/EV arithmetic (net ≈ -0.3% over 5-10 days) and on the absence of a verified NAV gap over any horizon; the short fails on a ~14x tail ratio versus a 7-8x threshold with no usable options chain. PRGS carries zero confirming accretion data and prices as noise.
- **direction:** none
- **confidence:** 85 (that NO TRADE is correct — reflects the compounding of two independent gates, event risk and cost/EV, estimated at P ≈ 0.12 that any directional expression clears both; quant's final 88/100 anchors the high end, bull's residual conditional starter position the low end)

### plan

| field | value |
|---|---|
| ticker | DOMO (secondary: PRGS) |
| action | no_trade |
| entry.time | null |
| entry.target_price | null |
| exit.time | null |
| exit.target_price | null |
| expected_profit_pct | null |

No position on either leg. No token starter, no "tiny defined-risk" options stub — there is no usable options chain on DOMO to express defined risk on either side, so the only available expression is unhedged microcap common, which fails both gates.

### dissent

The bull's residual conditional thesis is the strongest unresolved disagreement, and it is worth flagging precisely because it is now falsifiable. The bull retracted the "trading below cash" claim as unverified and dropped the accumulation-zone/deal-close-timed-exit framing, but holds that a small starter long becomes justified if three specific, checkable conditions are confirmed: (1) verified diluted net-cash-per-share meaningfully above the current price (the bull's unconfirmed ~24-25M share estimate implies ~$10/share against a $3.66 close; a filed share count confirming a ~15-20%+ NAV gap after taxes/fees/wind-down/public-company costs changes the arithmetic's character); (2) a committed return-of-capital mechanism (declared special distribution or formal liquidation plan, not open-ended reinvestment/reverse-merger discretion); (3) a dated re-rating catalyst (record date, vote date, or stated distribution timeline).

Quant and bear do not concede even if all three land. Quant: even granting a verified 15-20% NAV gap, a ~12% deal-break probability against a ~-30% break-case gap only reaches EV ≈ 0 — the gap must be verified *and* the closing date known just to reach breakeven, and frictions on a sub-$4 microcap don't amortize away cleanly if the position must be exitable at size. Quant also argues NAV-gap condition (1) and the NOL sweetener are negatively correlated: the reverse-merger route that monetizes 900M+ NOLs triggers a Section 382 ownership change that impairs them, so both upside legs can't be paid together. Bear: independent of pricing, absent disclosed breakup-fee, MAC, and antitrust/CFIUS terms, deal-completion risk is unpriced rather than favorably priced, and DOMO ceasing to be an "operating company" invites forced selling from small-cap mandates — a flow risk that gets worse, not better, as the shell thesis is confirmed. Neither dissenter can be hedged into comfort since there is no options chain.

**Post-mortem test:** If DOMO subsequently re-rates toward a verified net-cash-per-share on a disclosed distribution plan, the correct lesson is *not* "should have bought the shell" — it is "should have pulled the diluted share count and distribution language from the merger filing during research instead of debating an unverified number for three rounds." Grade the missing data-gathering step, not the directional call. Conversely, if DOMO drifts or the deal wobbles, confirm whether the ~14x tail ratio and no-options-chain constraint were the binding reasons to stand down, or whether NO TRADE was merely right by luck.
