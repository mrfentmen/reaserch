# R017_001 — U as a pure mathematical proposition (no program terminology)

## Proposition U
ASSUME: integers A,B ≥ 2; exponents xa,xb,e ≥ 3; gcd(A,B) = 1.
Let S = A^xa + B^xb. Let C ≥ 2 be the integer minimizing |S − C^e|
(ties broken upward), and D = S − C^e.
EQUATION (near-miss condition): D ∈ {+1, −1}, i.e. A^xa + B^xb − C^e = ±1.
CONCLUSION (P as predicate): gcd(A,B,C) = 1 AND [prime p|A,C OR prime p|B,C].
(T is impossible here: it would need p|A,B, excluded by assumption.)

## Decomposition verdicts (each attacked in R017_002/003; summary)
- U1 (D=+1): no forcing found. U2 (D=−1): no forcing found. Signs behave symmetrically
  under all attacks below; dataset has both (+1:7/−1:4 at 1000-scale).
- U3 ((A,B)=1 given): used everywhere; forces T=∅ only (with C26 arithmetic version).
- U4/U5 (adding (A,C)=1 / (B,C)=1, i.e. assuming class C for contradiction): every
  lever below returns "consistent" — no contradiction derivable by the attempted means.
- U6 (all pairs coprime): the open case. Consistent on all axes; no impossibility proof found.
- U7 (exactly one shared pair): observed in all data (e.g. (7,19,21): only (7,21)=7;
  (566,823,904): only (566? ...) — never explained, merely observed.
- U8 (multiple shared pairs): observed too (9,10,12: (9,12)=3 AND (10,12)=2). No separate theory.
- U9/U10 (C parity): no forcing (both parities occur in hits: C=12 even, C=21 odd, C=150 even…).
- U11 (x=y... precisely xa=xb): hits exist with xa=xb (71³+138³) and without (3⁶+10³) — no split.
- U12 (pairwise different exponents): e.g. (7,4,19,3,21,3): all of 4,3,3... mixed; no split.
- U13/U14 (even/odd exponents): both parities throughout hits (e=3,4,6 all occur); e=4 hits?
  (none with |off|=1 in data — but R011_001 moduli show e=4 admits class-C residues, so absence is empirical).
- NET: decomposition yields NO provable subcase distinction. The only proven statements in
  this neighborhood are L1, C26, and the two (A·B,C∓1)=1 lemmas of R017_002 (all consistent
  with — never forcing — P).
