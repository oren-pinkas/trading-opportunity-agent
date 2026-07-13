# Debate transcript — 2026-07-12-perrigo-opill-generic-entry

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Debate run: 2026-07-13T04:56:23Z. Ticker: PRGO. Event: Perrigo's Opill (norgestrel) OTC birth-control pill has an
estimated patent/marketing-exclusivity expiration of 2026-07-13, opening the door to generic competition.

Lessons applied (from `toa lessons-relevant --type regulatory --tickers PRGO`):
- Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward.
- Never map a corporate/legal calendar date directly onto an execution timestamp — treat it as a catalyst and derive
  the fill time from the nearest valid trading session. (2026-07-13 confirmed a Monday, valid NYSE session.)

Price-source note: `toa price PRGO 2026-07-13T13:30:00Z` (stub) returns `$122.51 (source: stub:deterministic)`.
`toa price PRGO 2026-07-13T13:30:00Z --provider twelvedata` fails with `MarketDataUnavailable` (HTTP 400) because
2026-07-13 has not occurred yet in the real world relative to the live data provider. The deterministic stub is
therefore the only valid, authoritative fill price for this simulation; any "real" price a persona surfaces via web
research for this simulated date is unverifiable and is treated as narrative color only, never as a fill basis.

---

## Round 1 — Independent research

### Bull (opening)

Found the bull case weak on inspection. Norgestrel has been off composition-of-matter patent since 1973 (Ovrette);
what actually lapses 2026-07-13 is Perrigo's 3-year Hatch-Waxman marketing exclusivity from the July 2023 Rx-to-OTC
switch approval. That lapse only allows the FDA to *accept* ANDAs — it does not put a generic on shelves the same
day. The Plan B One-Step precedent shows a multi-quarter-to-multi-year lag between exclusivity lapse and an actual
competing OTC launch. Opill is immaterial to Perrigo: Women's Health segment net sales were $132.8M FY2024 → $72.4M
FY2025 (-10.7% YoY, from lapping a one-time launch stocking benefit), but Q1 2026 Opill sales were +12% YoY — the
franchise is growing, not eroding. No ANDA, Paragraph IV notice, or generic launch was found tied to this date.
Verdict: no distinguishable PRGO move expected from this event; confidence in the Opill-as-catalyst thesis ~2/10.

Bull separately floated an unrelated tactical long — PRGO deeply depressed (~$10-11/share per web research, mkt cap
~$1.52B), CEO Lockwood-Taylor resigned (personal conduct, unrelated to the business) with an interim CEO and new
independent directors installed, a technical reversal (MACD turned positive, price crossed above the 50-day MA), and
a consensus analyst target ~2x the current price — explicitly flagged as riding on factors *unrelated* to this
dossier's stated catalyst, sized small, conviction ~4/10.

Sources cited: Perrigo FY2025/Q1 2026 earnings releases; FDA Opill OTC approval (2023-07-13); Plan B One-Step generic
timeline; consensus analyst target data.

### Bear (opening)

Bottom line: a non-catalyst dressed up as one. Would not trade PRGO in either direction off this event. Opill is a
subset of the Women's Health segment ($72.4M FY2025, -10.7% YoY) against Perrigo's ~$1.1B/quarter total revenue —
under 1.5-2% of revenue, likely less for Opill alone. The "patent expiration" is a DrugPatentWatch *estimate*, not an
FDA-confirmed event; no ANDA approval, Paragraph IV notice, or named generic competitor launch was found. Norgestrel
has been off-patent since the 1970s — the real moat was always the OTC-switch data/exclusivity plus shelf space and
brand, not a composition-of-matter patent.

What actually dominates PRGO's price action: an unrelated infant-formula business crisis — a strategic review to
exit/divest Infant Nutrition (Nov 2025), manufacturing underinvestment disclosed at the Gateway facility, an active
securities class action (Teamsters Local 710 Pension Fund / Cohen Milstein), ~4x net leverage ($3.64B debt vs $532M
cash), negative Q1 2026 operating cash flow (-$113.6M), the stock down from a 52-week high of $28.44 to ~$10-11, and
a distress-level ~10.5% dividend yield. Confidence that this event produces no meaningful move: 75-80%.

Sources cited: Perrigo Q4/FY2025 earnings release; securities litigation filings (Cohen Milstein); FDA OTC approval
press release; DrugPatentWatch listing; market-price data.

### Quant (opening)

Flagged the stub-vs-real price discrepancy (see price-source note above) for orchestrator reconciliation. Argued
patent-expiry/generic-entry for an OTC product is a gradual multi-quarter-to-year erosion story, not a single-day
repricing — OTC generic displacement is structurally slower than Rx (brand loyalty, shelf-space, ANDA + manufacturing
lead time). This is a scheduled, long-telegraphed, already-in-consensus calendar item on a SKU that is ~1.2-1.7% of
Perrigo's FY2025 revenue ($4.25B total; Women's Health $72.4M).

Round-1 scenario tree: 70% no detectable move / 22% mild -1% / 5% sharp -4% / 3% counter-move +2% →
E[move] ≈ -0.36%. Net EV after ~25bps round-trip costs ≈ +0.11% — statistically indistinguishable from zero
(implied t-stat ~0.07), dwarfed by PRGO's ~4-6% daily realized volatility. Recommendation: no trade / pass, or
de minimis size (≤0.25% of book) with a hard same-session stop if the debate insists on expression.

Sources cited: Perrigo FY2025/Q2 2025 earnings releases; NBER "Long Shadow of Patent Expiration"; Kyle, "Generic
Entry and Rx-to-OTC Switches"; market-price/volatility data.

---

## Round 2 — Rebuttal

### Bull (rebuttal)

Conceded fully. Bear's litigation/leverage/negative-operating-cash-flow evidence undermines even the "unrelated
oversold bounce" leg bull had floated — a technical MA cross and a CEO change are weak signals against a backdrop of
active securities litigation, ~4x leverage, negative operating cash flow, and an ongoing strategic divestiture.
**Withdraws the trade entirely**, converging with bear and quant. Confidence in no-trade-on-event revised up to ~8/10.
Recommends any standalone distressed-bounce idea be run as a separate watchlist item after Q2 earnings / divestiture
clarity — not attached to this dossier.

### Bear (rebuttal)

Nothing moves bear off no-trade — quant's EV math and bull's own 2/10 concession both independently confirm bear's
thesis from different angles. Bull's Hatch-Waxman/Plan-B-One-Step mechanism point sharpens bear's "soft/estimated
date" argument further; bear upgrades confidence to ~85%+ that the date itself produces no repricing. Bull's Q1 2026
+12% Opill growth is read as neutral-to-mildly-negative for urgency in *either* direction (undercuts both an
"imminent cliff" bull-fade and a "dying franchise" bear-short). Formally objects to bundling bull's unrelated
distressed-bounce idea into this dossier's trade record — doing so would misattribute any subsequent P&L to the
wrong catalyst and corrupt the post-mortem signal.

### Quant (rebuttal)

Revises the scenario tree tighter given bull's mechanism correction (exclusivity lapse ≠ same-day generic launch) and
bear's evidence that PRGO's real variance driver is unrelated distress: 82% flat / 13% mild -0.5% / 2% sharp -3% /
3% counter +1% → E[move] ≈ -0.095% (down from -0.36%). Net EV after ~25bps costs is now **negative** (≈ -0.15%) —
worse than Round 1's already-marginal case. Variance decomposition: event-attributable variance is ~1.2% of PRGO's
total 1-day variance; ~98.8% is uncompensated exposure to the unrelated infant-formula/litigation/leverage distress
complex (signal-to-carried-risk ≈ 0.02). Explicitly rejects bull's unrelated bounce idea as out of scope and
unhedgeable in this simulation, additionally noting it cannot even be entered at a price consistent with its own
distressed-valuation premise given the stub fill ($122.51 vs. an unverifiable web-researched ~$11.58). Final: no
trade, size 0.

---

## Round 3 — Synthesis

**Hypothesis**
- Statement: The 2026-07-13 lapse of Perrigo's 3-year Hatch-Waxman OTC marketing exclusivity on Opill (norgestrel)
  is not a tradable single-day catalyst for PRGO. Norgestrel has been off composition-of-matter patent since the
  1970s; the lapse merely lets the FDA begin accepting ANDAs and does not enable a same-day generic launch (the
  Plan B One-Step precedent implies a multi-quarter-to-multi-year lag), and Opill is under ~1.5-2% of Perrigo's
  ~$1.1B/quarter revenue, so the event is immaterial to the whole. PRGO's real 1-day variance is dominated by an
  unrelated distress complex (infant-formula divestiture, Gateway facility issues, securities litigation, ~4x
  leverage, negative operating cash flow), not this event.
- Direction: none
- Confidence: 85 (confidence that this specific event does not produce a tradable move)

**Plan**
- Ticker: PRGO
- Action: no_trade
- Rationale: Converged scenario tree yields E[move] ≈ -0.095% and net EV ≈ -0.15% after ~25bps costs (negative,
  statistically indistinguishable from zero). Event-attributable variance is ~1.2% of 1-day total variance
  (signal-to-carried-risk ≈ 0.02); ~98.8% of variance is uncompensated exposure to the unrelated distress complex.
  Materiality is negligible and the mechanism is wrong for a same-day repricing (no ANDA/Paragraph IV/generic launch
  found; "patent expiration" is a third-party estimate, not FDA-confirmed). All three personas converged
  independently on no edge.
- Entry: none — no position is opened.
- Exit: none — no position is opened.
- Expected profit: 0%

**Dissent** (preserved for post-mortem)
The only unresolved disagreement is procedural/scope, not analytical: whether bull's unrelated distressed-bounce idea
(CEO transition + technical MA reversal, against a ~4x-levered, litigation-and-divestiture backdrop) should be logged
anywhere near this dossier. Bear formally objects to bundling it — any resulting P&L would be misattributed to the
Opill catalyst and corrupt the post-mortem signal. Quant adds that the idea is quantitatively unhedgeable here and
cannot even be entered at a price consistent with its own distressed-valuation premise given the deterministic stub
fill. Bull withdrew the idea in Round 2 and agreed it belongs on a separate post-Q2/divestiture-clarity watchlist
item, not this trade record. Keep the distressed-bounce thesis out of this dossier's attribution; track separately
if at all.

**Narrative**
All three personas converged on no-trade because the event is a non-catalyst on inspection: the 2026-07-13 date is
the lapse of a 3-year OTC marketing exclusivity, not a composition-of-matter patent, and a lapse only lets the FDA
begin accepting ANDAs — it does not put a competing generic on the shelf. Opill is immaterial to Perrigo (under
~1.5-2% of revenue), and no ANDA, Paragraph IV filing, or generic launch was found. The quant's converged model makes
this concrete: E[move] ≈ -0.095% and net EV ≈ -0.15% after costs, with event-attributable variance only ~1.2% of the
stock's 1-day total — the other ~98.8% is uncompensated exposure to an unrelated distress complex (infant-formula
divestiture, litigation, leverage, negative operating cash flow). The bull conceded fully and withdrew its idea, the
bear held firm at ~85% confidence in no meaningful move, and the quant set size to 0. The single lingering
disagreement is procedural — whether an unrelated distressed-bounce idea belongs near this dossier at all — and all
three agree it must not be attributed to the Opill event.
