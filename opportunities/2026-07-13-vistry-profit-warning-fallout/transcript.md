# Research Debate Transcript — Vistry profit warning and CFO exit (VTY.L)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run at 2026-07-16 (event: 2026-07-08, impact_window: 2026-07-31).

**Event**: Vistry warned of a GBP30m H1 loss and its CFO resigned on July 8; new CEO's
cost-cutting plan and buyback pause remain in focus.
Source: Bloomberg, "Vistry's New CEO Targets Cost Cuts as Finance Chief Leaves",
https://www.bloomberg.com/news/newsletters/2026-07-08/vistry-s-new-ceo-targets-cost-cuts-as-finance-chief-leaves,
accessed 2026-07-13T07:44:04Z.

**Data-availability finding**: `toa price VTY.L <ts> --provider twelvedata` was tried
with three symbol formats — `VTY.L`, `VTY:LSE`, `VTY` — and all three returned
`HTTP 404` (MarketDataUnavailable). The same TwelveData API key was verified working
against `AAPL` (`toa price AAPL 2026-07-15T15:00:00Z --provider twelvedata` ->
`{"price": 323.91501, ...}`), confirming the key is valid and the gap is
VTY.L-specific (no LSE/GBX coverage on our current provider/plan). No real quote for
VTY.L could be cited anywhere in this debate; all price discussion below is
qualitative or in percentage-move space only, per the market-data skill's rule to
never estimate a price ourselves.

**Relevant institutional lessons injected** (via `toa lessons-relevant --type earnings
--tickers VTY.L`): NKE (confidence/adverse-tail no-trade filter; discount post-earnings
drawdown near 52-wk lows), TSLA (bar-boundary/timestamp-guard hygiene), DAL (priced-in
catalyst; align to quant's EV math), LEVI (no manufactured directional position when
EV is ~0; anchor entries to a live quote).

---

## Round 1 — Independent research

### Bull (sonnet), confidence 40/100

The catalyst isn't the profit warning itself — that news is already 8 days old (July 8)
and priced in. The tradeable catalyst is the **resolution of uncertainty** around two
open threads: the new CEO's cost-cutting plan and the buyback pause, both framed by
Bloomberg as "in focus." A GBP30m H1 loss bundled with a same-day CFO resignation
reads as "kitchen sink" capitulation under new leadership — a classic pattern where
a new CEO front-loads bad news early in tenure, then resets against a lowered bar.

Timeframe: the H1 results/trading update window, expected around the 2026-07-31
impact_window, where the cost-cutting plan should get fleshed out with numbers and
the buyback stance clarified.

Proposed action: small long VTY.L (or a defined-risk options structure if UK
single-stock options liquidity allows, which is uncertain), held into the July 31
catalyst, entered only if the stock is confirmed still near its post-warning lows
(not already round-tripped). Could not verify any live price — flagged this
explicitly as blocking real execution: "entry price, current level, and fill
mechanics are unverified for this name given the data gap."

Confidence rationale: moderate, not high — this is a sentiment-reversal thesis on a
name with a genuinely worsening near-term fundamental (an active GBP30m loss, not
noise), no verified price to confirm freshness of the setup, no CFO replacement named
yet, and no specifics on the cost-cutting plan itself. Per the NKE lesson, a
confidence this side of ~45 paired with an un-hedgeable tail (unverified UK options
liquidity) is a caution flag.

### Bear (sonnet), confidence 15/100

Thesis is stale: whatever gap-down repricing was going to happen already happened in
the first 1-3 sessions post-announcement (July 8). By day 8, institutional analysts,
sell-side notes, and short-interest positioning have already digested the loss warning
and CFO exit. The next real catalyst is the 2026-07-31 impact_window (~2 weeks out) —
trading today is trading residual drift, not the event.

Specific risks: (1) no verifiable price data anywhere — 404 across all three symbol
formats tried; (2) UK homebuilder sector macro overhang (mortgage-rate sensitivity,
build-cost inflation, Section 106 affordable-housing margin compression — the
disclosed cause of Vistry's own prior 2024 profit warnings); (3) the buyback pause
removes a technical support bid; (4) CFO vacancy is an ongoing governance/credibility
risk until a permanent replacement is named, not a resolved one-off; (5) GBX/currency
and LSE-hours mechanics are a mismatch with this desk's US-built infra and
timestamp-guard tooling; (6) the dossier has had zero research added in 8 days, a
mild signal no one has found a clean edge.

What the bull likely overweights: "bad news priced in" logic (per the NKE lesson)
applies best when the print risk is *behind* the stock, not ahead of it as it is here
(the real update is 07-31). What the bull likely underweights: the total absence of
verifiable market data needed to construct, size, or exit any real position.

Recommendation: NO TRADE, or at most a wait-and-watch flag for 2026-07-31.

### Quant (opus), confidence 20/100

Base rate: initial reaction is already spent by day 8. Forward 2-3 week distribution
assumed: ~40% further down (avg -6%), ~30% flat/noise, ~30% relief bounce (avg +7%) —
a coin-flip-ish distribution, not a clean continuation trade.

Explicit EV calculation (percentage-move space, no verified quote available) on a
hypothetical short: gross EV = 0.40×(+6%) + 0.30×(0%) + 0.30×(-7%) = +0.3%. Net of UK
round-trip frictions (spread/commission/borrow, ~0.4-0.8%) ≈ -0.3% to ~0% — negative
to breakeven. The adverse tail (relief bounce, un-hedgeable on a naked short) is
comparable in magnitude to the edge, tripping the "thin EV vs. adverse tail" no-trade
filter from the NKE lesson.

Decisive and separate from the EV math: VTY.L returns HTTP 404 on every symbol format
tried on TwelveData, while the same key prices AAPL cleanly. This is an
**infrastructure hard-stop**, not a research inconvenience — no verifiable entry/exit
bars means the plan is literally un-simulatable and un-fillable by this system,
independent of thesis quality, per the LEVI/TSLA lessons on anchoring entries to live
quotes and validating both legs map to available bars.

Recommendation: NO TRADE, on both EV grounds and feasibility grounds. If forced to
express a view, only a defined-risk options structure would be defensible (never a
naked short per the NKE lesson) — but that's moot since the underlying can't even be
priced.

---

## Round 2 — Rebuttal

### Bull rebuttal, updated confidence 15/100

Concedes: the infrastructure hard-stop is a *gating condition*, not just a confidence
modifier — un-simulatable means "not a trade in this system," full stop. Concedes
that "bad news priced in" is a claim about the past and does nothing to derisk the
still-ahead 07-31 event — conflated proximity to a past low with protection against a
future negative surprise. Concedes the quant's EV math (thin edge, comparable adverse
tail) beats narrative conviction; has no competing EV calc, only a story. Concedes
underweighting the UK sector overhang and the buyback pause as a removed technical
prop.

Still holds: the forward-catalyst *observation* (07-31 is where the real information
arrives) survives as a calendaring note even though the trade recommendation does
not — this isn't really a disagreement with the bear, since the bear's own
"wait-and-watch for 07-31" implicitly agrees on timing.

Recommendation: NO TRADE now; re-run as a watch item for 07-31 contingent on solving
data access first.

### Bear rebuttal, updated confidence 10/100

The bear and quant converge independently — one via qualitative risk-mapping, one via
EV arithmetic — on the same no-trade conclusion, which strengthens the case: it isn't
just priors about UK homebuilders, it survives a completely different analytical
lens. Credits the bull's "kitchen sink under new CEO" read as the most specific and
testable part of the bull case, but notes it's a hypothesis about intent that the
07-31 print itself is the mechanism for testing — i.e., the bull is asking to hold
*through* the very event risk they claim resolves favorably, competing against a
"structural margin problem across two comps in two years" read (2024 precedent).

Would only soften with: (a) a working, verifiable GBX price feed; (b) a specific
pre-07-31 confirmation of concrete cost-cutting milestones; or (c) a peer comp check
(Barratt, Persimmon, Taylor Wimpey) showing this is company-specific, not sector-wide
— nobody produced that comp check.

Recommendation: NO TRADE, reinforced.

### Quant rebuttal, updated confidence 15/100 (revised down from 20)

The bull's reframing (the real event is the 07-31 print, not the stale 07-08 print)
makes EV *worse*, not better — it converts a thin-edge drift trade into a
binary-into-print with a fat adverse tail, held across ~2.5 weeks of sector/macro
drift risk. Revised EV: UK round-trip friction for a long ≈ 0.95% (spread ~30bps +
commission ~15bps + ~0.5% stamp duty on the buy only) vs. ≈ 0.55% for a short (no
stamp, but borrow/locate risk). Granting the bull a generous 55/45 favorable skew on a
±6% print: gross EV ≈ (0.55-0.45)×6% = +0.6%; net for the bull's preferred long ≈
0.6% - 0.95% = **-0.35%**; net for a short ≈ 0.6% - 0.55% = **+0.05%** (statistically
zero). The adverse tail (a further guidance cut, -6% to -10%) exceeds the entire edge
either way.

Confirms NO-TRADE on both grounds, with feasibility as the binding/dispositive
constraint: the data blackout (404 on every symbol format vs. clean AAPL pricing) is
the one point all three panelists agree on, and even the bull's own confidence was
explicitly conditional on data the system doesn't have — the tie is already broken
before the EV math is even needed.

---

## Round 3 — Synthesis (opus)

**Hypothesis** (direction: none, confidence: 88 — conviction in the NO-TRADE call
itself): Vistry's GBP30m H1 loss warning and same-day CFO resignation (Bloomberg,
2026-07-08) is 8-day-old news whose real catalyst — the new CEO's cost-cutting plan
and buyback-pause resolution — does not land until the ~2026-07-31 H1 update; trading
today is trading drift, not the event. Reframing the trade around the forward print
converts a thin-edge drift bet into a binary-into-print with a fat adverse tail
(a further guidance cut of -6% to -10% exceeds the entire estimated edge). Net EV
nets negative for the bull's preferred long (~-0.35% after UK frictions including
~0.5% stamp duty) and statistically zero (~+0.05%) for a short. Decisively, VTY.L
returned HTTP 404 across every symbol format (VTY.L, VTY:LSE, VTY) on TwelveData
while the same key works for AAPL, so no verifiable entry/exit bars exist — the plan
is un-simulatable and un-fillable regardless of thesis quality.

**Plan**: ticker VTY.L, action **no-trade**, no entry/exit prices, expected_profit_pct
0.

**Dissent** (strongest unresolved disagreement, preserved for post-mortem): the
bull's "kitchen sink under a new CEO" framing — that the loss and CFO exit were
deliberately front-loaded to clear the decks — remains the most specific, testable,
and unresolved claim. If correct, the ~07-31 print skews to a relief bounce rather
than a further cut, flipping the trade's sign. It was never adjudicated because (a)
no one ran the peer comp check (Barratt, Persimmon, Taylor Wimpey) to isolate this as
company-specific vs. sector-wide drift, and (b) the data blackout made the question
moot before it could be priced. Worth re-checking at 07-31 if a verifiable GBX feed
is secured.
