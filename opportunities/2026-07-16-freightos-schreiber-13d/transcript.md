# Research Debate Transcript — 2026-07-16-freightos-schreiber-13d

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Run date: 2026-07-22.

## Context

Event: Freightos founder Zvi Schreiber, previously ousted, filed a Schedule 13D pushing for board change and a return to a high-growth strategy at Freightos.
Ticker: CRGOW. Impact window: 2026-08-15.
Source: "Activist Stakes Tracker - Alpha-Investor 13F", https://www.from2028.com/activists.html, accessed 2026-07-16T11:35:00Z.

Data note: `toa price CRGOW` and `toa price CRGO` both returned HTTP 400 (Twelve Data "Bad Request") as of 2026-07-22T10:13Z — no live quote fetchable for either the presumed warrant (CRGOW) or common (CRGO) ticker. Treated as a hard tradeability constraint throughout the debate, not a tooling glitch.

Relevant lessons injected (via `toa lessons-relevant --type economic --tickers CRGOW`):
1. Anchor entry to a live pre-event quote, not the research-day price; re-derive or void if drifted. (2026-07-01-ism-mfg)
2. If X already rallied to 52-week highs pre-event, treat the move as priced-in — fade or shrink, don't chase. (2026-07-01-ism-mfg)
3. Skip trades whose only positive-EV path is an unfillable conditional entry. (2026-07-02-june-jobs)
4. Require a differentiated surprise vs. consensus before trading a known regime shift. (2026-07-02-june-jobs)

## Round 1 — Independent Research

### Bull (sonnet)
A Schedule 13D — not a passive 13G — from an ousted founder is a credible activist catalyst archetype: founder-led campaigns compress the market's timeline for a strategy reset relative to outside-raider 13Ds, since the founder can point to specific post-ouster execution failures. The market typically reprices on the *possibility* of a proxy fight or settlement well before the outcome is known.

Evidence is limited to the single tracker source (from2028.com, accessed 2026-07-16): filer identity, instrument type, stated intent, and the 2026-08-15 window. Missing: stake size/%, share count, Freightos financials, board composition, and any live price (`toa price` 400'd on both CRGOW and CRGO).

Proposed action: small starter long in CRGOW (or CRGO common if the warrant proves illiquid), entered on confirmation of a live quote ahead of 2026-08-15, scaled as stake %/company response emerges; don't chase if the 13D headline already moved the price.

Confidence: 40/100. Capped by no stake size, no live price, no financials. Would rise with a confirmed quote, disclosed stake % (>5%), board/company response. Would fall if the ticker proves untradeable or the stake is nominal.

### Bear (sonnet)
CRGOW's "W" suffix almost certainly denotes a warrant, not common stock — embedded leverage/time decay, thin-to-nonexistent volume outside SPAC-adjacent pockets, and the dossier discloses zero strike/expiration/exercise-ratio terms. Without those, any target price is unanchored — this is the whole trade, not a gap to caveat around.

Base rate for "ousted founder returns via proxy fight" resolving within one quarter is low; these campaigns typically run 6-18 months of proxy solicitation, litigation, or negotiated settlement. The 13D has been public since at least 2026-07-16 — if it were going to move the stock on the news itself, it likely already did; by entry it's 6 days stale.

Missing: stake size/%, board composition and any company response, common vs. warrant volume/float, borrow availability, and the source itself (a tracker site, not a primary EDGAR filing).

Loss scenario: hold into 2026-08-15 expecting a governance re-rate; board rejects the demand or litigation drags, and the warrant has no bid/ask to exit — stuck in an illiquid instrument with no live price feed (confirmed 400s on both tickers).

Action: NO TRADE. Confidence in bull thesis being tradeable: 10/100. Would change with a confirmed common-stock ticker with live quotes, actual EDGAR 13D stake %/demands, a scheduled shareholder vote before 2026-08-15, and demonstrable liquidity.

### Quant (opus)
Base rate for a tradeable ~1-month move from a founder-led activist 13D at a small/micro-cap: ~35% ±20% — wide error bars given the dossier is a single tracker line with no filing date, stake size, or float data. The initial-filing pop, if any, has likely already happened; source is 6 days stale.

CRGOW is almost certainly a Freightos warrant (SPAC-legacy listing) — leverage cuts both ways: a 10% common move could be 25-40% on the warrant, but spreads can run 10-30%+ and warrants can expire worthless. No expiry/strike given.

EV (illustrative, assumption-laden): P(up)=35% at +30%; P(flat/decay)=45% at -8%; P(down)=20% at -25%.
EV = 0.35(30) + 0.45(-8) + 0.20(-25) = 10.5 - 3.6 - 5.0 = **+1.9% gross**. A 15-30% round-trip warrant spread alone swamps this — net EV is negative even under generous assumptions.

Executability: `toa price` 400'd for both CRGOW and CRGO — no live quote, no volume, no spread data. Per lesson 1 (anchor to a live quote) and lesson 3 (don't record an unfillable trade), there is no fillable entry.

Recommendation: SKIP. Confidence: 78/100 on the skip verdict (low confidence on the underlying event direction itself, high confidence that the process disqualifies the trade regardless).

## Round 2 — Rebuttal

### Bull rebuttal
Concedes the liquidity point is likely fatal — won't defend a trade that can't be priced or executed; this is disqualifying under our own process rules, not a minor caveat.

Pushes back: (1) quant's +1.9% gross EV actually supports the thesis direction — the 35% upside weight isn't unreasonable for a founder-led 13D, and bull's own confidence (40) was already discounted for this same execution gap. (2) Bear's 6-18mo base rate is the right reference class for a *control outcome* but conflates "thesis takes quarters to resolve" with "no near-term catalyst" — 13Ds on illiquid micro-caps often pop on the filing disclosure itself, independent of ultimate resolution.

Concedes that "near-term pop" is speculative without stake size, which bull doesn't have. Revises confidence to 20/100, leaning to NO TRADE on process grounds, not conviction grounds. Revival conditions: a quotable CRGO print with visible volume, plus disclosed stake >5%.

### Bear rebuttal
Notes convergence with quant from two independent angles (structural/timeline vs. mechanical/EV) — that should carry weight.

Pushes back: 40/100 (bull's original) was still too generous for an instrument bull cannot define — not knowing if it's common, warrant, or unit, nor strike/expiry if a warrant, isn't "a small position with unknowns," it's no position. Also reinforces the staleness point: 13Ds resolve over quarters via negotiation/proxy fights, and bull hasn't shown a mechanism tying the specific 24-day window to a price event.

Confidence unchanged: 10/100 in bull thesis tradeability. Would change with a confirmed live quote, disclosed stake %/explicit demands, and confirmation of instrument type with known terms.

### Quant rebuttal
Sharpens with numbers: with +1.9% gross EV and a 15-30% warrant spread, Kelly f* is negative — the mathematically correct size is zero, not "small starter." No position size rescues a negative-net-EV trade.

Instrument swap to CRGO common would cut spread to ~1-3%, lifting net EV positive — but CRGO also 400'd, so the one instrument that could flip this is unconfirmed as fillable. The blackout is a veto, not a gap.

Sharpens bear's timeline point numerically: the 24-day window (2026-07-22 → 2026-08-15) captures roughly 10-15% of the historical 13D-to-material-move latency distribution (median latency ~3-6 months, fat right tail).

Verdict: no size/instrument/timing flips this to positive EV given the data blackout. Recommendation: SKIP. Confidence: 80/100.

## Round 3 — Synthesis (opus)

**Hypothesis:** Schreiber's 13D is a real but weak catalyst. It is already ~6 days stale, founder/activist campaigns historically resolve over 6-18 months rather than weeks, and the ~24-day window to 2026-08-15 captures only the low-probability tail (~10-15%) of the 13D-to-material-move latency distribution. The only instrument with a defensible risk/reward (CRGO common, tight spread) is unquotable, and the default instrument (CRGOW warrant) carries undisclosed terms and a 15-30% spread that turns a marginally positive gross EV (+1.9%) net-negative. There is no fillable, priceable entry.
Direction: **none**. Confidence: **78/100** (high confidence in the no-trade verdict; low confidence in the underlying event direction itself).

**Plan:**
- Ticker: CRGOW (CRGO common referenced but also unquotable)
- Action: **no_trade**
- Entry: null
- Exit: null
- Expected profit: null

**Dissent (for post-mortem):** The live disagreement is the catalyst-mechanism question, not liquidity (all three converged liquidity kills the trade regardless). Bull maintained an initial-filing "pop" is mechanically distinct from and front-loaded ahead of the multi-quarter resolution timeline bear/quant priced in; bear/quant rejected this, arguing no mechanism ties the specific 24-day window to a price event and any pop likely already happened in the 6 days since the filing went public. If CRGO/CRGOW moves materially near 2026-08-15, the miss was a mispriced catalyst-timing model (bull vindicated); if flat, the staleness/latency reasoning holds. Since the instrument was never quotable, this cannot be resolved from the trade outcome alone — a post-mortem should pull actual CRGO/CRGOW price history around the filing date and the impact date to adjudicate.
