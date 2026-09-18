# R014 optimized implementation (C20 residue guards + C21 exponent-gcd skip; Newton root; Stein gcd)
# Tables REGENERATED from definitions below (never imported). Claim domain unchanged.
import math
EXPS = [3, 4, 5, 6, 7]
MOD = {3: 9, 4: 16, 5: 11, 6: 9, 7: 29}
RES = {e: {pow(c, e, MOD[e]) for c in range(MOD[e])} for e in EXPS}  # generated, complete over Z/mZ
SKIP21 = {(x, y, e) for x in EXPS for y in EXPS for e in EXPS if math.gcd(math.gcd(x, y), e) > 2}
def newt_root(v, e):
    if v <= 0: return 0
    x = 1 << ((v.bit_length() + e - 1) // e + 1)
    while True:
        y = ((e - 1) * x + v // pow(x, e - 1)) // e
        if y >= x: break
        x = y
    while pow(x + 1, e) <= v: x += 1
    while pow(x, e) > v: x -= 1
    return x
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
def opt_class(a, b, c):
    gab, gac, gbc = stein(a, b), stein(a, c), stein(b, c)
    if stein(gab, c) > 1: return "T"
    if gab > 1 or gac > 1 or gbc > 1: return "P"
    return "C"
def opt_eval(A, xa, B, xb, e, stats=None):
    """Same contract as ref_eval, plus C20/C21 guards. stats counts guard hits when provided."""
    if (xa, xb, e) in SKIP21:
        if stats is not None: stats["c21"] += 1
        return "SKIP21", None, None
    s = pow(A, xa) + pow(B, xb)
    if s % MOD[e] not in RES[e]:
        if stats is not None: stats["c20"] += 1
        return "SKIP20", None, None
    f = newt_root(s, e)
    lo, hi = s - pow(f, e), pow(f + 1, e) - s
    d, c = (lo, f) if lo < hi else (-hi, f + 1)
    assert pow(c, e) == s - int(d)
    if stats is not None: stats["exact"] += 1
    return int(d), c, opt_class(A, B, c)
