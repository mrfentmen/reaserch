# EXPERIMENT R016_004 — inter-block regression suite (permanent)

- Old blocks: [2..2000],[2001..3000],[3001..4000],[4001..5000],[5001..6000]. 8/10 suite
  pairs are INTER-block (the exact class the hunter never examined).
- Suite (pair → index, N=6000, all roundtrips PASS, Bun independently reproduced 4/4):
  (2,5000)→4998 INTER; (1999,2001)→9986999 INTER; (2000,2001)→9991000 INTER;
  (2000,3000)→9991999 INTER; (7,6000)→35978 INTER; (2,6000)→5998 INTER;
  (2000,2000)→9990999 INTRA; (5001,6000)→17497499 INTRA; (1500,4500)→7868249 INTER;
  (999,5555)→5489053 INTER.
- Machine record: ARTIFACTS/R016_001_index.json (indices) + R016_002_stdout.txt.
- Verifier (Bun): index formula + roundtrips + 7-shard contiguity + gcd spots re-derived. Veto retained.
