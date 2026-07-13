---
id: 2026-07-13-kddi-email-breach
title: KDDI discloses email system breach affecting five Japanese ISPs
status: scheduled
created: '2026-07-13T16:16:37Z'
event:
  type: regulatory
  summary: KDDI Corporation disclosed threat actors accessed an email system shared
    by five other Japanese ISPs, raising regulatory and liability exposure for the
    telecom.
  impact_window: '2026-08-01'
tickers:
- KDDIY
sources:
- title: Data Breach Roundup (July 3-9, 2026)
  url: https://www.privacyguides.org/news/2026/07/10/data-breach-roundup-july-3-9-2026/
  accessed_at: '2026-07-13T16:16:37Z'
hypothesis:
  statement: The KDDI five-ISP shared-email breach, as currently sourced (a privacy-newsletter
    aggregator, not a TDnet/KDDI IR/PPC filing), is not a confirmed, tradeable catalyst.
    It describes a contained B2B/vendor email-system exposure with no confirmed mass
    PII/financial data, no quantified liability, and no regulatory deadline actually
    tied to the soft 2026-08-01 window. Base rates for telecom breach disclosures show
    a weak, largely-retracing reaction (-0.5% to -2.5% T+1, ~70% retrace in 5-10 sessions),
    and KDDIY is a thin, lagging ADR that digests Tokyo's overnight move at a spread.
    Net expected value is negative after spread/slippage/carry (panel converged on
    approximately -0.15% to -0.33%).
  direction: no-trade
  confidence: 78
plan:
  ticker: KDDIY
  action: pass
  entry:
    time: '2026-07-16T13:30:00Z'
    target_price: null
  exit:
    time: '2026-07-31T19:30:00Z'
    target_price: null
  expected_profit_pct: 0
  note: Contingent watch-trigger only, not a live fill. Arm a ≤0.25% info-only starter
    only if a TDnet/KDDI IR/PPC filing confirms mass PII/financial exposure and a
    concrete liability item AND a confirmed 9433.T price+volume reaction is observed
    by the 2026-07-16T13:30:00Z checkpoint. If triggered, cap the window at the nearest
    valid NYSE session on/before the soft 08-01 date (rolled to 2026-07-31T19:30:00Z
    since 08-01 is a Saturday). Absent the trigger, hard pass.
research:
  last_updated: '2026-07-13T17:42:18Z'
  dissent: Bull vs. Bear/Quant on whether a defined-stop long has favorable asymmetry
    that static-hold EV understates. Bull argues the panel's own base rate (capped
    downside, ~70% retrace) plus a -3% stop converts a marginally-negative-EV event
    into a stop-managed asymmetric long. Bear/Quant counter that (i) there is no
    confirmed event to trade at all absent a TDnet/PPC filing, and (ii) the Docomo
    precedent reverted TO PAR, not to an overshoot, so buying a dip that must both
    exist and then exceed itself is double-counting a mean-reversion that historically
    only returns to zero. Unresolved without the missing primary-source filing.
---

## Scouted 2026-07-13T16:16:37Z

## Researched 2026-07-13T17:42:18Z

Three-round panel (bull/bear/quant → synthesis) converged on **no-trade / pass**.
Root cause: the only source is a privacy-newsletter aggregator, not a TDnet/KDDI
IR/PPC filing — there is no confirmed regulatory or financial anchor to trade
against. Base-rate EV for telecom breach disclosures is negative after ADR
spread/slippage/carry (~-0.15% to -0.33%). A contingent watch-trigger is set: arm
a token starter only if a primary-source filing confirms scope and a 9433.T
volume reaction is observed by 2026-07-16T13:30:00Z; otherwise hard pass. Full
debate: [transcript.md](transcript.md).
