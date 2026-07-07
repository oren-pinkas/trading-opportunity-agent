---
id: 2026-07-11-corcept-relacorilant-pdufa
title: Corcept relacorilant PDUFA decision (ovarian cancer)
status: researched
created: '2026-07-07T16:30:05Z'
event:
  type: regulatory
  summary: FDA target action date July 11 for relacorilant in platinum-resistant ovarian
    cancer; binary approval catalyst.
  impact_window: '2026-07-11'
tickers:
- CORT
sources:
- title: BiopharmaWatch PDUFA Calendar 2026
  url: https://www.biopharmawatch.com/PDUFA-calendar
  accessed_at: '2026-07-07T16:30:05Z'
- title: FDA approves relacorilant with nab-paclitaxel for platinum-resistant ovarian cancer
  url: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-relacorilant-nab-paclitaxel-platinum-resistant-epithelial-ovarian-fallopian-tube-or
  accessed_at: '2026-07-07T19:30:04Z'
- title: FDA Approves Corcept's Lifyorli (relacorilant) Plus Nab-Paclitaxel (BusinessWire, 2026-03-25)
  url: https://www.businesswire.com/news/home/20260325948774/en/
  accessed_at: '2026-07-07T19:30:04Z'
- title: ROSELLA Phase 3 overall survival (Lancet)
  url: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)00462-9/fulltext
  accessed_at: '2026-07-07T19:30:04Z'
- title: Corcept Receives Complete Response Letter for relacorilant in hypercortisolism (BusinessWire, 2025-12-31)
  url: https://www.businesswire.com/news/home/20251231309474/en/
  accessed_at: '2026-07-07T19:30:04Z'
hypothesis:
  statement: >-
    STALE CATALYST — the July 11 2026 PDUFA is not a live binary. The FDA already
    approved relacorilant + nab-paclitaxel (Lifyorli) for platinum-resistant ovarian
    cancer on 2026-03-25 (ROSELLA: OS HR 0.65, p=0.0004), ~3.5 months before the
    dossier date; the market has fully digested it (+13-40% pop in March). The prior
    2025-12-31 CRL was a different indication (Cushing's/hypercortisolism), not this
    oncology file, and does not revive a 7/11 event. Residual fundamental lean is
    long, but there is no tradable edge at this event window — verdict is NO-TRADE.
  direction: long
  confidence: 12
plan:
  ticker: CORT
  action: buy
  entry:
    time: '2026-07-11T13:30:00Z'
    target_price: 268.38
  exit:
    time: '2026-07-11T20:00:00Z'
    target_price: 268.38
  expected_profit_pct: 0.0
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-07T19:30:04Z'
---

## Scouted 2026-07-07T16:30:05Z

## Researched 2026-07-07T19:30:04Z — three-round-panel (bull/bear/quant → opus synth)

**Verdict: NO-TRADE (unanimous).** All three personas independently found that the
FDA already approved relacorilant + nab-paclitaxel (Lifyorli) for platinum-resistant
ovarian cancer on **2026-03-25**, roughly 3.5 months before this dossier's July 11
PDUFA date. The dossier's "BiopharmaWatch PDUFA Calendar" entry is a stale target
action date the FDA beat by acting early. There is no live binary to trade on 7/11.

- **Bull** retracted his opening long once the 2026-03-25 approval was corroborated
  from multiple sources (fda.gov, Corcept IR, BusinessWire, FiercePharma).
- **Bear** held dead-on-arrival: no information edge 3.5 months post-approval; the
  real live question is commercial execution vs Elahere, reported ~early August.
- **Quant** corrected his own EV model: with a public approval, market-implied
  P(approval) ≈ 0.99 (> his 0.90 estimate), so a long has negative edge and the
  event-move term ≈ 0. Blended EV ≈ −0.05%, Sharpe ≈ 0 → FLAT / size 0.

The `plan` block is a **zero-size placeholder** (entry == exit == 268.38,
expected_profit_pct 0.0) to satisfy the schema; **no position is intended.** The
dossier is deliberately held at `researched` and **not** promoted to `scheduled`, so
`simulate-plans` will not fill a trade.

**Data-integrity flags (for the scout/harness owner):**
1. The catalyst is stale — the scout recorded an FDA target date the agency had
   already beaten by ~3.5 months. Consider a dedup/recency check against post-filing
   FDA action news before recording PDUFA-calendar events.
2. The sim reference price CORT=268.38 is 3-4x above real-world CORT (~$61-93 in
   mid-2026). Absolute price targets are unreliable; the panel reasoned in % terms.

**Dissent (for the post-mortem):** Whether a *distinct, still-pending* FDA/EMA action
sits near 7/11 that would re-arm the trade (Bull's unconfirmed rescue: a Cushing's
resubmission PDUFA ~6mo after the Q4'25 CRL, or an OS-data/label-conversion event) —
neither confirmed nor refuted. Coupled with the Quant's Branch-B uncertainty: if the
simulator injects a synthetic move at the dossier event rather than filling against
the real post-approval tape, any P/L would be a harness artifact of unknowable sign.

Full debate with citations: `transcript.md`.
