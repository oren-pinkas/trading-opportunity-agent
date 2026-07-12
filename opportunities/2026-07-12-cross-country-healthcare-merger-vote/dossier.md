---
id: 2026-07-12-cross-country-healthcare-merger-vote
title: Cross Country Healthcare shareholder vote on merger set for July 16
status: researched
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: CCRN holders vote July 16, 2026 on proposed merger with KL Criss Cross
    entities.
  impact_window: '2026-07-16'
tickers:
- CCRN
sources:
- title: Cross Country Healthcare schedules July 16 shareholder vote on merger (TradingView)
  url: https://www.tradingview.com/news/tradingview:2f045e748baf3:0-cross-country-healthcare-schedules-july-16-shareholder-vote-on-merger-supplemental-proxy-disclosures/
  accessed_at: '2026-07-12T13:03:15Z'
- title: Cross Country Healthcare to be Acquired by Knox Lane in All-Cash Transaction
    Valued at $437 Million (BusinessWire)
  url: https://www.businesswire.com/news/home/20260506144806/en/Cross-Country-Healthcare-to-be-Acquired-by-Knox-Lane-in-All-Cash-Transaction-Valued-at-$437-Million
  accessed_at: '2026-07-12T19:06:00Z'
- title: Cross Country Healthcare merger moves forward as antitrust waiting period
    ends (Investing.com)
  url: https://www.investing.com/news/sec-filings/cross-country-healthcare-merger-moves-forward-as-antitrust-waiting-period-ends-93CH-4755587
  accessed_at: '2026-07-12T19:06:00Z'
- title: DEFM14A - Cross Country Healthcare, Inc. merger proxy statement (StockTitan/SEC)
  url: https://www.stocktitan.net/sec-filings/CCRN/defm14a-cross-country-healthcare-inc-merger-proxy-statement-08b83df3a680.html
  accessed_at: '2026-07-12T19:06:00Z'
- title: CCRN current quote reference (chartmill)
  url: https://www.chartmill.com/stock/quote/CCRN/profile
  accessed_at: '2026-07-12T19:06:00Z'
hypothesis:
  statement: CCRN trades at a ~0.53% discount ($13.18 vs $13.25 fixed cash deal
    price) on a near-certain, HSR-cleared, board-unanimous PE take-private (Knox
    Lane) heading into the July 16 vote. Residual upside is capped at $0.07/share
    (~2-3% annualized to a Q3 2026 close), which fails an 8-10% annualized hurdle
    by 3-4x, while the break-tail loss is ~$2.9/share down to an estimated
    unaffected price of $9.50-10.50. Risk/reward is roughly 59:1 against; the
    break-even approval probability (~97-98%) sits at or above the defensible
    estimate (90-97%). No exploitable edge for a paper-trading agent reacting to
    already-public vote-date news.
  direction: no_trade
  confidence: 88
plan:
  ticker: CCRN
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: Whether the residual spread is efficiently priced or hides an
    information gap, hinging on two unverified inputs. (1) The ISS/Glass Lewis
    proxy-advisor recommendation is unknown and unresolved, lands before the
    July 16 vote, and is the one realistic catalyst that could move votes, since
    "priced too low" is exactly the substance behind the Malone/Walsh disclosure
    suits. (2) The market price M itself ($13.18-13.19) is single-persona-sourced
    and not cross-checked, in an environment where live feeds proved unreliable
    (the internal toa price stub swung $26.06 to $103.03 to $396.51; a separate
    live-quote fetch returned an implausible $9.48 x $16.89 book). Quant flagged
    that a materially wider spread (M at $12.60-12.85) would signal the market
    knows something this debate doesn't and would flip the call from "no edge"
    to "re-investigate." Post-mortem should check the actual close outcome and
    whether M was ever truly $13.18.
  last_updated: '2026-07-12T19:09:00Z'
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-12T19:09:00Z — NO-TRADE

Three-round panel debate (bull/bear sonnet, quant/synthesizer opus). All three
personas converged on no-trade, moving from an epistemic disagreement in Round 1
to a quantified consensus in Round 2.

- **Bull → Bear → Quant convergence:** Bull and bear independently verified via
  web search that this is a signed, board-approved, all-cash Knox Lane take-private
  at $13.25/share (~$437M equity value), HSR antitrust clearance obtained
  2026-06-22, board unanimous "FOR," and that "supplemental proxy disclosures" is
  routine disclosure-only strike-suit litigation (Malone/Walsh actions) — boilerplate,
  not deal risk. Bear additionally sourced the real current CCRN price at
  ~$13.18-13.19, a ~0.53% discount to deal price. Quant, lacking search tools in
  Round 1, had abstained on epistemic grounds (EV undefined); given the corroborated
  D and M in Round 2, quant computed EV explicitly and reached the same conclusion
  for a quantitative reason instead.
- **Quant (decisive):** EV per share ≈ p·(D−M) − (1−p)·(M−U), D=$13.25, M≈$13.18,
  U≈$10.25 (reasoned from the disclosed ~31% announcement premium, since the
  internal stub's pre-deal print is corrupted/impossible). At p=0.96-0.97: EV ≈
  -$0.02 to -$0.05/share. Break-even p (net of ~15bps round-trip costs) ≈ 98.3%,
  above the defensible base-rate estimate. Success-case annualized return (ignoring
  break risk) ≈ 2.0-3.3% net, failing an 8-10% hurdle by 3-4x. Risk/reward ≈ 59:1
  against (risking ~$2.93 break-loss to make ~$0.05).
- **Bear:** Reframed the claim precisely — not "EV confidently negative" (fragile,
  depends on unverified U) but "EV positive-but-trivial at best (~2-3% annualized),
  failing the hurdle before costs" (robust, since upside is capped at $0.07/share
  regardless of U). Named the one concrete unresolved risk: the ISS/Glass Lewis
  recommendation, unknown, resolves before the July 16 vote.
- **Bull:** Opened long CCRN on a clean-catalyst thesis, but ran its own EV math in
  rebuttal (spread annualizes to ~2.7-4.6%, well below the hurdle; EV ≈ -1.4% at
  p=0.92 given ~24-31% break-loss severity) and downgraded to no-new-entry — a
  hold-only argument for pre-existing exposure, not a fresh-money buy.

**Cross-cutting issue:** the `toa price CCRN` feed returned an incoherent series
($26.06 on 6/1 → $103.03 on 7/10 → $396.51 on 7/12, continuing to $452.84 by the
vote date) — structurally impossible for a fixed $13.25 all-cash deal. A separate
live-quote fetch (bull, Round 2) also returned an implausible $9.48 x $16.89
book. All three personas discarded both artifacts and relied instead on bear's
sourced last-trade figure (~$13.18), explicitly flagged as not a firm executable
bid.

**What would need to change to revisit:** (1) a confirmed ISS/Glass Lewis
recommendation (against would materially raise deal-break risk; for would only
marginally help since the return is already hurdle-failing even at near-certainty);
(2) a live, executable, cross-checked CCRN quote — if the real spread is wider
than ~0.53% (e.g. M at $12.60-12.85), that would signal information this debate
doesn't have and could flip the call to investigate a real edge; (3) any topping
bid or injunction motion (as opposed to the already-priced-in demand letters).

Full transcript: see `transcript.md`.
