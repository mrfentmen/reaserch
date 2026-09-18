# REJECTED pruning candidates (R002 — FALSE as pair-pruners, with proof)

## R-PARITY ("skip pairs by A,B parity"): FALSE
Claim: some (A,B) parity pattern can be eliminated. Disproof: for every parity
pattern a consistent C parity exists for every e — S odd ⟹ C odd works
(odd^e is odd); S even ⟹ C even works (even^e is even). Hence NO (pair,e)
check is eliminable by parity. Parity only constrains C (corollary, no removal
value). No code needed; proof complete. Ordering-independent.

## R-VAL ("p-adic valuations prune coprime pairs"): FALSE in-pipeline
Claim: valuations eliminate coprime-pair checks. Disproof: downstream of the
L1 coprime prefilter (beal.ts:78), every pair has (A,B)=1. For p|exactly one
of A,B (say p|A, p∤B): v_p(S) = min(x·v_p(A), 0) = 0 (distinct valuations),
consistent with v_p(C)=0 for EVERY e — zero elimination. For p∤AB: v_p(S) ≥ 0
unconstrained a priori (a modular, not valuation, question). Hence valuations
contribute no elimination on coprime pairs. ORDERING DEPENDENCY (critic
finding): this rejection holds downstream of the coprime filter; applied
before it, valuations can constrain non-coprime pairs — but those are already
removed by L1. No code needed; proof complete.

## R011 directions (no pruner produced)
- Direction A (derive P from |off|=1): no derivation found (R011 verdict stands).
- Direction B (P ⟹ condition on off): genuine but pruner-useless — if p|B,C,
  p∤A then off ≡ A^xa (mod p). off is computed output, C unknown a priori;
  no check is eliminable in the current loop structure. Recorded, not pursued.
