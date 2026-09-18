# RULE FLT-gcd — exponent-gcd elimination (R002, PROVEN necessary condition)

- RULE: For candidate with base-exponents (x,y) and trial exponent e, let
  d = gcd(x,y,e). If d > 2, skip the exact check.
- MATHEMATICAL STATEMENT: A^x+B^y=C^e with d|x,y,e, d ≥ 3, is impossible.
- ASSUMPTIONS: A,B,C positive integers (Beal scope); FLT (lemma below).
- PROOF: write U=A^{x/d}, V=B^{y/d}, W=C^{e/d} (integers since d divides each
  exponent). Then U^d+V^d=W^d with d ≥ 3, contradicting Fermat's Last Theorem
  (no positive-integer solutions for exponent > 2). ∎ Subcase (4,4,4) already
  follows from Fermat's own n=4 proof; general case via Wiles.
- COUNTEREXAMPLE SEARCH / SMALL TEST: covered by R002_003 safety equality
  (24=24, planted survive) — FLT-pruned combos (e.g. (3,3,3),(3,3,6),(4,4,4),
  11 total) correctly never coincide with detections.
- REMOVAL RATE: 11/125 (x,y,e) combos (8.8%); measured check reduction
  100% → 91.2% on the benchmark domain. Runtime effect: 21.5 s → 18.5 s
  (1.16×) — near-zero overhead (precomputed 5×5 table, small-int gcds).
- IMPLEMENTATION: `ALLOW_E` table in R002_002_prune.py.
- INDEPENDENT VALIDATION: Bun recount confirms exactly the 11 combos:
  (3,3,3),(3,3,6),(3,6,3),(3,6,6),(4,4,4),(5,5,5),(6,3,3),(6,3,6),(6,6,3),
  (6,6,6),(7,7,7).
- LITERATURE STATUS: FLT — Wiles 1994/released-1995 (see
  `LITERATURE/flt_wiles_wikipedia.md`, tertiary record); n=4 Fermat.
- NOVELTY STATUS: REPRODUCTION (application of known theorem as a pruner).
- CANONICAL STATUS: PROVEN (conditional on FLT lemma, cited).
