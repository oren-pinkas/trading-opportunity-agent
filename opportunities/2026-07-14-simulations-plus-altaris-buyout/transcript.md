# Debate Transcript — SLP / Altaris Buyout

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel` (bull sonnet, bear sonnet, quant opus, synthesizer opus).

Sources:
- Simulations Plus to Be Acquired by Altaris For Approximately $375 Million — BusinessWire, 2026-06-16.
  https://www.businesswire.com/news/home/20260616126655/en/Simulations-Plus-to-Be-Acquired-by-Altaris-For-Approximately-$375-Million
- Live price: `toa price SLP <ts> --provider twelvedata` — SLP last USD 18.225 (2026-07-20 session); USD 18.24 confirmed on 2026-07-15 session.

Lessons injected (from prior regulatory-event debate, 2026-07-08-caesars-icahn-fertitta-bidding-war):
1. Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward.
2. Never map a corporate/legal calendar date directly onto an execution timestamp — derive fill time from the nearest valid trading session.

## Round 1 — Independent research

### Bull (confidence 55/100)
Deal: Altaris agreed 2026-06-16 to acquire SLP for USD 18.50/share cash, ~USD 375M total, board-approved, expected close Q4 2026, pending shareholder vote. Could not obtain a live price this round (`toa price` returned HTTP 429 on repeated attempts). Thesis: clean binary catalyst with a hard date; low antitrust friction (niche pharma-simulation software target, healthcare-focused PE buyer, no obvious HSR/CFIUS exposure); topping-bid optionality is the real alpha — SLP is a profitable, capital-light software business that could draw a strategic or rival PE bid, especially if a go-shop provision exists and the termination fee is low. Flagged the go-shop window and termination fee as the critical unconfirmed fact. Proposed: long SLP, arb-sized, exit at close or opportunistically on a topping-bid headline. Explicitly deferred pinning entry/exit timestamps until live pricing was available, per lesson 2.

### Bear (confidence 20/100)
Sourced spot: SLP USD 18.225 (2026-07-20 session, twelvedata). Spread to deal = USD 0.275 (1.51%), annualizing to ~3.3% over a ~5.4-month hold to Q4 2026 — below short-term T-bill yield, before costs. Read: the tight spread signals the market already prices high deal-close probability; the easy money was captured right after the 2026-06-16 announcement. Risk/reward: ~1.5% upside vs. 25-30%+ downside (SLP re-rating to an estimated USD 12-14 standalone value) if the deal breaks — roughly 1:15. Named specific break paths: shareholder-vote failure (dossier itself flags the vote as still pending; SLP is a founder-controlled, low-float name), routine disclosure litigation (adds timeline risk, rarely breaks deals), an unconfirmed financing contingency (Altaris is a PE sponsor), and antitrust/HSR overlap risk given Altaris's existing healthcare portfolio (the item bear would most want checked before touching this).

### Quant (confidence 20/100)
Sourced spot: SLP USD 18.225 (2026-07-20 and 2026-07-15 sessions, twelvedata). Spread 1.51%, annualized ~4.7% gross (mid-Q4 close estimate: 2026-07-21 to 2026-11-15, 117 days, 0.320yr). Assumed P(complete)=94%, P(break)=6%, break price USD 14.00 (-23%). EV = 0.94×(+0.275) + 0.06×(-4.225) = gross +0.005/share (+0.027%); net of ~15bps round-trip costs (-0.0273/share) = **net EV ≈ -0.022/share (-0.12%)**. Sensitivity: even at 96% complete / USD14 break, annualized only ~1.2%; at 92% complete, clearly negative. Verdict: pass — reward/risk of 0.275 up vs. 4.225 down (~1:15) requires ~94%+ precision on completion probability that isn't underwritable at this spread. Would only enter below ~USD 17.80 (spread >3.9%, annualized >12%).

## Round 2 — Rebuttal

### Bull (confidence 30/100, down from 55)
Conceded the static-spread case is weak once real price data (USD 18.225) is in hand — agreed with bear/quant that base-case carry doesn't compensate for routine break risk. Pushed back only on tail-modeling: argued quant's single break outcome (P=6%, USD 14.00) collapses two distinct tails — deal-breaks-with-no-bidder (craters to USD 12-14) vs. deal-contested-because-a-topping-bid-emerges (downside capped near USD 18.50, upside USD 20-22+). Acknowledged it still lacks the one fact that would make this rigorous: go-shop window status and termination fee. Would only re-enter on confirmed active go-shop or 8-K/proxy evidence other bidders were contacted. Scaled back to a small-starter-position stance at most.

### Bear (confidence 15/100 long spread, down from 20; 25/100 conditional-short — not initiated today)
Noted that bear's qualitative 1:15 read and quant's independent EV math converged without collaboration — treated as a strong signal. Granted topping-bid optionality nonzero weight but insufficient to move the EV needle absent deal-protection confirmation. Named the actual triggers that would turn this into a real short: Altaris financing/credit-market wobble (spread widening on sponsor debt, syndication trouble), a leak suggesting a contested vote, or an antitrust/HSR second request. None confirmed today — position is monitor-only, not short-now.

### Quant (confidence 25/100, up from 20)
Modeled topping-bid probability `t` explicitly: gross EV = 0.005 + 1.5t per share (assuming topping exit ~USD 20). Breakeven at t=1.5% (trivially low threshold). At bull's optimistic t=5-10%, net EV ranges +0.29% to +0.70%, but annualized (~0.4yr hold) that's only ~0.7-1.7% — still below the ~4.7% T-bill benchmark: positive EV but negative *excess* EV. Cross-checked bear's deeper break assumption (USD 12-13 vs. quant's USD 14): at USD 13 break, breakeven t rises to 5.5%, achievable only at bull's full optimistic scenario. Conclusion: spread capture fails, topping lottery fails on opportunity cost, short vol fails (no premium to harvest, naked tail risk). Credited bull 5 points for a mathematically real, if capital-inefficient, tail.

## Round 3 — Synthesis

**Hypothesis:** SLP at USD 18.225 vs. the USD 18.50 all-cash Altaris offer is a high-completion-probability deal whose spread capture, after costs and against a ~4.7% T-bill alternative, yields negative excess return. Topping-bid optionality is real but unquantifiable without confirmed go-shop/termination-fee terms; even at a defensible optimistic topping probability, excess EV stays negative. No edge in the long spread, the topping-bid lottery, or a naked short. **Direction: no_trade. Confidence: 78/100.**

**Plan:** No trade. Re-entry triggers: (1) SLP trades at or below ~USD 17.80 (spread >3.9%, annualized >12%); (2) 8-K/proxy confirms an active go-shop with a sub-3% termination fee; (3) evidence other bidders were contacted; (4) short-side only — Altaris financing trouble, contested-vote leak, or antitrust/HSR second request.

**Dissent:** The sharpest unresolved disagreement is the weight of topping-bid optionality, hinging on a fact the panel never obtained — go-shop window status and termination-fee size. Bull argues the sponsor/target profile makes a competing bid materially more likely than a generic deal. Bear and quant counter that without deal-protection confirmation, any topping probability large enough to matter is unsupported speculation, and opportunity cost against T-bills kills even the optimistic case. All three converged on no_trade for structurally different reasons — quant on excess-EV/opportunity cost, bear on asymmetric break risk, bull reluctantly on missing information rather than absent opportunity. If a subsequent filing reveals an active go-shop with a low break fee, bull's thesis reactivates and the consensus fractures — the primary post-mortem watch item.
