# Research Debate Transcript — Faraday Future 1-for-150 Reverse Split

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` | Personas: bull (sonnet), bear (sonnet), quant (opus) | Synthesizer: opus
Debate run: 2026-07-23T15:35:53Z

## Event

Faraday Future (FFAI) executes a 1-for-150 reverse stock split effective at the open of trading on 2026-07-24.
Source: [Stock Split Calendar & Reverse Splits News Live Feed - Stock Titan](https://www.stocktitan.net/news/stock-splits.html), accessed 2026-07-22T12:26:30Z.

## Institutional lessons injected

1. Validate entry/exit timestamps fall within an open trading session (regulatory/CZR).
2. Never map a corporate/legal calendar date directly onto an execution timestamp (regulatory/CZR).
3. S/N < ~0.15 on a linear-EV fade is not a durable edge; simulate-plans has no path-dependent stop enforcement (regulatory/PLD).
4. An actual fill outside the planned entry band is an early falsification signal (regulatory/PLD).
5. Test-query the real price provider for exact timestamps during research before finalizing a plan (regulatory/NYAX).

---

## Round 1 — Independent Research

### Bull (sonnet)

Confirmed real price via `toa price FFAI 2026-07-23T15:30:00Z --provider twelvedata`: **FFAI = $0.0829** (TwelveData), implying a theoretical post-split open of ~$12.44 (150x). Reads the 150:1 ratio as an aggressive, textbook Nasdaq-compliance split for a name with a chronic dilution history (ATMs/converts). Thesis: first-session pop from short covering and retail momentum chasing the "reset" nominal price in a meme-adjacent EV/robotaxi name — explicitly a timing/momentum trade, not a fundamentals trade. Concedes the fade/dilution-exit bear case is real and plausible.

Proposed action: long, common stock only, entry in the first 5-15 minutes of the 2026-07-24 open (~13:30-13:45 UTC), exit same day close or next session; conditioned on re-querying the real post-split print before locking entry, treating a fill far below ~$12.44 as invalidation (lesson #4).

**Confidence: 42/100.**

### Bear (sonnet)

No live price tool used; reasoned from priors. 150:1 is an extreme ratio signaling chronic distress; FFAI is a serial reverse-splitter (repeat splitters are value destroyers, not turnarounds). The split is fully anticipated (requires prior disclosure/vote), so there's no informational edge. Academic base rate: distressed-microcap reverse splits precede continued underperformance over 3-12 months, largely because the split re-enables further dilutive financing. No fundamental catalyst is bundled with this event — pure mechanics. Historical immediate-direction outcomes are genuinely ambiguous (pop vs. fade), which per lesson #3 is a low-S/N, non-durable edge.

Direction: no-trade default, slight bearish lean if forced.

**Confidence in a tradeable edge: 15/100.**

### Quant (opus)

Framed the split as economically neutral by construction (market cap unchanged). Cited academic literature showing -10% to -30% negative abnormal drift over the following quarter for distressed-microcap reverse splits — but that is a multi-week/month signal, not a 1-day one. On the 1-day window, direction is close to a coin flip with a slight negative tilt, often preceded by a brief pop. FFAI's ~20% daily idiosyncratic vol swamps any 1-day drift edge (S/N < 0.15, lesson #3). Assumed pre-split price range $0.30-$1.50 (flagged explicitly as an unverified assumption, no live tool access).

Explicit EV calc for a 1-day short: gross EV -1.8%, minus borrow cost (~0.3%/day, FFAI is HTB) and 2-4% spread/slippage → **net EV ≈ -5%**. Flagged critical risk of split-adjusted price-feed artifacts if entry/exit straddle the split date (lesson #5).

Direction: NO TRADE / stand aside — requires net EV > 0 and S/N ≥ 0.15 to deploy capital; fails both.

**Confidence in stand-aside: 75/100.**

---

## Round 2 — Rebuttal

### Bull rebuttal

Distinguishes trading the open-print reaction (where pop/short-covering dominates) from quant's full-day-close EV math, which was built for a different trade. Argues the split isn't "fully priced in with zero edge" — mechanical dislocation (odd-lot rounding, forced share reconciliation, momentum flow toward a "normal-looking" price) is a real, if noisy, microstructure event. Concedes quant's S/N point is the strongest point in the debate and commits to smaller size / first-minutes-only exit / hard stop on feed-artifact risk. Concedes bear's multi-month distress framing is correct but off-timeframe. Holds confidence at 42/100 (does not raise it), sharpens trade design instead.

### Bear rebuttal

Directly attacks bull's core mechanism: "150:1 forces short covering" is asserted with no short-interest or borrow-rate data, and — per quant's parallel rebuttal — is mechanically wrong: a reverse split divides short share counts by the same ratio, so dollar exposure is unchanged and nothing forces a cover. Flags the internal inconsistency of conceding the bear case is "plausible" while holding confidence at 42/100 with no offsetting data. Notes bull's real price quote is a genuine edge over bear's own Round 1 gap, but a pre-split quote says nothing about the post-split print — arithmetic, not forecast. Revises confidence in a tradeable edge **down to 10/100** after the short-covering mechanism is shown to be broken.

### Quant rebuttal

Accepts bull's price correction ($0.0829 → ~$12.44 theoretical, vs. quant's assumed $0.30-$1.50 → ~$45-$225) but shows the correction is largely price-level invariant for a percentage-based EV/base-rate argument — net EV and S/N conclusions hold. Notes the lower real price is mildly retail-friendlier (more plausible pop) but also implies more noise/lower S/N — a wash. **Refutes bull's short-covering mechanism as mechanically false**: reverse splits divide short shares 150x automatically; there is no forced-cover event. Stripped of that mechanism, bull's thesis reduces to "microcaps sometimes pop on the open," a coin flip priced at 42/100 that is negative EV after 2-4% round-trip friction. Agrees with bear's no-trade destination but pushes back on borrowing a 3-12-month academic drift to justify a 1-day directional short as overreaching from the cited evidence. Holds **NO TRADE, confidence 74/100** (nudged down 1pt for the marginally more-plausible-but-still-sub-EV pop).

---

## Round 3 — Synthesis (opus)

**Hypothesis:** FFAI's 1-for-150 reverse split (effective open 2026-07-24) is economically neutral by construction and offers no durable 1-day directional edge. The bull's central causal mechanism — that the 150x ratio "forces short covering" — is mechanically false: a reverse split divides short share counts by 150x automatically, with no forced-cover event. Stripped of that mechanism, the long thesis reduces to "distressed microcaps sometimes pop on the open," a near coin-flip that is negative EV after 2-4% round-trip friction. The bear's multi-month academic underperformance drift is real but off-timeframe for a 1-day trade and does not justify a directional short either.

**Direction:** no_trade
**Confidence:** 78/100 (in the stand-aside decision)

**Plan:** No position taken — no entry/exit/size. The one genuinely bullish primitive (the real quote, $0.0829 → theoretical ~$12.44 post-split) is arithmetic, not a forecast. Both non-bull personas independently price the residual "sometimes pops" idea as sub-EV after costs. No short-interest/borrow-rate data was ever produced to support the short-covering claim, and the claim is mechanically wrong regardless. FFAI's ~20% daily vol drives S/N below ~0.15; feed-artifact risk around the split ratio is elevated. Would only be revisited given hard data: a measured base rate of first-session pops for 150:1-class reverse splits, plus actual short interest and borrow rate.

**Dissent (for the post-mortem record):** The bull never got a Round 3 chance to rebut quant's mechanical refutation of forced short covering — the "unrebutted" status is procedural (both rebuttals landed in the same round), not conceded. The genuinely open empirical question none of the three personas resolved: what is the actual first-session (open-print) reaction frequency and magnitude for extreme-ratio reverse splits in meme-adjacent microcaps? All three positions rest on priors, not a measured 1-day distribution. If 2026-07-24 prints a sharp pop, that should not be read as vindicating the debunked short-covering mechanism — it should be read as evidence that this un-measured base rate needs to be quantified before the next reverse-split opportunity is judged.

---
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
