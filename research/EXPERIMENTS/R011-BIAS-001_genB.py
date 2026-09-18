# R011-BIAS-001 Generator B — value-sorted census of distinct S = A^x + B^y
# Ticket: R011-BIAS-001. Independent of the existing pipeline: NO base-pair enumeration,
# NO gcd(A,B) prefilter, NO S>1e6 filter, NO ratio bound. All distinct sums S (bases<=150,
# exps 3..7) processed in ASCENDING S order; nearest e-th power per e in 3..7 via bisect
# tables; both signs ±1; post-hoc P/C/T classification (naming-invariant; canonical
# display naming = smallest base). ±2 guard is a bug tripwire (documented in TICKET.md).
import math, bisect, json, time, sys
t0 = time.time()
BMAX = 150
EXPS = (3, 4, 5, 6, 7)
EVALS = (3, 4, 5, 6, 7)
GUARD = 2

maxS = 2 * BMAX ** 7
tables = {}
for e in EVALS:
    cmax = int(round(maxS ** (1.0 / e))) + 4
    tables[e] = [c ** e for c in range(2, cmax + 1)]

# power values with canonical (smallest-base) naming
canon = {}
for A in range(2, BMAX + 1):
    for x in EXPS:
        v = A ** x
        if v not in canon or A < canon[v][0]:
            canon[v] = (A, x)
vals = sorted(canon)

# distinct sums S = p+q, p<=q, with one representative pair
sums = {}
for i, p in enumerate(vals):
    for q in vals[i:]:
        s = p + q
        if s not in sums:
            sums[s] = (p, q)
ordered = sorted(sums)

def classify(A, x, B, y, C, e):
    g_ab, g_ac, g_bc = math.gcd(A, B), math.gcd(A, C), math.gcd(B, C)
    g_abc = math.gcd(g_ab, C)
    if g_abc > 1:
        return "T", (g_ab, g_ac, g_bc, g_abc)
    if g_ab > 1 or g_ac > 1 or g_bc > 1:
        return "P", (g_ab, g_ac, g_bc, g_abc)
    return "C", (g_ab, g_ac, g_bc, g_abc)

n_s = 0
evals = 0
raw_hits = 0
guard_anomalies = 0
seen = {}
smallS_hits = 0

for rank, S in enumerate(ordered):
    n_s += 1
    evals += len(EVALS)
    p, q = sums[S]
    for e in EVALS:
        tvals = tables[e]
        i = bisect.bisect_left(tvals, S)
        for j in range(max(0, i - GUARD), min(len(tvals), i + GUARD + 1)):
            d = S - tvals[j]
            if d == 1 or d == -1:
                C = j + 2
                raw_hits += 1
                if (j - i) < -1 or (j - i) > 0:
                    guard_anomalies += 1
                key = (S, C, e)
                if key in seen:
                    continue
                nA, nx = canon[p]
                nB, ny = canon[q]
                cls, gcds = classify(nA, nx, nB, ny, C, e)
                seen[key] = {"A": nA, "x": nx, "B": nB, "y": ny, "C": C, "e": e,
                             "S": S, "off": d, "class": cls, "gcds": gcds,
                             "value_rank": rank, "value_rank_frac": rank / len(ordered)}
                if S <= 10 ** 6:
                    smallS_hits += 1

classes = {"P": 0, "C": 0, "T": 0}
for r in seen.values():
    classes[r["class"]] += 1

out = {
    "generator": "B (value-sorted census of distinct S, ascending)",
    "seed": None, "bases": [2, BMAX], "exps": list(EXPS), "e_values": list(EVALS),
    "distinct_power_values": len(vals),
    "distinct_sums_processed": n_s,
    "sum_evaluations": evals,
    "guard_window": GUARD,
    "raw_hits": raw_hits,
    "deduped_equations": len(seen),
    "class_P": classes["P"], "class_C": classes["C"], "class_T": classes["T"],
    "smallS_le1e6_deduped_hits": smallS_hits,
    "guard_anomalies": guard_anomalies,
    "runtime_s": round(time.time() - t0, 2),
    "hits": sorted(seen.values(), key=lambda r: r["S"]),
}
print(json.dumps(out, indent=1))
sys.stderr.write(f"genB done: sums={n_s} raw={raw_hits} dedup={len(seen)} "
                 f"P/C/T={classes['P']}/{classes['C']}/{classes['T']} "
                 f"t={time.time()-t0:.1f}s\n")
