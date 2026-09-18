# R011-BIAS-001 — CRITIC PASS (2026-09-18)

The researcher claims: P-dominance survived independent sampling (11 unique |off|=1 equations in
the ≤150 box, all P, 0 C, 0 T, including hunter-excluded regions). Attacks:

1. SHARED EQUATION SHAPE. All three generators still test "sum of two powers vs one power" —
   the same shape as the hunter. Both signs are covered (|S−C^e|=1 includes C^e>S), but no
   genuinely different family (four-term, difference-of-powers on the sum side, C^z as a summand)
   was probed. The independence is in SAMPLING, not in equation shape. Scope of the claim must
   say exactly that.
2. B AND C ARE NOT INDEPENDENT EVIDENCE. Same 261,530-sum universe; they differ only in traversal
   order and agree exactly (as they must — both are full passes). They establish order-robustness,
   not sampling-robustness. The independent legs are A (random, with replacement) vs B/C (census).
3. SMALL SAMPLE FOR A "DOMINANCE" CLAIM. 11 unique equations. If the true class-C rate among
   |off|=1 were 5%, P(0 C in 11) ≈ 57% — this probe cannot rule that out. It STRENGTHENS the
   pattern (survival in previously unsampled regions) but is not a universality argument, and was
   never designed to be one.
4. SCOPE PARITY WITH THE HUNTER. Exponents 3–7 = the hunter's range; R013 already probed to
   exp 14 and R017 attacked with towers. This ticket adds nothing on the exponent axis; its
   novelty is sampling-order + filter-removal only. Stated honestly in the ticket; no inflation.
5. GenA WEIGHTING QUIRK. (A,B) uniform over bases with x,y uniform over exps weights power VALUES
   by naming multiplicity (e.g. 64 = 2⁶ = 4³ = 8²… within 3..7: 2⁶,4³,8^? — two namings get double
   weight). Documented; does not touch the class verdict (classification is post-hoc on exact
   arithmetic, no gcd-branching before hit detection — code paths for P vs C hits are identical,
   so the generators cannot be biased TOWARD P except via the |off|=1 condition itself, which is
   the phenomenon under test).
6. 0 T IS NOT A FINDING. C26 proved T=∅ for |off|=1 arithmetically; 0 T is a consistency check.
   Had T>0 appeared it would have contradicted a proof → bug indicator. Recorded as check, not evidence.
7. DEDUP AMBIGUITY. Reported both (S,C,e)-hits (13) and unique integer equations (11); class split
   P11/C0/T0 identical either way. No conclusion depends on the counting convention.
8. FLOAT BOUND IN TABLE SIZING. cmax = round(maxS^(1/e)) + 4 uses float roots; absolute float error
   at these magnitudes (~1e-11) is 15 orders below the +4 margin — safe. Corroborated by 0 guard
   anomalies and the planted-hit rediscovery. Not a risk, recorded for the verifier.
9. WHAT WOULD HAVE FALSIFIED THE "SURVIVES" READING. One verified class-C equation from any
   generator — none appeared. The probe was capable of finding one (no gcd filter anywhere in the
   hit path; 38.5% of GenA draws and 8/13 GenB hits lived in hunter-excluded gcd(A,B)>1 territory).
10. RESIDUAL RISK: SCOPE. Bases ≤150 is small; the ≤150 box could be P-typical while larger boxes
    differ (R015's 2..1000 census says otherwise for ITS shape, but that was hunter-shaped sampling).
    A wider independent census is the natural follow-up ticket, NOT this one.

CRITIC'S VERDICT: the researcher's result stands as REPRODUCIBLE COMPUTATIONAL EVIDENCE —
P-dominance survives independent sampling in the ≤150 box, including both hunter-excluded regions,
with 0 class-C. No flaw found that invalidates the per-generator tables. The result must NOT be
used to upgrade C19 (finite scope; rule). Recommended: UNDER_REVIEW; verifier pass (independent
reimplementation or director review) before any ledger evidence-pointer change beyond the
no-upgrade citation already recorded.
