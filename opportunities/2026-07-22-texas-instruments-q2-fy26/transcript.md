# Research Debate Transcript — TXN Q2 FY26 earnings

**PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.**

- Opportunity: `2026-07-22-texas-instruments-q2-fy26`
- Event: Texas Instruments (TXN) Q2 FY26 earnings — webcast after US close 2026-07-22; reaction trades 2026-07-23.
- Strategy: `three-round-panel` · Personas: bull (sonnet), bear (sonnet), quant (opus) · Synthesizer: opus
- Anchor price: TXN 340.26 @ 2026-07-07T19:59Z (sim stub, deterministic). Real Twelvedata for same minute ≈ 292.75 — discrepancy noted below.
- Execution env: equity-only, US session 13:30Z–19:59Z, no options, no overnight/pre-market fills. Intraday exits must be ≤19:59:00Z to map to a real bar.
- Synthesis timestamp: 2026-07-08T02:18:15Z

## Institutional lessons injected
- Confidence ≤~45 with an un-hedgeable positive tail and net EV <~2% against a ~7–8x adverse-tail-to-edge ratio is a NO-TRADE filter, not a size-down; defined-risk options are unavailable here.
- Discount post-earnings negative base rates when the name is at/near its 52-week low.
- Set intraday exits ≥1 min inside the session boundary; validate both legs map to available bars.

---

## Round 1 — Independent research (blind)

### Bull (Catalyst-hunter) — conditional LONG, confidence 58
TXN is the cleanest analog-upcycle vehicle with a second engine — AI/data-center power. Catalyst = beat-and-raise into a tape that reprices the narrative higher every print. Proposed a **post-earnings-announcement-drift intraday long** on 2026-07-23 (entry 13:31:00Z after the gap is visible, exit 19:59:00Z, +2.5% target) to sidestep the un-hedgeable overnight gap tail.
- Q1 FY26 (Apr 23): rev $4.8B, +19% YoY / +9% seq, above top of guide; stock +19%, record close, best day since 2000; data center +90% YoY (~12% of rev), industrial +30% YoY. ([CNBC](https://www.cnbc.com/2026/04/23/texas-instruments-stock-soars-on-q1-earnings-as-ai-demand-jumps.html), [TIKR](https://www.tikr.com/blog/texas-instruments-beats-q1-estimates-with-4-8b-revenue-and-19-year-over-year-growth))
- Q2 FY26 guide: rev $5.0–5.4B, EPS $1.77–2.05; consensus EPS $1.92 mid-guide = low bar. ([MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/TXN/earnings/))
- Last 5 earnings avg move ~6.43%; Q4'25 +9.9% despite a slight miss. ([StockTitan](https://www.stocktitan.net/news/TXN/ti-reports-q4-2025-and-2025-financial-results-and-shareholder-6koyxt3cx95k.html))
- Capex cut to $2–3B for 2026; CEO says $8 FCF/share "very likely." ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/texas-instruments-q1-earnings-call-214657661.html))
- Analyst targets: BofA $370, Stifel $360, UBS $350, Citi $345, all Buy. ([Investing.com](https://www.investing.com/news/stock-market-news/5-big-analyst-ai-moves-upgrades-for-txn-and-ddog-further-upside-seen-in-sndk-4608994))
- Flagged price discrepancy: sim stub 340.26 vs real Twelvedata ≈292.75 for the same minute (~16% gap).

### Bear (Skeptic) — NO-TRADE, mild short bias, confidence 40
A momentum name up ~70% YTD to ~$340, at/above its 52-wk high (~$334) and **above** the mean analyst 12-mo PT (~$294–298). Analog recovery *and* the data-center/AI-power narrative both fully priced in; Q1's +19.4% pop reset expectations higher. Classic sell-the-news trap.
- Valuation stretched: trailing P/E ~49–50x, fwd ~35–39x (~2x the 5-yr median). ([public.com](https://public.com/stocks/txn/pe-ratio), [TIKR](https://www.tikr.com/blog/texas-instruments-stock-has-fallen-15-from-its-high-is-the-selloff-a-bargain-or-a-warning))
- Sentiment cracking into the print: Goldman double downgrade (−3%+), removed from Russell value/defensive benchmarks (−4.34%), TXN −3.42% on Jul 7. ([TIKR/Goldman](https://www.tikr.com/blog/texas-instruments-nasdaq-txn-falls-over-3-as-goldman-sachs-double-downgrades-the-tech-stock), [TradersUnion](https://tradersunion.com/news/financial-news/show/2606055-texas-instruments-slides-4-34percent-to/))
- Data-center demand may be "borrowed" (pull-forward); capex overhang on the 300mm fab program. ([Investing SWOT](https://www.investing.com/news/swot-analysis/texas-instruments-swot-analysis-stock-faces-mixed-outlook-amid-recovery-93CH-4780262))
- Short is the deadlier tail: last reaction was +19.4%; a naked equity short faces an un-hedgeable ~15–20% up-gap. Neither leg is executable with edge → NO-TRADE.

### Quant (Pragmatist) — NO-TRADE, confidence 72
- Base rates (Trefis, 20 events, 5-yr): 30% positive / 70% negative 1-day; median +4.8% / −4.0%; 3-yr positive rate 25%. Avg abs move ~6.4%. Last two prints broke the bearish base rate (Q4 +9.9%, Q1 +19–21%). ([Trefis](https://www.trefis.com/stock/txn/articles/578674/how-will-texas-instruments-stock-react-to-its-upcoming-earnings/2025-10-10), [StockTitan](https://www.stocktitan.net/news/TXN/ti-reports-q4-2025-and-2025-financial-results-and-shareholder-6koyxt3cx95k.html))
- IV rank at yearly highs; expected move ~6–8%. TXN at/near ATH, not lows → the 52wk-low base-rate-discount lesson is inverted; raises sell-the-news risk.
- EV (naked long): P(up)=0.45, +7% / −6.5%, slippage 0.15% → **EV ≈ −0.6%**; at P(up)=0.50, ≈ +0.1% (zero). Adverse-tail-to-edge ≈ 60–75x, far above the 7–8x red line. Fails the no-trade filter decisively.

---

## Round 2 — Rebuttal

### Bull → concedes the instrument, not the thesis; confidence 58 → 40
Quant lands the fatal blow on the *instrument*: the edge lives in the overnight gap (~6.4% avg move) the sim forbids holding; the intraday-only equity leg is ~zero-EV after slippage — concedes it. Bear's "priced for perfection / above PT / at ATH" case is built on the 340.26 feed; at the real ≈292.75 fill, TXN is *below* the Street mean PT and ~12% below the high — softer valuation risk than the bear claimed, but still no way to monetize it intraday. Short is uninvestable (un-hedgeable up-gap). **Stand aside / NO-TRADE**; would flip to conviction long only if the gap were holdable or a confirmed gap-up + explicit guide-raise printed at the open.

### Bear → grants the structure, holds NO-TRADE; confidence 40 → 63
Grants that the bull's intraday-after-gap entry genuinely removes the overnight-gap tail (withdraws that specific objection). But removing the tail doesn't manufacture edge: PEAD is a cross-sectional, multi-day, diversified effect measured in bps/day — not a one-name one-session +2.5% signal; buying *after* the gap invites intraday reversal, especially in an extended name. The price discrepancy is the most important unresolved item — the sim fills against real bars (~292), making both his "riding record highs" and the bear's "above fair value at ATH" framings feed-dependent. Short is the same coin-flip mirrored. **NO-TRADE** on pure expectancy, tail aside.

### Quant → concedes tail point for intraday variant, prices it, holds NO-TRADE; confidence 72 → 70
Concedes the ~60–75x tail objection applies only to the naked-through-print variant, not the intraday-only one. But the intraday variant swaps a tail problem for a no-edge problem: PEAD is multi-week and arbitraged away in mega-cap TXN; the T+1 open→close residual is not sign-known.
- Intraday-only EV: P(continue)=0.54, ±2.0%, slippage 0.15% → **EV ≈ +0.01%** (at P=0.56, +0.09%) — ~zero, far under the 2% floor. The bull's "+2.5%" is the conditional-on-winning payoff, not probability-weighted.
- A 2:1 stop structure needs ~32% win rate but a 1.2% stop sits inside the T+1 post-print 3–5% ATR and gets whipsawed → stop framing fails.
- Price discrepancy: all inputs are percentage returns → scale-invariant; real ≈292.75 changes dollar P&L / share count, not the % edge. Valuation-tail softens slightly (below ATH) but +70% YTD and ~49–50x P/E keep sell-the-news live. **NO-TRADE.**

---

## Round 3 — Synthesis (opus)

**Convergent NO-TRADE.** The debate's real work was relocating the objection from "un-hedgeable overnight tail" (bull correctly showed an intraday-only entry escapes it) to "no edge that survives costs" (quant priced the intraday variant at EV ≈ 0; bear confirmed on expectancy). Under equity-only execution the sole tradable edge — the ~6.4% overnight earnings gap — cannot be held, and the intraday expression is a fresh coin-flip whipsawed by the highest-ATR session of the quarter. The 52wk-low base-rate-discount lesson is inverted (TXN near highs). No positive-EV leg exists long or short.

- **Hypothesis:** No positive-expectancy trade under the constraints; residual mild short lean on stretched valuation, insufficient to overcome ~0 net EV. Direction (residual) short; confidence 30.
- **Plan:** TXN — **NO-TRADE**. No entry/exit. Expected profit 0%.
- **Dissent (strongest unresolved):** Bull — the long edge is genuinely real but structurally un-executable (lives in the forbidden overnight gap); with a holdable gap or defined-risk options this flips to a conviction long. Plus the unresolved ~16% price-feed discrepancy (stub 340.26 vs real ≈292.75), which materially weakens the "priced for perfection" framing at the true fill even though it leaves percentage EV unchanged.

### Data/execution caveats logged for the post-mortem
1. Sim stub anchor (340.26) vs real Twelvedata (~292.75) for 2026-07-07T19:59Z differ ~16%; dollar P&L depends on the real fill. Percentage EV — the basis for this NO-TRADE — is scale-invariant, so the verdict stands regardless.
2. Any future intraday leg must exit ≤19:59:00Z to map to a real 1-minute bar.
