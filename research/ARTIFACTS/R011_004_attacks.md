# R011 Step 5 — algebraic attack derivations (all end recorded; none yields P)

Setup: A^xa + B^xb − C^e = ε, ε = ±1; (A,B)=1 (hunter); class-C assumption for
contradiction attempts: additionally (A,C)=(B,C)=1. All exps ≥ 3.

## (a) Equal-exponent subcase xa=xb=e: A^e+B^e−C^e=ε
Mod-9 cubes {0,±1}: 1+1−1=1 achievable (e.g. residues 1,1,1) — no obstruction.
Parity: A,B odd, C odd, e odd: odd+odd−odd=odd ∋ ±1 — consistent. No elimination.
FLT forbids ε=0 only. DEAD (no contradiction derivable; recorded).

## (b) Subcase e=xb (C,B same exponent): (C^e−B^e) − A^xa = −ε... precisely
C^e − B^e = A^xa + ε. Factor LHS: (C−B)·M, M=(C^e−B^e)/(C−B), k:=C−B>0
(C^e>S>B^xb ⟹ C>B since e=xb... C^e > B^e ⟹ C>B ✓; if ε=−1 side S<C^e still
C^e−B^e = A^xa−1 >0 for A≥2,xa≥3 ⟹ C>B ✓).
Class-C gives: every prime p|k with p|C divides B — impossible, so k's prime
factors avoid B,C. Then A^xa = k·M − ε. Mod p|k: A^xa ≡ −ε. No contradiction:
−ε=∓1 is always an xa-th-power residue for SOME A (take A≡∓1). The divisibility
k·M = A^xa+ε is a tautology of the equation, not a constraint. DEAD.

## (c) LTE attempt: needs a difference of LIKE powers. A^xa±1 = (A±1)(···) only
when xa is odd (for +1) — gives k·M = (A±1)·N in subcase (b): true by
definition, no contradiction (N integer automatically). LTE on C^e−B^xb needs
e=xb (reduces to (b)) or yields nothing. Inapplicable in general (three
distinct exponents). DEAD as a forcing tool.

## (d) Catalan/Mihăilescu: applies to u^p−v^q=±1 (TWO powers). Our equation has
THREE power terms; hypotheses do not match. The only two-term specialization
(A^xa=1, i.e. A=1) is outside Beal scope (bases ≥2) and outside the dataset.
RECORDED as inapplicable, not used. Pillai (gaps between single powers →∞):
S is a SUM, not a power — does not apply to S−C^e. RECORDED inapplicable.

## (e) Parity/mod-2^k exhaustive: for every (A,B,C)-parity pattern and e≥3 a
consistent residue assignment exists (odd^e≡odd, even^e≡even mod 2; mod 4/8
odd residues all occur as e-th powers for odd e... verified computationally
for moduli ≤32 in R011_001: no modulus forbids class-C ±1). No elimination.

## (f) S-unit shape: A^xa/C^e + B^xb/C^e = 1+ε/C^e — rational S-unit equation
with VARYING exponents; finiteness theorems (Siegel/Mahler/Evertse) fix
exponents. Pointer for literature, not a derivation. No forcing obtained.

## Net: no symbolic route forces a shared factor from ε=±1 under class-C
assumptions. The equation is compatible with C on every tested algebraic
axis. Proof path currently EMPTY (not failed — no candidate proof exists to
fail). Counterexample path open.
