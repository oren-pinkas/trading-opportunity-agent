---
id: 2026-07-14-lvmh-q2-earnings
title: LVMH reports Q2 2026 earnings
status: researched
created: '2026-07-14T04:02:05Z'
event:
  type: earnings
  summary: LVMH reports Q2 2026 results July 28; luxury demand recovery in Europe/Asia
    and US tariff exposure are the key swing factors.
  impact_window: '2026-07-28'
tickers:
- LVMUY
sources:
- title: LVMH Company Events, Publications and Financial Calendar - MarketScreener
  url: https://www.marketscreener.com/quote/stock/LVMH-4669/calendar/
  accessed_at: '2026-07-14T04:02:05Z'
hypothesis:
  statement: "LVMH Q2 2026 print offers no tradable edge. All three personas
    independently converged on a symmetric, roughly zero-drift distribution
    around USD 110-111 into the 2026-07-28 report. The -3.7 percent four-session
    drift (114.66 to 110.47) tests as approximately -1.03 sigma noise on
    approximately 1.8 percent daily vol, and the full two-week path is a round
    trip to flat (+4 percent then -3.7 percent), so no directional conviction
    exists. The only positive-EV structure, long volatility, is unreachable
    because the sole in-mandate instrument, the LVMUY OTC ADR, is thinly
    traded with wide spreads and no liquid options."
  direction: none
  confidence: 18
plan:
  ticker: LVMUY
  action: no-trade
  entry:
    time: '2026-07-28T13:31:00Z'
    target_price: null
  exit:
    time: '2026-07-28T19:59:00Z'
    target_price: null
  expected_profit_pct: -1.2
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
  dissent: "Residual uncertainty is entirely about missing inputs, not flawed
    reasoning - all three personas were internally consistent. No one produced
    Street consensus estimates, revision breadth, implied volatility, skew, or
    positioning data, so the symmetric prior is an assumption of ignorance,
    not a measured distribution. The bull's sentiment-reset thesis (less bad
    than feared) remains plausible but unfalsifiable without consensus
    revision data. The 103.00 fifty-two-week floor gives no protection against
    the feared -8 percent tail (which breaches to roughly 101.6), so it
    neither creates asymmetry nor caps downside. Revisit only if real Street
    estimates plus implied vol and skew imply P(up) materially above 0.82 or a
    mispriced vol surface, or if a liquid in-mandate volatility instrument is
    confirmed, such as verified MC.PA Paris-ordinary options with real depth.
    Absent both, NO-TRADE stands."
  last_updated: '2026-07-21T09:15:00Z'
---

## Scouted 2026-07-14T04:02:05Z

## Researched 2026-07-21T09:15:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), restricted
to this opportunity alone. Bull's independent Round 1 built a "less bad than
feared" bellwether re-rating thesis but flagged its own gaps (no Street
estimates, no confirmed live price, unsized tariff risk); confidence 40.
Bear's independent Round 1 surfaced real price data showing a -3.7 percent
four-session drift into the print (USD 114.66 to 110.47) and framed the
near-52-week-low positioning (152.95 high / 103.00 low) as a muddled
two-sided setup rather than a clean asymmetric trade; confidence 35, leaning
NO TRADE. Quant's independent Round 1 flagged LVMUY as a thinly-traded OTC ADR
with sparse 1-minute bars (wide spreads, real fill uncertainty), modeled a
symmetric earnings-day move distribution (approximately 5 percent expected
absolute move, approximately 0 percent expected directional move), and
computed net EV of approximately -1.2 percent after costs; confidence 22, NO
TRADE, since the only positive-EV structure (long volatility) has no liquid
in-mandate instrument on this ADR.

In Round 2, bull conceded the drift and failed-narrative points and the
options-illiquidity finding, dropping to confidence 22; a floated MC.PA
options avenue was explicitly flagged as unverified. Bear reconciled the full
two-week price path (up 4 percent then down 3.7 percent) as noisy chop rather
than a coiled-spring signal and declined to assert the 103.00 floor break was
"cleaner" without fresh evidence, dropping to confidence 22. Quant ran a
significance test showing the -3.7 percent drift is approximately -1.03 sigma
noise, computed that clearing a positive-EV trade would require an
unsupported P(up) of 0.82, and showed the 103.00 floor gives no protection
against the feared -8 percent tail scenario (which breaches to approximately
101.6); confidence fell to 15. All three personas converged to NO TRADE.
Verdict: NO-TRADE (not scheduled, not simulated). Full debate with citations
in `transcript.md`.
