# NKE Q4/FY2026 — Three-Round Panel Debate

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Event:** Nike reports fiscal Q4 + full-year FY2026 on Tue 2026-06-30 after close; reaction trades at the Wed 2026-07-01 open.
- **Strategy:** debate-three-round-panel | **Personas/models:** bull (sonnet), bear (sonnet), quant (opus); synthesizer (opus)
- **Relevant lessons injected:** none recorded for earnings/NKE.
- **Reference price:** ~$41.8 near 52-wk low $41.31 (web-researched; the local stub's $76.85 is wrong).

---

## Round 1 — Independent research

### Bull (sonnet)
LONG. NKE at a multi-year low (~$42, ~48% off the $80.17 high) discounts near-worst-case; a low-bar quarter plus a clean upside surprise can spark a violent short-cover rally. The ~$1B IEEPA tariff refund is a confirmed Q4 one-time benefit "not contemplated in previously provided guidance" — pure upside to the $0.11–0.12 consensus. Options imply ~±11%; historical median positive reaction +6.7%. Target LONG entry 2026-07-01T13:35Z ~$44.50 → exit 17:30Z ~$47.50 (~+6.7%). Risk: refund smaller/contested or weak FY27 guidance → the live -11% downside.
- [Capital.com market cap](https://capital.com/en-int/markets/shares/nike-inc-share-price/market-cap) · [Benzinga/BofA](https://www.benzinga.com/analyst-stock-ratings/reiteration/26/06/60076842/why-this-analyst-thinks-nike-guidance-matters-more-than-earnings) · [Investing.com tariff refund](https://uk.investing.com/news/stock-market-news/nike-stock-rises-on-cfo-transition-and-tariff-refund-benefit-93CH-4741184) · [Market Chameleon](https://marketchameleon.com/Overview/NKE/Earnings/Stock-Price-Moves-Around-Earnings/)

### Bear (sonnet)
SHORT. Five-year post-earnings record is brutal — ~35% positive one-day, **median -6.9%**, last two prints -20% (Jun 2024) and -15.5% (Mar 2026). Tariff refund is one-time and already in the $0.11 consensus (BofA: ex-refund, Q4 "aligns closely with prior guidance"). Greater China guided ~-20% with no floor; ~250 bps tariff GM headwind through Q1 FY27; FY27 guidance withheld until a fall Investor Day. At ~28x fwd on shrinking revenue there's no margin of safety. Short the reaction, target -7% to -12%.
- [Trefis preview](https://www.trefis.com/stock/nke/articles/604056/how-will-nike-stock-react-to-its-upcoming-earnings-3/2026-06-23) · [AInvest China reset](https://www.ainvest.com/news/nike-china-guidance-reset-term-pain-confirms-deep-rooted-inventory-demand-headwinds-2604/) · [OptionSlam NKE](https://www.optionslam.com/earnings/stocks/NKE) · [Benzinga/BofA](https://www.benzinga.com/analyst-stock-ratings/reiteration/26/06/60076842/why-this-analyst-thinks-nike-guidance-matters-more-than-earnings)

### Quant (opus)
NO TRADE *under the same-day open→close structure* — earnings print 6/30 AMC, so the ~9% move is an overnight GAP realized at the 7/1 open; an open→close hold sits out the gap and captures only random intraday drift (net EV ≈ -0.2% after costs). Flagged the real edge explicitly: SHORT into the print holding the gap → P(down)~0.65-0.75, median down -6.9% vs up +6.7% ⇒ gross EV ≈ +4.6%. Real price ~$41.72 near 52-wk lows; implied move ~9.5%.
- [stockanalysis NKE](https://stockanalysis.com/stocks/nke/) · [OptionSlam NKE](https://www.optionslam.com/earnings/stocks/NKE) · [Trefis](https://www.trefis.com/stock/nke/articles/604056/how-will-nike-stock-react-to-its-upcoming-earnings-3/2026-06-23)

---

## Round 2 — Rebuttal (gap-hold structure permitted)

### Bull → concedes
Honestly reassessed: the base rate dominates. P(down)~0.70 × median -6.9% vs 0.30 × +6.7% is negative-EV for a long, and NKE's downside gaps are fat-tailed (-20%, -15.5%), which hurts the long more than the median implies. The long was always "low price + squeeze + refund tail outweighs base rate" — but without information the market lacks, it doesn't. **Concedes to NO TRADE / defers to the short.** Would only flip if buy-side EPS were below the refund-inclusive consensus or short interest spiked >12%.

### Bear → SHORT, confidence 60
Reconciled price to ~$41.82 (near 52-wk low), tightening the case (cheap-looking, expensive on fundamentals at ~28x fwd). Accepts the quant's direction. Key concession: short interest is only ~3.5-5% of float — **too low for a mechanical squeeze**; the bull overstated it. The real binary is FY27 guidance: reinstated with a positive trajectory ⇒ bull wins; withheld again ⇒ bear confirmed. Tariff-refund EPS beat shaves conviction 70→60. Entry 2026-06-30 ~19:55Z ~$42 → exit 2026-07-01 ~13:30Z ~$38.50 (~+8.3% gross).
- [Yahoo NKE](https://finance.yahoo.com/quote/NKE/) · [MarketBeat short interest](https://www.marketbeat.com/stocks/NYSE/NKE/short-interest/) · [Fintel](https://fintel.io/ss/us/nke)

### Quant → SHORT but THIN, confidence 38
Gap now capturable, so the R1 objection is withdrawn. EV (gap-hold, short): P(down)=0.65 × +6.9% + P(up)=0.35 × -6.7% = +2.14% gross; minus ~0.35% costs ⇒ **net ≈ +1.8%**. But the adverse tail (a +10-15% squeeze gap) is un-hedgeable in a naked short — a ~7-8x loss-to-edge ratio. Quarter-size conviction at most; "no trade / await guidance clarity" is a defensible alternative. Entry 2026-06-30T19:50Z $41.85 → exit 2026-07-01T13:45Z $38.95 (median). **Not** on the bull's side — a long buys the median loss to chase the right tail.
- [Barchart expected move](https://www.barchart.com/stocks/quotes/NKE/expected-move) · [OptionSlam](https://www.optionslam.com/earnings/stocks/NKE)

---

## Round 3 — Synthesis (opus, neutral orchestrator)

- **hypothesis:** SHORT NKE held across the 6/30 AMC print into the 7/1 open gap. Edge = base rate (down ~65%, median -6.9%) + likely FY27 guidance withholding (sells off). **direction: short. confidence: 42.**
- **plan:** short NKE, entry 2026-06-30T19:50:00Z @ ~41.85, exit 2026-07-01T13:45:00Z @ ~40.95 (EV-weighted), expected_profit_pct 2.0.
- **dissent (strongest unresolved):** the un-hedgeable positive tail — a larger-than-modeled tariff-refund EPS beat and/or any FY27 guidance reinstatement triggers a +10-15% short-cover gap. The quant rates a quarter-size short OR no-trade as equally defensible (net EV only ~+1.8% vs a ~7-8x adverse-tail ratio). The bull conceded the long but did not endorse the short. Confidence is deliberately low (42) to encode this.
