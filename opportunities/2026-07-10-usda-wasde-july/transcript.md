# Research Debate Transcript — 2026-07-10-usda-wasde-july

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant
(opus). Synthesizer: opus. Run at 2026-07-12T16:37:26Z, ~2 days after the event's
impact window (2026-07-10).

## Event

USDA's July 10, 2026 WASDE report landed with soybean futures at a two-month high
heading into the print, driven by rising crush/export demand forecasts — a setup
framed as a volatility catalyst for ag processors (ADM) and fertilizer names (MOS).

Source: "Special Edition – Market Trends Report – USDA Report July 6, 2026" - Grain
Farmers of Ontario, https://gfo.ca/market-trends/special-edition-market-trends-report-usda-report-july-6-2026/
(accessed 2026-07-08T14:26:18Z).

## Price data used (toa price, stub/deterministic feed)

- ADM: 2026-07-09T20:00Z (pre-report) = $46.38; 2026-07-10T14:30Z (report day) =
  $70.40; 2026-07-12T16:00Z (analysis time) = $67.75
- MOS: 2026-07-09T20:00Z (pre-report) = $247.69; 2026-07-10T14:30Z (report day) =
  $317.07; 2026-07-12T16:00Z (analysis time) = $284.58

Implied: ADM +51.8% report-day pop then -3.8% pullback into analysis time; MOS +28.0%
report-day pop then -10.2% pullback into analysis time. All three personas
independently flagged these magnitudes as implausible for these tickers on a routine
monthly release (base rate ±1-4%), i.e. likely a stub/feed artifact rather than a
real market move.

## Institutional lessons injected (type=economic)

1. Anchor entry to a live pre-event quote, not the research-day price; if drift
   exceeds ~0.5-1% from the plan anchor, re-derive targets/EV or void the trade
   rather than filling blind. (2026-07-06, `2026-07-01-ism-mfg`)
2. When the thesis is "catalyst reprices X higher" and X has already rallied to a
   52-week high before the event, treat the move as priced-in: fade or shrink,
   don't chase the entry. (2026-07-06, `2026-07-01-ism-mfg`)
3. Skip trades whose only positive-EV path is a pre-market conditional entry the
   harness cannot fill; if the executable cash-open leg's EV is ~0, don't record
   the trade. (2026-07-06, `2026-07-02-june-jobs`)
4. After a known regime shift, require a differentiated surprise vs. consensus
   before trading a data print: an in-line print is already in the curve.
   (2026-07-06, `2026-07-02-june-jobs`)

---

## Round 1 — Independent research

### BULL (sonnet)

Read: the report landed into a market already leaning bullish (soybean futures at a
two-month high pre-print per the GFO note), consistent with a confirmation event —
both names gapped hard on the day. Two days out, the initial spike has partially
cooled (ADM -3.8%, MOS -10.2% off report-day highs) but hasn't fully round-tripped,
which reads as digestion of a real repricing rather than pure noise.

Data-quality flag: a +51.8%/+28.0% single-day move on a WASDE report is not
something expected historically for large-cap diversified processors/fertilizer
names; flagged as likely stub/test data, but treated the *directional* pattern
(gap, partial fade) as the tradeable structure while distrusting the magnitude.

Proposed action: **Long ADM only** (pass MOS — weaker/more indirect linkage to a
soy-specific report, and its pullback is sharper/less durable). Entry at the live
quote $67.75 (2026-07-12T16:00Z, not the stale pre-report price or the transient
spike high, per lesson 1). Target: retest of the $70.40 report-day high (+3.9%).
Stop: $65 (~-4%). Half-size given the data-integrity concern.

### BEAR (sonnet)

Data coherence: the observed moves (+51.8% ADM, +28.1% MOS) are not believable for
mega-cap, high-liquidity names on a routine monthly release — moves of this scale
would be front-page news and would likely trip circuit breakers; reads as a
stub/deterministic feed artifact. Any EV math built on these levels is untrustworthy
until confirmed against a real data source.

Even taking the data at face value: today (2026-07-12) is two full trading sessions
past the July 10 print — not a live catalyst window. Per lesson 3, this isn't just
late to the open, the informational asymmetry was arbitraged away within minutes of
release. Both names are already fading from report-day highs (ADM -3.8%, MOS
-10.3%), the classic signature of an overreaction unwinding rather than a
fundamental re-rating being confirmed. Per lesson 2, the underlying (soybean
futures) was already at a two-month high *before* the report on the same
crush/export narrative — the report's directional message was largely priced in
already.

Flagged MOS's weak/indirect linkage (fertilizer producer, not a crush/export
processor) as an additional reason to discount that leg specifically. No verified
consensus-vs-actual WASDE figures exist in the sources to confirm a genuine
differentiated surprise (lesson 4).

Proposed action: **No trade**, on two independent sufficient grounds — data
credibility and stale/priced-in catalyst. If forced to lean, a small skeptical
short-fade on MOS, unsized without verified data.

### QUANT (opus)

Timing: today is ~2 days after the print; edge on an event trade comes from being
positioned across the print or from a pre-positioned anchor, neither available now.
Drift from the pre-report anchor is +46% (ADM) / +15% (MOS) — an automatic void
condition per lesson 1.

Base rates: normal WASDE-day equity reaction for ADM (~±1-2%, tail ±3-4%) and MOS
(~±1-3%, tail ±5-6%). The observed +51.8%/+28.0% moves are ~25-40 sigma outliers —
outside the historical distribution entirely. P(feed materially wrong) ≈ 0.90;
P(feed roughly right) ≈ 0.10.

EV calculation (granting the feed for argument's sake), fade-the-spike short MOS at
$284.58 toward the pre-report $247.69: P(continued reversion) 0.55 × +4% -
P(continuation) 0.45 × -4% = +0.40% gross, minus 0.30-0.50% costs/borrow ≈ ~0% net.
Blended across feed-reliability states (0.90 × void/negative, 0.10 × ~0%): blended
EV < 0. Per lesson 2, chasing processor/fertilizer equities after both the futures
rally and the report is buying the second derivative of an already-consumed
catalyst.

Proposed action: **No trade** on ADM and MOS. Would flip only given (1) a verified
real feed replacing the stub, (2) evidence of a genuine consensus surprise with
coherent equity read-through, (3) a concrete borrow cost/fill to re-run EV.

---

## Round 2 — Rebuttal

### BEAR

Converges with quant via a different route — quant's "25-40 sigma / P(feed wrong)
0.90" is the quantitative spine for the same qualitative "this doesn't look like a
market" objection raised in Round 1. Even the residual MOS-fade trade quant grants
credit to is separately weak on fundamental-linkage grounds.

Directly rebuts bull's "buy the confirmed catalyst on the dip": entry, target, and
stop are all derived from the disputed print (the $70.40 target is a retest of the
same implausible number; the stop is sized off a base established by the spike). You
cannot trust the *shape* of the price path while discarding its *scale* — the
pattern is a feature of the disputed data, not independent confirmation that
survives if the magnitude is discarded. Reiterates the priced-in argument
independent of data quality: a report that confirms an already-building narrative
is an anticlimax, not a fresh catalyst, and nothing points to the current level
being a floor rather than a waypoint back toward pre-print levels.

### BULL

Concedes fully. Bear's "already priced in pre-report" point breaks the confirmation
framing at its root, independent of data quality: inferring "the report confirmed
the narrative" from post-print price action is circular once the pre-print rally on
the same narrative is accounted for. Concedes no independent verification of a
differentiated surprise exists — the case was built by using suspect price data to
validate itself. Concedes quant's base-rate framing removes any fundamental anchor
for the $70.40 target: if a real ~25-40 sigma surprise happened, that instability
argues for reversion, not continuation; if it didn't, the target has no anchor at
all. Notes quant's EV logic actually transfers worse for a continuation (long ADM)
trade than for a reversion (short MOS) trade, meaning the original long idea was the
weaker of the two directional options on the table, not a superior third path.

**Moves to No Trade on ADM**, matching bear and quant. Would need (1) a corrected
feed showing a real, unreversed, sane-magnitude ADM move, or (2) verified
WASDE actual-vs-consensus figures confirming a genuine crush/export beat, to revive
a much smaller version of the original idea.

### QUANT

Formalizes bull's concession as a category error: a percentage move is defined by
(P_t - P_anchor)/P_anchor — if the anchor is corrupted enough to produce a 25-40
sigma print, sign and magnitude are drawn from the same untrusted object; there is
no clean channel for direction alone. The "spike/fade/stabilize" pattern is
observationally identical to a stub feed that inserts one bad print and reverts,
meaning it carries ~zero incremental information above the glitch prior.

Re-runs long ADM numerically: feed-real branch (P=0.10) EV -0.49% (catalyst stale,
continuation odds ~0.45 even ignoring feed risk); feed-broken branch (P=0.90) EV
≈ -3% to -4% (entry price itself fictional, reversion toward true pre-report level).
Blended ≈ -2.75%/unit — the worst leg on the board; half-sizing doesn't flip the
sign.

Re-runs short MOS fade: bear's fundamental-linkage point sharpens rather than
weakens this leg (weaker linkage makes the +28% print less credible, which
*supports* the reversion-down direction) — the only leg directionally robust across
both feed states. But feed-real branch nets ~0 after costs (+0.05%), and
feed-broken branch means 90% of the time there is no real spike to fade at all
(phantom setup, can't fill/borrow against it) — realized ≈ -0.3%. Blended ≈ -0.27%,
still negative and the edge is largely fictitious.

**Conclusion: unambiguously No Trade** on every instrument/sizing/direction
considered. Final confidence in the no-trade call: 90/100 (the residual 10% is the
small chance the feed is real, but no-trade is robust even within that branch since
conditional EV is negative-to-flat there too).

---

## Round 3 — Synthesis (opus)

**hypothesis**
- statement: No credible, tradeable edge exists in ADM or MOS on the July WASDE
  catalyst. The observed report-day price series (~25-40 sigma moves, +51.8% ADM /
  +28% MOS) is non-credible and reads as stub/feed-glitch data (P(feed materially
  wrong) ≈ 0.90); the directional "spike-fade-stabilize" pattern is inseparable
  from the disputed magnitude and cannot be trusted on sign alone. Independently,
  even at face value the catalyst is stale (2 days old at analysis time), the
  pre-report thesis (crush/export demand, soy futures at 2-month highs) was already
  priced in before the print, and both names are already fading from report-day
  highs. MOS also has weak, indirect fundamental linkage to a soy-specific WASDE.
  Every instrument/sizing/direction considered carries negative or fictitious
  (phantom-P&L) expected value.
- direction: none
- confidence: 90

**plan**
- ticker: ADM/MOS
- action: no-trade
- entry: {time: null, target_price: null}
- exit: {time: null, target_price: null}
- expected_profit_pct: null

**dissent**

Convergence was full and genuine (bull opened Round 1 long ADM at $67.75 and
explicitly conceded to no-trade in Round 2), so no directional disagreement
survives. The residual worth preserving for post-mortem is a difference in
reasoning path: bull retains a weaker belief that a real-but-smaller signal could
exist beneath the corrupted feed (a differentiated WASDE surprise a clean data
source might confirm), whereas bear/quant hold a more totalizing skepticism grounded
in the priced-in/stale-catalyst argument, which kills the trade even if the data
were pristine. Revisit only if ALL of: (1) an independent, verified feed confirms
the report-day moves were ordinary-scale (~±1-4%), collapsing the feed-glitch null;
(2) evidence of a genuine differentiated WASDE surprise not already reflected in
pre-print futures positioning; (3) fresh positioning available before the next
print, since the only ever-positive-EV path was pre-report entry.
