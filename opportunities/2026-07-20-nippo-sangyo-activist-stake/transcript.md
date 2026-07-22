# Research Debate Transcript — 2026-07-20-nippo-sangyo-activist-stake

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Debate run: 2026-07-22.

## Dossier under review

- Ticker: 9913T (Nippo Sangyo, Japan)
- Event: activist fund raised stake to 17% via off-market purchase; may engage board on capital allocation and board composition.
- Source: Special Situations Digest #22 (accessed 2026-07-13T08:51:16Z) — single tier-3 source.
- impact_window: 2026-07-20 (already passed as of debate date, 2026-07-22).

## Institutional memory injected (from `toa lessons-relevant --type economic --tickers 9913T`)

1. Anchor entry to a live pre-event quote, not the research-day price; if the live price has drifted materially, re-derive targets/EV or void rather than fill blind. (source: 2026-07-01-ism-mfg)
2. When the thesis is "catalyst reprices X higher" and X has already rallied into the event, treat the move as priced-in: fade or shrink, don't chase. (source: 2026-07-01-ism-mfg)
3. Skip trades whose only positive-EV path is an entry the harness cannot fill; if the executable leg's EV is near zero, don't record the trade. (source: 2026-07-02-june-jobs)
4. After a known regime shift, require a differentiated surprise vs consensus before shorting into a data print. (source: 2026-07-02-june-jobs)

## Round 1 — Independent research

### Bull (sonnet)

An activist fund pushed its stake in Nippo Sangyo to 17% via an off-market block purchase, with likely engagement on capital allocation and board composition (Special Situations Digest #22). This is the textbook activist-catalyst pattern: crossing a disclosure-relevant ownership threshold, in the current Japan corporate-governance-reform environment (TSE's push for capital-efficiency disclosure since 2023), is a classic re-rating catalyst.

Evidence is thin: single source only, no named fund, no stated target price, no confirmation of board contact, no current share price. The impact_window (2026-07-20) has already passed as of today (2026-07-22) — buying now risks chasing a stale catalyst rather than front-running it, per lesson 2.

Tool note: ran `toa price 9913T 2026-07-20T09:00:00Z` and `toa price 9913T 2026-07-13T09:00:00Z` without `--provider twelvedata`; both returned `"source": "stub:deterministic"` (fake values 371.96 and 306.28) — discarded, not used as evidence.

Proposed action: long 9913T, conditional on a live quote confirming the stock has NOT already run up sharply (per lesson 2, shrink/skip if at/near 52-week highs). Target: modest 8-15% re-rating vs pre-news base over a multi-week window (not a same-day pop trade). Sizing: small starter position pending verification of price and fund identity.

### Bear (sonnet)

Single tier-3 source — a newsletter, not a primary filing (no TDnet/EDINET Large Shareholding Report reference). Under Japan's FIEA, any stake at 5%+ requires a Large Shareholding Report within 5 business days; its absence here is a red flag — either sloppy sourcing or unverified chatter.

Three gaps: (1) no fund identity or track record, so follow-through probability can't be priced; (2) no board meeting/AGM date — JP activist campaigns often take 6-18 months and stall against cross-shareholding defenses; (3) no current price — per lesson 1, will not anchor to the research-day price, and the stub tool confirms no live quote is retrievable.

Tool note: ran `toa price 9913T` at two timestamps; both returned `"source": "stub:deterministic"` (371.96 on 2026-07-20T09:00Z, 74.11 on 2026-07-22T09:00Z — the ~5x discontinuity itself proves it's fake). No real price available without `--provider twelvedata`.

What's already priced in: news dated 2026-07-13, impact window 2026-07-20 has passed 3 days ago with no confirmed price move recorded — per lesson 2, any pop may already be in the price. What could blow this up: the fund could be passive/non-activist despite the newsletter's framing; JP boards routinely rebuff activists; an off-market block purchase can also signal an exiting strategic partner selling to a friendly party, not upside pressure.

Proposed action: SKIP — fails the verifiability and timeliness bar independent of thesis quality.

### Quant (opus)

Base rate (stated prior, not from dossier): ~25% probability that an activist-crossing-threshold event in a small/mid-cap JP industrial produces a tradeable clean move still capturable 2+ days post-disclosure. Magnitude distribution conditional on a move: 50% chance +2-5%, 35% chance +5-12%, 15% chance +15%+.

EV (entering now, pop-capture frame): 0.25 × (+7%) − 0.75 × (2%) = +0.25% gross. JP small-cap round-trip costs (spread/slippage/commission/FX/tax) ≈ 1.0-1.3%. Net EV ≈ −0.75% to −1.0% — negative after costs. The only positive-EV path was entering on the disclosure print itself, which has passed.

Tool note: ran `toa price` twice; both returned `"source": "stub:deterministic"` (461.65 for 2026-07-20, 274.57 for 2026-07-21 — a nonsensical ~40% overnight drop confirms fake data). Discarded.

Missing data needed for real sizing: live price/ADV, activist fund's track record, market cap/float/52-week range (to test the already-priced-in filter), borrow/liquidity.

Proposed action: PASS/VOID. Post-catalyst, negative net EV, no live price to anchor, no fund history to raise the 25% prior.

## Round 2 — Rebuttal

### Bull rebuttal

Bear's "tier-3 source" objection is a request for more evidence, not counter-evidence — a real Large Shareholding Report is legally required and checkable, not proof the claim is false. Bear's "friendly exit" alternative is unfalsifiable and cuts both ways given the dominant pattern of unsolicited activist stake-building in the current TSE reform climate. Quant's EV math assumes market efficiency/decay ("2+ days post-disclosure") that hasn't been verified — this is a low-circulation newsletter, not a wire story; the stock's actual price action, not the calendar, tells us whether the catalyst is stale.

What would flip bull to skip: live price already up double-digits since disclosure (confirms priced-in); confirmation this is a related-party/friendly transfer; no Large Shareholding Report within the legal disclosure window (undermines the 17% figure itself).

What would raise conviction: live price flat-to-down since disclosure (stale-but-unpriced is the best setup); fund name with an activist track record; ADV/float data showing a 17% stake is large enough to force engagement.

Conclusion: un-actionable without price data, but "un-actionable" is not "false" — get the quote before killing it.

### Bear rebuttal

Agrees with quant's arithmetic but thinks the 25% base rate is generous given zero EDINET confirmation — if the underlying filing doesn't exist, the true base rate is lower than 25%, pulling EV further negative than quant's estimate.

Bull's own rebuttal concedes staleness and downgrades to a conditional/small/hedged position — that is not materially different from bear's skip; there is no daylight left between "modest target, small starter, conditional on verification" and "don't take it." The "friendly exit / cross-holder to related party" alternative was never rebutted by either bull or quant.

Verdict: converged skip across all three independent reasoning paths — verifiability (bear's), timeliness/staleness (bull's own admission), and cost-adjusted EV (quant's, likely still too generous). Would reopen only with an EDINET filing number, fund identity, or a live price bar showing the move hasn't already happened.

### Quant rebuttal

Tested bull's "ride the multi-week campaign" reframe numerically rather than dismissing it, since it's the one argument that could flip the EV sign. Costs amortize better over a longer hold (fixed ~1.0-1.3% round-trip spread across a bigger expected move), but campaign-completion base rate is the binding constraint: P(re-rating within holding window | genuine activist accumulation) ≈ 30-35% (JP campaigns run 6-18 months and often stall, per bear). Must also discount P(this is genuine bullish accumulation at all, vs. bear's friendly-exit/cross-holding-unwind scenario) ≈ 55%.

Revised multi-week EV: 0.55 × 0.32 × (+9%) + (1 − 0.176) × (−2.5% adverse drift) − 1.15% costs = +1.58% − 2.06% − 1.15% = −1.63%. Worse than the pop-capture frame — the longer window imports carry/drift risk that outweighs cost amortization at a ~17.6% net success rate. PASS/VOID stands.

Would flip to positive EV only with ALL of: (1) primary EDINET/TDnet confirmation naming a fund with a 2+ campaign track record (raises P(genuine) toward 80%); (2) live price showing <3% move since 2026-07-20 (preserves entry, not yet priced in); (3) ADV/float supporting <0.5% one-way slippage.

## Round 3 — Synthesis (opus, neutral)

**hypothesis**
- statement: Reported 17% activist stake in Nippo Sangyo (9913T) rests on a single tier-3 newsletter with no primary EDINET/TDnet filing, no fund identity, no live price, and an impact window that already passed on 2026-07-20 — failing the verifiability, timeliness, and cost-adjusted-EV bars simultaneously.
- direction: skip
- confidence: 82

**plan**
- ticker: 9913T
- action: no_action
- entry: null / null
- exit: null / null
- expected_profit_pct: 0

Skip rationale: all three seats converged on PASS/VOID. Quant's cost-adjusted EV is negative in both frames tested (pop-capture: -0.75% to -1.0%; multi-week campaign: -1.63%). Bull never established an actionable long — its own position degraded to "un-actionable without a live quote." No trade is placed.

Conditions to reopen (all three required): (1) primary EDINET/TDnet confirmation — a Large Shareholding Report naming a fund with a 2+ campaign track record; (2) live price showing less than 3% move since 2026-07-20 (confirms not yet priced in); (3) ADV/float data supporting under 0.5% one-way slippage. Absent all three, this stays voided rather than reconsidered later — the impact window has already lapsed, so even full confirmation would likely arrive too late for the original catalyst.

**dissent**

The unresolved crux, despite convergence: bull is right that "un-actionable" is not "false" — the panel skipped on absence of evidence (no filing found, no price fetched), not on counter-evidence, so a genuine campaign cannot be distinguished from a fabricated or misread one on the record available. The never-rebutted "friendly-exit / cross-holder-to-related-party" alternative is the live fault line: if true, the directional sign flips from bullish pressure to neutral-or-bearish, and neither bull nor quant ever addressed it directly — quant assigned it an implicit 45% weight without independent justification. A post-mortem should check whether the EDINET filing actually existed on 2026-07-20 and, if so, whether this skip was a correctly-priced pass or a missed verifiable catalyst.
