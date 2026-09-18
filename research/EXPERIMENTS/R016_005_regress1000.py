# R016 1000-regression: near-miss pipeline must reproduce R015's domain + hit set (no new claim).
import sys, time, json
sys.path.insert(0, "research/EXPERIMENTS")
from R016_003_pipelines import nearmiss_census
t0 = time.time()
hits = nearmiss_census(1000, [3, 4, 5, 6, 7], 1000)
dt = time.time() - t0
print(f"full census |off|<=1000 lines={len(hits)} (vs old intra-block file: scope differs — see record)")
hits = [h for h in hits if abs(h[6]) == 1]  # regression target: the |off|=1 subset == R015's question
ref = json.load(open("research/ARTIFACTS/R015_001_hits.json"))["hits"]
def key(h): return (frozenset({(h[0], h[1]), (h[2], h[3])}), pow(h[4], h[5]), h[6])
G, R = {key(h) for h in hits}, {key(h) for h in ref}
print(f"pipeline lines={len(hits)} ref lines={len(ref)} sets-equal={G == R} {dt:.0f}s")
print("missing:", [x for x in R - G][:5])
print("extra:", [x for x in G - R][:5])
from collections import Counter
print("classes:", dict(Counter(h[7] for h in hits)))
assert G == R, "1000-regression mismatch"
json.dump({"match": True}, open("research/ARTIFACTS/R016_005_regress1000.json", "w"))
print("1000-REGRESSION OK: domain reproduced, 11 lines identical, inter-block gap gone by construction")
