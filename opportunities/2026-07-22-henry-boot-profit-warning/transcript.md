# Research debate transcript: Henry Boot second profit warning (2026-07-22)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet),
quant (opus). Synthesizer: opus.

Event: Henry Boot (BOOT.L, LSE-listed UK property/construction group) issued
its second profit warning of 2026 on 2026-07-22, warning annual pre-tax profit
will land significantly below the GBP 20.4M market expectation, citing Middle
East conflict (Iran war) and domestic UK political uncertainty hitting
land-plot sales. Next preliminary results expected around 2027-03-24.

Source: "UK's Henry Boot warns on profit again as Iran war, domestic nerves hit
sales" - MarketScreener, accessed 2026-07-22T17:49:00Z,
https://www.marketscreener.com/news/uk-s-henry-boot-warns-on-profit-again-as-iran-war-domestic-nerves-hit-sales-ce7f51d8d08ff62d

**Data constraint (binding throughout the debate):** `toa price BOOT.L ... --provider
twelvedata` returned `HTTP 404` — no verified current price, market cap,
volatility, or borrow cost was available to any panelist for this LSE ticker.

Relevant institutional lessons injected (general EV/trade discipline from other
past debates, not BOOT-specific):
- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
  ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down.
- Discount post-earnings negative base rates when the name is already near its
  52-week low: most of the drawdown may already be priced in.
- A catalyst that already drove a large run/reaction is priced in — do not
  re-bet the same fundamental as a fresh trigger.
- When directional EV is ~0, log NO TRADE rather than manufacture a minimal
  directional position "for the learning loop."
- Anchor entry prices to a live quote at the actual entry timestamp; abort/re-price
  if the stock has run away from the modeled entry.

---

## Round 1 — Independent research

### BULL (sonnet)

Weak-to-moderate bullish case, confidence 35-40%. This is a timing problem
(deferred land-plot revenue), not value destruction — no impairment,
balance-sheet stress, or lost customer cited. Two warnings in one year likely
represents capitulation/overshoot selling by momentum holders, a setup for a
mean-reversion bounce once forced sellers are flushed. The 8-month gap to next
prelims is a runway for a "no news is good news" drift back up if Iran/UK
political noise de-escalates. Proposed action: delayed entry (not day-of) long
BOOT.L after the initial post-warning air-pocket sell-off (1-3 trading days),
confirm a live quote before filling, exit ahead of the 2027-03-24 prelims.
Explicitly flagged the missing price data as a material gap for sizing any
real trade.

### BEAR (sonnet)

NO TRADE, or at most a small short bias, confidence ~35-40%. A second warning
in one year is a credibility problem, not a one-off macro shock — management
leaning on macro twice should make the market discount forecasting ability,
not just the quarter's number. Land-plot sales are structurally
lumpy/discretionary (buyers can walk from options cheaply), so this
vulnerability doesn't fade with the headlines. Risks the bull underweights:
(1) repeat-offender re-rating triggering analyst FY2027 cuts and possible
mechanical index/passive selling; (2) no near-term catalyst — an 8-month dead
zone bleeding opportunity cost with no validating datapoint until March; (3)
geopolitical overhang is unpriceable and can worsen, not just resolve; (4) no
verified price makes any "already priced in" argument unfalsifiable in either
direction.

### QUANT (opus)

NO TRADE, confidence 32. Cannot compute a real EV — no verified price, market
cap, volatility, or borrow cost (twelvedata 404s BOOT.L). Illustrative,
assumption-laden EV sketch: P(further drift down over 8mo)=50%, magnitude
-12%; P(flat)=20%; P(relief squeeze)=30%, magnitude +15%. As first computed:
gross EV ≈ +1.5% (later corrected in R2 — see below), but net EV after
~4-8%/yr borrow and slippage on an illiquid name is ~0 or negative — trips the
no-edge filter. Listed the data needed to make this tradeable: a working price
feed (try `BOOT.LON` / `BOOT:LSE` / an ISIN-based feed), a vol/options chain
(defined-risk only, never naked short if taken), borrow cost, and the exact
gap already taken on 2026-07-22 vs. warning #1 to size remaining downside.

---

## Round 2 — Rebuttal

### BULL (sonnet)

Concedes the "repeat offender" credibility framing is stronger than first
credited — two warnings in a year does raise the odds this is model-level
lumpiness, not pure macro bad luck, independent of any de-escalation. Revises
confidence down to ~32-35%. Pushes back on both bear and quant's "no near-term
catalyst = pure negative" framing: quant's own EV sketch is right-skewed
(30%/+15% vs 50%/-12%), so the real objection is a short-structure/cost
problem (borrow drag over an 8-month hold), not a directional-sign problem — a
long or defined-risk call structure avoids that drag entirely. Argues both
bear and quant's "unfalsifiable" complaint is a data-gap problem affecting all
three equally, not evidence specific to the bear case. Revised action: small
starter long / stand aside pending price and options-chain confirmation, add
only on a confirmed capitulation low. Confidence 33%.

### BEAR (sonnet)

Rejects "deferred not destroyed" as an unfalsifiable hypothesis dressed as
fact — nothing in the disclosure (no impairment, covenant language, or
order-book detail) actually confirms deferral over cancellation/permanent
demand loss. Rejects "capitulation/overshoot" on the same grounds: it requires
knowing actual price/volume on the print, which none of the panel has. On
quant's EV math: argues it validates NO TRADE, not long — the same
illiquidity/spread/no-price-feed problem that erodes a short's edge erodes a
long's entry/exit too, and quant weighted the downside path as
higher-probability, not merely larger-tailed. Drops the short bias entirely
(no longer even a "small short bias"). Revises confidence in NO TRADE up to
~45%.

### QUANT (opus)

Corrects a sign error from Round 1: the gross EV sketch is actually **≈ -1.5%**,
not +1.5% (P(squeeze)=30%×+15%=+4.5% vs. P(drift)=50%×-12%=-6.0%, flat
contributes 0). Confirms the distribution is right-skewed (bigger up-tail than
down-tail) — meaning if forced to hold optionality, long convexity beats short
convexity, siding with bull over bear on structure specifically. But: the
center of mass is still negative (skew improves shape, not sign); no verified
price means it's impossible to confirm how much of warning #2 is already
gapped in; no visible options chain means any position would carry naked,
undefined-risk delta; and bear's unfalsifiability point is the tiebreaker
given the 8-month data-free window. Recommendation: still NO TRADE, confidence
raised slightly to 36 (moved by bull on skew, not on sign or tradeability).
Explicit IF-tradeable contingent lean for the synthesizer: **long, not short,
not neither** — IF (a) a live quote confirms the post-warning gap is under
8-10% (overshoot not yet complete), (b) borrow/options data appears, and (c) a
defined stop is set. Absent those conditions: flat.

---

## Round 3 — Convergence (synthesizer, opus)

**Hypothesis:** Henry Boot's second 2026 profit warning is plausibly a
deferral-driven overshoot with a mildly right-skewed payoff (quant's corrected
EV: +4.5% up-tail vs. -6.0% down-tail, center of mass still negative). But no
verified price, market cap, volatility, borrow cost, or options chain exists
for BOOT.L (twelvedata 404), and an 8-month data-free window to the
2027-03-24 prelims removes any validating datapoint before then. With
direction unresolved and structure unpriceable, there is no measurable edge to
act on today. Direction: none. Confidence: 62 (in NO TRADE as the correct call
today).

**Plan:** BOOT.L, action = no-trade. No entry/exit prices — none can be
anchored without a verified quote. Expected profit: 0% (gross EV ≈ -1.5%
before borrow/slippage; net EV negative after costs). Contingent revisit,
requiring all three: (a) a live quote confirms the post-warning gap is under
8-10% (overshoot incomplete, not fully priced); (b) borrow cost and/or a
visible options chain becomes available, enabling defined-risk sizing; (c) a
hard stop can be set. If all three hold, the corrected skew favors a small
long or long-convexity/defined-risk structure — never a short (borrow-cost
drag plus adverse skew make a short strictly worse). Absent any one condition:
stay flat. Reassess near the 2027-03-24 prelims when a validating datapoint
returns naturally.

**Dissent (for post-mortem loop):** The convergence to NO TRADE is a
data-availability verdict, not a resolved directional one. Strip away the
missing price feed and the residual sign disagreement leans mild-bullish, not
neutral: quant's own corrected math shows a right-skewed distribution where
long convexity beats short, and quant explicitly sided with the bull over the
bear on structure. The unresolved crux is the bear's unfalsifiability
argument — "deferred not destroyed" and "capitulation overshoot" are both
unprovable without price/order-book data — which quant made the tiebreaker.
Post-mortem gold: if BOOT.L later bounced, log whether NO TRADE cost us a
positive-skew long we correctly identified but couldn't size because of a
tooling gap (twelvedata 404 on this LSE ticker), i.e. an infrastructure
failure masquerading as analytical prudence — arguably the single
highest-value fix to feed back into the loop.
