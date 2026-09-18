# EXPERIMENT R016_002 — exhaustive validation (domains, roundtrips, coprime)

- CODE/COMMAND: EXPERIMENTS/R016_002_validate.py, exit=0, 4.3 s → ARTIFACTS/R016_002_stdout.txt.
- N=10/20/50/100/250/500: set equality vs nested loop; full roundtrip idx∘unrank;
  closed-form quadratic inverse agrees on EVERY k (two derivations, not one).
  Totals 45/190/1225/4950/31125/124750 all match n(n+1)/2.
- Coprime: Euclid vs Stein agree N=100 (2944), N=500 (75616); indexer output unfiltered.
- CRITIC: off-by-one would break contiguity asserts (none broke); ordered/unordered fixed
  by domain definition A≤B (superset of hunter's value-ordered coverage — extra ordered
  same-base exp pairs are gcd-skipped or duplicate-S, documented in R016_006 record).
