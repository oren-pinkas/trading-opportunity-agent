# Research debate transcript — 2026-07-12-jersey-mikes-ipo

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` (three independent personas, three rounds).
Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
Run at: 2026-07-12T22:55:42Z (current UTC time at debate start; today's date 2026-07-12).

Scope note: this debate considers **only** the Jersey Mike's IPO opportunity
(2026-07-12-jersey-mikes-ipo). No other opportunity, dossier, or transcript was
consulted in forming this hypothesis.

Institutional lessons injected (via `toa lessons-relevant --type ipo --tickers JMKE`):
- For IPO plans, don't hard-code entry to the raw listing-day open minute: day-one
  minute-bar coverage is unreliable; delay entry to a liquid window (30-60min after
  first print) or probe for a fillable bar before scheduling both legs. (source:
  2026-07-07-lime-ipo)
- Never convert an imprecise listing window ("late June/early July") into a single
  exact timestamp; gate IPO opportunities on a confirmed exchange listing date/time
  verified present in the price provider. (source: 2026-07-07-lime-ipo)

---

## Round 1 — Independent research

### BULL (Catalyst-hunter, sonnet)

This is a pre-listing catalyst chain, not a single-day event yet: (1) S-1 filed
2026-07-02 generating a wave of financial-media coverage; (2) roadshow/book-building
over the next 2-6 weeks with a deep bulge-bracket syndicate (Morgan Stanley, Jefferies,
J.P. Morgan as coordinators, plus Barclays, Guggenheim, Goldman Sachs, BofA Securities,
Wells Fargo) signaling strong anticipated institutional demand; (3) pricing/listing day
as the real tradeable catalyst.

Valuation & deal size: seeking at least $12B valuation and raising >$1B, per CNBC/Eastern
Herald/EBC Financial Group coverage. Blackstone bought its majority stake at ~$8B in 2024
— a ~50% markup in under two years signals genuine demand belief, not a fire-sale exit.

Financials: FY2025 revenue $724M (+11% YoY), net income $55M (up from $5M), adj. EBITDA
~$327M at ~47% margin, systemwide sales ~$4.2-4.3B across ~3,300 locations (+13% YoY),
cumulative same-store-sales growth 50% (2020-2025). Growth pipeline: 1,600+ additional
U.S. stores in development, a 400-store UK/Ireland agreement, Canada expansion.

Comps: CAVA (June 2023) priced $22, closed +99% day one; Dutch Bros (Sept 2021) priced
above range, +70% debut. Both are the closest structural analogs (high-margin,
high-growth, PE/founder-backed franchise/hybrid concepts) and show underwriters
recently underpricing restaurant IPOs relative to first-day demand.

Sequencing problem acknowledged explicitly: JMKE not tradeable today; typical
S-1-to-listing lag is 4-8 weeks; will not hard-code entry to the 2026-08-15 dossier
impact_window estimate, will gate on confirmed listing date in the price provider.

Proposed (R1): long JMKE common equity (no options pre-listing), entry 30-60 min
after first print on confirmed listing day (per institutional lesson, not the raw open
minute), exit within first 1-3 trading days to capture the pop before drift/lockup
dynamics. Expected magnitude: 30-80% first-day pop off IPO price, sizing for a realistic
20-40% base case.

Sources: CNBC (2026-07-02), MLQ News, EBC Financial Group, Eastern Herald, PitchBook,
The Deep Dive, Forbes (CAVA), CNBC (CAVA debut).

### BEAR (Skeptic, sonnet)

No tradeable security exists — the S-1 (filed 2026-07-02) is a registration statement,
not a listing; price range, listing date, and offering size are unfinalized. The
company had already confidentially filed back in April 2026 (CNBC, 2026-04-20) — three
months before the public S-1 — indicating the timeline has already slipped once. The
public narrative (47% EBITDA margin, cumulative SSS growth, $12B target) is now fully
consensus with zero remaining informational edge.

Recent comparable QSR/fast-casual IPO aftermarket base rates are poor: CAVA "dropped
50% during 2025" after its 2023 debut; Sweetgreen "collapsed by 80% in 2025"
(Restaurant Business Online). The broader restaurant IPO pipeline is thin (Panera
repeatedly delayed).

This is a textbook PE-sponsor cash-out/dividend-recap IPO, not a growth-funding IPO:
Blackstone bought at ~$8B in 2024, targeting $10-12B now (a 25-50%+ sponsor markup);
the company raised $760M via a whole-business securitization earlier in 2026, partly
funding a dividend to Blackstone (IFR); carries $2.1B long-term debt against just
$232M cash (as of 2026-03-29); IPO proceeds are used in part to pay down that same
debt. Founder-adjacent related-party payments flagged per Forbes (stepson ~$50.5M
2023-2025; aircraft transfer ~$41M).

Blackstone retains majority voting control post-IPO as a "controlled company" under
NYSE rules — no independent board majority requirement, a structural multi-year
overhang, not a one-time lockup blip.

Growth is already decelerating going into the print: same-store sales 2.3% most
recent period, down from 3.6% prior year, disclosed in the S-1 itself. Macro IPO
tailwind is concentrated in AI/digital-infra mega-deals, not consumer/restaurant;
rate-cut expectations have deteriorated; tariff policy uncertainty is a live risk to
market windows generally.

Biggest risk named: pricing disappointment/valuation gap at print as institutional
buyers price in the leverage and decelerating growth even if retail narrative ignores
it — the deal prices below range or opens flat-to-down, mirroring CAVA/Sweetgreen's
eventual multi-year fades. Would not initiate a bullish position today; challenges the
bull to explain why JMKE escapes the Cava/Sweetgreen pattern.

Sources: SEC EDGAR S-1, Eastern Herald, MLQ News, Forbes (Jim Osman), IFR, PitchBook,
AccessIPOs, EBC Financial Group, CNBC (2026-04-20, 2026-07-02), Restaurant Business
Online (x2), Foley & Lardner 2026 IPO Market Outlook, ScienceDirect (IPO lockup
literature).

### QUANT (Pragmatist, opus)

Nothing tradeable right now: no JMKE ticker, no price, no share count, no confirmed
listing date; S-1 price range and share count are still blank; the $100M raise figure
is the customary SEC placeholder, not the real deal size. Will not schedule any leg
until a confirmed exchange listing date/time is verified in the price provider; the
dossier's 2026-08-15 impact estimate is unschedulable.

Base rates: CAVA priced $22, opened ~$42, closed +99% day one; Sweetgreen priced $28,
opened $52, closed +76% day one then de-rated hard over the following two years;
Smith Douglas (non-restaurant control) only +12-15% day one as the "boring" outcome
absent hype.

Decisive point: the day-1 pop accrues to *allocated* investors at the IPO price;
retail/systematic accounts cannot get allocation on a hot Blackstone-led syndicate
deal — the first fillable print is the opening auction, i.e. after the pop already
happened. Cites Ritter's long-run IPO data: buyers at first-day close underperform
size-matched peers by ~29% over 3 years, ~2.1% annual underperformance persisting
through 2025, concentrated in exactly this kind of post-pop entry. Lockups (90-180
days) add forced-supply overhang later.

Explicit EV for the only fillable leg (buy first liquid print at listing, exit day-1
close): P(up) ≈ 0.43, win magnitude +4%, loss magnitude -5%, round-trip slippage 1.5%
→ EV = (0.43×4%) + (0.57×-5%) - 1.5% = 1.72% - 2.85% - 1.5% = **-2.63%** per unit
risked. Hold-through to +90 days also modeled negative given lockup overhang and
Ritter's documented post-listing underperformance.

Recommendation: position size **zero**, no trade today, hold/monitor. Trigger to
revisit: amended S-1/424B with a real price range AND a confirmed NYSE listing
date/time verifiable in the price provider — realistically 1-2 weeks pre-listing.

Sources: MLQ News, CNBC, StreetInsider (headline), Forbes/CNBC (CAVA), Yahoo/Reuters
(Sweetgreen), IPOScoop (Smith Douglas), Ritter (UFL long-run IPO returns), Nasdaq,
Uppsala lockup study.

---

## Round 2 — Rebuttal

### BULL rebuttal

Concedes: (1) the leverage/dividend-recap story is real, not hand-waved away; (2)
same-store-sales deceleration (3.6% → 2.3%) is a real yellow flag, a thinner reed
than credited in Round 1; (3) controlled-company status and 90-180 day lockups are
real structural overhangs, but on a months-to-years timescale — consistent with (not
a rebuttal to) a fast in-and-out trade.

Distinguishes offer-to-close ("the pop," CAVA +99%/Sweetgreen +76%) from
close-to-multi-year ("the fade," Bear's 50%/80% drawdown evidence) as different
return distributions — argues the fade evidence doesn't refute the pop's existence,
only argues against a long-term hold, which wasn't proposed.

Key concession: ran open-to-close arithmetic on his own cited comps — CAVA opened
~$42, closed $43.78 (+4.2%); Sweetgreen opened ~$52, closed $49.28 (-5.2%) — matching
the Quant's assumed +4%/-5% magnitudes almost exactly, independently derived. States
plainly: "I was implicitly pricing the wrong leg of the trade" — the big pop accrues
to allocated investors before anyone here can trade it; the retail-accessible
open-to-close slice is a coin flip on this n=2 sample and net negative after 1.5%
slippage. No data-backed rebuttal to Quant's P(up)=0.43 — only an unproven hypothesis
that a "hot syndicate + big first print" might shift the conditional probability
higher, stated explicitly as a hypothesis, not an edge.

Revised proposal: drops the 20-40% sizing and 1-3 day hold entirely. New proposal —
no pre-committed size today; same precondition as Bear/Quant (confirmed listing
date/time + real price range); if met, only enter if the first liquid print shows a
"hot-deal" pop signature (not Smith-Douglas-like); size small (low single-digit % of
risk capital); exit at day-1 close only; hard stop-loss at -3% intraday.

### BEAR rebuttal

Underwriter syndicate depth is not a demand signal — it reflects sponsor ability to
pay full underwriting economics and prior relationships; CAVA and Sweetgreen also had
credible syndicates and both cratered (50%/80%) within about a year, so syndicate
depth doesn't predict durable value. The 47% EBITDA margin is a capital-structure
artifact of the franchise/securitization model, not a rebuttal to the disclosed SSS
deceleration, which Bull's Round 1 case never addressed. Growth-pipeline size is a
sales document, not a track record — CAVA/Sweetgreen/Portillo's all led with
aggressive whitespace pipelines and still got re-rated down once SSS softened.

Key point: the Quant's negative EV for the only fillable (non-allocated) entry is an
*independent* reason to hold at zero, additive to the Bear's fundamental/leverage
case — even if the leverage/related-party/deceleration concerns are overstated, the
retail entry point still loses money mechanically because allocated buyers capture
the pop before the tape opens to non-allocated accounts.

What would change Bear's mind: pricing at a discount reflecting the SSS deceleration
(a disciplined-pricing signal), real (not partial) debt paydown in use-of-proceeds, a
reversing SSS print pre-pricing, or credible allocation access flipping the EV calc.

### QUANT rebuttal

Notes Bull and Bear cite the *same* two comps (CAVA, Sweetgreen) for opposite
conclusions because the day-1 print and the 12-month path are different return
distributions — Bull prices the first, Bear prices the second, Quant can only trade
whichever is fillable.

On Bull's upside: survives qualitatively, fails quantitatively — the cited 30-80% pop
is offer-to-close, inaccessible to a post-open entry; the only fillable leg is
open-to-close residual momentum, which is exactly the already-negative EV (-2.63%),
unchanged by anything Bull said. Reinterprets underwriter syndicate size as a
distribution-capacity/fee-pool signal, arguably supporting "the deal is being sold to
you" rather than "rationed away from you." Considers and rejects "buy the post-lockup
dip" as an alternative expression of upside — that is precisely when the CAVA/Sweetgreen
fades happened, into a decelerating-SSS, high-leverage story, so it's not a value
entry and is likely worse EV, not better.

On Bear: the leverage/dividend-recap/decelerating-SSS profile doesn't change the
intraday open-to-close trade (flow/momentum dominated) but does lower P(up) and fatten
the left tail for any multi-day/post-lockup hold — reinforces that hold-through is
negative EV and explains the mechanism (refinancing/repricing risk into a
deteriorating rate-cut tape). Explicitly declines to let Bear's fundamentals justify
shorting the open or buying puts — no borrow, no options chain pre-listing; leverage
is a why-it-fades-later story, not a why-it-opens-down story.

Revised: intraday EV unchanged (~-2.63%); multi-day EV revised more negative.
Recommendation unchanged: zero position, monitor only. Two triggers to revisit: (1) a
confirmed listing date/time plus a real range, enabling an actual open-to-close
conditional distribution calc; (2) a deal priced *below* the $10-12B target (a
"broken"/discounted IPO) — the one scenario where Bear's fundamentals are already
priced in and a fillable long could flip positive EV.

---

## Round 3 — Synthesis (neutral synthesizer, opus)

**Hypothesis:** JMKE is not yet a tradeable security — no confirmed price range,
share count, or exchange listing date/time exists. The debate resolved that the
well-documented IPO "pop" accrues to allocated investors, inaccessible to a
retail/systematic account on a hot Blackstone deal. The only fillable leg (buy the
first liquid print at listing, exit day-1 close) is negative EV, independently
confirmed by the Quant's model (~-2.63%) and the Bull's own comp arithmetic. Any
multi-day or post-lockup hold is worse once leverage, the dividend-recap structure,
controlled-company overhang, and decelerating same-store sales are priced in.
Direction: none (no actionable trade today). Confidence in "no action is currently
correct": 78/100.

**Plan:** No position today. Gate any future leg on (1) an amended S-1/424B with a
real price range and share count, (2) a confirmed NYSE listing date/time verified in
the price provider, (3) an observed liquid opening print showing a "hot-deal" pop
signature. If triggered: small (low single-digit %) conditional long, entered after
the opening auction clears (not at/before open — the standard "wait 30-60 min"
lesson is superseded here by the stricter conclusion that the pop is already gone by
the time a retail account can fill), exit at day-1 close only, hard -3% intraday
stop. The one scenario that flips EV positive: a deal priced *below* the $10-12B
target.

**Confidence: 78/100** on the recommendation to hold at zero today. High because all
three personas converged, and because the Bull's own independently-derived
open-to-close arithmetic reproduced the Quant's negative EV almost exactly — when the
sole advocate's own numbers refute his own tradeable expression, "no trade today" is
unusually well supported. Not higher, because the Bull did not fully capitulate to
zero — he preserved a small gated conditional long backed by an explicitly unproven
hypothesis (hot syndicate + big first print shifting P(up) above 0.43 on an n=2
sample), so real, non-cosmetic disagreement remains about the *conditional future*
trade.

**Dissent (gold for post-mortem):** Does a "hot-deal" opening signature (large first
print + deep bulge-bracket syndicate) raise the retail-accessible open-to-close P(up)
above the ~0.43 base rate enough to flip EV positive (Bull's unproven hypothesis), or
is a hot open itself the marker of maximum overpricing (Quant/Bear's view, whose only
EV-flipping path is a deal priced *below* target instead)? Falsifiable only once
JMKE actually lists — flagged explicitly for the post-mortem process.
