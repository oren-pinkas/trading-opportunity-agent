---
id: 2026-07-12-unitedhealth-q2-fy26
title: UnitedHealth Q2 2026 earnings
status: researched
created: '2026-07-12T17:02:21Z'
event:
  type: earnings
  summary: UnitedHealth Group reports Q2 2026 earnings July 16, 2026, closely watched
    after prior guidance and medical-cost-ratio turmoil.
  impact_window: '2026-07-16'
tickers:
- UNH
sources:
- title: 'Stock market next week: Outlook for July 13-17, 2026'
  url: https://www.cnbc.com/2026/07/10/stock-market-next-week-outlook-for-july-13-17-2026.html
  accessed_at: '2026-07-12T17:02:21Z'
hypothesis:
  statement: UNH enters its July 16 print at ~97.7% of its 52-week high after an
    +80%-off-lows run, with the MCR-normalization thesis largely priced in. All
    three panelists converged toward caution (bull 58->45, bear 35->40, quant
    ~70/100 that a fresh long is poor R/R). Reaction distribution centers on a
    mean of roughly -0.5% to -1% with a fat, negatively-skewed downside tail,
    while implied vol is rich (IV30 ~38, 6.1-6.6% implied move) and beat odds
    (~71%) are already consensus. Both directional option structures price
    negative-to-breakeven; no expression clears costs or the ~7-8x
    adverse-tail-to-edge ratio.
  direction: no_trade
  confidence: 68
plan:
  ticker: UNH
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  contingent:
    short_trigger: Fresh 52-wk high into 2026-07-15 close on thin breadth AND put
      skew richens vs upside, OR new DOJ/Massachusetts legal headline pre-print
      -> small put debit spread (~5% OTM long / ~12% OTM short, <=0.5% risk
      budget), exit by 2026-07-16T19:59:00Z.
    long_trigger: Q2 adj EPS bar confirmed at the lower ~$4.54 figure AND IV
      compresses into the print -> small call debit spread (~5% OTM long /
      ~10-12% OTM short), entry 2026-07-15 close or 2026-07-16 pre-market,
      stop $410, targets $434.30 then $450-460, exit within 1-2 sessions.
    hard_veto: FY26 MCR guide reiterated-not-raised or walked above ~89.3%,
      evidence prior-auth relaxation driving early-Q2 utilization uptick, or
      fresh DOJ/state legal action at the print.
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  last_updated: '2026-07-13T10:21:55Z'
  dissent: 'Two unreconciled inputs: (1) consensus Q2 adj EPS quoted as $4.84
    (bull/quant) vs $4.54 (bear), a ~7% gap never reconciled, which moves the
    beat/miss bar the market judges on 7/16; (2) whether the fat tail is
    symmetric (bull: two down-outliers distort the average, a real right tail
    exists) or negatively skewed (bear/quant: 3 of last 4 prints down, the two
    largest moves both downside, negative skew resolves violently near a
    52-week high). If the panel misjudges skew direction, no-trade is correct
    in expectancy but a missed directional move is the likely regret.'
  transcript: transcript.md
---

## Scouted 2026-07-12T17:02:21Z

## Researched 2026-07-13T10:21:55Z

Three-round bull/bear/quant debate converged to **no_trade** (confidence 68/100
in the no-trade verdict). Full transcript: [transcript.md](transcript.md).
