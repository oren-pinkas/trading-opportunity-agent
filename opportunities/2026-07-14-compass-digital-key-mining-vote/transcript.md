# Debate transcript — 2026-07-14-compass-digital-key-mining-vote

Strategy: `debate-three-round-panel` (bull/bear sonnet, quant opus; synthesizer opus).
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: Compass Digital Acquisition Corp (CDAQF) shareholders vote July 15, 2026 on a
fifth extension amendment (pushing the outside date to as late as January 20, 2027)
to complete the business combination with Key Mining Corp.

Source: [Compass Digital seeks SPAC deadline extension vote — DEF 14A](https://www.stocktitan.net/sec-filings/CDAQF/def-14a-compass-digital-acquisition-corp-definitive-proxy-statement-9bbdef7d1318.html)
(accessed 2026-07-14T01:15:00Z)

Institutional-memory lessons applied (from `toa lessons-relevant --type regulatory --tickers CDAQF`):
1. "Before finalizing any plan, validate that every entry and exit timestamp falls
   within an open trading session (not a weekend or exchange holiday) for the
   specific instrument, and roll non-trading exit dates forward to the next open
   session." (source: 2026-07-08-caesars-icahn-fertitta-bidding-war)
2. "Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines)
   directly onto an execution timestamp — treat such dates as catalysts and derive
   the fill time from the nearest valid trading session." (source: same)

Data note: attempts to pull a citable price via `toa price CDAQF ... --provider
twelvedata` and `toa price CDAQ ... --provider twelvedata` both failed (HTTP 400 on
CDAQF, HTTP 404 on CDAQ) — treated throughout as a real fact about this thinly-traded
OTC/pink-sheet SPAC vehicle, not a bug to guess around.

---

## Round 1 — Independent research

### BULL

Long CDAQF thesis, confidence LOW-MODERATE. Vote passage near-certain (~98%
insider-controlled voting bloc commits to vote FOR) — no info edge in the vote
outcome itself. Real catalyst framed as the deal-completion trajectory rather than
the vote:

- Merger agreement dated Jan 6, 2026 among CDAQ, Titan Holdings Corp, Titan SPAC
  Merger Sub Corp, Titan Merger Sub Inc., and Key Mining Corp (~USD 230M all-stock).
- Active **Form S-4/A** for Titan Holdings Corp is in progress with the SEC — a
  concrete, dated sign the registration/proxy process is moving
  ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2107523/000149315226016132/forms-4a.htm)).
- Prior **non-redemption agreements** (sponsor economically incentivizing holders not
  to redeem) signal genuine intent to close
  ([Investing.com](https://ng.investing.com/news/company-news/compass-digital-acquisition-corp-enters-nonredemption-agreements-93CH-1443881)).
- Trust redemption price sourced at **~USD 11.82/share** (accreted above the USD 10.00
  IPO reference via interest) — a real, citable NAV figure.
- Counter-signals bull itself flagged: **going-concern** language in the 10-Q, and
  cumulative redemptions of **~USD 225M against a USD 200M IPO raise**, leaving very
  thin remaining public float.
- No live tradeable price for CDAQF/CDAQ found via twelvedata — flagged explicitly as
  a data gap requiring manual verification, not a number to invent.
- Proposed timing: not the vote date itself (per CZR lesson) but positioning ahead of
  S-4/A effectiveness and the eventual merger-closing vote.

Sources cited: [DEF 14A](https://www.stocktitan.net/sec-filings/CDAQF/def-14a-compass-digital-acquisition-corp-definitive-proxy-statement-9bbdef7d1318.html),
[PRE 14A](https://www.stocktitan.net/sec-filings/CDAQF/pre-14a-compass-digital-acquisition-corp-preliminary-proxy-statement-c526ba13e8c1.html),
[10-K](https://www.stocktitan.net/sec-filings/CDAQF/10-k-compass-digital-acquisition-corp-files-annual-report-ed7f8db652f9.html),
[10-Q](https://www.stocktitan.net/sec-filings/CDAQF/10-q-compass-digital-acquisition-corp-quarterly-earnings-report-9d6970fcc769.html),
[non-redemption agreements](https://ng.investing.com/news/company-news/compass-digital-acquisition-corp-enters-nonredemption-agreements-93CH-1443881),
[S-4/A on EDGAR](https://www.sec.gov/Archives/edgar/data/2107523/000149315226016132/forms-4a.htm).

### BEAR

No clean edge, confidence ~85% no-trade.

- Vote outcome structurally near-certain and low-information: sponsors control the
  voting bloc; dissenters exit at trust NAV via redemption rather than voting no, so
  there's no real "fail" tail to price.
- A 5x-extended SPAC signals deal-stall/troubled merger, not optimism — the dossier
  gives no color on *why* extension #5 is needed.
- Redemption mechanics strip out the liquidity-providing holders each round, leaving
  a thinner, more illiquid post-vote float — a structural headwind, not a catalyst to
  trade into.
- OTC/pink-sheet illiquidity (confirmed by the broken price feed: HTTP 400/404)
  implies wide spreads and high slippage that could exceed any theoretical edge.
- At time of writing: no NAV figure, no current price, no trust balance available to
  verify any redemption-arb thesis.
- Would need: a confirmed live redemption-arb spread vs. disclosed NAV with an actual
  tradeable quote, disclosure of why extension #5 specifically is needed, or
  independent volume/price evidence — none present.

### QUANT

PASS, confidence 0.85.

- P(vote passes) ≈ 0.97 — structurally near-certain, no information content.
- P(deal ultimately closes | 5th extension) ≈ 0.30 — de-SPAC completion base rates
  degrade sharply with extension count; a 5th extension to Jan 2027 on a small-cap
  mining target is read as a distressed-tail signal.
- Only structurally valid trade: redemption arbitrage against trust NAV (theoretical
  edge ~0.5-2%), but OTC round-trip friction (spread + slippage, estimated 2-5%)
  likely consumes it entirely — net EV negative before even reaching sizing.
- Long-the-story equity leg is negative-EV at P(close)=0.30 with no anchored upside
  price.
- No price feed = cannot confirm entry below NAV, cannot size, cannot mark: "sizing
  an unmeasurable edge is gambling, not trading."
- Institutional-memory check: July 15, 2026 is a valid trading-session weekday, but
  per the CZR lessons it is a corporate/legal calendar date, not an execution
  timestamp — there is no tradeable "vote" fill, only (at best) a redemption-arb leg
  requiring a verified redemption-deadline session, which cannot be established here.

---

## Round 2 — Rebuttal

### BULL

- Concedes bear's "no NAV figure" objection is resolved (found ~USD 11.82) — but the
  matching **tradeable quote** gap remains: a real data gap, not a thesis flaw.
- Nudges P(close) only modestly, to **0.35-0.40**, based on the S-4/A being an active
  (not dormant) filing and non-redemption agreements being costly/informative signals
  — explicitly frames this as a small revision, not a refutation of quant's
  distressed-tail framing; agrees extension count is still a bad signal in aggregate.
- **Fully concedes** the redemption-arb-as-standalone-trade framing to quant's cost
  math — drops it entirely; the NAV floor was meant as downside protection context,
  not a tradeable arb on its own.
- Now agrees the thin post-redemption float (bear's point) is a bigger liquidity
  problem than credited in Round 1, and there is no vote-day pop to trade — the vote
  is a formality.
- Updated action: still **no trade today**, and no trade until the price-data gap
  closes. Reframes the only live idea as "wait for the S-4/A effectiveness
  checkpoint," not "trade the vote" — and even then, only a small NAV-floor-protected
  position *if* a later citable quote shows a discount to NAV with a spread thin
  enough to survive OTC slippage. Confidence stays LOW.

### BEAR

- Argues the S-4/A + NRAs **sharpen** rather than soften the deal-stall read:
  "paperwork existing ≠ paperwork closing." SPACs routinely file S-4/A amendments to
  clear SEC comment letters, which is itself a friction signal. NRAs are read as a
  bailout/propping-up signal — sponsor capital covering a redemption-driven shortfall
  — not organic conviction that the deal will close.
- Treats the 10-Q **going-concern language** as the dominant fact of the case: a
  formal auditor statement that liquidation is a live, material risk absent
  completing the transaction or raising capital.
- Pushes P(close) lower than quant's 0.30, toward **0.15-0.25**.
- Concedes the NAV objection is resolved by bull's ~USD 11.82 figure, but argues this
  only converts "no info" into "info with no tradeable quote to apply it to" — the
  tradability objection (zero live price, thin float, no visible market maker) is
  unresolved and dominant.
- Agrees with and extends quant's friction estimate (2-5%+, possibly worse given thin
  float — a retail-size order could itself move the print).
- Final verdict: no-trade confidence unchanged to slightly higher, **~85-90%**.

### QUANT

- Updates P(close) from 0.30 to **0.37** given S-4/A progress + NRAs (a real but
  modest signal of intent, not survival) — but notes the redemption arb doesn't
  depend on the deal closing at all (redemption pays NAV regardless of merger
  outcome), so this debate is largely orthogonal to the only structurally valid
  trade.
- Re-runs redemption-arb EV against the ~USD 11.82 NAV anchor:
  - Thin-discount case (3% below NAV, ~USD 11.46 entry): net edge ranges **+1% to
    -2%** depending on assumed friction (2-5%).
  - Wider-discount case (5% below NAV, ~USD 11.23 entry): net edge ranges **0% to
    +3%**.
  - Verdict: the arb only clears when entry discount strictly exceeds friction, and
    the margin is thin in every scenario — "an anchor without a live bid/ask is a
    ruler with no object to measure."
- Incorporates bull's "~USD 225M redeemed vs. USD 200M raised" fact: this **worsens**
  (not just confirms) friction — pushes the estimate to the top of the band and
  beyond (4-6%+) for anything above token size, and independently caps position size
  at "unsizeable" (shares may not even be sourceable at a discount — an unfillable
  trade has EV=0 by construction).
- Blended EV across all executable versions of the trade: **≈0, skewed negative**
  after the thin-float slippage tail.
- Final verdict: **PASS**, confidence 0.85 → **0.88**.

---

## Round 3 — Synthesis (neutral, opus)

**Hypothesis** (direction: none, confidence: 87):

Across three rounds the panel converged to no positive-EV trade in CDAQF. The July 15
vote is near-certain to pass (P ≈ 0.97) because ~98% of the voting bloc is
insider-locked and dissenters exit at trust NAV via redemption rather than voting no,
so the vote itself carries essentially zero tradeable information and produces no
vote-day pop. The forward question — whether the Key Mining de-SPAC actually closes —
was revised only modestly upward on S-4/A registration activity and prior
non-redemption agreements, but those are read as costly signals of sponsor intent
rather than evidence of survival, and the running 10-Q going-concern language plus a
fifth extension keep the completion probability low (panel range roughly 0.15 to
0.40, quant midpoint 0.37). The single structurally valid trade — redemption
arbitrage versus the ~USD 11.82 accreted trust NAV — is killed by a friction wall:
OTC/pink-sheet round-trip cost of 2-6%, worsened by a very thin post-redemption float
after cumulative redemptions of ~USD 225M against a USD 200M raise, meets or exceeds
any plausible discount to NAV, and no live/citable bid-ask ever surfaced (twelvedata
returned HTTP 400 on CDAQF and 404 on CDAQ). With an unmeasurable and likely
unfillable edge, blended EV rounds to zero and skews negative after the thin-float
slippage tail — the calibrated view is stand aside.

**Plan:** ticker CDAQF, action **no-trade**, entry/exit: none (no live tradeable
quote or open-session mark could be sourced to validate any fill), expected profit:
0%.

**Dissent** (strongest unresolved disagreement, for a future post-mortem):

The P(deal closes) spread was never reconciled: bear anchored lowest at 0.15-0.25
(going-concern doubt as the dominant fact), quant sat at 0.37, bull nudged highest to
0.35-0.40 (S-4/A + NRA signals). This gap went unresolved because it is orthogonal to
the only executable trade (redemption pays NAV regardless of merger outcome), so the
panel set it aside rather than settling it. The deeper unresolved unknown is
empirical, not probabilistic: no persona ever obtained a live bid-ask, so whether
CDAQF actually trades at a discount to ~USD 11.82 NAV wide enough to clear 2-6%
friction — and whether shares are even sourceable at that discount — remains
untested. A future post-mortem should record that this case died on a data gap (no
citable quote), not on a resolved probability judgment.

**Verdict: NO-TRADE / PASS.**
