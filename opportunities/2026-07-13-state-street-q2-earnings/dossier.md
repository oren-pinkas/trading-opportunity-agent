---
id: 2026-07-13-state-street-q2-earnings
title: State Street Q2 2026 earnings
status: researched
created: '2026-07-13T20:40:00Z'
event:
  type: earnings
  summary: State Street reports Q2 2026 results July 16; custody/asset-servicing read
    on AUC/A and fee trends
  impact_window: '2026-07-16'
tickers:
- STT
sources:
- title: State Street sets Q2 2026 earnings release date
  url: https://www.stocktitan.net/news/STT/state-street-corporation-nyse-stt-announces-date-for-release-of-dfrn98mn4oz0.html
  accessed_at: '2026-07-13T20:40:00Z'
- title: 'Top Wall Street Forecasters Revamp State Street Expectations Ahead Of Q2 Earnings (Benzinga)'
  url: https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60378153/top-wall-street-forecasters-revamp-state-street-expectations-ahead-of-q2-earnings
  accessed_at: '2026-07-14T08:45:00Z'
- title: 'Is State Street Corp (STT) Overvalued After 3.2% Rally? (GuruFocus)'
  url: https://www.gurufocus.com/news/8925832/is-state-street-corp-stt-overvalued-after-32-rally-gf-value-says-overvalued?mobile=true
  accessed_at: '2026-07-14T08:45:00Z'
- title: "State Street's SWOT analysis: stock faces mixed outlook on expenses (Investing.com)"
  url: https://www.investing.com/news/swot-analysis/state-streets-swot-analysis-stock-faces-mixed-outlook-on-expenses-93CH-4702913
  accessed_at: '2026-07-14T08:45:00Z'
- title: 'State Street Corporation''s Q2 2026 Earnings: What to Expect (Barchart)'
  url: https://www.barchart.com/story/news/2643164/state-street-corporation-s-q2-2026-earnings-what-to-expect
  accessed_at: '2026-07-14T08:45:00Z'
- title: 'OptionSlam STT implied move'
  url: https://www.optionslam.com/earnings/swim/STT
  accessed_at: '2026-07-14T08:45:00Z'
hypothesis:
  statement: >-
    STT enters its Q2 2026 print (Wednesday July 16) at USD 178.02, above every live
    analyst consensus figure the panel found (S&P Global 16-analyst mean USD 171.32,
    MarketBeat blended USD 162.91-166.84) and within about 3% of its 52-week high
    (USD 183.32, set July 6), after a roughly 66% trailing rally and four straight
    EPS beats. The bull's strongest pillar -- a cluster of fresh post-Q1 analyst
    target hikes (Wells Fargo USD 196, Goldman USD 194, BofA USD 190) -- does not
    survive scrutiny: those hikes are already embedded in the live consensus that
    still sits below spot, and a 12-month price target converts to roughly
    0.03-0.04%/trading-day of expected drift, negligible against STT's ~4.5%
    average post-earnings move. The quant's base-rate work shows STT "sells the
    beat" in 2 of the last 3 quarters (down ~4.4-5.1% on guidance/expense
    concerns despite beating EPS both times), and options-implied weekly move
    (~5.75%) exceeds realized (~4.5%), meaning any hedge is also negative-EV.
    Explicit EV is negative for a long (~-0.49%) and for the bull's specific
    USD 180/USD 190 call debit spread (~-27% of premium, since it needs a
    +6.7% move against a ~4.5% typical move while paying for rich pre-earnings
    IV). A naked short is excluded by an un-hedgeable ~9.3% monthly up-tail
    (~50:1 adverse-tail-to-edge). The one theoretically positive-EV structure
    (a small bear call spread selling the rich IV) does not clear the panel's
    ~2%-net-EV no-trade bar and was explicitly logged as sub-conviction, not
    traded.
  direction: none
  confidence: 74
plan:
  ticker: STT
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
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
  dissent: >-
    The strongest unresolved disagreement is bull vs. quant on whether the
    post-Q1 cluster of fresh, above-spot 12-month analyst price targets (Wells
    Fargo USD 196, Goldman USD 194, BofA USD 190, Evercore USD 186) carries any
    predictive power for STT's 1-2 day post-earnings move. The bull argued the
    blended consensus is structurally too slow to capture a genuine re-rating
    off record AUC/A and fee-revenue growth; the quant countered that the
    live (not stale) S&P Global consensus already embeds those hikes and still
    sits below spot, that a 12-month target implies negligible per-day drift
    over an 8-day-expiry trade, and that BofA's USD 190 target carries only a
    Neutral rating (fair-value-in-a-year, not a buy-now signal). Secondarily
    unresolved: the bull's Trump Accounts SPDR S&P 500 default-option ETF
    catalyst, which the bear and quant both treat as a real but multi-quarter,
    non-Q2 catalyst (the June-30 quarter predates any account flows). If STT
    rallies more than 2% on the July 16 print, the post-mortem should test
    whether the analyst target-cluster signal -- not the fundamentals -- was
    the driver the EV model under-weighted.
  last_updated: '2026-07-14T08:45:00Z'
---

## Scouted 2026-07-13T20:40:00Z

## Researched 2026-07-14T08:45:00Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). STT reports
Q2 2026 Thursday July 16; BNY Mellon (closest custody-bank peer) reports one day
earlier, July 15. Reference price USD 178.02 (twelvedata, 2026-07-13T19:59Z).
The bull's opening long thesis (defined-risk USD 180/USD 190 call debit spread)
leaned on five fresh post-Q1 analyst target hikes averaging roughly USD 186-190;
the quant showed the live S&P Global consensus (USD 171.32) already incorporates
those hikes and still sits below spot, and that a 12-month target implies
negligible daily drift against an 8-day-expiry trade. The bear's priced-for-
perfection read (52-week-high proximity, GF Value flagging ~53% overvaluation,
zero insider buying against USD 6.8M sold, two 2026 downgrades, fee-execution
and NII-fragility risk) independently converged with the quant's EV math
(long EV roughly -0.49%; the bull's actual call-spread instrument roughly -27%
of premium since it buys rich pre-earnings IV and needs a bigger-than-typical
move). The bull conceded the live-consensus point and the base-rate "sell the
beat" pattern (2 of last 3 quarters down despite EPS beats) but held a reduced,
BNY-gated position at 55/100 confidence; synthesis found that gate insufficient,
since STT sold its own beat 2 of 3 quarters regardless of peer read-through.
A naked short was excluded throughout by an un-hedgeable ~9.3% monthly up-tail
(~50:1 adverse-tail-to-edge); the quant's one theoretically positive-EV idea
(a small bear call spread selling rich IV) did not clear the panel's ~2%-net-EV
no-trade bar. Verdict: NO-TRADE (not scheduled, not simulated). Full debate with
citations in `transcript.md`.
