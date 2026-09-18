# R011_004 — higher-exponent tranche (filter-free falsification outside hunter scope)
# Hunter caps exps at 7 and requires S>1e6 + ratio<999 + intra-block. This tranche drops ALL of that:
# bases 2..60, exps 3..12, full cross pairs, every |off|=1 classified. A single class-C kills universality.
import math, time, json
t0=time.time()
def iroot(v,e):
    hi=1<<((v.bit_length()+e-1)//e+1)
    if hi>v: hi=v
    lo,best=1,1
    while lo<=hi:
        mid=(lo+hi)//2
        p=pow(mid,e)
        if p==v: return mid
        if p<v: best,lo=mid,mid+1
        else: hi=mid-1
    return best
EXPS=list(range(3,13))
pows=sorted((pow(b,e),b,e) for b in range(2,61) for e in EXPS)
def cls(a,b,c):
    gab,gac,gbc=math.gcd(a,b),math.gcd(a,c),math.gcd(b,c)
    if math.gcd(gab,c)>1: return "T"
    if gab>1 or gac>1 or gbc>1: return "P"
    return "C"
hits=[]; checked=0
for i,(vi,bi,ei) in enumerate(pows):
    for vj,bj,ej in pows[i:]:
        if math.gcd(bi,bj)!=1: continue
        s=vi+vj; checked+=1
        for e in EXPS:
            f=iroot(s,e)
            lo,hi=s-pow(f,e),pow(f+1,e)-s
            d,c=(lo,f) if lo<hi else (-hi,f+1)
            if abs(int(d))==1:
                hits.append((bi,ei,bj,ej,c,e,int(d),cls(bi,bj,c)))
from collections import Counter
print("pairs:",checked,"|off|=1:",len(hits),dict(Counter(h[7] for h in hits)))
for h in hits: print("  HIT:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}")
json.dump({"checked":checked,"hits":hits},open("/Users/dtaxk/reaserch/research/ARTIFACTS/R011_004_counts.json","w"))
print("TOTAL",round(time.time()-t0,1))
