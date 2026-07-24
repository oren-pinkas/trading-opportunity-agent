# Research Debate Transcript — RHI Q2 2026 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run at 2026-07-24T01:45Z.

## Event & verified price data

- RHI reported Q2 2026 earnings 2026-07-23.
- Dossier guidance text is corrupted by a shell-substitution bug (dollar signs/digits
  mangled). Best reconstruction: revenue guidance ~USD 1.275-1.375B, EPS guidance
  ~USD 1.20-1.30. Treated as low-confidence throughout the debate.
- Verified prices (`toa price RHI <ts> --provider twelvedata`):
  - 2026-07-22T19:59Z (prior close): $40.805
  - 2026-07-23T13:30Z (open, earnings day): $41.20
  - 2026-07-23T19:59Z (close, earnings day): $37.985
  - Net move: -7.8% intraday (open-to-close), -6.9% close-to-close.
- Source: "Does Robert Half (RHI) Capture Durable Value from Shifting Labor-Market
  Optimism in Staffing Demand?" — sahmcapital.com, accessed 2026-07-22.

## Round 1 — Independent research

### Bull
RHI opened flat ($41.20 vs $40.805 prior close), then slid all day to $37.985 — a
"digest the call, then sell" pattern implying the earnings call/guidance drove selling,
not the headline print. A -6.9% single-day move on a high-beta staffing name is large
but not extreme; staffing names often retrace 20-40% of an initial post-earnings drop
within 3-5 sessions absent a fresh confirmed negative catalyst. Proposed LONG RHI
mean-reversion bounce: entry 2026-07-24T13:30-15:00Z, exit 2026-07-28/29 ~19:59Z.
Confidence ~40/100; prefers a call spread/long calls over naked long given confidence
and the corrupted-guidance blind spot. Wants: clean guidance vs. consensus, earnings-call
demand commentary, confirmation of whether $37.985 is a new 52-week low.

### Bear
Flat-open-then-slide reads as a guide-down-on-the-call pattern. Staffing is a
leading/coincident labor-market indicator; RHI is in a multi-quarter down-cycle; the
source article's "durable value" question reads as answered "no" by the price action.
Risk case: gap-and-crap continuation (analyst downgrades typically lag 1-3 days, not yet
priced) vs. capitulation/overreaction bounce. Proposed NO-TRADE; if forced, only a small
defined-risk put spread, entry 2026-07-24T13:30Z, exit by 2026-07-28T20:00Z. Falsifiers:
guidance reaffirmed/modest and drop transitory; analyst notes within 48h calling it
"overdone" with targets held/raised; peers (MAN, ASGN, KFRC) not confirming sector-wide
deterioration.

### Quant
No RHI-specific sample; reasoning from general PEAD literature + staffing cyclicality.
Base-rate split from $37.985: continuation-down ~40%, flat/chop ~30%, reversion-bounce
~30% — near coin-flip, worsened by corrupted guidance digits. EV math (defined-risk,
entry ~$38.0, 1R≈2.5%≈$0.95, round-trip costs ≈0.2R): continuation short 1.5R/1R,
P(win)=0.42 → net EV -0.15R (negative); reversion long same structure, P(win)=0.38 →
net EV -0.25R (negative). Both stay negative even flexing P(win) ±5%. Recommendation:
NO-TRADE — pre-earnings window closed, move already realized, confidence well under 45,
refuses to size on corrupted guidance digits. Revisit only if the 2026-07-24 open gaps
>3% from $37.985, resetting risk/reward; then defined-risk options only, exits at
19:59:00Z.

## Round 2 — Rebuttal

### Bull
Concedes bear's "flat open then hard deterioration favors guide-down" diagnostic and
quant's point that the cheap/high-edge part of any reversion trade (front-running the
reaction) is already gone. Still argues $37.985 closing at/near the lows looks like a
saturation-selling signature, not a controlled distribution. Revises DOWN: confidence
40→30/100. New structure: do not enter blind at 13:30Z — wait 30-60 min to confirm no
follow-through gap-down and check peer tape (MAN/ASGN/KFRC); only if RHI holds within
~1% of $37.985 and peers aren't cracking, take a small defined-risk call spread, same
exit window. If it gaps down again or peers are red, stands down — converging with
bear/quant's no-trade line in that scenario.

### Bear
Holds NO-TRADE. Calls the bull's "20-40% retrace" claim unsupported speculation — no
source, no sample definition, and it ignores that a call-driven (digested-guidance)
selloff historically retraces less than a headline-driven gap. On quant's EV math: agrees
it validates caution, but argues the 30% reversion-bounce weight is if anything slightly
optimistic given the "digest then sell" institutional-distribution signature — not
enough to flip negative EV positive. Falsifiers unchanged: 2+ downgrades/target cuts
within 48h citing guidance deterioration; confirmed new 52-week-low breach on
above-average volume; reconstructed clean guidance showing an actual cut vs. consensus.

### Quant
Stress-tests both: bull's retrace claim is asserted not evidenced, and its mechanism (if
real) is already inside the 30% reversion weight — doesn't move the numbers. Bear's
"downgrade lag" is real but not incremental — already embedded in the 40% continuation
weight (would double-count); can't front-run a specific downgrade. Re-defends EV
unchanged: continuation short -0.15R, reversion long -0.25R, both negative even flexing
±5%. Corrupted guidance data widens error bars (lowers conviction), doesn't create a
positive-EV side. Verdict: REINFORCES NO-TRADE. Unchanged trigger: revisit only if the
2026-07-24 open gaps >3% from $37.985; defined-risk options only, hard exit 19:59:00Z.

## Round 3 — Synthesis (neutral, opus)

**hypothesis**: RHI's -6.9% post-earnings selloff shows a flat-open-then-all-day-slide
"digest-the-call-then-sell" signature consistent with a guidance-driven institutional
distribution, not a headline overreaction; with the tradeable move already realized,
corrupted guidance data blocking conviction, and both defined-risk directions carrying
negative expected value, no positive-EV edge exists into the 2026-07-24 session.
Direction: no-trade. Confidence: 68/100.

**plan**: Stand aside — no position at the 2026-07-24T13:30Z open. This reflects the
two-thirds panel consensus (bear + quant), backed by explicit negative-EV math
(continuation short -0.15R, reversion long -0.25R, both negative under ±5% P(win) flex);
the bull only offered a small, conditional, confirmation-dependent trade at reduced
30/100 confidence. Monitoring/conditional re-entry trigger (informational only, not an
active order): if the 2026-07-24 open gaps >3% from $37.985 (below ~$36.85 or above
~$39.12) AND peers MAN/ASGN/KFRC confirm direction rather than diverging, a small
defined-risk options structure (call spread on a reversion setup, put spread on a
continuation setup) could be considered, entry ~2026-07-24T14:00Z (after a 30-60 min
confirmation window), hard exit 2026-07-28T19:59Z, ~+2.5% expected profit on a small
size — skipped entirely if the gap threshold or peer confirmation doesn't fire.

**dissent**: Bull vs. bear/quant on whether the $37.985 close-at-the-lows is a
saturation/capitulation-selling signature seeding a reversion bounce (bull), or an
institutional-distribution "digest-then-sell" signature with below-average reversion
odds (bear, arguing quant's 30% reversion weight is if anything too generous).
Unresolved because no one could confirm whether an actual guidance cut vs. consensus
occurred (corrupted dossier digits). Bull's core evidentiary claim — staffing names
retrace 20-40% of the drop within 3-5 sessions — was challenged by both bear and quant as
asserted/unsourced and, per quant, already absorbed inside the existing 30% reversion
weight, so it never moved the EV math.
