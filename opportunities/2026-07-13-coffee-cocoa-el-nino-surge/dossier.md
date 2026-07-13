---
id: 2026-07-13-coffee-cocoa-el-nino-surge
title: Coffee and cocoa futures spike on El Nino weather risk
status: scheduled
created: '2026-07-13T09:57:39Z'
event:
  type: macro
  summary: Coffee futures jumped as much as 18.5% and cocoa rallied above $6,400/tonne
    in a historic session as traders repriced El Nino weather risk hitting Brazil
    and West African crops, pressuring input costs for chocolate and coffee retailers.
  impact_window: '2026-07-27'
tickers:
- SBUX
- HSY
- MDLZ
sources:
- title: Coffee Price Surge Enters 'Meme-Stock Territory' Amid Weather Fears
  url: https://www.forbes.com/sites/tylerroush/2026/07/07/coffee-price-surge-enters-meme-stock-territory-amid-weather-fears/
  accessed_at: '2026-07-13T09:57:39Z'
hypothesis:
  statement: "The El Nino commodity spike is unlikely to force a discrete downward
    repricing of HSY before 07/27 because multi-quarter hedge books and demonstrated
    pricing power delay COGS impact and no HSY/MDLZ earnings print occurs in-window;
    the tradeable edge is elevated implied volatility that should compress without
    a spot reversion, so sell defined-risk downside vol on HSY rather than
    establishing any directional short."
  direction: neutral
  confidence: 61
plan:
  ticker: HSY
  action: sell
  entry:
    time: '2026-07-15T14:35:00Z'
    target_price: 175.81
  exit:
    time: '2026-07-27T19:45:00Z'
    target_price: 176.50
  expected_profit_pct: 3.5
research:
  last_updated: '2026-07-13T14:50:00Z'
  dissent: "Bull maintains this commodity move (+18.5% coffee, cocoa >$6,400) is
    faster and larger than the 2024 cocoa or 2010-11 coffee analogues the quant's
    EV model relies on, so tail risk skews to the downside and a discrete
    sell-side/guidance-language repricing could still occur within three weeks even
    without an earnings print; if HSY gaps down through the short strike the
    defined-risk credit spread caps but does not avoid the loss, and the bull's
    collared short would outperform in that scenario."
---

## Scouted 2026-07-13T09:57:39Z

## Researched 2026-07-13T14:50:00Z

Three-round panel debate (bull/bear/quant, synthesizer opus) converged on **neutral /
sell volatility** (confidence 61) -- bear and quant aligned on a defined-risk HSY put
credit spread harvesting elevated IV rather than any directional short, after quant's
EV calc showed a naked 2-week short carrying a net -1.2% edge. Bull dissented,
dropping SBUX but keeping a smaller collared short on HSY/MDLZ. Entry ~07/15, exit
into the 07/27 impact window. Full transcript: `transcript.md`.
