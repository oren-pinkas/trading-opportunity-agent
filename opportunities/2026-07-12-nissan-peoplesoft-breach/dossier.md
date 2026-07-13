---
id: 2026-07-12-nissan-peoplesoft-breach
title: Nissan Americas confirms employee data breach via Oracle PeopleSoft zero-day
status: researched
created: '2026-07-12T19:10:51Z'
event:
  type: regulatory
  summary: Nissan Americas confirmed a ShinyHunters-linked breach (CVE-2026-35273)
    exposing employee SSNs/banking data across US/Canada/Mexico/Brazil, part of a
    100+ org PeopleSoft wave with further disclosures likely.
  impact_window: '2026-07-17'
tickers:
- NSANY
sources:
- title: Nissan Confirms Data Breach Following Oracle PeopleSoft 0-Day Attacks
  url: https://cybersecuritynews.com/nissan-confirms-data-breach/
  accessed_at: '2026-07-12T19:10:51Z'
hypothesis:
  statement: The Nissan Americas / Oracle PeopleSoft (CVE-2026-35273) breach is a
    stale, employee-data-only event (SSN/banking/payroll; no customer data, no operational
    or financial materiality) first disclosed ~2026-06-25 with no measurable NSANY
    price reaction at the time. Exposure is diluted across 100+ victim organizations
    in the ShinyHunters/UNC6240 PeopleSoft wave, legal precedent is trivial (~$1.5M
    prior Nissan breach settlement), and NSANY's price is dominated by Nissan's own
    restructuring/JPY 533.1B loss narrative, not the breach. The 2026-07-17 "impact
    window" is an unanchored calendar artifact, not an information catalyst -- with
    no fresh, dated, Nissan-specific catalyst there is no entry trigger and no exit
    trigger. Expected breach-attributable drift (~0.3%) is swamped by realistic thin-ADR
    round-trip friction (~2.5%), yielding negative EV in either direction.
  direction: none
  confidence: 90
plan:
  ticker: NSANY
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
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
  dissent: 'Near-unanimous convergence (bull confidence 30->12, bear 88->92, quant
    18->8-on-positive-EV) -- the unresolved items are second-order, not directional.
    All three agreed in principle on a contingent watch-only monitor for a fresh,
    dated, Nissan-specific escalation (named extortion demand, confirmed customer/financial
    PII, or a Nissan-specific regulatory action with stated materiality) but never
    operationally defined it: no agreed dislocation threshold, no resolution on whether
    a 7201.T (Tokyo primary listing) move without a corresponding NSANY move is even
    tradeable in the illiquid NSANY OTC ADR, and no reconciled borrow/capacity limits
    that may make the conditional +1.5% edge (unconditional ~+0.15%, P(trigger)~10%)
    uncapturable at any real size. Open question for post-mortem: whether this dossier
    warrants any revisit before 7/17 absent a fresh catalyst, or should be shelved
    to the 2026-07-29 earnings check. Separately, the toa NSANY price feed ($124-$400
    stub) was independently vetoed by quant and corroborated as wrong by both bull
    and bear (real price ~$4-6) -- a systemic data-layer issue to fix before any NSANY
    dossier is actioned.'
  last_updated: '2026-07-13T03:24:43Z'
---

## Scouted 2026-07-12T19:10:51Z

## Researched 2026-07-13T03:24:43Z — NO-TRADE

Three persona agents debated whether to trade NSANY on the Nissan Americas / Oracle PeopleSoft (CVE-2026-35273) employee-data breach headline (impact window 2026-07-17) across three rounds -- independent research, rebuttal, and neutral synthesis. Models: bull and bear on Sonnet, quant and synthesizer on Opus.

The bull opened cautious (30/100): employee-data-only breach, diffuse blame across 100+ ShinyHunters/UNC6240 victims, a trivial $1.5M prior-Nissan-breach settlement precedent, and NSANY's real ~$3.88 price driven by Nissan's own JPY 533.1B restructuring loss, not the breach. Proposed a small tactical long triggered only on a confirmed >=3% breach-specific dip between now and 7/17, exiting 7/24 before the 7/29 earnings. The bear opened NO TRADE (88/100): the real disclosure timeline (exploitation May27-Jun9, patch Jun10, class action filed Jul1) means the news is weeks stale with no fresh catalyst on 7/17; NSANY is a thin OTC ADR whose real price discovery sits in Tokyo (7201.T); academic evidence shows SSN-only breaches are historically LESS impactful than email breaches; and the 7/17 "impact window" is an unmapped calendar artifact -- the same error class flagged in a prior Caesars post-mortem lesson against mapping legal/corporate dates onto execution timestamps. The quant opened skeptical (18/100 on positive EV existing): flagged the toa NSANY price stub ($124-$400) as internally incoherent and refused to use it; modeled EV for a short at roughly -0.65% (favorable drift ~0.4% against ~0.9-1.2% round-trip friction on a thin ADR), with no edge on the fade side either.

By Round 2, all three converged further toward NO TRADE. Bull conceded that the absence of any reaction to the real 6/25 disclosure undercuts the entire fade-the-panic premise, that its own >=3% trigger sits above what these breaches historically produce, and cut confidence to 12/100, reducing the plan to a watch-only contingent monitor. Bear raised confidence to 92/100, noting the convergence of independent methodologies (its qualitative case and quant's EV math) as itself evidence, and steelmanned then rejected a "regulatory-aggregation/basket-trade" counter-scenario (rejecting it because any such flow would hit the Tokyo primary listing first, not the lagging illiquid NSANY OTC line). Quant recomputed EV using the real ~$4-6 price (independently confirmed by both bull and bear, versus the incoherent stub) and found friction is actually WORSE on a low-priced thin ADR -- fixed-cent spreads are a larger percentage of price -- pushing EV to roughly -2.2% to -2.5%, and cut confidence in a positive-EV trade existing to 8/100. Quant's only surviving construct was a strictly conditional short gated on a fresh, dated, Nissan-specific escalation, with unconditional EV of only ~+0.15% (P(trigger)~10%) -- "a monitoring alert, not a position."

Verdict: stand aside (confidence 90 in no-trade). All three personas independently converged on NO TRADE with worsening conviction and worsening EV across rounds. A data-integrity fault reinforced this: the repo's `toa price NSANY` stub tool returned incoherent synthetic prices ($124-$400) versus the real ~$4-6 tape (52-week range ~$4.05-$6.06) -- responsible entry/stop sizing would be impossible regardless of view. The only carry-forward is a watch-only monitor for a fresh, dated, Nissan-specific escalation, best observed on the Tokyo primary listing (7201.T) rather than the illiquid NSANY OTC ADR, expiring at the 2026-07-29 earnings check if no qualifying trigger appears. Full debate with citations in transcript.md.
