# Research Debate Transcript — easyJet Apollo Takeover Bid

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Opportunity: `2026-07-23-easyjet-apollo-bidding-war`.

## Event

Apollo Global tabled a GBP 5.7bn all-cash offer for easyJet, topping Castlelake's prior offer; the easyJet board switched its recommendation to Apollo, with a firm offer expected early August. (Euronews, 2026-07-10, "Apollo hijacks easyJet takeover with GBP 5.7bn bid, trumping Castlelake" — https://www.euronews.com/business/2026/07/10/apollo-hijacks-easyjet-takeover-with-57bn-bid-trumping-castlelake; accessed 2026-07-23T09:13:03Z). Dossier `impact_window`: 2026-08-05. Tickers: EZJ.L, APO.

## Round 1 — Independent opening positions

### Bull (sonnet)

- **Read**: Live, escalating cash bidding war; board flipped to support Apollo's topping bid — the strongest signal in M&A (management endorsement removes "will they say no" risk). Firm offer due early August, impact_window 2026-08-05, is a hard, near-term binary catalyst. Bidding wars historically see target price trade up toward/through offer price as the deadline nears.
- **Evidence**: Euronews 2026-07-10 (cited above). Dossier confirms board switch and "firm offer due early August."
- **Note**: `toa price EZJ.L 2026-07-24 --provider twelvedata` returned 404 — flagged as an unresolved symbol-format issue, not yet a market-data-unavailable verdict.
- **Proposed action**: Long EZJ.L (the target) into the firm-offer deadline. Entry at the nearest valid LSE session, exit at/after firm offer announcement (~2026-08-05, rolled to next open session per the CZR calendar-mapping lesson), modest/low-conviction sizing until the price-feed issue is resolved. Thesis invalidates if no firm offer lands by deadline, or if the actual fill prints outside a sane band.

### Bear (sonnet)

- **Read**: A GBP 5.7bn agreed cash bid with board recommendation is close to fully priced — this is merger-arb, not a growth story. The news is three weeks old (2026-07-10); by firm-offer time the spread should already be tight. Buying now bets on a higher bid or mispriced deal-break risk, not known facts.
- **Evidence**: Euronews 2026-07-10 (cited above). `toa price EZJ.L` for 2026-07-24 also 404'd for Bear — unable to confirm spread-to-offer levels independently, itself a caution flag.
- **Key risks**: (1) UK Takeover Code PUSU/firm-offer deadlines can slip or extend; (2) financing/leverage risk on a GBP 5.7bn LBO in an elevated-rate environment; (3) bidding-war reflexivity — Castlelake or easyGroup/Haji-Ioannou could re-enter or object.
- **Proposed action**: Avoid an outright directional long. At most a fade-the-euphoria/small-size arb-spread trade, entered only after confirming a valid EZJ.L quote at a real session near the firm-offer date — never mapping 2026-08-05 directly to a fill timestamp. Given low S/N on linear-EV fades and no path-dependent stop-loss in `simulate-plans`, leans toward no-trade.

### Quant (opus)

- **Base rates** (stated assumptions): board-recommended, financed, all-cash offer reaching completion ≈90%. Currently pre-firm-offer: P(firm offer posted near 2026-08-05) = 0.75; P(slip/extension) = 0.20; P(collapse) = 0.05. P(further counter-bid on target) ≈ 0.25 (target-side upside only, not acquirer-side).
- **EV calculation** (APO — the only priceable leg): deal size GBP 5.7bn ≈ USD 7.4bn vs APO cap ≈ USD 68bn (≈11% of cap). Conditional acquirer-side moves: firm offer posted +0.30%, slip 0.00%, collapse +0.20%. EV_gross = 0.75(0.30) + 0.20(0.00) + 0.05(0.20) = **+0.235%**. Costs (spread + slippage + fees) ≈ 0.10%. **EV_net ≈ +0.13%.** APO daily sigma ≈ 2%. Signal-to-noise = 0.235/2.0 = **0.12** — below the 0.15 floor from the PLD bid-deadline lesson.
- **Price check**: real `toa price --provider twelvedata` data for APO: 120.49 (2026-07-22T14:00Z), 119.04 (07-22T15:30Z), 119.79 (07-23T14:35Z), 120.235 (07-23T14:30Z), 120.72 (07-24T15:00Z) — 3-day range 1.4%, pure chop, no visible deal repricing. **EZJ.L is unpriceable**: `EZJ.L`, `EZJ.LON`, `EASYJET.L` all HTTP 404 across three dates; bare `EZJ` returns sparse bars at ~62.99 — not easyJet in pence (would be several hundred p), a different, wrong-scale instrument. Do not use it. Per the NYAX lesson, any EZJ.L plan resolves uninformative-neutral.
- **Proposed action**: The edge lives in the target (merger-arb spread capture, ~88-90% completion base rate), but that instrument cannot be priced here, so it cannot be traded. The only priceable instrument (APO) carries EV_net of 13bp against 200bp daily noise — sub-floor. Vote: no trade, or at most a token 0.25% notional long APO with a tolerance-window entry/exit around the 08-05 catalyst (never using the calendar date itself as a fill timestamp).

## Round 2 — Rebuttals

### Bull rebuttal

- **Where I disagree**: Bear's "close to fully priced" is asserted, not shown — Bear got the same 404, so "should be tight" is a guess. Quant's EV framework is sound but mis-scoped: running EV on APO's 11%-of-cap exposure kills a *different* trade (acquirer re-rate) than the one proposed (target re-rate into a bidding war) — a straw man against a trade Bull didn't make.
- **What they missed**: The core catalyst mechanic — board-recommended bids in active bidding wars routinely see target shares creep toward/through the new offer pre-firm-offer, distinct from post-announcement arb-spread compression. That edge sits on EZJ.L, not APO. Bear's risk list (PUSU slippage, financing, re-entry) is fair but bounded and dated — arguing for smaller size and a tight window, not zero.
- **What would change my mind**: Confirmation EZJ.L is genuinely unpriceable across every reasonable symbol/ISIN route, not just one variant.
- **Revised proposed action**: **Concedes no-trade on the target leg.** Two independent 404s plus the bare-EZJ wrong-instrument trap is a system-level block, not a transient feed issue — will not force a fake print to keep the thesis alive (toa-price-stub lesson). The bidding-war thesis cannot express cleanly via APO (acquirer-side EV is a different, weaker, already sub-floor signal). Moves to: no trade, revisit only if a valid EZJ.L/ISIN quote surfaces before 2026-08-05.

### Bear rebuttal

- **Where I disagree**: Bull's "still-escalating bidding war" assumes a contested process, but Castlelake never countered — this is a settled outcome awaiting paperwork, not an active war. Quant's EV only prices the wrong leg (APO) because the right leg (EZJ.L) is unpriceable — that's not a reason to trade APO at any size, it's a reason this venue can't express the thesis at all.
- **What they missed**: PUSU/firm-offer timelines routinely slip a week or more under the Takeover Code; nobody flagged whether the bid carries financing conditions (a real collapse path Quant's 5% may underweight). Also: Quant's own APO data shows pure chop three weeks in — evidence against urgency, not neutral noise.
- **What would change my mind**: A confirmed, quoted EZJ.L (or ADR/CFD equivalent) price showing a live, calculable spread-to-offer wide enough to justify carry given real deal-break risk, plus explicit confirmation the bid is unconditional on financing.
- **Revised proposed action**: All three independently hit the same wall — EZJ.L unpriceable, APO S/N (0.12) below the 0.15 floor. Not coincidence — the system is telling us this trade can't be executed within our own risk rules. **No trade, full stop — not even token APO exposure**, since sub-floor S/N was the exact lesson from a prior loss.

### Quant rebuttal

- **Where I disagree**: Bull's "long EZJ.L into the deadline" is an intention, not a plan — three independent symbol resolutions failed; a leg with no fill price has EV of exactly zero (NYAX lesson) and resolves uninformative-neutral. Bear's "mispriced deal-break risk" framing: P(collapse)=0.05 vs P(slip)=0.20 — slip is the modal risk, not break, and slip is worth only ~0-1% of spread widening, too small to fade profitably after costs either. Bear's fade is symmetric to Bull's long: both need a quote neither side can get.
- **What they missed**: Neither side priced the only tradeable leg. APO real data: 119-120.7 chop over 07-22 to 07-24, no deal repricing visible; deal ≈11% of APO cap; EV_gross +0.235%, costs ~0.10%, EV_net ≈ +0.13% vs ~2% daily sigma — S/N 0.12 < 0.15 floor. Even the priceable leg fails the bar.
- **What would change my mind**: (1) a resolving EZJ.L quote in pence with spread-to-offer above ~4%; (2) credible reporting of a Castlelake counter above GBP 5.7bn (P(counter) 0.25 → 0.45, making the target leg convex); (3) APO showing deal-linked drift rather than chop.
- **Revised proposed action**: **No trade.** Target leg unpriceable by three checks; acquirer leg S/N 0.12 below the 0.15 floor. Resolve neutral/no-trade; keep the 08-05 catalyst on watch.

## Round 3 — Synthesis (opus)

**Hypothesis**: Apollo's GBP 5.7bn all-cash topping bid for easyJet, board-recommended with a firm offer due near 2026-08-05, is a high-probability completion event (~90% base rate) already substantially priced in on the target side and immaterially reflected on the acquirer side. The tradeable edge is target-side merger-arb spread capture, and that leg cannot be priced in this venue: EZJ.L is unresolvable across three symbol formats (EZJ.L, EZJ.LON, EASYJET.L all 404; bare EZJ resolves to a wrong-scale, wrong-listing instrument at ~62.99). The only priceable leg, APO, carries EV_net ≈ +0.13% against ≈2% daily sigma — signal-to-noise ≈0.12, below the 0.15 floor. No expressible position has positive risk-adjusted expectancy. Direction: **neutral**. Confidence: **82** (confidence in the no-trade call itself — all three personas converged independently, and two independent blockers each suffice alone: an unpriceable target leg, and a sub-floor acquirer leg).

**Plan**: **No trade.** Ticker EZJ.L unpriceable; APO fails the S/N floor even at token size. Watch 2026-08-05 (firm offer / PUSU deadline); re-open only if a valid EZJ.L or ISIN-level quote becomes obtainable before then.

**Dissent** (strongest unresolved disagreement, kept for the post-mortem): Bull and Bear converged on no-trade for *incompatible* reasons the debate could not adjudicate. Bull's residual claim: the edge was real and target-side; only a tooling gap (symbol resolution) blocked it — fixing EZJ.L pricing could have produced a legitimate long into 08-05, and Bear's "close to fully priced" was asserted, never measured (no one ever obtained the actual spread-to-offer). Bear's residual claim: even with a perfect quote, this is a thin, three-week-stale, ~90%-base-rate arb whose remaining spread compensates for slip/financing risk, not alpha, worsened by `simulate-plans` having no path-dependent stop-loss to manage a deal-break gap. This is unresolvable without the missing quote — the debate could not falsify either side because the measurement was unavailable, which is itself the lesson worth keeping. Secondary dissent: Quant would have accepted a token 0.25% APO long in Round 1; Bear rejected any non-zero exposure below the S/N floor, and the stricter reading won on the grounds that sub-floor sizing converts a risk rule into a suggestion.

## Durable lesson for institutional memory (data layer)

UK LSE-listed equities are not reliably resolvable via the twelvedata provider in this system. For easyJet, all of `EZJ.L`, `EZJ.LON`, and `EASYJET.L` returned HTTP 404, and the bare root symbol `EZJ` silently returned a different instrument at ~62.99 — plausible-looking but wrong listing and wrong scale (same failure class as the toa-price-stub-default note: the tool returns something that looks like a price instead of failing loudly). Operational rules going forward: (1) before accepting any non-US-listed ticker into a plan, resolve the quote first — if the exchange-suffixed symbol 404s, treat the root symbol as poisoned, not as a fallback, and verify scale/currency against a known reference before using it; (2) a leg with no verifiable fill price has EV of exactly zero — never write an entry/exit price that wasn't actually fetched; (3) flag non-US-listed primary tickers as pricing-at-risk during scouting, so a full three-round debate isn't spent on a thesis the venue cannot price; (4) when the only priceable leg is an acquirer whose deal exposure is a single-digit percentage of market cap, expect sub-0.15 S/N by construction — screen this out before running the EV computation.
