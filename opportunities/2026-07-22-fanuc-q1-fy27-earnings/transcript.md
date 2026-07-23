# Research Debate Transcript — 2026-07-22-fanuc-q1-fy27-earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.

Event: Fanuc reports next earnings Jul 31, 2026 — bellwether for global manufacturing capex and robotics/CNC demand after a record FY2025. Ticker FANUY (US OTC ADR of TSE-listed Fanuc, 6954).

Source: ["Fanuc stock: earnings update and factory automation outlook"](https://www.ad-hoc-news.de/boerse/news/ueberblick/fanuc-stock-jp3802300008-earnings-update-and-factory-automation-outlook/69393758), accessed 2026-07-22T23:08:41Z.

Data note: `toa price FANUY` failed against the twelvedata provider (HTTP 400) — no live quote was obtainable for this symbol at any point in the debate. This absence of a tradable quote became a central factor in the panel's conclusion, not just a caveat.

Institutional lessons injected (from prior post-mortems on other tickers, applied as general principles — not data about Fanuc):
- NKE: confidence <=~45 with net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down.
- NKE: discount post-earnings negative base rates when a name is near its 52-week low — but conversely, a name already near highs off a record year has priced-in risk (used in reverse by the bear/DAL lesson below).
- TSLA: set intraday exits inside the session boundary; add a timestamp guard so both legs map to available bars instead of silently voiding.
- DAL: a catalyst that already drove a large run to a high is priced in — don't re-bet the same fundamental as a fresh trigger.
- DAL: when the strongest dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size position.
- LEVI: when the quant says directional EV is ~0 and no in-mandate positive-EV structure exists, log NO TRADE — don't manufacture a token position "for the learning loop."
- LEVI: anchor entry prices to a live quote fetched at the actual entry timestamp; validate against current price before filling.

---

## Round 1 — Independent Opening Positions

### Bull (sonnet)

Thesis: Fanuc's Jul 31 print is the cleanest available bellwether read-through on global manufacturing capex and robotics/CNC re-acceleration. The market treats Fanuc as a proxy for whether the industrial-automation destocking cycle is over; a clean beat/raise reframes the capex narrative across semis, EV/auto lines, and factory automation broadly.

Evidence cited: dossier source confirms the Jul 31, 2026 date and frames the update explicitly around "factory automation outlook" (cited fact). Dossier notes Fanuc is coming off "a record FY2025" (cited fact) — high comp bar, but the prior trend was intact as of the last full fiscal year. Flagged as general knowledge/inference, not cited: Japanese FA names (Fanuc, Yaskawa, Keyence) have been trading a China/EV-capex-bottoming narrative through 2025-2026.

Action proposed: Long FANUY, small-to-moderate size, enter Jul 28-29 (pre-print positioning drift), hold through the print, exit by Aug 3. Explicitly flagged the no-live-quote gap (twelvedata HTTP 400) as a real problem requiring qualitative validation against last known OTC print and JPY/USD cross, wider limit bands, and — applying the NKE un-hedgeable-tail lesson — a defined-risk options structure if one exists rather than a naked cash position. Open question raised for Round 2: is this already priced in via TSE-listed 6954's recent run (DAL lesson)?

### Bear (sonnet)

Thesis is stale, not fresh: Fanuc's "record FY2025" is already baked into a valuation that has run alongside the China-recovery/robotics rally since late 2025 — the classic DAL pattern of betting an already-realized move as a fresh trigger. No live quote exists to confirm where FANUY or 6954 sit vs. 52-week range, which is disqualifying for sizing under the LEVI live-quote-anchoring lesson.

What's priced in / what disappoints: consensus already expects a capex-bellwether narrative (China restocking, robotics-capex supercycle, reshoring). Fanuc's order book (CNC/FA orders) is cyclical and lags capex announcements by quarters; a soft book-to-bill, weak China/auto demand, or Fanuc's historically conservative FY27 guidance would break the "bellwether confirms recovery" story.

Execution/liquidity risk — treated as the real kill switch: FANUY is a thin, wide-spread OTC ADR; Fanuc reports on the JST corporate calendar, so by the time US markets can react, Tokyo has already traded through the full information event (a TSLA-style "no bar exists when you need it" problem in a different guise); JPY/USD adds an uncorrelated second risk factor; no live quote at all means no way to verify price, 52-week distance, or vol/skew for any options structure. Stance: NO TRADE — no live quote to anchor entry/size risk, no confirmed liquid execution window around the actual information event, and the catalyst is largely already priced into a name coming off a record year.

### Quant (opus)

Data caveat: no consensus EPS/revenue, no whisper number, no options-implied move, no live quote — every probability is a prior, not a filed estimate.

Base rate priors: P(tradable pop, >+3%) ≈ 30%, P(muted, ±3%) ≈ 35%, P(sell-the-news, <-3%) ≈ 35%. Magnitudes: up ≈ +5%, down ≈ -6% (guidance/FX disappointment tends to hit harder off a record base). Gross EV = 0.30(+5%) - 0.35(-6%) = +1.5% - 2.1% = **-0.6%**, negative before costs. Round-trip cost on a thin, unsponsored OTC ADR assumed at ~2% (midpoint of a 1-3% conservative range). Net EV ≈ **-2.6%**.

Tradability structurally broken: no live quote (twelvedata HTTP 400) means no way to mark entry, size, or validate exit against a real feed — independent of the fundamental thesis. Compounded by the TSLA-style bar-gap risk (OTC names routinely have missing/stale 1-min bars in the simulator). Recommendation: NO TRADE, confidence ~70% — two independent kill switches, either sufficient alone: (1) net EV ≈ -2.6%, a no-trade-filter case per NKE/DAL/LEVI, not a size-down; (2) unexecutable/unmeasurable in this infrastructure (LEVI + TSLA lessons). Explicitly noted: if a real options-implied move or estimate set surfaces, will re-run the EV.

---

## Round 2 — Rebuttals

### Bull rebuttal

Concedes: the tradability problem is fatal, not a footnote — no live quote, no confirmed options chain, thin OTC ADR with JST reporting lag means the Round 1 options-structure plan doesn't exist in practice. Accepts the JST-lag point (was implicitly assuming a same-day US-session reaction to an overnight Tokyo print). Accepts "already priced in via China-recovery rally" is fair — didn't demonstrate the July print contains a surprise not already reflected in the recent move.

Pushes back narrowly: the fundamental bellwether logic itself isn't wrong — Fanuc remains a legitimate capex/robotics proxy, and the quant's asymmetric magnitude assumption (+5%/-6%) is a base-rate guess, not evidence this specific print skews negative. But distinguishes "thesis could be directionally right" from "trade is executable at acceptable cost," and concedes the panel correctly forced the second question.

What would change this: a live quote or confirmed liquid access to TSE 6954 directly; an actual options chain with quoted IV; evidence of a specific surprise (order-intake acceleration, guidance raise) not yet reflected in the recent rally. Updated stance: **NO TRADE, withdraws the long.**

### Bear rebuttal

The quant's -2.6% net EV doesn't just support the bear case, it sharpens it — the qualitative liquidity/JST-lag concerns and the quant's ~2% cost haircut are the same structural problem viewed from two angles, not two independent objections. Notes gross EV (-0.6%) was already negative before any cost was applied, meaning the "pop" scenario doesn't even carry the raw probability distribution.

Bull's own "check if priced in via 6954" flag from Round 1 is read as a tell: if the bull can't confirm the ADR reaction isn't a stale echo of Tokyo's move, the Jul 28-29 entry is a bet on a catalyst that price discovery may have already resolved. The proposed defined-risk options structure is called out as aspirational, not real — no confirmed chain. Sharpest remaining risk, stated most sharply: this trade requires precise entry/exit timing in an instrument with no live quote and no confirmed options chain — you cannot manage risk you cannot see. Updated stance: **NO TRADE, confidence raised to ~80%.**

### Quant rebuttal

On the bull's options/IV ask: no listed US options chain exists on FANUY to price. Hypothetically, even if a defined-risk debit spread could cap loss at ~1% of notional, the underlying gross EV (-0.6%) is still negative before ADR friction — a defined-risk wrapper caps downside, it does not manufacture positive edge. Doesn't move the recommendation.

On the bear's JST-lag point: accepted and re-priced. Tokyo trades the reaction during JST hours; the OTC ADR only re-rates on the next US session, converting the directional bet into systematic adverse selection (entering after the information, not before). Adds a ~0.5-1.0% stale-fill slippage term. Revised net EV ≈ -2.6% - 0.75% ≈ **-3.35%**, with a fat left tail from no-fill/gap void risk.

Final verdict: net EV ≈ -3.3%, negative before any tail risk; no live quote to anchor entry, no chain to bound risk, structural post-hoc fill disadvantage. Clears no bar, not even a token or defined-risk position. **Clean NO TRADE, confidence ~80%**, full convergence with the bear; bull's edge is unfundable.

---

## Round 3 — Synthesis

```json
{
  "hypothesis": {
    "statement": "Fanuc's Jul 31 FY27 Q1 print is a genuine global-capex/robotics bellwether, but the FANUY ADR is untradeable for this event: net expected value is negative (~-3.35%) after OTC round-trip costs and JST reporting-lag adverse selection, and the fundamental edge is plausibly already priced in via the China-recovery rally. The bellwether logic is sound but unexecutable and unmeasurable, so there is no fundable edge.",
    "direction": "none",
    "confidence": 80
  },
  "plan": {
    "ticker": "FANUY",
    "action": "no_trade",
    "entry": null,
    "exit": null,
    "expected_profit_pct": null,
    "rationale": "The panel converged to NO TRADE on two independent grounds. First, negative expected value: quant's gross EV was already -0.6% pre-cost, and after ~2% OTC round-trip cost plus ~0.5-1.0% stale-fill slippage from the JST reporting lag, net EV is roughly -3.35%. Second, a structural execution blocker: the thin OTC ADR has no live quote to anchor entry and no options chain / IV to build a defined-risk wrapper, while Tokyo (TSE 6954) trades through the reaction before the ADR responds, forcing fills after the information is already in the price. A defined-risk options structure would only cap downside, not create positive edge, and even the directional thesis is likely discounted by the prior China-recovery move. Bull withdrew the long in Round 2, conceding tradability is fatal. No trade."
  },
  "dissent": "The panel fully converged -- bull withdrew the long, and bear and quant reached the same conclusion from two non-overlapping angles (negative net EV and structural unexecutability). The single most fragile assumption underlying the consensus is the cost/slippage stack itself: the ~-3.35% net EV rests on estimated OTC round-trip cost (~2%) and JST-lag slippage (~0.5-1.0%) that were never measured against a live quote or real spread. If FANUY actually traded with tighter spreads and a usable options chain existed, the execution blocker would soften and the call would hinge entirely on the unproven 'already priced in' claim -- which no participant substantiated with the print's surprise versus current price."
}
```
