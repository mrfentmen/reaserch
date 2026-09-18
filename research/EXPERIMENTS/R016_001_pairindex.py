# R016 pair index — mathematics (PROVEN claims live here; code mirrors them exactly)
#
# DOMAIN: base pairs (A,B) with 2 <= A <= B <= N (unordered, with replacement).
# Let n = N-1, a = A-2, b = B-2, so 0 <= a <= b <= n-1.
#
# ROW START: S(a) = #{(a',b'): a'<a} = sum_{i< a} (n-i) = a*n - a*(a-1)/2.
#   Proof: row i holds b in [i, n-1], i.e. n-i entries. Sum 0..a-1 telescopes. QED.
# INDEX: idx(a,b) = S(a) + (b-a). TOTAL = S(n) = n(n+1)/2. (S(n)=n*n-n(n-1)/2.)
#   Monotone: row a occupies exactly [S(a), S(a+1)). Contiguous, collision-free
#   by construction (each pair sits in its row-block at offset b-a < n-a). QED.
# INVERSE: given k, a = max{a : S(a) <= k} (exists: S(0)=0; unique by strict
#   increase S(a+1)-S(a)=n-a>=1); b = a + (k - S(a)) (0<=k-S(a)<n-a so b<=n-1). QED.
#   Implemented by integer binary search on S (exact) + closed-form cross-check.
# SHARD: [s,e) index interval -> pairs {unrank(k)}. Partition of [0,TOTAL):
#   union = all pairs, intersections empty (interval partition theorem). QED.
# COPRIME: no closed form used; counted by enumeration with two gcd algorithms
#   (Euclid vs Stein) required to agree. Coverage (indexing) and filtering
#   (gcd) are separate stages by construction: indexer never calls gcd.
import math
def S(a, n): return a * n - a * (a - 1) // 2
def idx_of(A, B, N):
    n = N - 1; a, b = A - 2, B - 2
    assert 2 <= A <= B <= N
    return S(a, n) + (b - a)
def unrank(k, N):
    n = N - 1
    assert 0 <= k < n * (n + 1) // 2
    lo, hi, best = 0, n - 1, 0
    while lo <= hi:  # max a with S(a) <= k
        mid = (lo + hi) // 2
        if S(mid, n) <= k: best, lo = mid, mid + 1
        else: hi = mid - 1
    a = best; b = a + (k - S(a, n))
    return a + 2, b + 2
def unrank_closed(k, N):
    import math as m  # second derivation: quadratic formula + correction (exact)
    n = N - 1
    a = int((2 * n + 1 - m.sqrt((2 * n + 1) ** 2 - 8 * k)) // 2)
    while S(a + 1, n) <= k: a += 1
    while S(a, n) > k: a -= 1
    return a + 2, a + (k - S(a, n)) + 2
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
def shard(TOTAL, shard_i, nshards):
    base, rem = divmod(TOTAL, nshards)
    s = shard_i * base + min(shard_i, rem)
    e = s + base + (1 if shard_i < rem else 0)
    return s, e
