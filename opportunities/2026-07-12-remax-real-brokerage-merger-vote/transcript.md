# Debate transcript: 2026-07-12-remax-real-brokerage-merger-vote

Strategy: `debate-three-round-panel` (bull/bear/quant, models per `config/research.json`:
bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus).

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Debate run: 2026-07-13T08:15:26Z (UTC).

Source: "Real and RE/MAX to Combine into Real REMAX Group Inc." (StockTitan,
DEFM14A proxy filing) —
https://www.stocktitan.net/sec-filings/RMAX/defm14a-re-max-holdings-inc-merger-proxy-statement-82f7e6b8ed81.html
(accessed 2026-07-12T13:03:15Z)

Institutional lessons injected (from `toa lessons-relevant --type regulatory
--tickers RMAX,REAX`, source: 2026-07-08-caesars-icahn-fertitta-bidding-war
post-mortem):
1. Validate that every entry/exit timestamp falls on an open trading session;
   roll non-trading exit dates forward to the next open session.
2. Never map a corporate/legal calendar date directly onto an execution
   timestamp — derive fill time from the nearest valid trading session.

Data-integrity note carried through the whole debate: the `toa price` CLI
shim returned a broken/stubbed feed this session (e.g. RMAX prints of
$249–$400+ against a $13.80/share cash election) — no persona could obtain a
real live spread. This is a confirmed blocker, not merely "not yet checked."

---

## Round 1 — Independent research (parallel, no cross-visibility)

### Bull (sonnet)

Long RMAX to capture the $13.80 cash-election floor. Framed as spread
compression into a high-probability, board-negotiated, no-competing-bid deal
(DEFM14A filed, firm vote date). Aug 14, 2026 confirmed as a Friday (valid
NYSE session, no holiday conflict). Proposed entry ~week of Aug 3–7, 2026
(after typical ISS/Glass Lewis recommendation timing, still ahead of the
vote, to buy once "will advisors recommend FOR" uncertainty resolves).
Proposed exit tied to vote-result release: same day if released during market
hours Aug 14, else rolled to next open session Mon Aug 17, per the
institutional lessons. Preferred RMAX over REAX as the cleaner instrument
(REAX carries acquirer-side dilution/integration ambiguity). Flagged own data
gaps: no live RMAX/REAX quote, no stock-election exchange ratio, no ISS
recommendation status — all needed before real sizing.

### Bear (sonnet)

Skeptical of the "easy merger-arb" framing. Key points, all cited to the
dossier's DEFM14A source plus general merger-arb structure/background
knowledge (flagged as such given no live web access this session):
1. **Dual-key vote** — both RMAX and REAX shareholders must independently
   approve; a single "vote passes" probability hides a joint-probability
   problem.
2. **Cash-pool proration** — stock/cash election mergers routinely cap
   aggregate cash consideration; if oversubscribed, "cash electors" get
   partially bought down into new-entity stock. $13.80 may not be a real
   floor.
3. **REAX-side dilution resistance** — Real Brokerage holders are being
   asked to dilute a growth story to absorb a structurally declining
   franchisor (NAR commission-litigation overhang, leverage, shrinking agent
   count).
4. **Appraisal rights** — dissenting-shareholder appraisal risk is a
   classic underpriced tail in exactly this deal type.
5. **Antitrust/state-licensing delay risk** — closing timeline extends
   holding-period risk without added compensation.
6. **Disclosure timing** — vote results for this kind of meeting typically
   post via 8-K after Friday's close or the next business day, making a
   same-day Aug 14 exit unrealistic.

Recommended **no trade**, pending verification of the cash-pool cap terms,
financing certainty, voting/support agreements, and disclosure-timing
mechanics. Framed the market's apparent "sure thing" consensus (if the spread
is currently tight) as exactly what a bear should distrust on EV grounds.

### Quant (opus)

Flagged the `toa price` feed as returning impossible values (RMAX
$249.09/$280.98, REAX $131.54/$280.67 — incompatible with a $13.80 cash
election) and discarded it, working instead from a parameterized decision
rule on the observable spread.

- P(vote passes) = 0.96; P(full deal completes) = 0.93 — based on base rates
  for board-recommended, definitive-agreement mergers reaching a scheduled
  DEFM14A vote (~95–98% historical completion rate for friendly deals; <2%
  failed-vote rate).
- Break scenario ≈ −25% give-back to standalone value.
- EV formula: `EV = P(complete)·upside − P(break)·downside`. Breakeven
  spread (gross) = (0.07 × 25%) / 0.93 ≈ 1.88%; with ~0.5% round-trip
  costs/slippage, effective entry gate ≈ 2.5–3% observable spread to $13.80.
- Recommended a small conditional long RMAX (~2% NAV, quarter-Kelly sizing —
  full Kelly on these inputs would be ~8%, cut for model-error and tail
  risk), entering only if live spread ≥3%.
- Entry: 2026-07-14T13:30:00Z (Tuesday, next valid session after "now").
  Exit: 2026-08-17T13:30:00Z (Monday, first valid session after the Friday
  Aug 14 vote) — deliberately not trading the event minute itself, per the
  institutional lessons.
- Explicitly gated the entire recommendation on live quotes being checked
  before entry, since the feed was unusable this session.

---

## Round 2 — Rebuttal (parallel, each sees the other two openings)

### Bull rebuttal

Conceded ground: the "$13.80 floor" framing in Round 1 was too loose —
proration could convert part of the cash election into REAX-linked stock
exposure, which changes what asset the trade is actually long. Also conceded
bear's disclosure-timing point outright: adopted Monday Aug 17 exit as the
*base case*, not a contingency exception.

Pushed back: most of bear's risk list (antitrust, appraisal, state-licensing
delay) lives in the post-vote-to-close window, outside a vote-catalyst trade
that exits at the vote result — bull is not proposing to hold to closing.
Conceded the one bear risk that *does* live inside the holding window: vote
adjournment/postponement risk is real and unaddressed. Argued (without hard
data) that quant's −25% break assumption may be conservative on the downside
since failed first votes in friendly deals often lead to re-solicitation with
sweetened terms rather than immediate collapse to standalone value — flagged
this as directional, not load-bearing.

Revised entry gates: now requires confirmed ISS/Glass Lewis FOR
recommendations on **both** RMAX and REAX proxies (incorporating bear's
dual-key point), requires S-4 proration mechanics confirmed, accepts a
slightly lower spread gate (~2.25%) given the vote-only holding-window
argument. Added mitigations: trim to half size into Friday close to reduce
weekend gap risk; consider an options collar if a liquid RMAX chain exists,
to cap the tail quant/bear describe.

### Bear rebuttal

Engaged directly with quant's EV math rather than repeating Round 1: agreed
quant's quarter-Kelly/2% NAV sizing is a reasonable *implementation* of
bear's own risk concerns, not a rebuttal of them. But disputed quant's
**inputs**:
1. P(pass)=0.96 is too high absent confirmed voting/support agreements for
   RIHI (RMAX) and Poleg (REAX) — without that, bear wants the RMAX-leg
   probability below ~0.85–0.88.
2. Cash-pool proration may not be a mere tail risk — it could invalidate the
   "spread to $13.80" reference price itself, since realized value becomes
   contingent on REAX's price at close (an embedded equity-beta component
   quant's simple cash-floor EV calc doesn't capture).
3. The −25% break scenario likely understates downside, since RMAX's
   standalone fundamentals have kept deteriorating (a break isn't a clean
   reversion to the pre-deal price, but to a lower, still-declining
   baseline).
4. The binary complete/break framing misses an "approved-but-delayed"
   scenario (multi-state real-estate licensing approvals) that decays
   annualized return on an already-thin spread without technically breaking
   the deal.

Still recommended **no trade** as the base case, pending: confirmed live
spread ≥3% held across ≥2 sessions, filed voting/support agreements,
confirmed cash-cap/proration formula, ISS/Glass Lewis FOR on both sides with
no organized opposition, confirmed same-day-or-next-session disclosure
precedent, and no pending appraisal-demand/injunction litigation. Would
endorse a scaled-down version of quant's trade once verified, with two added
constraints: don't enter until confirmed no adjournment filing; treat the
realized spread as REAX-price-contingent, not fixed to $13.80.

### Quant rebuttal

Re-checked the price feed (still stubbed: RMAX $400.48, REAX $205.16 as of
2026-07-13T08:15Z) — the blocker persists.

Recomputed P(complete) as a genuine joint probability per bear's dual-key
point: P(RMAX approves) = 0.97 (controlled/insider structure, cash exit
attractive to a legacy franchise holder base) × P(REAX approves) = 0.95
(dilution-optics risk bear raised) → naive product 0.9215, adjusted upward
for positive correlation to a joint **0.93**; combined with P(close|approve)
= 0.96 (state-licensing risk) → **P(complete) revised down from 0.93 to
0.89**. Break probability revised up from 0.07 to 0.11.

Recomputed breakeven spread: Round 1 was ~1.88% gross (~3% with costs);
Round 2 is **~3.09% gross (~4% with costs)**. At a 3% observed spread and
p=0.89, EV is actually *negative* before costs (−0.08%); ~4% is needed to
clear.

On proration: confirmed it does **not** change the break-leg math (a dead
deal reverts to standalone value regardless of election mechanics) but does
mean the completion-scenario deliverable is a blend of cash + REAX-linked
stock (~$13.30–13.60 estimated, not a clean $13.80) — a new REAX-correlated
variance term not priced in Round 1.

Flagged fragility explicitly: at P(complete)=0.85, the trade is negative-EV
at *any* reasonable spread — the position is knife-edge on a probability
estimate with real uncertainty (±0.05), arguing for small size (not zero) IF
the inputs verify.

Restated recommendation: cut size to 1–1.5% NAV (from 2%), raise entry gate
to spread ≥4% to $13.80 (uncapped case) or ≥3.5% to blended consideration
(capped case), net of ~0.6% costs. Entry/exit timing unchanged
(2026-07-14T13:30:00Z entry / 2026-08-17T13:30:00Z exit). Explicit hard gate,
all four required: (1) live quotes confirmed (still failing), (2)
cash-pool cap/proration terms confirmed, (3) RIHI/Poleg voting/support
agreements confirmed, (4) spread clears the revised gate. If any fail:
**no trade**, converging with bear.

---

## Round 3 — Synthesis (neutral, opus)

All three personas converged on the same structural conclusion: this trade
is conditional on verifying data that is currently unavailable (live spread,
cash-pool proration terms, voting/support agreements) — none reached a clean
unconditional "trade now" or "never trade." The synthesizer treated the
broken price feed as a confirmed, not-merely-unchecked blocker, and rendered
the panel's conditional convergence as a decisive **no-trade** for this
session (not a hedge/restatement of ambivalence).

### Hypothesis

- **Statement:** The RMAX/REAX merger is a genuine, board-negotiated,
  single-bidder deal with high vote-passage odds, but it is not a tradeable
  merger-arb setup this session. The bull case rests on a measurable spread
  to the $13.80 cash election that (a) is contingent on unconfirmed
  cash-pool proration mechanics — making the true deliverable a cash +
  REAX-linked-stock blend, not a clean cash floor — and (b) cannot be
  observed because the price feed is confirmed broken. The debate converged
  on P(complete) ≈ 0.89 (±0.05, down from an initial 0.93 once the dual-key
  vote was modeled as a joint probability), with a breakeven spread of ~4%
  net of costs. The edge is unmeasurable, not merely thin.
- **Direction:** no-trade
- **Confidence:** 78 (high conviction in the *no-trade-this-session*
  decision, driven by the hard data blocker — not a confidence rating on
  eventual deal direction)

### Plan

- **Ticker:** RMAX
- **Action:** no-trade
- **Entry:** none this session. Gated on ALL of: (1) a live two-sided RMAX
  quote from a validated feed; (2) observed spread ≥4.0% to $13.80
  (uncapped) or ≥3.5% to blended consideration (~$13.30–13.60 est., capped),
  sustained ≥2 sessions, net of ~0.6% costs; (3) filed RIHI/Poleg
  voting/support agreements; (4) confirmed S-4 cash-pool cap/proration
  formula; (5) ISS and Glass Lewis FOR on both RMAX and REAX proxies with no
  organized opposition; (6) no adjournment/postponement filing and no
  pending appraisal-demand/injunction litigation.
- **Exit (if gates ever clear):** 2026-08-17T13:30:00Z — first valid trading
  session after vote-result disclosure. Aug 14, 2026 is a Friday (valid
  session) but disclosure is expected after close, so the exit rolls
  forward to Monday per the institutional lessons; same-day Aug 14 exit is
  rejected as unrealistic.
- **Expected profit:** 0.0% (flat position this session).

### Dissent (strongest unresolved disagreement — flagged for post-mortem)

Whether the −25% break scenario is symmetric-conservative or optimistic.
Bull argued a failed first vote likely triggers re-solicitation with
sweetened terms — a shallower, less probable left tail — but had no data to
support it. Bear argued the opposite: RMAX's deteriorating standalone
fundamentals (NAR commission-litigation overhang, leverage, shrinking agent
count) mean a break reverts to *below* the pre-deal price, making −25% an
understatement. Quant noted the whole thesis is negative-EV at any
reasonable spread once P(complete) drops to 0.85 — i.e. the trade is
fragile to a ±0.05 swing in a probability estimate that could not be
tightened this session. This question is only observable if the deal
actually fails, so it is not resolved merely by verifying the pre-vote data
gates (spread, proration, support agreements) — it should be tracked as a
lesson candidate if this opportunity is revisited or if the deal breaks.
