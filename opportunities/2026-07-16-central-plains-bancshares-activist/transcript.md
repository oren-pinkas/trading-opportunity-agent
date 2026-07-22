# Research debate transcript — 2026-07-16-central-plains-bancshares-activist (CPBI)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet),
quant (opus). Synthesizer: opus. Run at 2026-07-22T08:59:54Z UTC.

Event: Stilwell Activist Investments disclosed a ~9.73% stake in Central
Plains Bancshares (CPBI) and sent a public letter (SEC Form DFAN14A, filed
2026-07-14, disclosed 2026-07-16) criticizing weak share repurchase activity
despite the stock trading below book value.
Source: https://www.sec.gov/Archives/edgar/data/0001979332/000092189526001807/dfan14a10318031_07142026.htm

Relevant lessons injected (from prior post-mortems, event.type=regulatory):
1. [CZR, 2026-07-12] Validate every entry/exit timestamp falls within an open
   trading session; roll non-trading exit dates forward to the next open
   session.
2. [CZR, 2026-07-12] Never map a corporate/legal calendar date directly onto
   an execution timestamp — treat such dates as catalysts and derive the
   fill time from the nearest valid trading session.

---

## Round 1 — Independent research

### Bull

Price data unavailable via `toa price CPBI --provider twelvedata` (HTTP 400,
no coverage at the time) — working from SEC filing evidence alone.

Read: textbook small-cap bank activist setup. Stilwell — a serial small-bank
activist with a track record of forcing buybacks/sales at thrift converts —
disclosed a 9.73% stake and sent a public letter hammering management for
under-deploying capital via buybacks while trading below book value. Stilwell
doesn't take 10% positions and write letters to be ignored — they escalate
until management acts. The below-book valuation is the setup; the letter is
the trigger.

Evidence: SEC DFAN14A (cited above), 9.73% stake, below-book + weak
repurchases narrative. Historically prompts an accelerated buyback
authorization within weeks to defuse activist pressure (Stilwell's playbook
at prior thrift holdings).

Proposed action: long CPBI, entry at the next valid trading session, catalyst
window through 2026-09-01 (~6 weeks), target = re-rating toward tangible
book value (30-50% discount closure typical within one quarter of public
pressure), exit at/before the impact window or earlier on buyback news. Risk
control: below-book value provides a natural floor.

### Bear

No live price data available at the time. Bearish on trading this catalyst.

Read: a garden-variety small-bank activist letter — not a tender offer, board
fight, or merger proposal. No forcing mechanism, no stated deadline besides
the dossier's impact window.

Risks: (1) already priced in — Stilwell is a known serial activist, and thin
microcap bank names re-rate fast on activist headlines; no pre/post price
move has been shown to underwrite an edge. (2) no catalyst forcing
management's hand within 6 weeks — a letter is not a settlement, proxy
commitment, or board seat; small bank boards often sit on letters for
quarters/years; the 2026-09-01 window looks like an arbitrary date bolted
onto a corporate-letter timeline (the exact failure mode flagged in the CZR
post-mortem). (3) liquidity/float risk — thin volume, wide spreads, small
free float typical of this structure. (4) base rate — Stilwell runs a
portfolio strategy across dozens of small thrifts/banks simultaneously; most
campaigns are slow/incremental, not resolved in 6 weeks. (5) below-book could
reflect legitimate fundamentals (rate risk, credit normalization, low ROE)
rather than mispricing — nothing in the dossier addresses CPBI's actual
capital ratios or credit quality.

What would change my mind: evidence of an actual price dislocation
(pre-letter vs. post-letter), a concrete forcing event before 2026-09-01,
confirmed adequate liquidity, or bank fundamentals showing the discount is
unwarranted.

### Quant

Pulled a real price via `toa price CPBI 2026-07-21T19:45Z --provider
twelvedata`: **CPBI $20.48** (near close). Most 1-minute bars in the session
returned no print — direct evidence of thin trading (sub-$300mm microcap
thrift, wide spreads, shallow depth).

Base rates: Stilwell-style thrift activism has a high (>50%) success rate on
governance/buyback/sale outcomes over a 12-24 month horizon — but the
relevant window here is 6 weeks (to 2026-09-01). Near-term (<6wk) probability
that a first letter alone forces a concrete catalyst is historically ~15-20%.
The initial disclosure pop (2026-07-16) is 5 trading days old by the
reference price and is likely already reflected in the quote.

Probability table (6-week horizon, from $20.48):

| Outcome | Prob | Move |
|---|---|---|
| Positive catalyst (buyback bump / stake increase / board concession) | 18% | +8% |
| Drift up, no hard catalyst | 22% | +2% |
| No movement | 45% | 0% |
| Fade (initial pop unwinds) | 15% | -6% |

Gross EV = (0.18×8) + (0.22×2) + (0.45×0) + (0.15×-6) = **+0.98%**.
Round-trip spread/slippage on this illiquid microcap: realistically
1.5-2.5% (conservative estimate: 2.0%). Net EV = **-1.0%** (negative).

Verdict: **PASS / no trade** — the edge does not survive costs. Even bumping
the catalyst probability to 25%, net EV is still ~-0.4%.

Operational flag: 2026-09-01 is Labor Day (US exchange holiday) — any exit
must roll forward to 2026-09-02.

---

## Round 2 — Rebuttal

### Bull rebuttal

Concedes: the quant's ~2% round-trip cost estimate is fair, and the Round 1
"favorable risk/reward, full stop" framing was too glib without a cost
estimate attached — a below-book thesis is worthless if the spread eats the
edge before the catalyst fires. Also concedes to the bear: a letter isn't a
forcing mechanism, "Stilwell doesn't write letters to be ignored" doesn't
settle the timeline, and there's no specific date (shareholder meeting, proxy
deadline, board response window) inside 2026-09-01 to point to — a real gap.

Pushes back: the quant's probability table may reflect a generic small-cap
activism base rate rather than one conditioned on Stilwell's specific
campaign history (dozens of prior thrift/bank targets); if the positive-
catalyst probability is really 25-28% rather than 18%, net EV flips positive
even after the cost haircut. Also pushes back on the bear: "already priced
in" is asserted, not demonstrated — nobody in the debate has actually pulled
a pre-2026-07-14 vs. post-2026-07-16 price series; the quant's single
2026-07-21 print doesn't establish that either.

Revised action: size down materially to a small starter position (not full
conviction), require a confirmed executable spread check before entry, keep
the below-book floor as the risk control since neither bear nor quant
rebutted that the downside is structurally cushioned — only the timing and
cost of the upside.

### Bear rebuttal

Argues the quant's independent, purely execution-mechanics-based math (gross
EV +0.98%, eaten by ~2.0% cost, net -1.0%) converges with her own
fundamental/informational case (already-priced-in, no forcing mechanism) on
the same PASS conclusion via two entirely different methodologies — calls
this convergence the strongest evidence in the debate.

Concedes: the DFAN14A's specific ask (below book + under-deployed capital +
buyback demand) is more concrete than her Round 1 framing gave credit for,
and Stilwell's track record forcing buyback/sale outcomes is a legitimate
base rate — for a 6-12 month horizon.

Counters the bull: his own "30-50% discount closure within one quarter" is
materially longer than the 6-week window this trade is scoped to — the bull
is underwriting a quarter-plus thesis into a 6-week wrapper. The quant's own
breakdown (45% no-movement, 15% fade, only 18% positive-catalyst inside 6
weeks) is not a distribution you underwrite a directional long against,
especially with transaction costs layered on.

Final: PASS, more confidently than Round 1 — the bull's thesis is
directionally plausible on a 3-6 month horizon; not actionable on this 6-week
catalyst window.

### Quant rebuttal

Stress-tested own Round 1 EV math against both opponents.

On cost: granting the bull's "use limit orders" argument, best-case
round-trip cost could drop from ~2.0% to ~1.3% (passive entry, but the exit
leg — the moment everyone wants out — likely still crosses the spread).

On the floor argument: partially fair. If below-book genuinely truncates
downside, the -6% fade tail is too fat; tightened to -3% with adjusted
probabilities. But the bear's fundamentals point (below-book could reflect a
real ROE/credit/rate problem, not mispricing) caps how much credit this
deserves — estimated at +0.2% EV improvement, not enough alone.

On "already priced in": agrees with the bear — this is already baked into
the probability table (which is why the positive-catalyst move is framed as
+8% incremental, not the full 30-50% discount-to-book the bull cites) and
doesn't permit raising the catalyst probability further absent a fresh, dated
forcing event, which doesn't exist in the filing.

Sharpened probability table: positive catalyst 18% (+8%), drift up 22%
(+2%), no movement 47% (0%), fade 13% (-3%). Gross EV = **+1.49%**
(up from +0.98% after crediting the floor). Net EV at 2.0% cost = **-0.5%**;
net EV at optimized 1.3% cost = **+0.19%** — razor-thin positive, resting
entirely on flawless passive execution in a name whose order book is mostly
empty (the same condition that makes passive fills unreliable).

Final: **PASS / no trade** — the edge lives entirely inside the
transaction-cost error bar and does not survive realistic execution. Would
flip to a small long only with a documented pre-catalyst price dislocation
or a dated forcing event before the window closes. Neither exists today.
Operational flag reaffirmed: 2026-09-01 is Labor Day — any exit must roll to
2026-09-02.

---

## Round 3 — Synthesis (opus)

**hypothesis:**
- statement: Stilwell's 9.73% stake and public DFAN14A letter demanding
  buybacks against a below-book valuation is a directionally plausible
  re-rating thesis on a 3-6 month horizon, but has no dated forcing
  mechanism inside the scoped 6-week window (2026-09-01). CPBI is a
  sub-$300mm microcap thrift trading at $20.48 (twelvedata, 2026-07-21T19:45Z)
  with mostly-empty 1-minute bars, confirming thin liquidity and wide
  spreads. The quant's EV math (gross +0.98% to +1.49%, depending on floor
  assumptions) is erased by realistic round-trip execution cost of ~2%, and
  even optimistic limit-order execution only reaches a razor-thin +0.19% net
  EV that does not survive a single bad exit print in a name this illiquid.
  The initial disclosure pop (2026-07-16) is five trading days old by the
  quant's reference price and is likely already reflected in the quote. No
  position clears the bar within this window.
- direction: none
- confidence: 72

**plan:**
- ticker: CPBI
- action: no-trade
- entry: time null, target_price null
- exit: time null, target_price null
- expected_profit_pct: -1.0

**dissent (strongest unresolved disagreement):**
Whether the positive-catalyst probability is correctly ~18% (quant's generic
small-cap activism base rate) or materially higher at ~25-28% (bull's claim
it should be conditioned on Stilwell's specific campaign history at prior
thrift targets). This single input is the pivot: at 18% net EV is negative;
near 25-28% net EV flips positive even after costs. It stayed unresolved
because nobody pulled the two pieces of evidence that would settle it — an
actual pre/post price series to test the contested "already priced in"
assumption, and a Stilwell-specific 6-week catalyst conversion rate. Both
quant and bull stated they would flip to a small long given a documented
pre-catalyst price dislocation or a dated forcing event inside the window;
neither exists today.

Operational flag carried through all three rounds: 2026-09-01 is Labor Day
(US exchange holiday) — had a trade been taken, any exit would need to roll
to 2026-09-02.
