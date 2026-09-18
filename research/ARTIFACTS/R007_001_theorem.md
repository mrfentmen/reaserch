# THEOREM (R007) — correctness domain of quick.ts prime()

## Implementation (quick.ts lines 15–24)
Trial division: reject n<2; accept 2; reject even >2; accept 3; reject
multiples of 3; else test divisors i, i+2 for i = 5, 11, 17, … while i ≤ r,
r = Math.sqrt(n); return true iff none divide n.

## Contract
Input n must be an integer with 0 ≤ n < 2^53. Non-integers are OUT of contract
(demonstrated: TS prime(4.5) = true, prime(2.5) = true — wrong, but no call
site passes non-integers). n ≥ 2^53 is OUT of contract (representability).

## Theorem
Under the contract, prime() returns true iff n is prime.

## Proof
1. Exactness: every integer with |m| < 2^53 is exactly representable as a
   double; all of n, i, i+2, n%i, comparisons are exact. (Standard.)
2. sqrt-floor lemma: let r = fl(√n) (correctly rounded per IEEE-754/JS spec).
   For every integer p with 0 ≤ p ≤ √n, r ≥ p. Proof: |r − √n| ≤ u/2 where u
   is the ulp at r's binade. Then p − r ≤ √n − (√n − u/2) = u/2 < u. Both p
   (integer, and u ≤ 1 throughout √n < 2^27 since n < 2^53… more directly:
   p·(1/u) is an integer because 1/u is a power of two ≥ 1 for all
   √n ≥ 1… for √n < 1, i.e. n = 0, handled before the loop) and r are integer
   multiples of u, so p − r is a multiple of u strictly below u, hence ≤ 0.
   Therefore every integer p ≤ √n satisfies the loop condition i ≤ r when
   reached. (Extra iterations above √n are harmless.)
   Edge n = 0,1: rejected before loop. n = perfect square m²: √n = m exact.
3. Wheel coverage: every integer > 3 coprime to 6 is ≡ ±1 (mod 6) (one line:
   residues 0,2,3,4 share 2 or 3), and the loop tests exactly the pairs
   (5,7),(11,13),… i.e. all numbers ≡ 5,1 (mod 6) from 5 upward. Any composite
   n ≥ 5 has a prime divisor p ≤ √n; p = 2,3 caught by the early checks;
   p > 3 is ±1 mod 6 hence tested by step 2's reachability. If none divide,
   n is prime.
4. Call sites (gold lines 25–31, hunt 53–78): g is an even integer (loaded
   integer or start arg, += 2); p runs over odd integers 3..g/2; g−p integer.
   All prime() inputs are integers; Goldbach usage stays ~10^8 ≪ 2^53. ∎

## Empirical confirmation (not the proof, but the reproducer)
- Exhaustive mirror-vs-MR oracle on [0,100000]: 0 mismatches.
- Stratified 322 (Carmichaels, prime squares, frontier odds, 2^53−1, random): 0.
- 79,998 sqrt-floor adversarial checks (squares, squares±1 to 2^53): 0 mismatches.
- Wheel residue spot to 10^6: holds. TS edge run: 0,1→false; 2,3,5→true;
  4,9,25,27,49,561,1105,1729→false; 2147483647→true; all agree with oracle.
- Fractional misbehavior exhibited (4.5, 2.5 → true) to delimit the contract.

## Status implication
C10 upgrades PARTIAL → PROVEN for the contracted domain [0,2^53) integers,
with the integer-input assumption recorded and call-site-checked. Anything
outside the contract remains UNVERIFIED by design.
