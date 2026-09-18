# R017_006 tower (OPTIMIZED; math identical to R017_005_baseline.py — see equivalence record)
# Changes ONLY: Newton primary root; binary kept as iroot_reference (validation only);
# S_A=1<<(X*X) once per X; B^xb table once globally; per-X progress + heartbeats; pow counter.
# NO floats. NO pruners (no C20/C21/residue logic in this file). Same domain/classification/ties/signs.
import math, time, json, sys
POWC = [0]
def P(a, b):
    POWC[0] += 1
    return pow(a, b)
def newton_floor(v, e):
    if v <= 0: return 0
    x = 1 << ((v.bit_length() + e - 1) // e + 1)
    while True:
        y = ((e - 1) * x + v // P(x, e - 1)) // e
        if y >= x: break
        x = y
    while P(x + 1, e) <= v: x += 1
    while P(x, e) > v: x -= 1
    return x
def iroot_reference(v, e):
    hi = 1 << ((v.bit_length() + e - 1) // e + 1)
    if hi > v: hi = v
    lo, best = 1, 1
    while lo <= hi:
        mid = (lo + hi) // 2
        p = P(mid, e)
        if p == v: return mid
        if p < v: best, lo = mid, mid + 1
        else: hi = mid - 1
    return best
def check_ineq(r, v, e):
    assert P(r, e) <= v < P(r + 1, e), f"inequality violated r={r} e={e}"
def stein(a, b):
    if a == 0: return b
    if b == 0: return a
    s = 0
    while not (a & 1 | b & 1): a >>= 1; b >>= 1; s += 1
    while not a & 1: a >>= 1
    while b:
        while not b & 1: b >>= 1
        if a > b: a, b = b, a
        b -= a
    return a << s
def cls(A, B, c):
    gab, gac, gbc = stein(A, B), stein(A, c), stein(B, c)
    if math.gcd(gab, c) > 1: return "T"
    if gab > 1 or gac > 1 or gbc > 1: return "P"
    return "C"
def gate():
    print("GATE: exhaustive small + random large + boundaries, exps 3..9", flush=True)
    n = 0
    for v in range(1, 50001):
        for e in range(3, 10):
            r1, r0 = newton_floor(v, e), iroot_reference(v, e)
            check_ineq(r1, v, e); check_ineq(r0, v, e)
            if r1 != r0: print("MISMATCH", v, e); sys.exit(1)
            n += 1
    import random
    rnd = random.Random(1701)
    for _ in range(400):
        v = rnd.getrandbits(rnd.randint(64, 1200)) | 1
        for e in range(3, 10):
            r1, r0 = newton_floor(v, e), iroot_reference(v, e)
            check_ineq(r1, v, e); check_ineq(r0, v, e)
            if r1 != r0: print("MISMATCH-LARGE", v, e); sys.exit(1)
            n += 1
    bases = list(range(2, 2001)) + [rnd.randint(2, 10**6) for _ in range(200)]
    for b in bases:
        for e in range(3, 10):
            for dv in (-2, -1, 0, 1, 2):
                v = pow(b, e) + dv
                if v < 1: continue
                r1, r0 = newton_floor(v, e), iroot_reference(v, e)
                check_ineq(r1, v, e); check_ineq(r0, v, e)
                if r1 != r0: print("MISMATCH-BOUND", v, e); sys.exit(1)
                n += 1
    for X in range(8, 121, 7):
        for dv in (-2, -1, 0, 1, 2):
            v = (1 << (X * X)) + dv
            for e in range(3, 10):
                r1, r0 = newton_floor(v, e), iroot_reference(v, e)
                check_ineq(r1, v, e); check_ineq(r0, v, e)
                if r1 != r0: print("MISMATCH-TOWER", v, e); sys.exit(1)
                n += 1
    print(f"GATE PASS: {n} (v,e) cases, zero mismatches, all inequalities hold", flush=True)
def bench():
    import random
    rnd = random.Random(99)
    vals = [rnd.getrandbits(rnd.randint(100, 1100)) | 1 for _ in range(300)]
    vals += [(1 << (X * X)) + rnd.randint(-10**6, 10**6) for X in range(8, 121, 5)]
    for name, fn in (("binary", iroot_reference), ("newton", newton_floor)):
        POWC[0] = 0
        t = time.time(); nc = 0
        for v in vals:
            for e in range(3, 10):
                r = fn(v, e)
                assert pow(r, e) <= v < pow(r + 1, e)
                nc += 1
        dt = time.time() - t
        print(f"BENCH {name}: {dt:.1f}s over {nc} roots, big-pows={POWC[0]}", flush=True)
def tower():
    EXPS = list(range(3, 10))
    odds = list(range(3, 61, 2))
    BTAB = {B: {xb: pow(B, xb) for xb in EXPS} for B in odds}
    hits = []; checked = 0; calls = 0; t0 = time.time()
    for X in range(8, 121):
        A = 1 << X
        SA = 1 << (X * X)  # A^X with A=2^X, computed ONCE per X
        hx = 0; hb = 0
        for B in odds:
            for xb in EXPS:
                s = SA + BTAB[B][xb]
                if stein(A, B) != 1: continue
                checked += 1
                for e in EXPS:
                    calls += 1
                    f = newton_floor(s, e)
                    if calls % 1000 == 0: check_ineq(f, s, e)
                    lo, hi = s - pow(f, e), pow(f + 1, e) - s
                    d, c = (lo, f) if lo < hi else (-hi, f + 1)
                    if abs(int(d)) == 1:
                        hits.append((A, X, B, xb, c, e, int(d), cls(A, B, c))); hx += 1
            hb += 1
            if hb % 10 == 0:
                print(f"  hb X={X} B={B} elapsed={time.time()-t0:.0f}s", flush=True)
        for B in odds:
            for xa in EXPS:
                s = BTAB[B][xa] + SA
                if stein(B, A) != 1: continue
                checked += 1
                for e in EXPS:
                    calls += 1
                    f = newton_floor(s, e)
                    if calls % 1000 == 0: check_ineq(f, s, e)
                    lo, hi = s - pow(f, e), pow(f + 1, e) - s
                    d, c = (lo, f) if lo < hi else (-hi, f + 1)
                    if abs(int(d)) == 1:
                        hits.append((B, xa, A, X, c, e, int(d), cls(B, A, c))); hx += 1
        el = time.time() - t0
        print(f"X={X} pairs={checked} hits={hx} elapsed={el:.0f}s rate={calls/max(el,1):.0f}roots/s", flush=True)
    from collections import Counter
    print("tower pairs checked:", checked, "|off|=1:", len(hits), dict(Counter(h[7] for h in hits)))
    def fmt(v, x):
        return f"2^{x}" if v == 1 << x else str(v)
    for h in hits[:20]:
        print(f"  TOWER-HIT: {fmt(h[0],h[1])}^{h[1]} + {fmt(h[2],h[3])}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}", flush=True)
    json.dump({"checked": checked, "hits": [[str(a), xa, b, xb, c, e, d, k] for a, xa, b, xb, c, e, d, k in hits]},
              open("research/ARTIFACTS/R017_006_counts.json", "w"))
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "tower"
    if mode == "gate":
        gate()
    elif mode == "bench":
        bench()
    elif mode == "tower":
        tower()
