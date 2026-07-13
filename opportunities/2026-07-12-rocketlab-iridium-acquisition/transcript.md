# Research Debate Transcript — 2026-07-12-rocketlab-iridium-acquisition

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel` (bull/bear/quant, bull+bear on sonnet, quant+synthesizer on
opus). Run 2026-07-13T08:25:02Z, single opportunity in scope.

## Event

Rocket Lab (RKLB) agreed to acquire Iridium Communications (IRDM) for $54/share ($27 cash
+ $27 in RKLB stock, nominal), ~$8B enterprise value. Deal requires Iridium shareholder
approval and regulatory approval (likely CFIUS/FCC given the satellite/defense angle), and
must close by 2027-06-28. Announced Sunday 2026-07-12T13:03:15Z, ahead of Monday's open.

Source: "Rocket Lab to Acquire Iridium in Historic Deal" — Rocket Lab investor news
release, https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully
(accessed 2026-07-12T13:03:15Z)

## Verified market data

- IRDM close Fri 2026-07-10T19:59:00Z: **$50.075** — source: `https://api.twelvedata.com/time_series?symbol=IRDM&interval=1min&date=2026-07-10&timezone=UTC`
- RKLB close Fri 2026-07-10T19:59:00Z: **$80.93** — source: `https://api.twelvedata.com/time_series?symbol=RKLB&interval=1min&date=2026-07-10&timezone=UTC`
- No Monday (2026-07-13) intraday print exists yet as of synthesis time (2026-07-13T08:25:02Z, pre-market-open) — confirmed via `toa price IRDM/RKLB 2026-07-13T* --provider twelvedata`, which returned `MarketDataUnavailable` (HTTP 400) for all queried minutes, consistent with the market not yet having opened.
- Implied spread: ($54 − $50.075) / $50.075 ≈ **7.8%** over the last clean pre-announcement close.

## Institutional lessons injected

1. Before finalizing any plan, validate that every entry and exit timestamp falls within an
   open trading session (not a weekend or exchange holiday) for the specific instrument,
   and roll non-trading exit dates forward to the next open session.
   (source: `2026-07-08-caesars-icahn-fertitta-bidding-war`)
2. Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines) directly
   onto an execution timestamp — treat such dates as catalysts and derive the fill time
   from the nearest valid trading session. (source: `2026-07-08-caesars-icahn-fertitta-bidding-war`)

---

## Round 1 — Independent research

### Bull (sonnet)

Clean, catalyst-confirmed re-rating event on both sides of the tape. The Sunday
announcement timing (ahead of Monday's open) signals management wanted a full trading day
of price discovery — read as bullish. Market has not yet priced this (no Monday print).
IRDM's $50.075 close vs. $54 deal price is a real, quantifiable 7.8% arb spread the market
must close as the deal de-risks. RKLB's stock consideration ($27 of the $54) means good
RKLB sentiment tightens the spread further — self-reinforcing. CFIUS/FCC regulatory
overhang is real but a medium-term tail risk, not a reason to skip the immediate open-day
pop; first-day reaction to large strategic deals is historically the sharpest move, before
deal-risk discounting sets in.

**Proposed action:**
- Primary: long IRDM, entry `2026-07-13T13:35:00Z` (5min after open), exit
  `2026-07-13T19:55:00Z` (same session) — capture the initial catalyst repricing without
  holding into multi-month regulatory uncertainty.
- Secondary momentum sleeve: long RKLB, entry `2026-07-13T13:35:00Z`, exit
  `2026-07-14T19:55:00Z` (next session close) — rides the "integrated space and defense
  platform" narrative re-rating independent of deal completion.
- Both timestamps fall on valid weekday sessions; explicitly does NOT use the 2027-06-28
  deadline as an execution timestamp.

### Bear (sonnet)

A $54 headline vs. IRDM's $50.075 close is only ~7.8% — unusually **low** for strategic
M&A (typical premiums run 20-40%). Either the board caved under pressure/conflicts
(underpriced, could draw a topping bid) or the market already suspects the $27 stock leg
is soft (RKLB is volatile/speculative-growth-priced, so "$27 in RKLB stock" is a moving
target, not fixed) — a low headline premium paired with a stock-for-stock component is a
classic setup for deal-value erosion between signing and close.

**Risks:** (1) RKLB dilution/financing risk — $8B EV is large relative to RKLB's own scale
(unconfirmed here, flagged as an open question). (2) Regulatory risk — satellite+defense
combination is a novel CFIUS/FCC fact pattern with no clean precedent; timeline/outcome
genuinely uncertain. (3) Duration risk — ~11.5 months to close means deal-break risk
compounds over time. (4) Stock-component exposure — IRDM holders are implicitly long
RKLB's own volatility, not just deal completion.

**What would change my mind:** confirmation the true premium is higher once the RKLB leg
is marked at signing-date value; a strong orderly IRDM rally toward $54 on Monday's open
with no RKLB gap-down; early positive regulatory signals.

**Proposed action:** would NOT take an outright long IRDM. Merger-arb pairs trade instead
— long IRDM / short RKLB in the ~$27:$27 stock ratio — entering only after observing the
actual Monday reaction: `2026-07-13T13:30:00Z` (NYSE open, first valid post-announcement
session) for both legs. Exit contingent on deal resolution, not the legal deadline; if held
to the outside date, roll to the nearest valid session at or before the deadline, not the
deadline itself.

### Quant (opus)

Base-rate priors (general merger-arb, not fabricated precedent): announced strategic deals
typically complete ~85-90%; haircut for CFIUS/FCC-adjacent review overhang →
**P(complete)=0.83, P(break)=0.17**. Timing prior: right-skewed distribution centered
8-11 months toward the 2027-06-28 (~11.5mo) deadline.

**EV calculation** (unhedged long IRDM): assumed first tradeable fill $51.50 (between
Friday's $50.075 and the $54 deal value, since no post-announcement print exists yet).
Complete → $54 (+$2.50/+4.85%). Break → assumed $44 (−$7.50/−14.56%, breaks typically
overshoot down). EV = 0.83(+4.85%) + 0.17(−14.56%) = **+1.55% gross**, ~+1.4% net of
slippage. Asymmetric: +4.9% upside / −14.6% downside — "size down, not size up."

**Critical unknown:** is "$27 in RKLB stock" a fixed-dollar value (share count floats,
deal value locked at $54) or a fixed exchange ratio (~0.334 RKLB/IRDM at signing, deal
value floats with RKLB)? This single fact flips whether/how to hedge. Will not commit a
RKLB short until confirmed — under fixed-ratio, hedging costs ~1-3%/yr borrow
(~$0.30-0.70/share), roughly halving net EV.

**Proposed action:** modest long IRDM, unhedged pending exchange-ratio confirmation.
Size: cap break-scenario loss at ~0.4% of book → 0.4%/14.6% ≈ 2.7%, round to **3% of
paper book**. Entry `2026-07-13T14:00:00Z` (30min after open, let gap settle). Exit:
profit-take limit at IRDM ≥$53.50, or time-stop rolled back from 2027-06-28 to the prior
valid session, **2027-06-25T14:00:00Z** — never treating the deadline itself as a fill.

---

## Round 2 — Rebuttal

### Bull rebuttal

Bear and quant both anchor on deal-completion risk, but that's the wrong frame for the
RKLB leg — it's a standalone re-rating bet that pays off on Monday's narrative reaction
regardless of whether the deal closes in 2027. **Concedes:** the 7.8% premium is a
legitimate quality flag for the IRDM arb leg specifically, and the exchange-ratio unknown
genuinely gates any hedge (won't hedge until confirmed) — Round 1 sizing was
underspecified there. **Pushes back on quant:** "size down" is right for an 11.5-month
arb sleeve but doesn't transfer to a same-day momentum trade with a hard time-stop
(19:55Z same session) — conflates two different risk profiles under one number.

**What would change my mind:** if Monday's open shows IRDM gapping toward $54 with RKLB
flat/down (no dilution punishment priced in), thesis holds. If RKLB gaps down hard
alongside only partial IRDM repricing, that's evidence the market is pricing dilution/
regulatory doubt into both legs at once — would cut IRDM long size and drop the standalone
RKLB long, converging toward bear's arb structure.

**Revised:** keep RKLB momentum long as designed; resize the outright IRDM long down
modestly pending Monday's actual print; ready to convert to quant's hedged structure once
the exchange mechanism is confirmed.

### Bear rebuttal

**On bull's RKLB thesis:** has the sign risk backwards or at least unexamined — large
stock-funded acquisitions routinely see acquirer weakness on announcement (dilution
overhang, integration risk, "why only 7.8% premium if confident" skepticism). Doesn't
assert RKLB *must* sell off (dilution mechanics unconfirmed), but treating the
announcement as a clean bullish catalyst decoupled from deal-completion risk is the weaker
prior — a coin-flip with a plausible left tail, not a momentum layup. Bull's RKLB sleeve
is the least-supported leg of either Round 1 position.

**On quant's EV math:** 0.83/0.17 is reasonable for a friendly deal in isolation, but
doesn't fully price novel CFIUS/FCC exposure with no clean precedent and the 11.5-month
runway. Would nudge break odds up (not wildly); $44 as the sole break-price likely
undersells the tail given forced-seller dynamics in a late regulatory block. The fat left
tail doesn't just vindicate caution, it likely understates it.

**Concession:** quant's positive-EV framework is the right lens, and a small, hedged
position is defensible where an outright unhedged long is not — a properly-sized pairs
trade captures the spread while netting out the acquirer-stock uncertainty bear is most
worried about, a genuine improvement over either Round 1 framing alone.

**Revised:** go along with a pairs trade, smaller than quant's 3%, gated strictly on
Monday's actual print and confirmed exchange mechanics — no entry before 14:00Z, no RKLB
short sized until stock-leg terms verified; exit immediately if regulatory commentary
breaks negative intraday.

### Quant rebuttal

**Stress-test vs. bear:** from fill $51.50 — complete → +4.85%, break → −14.56%.
At P(complete)=0.70: EV = 0.70(4.85) + 0.30(−14.56) = **−0.97%** (negative before costs).
Break-even P(complete) = 14.56/19.41 = **0.750**. But bear conflates *takeover premium*
with *deal spread* — the clean signal is the 7.8% spread over 11.5mo (~8.4% annualized),
which is not distressed-wide (broken/contested deals trade 15-30%+); the low headline
premium plausibly reflects IRDM's pre-announcement run-up, not board fragility. Haircuts
prior for regulatory novelty to **P(complete)=0.80** (not 0.70) → fair value = 0.80(54) +
0.20(44) = **$52.00**; positive EV requires fill <$52.

**On bull's RKLB leg:** zero deal-arb content — no $54 anchor, no convergence, pure
directional beta on a high-vol name, arguably wrong-signed (acquirers often fall on
announcement). Tell: bear wants to short the exact leg bull wants to long — not one
opportunity, two uncorrelated bets smuggled under one label. Does not price it as arb,
does not take it.

**On bear's pairs trade:** only coherent under fixed-ratio exchange (unconfirmed under
fixed-dollar, a RKLB short is a naked short, not a hedge). Even under fixed-ratio: on a
deal break, IRDM falls to $44 (long loses) while RKLB typically bounces on relief (short
also loses) — the hedge is wrong-way exactly when needed. Borrow cost ≈1% drag on the
position. Bear's escape (dilution re-rates RKLB down, improving hedged EV) requires
committing to a RKLB-down directional view — opposite bull, and itself just a directional
bet. Hedge doesn't clearly improve EV; it swaps deal-break asymmetry for RKLB-beta risk.

**Revised recommendation:** small **unhedged** long only. Enter only if Monday's actual
13:30Z print is ≤$51.50 (stand down if IRDM opens ≥$52 — spread too thin, EV negative).
Size cut to **1.5% of paper book** (from 3%, given the thinner margin at P=0.80). Entry
`2026-07-13T14:00:00Z`, profit-take limit $53.50, time-stop `2027-06-25` (rolled off the
legal deadline).

---

## Round 3 — Synthesis (opus, neutral)

The panel converged more than the three-round structure suggests: all three agree the
7.8% spread is a genuine deal-quality flag, the exchange mechanism is unconfirmed and
gates any hedge, and no position should open before Monday's actual print.

**RKLB momentum leg — cut.** Zero deal-arb content (no $54 convergence anchor), pure
directional beta on a high-vol name, plausibly wrong-signed (stock-funded acquirers often
sell off on dilution overhang). Bear independently reached the same sign concern, wanting
to *short* exactly what bull wanted to *long* — when bull and bear want opposite sides of
the "same" leg, it's not one priced opportunity, it's an unpriced coin-flip. Does not
survive synthesis.

**Bear's hedged pairs trade — declined.** Break-cyclicality problem: on a deal break,
IRDM falls *and* RKLB typically bounces on relief, so the pair loses on both legs exactly
when the hedge is needed, while paying ~1% borrow drag. Only even coherent under an
unconfirmed fixed-ratio mechanism. Not a hedge worth paying for.

**Adopted: quant's small unhedged long**, with an independent synthesizer caution — the
edge is thin and fragile. EV goes negative below P(complete)=0.75; fair value is $52.00;
the entire trade rests on getting filled below $52 and on the 0.80 completion estimate
holding against genuine CFIUS/FCC novelty. Positive-but-slim EV must be sized as such and
abandoned if Monday opens rich.

Institutional lessons respected: entry `2026-07-13T14:00:00Z` is a valid Monday session;
the time-stop rolls the 2027-06-28 legal deadline back to the nearest valid trading
session (`2027-06-25`), never using the deadline itself as an execution timestamp.

### Final structured output

**hypothesis**
- statement: IRDM trades below the $54 deal terms on a completion probability (~0.80)
  high enough for a small unhedged long to carry modestly positive EV, but only if
  entered below fair value (~$52) on Monday's actual print; the RKLB narrative-re-rating
  leg and the long/short pairs hedge both fail to add priceable edge and are rejected.
- direction: long
- confidence: 60

**plan**
- ticker: IRDM
- action: buy
- entry: { time: `2026-07-13T14:00:00Z`, target_price: `51.50` } — conditional gate: only
  if Monday's 13:30Z print is ≤$51.50; stand down entirely if IRDM opens ≥$52.00.
- exit: { time: `2027-06-25T19:55:00Z`, target_price: `53.50` } — profit-take limit at
  $53.50, otherwise time-stop at this session (rolled back from the 2027-06-28 legal
  deadline to the nearest valid trading session); exit immediately intraday on negative
  CFIUS/FCC headlines.
- expected_profit_pct: 1.2

**dissent (preserved, unresolved)**

Is the true left tail correctly priced? Bear maintains CFIUS/FCC novelty (no clean
satellite-defense precedent) plus ~11.5-month duration means quant's P(break)=0.20 and
$44 break-price understate the real downside, pushing the trade toward or below its own
P(complete)=0.75 break-even. Quant holds that an 8.4%-annualized spread is not
distressed-wide (broken deals trade 15-30%+), so only a modest haircut (0.83→0.80) is
warranted. Preserved unresolved for the post-mortem: if the deal breaks, test whether
completion probability was miscalibrated for regulatory-novel deals, not whether the
trade structure itself was wrong.
