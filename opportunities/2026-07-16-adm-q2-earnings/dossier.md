---
id: 2026-07-16-adm-q2-earnings
title: Archer-Daniels-Midland Q2 2026 earnings
status: researched
created: '2026-07-16T05:04:39Z'
event:
  type: earnings
  summary: ADM reports Q2 2026 results Aug 4 before the open, with China back buying
    US soybeans and a record projected 2026/27 crop shaping crush-margin outlook
  impact_window: '2026-08-04'
tickers:
- ADM
sources:
- title: ADM to Release Q2 Financial Results Amid Market Volatility
  url: https://www.gurufocus.com/news/8958064/adm-to-release-q2-financial-results-amid-market-volatility
  accessed_at: '2026-07-16T05:04:39Z'
hypothesis:
  statement: "ADM enters its Aug 4 2026 pre-market print near a 52-week high
    (around USD 86) and roughly 9 percent above the revised USD 78.11 mean
    analyst target, into a Hold/Sell-leaning consensus. The bull's directional
    edge collapsed on its own concessions in rebuttal (dropped the China leg,
    conceded Brazil's record crop is structural, conceded the sell-the-beat
    pattern was the single best piece of evidence against the bull case). The
    bear's downside thesis rests on an n equals 2 sell-the-beat pattern that did
    not survive the quant's close-to-close correction: the widely cited -9.4
    percent Q4 2025 tumble was a premarket print that reversed to a -0.5 percent
    close, and Q1 2026 closed +4.9 percent, not the -1.45 percent originally
    cited. With no live Aug 4 options chain or implied volatility available, no
    structure - long or short, naked or defined-risk - can be certified as
    clearing the approximately 2 percent net-EV no-trade threshold. There is no
    reliable, quantified edge in either direction."
  direction: none
  confidence: 62
plan:
  ticker: ADM
  action: no-trade
  entry:
    time: '2026-08-03T19:55:00Z'
    target_price: null
  exit:
    time: '2026-08-04T19:59:00Z'
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
  dissent: "The bear (confidence raised to 63 out of 100) still argues its
    specific USD 82 / USD 75 defined-risk put spread should trade: max loss is
    capped at premium, so the quant's un-hedgeable positive tail-risk discount -
    valid against a naked short - is misapplied to a capped structure, and once
    that discount is removed, the quant's own roughly plus 0.9 percent gross
    short EV plus the directional lean (price now even further above raised
    targets) constitute a green light at small, 1 to 2 percent, size. The quant
    (48 out of 100) does not concede: it declined to certify any defined-risk
    spread, call or put, as positive-EV, on the grounds that with no live Aug 4
    options chain or implied volatility, the premium and strike economics are
    unknown, and a spread needing more than a 3 percent move to reach the money
    against a roughly 5 percent expected move on a near coin-flip distribution
    cannot be shown to clear the threshold. This is a data-availability dispute
    as much as a tail-risk dispute - the bear reasons from the payoff shape, the
    quant refuses to price a structure whose actual cost is unobserved. Whether
    the bear's capped put spread would in fact have printed positive is the
    empirical question the post-mortem should adjudicate against realized Aug
    4/Aug 5 option marks."
  last_updated: '2026-07-21T15:52:00Z'
---

## Scouted 2026-07-16T05:04:39Z

## Researched 2026-07-21T15:52:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), restricted to
this opportunity alone. Bull's independent Round 1 research built a bullish case on
crush-margin and China-demand tailwinds plus two FY26 guidance raises and a four-
quarter EPS beat streak (confidence 42), while flagging that ADM sat at a 52-week
high (USD 86.155) above a stale-looking Street target cluster. Bear's independent
Round 1 research argued the dossier's stated catalyst (China and crush) was not
the actual rally driver - ethanol and RVO finalization was - and that crush
margins were softening, Brazil's crop was a record, and only a fraction of
China's committed soybean purchases had shipped (confidence 58). Quant's
independent Round 1 EV math found a "sell-the-beat" pattern and computed a
negative long EV and a sub-threshold short EV, recommending NO TRADE
(confidence 40). In Round 2, bull conceded the sell-the-beat pattern and
Brazil's structural crop record, dropped China as a thesis leg, and withdrew its
call spread, dropping to confidence 30. Bear raised confidence to 63, arguing the
quant's tail-risk discount does not apply to a capped-loss put spread. Quant
self-corrected a Round 1 data error - the cited "-9.4 percent Q4 tumble" was a
premarket print that reversed to a -0.5 percent close, and Q1 2026 actually
closed +4.9 percent - which invalidated the sell-the-beat pattern on a close-to-
close basis; quant's revised EV stayed sub-threshold on both sides with no live
options chain available to certify a defined-risk structure, holding at NO TRADE
(confidence 48). Verdict: NO-TRADE (not scheduled, not simulated). Full debate
with citations in `transcript.md`.
