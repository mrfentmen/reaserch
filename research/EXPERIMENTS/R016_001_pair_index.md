# EXPERIMENT R016_001 — pair-index mathematics

- TICKET: R001/R016. CODE: EXPERIMENTS/R016_001_pairindex.py (pure math, zero filtering).
- CLAIMS (PROVEN, proofs in file header): row-start S(a)=a·n−a(a−1)/2 (telescoping sum);
  idx total n(n+1)/2 with contiguous collision-free rows; inverse via max{a:S(a)≤k}
  (existence/uniqueness from strict increase); shard intervals partition [0,TOTAL)
  (union complete, intersections empty). C30.
- Coefficient check: N=6000 → TOTAL=17,997,000 pairs (vs hunter's intra-block 60.7M
  power-pairs — different enumeration units by design: base pairs × exp grid;
  inter-block included by construction).
