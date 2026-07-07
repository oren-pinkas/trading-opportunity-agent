# Debate transcript — TSMC Q2 FY26 earnings (2026-07-16)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Strategy:** three-round-panel
- **Personas / models:** bull (sonnet), bear (sonnet), quant (opus); synthesizer (opus)
- **Run:** 2026-07-07T23:40:00Z
- **Anchor prices (2026-07-07T19:59Z, `toa price`, stub:deterministic):** TSM 474.45, NVDA 460.35
- **Event source:** TSMC Q2 2026 Earnings Conference — https://investor.tsmc.com/english/quarterly-results/teleconference
- **Institutional lessons injected** (`toa lessons-relevant --type earnings --tickers TSM,NVDA`):
  - No-trade filter: confidence ≤~45 + un-hedgeable positive tail + net EV <~2% vs ~7–8x adverse-tail-to-edge ratio ⇒ NO-TRADE, not a size-down. (2026-06-25-nike-q4-fy26)
  - Discount negative base rates when near 52-wk low. (2026-06-25-nike-q4-fy26)
  - Intraday exit ≥1 min inside session (19:59:00Z, not 20:00:00Z) or leg no-fills. (2026-07-02-tesla-deliveries)
  - Validate both legs map to available US-equity bars 13:30Z–19:59Z; options do not fill. (2026-07-02-tesla-deliveries)

> All persona evidence is drawn from model training knowledge (cutoff Jan 2026) and explicitly flagged as such — no live figures for this quarter's print were available. TSMC reports before the US open (Taiwan morning); the tradeable window is the US regular session on 2026-07-16, and the post-print gap is not capturable under the simulator's equity-only, in-session fill constraints.

---

## Round 1 — Independent research

### Bull (sonnet) — LONG, confidence 58
TSMC is the highest-signal event in the AI hardware supply chain (sees the order book ~2 quarters ahead of Nvidia itself). Beat-and-raise pattern on HPC/AI revenue driven by CoWoS advanced-packaging capacity and N3/N2 demand (Nvidia, AMD, hyperscaler ASICs). Demand is capacity-constrained, not demand-constrained — structurally bullish because upside comes from capacity adds. Historical earnings-day reactions frequently mid-single-digit %. Proposed: BUY TSM entry 2026-07-16T13:35:00Z (5 min after open to confirm direction), exit 19:58:00Z, target +4–6%; secondary BUY NVDA +2–3%. Invalidation: exit if 13:30–13:40Z tape is red/flat. Conceded upfront that much good news is already in the anchor and "sell the news" is a live risk.

### Bear (sonnet) — NO-TRADE, confidence 30 (that an edge exists)
TSM is one of the most heavily-owned AI-capex proxies; consensus already bakes CoWoS/packaging capacity, N2 ramp, and hyperscaler capex. The ADR gaps overnight to the Taiwan-morning print, so the cleanest edge (surprise vs consensus) is resolved before the simulator can fill. What remains in-session is noisy second-derivative digestion, prone to buy-the-rumor-sell-the-news / priced-for-perfection fades in this exact name. NVDA is a noisy second-order read-through (TSMC rarely names customers). No options hedge ⇒ full linear reversal exposure. Meets the spirit of the no-trade filter: modest edge, large uncapped adverse tail, no hedge instrument.

### Quant (opus) — NO-TRADE, confidence 38 (that an edge exists)
Base rates (training recollection): TSM earnings-day abs move ~4–6% close-to-close; options-implied ~5–7% (irrelevant — options don't fill). Decisive number: ~70–85% of the move is realized in the overnight gap, leaving only ~0.8–1.5% capturable intraday drift, with a weak ~52–56% gap-continuation hit rate. EV (blind gap-continuation): p=0.54, win +1.2% / loss −1.1%, costs ~0.13% ⇒ net ≈ +0.0–0.15%. Even optimistic p=0.57 ⇒ +0.20%. An order of magnitude below the 2% threshold; adverse-tail-to-edge ≈ 10–15x, worse than the 7–8x screen. NO-TRADE. Would flip only if p(continuation) ≥ ~0.62 or a same-day catalyst widens the capturable intraday fraction.

---

## Round 2 — Rebuttal

### Bull (sonnet) → folds to 40
Concedes the math: "+4–6%" was the *total event move*, and the overwhelming majority is in the gap the simulator can't capture — conflating total with in-session capturable was an error. Residual defense: a US-session second wave (sell-side PT revisions, hyperscaler-capex read-throughs) does reprice during US RTH, but widens the capturable fraction only modestly (~1% → ~1.5–2%) and only on a minority of clean beat-and-raise prints. Can't credibly push p(continuation) to 0.62 without live tape. Folds to a de-minimis, confirmation-gated TSM long (enter 13:46:00Z only if 13:30–13:45Z tape is green and holding opening-range high; exit 19:58:00Z; target +1.5%), drops the NVDA leg, else NO-TRADE.

### Bear (sonnet) → hardens to 78 (no-trade conviction)
Adopts the quant's arithmetic as the quantitative spine. Identifies the bull's **double-count**: entering at 13:35Z means buying at the post-gap price, so the +4–6% is arithmetically unreachable without a second independent intraday catalyst. The bull's own invalidation rule ("exit if early tape red/flat") concedes direction is undetermined at open and self-defeatingly filters out the entries that had edge. NO-TRADE; confidence a clean directional in-session edge exists: ~20.

### Quant (opus) → holds NO-TRADE, ~66 conviction
Names the bull's error precisely: harvesting +4–6% from a 13:35Z entry would require a ~9–11% total day (a ~5–12%-of-quarters tail), not a base case. Holds the 0.8–1.5% capturable-drift estimate (constraint doc explicitly agrees the gap is not capturable). Grants that confirmation-gating raises p to ~0.56–0.60 but you pay ~0.3–0.5% of the move for it and shrink the remaining distance. Conditioned EV: p=0.58, win +0.9%/loss −1.0%, costs 0.13% ⇒ **−0.03%**; generous p=0.60, +1.2%/−1.0% ⇒ **+0.19%**. Conditioning changes the sign risk but not the verdict. NO-TRADE; edge-exists confidence 34, no-trade conviction ~66.

---

## Round 3 — Synthesis (opus)

**Verdict: NO-TRADE.** All three personas converge. The fundamental bias is genuinely long (TSMC beat-and-raise remains the base case, AI demand capacity-constrained), but the entire information content of this event lands in the overnight ADR gap that closes before the 13:30Z US cash open — un-capturable under the equity-only, in-session fill constraints. What remains tradeable is ~0.8–1.5% of near-directionless intraday drift at a ~52–56% continuation hit rate. Every EV path — blind or confirmation-gated — nets ~0.0% to +0.2% after costs, an order of magnitude below the 2% threshold, against a ~7–15x adverse-tail-to-edge ratio with no options hedge available to define the tail. This is a textbook application of the no-trade filter. The bull's best surviving idea (a de-minimis confirmation-gated TSM long) still nets ~0% EV and is not worth the linear reversal exposure. NVDA as a vehicle is strictly worse (second-derivative read-through noise) and rejected by all three.

- **hypothesis:** {statement: "TSMC Q2 FY26 fundamental bias is a beat-and-raise (long), but the entire edge lands in the un-capturable overnight ADR gap; only ~0.8–1.5% of directionless intraday drift is in-session tradeable, netting ~0–0.2% EV after costs — an order of magnitude below the 2% threshold with a ~7–15x adverse-tail-to-edge ratio and no options hedge. NO-TRADE.", direction: long, confidence: 34}
- **plan:** NO-TRADE. Only executable expression (conditional de-minimis TSM long, gated on green opening tape, target +1.5%) is ~0% EV after costs; not scheduled, not simulated. `expected_profit_pct: 0`.
- **dissent (strongest unresolved):** The bull's contention that a same-day in-session catalyst — a sell-side PT-revision cascade or NVDA sympathy momentum with volume confirmation by ~13:45Z — can widen the capturable fraction enough to matter. The panel could not resolve this without live tape; if such a catalyst appears intraday, the de-minimis confirmation-gated long is the only structure worth revisiting. Falsifiable test: conditional open→close continuation on strong-tape TSM earnings days with hit rate ≥62% AND mean captured move ≥2% net — no persona believes that dataset exists.
