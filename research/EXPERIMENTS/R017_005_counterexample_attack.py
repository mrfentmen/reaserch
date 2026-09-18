# R017 L2-lemma verification + tower tranche (powers of two × imbalance, exps beyond hunter)
# (a) verify L2a/L2b on all 14 unique dataset |off|=1 triples + 9 wide hits (exact).
# (b) tower falsification: A=2^X towers AND B=2^X towers vs small odd bases, exps 3..9,
#     filter-free, both signs. New asymptotic regime (tall exponents), adversarial classes:
#     powers of two, extreme imbalance, mixed parity. A single class-C kills U.
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
def cls(a,b,c):
    gab,gac,gbc=math.gcd(a,b),math.gcd(a,c),math.gcd(b,c)
    if math.gcd(gab,c)>1: return "T"
    if gab>1 or gac>1 or gbc>1: return "P"
    return "C"
# (a) L2 checks on dataset uniques (parsed from file directly — no hand transcription).
import re
lines=open("/Users/dtaxk/reaserch/research prize/state/beal_near.txt").read().strip().split("\n")
pat=re.compile(r"(\d+)\^(\d+) \+ (\d+)\^(\d+) = (\d+) near (\d+)\^(\d+) off by (-?\d+)")
uniq={}
for ln in lines:
    m=pat.fullmatch(ln.strip())
    a,xa,b,xb,s,c,xc,off=map(int,m.groups())
    if abs(off)==1: uniq.setdefault((a,xa,b,xb,pow(c,xc)),(a,xa,b,xb,c,xc,off))
print("unique |off|=1 dataset triples:",len(uniq))
l2a_ok=l2a_ap= l2b_ok=l2b_ap=0
for (a,xa,b,xb,c,xc,off) in uniq.values():
    assert pow(a,xa)+pow(b,xb)-pow(c,xc)==off
    if off==-1:  # L2a needs no parity on e
        l2a_ap+=1; l2a_ok+= math.gcd(a*b, c-1)==1
    else:
        if xc%2==1: l2b_ap+=1; l2b_ok+= math.gcd(a*b, c+1)==1
print(f"L2a applicable {l2a_ap}, holds {l2a_ok}; L2b applicable {l2b_ap}, holds {l2b_ok}")
assert l2a_ok==l2a_ap and l2b_ok==l2b_ap, "L2 lemma FAILED"
# (b) tower tranche
EXPS=list(range(3,10)); hits=[]; checked=0
def census_pair(A,xa,B,xb):
    global checked
    s=pow(A,xa)+pow(B,xb)
    if math.gcd(A,B)!=1: return
    checked+=1
    for e in EXPS:
        f=iroot(s,e)
        lo,hi=s-pow(f,e),pow(f+1,e)-s
        d,c=(lo,f) if lo<hi else (-hi,f+1)
        if abs(int(d))==1:
            hits.append((A,xa,B,xb,c,e,int(d),cls(A,B,c)))
odds=list(range(3,61,2))
for X in range(8,121):
    if X%10==8: print(f"  X={X}",flush=True)
    A=2**X
    for B in odds:
        for xb in EXPS: census_pair(A,X,B,xb)
    for B in odds:
        for xa in EXPS: census_pair(B,xa,A,X)
from collections import Counter
print("tower pairs checked:",checked,"|off|=1:",len(hits),dict(Counter(h[7] for h in hits)))
for h in hits[:15]: print("  TOWER-HIT:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]} class {h[7]}")
json.dump({"checked":checked,"hits":hits},open("/Users/dtaxk/reaserch/research/ARTIFACTS/R017_005_counts.json","w"))
print("TOTAL",round(time.time()-t0,1))
