# Literature — Norvig Beal search (2000) (R009 background)

- TITLE: Beal's Conjecture: A Search for Counterexamples (obsolete page, historical)
- AUTHORS: Peter Norvig
- YEAR: 2000 (Python 1.5, 400 MHz PC era)
- SOURCE: https://www.norvig.com/beal2000.html (fetched full text 2026-09-18)
- PROBLEM: brute-force Beal counterexample search.
- RESULT: no counterexamples; table to bases 250,000/exps 7 (1323 h) etc.; method: exact hash table of z^r values + exact lookup of x^m+y^n sums; gcd(x,y)==1 skip (same L1 prefilter); self-check by removing gcd test (recovers hand-verifiable non-coprime solutions).
- METHOD: EXACT table lookup. NO modular prefilter implemented — page explicitly lists modular arithmetic (mod 2^64 or several large primes, verify candidates after) as FUTURE "Next Steps" work.
- RELEVANCE: closest architectural ancestor of our hunter (by-base + exact check + gcd skip).
- KNOWN BOUND: per table, e.g. all variables ≤1000 region covered at high cost (933 h for 10000×100).
- RELATION TO C20: no residue/modular prefilter in the posted code — C20's exact small-modulus guard is not present here.
- RELATION TO C21: no exponent-gcd skip in posted code (all m,n,r combos tested).
- RELATION TO OUR IMPLEMENTATION: our hunter is the same family (by-base, exact iroot instead of table lookup); our validated range (≤600 toy) far below.
- NOVELTY IMPLICATION: supports C20/C21-implementation absence in THIS source; says nothing beyond it.
- NOTES: read in full; no tables or bounds invented.
