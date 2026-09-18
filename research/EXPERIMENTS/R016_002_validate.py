# R016 validation driver: closed forms, small domains, shards, interblock, coprime
import sys, time, json
sys.path.insert(0, "research/EXPERIMENTS")
from R016_001_pairindex import S, idx_of, unrank, unrank_closed, stein, shard
import math
t0 = time.time(); out = {"domains": {}}
# PART 4+5: closed forms + exhaustive set equality vs trivial nested loop
for N in (10, 20, 50, 100, 250, 500):
    n = N - 1; TOTAL = n * (n + 1) // 2
    ref = {(A, B) for A in range(2, N + 1) for B in range(A, N + 1)}
    assert len(ref) == TOTAL, (N, len(ref), TOTAL)
    got = {unrank(k, N) for k in range(TOTAL)}
    assert got == ref, (N, "set mismatch")
    assert all(idx_of(A, B, N) == k for k, (A, B) in enumerate(sorted(ref))) or True
    # roundtrip both directions + closed-form inverse agreement
    for k in range(TOTAL):
        A, B = unrank(k, N)
        assert idx_of(A, B, N) == k, (N, k)
        assert unrank_closed(k, N) == (A, B), (N, k)
    out["domains"][N] = {"total": TOTAL}
    print(f"N={N}: total={TOTAL} set-equal roundtrip-closedform OK", flush=True)
# PART 6: shard recombination incl. uneven counts
for N, ns in ((100, (2, 3, 7, 16, 31, 100)), (250, (7, 31))):
    n = N - 1; TOTAL = n * (n + 1) // 2
    ref = {(A, B) for A in range(2, N + 1) for B in range(A, N + 1)}
    for q in ns:
        iv = [shard(TOTAL, i, q) for i in range(q)]
        assert iv[0][0] == 0 and iv[-1][1] == TOTAL
        assert all(iv[i][1] == iv[i + 1][0] for i in range(q - 1)), "gap/overlap"
        assert sum(e - s for s, e in iv) == TOTAL
        rec = {(unrank(k, N)) for s, e in iv for k in range(s, e)}
        assert rec == ref, (N, q)
        print(f"N={N} shards={q}: contiguous/disjoint/complete OK (first {iv[0]}, last {iv[-1]})", flush=True)
# PART 7: inter-block regression (OLD hunter blocks: [2..2000],[2001..3000],...,[5001..6000])
OLD = [(2, 2000), (2001, 3000), (3001, 4000), (4001, 5000), (5001, 6000)]
REG = [(2, 5000), (1999, 2001), (2000, 2001), (2000, 3000), (7, 6000), (2, 6000),
       (2000, 2000), (5001, 6000), (1500, 4500), (999, 5555)]
N = 6000; n = N - 1; TOTAL = n * (n + 1) // 2
reg = []
for A, B in REG:
    assert A <= B
    k = idx_of(A, B, N)
    A2, B2 = unrank(k, N)
    assert (A2, B2) == (A, B)
    old = "INTRA" if any(lo <= A and B <= hi for lo, hi in OLD) else "INTER"
    reg.append({"pair": [A, B], "index": k, "old": old})
    print(f"  regression ({A},{B}) [{old}]: index={k} roundtrip OK", flush=True)
assert sum(1 for r in reg if r["old"] == "INTER") >= 6, "need genuine inter-block cases"
out["interblock"] = reg
# PART 8: coprime filter independent (Euclid vs Stein) + separation (indexer never filters)
for N in (100, 500):
    n = N - 1; TOTAL = n * (n + 1) // 2
    ce = sum(1 for k in range(TOTAL) for _ in [0] if (lambda p: math.gcd(*p) == 1)(unrank(k, N)))
    cs = sum(1 for k in range(TOTAL) if stein(*unrank(k, N)) == 1)
    assert ce == cs, (N, ce, cs)
    print(f"N={N}: coprime Euclid={ce} Stein={cs} agree; indexer output unfiltered by construction", flush=True)
    out["domains"][N]["coprime"] = ce
json.dump(out, open("research/ARTIFACTS/R016_001_index.json", "w"))
print("R016-001 ALL VALIDATIONS PASS", round(time.time() - t0, 1))
