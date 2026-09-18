# R011_002 — size-bias firewall: is |off|=1 ⟹ P explained by P-enrichment at large S?
# Q: P-fraction as function of S magnitude; S-distribution of |off|=1 vs rest.
# If |off|=1 lines live where P-rate is ~0.8+, then 12/12 unique needs no theorem (p~0.07).
import re, math
lines = open("/Users/dtaxk/reaserch/research prize/state/beal_near.txt").read().strip().split("\n")
pat = re.compile(r"(\d+)\^(\d+) \+ (\d+)\^(\d+) = (\d+) near (\d+)\^(\d+) off by (-?\d+)")
def cls(a,b,c):
    gab,gac,gbc = math.gcd(a,b),math.gcd(a,c),math.gcd(b,c)
    if math.gcd(gab,c)>1: return "T"
    if gab>1 or gac>1 or gbc>1: return "P"
    return "C"
import collections
bins = collections.Counter(); pbins = collections.Counter()
off1_S, rest_S = [], []
seen_off1 = set(); uniq_off1_P = 0
for ln in lines:
    m = pat.fullmatch(ln.strip())
    a,xa,b,xb,s,c,xc,off = map(int, m.groups())
    k = len(str(s))  # magnitude bin = digits of S
    bins[k] += 1
    cc = cls(a,b,c)
    if cc == "P": pbins[k] += 1
    (off1_S if abs(off)==1 else rest_S).append(s)
    if abs(off)==1:
        key = (a,xa,b,xb,pow(c,xc))
        if key not in seen_off1:
            seen_off1.add(key)
            if cc == "P": uniq_off1_P += 1
print("digits(S): total / P-fraction")
for k in sorted(bins): print(f"  {k}d: n={bins[k]} P-rate={pbins[k]/bins[k]:.3f}")
print(f"|off|=1 unique triples: {len(seen_off1)}, in P: {uniq_off1_P}")
def med(v):
    v = sorted(v); n = len(v); return v[n//2]
print(f"median S: |off|=1 -> {med(off1_S):.3e}; rest -> {med(rest_S):.3e}")
# null-model p-value: product over unique off1 triples of bin-P-rate (independence assumption, stated)
import functools
ps = []
for ln in lines:
    m = pat.fullmatch(ln.strip())
    a,xa,b,xb,s,c,xc,off = map(int, m.groups())
    if abs(off) != 1: continue
    key = (a,xa,b,xb,pow(c,xc))
    if key in seen_off1:
        seen_off1.discard(key)
        ps.append(pbins[len(str(s))]/bins[len(str(s))])
p = functools.reduce(lambda x,y: x*y, ps, 1.0)
print(f"null-model P(all {len(ps)} unique off1 in P | bin rates) = {p:.3e}")
print("unique off1 count check:", len(ps))
