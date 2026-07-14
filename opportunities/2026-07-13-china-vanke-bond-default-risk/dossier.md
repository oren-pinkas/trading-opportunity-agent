---
id: 2026-07-13-china-vanke-bond-default-risk
title: China Vanke faces renewed default risk on failed bond extension bids
status: researched
created: '2026-07-13T23:47:30Z'
event:
  type: economic
  summary: China Vanke's proposal to extend a M bond failed after three bids; company
    still has hundreds of millions more in yuan bonds maturing through 2026, threatening
    wider property-sector contagion.
  impact_window: '2026-07-31'
tickers:
- CHVKY
sources:
- title: China Vanke unveils fresh proposal to extend US$366 million bond after 3
    failed bids
  url: https://www.scmp.com/business/banking-finance/article/3336719/china-vanke-unveils-fresh-proposal-extend-us366-million-bond-after-3-failed-bids
  accessed_at: '2026-07-13T23:47:30Z'
hypothesis:
  statement: China Vanke's unsponsored US OTC ADR (CHVKY) is in accelerating credit
    deterioration - three consecutive failed extension bids on a $366M bond, hundreds
    of millions more in yuan maturities through 2026, and a degrading state backstop
    (Shenzhen Metro Group reportedly capped further financing and demanded collateral,
    even retroactively, after roughly two years of open-ended support). The directional
    read strengthened round over round as the quant panelist revised gross short EV
    from about +4.8% to about +8.0% once the backstop-degradation datapoint was
    incorporated. However the thesis is not actionable in this harness - toa price
    CHVKY returns HTTP 400 on the only configured provider (twelvedata) across multiple
    timestamps while a SPY control resolves normally, independently reproduced by
    all three personas, and no defensible liquid single-name proxy exists (peer
    distressed developers share the same OTC data gap; a broad China ETF dilutes
    the idiosyncratic default catalyst to noise). Confidence below reflects thesis
    conviction only, not executability, which is independently zero.
  direction: no-trade
  confidence: 62
plan:
  ticker: CHVKY
  action: no-trade
  entry:
    time: null
    target_price: null
    trigger: No position will be opened. toa price CHVKY has no working data feed
      (HTTP 400 vs a working SPY control), so there is no anchorable entry, mark,
      or exit; recording a fill would be fabricated P/L. Revisit only if (a) a single
      successful toa price call on CHVKY succeeds on any provider, (b) a genuinely
      liquid single-name proxy emerges with a comparable default-risk profile and
      a dated near-term catalyst, or (c) a CDS or offshore-bond price feed becomes
      available in this harness. Log as a high-conviction directional short thesis
      for monitoring only.
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: Two cruxes never converged even though all three personas agreed on the
    no-trade/executability verdict. First, the bull holds each new failed bond-extension
    print is a fresh re-pricing draw even when the broader distress narrative is
    known, while the bear holds this is an 18+ month stale trend (roughly 15 Shenzhen
    Metro loan commitments totaling over RMB 34.6bn since early 2025) already priced
    in, so a failed extension confirms rather than surprises - this is the core question
    of whether any edge remains if execution ever becomes possible. Second, on the
    bailout-relief magnitude, the bear argued the December 2025 Shenzhen Metro facility
    being capped and collateralized should haircut the relief-rally magnitude to
    roughly plus 6-8 percent rather than the quant's unrevised plus 15 percent estimate;
    the quant instead lowered only the bailout scenario's probability (0.25 to 0.17)
    and left magnitude unchanged, so the two never settled on one bailout-scenario
    value. A lower magnitude would pull gross EV below the quant's revised plus 8.0
    percent and could push net EV back toward noise even before the zero-executability
    gate. Both cruxes should be revisited first if the data-feed blocker ever clears.
  last_updated: '2026-07-14T00:45:59Z'
---

## Scouted 2026-07-13T23:47:30Z

## Researched 2026-07-14T00:45:59Z
