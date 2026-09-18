# Literature — danvk Beal search (2006+) (R009 background)

- TITLE: Beal's Conjecture (blog writeup + comments)
- AUTHORS: Dan Vanderkam (danvk)
- YEAR: ~2006–2007 (comments to 2014)
- SOURCE: https://www.danvk.org/wp/beals-conjecture/ (fetched full text 2026-09-18, incl. comment thread)
- PROBLEM: extend Norvig's search on 64-bit hardware.
- RESULT: no counterexamples; max_base=max_pow=1000 in ~17 h; result stated as "Beal true for all variables up to 1,000".
- METHOD: hash table of z^r + PROBABILISTIC modular prefilter with large 32-bit primes p1=2^32−5, p2=2^32−17 (false positives possible; survivors verified with exact arithmetic); x<y symmetry; gcd(x,y)==1 skip (same L1 family); Thomas Wang hash. Measured: 115,555,328 combos → 545 (mod p1) → 0 (mod p2) at 200×100; 302G combos → 15,683 survivors → 0 at 1000×1000. Correctness argued by filter-off reproduction of 809 known non-coprime solutions.
- RELEVANCE: the directly comparable filtering work — large-modulus probabilistic vs our small-modulus exact.
- KNOWN BOUND: 1000×1000 exact-verified (survivors).
- RELATION TO C20: C20 (complete small-modulus residue tables as PROVEN pre-iroot guards, zero false positives) is a DIFFERENT filter philosophy; not present here. Commenter fwjmath claims composite moduli cut 30% in his implementation (experimental repo fwjmath/beal-optimize, fetched 2026-09-18: skeleton only, no technical content retrievable) — modulus-choice tuning exists as folk engineering; detail UNVERIFIED.
- RELATION TO C21: not implemented; page text suggests "consider only exponents prime or power of two... analogous to FLT" as a FUTURE idea only.
- RELATION TO OUR IMPLEMENTATION: strictly stronger engineering at far larger scale; our Python-only ≤600 benchmark is not competitive as search.
- NOVELTY IMPLICATION: C20-as-exact-guard and C21-as-code not found HERE; probabilistic large-modulus filtering predates and outperforms ours in raw power.
- NOTES: read in full; comment claims (proofs, fwjmath figures) NOT endorsed — recorded as unverified thread content.
