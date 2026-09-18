# R013_001 — independent falsification search (deliberately non-lineage implementation)
# INDEPENDENCE (vs beal.ts / R004/R011 scripts):
#  - enumeration: base-major (A<=B) x exponent-grid (vs value-sorted power list)
#  - root: Newton's method primary (vs binary search); binary kept ONLY as assert-oracle per (S,e)
#  - gcd: hand-written binary GCD/Stein (vs Euclidean); math.gcd kept ONLY as assert-oracle
#  - detection: direct-D formulation (vs floorRoot+low/high); nearest-C agreement asserted
#  - NO hunter filters: no S>1e6, no ratio, no blocks, exps to 14, C21 NOT applied anywhere
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
def binary_floor(v,e):
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
def cls_stein(a,b,c):
    gab,gac,gbc=stein(a,b),stein(a,c),stein(b,c)
    assert (gab, gac, gbc)==(math.gcd(a,b),math.gcd(a,c),math.gcd(b,c)), "stein-vs-euclid disagree"
    if math.gcd(gab,c)>1: return "T"
    if gab>1 or gac>1 or gbc>1: return "P"
    return "C"
root_disagree=0
def scan(A_rng, EXPS, label, prefilter=True, note=""):
    global root_disagree
    pairs=checked=hitsP=hitsC=hitsT=plus=minus=0
    uniq=set(); det=[]
    for A in A_rng:
        for B in A_rng:
            if B<A: continue
            pairs+=1
            if prefilter and stein(A,B)!=1: continue
            for xa in EXPS:
                for xb in EXPS:
                    s=pow(A,xa)+pow(B,xb); checked+=1
                    for e in EXPS:
                        fn=newton_floor(s,e); fb=binary_floor(s,e)
                        if fn!=fb: root_disagree+=1; continue
                        lo,hi=s-pow(fn,e),pow(fn+1,e)-s
                        d,c=(lo,fn) if lo<hi else (-hi,fn+1)
                        if abs(int(d))==1:
                            k=cls_stein(A,B,c)
                            if k=="P": hitsP+=1
                            elif k=="C":
                                hitsC+=1; det.append((A,xa,B,xb,c,e,int(d)))
                            else: hitsT+=1
                            if int(d)==1: plus+=1
                            else: minus+=1
                            uniq.add((A,xa,B,xb,pow(c,e)))
    print(f"{label}: basepairs={pairs} pairchecks={checked} off1:P={hitsP} C={hitsC} T={hitsT} (+1:{plus}/-1:{minus}) unique={len(uniq)} {note}",flush=True)
    return det
print("== STAGE A (bases 2..150, exps 3..8, prefiltered; must rediscover 71/138/144, 73/144/150, 1729-family) ==",flush=True)
dA=scan(range(2,151),[3,4,5,6,7,8],"A")
print("== STAGE B (bases 2..60, exps 3..14, prefiltered; exponent-regime extension) ==",flush=True)
dB=scan(range(2,61),list(range(3,15)),"B")
print("== STAGE C (adversarial classes, exps 3..12, prefiltered) ==",flush=True)
primes=[p for p in range(2,201) if all(p%q for q in range(2,int(p**0.5)+1))]
twinB=sorted({b for p in primes for b in (p,p+2) if b<=202})
comp=[30,42,60,66,70,78,84,90,96,102,108,114,120]
pow2=[4,8,16,32,64,128]
imbal=[(a,b) for a in range(2,11) for b in range(500,560)]
advBases=sorted(set(twinB+comp+pow2+[a for a,b in imbal]+[b for a,b in imbal]))
dC=scan(advBases,[3,4,5,6,7,8,9,10,11,12],"C")
print("== CONTROL (bases 2..40, exps 3..6, NO prefilter; machinery check on all gcd relations) ==",flush=True)
dT=scan(range(2,41),[3,4,5,6],"CTRL",prefilter=False)
print("root newton-vs-binary disagreements:",root_disagree)
allC=dA+dB+dC
print("CLASS-C COUNTEREXAMPLES:",len(allC))
for h in allC[:20]: print("  COUNTEREXAMPLE:",f"{h[0]}^{h[1]} + {h[2]}^{h[3]} vs {h[4]}^{h[5]} off {h[6]}",flush=True)
json.dump({"counterexamples":allC,"root_disagree":root_disagree},open("/Users/dtaxk/reaserch/research/ARTIFACTS/R013_001_counts.json","w"))
print("TOTAL",round(time.time()-t0,1))
