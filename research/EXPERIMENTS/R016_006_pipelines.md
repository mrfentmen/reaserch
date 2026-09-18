# EXPERIMENT R016_006 — pipeline separation + equivalence + critic/verifier summary

- SEPARATION: exact pipeline `R016_006_exact_pipeline.py` (C20/C21 inside) vs near-miss
  pipeline `R016_007_nearmiss_pipeline.py` (grep-clean: zero MOD/RES/SKIP/c20/c21 tokens
  outside a header comment; split from the combined module AFTER validation, re-validated:
  split file reproduces R013-A 7/6 exactly). Indexer `R016_001_pairindex.py` calls no gcd
  in its index path (grep-clean modulo docstring + Stein def used only by validators).
- EQUIVALENCE: near-miss pipeline vs independent value-sorted brute (third root
  implementation inline), 2..40/exps 3..5: 2340 = 2340 hits, canonical sets equal
  (order-free keys; an order-sensitive first attempt correctly FAILED then passed —
  comparison bug, not pipeline bug). ARTIFACTS/R016_004_stdout.txt.
- CRITIC (15 attacks): pair math (proven + dual-inverse agreement on all k to N=500);
  off-by-one (contiguity asserts); ordered/unordered (domain A≤B ⊇ hunter coverage);
  gaps/overlap (asserted per sharding); duplicates (canonical keys); boundaries (suite);
  coprime (dual-gcd); legacy blocks (grep-absent); hidden filters (grep + agreement);
  counts (closed forms); exact/near-miss mixing (file split + grep); pruner reuse (refused
  by ARCHITECTURE.md rule); two self-caught harness bugs repaired with reruns.
- VERIFIER: Bun spots (4 interblock roundtrips with identical indices, 7-shard
  contiguity, gcds) + full R015-hit agreement history; veto retained, no veto cast.
  2000-scale launch explicitly NOT approved here (needs ticket).
