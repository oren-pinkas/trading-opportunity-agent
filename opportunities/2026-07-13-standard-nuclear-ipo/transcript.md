# Debate transcript — Standard Nuclear (STDN) IPO

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Event:** Standard Nuclear (TRISO nuclear fuel maker) prices its IPO at USD
  18-21/share, up to USD 3.55-3.7B fully-diluted valuation, ~18.25M shares plus
  a 2.7375M-share greenshoe (~USD 356-383M raise). NYSE debut Wednesday
  2026-07-16, ticker STDN.
- **Strategy:** three-round-panel. **Personas/models:** bull (sonnet), bear
  (sonnet), quant (opus), synthesizer (opus).
- **Price-provider check:** `toa price STDN <ts>` returns a fake
  `stub:deterministic` quote on the default provider; `--provider twelvedata`
  returns an HTTP error / no data (ticker does not exist pre-listing). No real
  STDN price data exists anywhere in the provider as of research time
  (2026-07-14).
- **Verdict:** NO-TRADE. direction=none, confidence=25.

---

## Round 1 — Independent research

### Bull (LONG, gated post-open entry)
- IPO terms: 18.25M shares at USD 18-21, ~USD 356-383M raise, up to USD
  3.55-3.7B fully diluted valuation. [StreetInsider](https://www.streetinsider.com/Corporate+News/Standard+Nuclear+files+for+18.25M+share+IPO+at+$18-$21+per+share/26738322.html); [Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News/120310/Small-modular-reactor-fuel-developer-Standard-Nuclear-sets-terms-for-$356-m); [USNews/Reuters](https://money.usnews.com/investing/news/articles/2026-07-07/nuclear-fuel-firm-standard-nuclear-eyes-up-to-3-55-billion-valuation-in-us-ipo)
- Valuation trajectory: USD 28M 2024 bankruptcy-auction buyout of Ultra Safe
  Nuclear's TRISO line → USD 838M January 2026 private round → up to USD 3.6B
  IPO valuation, a ~4x re-rate in six months. [Value Add VC S-1 breakdown](https://valueaddvc.com/blog/standard-nuclear-s1-ipo-breakdown-valuation-microreactor); [TechFundingNews](https://techfundingnews.com/standard-nuclear-28m-bankruptcy-3-5b-ipo-triso/)
- Bulge-bracket underwriters (BofA, Goldman Sachs, Barclays, UBS); up to USD
  245M contract backlog (USD 65M funded). [Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News/120310/Small-modular-reactor-fuel-developer-Standard-Nuclear-sets-terms-for-$356-m); [Value Add VC](https://valueaddvc.com/blog/standard-nuclear-s1-ipo-breakdown-valuation-microreactor)
- Sector comps bid on AI-power-demand narrative: Centrus Energy (LEU) up
  sharply YTD; Oklo (OKLO) +~700% trailing 12mo; NuScale (SMR) Q2 revenue
  USD 8.1M vs USD 1M prior year. [carboncredits.com](https://carboncredits.com/nuclear-stocks-oklo-nuscale-centrus-energy-rise-as-u-s-pushes-for-military-and-microreactor-expansion/)
- STDN positioned as the only dedicated, privately-funded industrial-scale
  TRISO production line in the US — a fuel-layer position serving any reactor
  developer regardless of whose design wins, differentiating it from
  X-Energy's vertically-integrated reactor+fuel model.
- **Action:** long STDN common (no listed options day 1). Entry NOT at the
  open — wait 30-60min post-first-print on 2026-07-16 (targeting ~10:30-11:00am
  ET) contingent on a confirmed fillable price, per the Lime IPO lesson on
  unreliable day-one minute bars. Exit 3-5 sessions post-debut (~2026-07-21 to
  07-23). Target +15-25% from fill; hard stop below USD 18 (IPO band low).

### Bear (Avoid)
- Pop narrative is fully anticipated: a bulge-bracket syndicate (BofA,
  Goldman, Barclays, UBS, Evercore, RBC, William Blair, Stifel) is built to
  generate a first-day pop by design, not an inefficiency the market missed.
  [BusinessWire](https://www.businesswire.com/news/home/20260706412569/en/Standard-Nuclear-Announces-Launch-of-its-Initial-Public-Offering)
- X-Energy — a *direct* TRISO-fuel competitor via its TRISO-X unit — already
  IPO'd on Nasdaq 2026-04-24 and popped 27% on debut; STDN is the sector's
  second/third mover, not first, so the novelty premium is already spent.
  [MLQ.ai](https://mlq.ai/news/x-energy-shares-surge-27-in-nasdaq-debut-after-upsized-ipo-pricing/); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/x-energy-stock-pops-27-201054076.html)
- Pop-then-fade is the base rate for this cohort: NuScale (SMR) down >22% YTD
  as of May 2026; Oklo (OKLO) declining since its October 2025 peak (~USD
  171.56) despite an intact demand story. [stockanalysis.com](https://stockanalysis.com/stocks/oklo/); [24/7 Wall St](https://247wallst.com/investing/2026/07/10/one-nuclear-energy-stock-with-a-100-upside-potential/)
- USD 3.55B is rich against thin disclosed revenue history; day-1/2 minute-bar
  liquidity is thin on both entry and exit (per the Lime IPO lesson), and
  X-Energy's recent IPO creates a direct supply overhang pulling incremental
  dollars from the same investor base.
- **Stance:** Avoid, or wait 4-6 weeks post-listing to reassess on confirmed
  volume/price data. If any exposure at all, small size, tight stop,
  short-duration momentum trade only — not a valuation-based long.

### Quant (No position — negative EV)
- Broad 2025-26 US IPO first-day pop averages ~27.5%, but that accrues to
  *allocation* holders at the offer price, not to a secondary buyer entering
  post-open. [Yahoo Finance](https://finance.yahoo.com/news/ipo-pops-are-nearing-10-year-highs-and-tech-is-leading-the-way-155742294.html)
- Sector-specific analogues are weaker: Oklo opened ~USD 16.45, closed ~USD
  8.09 on its NYSE debut day (~-50%, multiple volatility halts); NuScale
  opened USD 10.70, closed USD 10.55 (~-1.4%). Both are SPAC de-mergers, not
  bookbuilt IPOs — an imperfect, n=2 comp set, flagged as assumption not fitted
  data. [ipos.fyi Oklo tracker](https://ipos.fyi/tracker/oklo-ipo); [Oklo NYSE debut release](https://oklo.com/newsroom/news-details/2024/Oklo-Inc.-Begins-Trading-on-the-New-York-Stock-Exchange/default.aspx); [Renaissance Capital NuScale profile](https://www.renaissancecapital.com/Profile/SMR/NuScale-Power/IPO); [Motley Fool — nuclear stocks slumped H1 2026](https://www.fool.com/investing/2026/07/08/these-nuclear-energy-stocks-slumped-in-the-first/)
- Price-provider check: `toa price STDN 2026-07-16T13:30Z` → fake
  `stub:deterministic` quote on the default provider; `--provider twelvedata`
  → HTTP error / no data. Confirms no real STDN data exists pre-listing.
- **EV calc (Round 1):** assumed P(up)=0.45 at mean +8%, P(down)=0.55 at mean
  -10% for a secondary post-open entry → gross EV = 0.45(8%) + 0.55(-10%) =
  3.6% - 5.5% = **-1.9%**; minus ~1.5% assumed round-trip slippage/spread on a
  hot small-cap IPO day → **net EV ≈ -3.4%**. Negative EV does not survive
  costs.
- **Stance:** No position / pass. Kelly on negative EV is zero. Hard gate:
  no confirmed listing timestamp exists in the provider yet. Open to being
  moved by the Bull on the base-rate parameters.

---

## Round 2 — Rebuttal

### Bull
- Concedes the data gate: reframes the plan as a **gated order**, not a hard
  timestamp — no fill unless the provider returns a real live post-open print
  with real volume; if data isn't live by market open, no trade is placed
  that day.
- Disputes the Oklo/NuScale reference class: both are SPAC de-mergers with
  structurally different float mechanics (no lockup-aligned insider
  allocation, no underwriter stabilization/greenshoe), which mechanically
  produces more violent air-pockets than a traditional bookbuilt IPO. Argues
  X-Energy — same TRISO niche, same bookbuilt structure, +27% day one and
  held — is the better comp to weight.
- Concedes the Bear's liquidity point: thin day-1/2 minute bars are real
  execution risk on both entry and exit, which is exactly why the plan avoids
  the open.
- **Would drop the trade if:** the confirmed open shows first-print volume
  collapsing below what a USD 356-383M raise implies, or the stock is in
  freefall with no stabilization at the 30-60min checkpoint.
- **Revised action:** long STDN common, entry gated on (1) a confirmed live
  provider quote and (2) price at/above the USD 18 band low with stabilizing
  volume in the 30-60min post-open window on 2026-07-16. No fill if data
  isn't live or price is below USD 18 at checkpoint. Target +15-25% from
  fill, exit by 2026-07-21 to 07-23, stop below USD 18.

### Bear
- STDN's fuel-layer monopoly-adjacent positioning is a multi-year structural
  story; it is irrelevant to a 3-5 session flip, which is what the Bull is
  actually proposing.
- Turns the underwriter-quality argument against the Bull: a prestige
  syndicate (BofA/Goldman/Barclays/UBS) is exactly the signature of a book
  built to pop by design — it raises the odds this is a manufactured
  allocation-holder payday, not organic demand discovery, and does not
  insulate secondary buyers from the Oklo/NuScale pop-then-fade pattern.
- Fully agrees with the Quant: the -3.4% net EV calc is a sharper, falsifiable
  version of the Bear's own "pop-then-fade is the base rate" argument. Finds
  the Quant more convincing than the Bull — the Bull's plan depends on a
  fillable price beating a hard stop within days but offers no EV, only
  narrative; the Quant quantifies the exact entry the Bull proposes and finds
  it negative even before full slippage.
- **Would change mind on:** confirmed provider data showing STDN trading with
  sustained (not day-1-only) volume above pre-IPO comps, a hard multi-year
  offtake contract disclosed (not just backlog), or the first two sessions
  holding flat-to-up unlike Oklo/NuScale.
- **Final stance:** Reaffirm Avoid. No position at IPO or in the first week.

### Quant
- Engages the Bull's "fuel-layer monopoly" argument: this is a claim about
  long-horizon intrinsic value; a 3-5 session hold is not moved by it, and if
  it were, the 4x private re-rate (USD 838M Jan → USD 3.55B IPO) means it is
  already in the print. No probability change from this argument alone.
- **Concedes the Bear's X-Energy comp is a real correction:** X-Energy is a
  bookbuilt IPO (not a SPAC de-merger), same TRISO niche, +27% day one — a
  genuinely better comp than Oklo/NuScale. Two caveats cap the adjustment:
  (a) "+27% day one" is offer-to-close and accrues to allocation holders, so
  a secondary entrant 30-60min post-open captures only a fraction; (b) the
  second/third-mover discount plus the sector's pop-then-fade base rate still
  apply over a multi-day hold.
- **Revised EV:** P(up) 0.45→0.50, up-magnitude +8%→+9%, P(down) 0.50 at
  -10%: gross EV = 0.50(9%) + 0.50(-10%) = **-0.5%**; minus ~1.5% slippage =
  **net EV ≈ -2.0%**. Even a generous 0.55/+10%/-10% case: gross +1.0%, net
  -0.5%. Clearing costs would need P(up) ≥ ~0.58 at +10/-10, which the
  second-mover discount does not support.
- **Concedes the scheduling-gate objection was overstated:** 2026-07-16 is a
  confirmed specific NYSE debut date, not an imprecise window like the Lime
  lesson's "late June/early July" — it IS schedulable via a conditional/gated
  entry rule. The only remaining blocker is that no fillable minute-bar
  exists until the stock actually lists — a timing fact, not a permanent bar.
- **Final stance:** Pass / no position, now on EV grounds rather than
  scheduling grounds. Best case net EV ~-0.5%, base case ~-2.0% — still
  negative after costs. Moveable only if the Bull produces evidence pushing
  P(up) to ~0.58+ (e.g. X-Energy's day 2-5 path holding, not fading).

---

## Round 3 — Synthesis (NO-TRADE, confidence 25)

**Hypothesis:** STDN's NYSE debut is a well-anticipated, syndicate-engineered
IPO pop whose day-one gains accrue to allocation holders, not to a secondary
buyer entering 30-60 minutes post-open. After correcting the comp set to
X-Energy, every quantified entry path for a 3-5 session secondary hold still
carries negative expected value once slippage is included (best case ~-0.5%
net, base case ~-2.0% net).

**Plan:** STDN, no-trade. (If revisited: entry-checkpoint 2026-07-16T14:00:00Z,
exit-checkpoint 2026-07-23T19:30:00Z.) expected_profit_pct = 0.

**Dissent:** Which reference class governs a secondary post-open entry. The
Bull treats X-Energy (+27% day one, held, bookbuilt, same TRISO niche) as
evidence a gated long can still capture upside; the Quant concedes X-Energy
improves the comp set yet holds that the offer-to-close pop accrues to
allocation holders while the second/third-mover discount and the pop-then-fade
base rate (NuScale, Oklo) still drag a multi-day secondary hold negative.
Testable post-mortem: does X-Energy's day 2-5 path hold or fade, and does a
real fillable STDN minute-bar even exist in the window the Bull proposed.

**Rationale:** All three personas converged on caution: the Bear reaffirmed
Avoid, the Quant held Pass on EV grounds (best case ~-0.5%, base case ~-2.0%,
both negative after ~1.5% assumed slippage), and even the Bull's Round 2
position had degraded from a confident directional call into a heavily gated
conditional order he himself agreed to abandon on weak volume or price below
USD 18. The decisive input is the Quant's EV math, which the Bear explicitly
endorsed as a sharper version of his own thesis and which the Bull never
rebutted with numbers — the Bull offered narrative (monopoly-adjacent TRISO
position) that the Bear correctly flagged as a multi-year story irrelevant to
a 3-5 session flip. With no real STDN price data existing pre-listing and
two of three seats recommending pass, no-trade is the defensible synthesis.
