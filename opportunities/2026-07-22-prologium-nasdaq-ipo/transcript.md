# Research Debate Transcript — ProLogium Nasdaq listing (PRLG)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Run at 2026-07-24T00:49:57Z.

Institutional lessons applied (source: 2026-07-07-lime-ipo):
1. For IPO plans, don't hard-code entry to the raw listing-day open minute — delay entry to a liquid window (30-60min after first print) or probe for a fillable bar before scheduling both legs.
2. Never convert an imprecise listing window ("H2 2026") into a single exact timestamp; gate IPO opportunities on a confirmed exchange listing date/time verified present in the price provider.

Dossier facts referenced: event type ipo, ticker PRLG, ~USD 3.8B valuation, "expected to close H2 2026", single source (Electrek, 2026-05-27, accessed 2026-07-22), dossier impact_window 2026-07-31.

## Round 1 — Independent research

### Bull (sonnet)
Read: solid-state EV battery maker going public via SPAC/IPO on Nasdaq (PRLG), ~USD 3.8B valuation (Electrek, 2026-05-27). Thematic momentum in solid-state battery narrative could drive a listing-day pop as momentum funds/retail chase the story.

Evidence: dossier's event summary and single Electrek source only; expected close "H2 2026", no exact date; 2026-07-31 impact_window appears to be a placeholder, not a confirmed exchange date; no SEC filing, no second source.

Proposed action (contingent): long PRLG common, entry gated on a confirmed listing date verified live in the price provider (not the raw listing-day open — wait 30-60min for a liquid, fillable bar per lesson 1), exit via trailing stop (15-20% off intraday high) scaled out over 3-5 sessions, small/starter size given single-source evidence.

Flagged gaps: listing date NOT confirmed; only one stale source; no float/lockup/PIPE/sponsor data. Action explicitly "contingent, not immediate."

### Bear (sonnet)
Thesis: this isn't a tradeable event yet. "Expected to close H2 2026" spans a ~150-day window; the dossier's 2026-07-31 impact_window (7 days out) is unconfirmed and likely premature/fabricated — no listing date exists in evidence. Per lesson 2, don't gate a trade on an unconfirmed date.

Consensus/pricing: solid-state SPAC/de-SPAC names (QuantumScape, Solid Power, Northvolt-adjacent) trade on narrative; pattern is retail pop then multi-month fade once lockup/dilution reality sets in — nothing proprietary in a single 2-month-old Electrek post.

Risks: SPAC deal collapse/delay (flagged CFIUS/national-security review risk given ProLogium's Taiwan-based, China-adjacent supply chain); dilution/redemption/PIPE overhang; lockup overhang capping upside; thin/unreliable day-1 liquidity (lesson 1); single stale source with no corroborating SEC filing or exchange notice.

Recommendation: NO TRADE until a confirmed dated listing announcement (8-K/press release) is verified live in the price provider, plus 30-60min of liquid post-open data, plus lockup/PIPE/redemption clarity, plus a second independent source.

### Quant (opus)
Base rates from EV-battery de-SPAC cohort (QuantumScape, Microvast, Romeo Power, SES AI, Solid Power, Freyr): P(day-1 close >+10%) ≈ 0.20; P(flat ±10%) ≈ 0.45; P(day-1 fade <-10%) ≈ 0.35. Over 1-2 weeks, negative-skewed drift from redemption/PIPE/warrant overhang: P(up >10%) ≈ 0.25, P(down >10%) ≈ 0.50, P(range) ≈ 0.25.

Key uncertainty: P(tradeable by 2026-07-31 at all) ≈ 0.10-0.15 — "H2 2026" is a ~150-day window and de-SPAC closes routinely slip toward Q4; the dossier's 2026-07-31 impact_window is a manufactured point inside that range, exactly what lesson 2 warns against.

EV: conditional-on-tradeable naive day-1 long EV = 0.20(0.15) − 0.35(0.12) = −1.2% gross; net of ~1-1.5% costs/slippage on an illiquid day-1 de-SPAC ≈ −2.2%. Unconditional EV ≈ 0.125 × (−2.2%) + 0.875 × (~0, no fill) ≈ −0.3%, dominated by high probability of no fill at all.

Recommendation: size = 0. DEFER. Gate re-engagement on a confirmed exchange listing date/time verified in the price provider (lesson 2); if/when confirmed, do not hard-code to the raw open minute (lesson 1) — probe for a fillable bar 30-60min post-print. Even then base-rate skew is neutral-to-negative for longs and the favored fade side is likely unborrowable day 1. Flagged the dossier's 2026-07-31 impact_window as fabricated/inconsistent with sourcing.

## Round 2 — Rebuttal

### Bull rebuttal
Conceded: Bear/Quant are right — not tradeable by 7/31; "H2 2026" is the only sourced fact and 2026-07-31 is an unsourced placeholder. Retracted the implicit claim that the "solid-state" label alone earns a premium over liquid-electrolyte peers (no dossier evidence for differentiation — would be inventing a fact). Did not contest Quant's base-rate math, only flagged it borrows a peer distribution with zero PRLG-specific conditioning (no deal structure/PIPE/redemption/lockup data known).

Smallest confirmable trigger to re-engage: dated SEC filing or press release (ideally second source) with a specific closing/listing date; PRLG live and confirmed in the price provider (non-stub); basic deal-structure facts (PIPE size, redemption rate, lockup schedule); ideally 30-60min of liquid post-open data before any entry decision.

Revised action: No trade now; size = 0 through 2026-07-31; re-scout only once a dated, sourced listing announcement appears, and re-run the panel with fresh evidence.

### Bear rebuttal
Noted unanimous convergence on DEFER/NO TRADE across all three personas. Conceded that Bull's proposed entry/exit mechanics (gated entry, 30-60min liquidity wait, trailing stop, small size) are sound risk management IF a listing does confirm — not conceding the trade itself is attractive, only that the structure isn't reckless.

Sharpened risk: CFIUS/national-security review on a Taiwan-based, China-adjacent-supply-chain issuer is a binary, fat-tailed, largely unpriced deal-completion risk that the Quant's peer cohort (all US/Euro-domiciled: QS, MVST, RMO, SES, SLDP, FREY) does not capture — categorically different from generic de-SPAC redemption/PIPE overhang, and could produce a permanent "no listing ever" outcome, not just a slip to Q4.

Final: NO TRADE, size = 0, watchlist only, pending (a) confirmed dated listing via a second non-Electrek source verified live in the price provider, (b) lockup/PIPE/redemption disclosure, (c) explicit CFIUS status clarity (or absence of red flags).

### Quant rebuttal
Confirmed convergence explicitly — all three land on "no trade yet" via three independent frames (narrative, risk, base-rate/EV).

Incorporated Bear's CFIUS risk: this is a deal-completion hazard, so it lowers P(tradeable) rather than P(win|tradeable). Revised P(tradeable by 2026-07-31) from 0.10-0.15 down to 0.08-0.12 (haircut ~5-10pts for cross-border/Taiwan-China-adjacent review risk). Conditional EV unchanged at ≈ −1.2% gross / −2.2% net; 2-week drift still negative-skewed (P(down>10%)≈0.50) — CFIUS is binary-completion risk resolved before the print, doesn't rescue the day-1 long.

Minimum bar to flip to tradeable (all required): (a) live non-stub quotes in the price provider (e.g. `toa price PRLG --provider twelvedata` returning real prints, not stub data); (b) confirmed dated first-trade/listing date from a primary source; (c) day-1 liquidity ≥ USD 5-10M notional with quoted spread ≤ 50-75bps in the 30-60min post-print window; (d) PIPE/redemption/lockup terms disclosed. EV recalculation once (a)-(d) exist should use live order-book depth; act only if EV_net > 0 and clears a ~0.5 Sharpe-equivalent hurdle, sized at ≤0.25×Kelly given the fat left tail.

Final numeric: confidence this is NOT currently actionable = 93/100. Confidence in the long-term solid-state thesis IF the listing confirms and prices = 45/100 (narrative real but pre-revenue; de-SPAC cohort mostly underperforms 6-12mo post-list — tradeable ≠ good trade).

## Round 3 — Convergence (synthesizer, opus)

**hypothesis:** ProLogium (PRLG) Nasdaq listing at ~USD 3.8B is NOT currently tradeable. The only catalyst source is a single stale Electrek article (2026-05-27) citing an imprecise "expected H2 2026" close; the dossier's 2026-07-31 impact_window is an unsourced placeholder inconsistent with a ~150-day window. Direction: **no_trade**. Confidence: **93/100** (that this is not actionable now).

**plan:**
- ticker: PRLG
- action: no_trade / hold (watchlist only)
- entry: null — pending confirmation (do NOT schedule a leg against "H2 2026"; per Lime IPO lesson, no timestamp fabricated from an imprecise window)
- exit: null — pending confirmation
- expected_profit_pct: 0 (conditional EV of a naive day-1 long ≈ −1.2% gross / −2.2% net; unconditional EV ≈ −0.3%, dominated by P(no fill) ≈ 0.85-0.92)
- re-scout trigger (all required to flip to tradeable): (1) confirmed dated listing from a second, non-Electrek primary source; (2) live non-stub quotes in price provider; (3) day-1 liquidity ≥ USD 5-10M notional, spread ≤ 50-75bps in 30-60min post-print window; (4) PIPE/redemption/lockup terms disclosed; (5) CFIUS/national-security review status clarified. Minimum bar to re-open analysis: (1) + (2).

**dissent:** Rare near-unanimous DEFER — all three personas agree size=0. The one unresolved divergence is the nature of the dominant tail risk: Bear frames it as a binary, fat-tailed, largely unpriced CFIUS/national-security review risk (Taiwan-based, China-adjacent supply chain) that the US/Euro-domiciled peer cohort doesn't capture; Quant absorbs CFIUS only as a modest probability haircut (0.10-0.15 → 0.08-0.12) within a market-structure framing (P(no fill), redemption/PIPE/warrant overhang, negative post-list drift), leaving conditional EV unchanged; Bull (retracted to size=0) retains a residual belief that the entry/exit mechanics would be sound risk management if a listing confirms — a claim Bear declined to concede makes the trade attractive, only executable. Log for post-mortem: whether CFIUS is a distinct fat-tailed binary (Bear) or a priced-in haircut (Quant) — if Bear is right, peer base rates systematically understate downside and no market-structure trigger bar suffices without explicit CFIUS clearance.

Paper-trading simulation only. Not financial advice.
