# EXPERIMENT R016_003 — shard validation (recombination incl. uneven splits)

- Evidence: ARTIFACTS/R016_002_stdout.txt (shard block) + R016_002_validate.py (Part 6).
- N=100 × {2,3,7,16,31,100 shards} and N=250 × {7,31}: contiguity (end==next start),
  disjointness, sum==TOTAL, recombined set == unsharded set — ALL PASS.
- Uneven splits covered (7, 16, 31, 100 deliberately non-dividing). No gaps, no overlaps.
