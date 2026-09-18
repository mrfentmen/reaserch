# R011 Steps 1–4 — exact definitions from beal.ts:72–101 (re-read 2026-09-18 cycle)

## Primitives (code → math)
- Power list P sorted by VALUE; pair (first,second) =: ((A,xa),(B,xb)) with A^xa ≤ B^xb.
- Line 78 FORCES throughout the near-miss file: gcd(A,B) = 1. (Pairs violating it
  `continue` before any logging.)
- S := A^xa + B^xb (exact bigint, line 83). f := ⌊S^{1/e}⌋ exact (floorRoot).
- low := S − f^e (≥ 0); high := (f+1)^e − S (> 0 strictly).
- d := low if low < high else −high (tie low==high goes UPPER, C=f+1).
- Logged (line 98) iff 0 < |d| ≤ 1000 AND S > 10^6 AND A^xa·1000 > S
  (i.e. B^xb/A^xa < 999, value-ratio bound). Line format:
  "A^xa + B^xb = S near C^e off by d" with C := f (d≥0) or f+1 (d<0).
- IDENTITY (exact, both branches): S − C^e = d. Hence |off|=1 ⟺
  **A^xa + B^xb − C^e = ±1** with C^e the nearest e-th power (ties up).

## Classes as exact propositions (no labels-as-math)
- P := [gcd(A,B,C)=1] ∧ [gcd(A,B)>1 ∨ gcd(A,C)>1 ∨ gcd(B,C)>1].
  In-file (gcd(A,B)=1 forced): P ⟺ triple-1 ∧ (gcd(A,C)>1 ∨ gcd(B,C)>1).
- C := pairwise coprime (all three gcds = 1; implies triple-1).
- T := gcd(A,B,C) > 1.
- PROVEN selection effect: T = ∅ in-file, FORCED by line 78 (triple>1 ⟹
  gcd(A,B)>1 ⟹ skipped). No mathematics beyond L1's contrapositive-free zone:
  skipped pairs are exactly those that could never be counterexamples anyway.

## Step-4 verdict (prefilter forcing, formal)
- Forced by filters: gcd(A,B)=1 on every line; T=∅; S>10^6; value-ratio<999;
  intra-block bases; |d|≤1000; e∈3..7.
- NOT forced: P over C. Proof of non-forcing: 1528 C-lines satisfy ALL filters
  simultaneously (R004_001, dual-verified). Hence no filter or filter
  combination logically entails P. The puzzle is confined to the |off|=1
  SUBSET (14 unique dataset triples + 9 wide-search hits, all P).
- Option 6 (coprime prefilter forces the phenomenon): REJECTED as stated —
  the prefilter explains T=∅ only. It cannot enrich P over C (both survive it).
