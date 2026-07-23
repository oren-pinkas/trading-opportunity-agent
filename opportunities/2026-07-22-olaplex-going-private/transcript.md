# Research Debate Transcript — OLPX (Olaplex Holdings going-private merger)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Debate run: 2026-07-23T21:30:06Z (current UTC at research time).

Source: OLAPLEX HOLDINGS, INC. Form DEFM14C - FY2026, filed 2026-07-22.
https://www.sec.gov/Archives/edgar/data/0001868726/000119312526202411/d544500ddefm14c.htm

Data check performed before the debate: `toa price OLPX <ts> --provider twelvedata` returned
HTTP 400 for 2026-07-22 and 2026-07-23, while `toa price AAPL` priced fine on the same dates —
i.e. OLPX is currently unpriceable via the house real-data provider. This was injected into
every persona's context per house lesson (NYAX case, 2026-07-12-nayax-cyber-breach-ultimatum).

Relevant house lessons injected (all personas):
1. (CZR) Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward.
2. (CZR) Never map a corporate/legal calendar date directly onto an execution timestamp — derive fill time from the nearest valid trading session.
3. (PLD) A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge; simulate-plans has no path-dependent stop-loss enforcement — only diffs fixed entry/exit prices.
4. (PLD) When the actual entry fill prints outside the planned entry band, treat that as an early falsification signal.
5. (NYAX) Test-query the real price provider for exact plan timestamps during research — an unpriceable plan resolves as uninformative-neutral.

---

## Round 1 — Independent research

### Bull (opening)

OLPX filed a DEFM14C, not a DEFM14A. That distinction is the whole trade. A DEFM14A solicits a
vote — meaning outcome is still uncertain and subject to a shareholder meeting, proxy fights, and
potential vote-down risk. A DEFM14C is filed when a majority of voting power has already delivered
written consent approving the merger (Reg 14C, no vote needed). Legally, the shareholder-approval
risk — historically the single largest source of merger-arb blowups — is already retired before
this filing even hits EDGAR. What's left is a mechanical process: information/waiting period (Rule
14c-2's ~20-day minimum from mailing), then closing.

Evidence: Sourced — OLPX filed DEFM14C on 2026-07-22 (SEC EDGAR, accession
000119312526202411). Sourced (dossier) — expected closing window 2026-09-15, ~8 weeks out,
consistent with the mailing period plus standard closing conditions. Inferred (could not pull the
per-share consideration from the filing in this session) — thesis assumes OLPX trades at a
discount to deal price; that spread is the return driver and must be confirmed before sizing.

Proposed action: Long OLPX, merger-arb structure — buy the spread between market price and stated
cash consideration, hold to close. Entry as close to now as a valid session allows; exit rolled
forward from 2026-09-15 to the next open trading session after close is confirmed (lesson #2).
Expected profit: the arb spread annualized over ~8 weeks — typically low-single-digit-percent
absolute for a consent-secured deal, with high win-rate.

Pricing-data risk acknowledged explicitly: HTTP 400 on toa price for OLPX (AAPL prices fine same
day) suggests thin-to-no intraday coverage, plausibly consistent with a stock already trading
near-mechanically at the deal price. Per lesson #5, if this can't be priced, the plan is not
simulate-able — flagged as informative about liquidity, not a reason to abandon the thesis.

### Bear (opening)

A DEFM14C means majority-holder written consent already secured the vote — no shareholder-approval
risk left to trade, and the market has had this information since the 2026-07-22 filing (or
earlier, since consent deals are often pre-negotiated/leaked). Merger-arb spreads on
consent-secured, no-vote-risk deals compress to reflect only closing-mechanics/regulatory risk —
often just a few percent annualized. The DEFM14C is a confirmation event, not new information —
low-alpha by construction; a naive "easy money" read likely ignores that professional arb funds
with lower cost of capital have already compressed this spread.

What blows this up: regulatory delay/block (HSR second requests, foreign regulatory holdups);
financing contingency (sponsor debt commitment letters, financing-out/reverse-termination-fee
exposure if credit tightens); deal-price renegotiation/MAC claim — Olaplex has a documented history
of guidance cuts, a specific and real reason a sponsor could push for a price cut, not merely
hypothetical; litigation (routine disclosure suits, usually nuisance but can delay); and a
governance red flag — a controlling-holder consent structure gives minority holders less leverage
and transparency.

Tradability: the HTTP 400 is disqualifying, not incidental — OLPX-specific while AAPL prices fine
same day, consistent with thinning float, wide bid-ask, or a delisting-in-progress data-vendor
flag as a merger nears completion. Per lesson #5 this alone should stop the trade regardless of
fundamental view.

Recommended action: No trade. If forced, token/nominal size only, flagged as unverifiable P/L for
post-mortem.

### Quant (opening)

Base rate: DEFM14C retires vote risk entirely. For signed going-private deals with consent locked
and no announced antitrust/financing overhang, historical completion runs ~95%+. Set P(close by
2026-09-15) = 0.90 (shaved for closing-condition tail, unknown regulatory posture, incomplete read
of filing conditions); P(break) = 0.10.

EV calc (merger-arb frame): the deal consideration per share is NOT available from this dossier —
a disqualifying gap for a real arb, but sensitivity illustrated: assuming an illustrative ~2%
gross spread at ~55 days to close and a 25% break-downside — EV_gross = (0.90 × +2.0%) + (0.10 ×
−25%) = +1.8% − 2.5% = **−0.7% per trade, before costs**. Tight spreads are dwarfed by break-case
downside even at modest break probability; sign flips entirely on the true (unknown) spread.

Does the edge survive? No, on two independent grounds, either fatal alone: (a) missing deal-price
input — no computable spread, no edge to size; (b) unpriceable in the house provider — HTTP 400 for
OLPX vs. clean AAPL price same days. Per lesson #5, this resolves as uninformative-neutral;
simulate-plans only diffs fixed entry/exit prices (lesson #3) — no series, nothing to diff.

Recommended action: NO TRADE (stand aside). Thesis confidence (deal closes): ~90%. Executable-plan
confidence: ~0%.

---

## Round 2 — Rebuttal

### Bull (rebuttal)

Bear's litigation/MAC-repricing scenario is plausible but unevidenced — nothing in the DEFM14C
indicates an asserted MAC claim; guidance-cut history is a reason a sponsor might walk
*pre-signing*, not necessarily post-signing absent a new specific trigger. Quant's EV calc is
honest but the 2% spread is assumed, not observed — a controlling-holder-consent deal may carry a
tighter break-downside than the assumed 25%, since the biggest ordinary-merger break mode (vote
failure) is structurally removed; quant's generic small-cap prior doesn't capture that.

What would change my mind: an observed deal spread showing negative/near-zero carry, a confirmed
MAC assertion, or a working price feed showing wide bid-ask/thin float consistent with bear's
"untradeable" read.

Honest conclusion: **no, this is not actionable today.** Both bear and quant are right that the
fundamental thesis is separable from the execution question, and the HTTP 400 is not incidental —
cannot size, spread-check, or mark this position without a price. Concur: NO TRADE / dossier-only
pending a working OLPX price feed. Thesis stands as a monitoring item, not a trade to execute now.

### Bear (rebuttal)

Bull and quant both anchor on "vote risk retired, therefore the biggest historical blowup source
is gone" — the mechanism isn't disputed, the conclusion is. Retiring one tail risk doesn't shrink
the remaining risk stack; it makes the remaining risks (regulatory, financing, MAC/repricing,
litigation, governance) the *entire* remaining distribution. Quant's own math shows even a 10%
break probability at a 2% spread is roughly break-even-to-negative — that's not a footnote, it's
the trade. Nobody has adjusted P(break)=0.10 for Olaplex's specific repricing history.

On the HTTP 400: bull's "unprovable but directionally correct — informative about liquidity, not a
reason to abandon the thesis" conflates "the thesis may be right in reality" with "therefore act on
it here" — that's the cop-out. Quant gets it right: 90% thesis confidence and ~0% plan confidence
are different numbers, and only the second gates a trade.

What would change my mind: (1) a working, quotable OLPX price/spread from a real provider; (2) an
actual deal-price/current-offer figure so EV can be computed, not assumed; (3) evidence the merger
agreement lacks a financing-out/reverse-termination structure; (4) HSR/regulatory clearance status.
Absent all four: no trade, or token size only.

### Quant (rebuttal)

Bull's "unprovable but directionally correct" is narrative, not numbers — a spread whose sign I
can't observe cannot enter an EV calc; reframing the data failure as "informative about liquidity"
is a qualitative pivot, not an input. No change to EV.

Bear's MAC-repricing risk is the only substantive new input from either side. Olaplex's
guidance-cut history is FACT and does raise conditional renegotiation risk. Adjustment: lift
P(break-or-reprice) from 0.10 to ~0.15 (~0.09 clean break, ~0.06 downward reprice at roughly half
the break-downside). This lowers P(clean close at original terms) from 0.90 to 0.85. Does not
rescue the trade — a higher, better-characterized downside on an unobservable spread makes EV
worse, not investable.

Fact vs. assumption: FACT — DEFM14C filed (retires vote risk); HTTP 400 for OLPX; Olaplex
guidance-cut history. ASSUMPTION — every probability/magnitude above; the 2% spread remains a
placeholder, not a quote.

Final numeric take: P(close on original terms) ~0.85, P(break) ~0.09, P(downward reprice) ~0.06.
Position size: ZERO — no price series to diff (lesson #5); bear's thinning-float/delisting read
makes a fillable spread less likely, not more. Thesis confidence: 82/100. Actionable/simulatable
confidence: 3/100. Recommendation unchanged: NO TRADE.

---

## Round 3 — Synthesis (opus)

All three personas converged on the same verdict; the bull explicitly conceded in Round 2. Not a
coin-flip.

**hypothesis**
- statement: OLPX is in a going-private merger (DEFM14C filed 2026-07-22, expected close
  ~2026-09-15). Shareholder-vote risk is already retired via majority written consent, so the
  residual break distribution is dominated by regulatory, financing, MAC-repricing, litigation, and
  controlling-holder governance risk. The directional thesis (spread likely closes at original
  terms) is probably correct in reality, but is NOT actionable here: the deal-price/consideration
  figure is missing and the OLPX price feed returns HTTP 400 on the relevant dates, so no real
  entry/exit spread can be computed or simulated.
- direction: no-trade
- confidence: 82 (thesis-that-deal-closes confidence; actionable/simulatable-trade confidence ~3)

Quant's Round 2 numbers: P(clean close at original terms) ~0.85, P(clean break) ~0.09, P(downward
reprice) ~0.06.

**plan** — STAND ASIDE (no trade)
- action: STAND_ASIDE, ticker: OLPX, position_size: 0, entry: null, exit: null,
  expected_profit_pct: null (no timestamps invented, per house lesson #5)
- Blocking conditions: (1) unpriceable feed — `toa price OLPX --provider twelvedata` returns HTTP
  400 on 2026-07-22/23 while AAPL prices fine same dates; no usable price series means
  simulate-plans has nothing to diff. (2) missing deal price — per-share merger consideration was
  never available; without it the spread/EV/break-downside are all unquantifiable, and quant's
  illustrative EV (unconfirmed 2% spread) came out negative (−0.7% gross) even before this gap.
- Reopen criteria (all required): working OLPX price feed (400 resolved, verified sane); confirmed
  per-share deal price from the DEFM14C; observable market spread to deal price at a real
  timestamp; merger-agreement financing-out/reverse-termination-fee and HSR/regulatory clearance
  status read; EV recomputed with real spread + real downside, requiring positive EV net of costs.

**dissent** (strongest unresolved disagreement, gold for post-mortem)

The HTTP 400 pricing failure: incidental data-plumbing glitch vs. material adverse signal about the
instrument itself. Bull/quant treat it as a tooling constraint carrying no information about deal
risk (blocks execution, doesn't change thesis confidence). Bear treats it as an OLPX-specific
signal — AAPL prices fine same dates — possibly reflecting thinning float/delisting-in-progress/
impaired live quoting, which should lower thesis confidence, not just gate execution. Nobody ran
the diagnostic that would resolve which reading is correct (is the 400 a provider/symbol-coverage
gap, or genuinely impaired quoting?). Whichever way it resolves changes both the reopen path and
whether the 82 thesis-confidence number was even correct. Secondary unresolved thread: whether
quant's P(break-or-reprice) bump to 0.15 adequately prices Olaplex's guidance-cut history as a MAC
vector, or whether bear's fatter reprice tail is warranted.
