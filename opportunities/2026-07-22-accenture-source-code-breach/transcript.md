# Debate transcript: 2026-07-22-accenture-source-code-breach

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Models: bull=sonnet, bear=sonnet, quant=opus, synthesizer=opus.
Debate run: 2026-07-23T04:30:04Z.

## Dossier facts in scope

- Event: Accenture confirmed a breach after a threat actor claimed exfiltration of 35GB of
  source code and other data, raising client-disclosure and liability questions.
- Ticker: ACN. Event type: regulatory. Impact window: 2026-08-15.
- Source: "Hacked, leaked, and held for ransom: The worst breaches of 2026 so far" —
  https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/
  (published 2026-07-07, accessed 2026-07-22).

## Relevant lessons injected

1. [PLD/regulatory] Sub-~0.15 signal-to-noise linear-EV fades are not durable edges; simulate-plans
   does not enforce path-dependent stop-losses.
2. [PLD/regulatory] An entry fill printing outside the planned band is an early falsification signal.
3. [NYAX/regulatory] Test-query the real price provider for exact entry/exit timestamps before
   finalizing a plan, or it resolves as an uninformative neutral.
4. [CZR/regulatory] Validate every entry/exit timestamp falls within an open trading session; roll
   non-trading dates forward.
5. [CZR/regulatory] Never map a corporate/legal calendar date directly onto an execution timestamp.

## Round 1 — Independent research

**Bull (confidence 55/100).** Long ACN, buy-the-dip / fade-the-overreaction. Confirmed breaches at
large diversified consulting/IT-services firms typically produce an initial overreaction followed
by re-rating once no material client-contract loss or regulatory fine materializes. Proposed entry
near the nearest open session after 2026-07-23, exit near the impact window rolled to the next open
session (Mon 2026-08-17, since 2026-08-15 is a Saturday). Wanted real price data test-queried before
finalizing (lesson 3).

**Bear (confidence 15/100 in the bull thesis).** No confirmed materiality: single secondary source
(TechCrunch aggregation), no client list disclosed, no regulatory filing referenced. Source-code
theft (vs. client PII) rarely moves an IT-services stock's fundamentals. Zero price-reaction data
exists in the dossier to confirm any overreaction happened. News is already 16 days stale by
dossier-access date (published 2026-07-07, accessed 2026-07-22) — a timeline mismatch against the
2026-08-15 impact window and against typical reaction decay. Kill condition: no discernible move on
disclosure.

**Quant (confidence 72/100 in a NO TRADE verdict).** Base rate for cyber-breach disclosures on
large-cap ($150B+) diversified IT-services names, absent a guidance cut, is near-noise: median 1-day
abnormal move -0.5% to -1.5%, ~60-70% mean-revert within 5-15 trading days. Since the dossier is
already 16 days post-disclosure, most of any reaction is already in the tape. Explicit EV:
P(fresh >2% down-move by 2026-08-15) = 20%, P(no material move) = 65%, P(upside surprise) = 15%,
conditional magnitude ≈3%, decay half-life 4-6 trading days. Net EV ≈ +0.03% gross − ~0.40% costs
≈ **-0.37%**, negative after costs. Verdict: NO TRADE / PASS.

## Round 2 — Rebuttal

**Bull → 25/100.** Conceded the quant's EV math is the strongest argument on the table and conceded
there is no evidence an overreaction ever happened (no price series in dossier) — "buy the dip" was
solving a problem that may not exist. Accepted the staleness objection (16 days vs. a 4-6 day
half-life). Retained only a weak residual idea: second-order tail risk (client contract reviews,
security-audit costs, bid-reputation drag) that could surface a slower catalyst into 2026-08-15,
explicitly downgraded from a directional trade to "small optionality."

**Bear → 8/100 (in bull thesis).** Argued the bull's own thesis is now internally incoherent: you
cannot fade an overreaction that, per the quant's own base rate, should already be 60-70% reverted
by day 16 — the bull is "chasing a ghost," not buying a dip. Negative EV is "the real kill shot" even
granting the directional logic. Materiality gaps (single source, no filing, no client list) remain
unaddressed. Would need: a confirmed >2% unreverted move, a second independent source or regulatory
filing, and an EV that clears costs with margin — none present.

**Quant → 74/100 (NO TRADE, up from 72).** Neither rebuttal moved the model. The bull's own
concession that entry must occur 16+ days post-disclosure — after most mean-reversion should be
complete — confirms the trade is structurally too late. The bear's materiality gaps corroborate the
base-rate read. EV unchanged at ≈ -0.37% after costs. Final verdict: NO TRADE / PASS.

## Round 3 — Synthesis

**Hypothesis:** The Accenture (ACN) source-code breach is not a tradeable edge: there is no
confirmed materiality, only a single secondary source, and the dossier was accessed 16 days
post-disclosure — well beyond the 4-6 day reaction half-life — leaving negative expected value
(≈-0.37% after costs) with most of any base-rate move already reverted in the tape.
Direction: neutral. Confidence (in the no-trade call): **80/100**.

**Plan:** No trade. Ticker ACN, action `no_trade`, entry/exit/expected_profit_pct: null.

**Dissent (for the post-mortem):** The only surviving disagreement is the bull's residual tail-risk
optionality — that second-order client-contract-review or reputational drag could still surface a
fresh downward catalyst into the 2026-08-15 window, which the base-rate EV model (built on typical
4-6 day reaction decay) would systematically under-weight if this breach proves atypical in
materiality. The panel judged this too speculative and unfunded by evidence to trade, but it is the
scenario a post-mortem should check against if ACN moves materially before 2026-08-15.

**Synthesis narrative:** The panel converged cleanly on NO TRADE, with confidence rising across all
three seats over the debate. The decisive argument was the quant's expected-value model: a net EV of
roughly -0.37% after costs, anchored in a base rate where cyber-breach disclosures on large
diversified IT-services names produce only near-noise moves that mean-revert 60-70% within 5-15
days. The timing compounds the problem — the dossier was accessed 16 days after disclosure, far past
the typical 4-6 day reaction half-life, so any move worth fading has almost certainly already
reverted. The bull recognized this directly, cutting confidence from 55 to 25 and conceding there is
no evidence of an overreaction to fade in the first place, since the dossier contains no price
series. The bear reinforced the structural incoherence: you cannot fade a move that should already
be reverted, and materiality remains unconfirmed with only a single secondary source and no
regulatory filing or client list. All three seats agreed the setup is structurally too late and too
thinly evidenced to clear costs. The lone residual is the bull's weak tail-risk optionality into the
2026-08-15 window — retained in the dissent note, but judged too speculative to fund a position.
