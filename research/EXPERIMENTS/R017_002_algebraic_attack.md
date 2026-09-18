# R017_002 — algebraic attack (contrapositive, prime divisors, factorization, signs)

## Contrapositive program (Part 4)
Assume class C: (A,B)=(A,C)=(B,C)=1, plus Beal-shape (bases≥2, exps≥3),
A^xa+B^xb−C^e=ε=±1. Goal: contradiction. RESULT: none of the below derives one.
Every lever returns "consistent". The all-pairs-coprime case is compatible with
±1 on every tested axis — possibility (not existence) established repeatedly.

## Prime-divisor attack (Part 5) — exact congruences, all consistent
- Mod A (class C): B^xb − C^e ≡ ε. Mod B: A^xa − C^e ≡ ε. Mod C: A^xa + B^xb ≡ ε.
  With all bases coprime to the modulus, these are non-degenerate congruences with
  solutions (e.g. B^xb−C^e≡ε mod A solvable). No force. CHECKED: no modulus among
  A,B,C or small prime divisors of C^e±1,A^xa,B^xb yields impossibility in general.
- Mod p | (C−1), ε=−1: S≡0 automatic; forces nothing on A,B beyond L2a below.

## Factorization attack (Part 6) — split signs
- ε=−1, e odd: S=C^e−1=(C−1)·M. LEMMA L2a (PROVEN, any e): (A,B)=1 ⟹ gcd(A·B,C−1)=1.
  Proof: d|A, d|C−1 ⟹ C≡1 ⟹ S≡B^xb≡C^e−1≡0 ⟹ d|B ⟹ d=1; symmetric. ∎
  Usefulness for U: NONE (constrains (A·B, C−1), disjoint from (A,C),(B,C)). Verified
  computationally on all 14 unique dataset triples (script below): holds 14/14.
- ε=+1, e odd: S=C^e+1=(C+1)·M'. LEMMA L2b (PROVEN, e odd ESSENTIAL): (A,B)=1 ⟹
  gcd(A·B,C+1)=1. Proof: d|A,d|C+1 ⟹ C≡−1 ⟹(e odd) C^e+1≡0; S≡B^xb≡0 ⟹ d|B ⟹ d=1. ∎
  Verified on all dataset ε=+1/e-odd triples. Usefulness for U: NONE (same reason).
- ε=+1, e even: derived CONDITION (not elimination): d|A, d|C+1 ⟹ B^xb≡2 (mod d).
  (Since C≡−1, C^e+1≡2.) Consistent, non-forcing. Recorded.
- Cyclotomic/Aurifeuillean: no general factorization of C^e+1 (e even) or of the
  three-term sum; inapplicable without extra hypotheses. Not invoked.
- Zsigmondy (Part 9): primitive prime divisor q of C^e∓1 (exists except (C,e)=(2,6),
  e=2, C+1 a power of 2 — hypotheses CHECKED per application, none of our e≥3, C≥2
  hits fall in exceptions... where applied) satisfies q∤C, and q|A ⟹ q|B (shown:
  A≡0 ⟹ B^xb≡S≡0 mod q) contradicting (A,B)=1, so q divides NONE of A,B,C.
  IRRELEVANT to forcing (documented with hypothesis check, not forced).

## GCD attack (Part 7)
- gcd(A^xa, C^e±1), gcd(B^xb, C^e±1): no forced common divisor (L2a/L2b show the
  natural candidates (C∓1) are coprime to A·B — the OPPOSITE of forcing).
- gcd(A^xa+B^xb, C^e)=gcd(S,C^e): = gcd(±1+... S=C^e±1 ⟹ gcd(S,C^e)=gcd(±1,C^e)=1.
  So (S,C)=1 ALWAYS for |off|=1 (both signs). Hence any prime dividing S avoids C —
  again pointing AWAY from P. (Trivial but recorded: it rules out "C shares via S".)
- gcd(A^xa,B^xb)=1 (from (A,B)=1). No lever.

## Valuation attack (Part 8) — LTE only where hypotheses match
- p|A, p∤B (coprime pairs): v_p(S)=0 shown in R002-rejection; with S=C^e±1 this gives
  C^e≡±1 mod p... wait: S=C^e±1 and v_p(S)=0 means p∤S, i.e. C^e≢∓1... C^e ≡ ∓1+... hmm:
  S = C^e−ε' ... let me restate cleanly: S−C^e=ε, p|A: A^xa≡0, so B^xb−C^e≡ε (mod p).
  With (B,p)=(C,p)=1 possible... v_p gives NOTHING beyond this congruence (p∤S needed?
  S = A^xa+B^xb ≡ B^xb ≢ 0 mod p ✓ automatic). No contradiction. LTE needs
  p|(x±y) with same exponents — our three exponents generally differ; the only
  matchable subcase (e=xb, C^e−B^e=(C−B)M) was exhausted in R011_004(b): dead.
- VERDICT: valuations contribute no forcing (consistent with R002 VAL rejection).

## Parity/local (Part 10) — narrowed to class-C ±1 impossibility proofs
- None found. R011_001 moduli≤32 sweep already showed residues permit class-C ±1.
  No new modulus attempted here (would repeat R002 blindly — refused per instructions).

## Exponent split (Part 11) — C21 used ONLY as mathematics, never as filter
- gcd(xa,xb,e)>2 + EXACT equality ⟹ FLT contradiction (C21, proven). For ±1 (not
  equality) C21 says NOTHING (R014). All-equal-exponent ±1 (A^e+B^e−C^e=±1):
  no theorem (FLT needs =0). Mixed parities: present in hits, no split found.

## Net of Steps 4–11
Proven this cycle: L2a (any e), L2b (e odd) + non-sufficiency for U (explicitly:
they constrain (AB, C∓1), disjoint from the P-predicate). Everything else:
investigated, no forcing. The contrapositive stands unrefuted AND unproven.
