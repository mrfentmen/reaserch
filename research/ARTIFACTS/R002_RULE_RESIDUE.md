# RULE RESIDUE — power-residue prefilter (R002, PROVEN necessary condition)

- RULE: For candidate (pair S=A^x+B^y, exponent e), with (m_e, R_e) =
  (9,{0,1,8}) e=3; (16,{0,1}) e=4; (11,{0,1,10}) e=5; (9,{0,1}) e=6;
  (29,{0,1,12,17,28}) e=7: skip the exact iroot check unless S mod m_e ∈ R_e.
- MATHEMATICAL STATEMENT: S = C^e ⟹ S mod m_e ∈ {c^e mod m_e : c ∈ Z}.
- ASSUMPTIONS: exact integer arithmetic for S and S mod m_e (holds: Python
  big ints; TS BigInt likewise); residue tables complete over Z/mZ.
- PROOF: congruence preserves equality; contrapositive eliminates. The tables
  are complete by exhaustive enumeration over representatives 0..m−1. ∎
- COUNTEREXAMPLE SEARCH: safety scan (R002_003, no coprime skip, 2..60,
  exps 3..6) compared full perfect-power detection sets pruned vs unpruned:
  24 = 24, identical; planted valid solutions (3³+6³=3⁵, 2⁵+2⁵=2⁶) survive.
- EXHAUSTIVE SMALL TEST: same as above (M/N = 1 on stated domain).
- REMOVAL RATE (bases 2..300, exps 3..7, 3,387,250 checks): residue alone
  removes 69.9% of iroot calls (3,387,250 → 1,020,464); with FLT rule 75.1%.
- COMPUTATIONAL SPEED EFFECT (same-run, Python): none 21.5 s → res 7.7 s
  (2.79×), both 7.3 s (2.95×). NOTE: earlier 15.7 s baseline was a different
  run (machine variance); within-run ratios are the valid metric. Removal %
  transfers to any exact implementation; TS wall-clock speedup NOT measured.
- IMPLEMENTATION: `research/EXPERIMENTS/R002_002_prune.py` (reference);
  drop-in pre-iroot guard for beal.ts (not yet ported — porting is engineering).
- INDEPENDENT VALIDATION: Bun/TS recomputation of all five tables agrees
  exactly; planted residues hand-verified (243 mod 11 = 1; 64 mod 9 = 1).
- LITERATURE STATUS: standard power-residue sieving (computational number
  theory folklore); no novelty claimed for the technique.
- NOVELTY STATUS: REPRODUCTION (technique) + measured application here.
- CANONICAL STATUS: PROVEN (necessity statement). Effectiveness numbers are
  VERIFIED COMPUTATIONALLY (supporting evidence, separate).
