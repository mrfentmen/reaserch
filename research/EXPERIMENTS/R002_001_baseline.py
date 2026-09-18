# R002_001 — baseline benchmark (exact mirror of beal.ts check loop, near-logging off)
# Measures: total/coprime/check counts, wall time, stage split, time per M checks.
# Domain: bases 2..300, exps 3..7 (299*5=1495 powers). Python exact arithmetic.
import math, time, json
t0 = time.time()
BMAX, EXPS = 300, [3, 4, 5, 6, 7]
t = time.time(); pows = sorted((pow(b, e), b, e) for b in range(2, BMAX+1) for e in EXPS)
t_gen = time.time() - t
def iroot(v, e):
    hi = 1 << ((v.bit_length() + e - 1)//e + 1)
    if hi > v: hi = v
    lo, best = 1, 1
    while lo <= hi:
        mid = (lo + hi)//2
        p = pow(mid, e)
        if p == v: return mid
        if p < v: best, lo = mid, mid + 1
        else: hi = mid - 1
    return best
t = time.time(); pairs = [(vi, bi, vj, bj) for ii, (vi, bi, ei) in enumerate(pows)
        for (vj, bj, ej) in pows[ii:] if math.gcd(bi, bj) == 1]
t_pair = time.time() - t
t = time.time(); found = []; checks = 0
for vi, bi, vj, bj in pairs:
    s = vi + vj
    for e in EXPS:
        checks += 1
        f = iroot(s, e)
        if pow(f, e) == s and math.gcd(bi, int(f)) == 1 and math.gcd(bj, int(f)) == 1:
            found.append((bi, vj and bj, int(f), e))
t_chk = time.time() - t
wall = time.time() - t0
print(f"powers={len(pows)} pairs_total={len(pows)*(len(pows)+1)//2} coprime_pairs={len(pairs)} checks={checks} found={found}")
print(f"stage gen/sort={t_gen:.1f}s pairfilter={t_pair:.1f}s checks={t_chk:.1f}s wall={wall:.1f}s")
print(f"time per M checks = {t_chk/checks*1e6:.1f}s; checks/s = {checks/t_chk:.0f}")
json.dump({"powers": len(pows), "coprime_pairs": len(pairs), "checks": checks,
           "t_gen": t_gen, "t_pair": t_pair, "t_chk": t_chk, "wall": wall,
           "found": found}, open("/Users/dtaxk/reaserch/research/ARTIFACTS/R002_001_baseline.json", "w"))
