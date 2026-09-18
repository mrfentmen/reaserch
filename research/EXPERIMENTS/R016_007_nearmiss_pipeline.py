# R016 pipelines — ARCHITECTURALLY SEPARATE by construction (see ARCHITECTURE rule)
# EXACT pipeline : indexer -> coprime filter -> C20 guards -> C21 skip -> exact iroot (FOUND iff S==C^e)
# NEAR-MISS pipeline: indexer -> coprime filter -> direct-D census for |off| in 1..1000 (NO C20/C21/residue/skip
#   logic anywhere in this file — verified by inspection; grep for SKIP/MOD/RES/gcd(x yields nothing but the
#   claim-scope pair prefilter and classification gcds).
import math, sys
sys.path.insert(0, "research/EXPERIMENTS")
from R016_001_pairindex import idx_of, unrank, shard
EXPS = [3, 4, 5, 6, 7]
def iroot(v, e):
    hi = 1 << ((v.bit_length() + e - 1) // e + 1)
    if hi > v: hi = v
    lo, best = 1, 1
    while lo <= hi:
        mid = (lo + hi) // 2
        p = pow(mid, e)
        if p == v: return mid
        if p < v: best, lo = mid, mid + 1
        else: hi = mid - 1
    return best
def cls_euc(a, b, c):
    gab, gac, gbc = math.gcd(a, b), math.gcd(a, c), math.gcd(b, c)
    if math.gcd(gab, c) > 1: return "T"
    if gab > 1 or gac > 1 or gbc > 1: return "P"
    return "C"
def iter_pairs(N, shard_i=0, nshards=1):
    n = N - 1; TOTAL = n * (n + 1) // 2
    s, e = shard(TOTAL, shard_i, nshards)
    for k in range(s, e):
        yield unrank(k, N)
def nearmiss_census(N, EXPS=EXPS, off_max=1000):
    """R011-style census. NO pruners. Returns list of (A,xa,B,xb,C,e,d,cls) with 0<|d|<=off_max."""
    hits = []
    for A, B in iter_pairs(N):
        if math.gcd(A, B) != 1: continue
        for xa in EXPS:
            for xb in EXPS:
                s = pow(A, xa) + pow(B, xb)
                for e in EXPS:
                    f = iroot(s, e)
                    lo, hi = s - pow(f, e), pow(f + 1, e) - s
                    d, c = (lo, f) if lo < hi else (-hi, f + 1)
                    if 0 < abs(int(d)) <= off_max:
                        hits.append((A, xa, B, xb, int(f) if int(d) >= 0 else int(f) + 1, e, int(d),
                                     cls_euc(A, B, int(f) if int(d) >= 0 else int(f) + 1)))
    return hits
