---
id: 2026-07-13-viatris-contraceptive-patch-pdufa
title: Viatris PDUFA decision on MR-100A-01 weekly contraceptive patch
status: researched
created: '2026-07-13T15:12:42Z'
event:
  type: regulatory
  summary: FDA target action date July 30, 2026 for Viatris' low-dose weekly transdermal
    contraceptive patch
  impact_window: '2026-07-30'
tickers:
- VTRS
sources:
- title: MR-100A-01 Weekly Contraceptive Patch Data Presented at ACOG 2026 Ahead of
    FDA Decision
  url: https://www.patientcareonline.com/view/mr-100a-01-weekly-contraceptive-patch-data-presented-at-acog-2026-ahead-of-fda-decision
  accessed_at: '2026-07-13T15:12:42Z'
hypothesis:
  statement: The panel converged on no-trade. Approval is probable (Bayesian-updated
    posterior around 0.82 after weighing the Twirla CMC/manufacturing precedent against
    Viatris' in-house manufacturing track record), but the expected move is too small
    to matter -- VTRS is a roughly USD 19B-cap company where this asset is about 2-3
    percent of revenue, the stock is already near 94 percent of its 52-week high after
    an 11.6 percent 30-day run, and much of any approval reaction is likely pre-priced.
    Net EV on a directional long is only about +0.49 percent after costs and turns
    negative if the true approval move is closer to +1.5 percent, a plausible outcome
    given the run-up. A short is not justified either -- the approval probability sits
    comfortably above the roughly 0.69-0.76 short break-even, and no hard CMC/manufacturing
    evidence (no Form 483, no confirmed prior CRL on this molecule) was found to push
    the odds lower. No trade.
  direction: no_trade
  confidence: 66
plan:
  ticker: VTRS
  action: pass
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
  dissent: The bear and the quant never converged on how far below the FDA-wide base
    rate the approval probability should be adjusted for this sub-class. The bear's
    strongest surviving argument is that the only close class analog, Twirla, went
    0-for-2 on first-pass approval over roughly seven years, both times on CMC/manufacturing
    grounds, and that this alone should pull the probability well below a generic 0.85
    prior. The quant's counter is that Twirla's failures were idiosyncratic to a specific
    under-resourced manufacturer (Agile/Corium), not a hard class-wide safety signal,
    so the correct Bayesian update is a modest haircut (0.85 to somewhere between 0.69
    and 0.82 depending on the likelihood ratio assumed), partly offset by Viatris'
    own in-house manufacturing track record. Both agree the adjustment should be downward;
    they disagree by roughly 13 probability points on magnitude, and that gap is exactly
    where the no-trade/short-lean boundary lives. Neither side could resolve it because
    the one fact that would settle it -- whether MR-100A-01's actual manufacturing
    site has a clean recent FDA inspection record -- was never obtained. Data not checked
    that a pre-2026-07-30 revisit should verify -- options-implied volatility/straddle
    pricing around the PDUFA date, and manufacturing-site/Form 483 inspection status
    for MR-100A-01.
  last_updated: '2026-07-16T06:50:05Z'
---

## Scouted 2026-07-13T15:12:42Z

## Researched 2026-07-16T06:50:05Z — NO TRADE

Three-round panel debate (bull/bear/quant, synthesized by opus). All three personas
converged on PASS by round 2: the bull cut sizing and confidence (58 to 45) after
conceding the bear's Twirla CMC/manufacturing precedent addressed a failure mode the
bull's efficacy-focused evidence never touched; the bear held firm and inverted the
bull's Xulane point (Xulane is itself a generic Ortho Evra, the patch with a black-box
VTE warning); the quant ran an explicit Bayesian update landing at approval probability
around 0.82 and net EV of only about +0.49 percent after costs, thinner than round 1's
+0.96 percent, and ruled out a short since no persona could produce hard evidence
(a Form 483 or a confirmed prior CRL on this molecule) to push the odds low enough.
Verdict: no_trade, confidence 66. Full transcript in `transcript.md`. Central dissent:
whether the approval probability should be haircut further for the sub-class's 0-for-2
first-pass approval record (Twirla) -- unresolved because manufacturing-site inspection
status was never checked. Flagged for a pre-2026-07-30 revisit if that data surfaces.
