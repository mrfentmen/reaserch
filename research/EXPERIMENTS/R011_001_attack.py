# R011_001 — attack the |off|=1 ⟹ P generalization (researcher + critic pass)
# Definitions: S=A^xa+B^xb; f=floor(S^{1/e}); low=S-f^e; high=(f+1)^e-S;
#   off = low if low<high else -high; C=f or f+1 accordingly. So S-C^e = off, C^e nearest (ties up).
# Q: is |off|=1 ==> P (triple-1 + pair-shares) a theorem? Critic: expect NO — hunt explicit counterexample.
import math, time, json
t0 = time.time()

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

def off_of(s, e):
    f = iroot(s, e)
    lo, hi = s - pow(f, e), pow(f+1, e) - s
    return (lo, f) if lo < hi else (-hi, f+1)

def cls(a, b, c):
    gab, gac, gbc = math.gcd(a,b), math.gcd(a,c), math.gcd(b,c)
    if math.gcd(gab, c) > 1: return "T"
    if gab > 1 or gac > 1 or gbc > 1: return "P"
    return "C"

# ATTACK 1: brute-force mini-search, bases 2..200, exps 3..5, full cross pairs — seek class-C |off|=1
EXPS = [3, 4, 5]
pows = sorted((pow(b, e), b, e) for b in range(2, 201) for e in EXPS)
found_C1, checked = [], 0
for i, (vi, bi, ei) in enumerate(pows):
    for vj, bj, ej in pows[i:]:
        if math.gcd(bi, bj) != 1: continue
        s = vi + vj
        checked += 1
        for e in EXPS:
            d, c = off_of(s, e)
            if abs(d) == 1 and cls(bi, bj, c) == "C":
                found_C1.append((bi, ei, bj, ej, c, e, int(d), s))
print(f"mini-search pairs checked={checked}; class-C |off|=1 counterexamples={len(found_C1)}")
for r in found_C1[:10]:
    print("  COUNTEREXAMPLE:", f"{r[0]}^{r[1]} + {r[2]}^{r[3]} = {r[7]} vs {r[4]}^{r[5]} off by {r[6]}")

# ATTACK 2: mechanism measurement on the real dataset — is P-|off|1 driven by small gaps?
import re
lines = open("/Users/dtaxk/reaserch/research prize/state/beal_near.txt").read().strip().split("\n")
pat = re.compile(r"(\d+)\^(\d+) \+ (\d+)\^(\d+) = (\d+) near (\d+)\^(\d+) off by (-?\d+)")
def gap_stats(pred):
    gaps = []
    for ln in lines:
        m = pat.fullmatch(ln.strip())
        a, xa, b, xb, s, c, xc, off = map(int, m.groups())
        if not pred(a, xa, b, xb, c, xc, off, ln): continue
        g1, g2 = abs(c-a), abs(c-b)
        gaps.append(min(g1, g2))
    gaps.sort()
    return len(gaps), (sum(gaps)/len(gaps) if gaps else None), gaps[:5]
n1, m1, _ = gap_stats(lambda a,xa,b,xb,c,xc,off,ln: abs(off)==1)
n2, m2, _ = gap_stats(lambda *x: True)
print(f"dataset: |off|=1 lines={n1} mean-min-gap={m1:.1f}; all lines={n2} mean-min-gap={m2:.1f}")
# fraction of P lines where min-gap divides both relevant bases (gap-divisibility signature)
def gapdiv_frac():
    hit = tot = 0
    for ln in lines:
        m = pat.fullmatch(ln.strip())
        a, xa, b, xb, s, c, xc, off = map(int, m.groups())
        if not (abs(off) == 1 and cls(a, b, c) == "P"): continue
        tot += 1
        g = min(abs(c-a), abs(c-b))
        base = b if abs(c-b) <= abs(c-a) else a
        if g > 0 and base % g == 0 and c % g == 0: hit += 1
    return hit, tot
h, t = gapdiv_frac()
print(f"P-|off|1 gap-divisibility signature: {h}/{t}")

# ATTACK 3: small-modulus obstruction sweep — does any m<=32 forbid class-C +-1 in-range?
mods_blocked = []
for m in range(3, 33):
    seen = set()
    for a in range(2, 60):
        for b in range(a, 60):
            for e1 in (3, 4, 5):
                for e2 in (3, 4, 5):
                    for cc in range(2, 60):
                        for e3 in (3, 4, 5):
                            if not (math.gcd(a,b)==math.gcd(a,cc)==math.gcd(b,cc)==1): continue
                            seen.add((pow(a,e1,m)+pow(b,e2,m)-pow(cc,e3,m)) % m)
    if 1 % m not in seen and (m-1) not in seen:
        mods_blocked.append(m)
print("moduli <=32 forbidding class-C +-1 residue:", mods_blocked if mods_blocked else "NONE (no small-modulus obstruction)")
print(f"runtime = {time.time()-t0:.1f}s")
json.dump({"counterexamples": len(found_C1), "ex1": found_C1[:5],
           "off1_gaps": n1, "off1_meangap": m1, "all_meangap": m2,
           "gapdiv": [h, t], "mods_blocked": mods_blocked},
          open("/Users/dtaxk/reaserch/research/ARTIFACTS/R011_001_counts.json", "w"))
