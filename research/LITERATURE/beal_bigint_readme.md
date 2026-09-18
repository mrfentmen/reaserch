# Literature — GPU by-C^z search (beal_bigint) (R009 background, excerpt-level)

- TITLE: beal_bigint — GPU search for Beal counterexamples (by-C^z parametrization)
- AUTHORS: pscamillo (GitHub)
- YEAR: 2026 (repo live at search time)
- SOURCE: https://github.com/pscamillo/beal_bigint (README excerpts retrieved via search 2026-09-18; code NOT reviewed — all claims below are README-level)
- PROBLEM: empirical Beal verification at scale.
- RESULT (per README): 0 counterexamples; tier ladder to bound 500,000/exps 3–15 (13,377 s tier 9); 20,341 unique hits total; sub-linear wall scaling (~1.85–2.04× per C-doubling).
- METHOD (per README): outer iteration over (C,z) instead of (A,B) — no upper bound on A,B; BSGS-style hashing with dual Solinas primes; GPU hash table; full-precision GMP verification of coprime hits; M6 10M-skip tradeoff documented (~12% hit loss, 20× speedup).
- RELEVANCE: state of the art for brute-force Beal search; different parametrization from ours.
- KNOWN BOUND: C to 500,000 (per README table).
- RELATION TO C20: hash moduli are probabilistic data-structure moduli + GMP exact verify — same two-stage philosophy as danvk, not exact small-modulus guards; C20 not present at README level.
- RELATION TO C21: not mentioned at README level.
- RELATION TO OUR IMPLEMENTATION: different parametrization + orders larger scale; our ≤600 by-base benchmark is redundant as search.
- NOVELTY IMPLICATION: none for us beyond "not present at README level"; code-level comparison NOT performed (stated limitation).
- NOTES: excerpt-level only; no code claims made.
