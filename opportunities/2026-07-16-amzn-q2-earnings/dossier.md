---
id: 2026-07-16-amzn-q2-earnings
title: Amazon Q2 2026 earnings report
status: researched
created: '2026-07-16T03:59:59Z'
event:
  type: earnings
  summary: Amazon reports Q2 2026 results on 2026-07-30 with AWS growth and retail
    margins in focus
  impact_window: '2026-07-30'
tickers:
- AMZN
sources:
- title: Kiplinger Earnings Calendar
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-16T03:59:59Z'
hypothesis:
  statement: >-
    AMZN Q2 2026 earnings (print 2026-07-30, after market close) offers no clean
    directional edge for a 1-day post-earnings reaction trade. All three panelists
    converged on this by Round 2. Bull evidence going in looked strong (AWS grew 28
    percent YoY to USD 37.6B in Q1, fastest pace in 15 quarters, record 13.1 percent
    operating margin, Strong Buy consensus, average target USD 314.23, KeyBanc raised
    to USD 335 on 2026-07-16) but the bear showed this good news is already priced:
    sell-side targets sit 27-36 percent above the USD 246.71 spot (2026-07-17)
    BEFORE the print, meaning Q2 must clear an already-raised bar, not a fresh low
    one. Additional bear-sourced risk: Q1 net income of USD 30.25B included a USD
    16.8B one-time non-cash Anthropic mark-to-market gain (earnings-quality flag);
    TTM free cash flow collapsed roughly 95 percent from about USD 26B to about USD
    1.2B on AI capex (FY26 capex target about USD 200B, up about 60 percent YoY);
    long-term debt roughly doubled YoY to USD 119.1B; and Q2 guidance (USD 194-199B
    revenue, USD 20-24B operating income) is explicitly conditioned by management on
    "current tariff conditions holding." The quant, highest-confidence panelist,
    revised its scenario grid after seeing this data, split out a new "headline beat
    but flattered by the one-time gain" bucket, and moved expected signed 1-day move
    from plus 0.10 percent to minus 0.90 percent, making net long EV about minus 1.15
    percent after costs. The bull conceded from 55 to 42 confidence and dropped to a
    token defined-risk structure only, accepting no-trade as the honest outcome if
    the quant holds its beat probability at 0.30-0.35. The bear held 55 confidence
    no-trade with a mild left-tail lean. The one residual edge found — the quant's
    estimated 5.1 percent expected absolute move versus a roughly 6-7 percent implied
    straddle — is a short-volatility observation, not a directional one, rated only
    about 55 confidence by the quant itself and out of a plain long/short mandate.
  direction: none
  confidence: 80
plan:
  ticker: AMZN
  action: no-trade
  entry:
    time: '2026-07-30T19:59:00Z'
    target_price: null
  exit:
    time: '2026-07-31T19:58:00Z'
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
    The strongest unresolved disagreement is the mandate-vs-edge tension around
    volatility. The quant's most rigorous finding is that the only honest edge is
    short-volatility: its modeled 5.1 percent expected absolute move sits below the
    roughly 6-7 percent implied straddle, meaning options look rich relative to its
    distribution. That edge is real but low-confidence (about 55 out of 100 on the
    quant's own scale, thin and subjective, no positioning data, no euphoric extreme
    to anchor it) and cannot be expressed within a plain long/short equity mandate,
    since capturing it needs a defined-risk short-premium options structure (bear
    call spread or iron condor). Open question for a future post-mortem: was
    no-trade the correct call, or did the mandate itself cause the panel to leave a
    legitimate, if marginal, short-vol edge on the table? Secondary tension: the
    bull never fully conceded that AWS momentum deserves less weight than the
    quant's reaction-conditioned framing implies, holding P(beat) around 0.40-0.45
    versus the quant's 0.30 — but even the bull's higher figure sits below the
    quant's stated tradable-edge threshold of about 0.556, so this disagreement does
    not change the outcome.
  last_updated: '2026-07-22T07:59:00Z'
---

## Scouted 2026-07-16T03:59:59Z

## Researched 2026-07-22T07:59:00Z — NO-TRADE

Three-round panel (bull/bear on sonnet, quant on opus; synthesizer on opus). Bull
opened long on an AWS-reacceleration and retail-margin thesis (55 confidence) but
lacked live price/consensus data. Bear brought sourced facts: spot USD 246.71
(2026-07-17), 52-week range USD 196.00-278.56, Strong Buy consensus with average
target USD 314.23 and a KeyBanc raise to USD 335 on 2026-07-16, Q1 AWS growth of 28
percent YoY to USD 37.6B (fastest in 15 quarters, record 13.1 percent operating
margin), a USD 16.8B one-time non-cash Anthropic mark-to-market gain inflating Q1
net income, TTM free cash flow collapse of about 95 percent to roughly USD 1.2B on
an FY26 capex target near USD 200B, long-term debt roughly doubled to USD 119.1B,
and Q2 guidance (USD 194-199B revenue, USD 20-24B operating income) explicitly
conditioned on tariff conditions holding. Quant's Round 1 base-rate/EV math (built
without live data) already showed near-zero net directional edge after costs; in
Round 2, incorporating the bear's sourced data, the quant revised its scenario grid
to a new expected signed move of minus 0.90 percent and long EV of about minus 1.15
percent, raising its no-clean-directional-edge confidence from 72 to 78. The bull
conceded to 42 confidence and a token size only; the bear held 55 confidence
no-trade with a bearish tilt. All three converged on no directional edge. Per the
DAL and LEVI institutional lessons, this converges to NO-TRADE rather than a
quarter-size or "for the learning loop" position. See transcript.md for the full
three-round debate and citations.
