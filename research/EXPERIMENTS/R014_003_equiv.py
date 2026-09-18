# R014 equivalence test (validation domain: bases 2..60, exps 3..6) + coverage asserts
import sys, time, json
sys.path.insert(0, "research/EXPERIMENTS")
from R014_001_reference import ref_eval
from R014_002_optimized import opt_eval
BASES = list(range(2, 61)); EXPS = [3, 4, 5, 6]
n = len(BASES)
assert n * (n + 1) // 2 == 1770, "base-pair closed form"
tot = mis = rootm = clsm = 0
ref_hits = []
stats = {"c21": 0, "c20": 0, "exact": 0}
t0 = time.time()
for A in BASES:
    for B in BASES:
        if B < A: continue
        tot += 1
        cop = __import__("math").gcd(A, B) == 1
        for xa in EXPS:
            for xb in EXPS:
                for e in EXPS:
                    if not cop: continue
                    rd, rc, rk = ref_eval(A, xa, B, xb, e)
                    od, oc, ok = opt_eval(A, xa, B, xb, e, stats)
                    if isinstance(od, str):
                        # optimized skipped: legal ONLY if no exact |off|<=1000... NO — legality is:
                        # SKIP21 needs d irrelevant (equation impossible); SKIP20 needs S!=C^e... but |off|=1
                        # means S-C^e=±1 != 0, still must be REJECTED correctly. Verify: recompute D exactly.
                        s = pow(A, xa) + pow(B, xb)
                        if od == "SKIP20":
                            assert s % {3: 9, 4: 16, 5: 11, 6: 9}[e] not in {c for c in
                                [pow(z, e, {3: 9, 4: 16, 5: 11, 6: 9}[e]) for z in range({3: 9, 4: 16, 5: 11, 6: 9}[e])]}, "SKIP20 without residue cause"
                        if abs(rd) == 1:
                            mis += 1
                            print("FALSE REJECTION:", A, xa, B, xb, e, rd)
                    else:
                        if (od, oc, ok) != (rd, rc, rk):
                            mis += 1
                            if od != rd: rootm += 1
                            if ok != rk: clsm += 1
                            print("MISMATCH:", (A, xa, B, xb, e), (rd, rc, rk), (od, oc, ok))
                    if abs(rd) == 1: ref_hits.append((A, xa, B, xb, rc, e, rd, rk))
from collections import Counter
print("basepairs:", tot, "| ref |off|=1:", len(ref_hits), dict(Counter(h[7] for h in ref_hits)))
print("mismatches:", mis, "root:", rootm, "class:", clsm, "stats:", stats, f"{time.time()-t0:.1f}s")
assert mis == 0, "UNEXPLAINED MISMATCHES"
json.dump({"ref_hits": ref_hits}, open("research/ARTIFACTS/R014_002_equiv.json", "w"))
print("EQUIVALENCE OK: zero unexplained mismatches")
