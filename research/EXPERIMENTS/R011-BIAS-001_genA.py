# R011-BIAS-001 Generator A — random (A,B) draws, no prefilter, bisect-table nearest-power
# Ticket: R011-BIAS-001. Independent of the existing pipeline: random base-space sampling
# WITH replacement, fixed seed; NO gcd(A,B) prefilter; NO S>1e6 filter; NO ratio bound.
# Both signs ±1. Post-hoc P/C/T classification (naming-invariant; canonical display naming
# = smallest base). Nearest power via bisect on precomputed C^e tables; ±2 guard is a
# bug tripwire (any |S-C^e|=1 hit is at the UNIQUE nearest power: consecutive e-th
# powers are >=7 apart for e>=3), documented, not claimed as an innovation.
import math, random, bisect, json, time, sys, os
t0 = time.time()
SEED = 20260918
BMAX = 150
EXPS = (3, 4, 5, 6, 7)
EVALS = (3, 4, 5, 6, 7)
N_DRAWS = 300000
GUARD = 2

rng = random.Random(SEED)
maxS = 2 * BMAX ** 7

# power tables: e -> sorted list of C^e values, C>=2
tables = {}
for e in EVALS:
    cmax = int(round(maxS ** (1.0 / e))) + 4
    tables[e] = [c ** e for c in range(2, cmax + 1)]

# canonical naming: value -> (smallest base, exp) over EXPS
canon = {}
for A in range(2, BMAX + 1):
    for x in EXPS:
        v = A ** x
        if v not in canon or A < canon[v][0]:
            canon[v] = (A, x)

def check_hit(S):
    """Return list of (C, e, off, guard_offset) with |off|==1; guard_offset = index - bisect pos."""
    hits = []
    for e in EVALS:
        vals = tables[e]
        i = bisect.bisect_left(vals, S)
        for j in range(max(0, i - GUARD), min(len(vals), i + GUARD + 1)):
            d = S - vals[j]
            if d == 1 or d == -1:
                hits.append((j + 2, e, d, j - i))  # C = j+2 since vals[0] = 2^e
    return hits

def classify(A, x, B, y, C, e):
    g_ab, g_ac, g_bc = math.gcd(A, B), math.gcd(A, C), math.gcd(B, C)
    g_abc = math.gcd(g_ab, C)
    if g_abc > 1:
        return "T", (g_ab, g_ac, g_bc, g_abc)
    if g_ab > 1 or g_ac > 1 or g_bc > 1:
        return "P", (g_ab, g_ac, g_bc, g_abc)
    return "C", (g_ab, g_ac, g_bc, g_abc)

draws = 0
evals = 0  # total (S, e) nearest-power evaluations
gcd_ab_gt1 = 0
raw_hits = 0
guard_anomalies = 0
seen = {}  # (S, C, e) -> record
smallS_hits = 0  # S <= 1e6 (region the hunter excluded)

for _ in range(N_DRAWS):
    A = rng.randint(2, BMAX)
    B = rng.randint(2, BMAX)
    x = rng.choice(EXPS)
    y = rng.choice(EXPS)
    draws += 1
    if math.gcd(A, B) > 1:
        gcd_ab_gt1 += 1
    S = A ** x + B ** y
    evals += len(EVALS)
    for (C, e, off, goff) in check_hit(S):
        raw_hits += 1
        if goff < -1 or goff > 0:
            guard_anomalies += 1  # mathematically impossible; tripwire
        key = (S, C, e)
        if key in seen:
            continue
        nA, nx = canon[A ** x]
        nB, ny = canon[B ** y]
        cls, gcds = classify(nA, nx, nB, ny, C, e)
        # naming-invariance sanity: classify under largest-base naming too
        seen[key] = {"A": nA, "x": nx, "B": nB, "y": ny, "C": C, "e": e,
                     "S": S, "off": off, "class": cls, "gcds": gcds,
                     "guard_offset": goff}
        if S <= 10 ** 6:
            smallS_hits += 1

# naming-invariance verification on every deduped hit: classify under the
# LARGEST-base naming as well; class must be identical (same prime support).
inv_ok = True
for key, r in seen.items():
    A, x, B, y, C, e = r["A"], r["x"], r["B"], r["y"], r["C"], r["e"]
    bigA, bigx = max((b, xx) for b in range(2, BMAX + 1) for xx in EXPS
                     if b ** xx == A ** x)
    bigB, bigy = max((b, yy) for b in range(2, BMAX + 1) for yy in EXPS
                     if b ** yy == B ** y)
    cls2, _ = classify(bigA, bigx, bigB, bigy, C, e)
    if cls2 != r["class"]:
        inv_ok = False
        print("NAMING-VARIANCE:", key, r["class"], cls2, file=sys.stderr)

classes = {"P": 0, "C": 0, "T": 0}
for r in seen.values():
    classes[r["class"]] += 1

out = {
    "generator": "A (random base-space draws, with replacement)",
    "seed": SEED, "bases": [2, BMAX], "exps": list(EXPS), "e_values": list(EVALS),
    "n_draws": draws, "guard_window": GUARD,
    "calibration_gcdAB_gt1_draws": gcd_ab_gt1,
    "calibration_gcdAB_gt1_frac": gcd_ab_gt1 / draws,
    "raw_hits": raw_hits,
    "deduped_equations": len(seen),
    "class_P": classes["P"], "class_C": classes["C"], "class_T": classes["T"],
    "smallS_le1e6_deduped_hits": smallS_hits,
    "guard_anomalies": guard_anomalies,
    "naming_invariance_ok": inv_ok,
    "runtime_s": round(time.time() - t0, 2),
    "hits": sorted(seen.values(), key=lambda r: r["S"]),
}
print(json.dumps(out, indent=1))
sys.stderr.write(f"genA done: draws={draws} raw={raw_hits} dedup={len(seen)} "
                 f"P/C/T={classes['P']}/{classes['C']}/{classes['T']} "
                 f"t={time.time()-t0:.1f}s\n")
