# R016 pipeline validation: near-miss pipeline vs independent brute one-liner (value-sorted power
# list a la original hunter — maximally different enumeration); exact pipeline pair-count sanity.
import sys, time, json
sys.path.insert(0, "research/EXPERIMENTS")
from R016_003_pipelines import nearmiss_census, exact_search, iter_pairs
import math
t0 = time.time()
# A. near-miss pipeline (base-major) vs brute (value-sorted power list), 2..40/exps3..5, |off|<=1000
N, EXPS, OFF = 40, [3, 4, 5], 1000
got = nearmiss_census(N, EXPS, OFF)
pows = sorted((pow(b, e), b, e) for b in range(2, N + 1) for e in EXPS)
exp = []
for i, (vi, bi, ei) in enumerate(pows):
    for vj, bj, ej in pows[i:]:
        if math.gcd(bi, bj) != 1: continue
        s = vi + vj
        for e in EXPS:
            f = 1
            lo, hi = 1, 1 << ((s.bit_length() + e - 1) // e + 1)
            while lo <= hi:  # inline binary root (third implementation)
                mid = (lo + hi) // 2
                p = pow(mid, e)
                if p == s: f = mid; break
                if p < s: f, lo = mid, mid + 1
                else: hi = mid - 1
            lo2, hi2 = s - pow(f, e), pow(f + 1, e) - s
            d, c = (lo2, f) if lo2 < hi2 else (-hi2, f + 1)
            if 0 < abs(int(d)) <= OFF:
                gab, gac, gbc = math.gcd(bi, c), 0, 0
                gac, gbc = math.gcd(bi, c), math.gcd(bj, c)
                k = "T" if math.gcd(math.gcd(bi, bj), c) > 1 else ("P" if gab > 1 or gac > 1 or gbc > 1 else "C")
                exp.append((bi, ei, bj, ej, c, e, int(d), k))
def canon(hits):
    # order-free: unordered end-pair + C value (value-order vs base-order namings coincide here)
    return {(frozenset({(px[0], px[1]), (px[2], px[3])}), pow(px[4], px[5])) for px in hits}
print("pipeline hits:", len(got), "brute hits:", len(exp), "canonical-equal:", canon(got) == canon(exp))
assert canon(got) == canon(exp), "near-miss pipeline mismatch"
# B. exact pipeline pair accounting on 2..300/exps3..7 (compare structure, not R002 power-pair counts)
det, st = exact_search(300)
print("exact N=300:", st, "counterexamples:", det)
assert det == []
json.dump({"got": len(got), "exp": len(exp)}, open("research/ARTIFACTS/R016_004_pipecheck.json", "w"))
print("PIPELINES OK", round(time.time() - t0, 1))
