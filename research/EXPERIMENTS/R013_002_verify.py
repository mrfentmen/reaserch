# R013_002 — evidence repair: re-run Stage-A domain SAVING all P-hit details + closed-form coverage recheck
import math, time, json
t0=time.time()
def newton_floor(v,e):
    if v<=0: return 0
    x=1<<((v.bit_length()+e-1)//e+1)
    while True:
        y=((e-1)*x+v//pow(x,e-1))//e
        if y>=x: break
        x=y
    while pow(x+1,e)<=v: x+=1
    while pow(x,e)>v: x-=1
    return x
def stein(a,b):
    if a==0: return b
    if b==0: return a
    s=0
    while not (a&1|b&1): a>>=1;b>>=1;s+=1
    while not a&1: a>>=1
    while b:
        while not b&1: b>>=1
        if a>b: a,b=b,a
        b-=a
    return a<<s
# coverage closed forms
for name,rng in (("A",range(2,151)),("B",range(2,61)),("CTRL",range(2,41))):
    n=len(rng); assert n*(n+1)//2=={ "A":11175,"B":1770,"CTRL":780}[name], name
print("closed-form basepair counts CONFIRMED: A=11175 B=1770 CTRL=780")
# independent coprime-basepair count (Euclid, vs run's Stein) for Stage A
ca=sum(1 for A in range(2,151) for B in range(A,151) if math.gcd(A,B)==1)
print("Stage-A coprime base pairs (Euclid recount):",ca,"=> pairchecks expect",ca*36)
EXPS=[3,4,5,6,7,8]
hits=[]
for A in range(2,151):
    for B in range(A,151):
        if stein(A,B)!=1: continue
        for xa in EXPS:
            for xb in EXPS:
                s=pow(A,xa)+pow(B,xb)
                for e in EXPS:
                    f=newton_floor(s,e)
                    lo,hi=s-pow(f,e),pow(f+1,e)-s
                    d,c=(lo,f) if lo<hi else (-hi,f+1)
                    if abs(int(d))==1:
                        gab,gac,gbc=stein(A,B),stein(A,c),stein(B,c)
                        k="T" if math.gcd(gab,c)>1 else ("P" if gab>1 or gac>1 or gbc>1 else "C")
                        hits.append((A,xa,B,xb,c,e,int(d),k))
from collections import Counter
print("hits:",len(hits),dict(Counter(h[7] for h in hits)),"unique:",len({(h[0],h[1],h[2],h[3],pow(h[4],h[5])) for h in hits}))
for h in hits: print("  HIT:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}")
json.dump({"hits":hits},open("/Users/dtaxk/reaserch/research/ARTIFACTS/R013_002_hits.json","w"))
print("TOTAL",round(time.time()-t0,1))
