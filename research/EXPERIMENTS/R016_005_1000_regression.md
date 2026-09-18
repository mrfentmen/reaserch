# EXPERIMENT R016_005 — 1000 regression + benchmark + 2000-gate status

- 1000-REGRESSION: nearmiss pipeline (split file) over 2..1000/exps 3..7 → 11/11 lines
  IDENTICAL to R015 (sets equal, 471 s). Full |off|≤1000 census alongside: 68,764 lines
  (P 66580/C 2184 — scope differs from old intra-block file (no S/ratio filters here), so
  no finding claimed from that ratio; recorded to prevent misreading).
- This establishes: inter-block gap gone BY CONSTRUCTION (single range) + IN EVIDENCE
  (old-hunter-missing pairs now enumerated; R015 subset reproduced exactly).
- BENCHMARK (N=2000, 1,999,000 pairs, enumeration only): nested loop 0.36 s vs indexer
  unranking 8.68 s (24× slower; ~4 µs/pair — negligible vs exact-check cost; correctness
  deliberately bought with binary-search unranking; closed-form fast path noted, not taken).
- EXACT PIPELINE cross-check: N=300 checks=842,535 — EXACTLY R002 "both"-mode iroot count
  (independent enumeration, same mathematics). Counterexamples [].
- 2000-GATE (10 conditions): 1 coverage PROVEN+validated; 2 small validation PASS; 3 shard
  recomb PASS; 4 interblock PASS (+Bun); 5 gcd PASS (Euclid/Stein); 6 exact pipeline PASS
  (R002-count match, [] found); 7 near-miss independence PASS (file split, grep-clean,
  brute agreement 2340/2340); 8 perf measured; 9 critic (15 attacks incl. two self-caught
  comparison bugs: order-free keys; census-vs-|off|1 category fix); 10 verifier (Bun spots).
  GATE: TECHNICALLY READY — launch NOT AUTHORIZED (2000-scale needs its own ticket per
  queue discipline; no run launched, correctly).
- R011 untouched (no status change from infrastructure work).
