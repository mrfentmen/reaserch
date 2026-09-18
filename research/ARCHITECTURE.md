# ARCHITECTURAL RULE (permanent): exact-equality and near-miss pipelines are SEPARATE

1. The EXACT pipeline (`research/EXPERIMENTS/R016_006_exact_pipeline.py`) MAY use C20/C21
   (proven safe for exact equality: R002 safety 24=24).
2. The NEAR-MISS pipeline (`research/EXPERIMENTS/R016_007_nearmiss_pipeline.py`) MUST NOT
   contain residue-table, skip-set, or any exact-equality pruner logic (grep-verified clean;
   R014 proved such reuse census-unsafe with measured false rejections).
3. Both consume the pair indexer (`R016_001_pairindex.py`), which MUST NOT filter
   (grep-verified: no gcd call in index path). Coverage and filtering stay separate concepts.
4. Any future pruner needs a per-question safety proof + equivalence test before touching
   either pipeline. Violations fail the GO gate by rule, not by review.
