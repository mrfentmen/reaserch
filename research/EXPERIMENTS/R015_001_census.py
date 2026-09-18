# R015_001 — unpruned full-cross |off|=1 census, bases 2..1000, exps 3..7 (NO pruners, NO prefilter except claim-scope (A,B)=1)
# Motivation: hunter never examined inter-block pairs (77.8% gap); R014 proved pruners census-unsafe.
# Reference logic (binary root + Euclid + direct-D), base-major enumeration. Saves every |off|=1 hit.
import math, time, json
t0=time.time()
EXPS=[3,4,5,6,7]; BMAX=1000
def biref_root(v,e):
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
N=BMAX-1
assert N*(N+1)//2==499500, "base-pair closed form"
cop=tot=hP=hC=hT=plus=minus=0
uniq=set(); hits=[]
t1=time.time()
for A in range(2,BMAX+1):
    for B in range(A,BMAX+1):
        tot+=1
        if math.gcd(A,B)!=1: continue
        cop+=1
        for xa in EXPS:
            va=pow(A,xa)
            for xb in EXPS:
                s=va+pow(B,xb)
                for e in EXPS:
                    f=biref_root(s,e)
                    lo,hi=s-pow(f,e),pow(f+1,e)-s
                    d,c=(lo,f) if lo<hi else (-hi,f+1)
                    if abs(int(d))==1:
                        gab,gac,gbc=math.gcd(A,B),math.gcd(A,c),math.gcd(B,c)
                        k="T" if math.gcd(gab,c)>1 else ("P" if gab>1 or gac>1 or gbc>1 else "C")
                        if k=="P": hP+=1
                        elif k=="C": hC+=1
                        else: hT+=1
                        if int(d)==1: plus+=1
                        else: minus+=1
                        uniq.add((A,xa,B,xb,pow(c,e)))
                        hits.append((A,xa,B,xb,c,e,int(d),k))
    if A%250==0: print(f"  A={A} hits={len(hits)} {time.time()-t1:.0f}s",flush=True)
from collections import Counter
print(f"basepairs={tot} coprime={cop} off1:P={hP} C={hC} T={hT} (+1:{plus}/-1:{minus}) unique={len(uniq)}",flush=True)
for h in hits: print("  HIT:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}",flush=True)
json.dump({"hits":hits},open("research/ARTIFACTS/R015_001_hits.json","w"))
print("TOTAL",round(time.time()-t0,1),flush=True)
