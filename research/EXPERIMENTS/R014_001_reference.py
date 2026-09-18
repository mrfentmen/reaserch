# R014 reference implementation (slow, exact, obviously-correct; NO optimizations)
# Root: binary search. GCD: Euclid (math.gcd). Detection: direct-D. No C20/C21/filters.
import math
def biref_root(v, e):
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
def ref_class(a, b, c):
    gab, gac, gbc = math.gcd(a, b), math.gcd(a, c), math.gcd(b, c)
    if math.gcd(gab, c) > 1: return "T"
    if gab > 1 or gac > 1 or gbc > 1: return "P"
    return "C"
def ref_eval(A, xa, B, xb, e):
    """Return (d, C, cls) exactly, or None if pair prefiltered (caller handles)."""
    s = pow(A, xa) + pow(B, xb)
    f = biref_root(s, e)
    lo, hi = s - pow(f, e), pow(f + 1, e) - s
    d, c = (lo, f) if lo < hi else (-hi, f + 1)
    assert pow(c, e) == s - int(d)  # definitional identity, checked every call
    return int(d), c, ref_class(A, B, c)
