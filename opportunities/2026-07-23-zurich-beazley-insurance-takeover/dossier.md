---
id: 2026-07-23-zurich-beazley-insurance-takeover
title: Zurich Beazley takeover completion window
status: researched
created: '2026-07-23T09:13:03Z'
event:
  type: regulatory
  summary: Zurich's GBP 8.1bn all-cash takeover of Lloyd's insurer Beazley has EU
    antitrust clearance and shareholder approval but still awaits PRA, FCA, Lloyd's
    and FINMA sign-off before expected completion
  impact_window: '2026-09-30'
tickers:
- ZURN.SW
- BEZ.L
sources:
- title: Zurich files for EU approval on GBP 8.1 billion Beazley takeover
  url: https://www.insurancebusinessmag.com/uk/news/mergers-acquisitions/zurich-files-for-eu-approval-on-8-1-billion-beazley-takeover-578799.aspx
  accessed_at: '2026-07-23T09:13:03Z'
hypothesis:
  statement: "The Zurich/Beazley all-cash GBP 8.1bn takeover is a textbook merger-arb
    setup with EU antitrust and shareholder approval already secured, but it is not
    actionable here for two independent reasons. (1) Execution-data failure: the
    only legs with completion-tied payoff are unpriceable -- BEZ.L returns HTTP 404
    and ZURN.SW returns HTTP 404 on the price provider (confirmed structural gaps
    for the London Stock Exchange and SIX Swiss Exchange, not transient), no
    Beazley ADR exists in the security universe at all, and the sole resolving
    substitute ZURVY (Zurich US OTC ADR) has approximately 4 percent minute-bar
    coverage, roughly USD 7,000 notional per bar, and is the wrong (acquirer) leg
    with no completion-linked payoff. (2) Standalone-negative economics: even
    assuming perfect execution on a hypothetically priceable BEZ.L, the residual
    ~2.0 percent spread against a four-regulator gauntlet (PRA, FCA, Lloyd's
    Council/Franchise Board, FINMA) with revised probabilities of completion 0.68,
    delay 0.28, break 0.04 yields gross expected value of roughly +0.9 percent
    over a stretched ~3.2-month horizon, which net of ~0.70-0.80 percent all-in
    costs (UK stamp duty 0.50 percent fixed regardless of holding period,
    commission, half-spread) leaves roughly +0.15 percent, about 0.6 percent
    annualized -- below risk-free with a fat left tail. Correct residual posture:
    watch, do not trade."
  direction: none
  confidence: 88
plan:
  ticker: none
  action: none
  entry: none
  exit: none
  expected_profit_pct: null
research:
  dissent: "Bear and Quant disagree on how to allocate the four-regulator gauntlet
    risk inside the EV model -- a modeling disagreement, not a conclusion
    disagreement. Bear argues Lloyd's/FCA-specific friction history (capital
    adequacy review, Part VII-style transfer precedent, fit-and-proper checks) is
    a substantive break risk not captured by a generic risk-arb base rate, and
    puts break probability at 0.06-0.08, which would drive EV negative before
    costs. Quant rejects the reallocation to break probability, holding that Bear
    demonstrated process count and serial dependency rather than a substantive
    break thesis, and moved the mass into the delay bucket instead (completion
    0.80 to 0.68, delay 0.17 to 0.28, break only 0.03 to 0.04). Unresolved because
    it was never tested -- the deal is unpriceable, so neither model could be
    calibrated against a real spread. Both land at NO TRADE, and Bull conceded to
    both, making the panel 3-0."
  last_updated: '2026-07-26T08:20:00Z'
---

## Scouted 2026-07-23T09:13:03Z

## Researched 2026-07-26T08:20:00Z

Three-round panel debate (bull/bear/quant, synthesizer opus) unanimously converged
on NO TRADE. Both ZURN.SW (SIX Swiss Exchange) and BEZ.L (London Stock Exchange)
return HTTP 404 from the twelvedata price provider -- the 7th and 8th confirmed
structural venue gaps in this system, after NSE/India, Euronext Paris, Tokyo, Oslo
Bors, and Nasdaq Stockholm. The one resolving acquirer-side substitute, ZURVY
(Zurich's US OTC ADR), has only ~4% minute-bar coverage on its session (the thinnest
confirmed ADR yet, worse than Tokyo's ~47-50% and Stockholm's ~12%) and is the wrong
leg regardless, since merger-arb spread convergence lives in the target (Beazley),
which has no US-listed proxy at all. Independent of executability, the quant's EV
model on the (hypothetical) correct leg found the underlying edge economically dead
on its own terms: net EV of roughly +0.15% over a ~3.2-month stretched horizon
(~0.6% annualized) against a -22% break-case tail, driven by fixed UK stamp duty and
an elongated multi-regulator (PRA/FCA/Lloyd's/FINMA) completion timeline. Full
transcript in transcript.md. Recommend the scout-time venue+listing+coverage-quality
gate be extended to SIX Swiss Exchange and LSE, and to check both legs of a
merger-arb dossier for a completion-tied proxy, not just the acquirer.
