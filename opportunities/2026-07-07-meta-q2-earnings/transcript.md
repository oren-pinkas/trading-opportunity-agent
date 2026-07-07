# Research Debate — META Q2 2026 Earnings

- **Opportunity:** `2026-07-07-meta-q2-earnings`
- **Event:** Meta Platforms (META) Q2 2026 earnings, reported 2026-07-29 after market close (AMC). Catalyst: ad-revenue trajectory + AI capex trajectory.
- **Strategy:** `three-round-panel` (personas: bull, bear, quant; models — bull/bear=sonnet, quant/synthesizer=opus)
- **Run at:** 2026-07-07T22:37:55Z
- **Reference price (deterministic sim provider):** META = 327.31 @ 2026-07-07T19:59Z
- **Outcome:** NO-TRADE (neutral), overall confidence 72/100.

> PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Relevant institutional lessons injected
- Confidence ≤~45 with an un-hedgeable positive tail and net EV <~2% against a ~7–8x adverse-tail-to-edge ratio is a **no-trade filter**, not a size-down; express earnings gap trades via defined-risk options, never naked shorts. (`2026-06-25-nike-q4-fy26`)
- Discount negative base rates when a name is at/near its 52-week low — most drawdown is already priced. (`2026-06-25-nike-q4-fy26`)
- Set intraday exits ≥1 minute inside the session boundary (19:59:00Z, not 20:00:00Z): the 1-min-bar provider has no bar at exactly the close. (`2026-07-02-tesla-deliveries`)
- Both legs must map to available US-equity bars (13:30Z–19:59Z). (`2026-07-02-tesla-deliveries`)

---

## Round 1 — Independent opening positions

### Bull (Catalyst-hunter, sonnet) — confidence 58
Long META via a defined-risk bull call spread (~332/352), anchored to 327.31. Ad engine compounding: Q1'26 revenue +33% YoY to $56.3B, impressions +19%, price/ad +12%; 4M+ advertisers on Advantage+ generative tools with 15–25% higher ROAS. Q2 consensus $61.32B sits **above** the top of management's own $58–61B guide — the Street is pricing a beat. Capex overhang ($125–145B, which triggered ~-7% AH on the Q1 print) is now three months old and digested; absent a fresh capex shock, ad execution drives the reaction this time. Entry 07-29T19:55Z, exit 07-30T19:59Z, target +6–8%.
Evidence: Q1'26 EPS $7.31 vs $6.67 cons (+9.6%); 2026 capex guide raised to $125–145B on 2026-04-29; META avg post-earnings move ±11.8% (largest of mega-caps); ~84% buy across 72 analysts.
Sources: stocktitan.net (2026-04-29), investing.com (2026-04-29), fool.com transcript (2026-04-29), fortune.com (2026-04-29), seekingalpha.com (2026-05-04), adstatus.app (2026), digitalapplied.com (2026), earnings-watcher.com, chartmill.com.

### Bear (Skeptic, sonnet) — confidence 38 (directional)
NO naked directional trade. The obvious long fights the tape: Q1'26's beat produced a ~6–7% AH selloff because 2026 capex was raised to $125–145B, and "every quarter since last October" capex raises have been followed by declines (Motley Fool, 2026-05-05). On 2026-07-02, META fell up to 4% intraday on Wolfe Research commentary that a cloud/compute-resale business could push 2027 capex to $200B (from ~$160B) — a live, escalating, un-digested capex vector. FCF fell 19.4% in 2025. Regulatory headline risk (EU DMA, US antitrust). Flags a real-vs-sim price anomaly (real-world META ~$615.58 on 2026-07-07 vs sim stub 327.31) as a data-hygiene concern only. No reliable options-implied move 3 weeks out. If any trade, defined-risk non-directional (strangle/straddle) sized ~1 week out once IV firms.
Sources: CNBC/Yahoo Finance/Sherwood News (2026-04-29/30), Motley Fool (2026-05-05, 2026-07-02), investor.atmeta.com, optionslam.com/earnings-watcher.com aggregation.

### Quant (Pragmatist, opus) — confidence 42
NO-TRADE. Base rate: META avg absolute earnings-day move ±11.8%, median ±11.0%, 95th pct ±25.8%; clears its options-implied move ~63% of reports (10 of 16). Last four prints: Q1'26 -8.6% (capex raise), Q4'25 +10%, Q3'25 -11%, Q2'25 +11.3% — **direction is a coin flip** (signed 8-qtr avg +1.04%), magnitude is huge. Assumed probabilities: 30% up +10% (~360), 35% down -10% (~295), 35% muted (~327). Naked long 100sh EV_gross ≈ -$1.64/sh ≈ -0.5%, net -0.6% to -0.7% after slippage.
**Key execution constraint:** the simulator fills only US-equity bars 13:30Z–19:59Z; options do not map, so no defined-risk options expression is executable in-sim. Earnings drop AMC 07-29, so any equity position through the print is a naked overnight gap with a ±26% un-hedgeable tail. All four no-trade filters trip.
Sources: earnings-watcher.com, optionslam.com/META, Yahoo Finance (2026-04-29), CNBC (2026-01-28, 2025-10-30).

---

## Round 2 — Rebuttals

### Bull — revised confidence 47
Concedes the bull call spread is **non-executable** (options don't fill in-sim); an unfillable structure is a wish, not a plan. But argues both opponents assumed the only tradable window is the earnings **gap**. Pivots to a **pre-earnings positioning-drift** trade, fully equity-executable and gap-free: ride drift into the print and be **flat before the AMC release**. Entry 2026-07-28T13:35:00Z, exit 2026-07-29T19:59:00Z (last bar before print), target +2–3%, no overnight gap, no options. Argues the capex-punishment base rate is a *gap-reaction* pattern irrelevant to pre-print drift, and the 07-02 Wolfe capex risk is already priced by entry. Concedes it clears the ≤45 filter only narrowly and will fold to no-trade if the drift edge doesn't survive slippage.

### Bear — revised confidence 72 (in NO-TRADE)
NO-TRADE hardened. The options-non-executable constraint kills his own defined-risk fallback too, leaving only naked overnight equity or nothing. A "defined-risk short" is unavailable; a naked short carries the explicitly-prohibited un-hedgeable positive tail (Q4'25 +10%, Q2'25 +11.3% — two of the last four prints gapped up double digits). Direction is a coin flip; his capex lean informs magnitude/character, not a tradeable sign. Rebuts the bull directly: consensus **above** the guide top **raises** the bar (an in-line-to-guide print becomes a disappointment), so it weakens a long rather than strengthening it; "capex digested" was falsified by the 07-02 -4% move. Accepts the 327.31 stub as instructed; the real-vs-sim anomaly is a data-hygiene flag, not a signal.

### Quant — revised confidence 44 (in NO-TRADE)
NO-TRADE locked in. Folds the bull's "beat already priced" logic against him and incorporates the bear's 07-02 datapoint → updated probabilities 28% up / 38% down / 34% muted → naked-long EV now ≈ **-1.0%** after costs. Directly adjudicates the pre-print drift idea: post-earnings drift (PEAD) is a sign-of-surprise, multi-week effect (~2–4 bps/day); single-name pre-print positioning drift is ~50/50 noise. Generous P(continue)=55% at 1.5% magnitude ⇒ same-session drift EV +0.15% gross, ~-0.05% to -0.10% net — sub-threshold and negative. The only edge-positive vehicle — a long straddle exploiting the 63% implied-move beat rate — is non-executable in an equity-only sim.

---

## Round 3 — Synthesis (opus, neutral)

**Hypothesis (neutral, confidence 72):** META Q2 2026 earnings offer no positive-expected-value expression under the equity-only, options-non-executable simulator. The gap direction is a coin flip (signed 8-qtr avg +1.04%) with a huge ±11.8% average magnitude and an un-hedgeable ±26% overnight tail, so any position held through the AMC print is a naked gap and every no-trade filter trips. The only edge-positive vehicles (defined-risk spread, long straddle exploiting the 63% implied-move beat rate) are non-executable, and the pre-print positioning-drift alternative nets to roughly zero (~-0.05% to -0.10%) after slippage.

**Plan:** NO-TRADE. `action: none`; no entry/exit; expected_profit_pct 0. Binding constraint: options are non-executable in-sim, so no defined-risk earnings structure exists; holding equity through the 07-29 AMC print is a naked overnight gap (±26% tail); naked-long EV ≈ -1.0% net; a naked short is prohibited and carries the positive-tail squeeze risk realized twice in the last four prints; the pre-print drift fallback nets ~breakeven-negative. All four institutional no-trade filters trip simultaneously. Recorded as status `researched` (not scheduled).

**Dissent (for the post-mortem):** The bull's pre-print positioning-drift trade (enter 07-28T13:35Z, flat by 07-29T19:59Z before the AMC release) is gap-free and equity-executable, sidestepping the entire naked-overnight objection. The synthesis rejects it on the quant's PEAD adjudication that single-name pre-print drift is ~50/50 noise netting near zero after slippage — but that near-zero EV is an *estimate*, not a demonstrated negative edge. If positioning drift on a mega-cap into a high-attention print is even marginally positive, a small gap-free long was the one defensible trade left on the table.
