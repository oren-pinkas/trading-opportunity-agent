# Post-mortem — 2026-07-13-oil-iran-tension-surge

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Investigator (reconstruction)

Plan: short USO, entry 2026-07-14T13:35:00Z target $117.00, hedged exit
2026-07-20T14:30:00Z target $111.75. Thesis: USO was ~7% rich to its CL-tracking fair
value (decisive Round-2 fact: WTI fell -0.85% while USO rose +5.19% in the same
intraday window on 07-13), a geopolitical-rhetoric premium + ETF dislocation expected
to mean-revert toward the 07-20 horizon.

Actual fills (twelvedata):
- Entry 2026-07-14T13:35Z: **$120.98** (vs. planned $117.00 — already +3.4% above the
  synthesizer's reference spot of $117.89 taken the prior evening, and above the
  planned entry itself).
- Exit 2026-07-20T14:30Z: **$124.099998** (vs. planned $111.75).
- Realized: **-2.5789%, loss**, matched_hypothesis: no.

USO did not mean-revert at any point in the holding window — it kept rising, gaining
another ~+2.6% from entry to exit, on top of having already gapped up ~2.6% between
the debate's reference print and the actual entry fill the next day. The premium the
panel identified as a dislocation never compressed; if anything it (or the underlying
narrative) kept extending.

## Critic (root cause)

The quant's own scenario tree assigned P(continuation) = 25% and P(fade) = 50%,
explicitly naming the fade case as favored but not overwhelming. Continuation is what
happened. The transcript's own dissent flagged the surviving, unresolved risk clearly:
*"the entire short thesis rests on an inferred ~7% USO-to-NAV premium that was never
confirmed with actual creation/redemption or published-NAV data — only implied from a
divergence in a thin, choppy price series."* No persona ever obtained NAV/creation-
redemption data to confirm the divergence was a mechanical mispricing rather than
durable, flow-driven demand tracking a real (or continuing to escalate) geopolitical
event. The plan's own hard invalidation clause — "cover on any confirmed physical
disruption" — was never checked against reality during simulation, same structural gap
as the Prologis case: `simulate-plans`/`lib/pnl.py` has no path-dependent monitoring,
so even if a disruption headline did print mid-window, the sim would have held to the
fixed exit regardless.

Was it knowable at research time? The bear/quant case was well-argued and the base
rate (Abqaiq, Soleimani, 2025 Israel-Iran) genuinely favors fade over continuation —
this was a legitimate, non-negligent bet on a 50/25/... distribution that landed in
the less-likely tail. But the un-confirmed NAV-premium assumption was a real,
flagged, unresolved gap at research time, and the entry fill printing *outside* the
reference spot before the position even opened (a second data point in the same
direction as continuation) went unchecked.

**Root cause: wrong-assumption** — the core "ETF dislocation must mean-revert"
assumption was never verified against NAV/creation-redemption data and turned out to
be wrong; the divergence was durable, not mechanical, in this instance.

## Lessons

1. A USO-vs-CL (or any ETF-vs-underlying) price divergence is not by itself evidence
   for a mean-reversion fade — require confirmed NAV/creation-redemption data (not an
   inferred premium from a thin, choppy intraday series) before sizing a trade on the
   dislocation; absent that confirmation, treat the divergence as ambiguous between
   "mispricing to fade" and "real flow to follow."
2. Same structural gap as other 2026-07 fades: `simulate-plans` has no path-dependent
   stop-loss/invalidation-trigger enforcement — a plan's "hard invalidation: cover on
   confirmed disruption" is prose only. Do not assume conditional risk controls
   written into a plan will actually bound the simulated loss.
