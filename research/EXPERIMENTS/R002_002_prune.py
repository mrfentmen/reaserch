# R002_002 — pruning benchmark: RESIDUE + FLT-gcd rules vs baseline (same domain 2..300, exps 3..7)
# Rule RESIDUE (necessary): S=C^e ==> S mod m_e in {c^e mod m_e}. Moduli: 3->9, 4->16, 5->11, 6->9, 7->29.
# Rule FLT (necessary via FLT): gcd(x,y,e)>2 ==> A^x+B^y=C^e impossible (reduces to U^d+V^d=W^d, d>=3).
import math, time, json
BMAX, EXPS = 300, [3, 4, 5, 6, 7]
MOD = {3: 9, 4: 16, 5: 11, 6: 9, 7: 29}
RES = {e: sorted({pow(c, e, MOD[e]) for c in range(MOD[e])}) for e in EXPS}
print("residue sets:", {e: (MOD[e], RES[e]) for e in EXPS})
ALLOW_E = {}
for x in EXPS:
    for y in EXPS:
        ALLOW_E[(x, y)] = [e for e in EXPS if math.gcd(math.gcd(x, y), e) <= 2]
n_flt_out = sum(1 for x in EXPS for y in EXPS for e in EXPS if math.gcd(math.gcd(x, y), e) > 2)
print(f"FLT eliminates {n_flt_out}/125 (x,y,e) combos = {n_flt_out/125:.1%}")
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
pairs = [(vi, bi, ei, vj, bj, ej) for ii, (vi, bi, ei) in enumerate(pows)
         for (vj, bj, ej) in pows[ii:] if math.gcd(bi, bj) == 1]
print(f"pairs={len(pairs)}")
def run(mode):
    t = time.time(); iroots = 0; found = []
    for vi, bi, ei, vj, bj, ej in pairs:
        s = vi + vj
        for e in EXPS:
            if mode in ("flt", "both") and math.gcd(math.gcd(ei, ej), e) > 2: continue
            if mode in ("res", "both") and s % MOD[e] not in RES[e]: continue
            iroots += 1
            f = iroot(s, e)
            if pow(f, e) == s and math.gcd(bi, int(f)) == 1 and math.gcd(bj, int(f)) == 1:
                found.append((bi, ei, bj, ej, int(f), e))
    return time.time() - t, iroots, found
base_checks = len(pairs) * len(EXPS)
for mode in ("none", "flt", "res", "both"):
    dt, ir, fnd = run(mode)
    print(f"mode={mode}: iroots={ir}/{base_checks} ({ir/base_checks:.2%}) time={dt:.1f}s speedup={15.7/dt:.2f}x found={fnd}")
    assert fnd == []
json.dump({"base_checks": base_checks}, open("/Users/dtaxk/reaserch/research/ARTIFACTS/R002_002_bench.json", "w"))
