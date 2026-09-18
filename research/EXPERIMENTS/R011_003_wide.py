# R011_003 — wider falsification: bases 2..600, exps 3..7 (hunter scope), full cross pairs.
# Records ALL |off|=1 triples by class (P/T/C) + nearest-C context. A single class-C kills universality.
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
EXPS=[3,4,5,6,7]
pows=sorted((pow(b,e),b,e) for b in range(2,601) for e in EXPS)
print("powers:",len(pows),flush=True)
def cls(a,b,c):
    gab,gac,gbc=math.gcd(a,b),math.gcd(a,c),math.gcd(b,c)
    if math.gcd(gab,c)>1: return "T"
    if gab>1 or gac>1 or gbc>1: return "P"
    return "C"
hits=[]; checked=0; t1=time.time()
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
    if i%500==0: print(f"  i={i}/{len(pows)} checked={checked} hits={len(hits)} {time.time()-t1:.0f}s",flush=True)
from collections import Counter
print("checked pairs:",checked,"|off|=1 hits:",len(hits),"by class:",dict(Counter(h[7] for h in hits)))
for h in hits[:20]: print("  HIT:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}",flush=True)
json.dump({"checked":checked,"hits":hits},open("research/ARTIFACTS/R011_003_counts.json","w"))
print("TOTAL",time.time()-t0,flush=True)
