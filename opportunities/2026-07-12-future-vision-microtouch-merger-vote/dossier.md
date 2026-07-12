---
id: 2026-07-12-future-vision-microtouch-merger-vote
title: Future Vision II SPAC shareholder vote on MicroTouch merger set for July 23
status: researched
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: Future Vision II Acquisition Corp (FVN) holders vote July 23, 2026 on a
    ~$90M business combination to become MicroTouch Inc.
  impact_window: '2026-07-23'
tickers:
- FVN
sources:
- title: Future Vision II Acquisition Corp prospectus (StockTitan)
  url: https://www.stocktitan.net/sec-filings/FVN/424b3-future-vision-ii-acquisition-corp-prospectus-filed-pursuant-to--2a17e13002c0.html
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: 'All three personas converged on NO TRADE. The vote itself is a non-event
    (SPAC merger votes pass ~92-95% of the time, and 100% of MicroTouch holders already
    signed a Transaction Support Agreement), so the only candidate edges were (a) a
    directional hold-through-close long and (b) a "buy common, redeem for NAV, keep
    the rights for free" structural arb. Both fail. The directional long is negative
    EV under base rates for de-SPACs (going-concern disclosure in the 10-K, a $61.0M
    trust below the $90M deal EV, a thin Hong Kong target with standard PRC/HFCAA risk
    language, and a median de-SPAC 12-month drawdown of 30-65%); corrected EV ≈ -12.9%
    gross (~-14% after costs) using the actual ~$10.96 market entry. The "free rights"
    arb is a category error: SPAC units separate into common + rights well before a
    vote, so redeeming a common share returns trust cash but conveys zero rights --
    rights must be bought outright via a units/rights quote that cannot be verified
    (the only available price feed is a deterministic, non-physical stub returning
    $161-$454 for a sub-$11 stock). Once the $10.90-vs-$10.51 NAV figures are reconciled
    to a plausible accreted floor (~$10.75-10.90), the common leg alone is a guaranteed
    small loss before fees. Separately, a live and unresolved deadline/vote-date
    mismatch exists: the last confirmed extension only pushes the outside date to
    July 13, 2026, ten days before the scheduled July 23 vote, with no located filing
    covering the gap -- this alone lowers effective P(deal closes) to roughly 0.78
    and raises the probability of a total loss on any rights-only structure to ~20-23%.
    No verified live price and no confirmed extension filing exist at decision time,
    so no edge can be sized in either direction.'
  direction: no-trade
  confidence: 82
plan:
  ticker: FVN
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  monitor_conditions:
  - SEC filing (8-K/proxy supplement) confirming the extension outside date covers
    the July 23, 2026 vote date
  - A reproducible, unit-verified live FVN unit/rights/common quote replacing the
    deterministic stub feed (non-physical $161-454 prints for a sub-$11 stock)
  - Rights-agreement language confirming rights survival/mechanics through a redemption
    election, plus broker/DTC redemption-election handling confirmed clean before
    the ~July 21 deadline
  - Sourced current trust NAV per share and public share count reconciling the $10.51
    (12/31/2025 10-K) vs ~$10.90 (accreted estimate implied by the ~$10.96 market
    print) figures
  - Post-close actual redemption percentage vs. the 58.6% Nasdaq public-float threshold
    and Nasdaq's continued-listing determination (feeds the bear's post-close short/avoid
    setup)
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
  dissent: 'The panel unanimously reached NO TRADE, but split on whether the "rights-isolation"
    structural trade is a mispriced non-trade or a real low-risk trade merely blocked
    by missing data. Bear upgraded it to "conditional small size" (1-2% of book) on
    the premise that IF rights survive a redemption election as a separate security
    AND NAV is close to purchase price, it is a legitimate catalyst-isolation trade
    distinct from the directional thesis. Quant rejects the premise mechanically:
    units separate into common + rights before the vote, so there is no "keep the
    rights while redeeming your common" structure -- rights must be owned outright,
    making it a units trade, not a free option, and reconciling the NAV gap turns
    the common leg into a guaranteed small loss regardless of the rights question.
    Gold for the post-mortem: was there ever a real, tradeable rights-isolation structure
    the panel wrongly dismissed for lack of data, or was the bull''s original trade
    a category error (redeeming common != retaining rights) that no amount of verified
    data would have rescued? Unverified at decision time, all load-bearing: (1) whether
    any filing extends the outside date past the July 23 vote (deadline/vote-date
    mismatch is live and material, driving P(deal closes) to ~0.78); (2) any real
    live quote for common or units/rights (only feed available is a deterministic
    stub returning non-physical prices, confirmed independently); (3) the true accreted
    trust NAV/share and public share count ($10.51 vs ~$10.90 gap reasoned-about but
    never freshly sourced); (4) rights-agreement survival mechanics and broker/DTC
    redemption-election handling (an unpriced execution cost specific to the arb).'
  last_updated: '2026-07-12T22:11:53Z'
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-12T22:11:53Z — NO-TRADE

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesizer opus). Round 1:
bull proposed a barbell -- buy FVN common and file a redemption election to lock a
~$10.90 floor while keeping the attached rights (1/10 share -> ~575,000 MicroTouch
Inc shares, 3.3% of post-close cap) "funded by the trust's own cash," plus a
directional sleeve targeting $12-13 post-close, citing the 100% MicroTouch Transaction
Support Agreement and serial sponsor-funded extensions as de-risking signals
(confidence 6/10). Bear independently found a live deadline/vote-date mismatch (last
confirmed outside-date extension only to July 13, 2026, vote scheduled July 23, no
covering filing located) and framed the extensions as a going-concern distress signal
rather than commitment; recommended pass, at most a post-close short/avoid once
redemption% and Nasdaq float determination are known. Quant computed trust NAV at
$10.51/share from the 10-K and ran an EV table on the directional hold-through sleeve
(20% pop/45% drift/27% collapse/8% fail) yielding ~-10.6% after costs; flagged the
`toa price` feed as a deterministic non-physical stub ($161-$454 for a sub-$11
stock), independently confirmed by the orchestrator, leaving no verified live price.
Round 2: bull conceded significant ground -- treated the deadline mismatch as
disqualifying-until-verified, conceded quant's $10.51 NAV was more rigorously sourced,
and conceded the going-concern disclosure undercuts the "commitment" framing; cut
confidence to 3/10 and restricted any action to a conditional capped redemption-arb.
Bear engaged the rights-isolation trade on its own terms, conceding it could be
legitimate IF two preconditions verify (rights survive redemption as a separate
security; NAV gap reconciled) but flagged both as unresolved, and separately argued
quant's 27% collapse probability was if anything too low. Quant delivered the
decisive correction: SPAC units separate into common + rights before a vote, so
redeeming common conveys zero rights -- the bull's "free" trade requires owning
rights/units outright at an unverifiable quote; reconciling the $10.90-vs-$10.51 gap
to a plausible accreted floor (~$10.75-10.90) means buying common at the ~$10.96
market print and redeeming is a guaranteed small loss before fees, before rights even
enter. Quant also priced the deadline mismatch as lowering P(deal closes) to ~0.78
and raising P(rights total loss) to ~20-23%, producing a corrected EV of -12.9% gross
(~-14% after costs). Round 3 synthesis: high-confidence (82/100) NO TRADE from
genuine three-way convergence including real concessions on all sides, not just an
outvoted position. Monitor-only pending: (1) an extension filing covering the July
23 vote, (2) a verified non-stub live quote, (3) rights-agreement survival mechanics
and clean broker redemption-election handling, (4) a sourced current trust NAV/share
count, (5) post-close redemption% vs. the 58.6% Nasdaq float threshold.
