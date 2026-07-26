# Research Debate Transcript — Ryanair Q1 profit slump on Mideast fuel costs

Strategy: debate-three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. PAPER-TRADING SIMULATION ONLY — NOT FINANCIAL ADVICE.

Scope note: this debate was run in isolation for `2026-07-23-ryanair-q1-profit-slump-mideast`
only; no other opportunity's dossier was read or referenced.

## Event

Ryanair (RYAAY / RYA.L) reported Q1 net profit down 34% YoY, attributed to elevated
jet-fuel costs tied to the Mideast/Iran conflict and lower average fares. Management
stated "zero visibility" into H2/winter trading ahead of formal winter guidance.

- Source: Yahoo Finance, "Ryanair Q1 profit falls 34% on Iran war fuel costs, lower fares",
  https://finance.yahoo.com/markets/stocks/articles/ryanair-q1-profit-falls-34-112114255.html,
  accessed 2026-07-23T09:13:03Z.
- Impact window: 2026-09-30.

Institutional lessons injected (general earnings-type, not RYAAY-specific; via
`toa lessons-relevant --type earnings --tickers RYAAY,RYA.L`):
- Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
  ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down.
- Discount post-earnings negative base rates when the name is already near its
  52-week low — much of the drawdown may be priced in.
- Set intraday exits at least one minute inside the session boundary (bar-fill risk).
- A catalyst that already drove a large move to a price reflecting it is priced in.
- When the highest-confidence panelist says directional EV is ~0, synthesize to
  NO-TRADE rather than a token position.
- Anchor entries to a live quote fetched at the actual entry timestamp.

Price data cited below is sourced live via `toa price RYAAY <ts> --provider twelvedata`
(twelvedata, 1-minute bars).

---

## Round 1 — Independent research

### Bull (sonnet) — confidence 55/100

Direction: LONG RYAAY. Fuel-cost shock and fare softness are self-correcting/decaying
inputs (geopolitical fuel shocks fade as hedges roll; Ryanair trims winter capacity to
defend yields). "Zero visibility" read as a hedge disclosure, not a profit warning —
markets often overreact to admitted uncertainty as if it were bad news, setting up a
relief rally once formal winter guidance resolves the ambiguity. Cited: Yahoo Finance
source; 34% YoY profit decline; "zero visibility" language. Live check: RYAAY = USD 56.40
at 2026-07-23T15:00Z (twelvedata). Proposed: long RYAAY (cleaner ADR than RYA.L per prior
coverage notes), entry within 1-3 days of print digestion ideally on a dip (re-priced at
actual entry timestamp), hold into formal winter guidance release before 2026-09-30, exit
ahead of the date inside the session boundary; instrument = outright long or defined-risk
call/call-spread if IV elevated.

### Bear (sonnet) — confidence 30/100

Leans NO-TRADE. Earnings reactions are overwhelmingly same-day phenomena — by the time a
paper trade can be entered, the "easy" gap move is gone. The Mideast/Iran conflict and
elevated fuel costs are not new information; the genuinely new information is the 34%
magnitude and "zero visibility" language, but there is no consensus EPS/profit baseline
to judge whether this beat or missed expectations — flagged as the critical unresolved
unknown. Risks to any directional thesis: oversold-bounce risk (airlines often see relief
rallies post-gap), "zero visibility" may be boilerplate caution rather than a real
warning, fuel-cost reversal is a real un-hedgeable positive tail, and any short entered
now chases an already-happened move. Recommendation: NO-TRADE absent consensus-miss data,
continued negative momentum/volume, or a fresh forward catalyst before 2026-09-30.

### Quant (opus) — confidence 22/100

Base rate for airline exogenous-fuel-shock + guidance-withdrawal prints: ~70-75% negative
same-day reaction (median -4% to -7%), but only ~55%/45% down/flat-up drift over the
following 1-2 weeks (median drift ~-1.5%) — fuel-cost misses are among the most-forgiven
airline miss categories since the market can price/hedge the input directly.

Live price table pulled via `toa price RYAAY <ts> --provider twelvedata`:

| Timestamp (UTC) | Price (USD) |
|---|---|
| 2026-07-17 19:55 | 62.90 |
| 2026-07-21 19:55 | 59.095 |
| 2026-07-22 19:59 (pre-print close) | 58.445 |
| 2026-07-23 13:35 | 57.11 |
| 2026-07-23 15:00 | 56.40 |
| 2026-07-23 19:55 (event-day close) | 56.315 |
| 2026-07-24 15:00 | 57.40 |
| 2026-07-24 19:55 (close) | 57.11 |

(2026-07-25 returned no bar via the provider.) The stock is -10.47% from 07-17 peak but
already recovered ~40% of the print-day drop by 07-24 — the event-day gap did its job;
drift since is positive, not negative.

EV calc, short RYAAY at 57.11 held to 2026-09-30 (~10 weeks): P(down)=0.52, mean +4.0%;
P(up)=0.48, mean -5.5% (deliberately asymmetric — un-hedgeable positive tail from a
fuel-unwind, benign guide, or LCC share-gain snapback). Gross EV = (0.52x4.0%) +
(0.48x-5.5%) = 2.08% - 2.64% = -0.56%. Costs (spread/slippage/borrow, ~10 weeks) ~0.34%.
**Net EV ~ -0.90%.** Breakeven needs P(down) ~ 0.615, unsupported by the tape (which is
drifting up). Long side: P(up)~0.50 symmetric ~5% magnitudes -> EV ~ -0.34% after costs.
Recommendation: NO-TRADE. Would flip on the actual winter guidance landing inside the
window as a fresh catalyst, or the 07-24 bounce failing (break below 56.315 on volume).

---

## Round 2 — Rebuttal

### Bull rebuttal — confidence 38/100 (down from 55)

Concedes: the print-day gap already did its work (56.315 close) and the "easy" post-print
entry is gone; also concedes "zero visibility" is genuinely ambiguous language, not pure
boilerplate. Still disagrees that quant's EV math (a backward-looking, unconditional
random-walk assumption over ~9 weeks) properly prices a known, discrete, *undated* future
catalyst (formal winter guidance) — the no-consensus-baseline problem cuts both ways and
could mean the market is under-reacting to the recovery already underway. Would flip
bearish on: a break below 56.315 on volume, confirmed impaired H2 bookings, or the bounce
failing to hold above ~57 into the next week. Downgrades recommendation from active LONG
to **WATCH** — no new entry at current levels; would re-engage only on a pullback to
56.3-56.9 or confirmed positive guidance language, sized small via call spread.

### Bear rebuttal — confidence 20/100 (down from 30)

Concedes the priced-in mechanism was right but the magnitude was understated — quant's
data shows a genuine capitulation-and-recovery pattern (58.445 pre-print -> 56.315 trough
-> 57.11 by 07-24), ~40% of the drop reverted within one session, meaning whatever edge
existed at print time is now smaller. Pushes back that the bull's relief-rally needs a
second, undated catalyst to resolve *positively* — quant's own numbers show a slightly
bear-skewed 52/48 split, not clean asymmetric upside; this reads as a coin-flip with
negative EV after costs, not a mispricing. Would flip on a confirmed capacity-trim
announcement, fuel-hedge update, or peer (easyJet/Wizz) guidance showing sector-wide fare
stabilization. Recommendation: **NO-TRADE**, confirmed rather than merely inferred by the
bounce data.

### Quant rebuttal — confidence 20/100 (down from 22)

Neither the bull's nor the bear's Round 1 argument is a full numbers argument: bull's
relief-rally supplies direction with no probability/magnitude/timing; bear's "priced in"
claim is checkable and the stronger half — ~66% of the total peak-to-trough drawdown
(62.90->56.315, -10.47%) occurred *before* the print (62.90->58.445 pre-print = -7.08%),
meaning the market pre-positioned and the residual surprise term is small, shrinking both
tails. Sensitivity table: short breakeven requires P(down)~0.615 (9.5pp edge over
coin-flip) or a down-case magnitude of 5.73% vs the assumed 5.5% up-case — neither
defensible from evidence in hand. Long is the cheaper side (breakeven P(up)~0.534, only
3.4pp edge) but explicitly refuses to launder the bull's stated 55/100 narrative
confidence into a calibrated probability absent supporting data. The 07-24 bounce
(+1.41% off close, then an intraday fade 57.40->57.11) is read as the signature of a
finished move, not a tradeable signal either direction. Holds firm: **NO-TRADE**,
confidence 20/100. Would flip only with a hard consensus-vs-actual baseline plus
P(down)>=0.62.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** The Q1 fuel-driven miss and "zero visibility" language are already
reflected in RYAAY's price. ~66% of the peak-to-trough drawdown (62.90 -> 56.315, -10.47%)
occurred before the print; ~37-40% of the residual print-day drop reverted within one
session (56.315 -> 57.11, +1.41%). The residual surprise term is small and drift since the
print is positive, not negative — neither a long relief-rally nor a short continuation
carries a defensible edge into the 2026-09-30 window. Direction: **none**. Confidence: 22.

**Plan: NO-TRADE.** No persona cleared the institutional no-trade filter (final
confidences: bull 38/self-downgraded to WATCH, bear 20, quant 20). Both directions are
EV-negative after costs (short net EV ~-0.90%, long net EV ~-0.34%); breakevens require a
9.5pp edge (short) or 3.4pp edge (long) that no persona could source from evidence. The
catalyst is spent — pre-print price action shows the market pre-positioned, and the
post-print bounce faded intraday rather than extending. No consensus EPS/profit baseline
exists, so the miss cannot be scored as better/worse than expected.

Re-open only on: (a) a hard consensus-vs-actual baseline plus P(down)>=0.62; (b) a
confirmed capacity trim or fuel-hedge update; (c) peer (easyJet/Wizz) read-through
establishing sector-wide fare direction; or (d) a clean break below 56.315 on volume.

**Dissent (for post-mortem):** Is the quant's EV model structurally blind to the
undated winter-guidance catalyst, or is the bull's catalyst thesis structurally undated
and therefore untradeable? The bull's strongest surviving point — that a fixed-horizon
random-walk EV cannot price a known, discrete, upcoming re-rating event — was never
rebutted on its merits; the quant instead demanded a calibrated probability the bull
could not supply, which wins the decision but not the argument. Post-mortem test: check
whether formal winter guidance landed inside the 2026-09-30 window and moved the stock
beyond the assumed ~+-5.5% band. A large move either direction would indicate the panel
under-weighted a datable catalyst; drift inside the band confirms the NO-TRADE call.
Secondary dissent: the "no consensus baseline cuts both ways" claim was treated as
neutral by the panel, but a genuine absence of a consensus anchor may signal *wider*
variance rather than *zero* edge — this was asserted, not tested.

**Closing rationale:** Ryanair's Q1 miss is real but reflexively legible — fuel costs
tied to the Mideast/Iran conflict and softer fares, with management declining forward
guidance. The tradeable question is not whether the quarter was bad but whether the price
still owes the market anything for it, and the tape says no: two-thirds of the
peak-to-trough decline printed before the release, and over a third of the residual gap
reverted inside one session, with the bounce fading intraday rather than extending. With
no consensus baseline to score the surprise against, both tails compress toward
symmetry, and the arithmetic follows — net EV negative on both sides, with breakevens
requiring edges no persona could source from evidence. The bull conceded the entry and
downgraded to WATCH; bear and quant held NO-TRADE at 20. Convergence at low confidence is
a verdict, not a tie to split with a token position.
