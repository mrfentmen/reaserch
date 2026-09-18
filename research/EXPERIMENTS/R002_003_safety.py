# R002_003 — safety test: pruned vs unpruned perfect-power detection equality (NO coprime skip)
# Domain 2..60, exps 3..6. Records EVERY S==C^e detection (any gcd) in both modes; asserts identical sets
# and asserts planted valid solutions present: 3^3+6^3=3^5 (27+216=243), 2^5+2^5=2^6 (32+32=64).
import math, time
BMAX, EXPS = 60, [3, 4, 5, 6]
MOD = {3: 9, 4: 16, 5: 11, 6: 9}
RES = {e: {pow(c, e, MOD[e]) for c in range(MOD[e])} for e in EXPS}
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
pows = sorted((pow(b, e), b, e) for b in range(2, BMAX+1) for e in EXPS)
def scan(prune):
    det = set()
    for ii, (vi, bi, ei) in enumerate(pows):
        for vj, bj, ej in pows[ii:]:
            s = vi + vj
            for e in EXPS:
                if prune:
                    if math.gcd(math.gcd(ei, ej), e) > 2: continue
                    if s % MOD[e] not in RES[e]: continue
                f = iroot(s, e)
                if pow(f, e) == s:
                    det.add((bi, ei, bj, ej, int(f), e))
    return det
t = time.time(); d0 = scan(False); t0 = time.time() - t
t = time.time(); d1 = scan(True); t1 = time.time() - t
print(f"unpruned detections={len(d0)} ({t0:.1f}s); pruned detections={len(d1)} ({t1:.1f}s)")
print("sets identical:", d0 == d1)
planted = {(3, 3, 6, 3, 3, 5), (2, 5, 2, 5, 2, 6)}
print("planted present in unpruned:", planted <= d0, "in pruned:", planted <= d1)
for d in sorted(d0)[:15]: print("  det:", f"{d[0]}^{d[1]} + {d[2]}^{d[3]} = {d[4]}^{d[5]}",
      "gcds:", math.gcd(d[0], d[2]), math.gcd(d[0], d[4]), math.gcd(d[2], d[4]))
assert d0 == d1 and planted <= d1
print("SAFETY OK: PRUNED_SET == UNPRUNED_SET and planted valid solutions survive")
