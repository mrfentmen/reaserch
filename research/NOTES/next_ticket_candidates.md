# Next-ticket candidates (2026-09-18, worker-drafted for director approval)

No ticket is filed here — these are proposals only. Per protocol, no compute
may run until the director approves one and files it with its state machine.

---

## Candidate 1

TITLE: R011 restricted proof — fixed exponent pattern (3,3,3)

QUESTION: For the fixed pattern A^3+B^3−C^3=±1 with (A,B)=1, can an elementary
argument force a shared prime factor between some pair (i.e. class P)?

WHY DOES THIS MATTER: R017 exhausted general algebraic levers (every divisor
lever returned "consistent", pointing away from P). If even the smallest
nontrivial fixed pattern resists proof, that is evidence the phenomenon — if
true — needs deeper tools; if the pattern yields, we get the first conditional
theorem and a template for other patterns.

CURRENT EVIDENCE: C18/C24/C28/C36 — no class-C ±1 observed in any searched
scope (2.7M pairs, higher-exp tranche, full-cross-1000, tower tranche). C35
(L2a/L2b): natural gcd lemmas are proven but explicitly INSUFFICIENT for U.
R017_002 documents the failed general attacks (contrapositive, prime-divisor,
factorization, valuations, parity, exponent attacks).

HYPOTHESIS: Neutral-to-skeptical. Fixing (3,3,3) may let sum-of-cubes
factorization (A^3+B^3=(A+B)(A^2−AB+B^2)) interact with the ±1 condition in a
way the general-exponent attacks could not exploit.

WHAT WOULD FALSIFY IT: (a) A verified class-C triple with pattern (3,3,3)
(found by a small targeted search — would also wound C19's plausibility);
(b) a clean argument that the (3,3,3) algebra reduces to the same
"consistent-but-inconclusive" verdict as R017's general attacks.

CHEAPEST TEST / SUCCESS CONDITION: One focused algebra session against the
R017 attack checklist (no compute first): attempt the (3,3,3) closure; stop at
the first lever that reproduces R017's "consistent" dead end and document
exactly where it dies. SUCCESS = a written proof sketch surviving critic
review, or a documented kill (which itself becomes evidence about where proof
cannot come from). A targeted (3,3,3) class-C search is the cheap computational
falsifier if the algebra stalls.

---

## Candidate 2

TITLE: R011 bias audit — attack the sampling process, not the phenomenon

QUESTION: Is the "|off|=1 ⟹ P" observation an artifact of how the searches
generate and select triples (coprime-(A,B) prefilter, nearest-power rounding,
hunter logging filters)?

WHY DOES THIS MATTER: Every scope so far (R004/R011/R013/R015/R017) uses the
same family of generators: enumerate coprime (A,B) pairs, form S=A^x+B^y, take
the nearest e-th power. If that pipeline systematically suppresses or cannot
produce class-C ±1, the observation is about the generator, not the mathematics —
and no amount of wider searching within the same pipeline will ever falsify it.

CURRENT EVIDENCE: C16/C18/C28 — P-dominance across dataset, 2.7M-pair scope,
and full-cross-1000 census. All from the same generator family. C14 records
that the original near-miss file carried logging filters (ratio cuts etc.).
No independent-sampling census exists.

HYPOTHESIS: Skeptical. The generator's selection step (nearest perfect power to
S) may interact with divisibility structure to favor P-class hits; the
phenomenon may be partly or wholly a sampling artifact.

WHAT WOULD FALSIFY IT: A differently-sampled census (different enumeration
order, random sampling, no coprime prefilter with post-hoc classification) in
which P-dominance persists at the same strength — that would weaken the bias
hypothesis and strengthen the phenomenon. Conversely, finding class-C hits
under different sampling would kill the universality claim outright.

CHEAPEST TEST / SUCCESS CONDITION: Small independent census (bases ≤150, all
exp combos 3–7, both signs), implemented WITHOUT the coprime prefilter
(classify P/C/T post hoc), run once with sequential and once with randomized
enumeration; compare P-fractions. SUCCESS = a written bias report: measured
P-fractions per sampling scheme, explicit statement of which generator choices
move the numbers, and a verdict on whether the observation survives independent
sampling. Small scope only — no large compute without a follow-up ticket.

---

## Candidate 3

TITLE: Literature closure — bounded survey for a covering theorem (or a documented gap)

QUESTION: Does any published result (S-unit equation, Lebesgue–Nagell
x^2+D=y^n, Ramanujan–Nagell x^2+7=2^n, Mihăilescu/Catalan, Fermat–Catalan,
modular method) already cover a subcase of coprime A^x+B^y−C^z=±1, or is the
gap documented and clean?

WHY DOES THIS MATTER: C19's novelty field is "not assessable" partly because
the survey is bounded and non-English sources were not covered. If a theorem
already covers a subcase (e.g. an exponent pattern), that subcase moves to
KNOWN and the open question shrinks honestly. If the gap is documented
per-source with shape-mismatch reasons, C25's negative result hardens and
future workers stop re-asking the literature question.

CURRENT EVIDENCE: C25 — bounded survey (Pillai/Catalan/LRN/Fermat-Catalan/
modular) found no covering theorem; per-source shape-mismatch on record in
`LITERATURE/pillai_catalan_lrn_adjacency.md`. R017 mapped taxicab/sums-of-two-
cubes adjacency (explains duplicate namings, not P).

HYPOTHESIS: Neutral. The shape (three-term, pairwise-coprime-or-P, ±1, all
exponents ≥3) is unusual; absence of a covering theorem is likely but not
established for the newly named areas.

WHAT WOULD FALSIFY IT: Locating a theorem that covers a clean subcase (e.g.
S-unit finiteness applied to a fixed pattern, or a Lebesgue–Nagell-type result
biting on an exponent-2-adjacent case) — that would be a positive discovery
and would reclassify part of R011 as KNOWN.

CHEAPEST TEST / SUCCESS CONDITION: Strictly bounded, query-logged survey of a
named shortlist only: S-unit equation, Lebesgue–Nagell, Ramanujan–Nagell,
Mihăilescu, Fermat–Catalan conjecture status. For each: verdict (covers a
subcase / shape-mismatch / unclear) with one-line reason, queries on record.
SUCCESS = updated LITERATURE record with per-source verdicts — either a located
covering theorem or a documented gap. Hard stop after the shortlist; no
open-ended reading (that way lies C25 repeated forever).

---

## CRITIC REVIEW (attack each candidate)

### vs Candidate 1 (restricted proof)
- What makes it worthless: R017 already ran factorization-flavored attacks
  (R017_002) and every lever returned "consistent". A (3,3,3) attempt risks
  being R017 with narrower notation — same dead end, new file.
- Hidden assumption: that fixing exponents makes the divisibility close. C35
  already warns natural lemmas are insufficient for U; nothing says (3,3,3)
  escapes that.
- Cheapest way it fails: one algebra session reproducing the R017 "consistent"
  verdict at the first lever. Mitigation is built in: the ticket's cheapest
  test IS that kill — time-box it to a single session, document the death
  precisely, move on.

### vs Candidate 2 (bias audit)
- What makes it worthless: if the "independent" census reuses nearest-power
  selection, it is not independent at all — same pipeline, new seed, zero
  information. Also, P-dominance already survived R013's staged falsification,
  R015's full-cross-1000, and R017's tower attack: the bias hypothesis is
  already weakened by generator diversity.
- Hidden assumption: that P-dominance is fragile. The evidence says it is
  robust across scopes; the audit may just re-confirm at small scale.
- Cheapest way it fails: the small census finds 0 class-C again and
  P-fractions barely move — a weak negative. Still worth it ONLY because it is
  cheap and because a positive result (class-C under different sampling) would
  be decisive. Keep the scope tiny.

### vs Candidate 3 (literature closure)
- What makes it worthless: unbounded surveys expand to fill all available
  time; C25 already did the bounded pass and found nothing. A second survey
  that merely re-confirms "no covering theorem" adds little.
- Hidden assumption: that a relevant theorem exists and is findable in the
  surveyed (mostly English) literature. C19 already notes non-English sources
  unsurveyed — this ticket does not fix that either.
- Cheapest way it fails: the shortlist all show shape-mismatch within a day.
  Mitigation is built in: hard stop after the named shortlist, document the
  gap, do not keep reading. Value is in the documentation (stops future
  re-asks), not in expecting a positive hit.
