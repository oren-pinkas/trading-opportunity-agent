---
id: 2026-07-23-kospi-softbank-ai-capex-rally
title: KOSPI SoftBank AI capex rally
status: researched
created: '2026-07-23T09:13:03Z'
event:
  type: macro
  summary: KOSPI closed up 4.4% on a third straight gain as Alphabet's disclosed AI
    capex plan lifted Korean/Japanese chip and AI-adjacent names ahead of regional
    earnings
  impact_window: '2026-07-29'
tickers:
- 9984.T
sources:
- title: KOSPI Closes Up 4.40% at 7096.89
  url: https://en.sedaily.com/finance/2026/07/23/kospi-closes-up-440-percent-at-709689-gaining-29919-points
  accessed_at: '2026-07-23T09:13:03Z'
hypothesis:
  statement: The KOSPI +4.40% print on 2026-07-23 does not support a tradeable
    long in SoftBank Group (9984.T) into the 2026-07-29 window. Three independent
    disqualifiers hold - (a) the named instrument is unpriceable, since 9984.T
    returns HTTP 404 on the twelvedata feed, confirmed structural via a
    same-shape AAPL control call that succeeded, so no entry, mark, or exit
    price can be produced; (b) the only coverage-resolving substitute, SFTBY
    (SoftBank's US OTC ADR), fails an executability screen on live-verified
    data - only 47-50% of 1-minute bars present over two sessions versus 100%
    for an SPY control, roughly USD 4.45M day notional versus roughly USD 36.7B
    for SPY, median bar volume 400 shares, estimated P(clean two-leg fill)
    around 22%; and (c) the SFTBY tape itself falsifies the momentum premise -
    closes of 17.10, 18.16, 17.65, 17.60 across 2026-07-20 through 2026-07-23,
    i.e. one spike then two lower closes, with SFTBY flat-to-down on the very
    session KOSPI printed +4.40%. Even granting a hypothetical clean feed on
    9984.T, the signal is a weak cross-market proxy (KOSPI to 9984.T R-squared
    roughly 0.15-0.25, idiosyncratic-alpha R-squared roughly 0.00-0.05) on a
    2-session-stale catalyst, yielding net expected value of -0.45% to -0.19%
    hypothetically and -0.70% to -0.45% on the actually-executable SFTBY path,
    against a required breakeven P(up) of 60.5% (clean feed) to 78-86% (SFTBY)
    versus a measured 50-54% continuation base rate.
  direction: no_trade
  confidence: 93
plan:
  ticker: 9984.T
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: No plan is placed on 9984.T or on any substitute - not even a
    conditional or watch-and-enter variant. Gate order - (1) threshold gate,
    9984.T is unpriceable (confirmed structural 404, verified via AAPL control
    on the same call shape), so any recorded fill would be fabricated data;
    (2) substitute gate, SFTBY resolves but fails all three proposed coverage
    criteria (at least 90% one-minute bar coverage over 2 sessions, no gap
    over 2 minutes, at least USD 50M day notional), and its ADR-to-ordinary
    conversion basis is itself unverifiable since the ordinary-share feed
    404s, making it an unpriced second bet; (3) edge gate, even cost-free
    execution would be negative EV given a stale, weak-proxy catalyst with no
    SoftBank-specific idiosyncratic news. Any one of the three is sufficient;
    all three held. Revisit only if all of - a live feed on an
    exchange-listed instrument passing the coverage gate; fresh
    SoftBank-specific idiosyncratic news resetting the decay clock; and a
    30-plus-analog backtest showing P(continuation) at least 78% with a 95%
    CI lower bound above 65%, measured on an instrument that itself passes
    the coverage gate - are met.
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
  dissent: The tradability gate fires first and is dispositive, so the
    directional KOSPI-to-SoftBank thesis was never actually refuted by
    measurement - it was abandoned by concession. If 9984.T later resolves
    and the stock has rallied into 2026-07-29, the recorded outcome will read
    as a miss whose cause is unrecoverable - genuine signal weakness, or an
    edge that simply could not be priced. Three specific unresolved caveats -
    (1) SFTBY's tape was treated as authoritative evidence against momentum
    but non-authoritative as a tradable instrument, an unresolved asymmetry
    given its own thin coverage (47-50% of 1-minute bars); (2) the
    approximately 70-80%-already-priced-in figure rests on an assumed
    approximately 1-session decay half-life that was never estimated from
    data - a longer half-life would raise hypothetical gross EV, though not
    enough to clear the SFTBY-path breakeven; (3) this is the fourth
    confirmed venue coverage gap after NSE, Euronext Paris, and Euronext
    Paris again, now Tokyo - the provider's non-US-exchange coverage should
    be treated as absent by default and gated at scout time, not rediscovered
    per-debate.
  last_updated: '2026-07-25T15:48:37Z'
---

## Scouted 2026-07-23T09:13:03Z

## Researched 2026-07-25T15:48:37Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas independently converged on NO TRADE by round 2 (bull opened long on
9984.T as an AI-capex-supercycle proxy via SoftBank's Arm/Vision Fund exposure,
then fully conceded). Decisive fact, confirmed live: twelvedata 404s on
9984.T (Tokyo Stock Exchange) - the fourth confirmed structural non-US-venue
coverage gap after NSE and Euronext Paris tickers - verified against a
same-shape AAPL control call that succeeded. Quant tested the proposed US OTC
ADR substitute (SFTBY) live and found it resolves but is unexecutable (47-50%
one-minute bar coverage vs 100% for an SPY control, roughly USD 4.45M day
notional vs roughly USD 36.7B for SPY, estimated ~22% chance of a clean
two-leg fill) and that its own tape falsifies the momentum premise (closes
17.10 / 18.16 / 17.65 / 17.60 across 2026-07-20 to 07-23 - one spike then two
down closes, flat-to-down on the very day KOSPI printed +4.40%). Even on a
hypothetical clean 9984.T feed, net EV computed at -0.45% to -0.19% (weak
KOSPI-to-single-name proxy, ~70-80% of the move already priced in); on the
actually-tradable SFTBY path, -0.70% to -0.45%, against breakeven P(up) of
78-86% versus a measured 50-54% base rate. Synthesis: no_trade, confidence 93.
Full debate with citations in `transcript.md`.
