# R002 Step 1 — exact Beal search space (reconstructed from beal.ts, re-read 2026-09-18)

Source: `research prize/beal.ts` lines 60–112. No other implementation exists in repo.

## Definitions
- Inputs: max, emax, shard, shards, bmin (defaults 200, 5, 0, 1, 2).
- Power list P = { (v,b,e) : bmin ≤ b ≤ max, b % shards == shard, 3 ≤ e ≤ emax,
  v = b^e }, sorted ascending by v (line 68; sort is by value only, unstable
  order among equal values — duplicates like 64=8^2… note exps ≥3 so e.g.
  64 = 4^3 = 8^2(excluded) = 2^6: entries (4,3),(2,6) both present as DISTINCT
  list elements with equal v).
- Candidate pairs: all (i,j) with 0 ≤ i ≤ j < |P| (lines 72–75; ordered by
  VALUE, i.e. unordered value-pairs with replacement; same-(b) different-e
  entries included as separate elements).
- Coprimality prefilter (line 78): skip unless gcd(bi,bj) == 1. (Proven safe
  by L1: a shared prime would divide C too, so skipped pairs cannot be
  counterexamples. Note: they also cannot be VALID Beal solutions with
  triple-gcd 1 — consistent.)
- Per surviving pair: S = vi+vj; for each e in 3..emax (line 84): f =
  floorRoot(S,e) (exact binary search); if f^e == S: let c = f (fits double
  exactly in stated scopes); report FOUND unless gcd(bi,c),gcd(bj,c) ≠ 1
  (line 88 — pairwise check, valid by L1 given the equation holds).
- Near-miss logging (lines 94–101): absolute |S − nearest e-th power| ≤ 1000,
  S > 10^6, ratio first.v·1000 > S. Heuristic only; excluded from baseline
  timing (I/O-dominated, mathematically irrelevant).

## Normalization / symmetries / duplicates
- Ordering: pairs ordered by value (i≤j), NOT by base — each unordered pair of
  LIST ELEMENTS visited once. Duplicate values (2^6=4^3) yield multiple
  elements; pairs among them are skipped anyway (same base, gcd≠1) except
  cross-base value collisions (e.g. 2^9=8^3? exps≥3: 2^9 vs 8^3=512: bases
  2,8 gcd 2≠1 skip; genuine cross-base collisions like 4^3=2^6 share base
  factors… a value collision with COPRIME bases, e.g. 12^2-type, needs
  a^e=b^f coprime ⟹ a=b=1 by unique factorization — impossible for bases≥2.
  Hence equal-v coprime-base pairs do not exist; value-ordering ≡ base-pair
  coverage modulo the (b,e)-naming multiplicity. The (pair,e)-check loop may
  still test the same integer S twice under different namings — pure overhead.)
- No exponent normalization (e.g. no gcd(x,y,e) reduction), no modular
  prefilter, no parity filter. Cost per (pair,e): one exact iroot (~bitlen
  big-int pow iterations) + O(1) big-pow verifications.

## Current filters (all proven-safe): coprimality prefilter only.
## Current coverage (design): intra-shard value-pairs only (C1 FALSE as full
  bound; R001 open). R002 does NOT change coverage — only per-check cost and
  check count via necessary conditions.
## Cost model: #iroot-calls = #{coprime pairs} × #{e values}; iroot dominates.
