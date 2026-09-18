# R018 mechanized local classification for A^x+B^y-C^e=±1 (finite exhaustion = proof per instance)
# For (modulus m, exps): enumerate ALL residue triples; for each zero-pattern (which of A,B,C =0 mod p grid)
# record achievable D-values; a (pattern,eps) with eps unreachable is PROVEN impossible.
# Then: assert every observed integer-equation hit complies; report C-compatible witness patterns.
import math, json
def residues(powspec):
    m, exps = powspec
    R = {}
    for e in set(exps):
        R[e] = sorted({pow(a, e, m) for a in range(m)})
    return R
def classify(m, xa, xb, e):
    """returns (residue_sets, forbidden[(zpat,eps)], allowed C-compatible witnesses)"""
    Rx = sorted({pow(a, xa, m) for a in range(m)})
    Ry = sorted({pow(a, xb, m) for a in range(m)})
    Re = sorted({pow(a, e, m) for a in range(m)})
    forb, wit = [], {}
    # zero-patterns keyed by divisibility proxy: use representative residues 0 vs nonzero set
    for za in (False, True):
        for zb in (False, True):
            for zc in (False, True):
                XA = [0] if za else [r for r in Rx if r != 0]
                XB = [0] if zb else [r for r in Ry if r != 0]
                XC = [0] if zc else [r for r in Re if r != 0]
                if not (XA and XB and XC): continue
                Ds = {(a + b - c) % m for a in XA for b in XB for c in XC}
                for eps in (1, m - 1):
                    if eps not in Ds:
                        forb.append(((za, zb, zc), 1 if eps == 1 else -1))
                    elif not (za or zb or zc):
                        wit.setdefault(1 if eps == 1 else -1, (XA[0], XB[0], XC[0]))
    return (Rx, Ry, Re), forb, wit
INST = [("cubes@9", 9, 3, 3, 3), ("cubes@7", 7, 3, 3, 3), ("fourth@16", 16, 4, 4, 4),
        ("fifth@11", 11, 5, 5, 5), ("sixth@9", 9, 6, 6, 6), ("sixth@7", 7, 6, 6, 6),
        ("eighth@17", 17, 8, 8, 8), ("tenth@11", 11, 10, 10, 10), ("parity@2-(3,4,5)", 2, 3, 4, 5),
        ("mixed443@16", 16, 4, 3, 3)]
for name, m, xa, xb, e in INST:
    (Rx, Ry, Re), forb, wit = classify(m, xa, xb, e)
    npat = len(forb)
    print(f"{name}: Rx={Rx} Ry={Ry} Re={Re}")
    print(f"   forbidden (zeropat,eps): {forb}")
    print(f"   C-compatible witnesses (eps->residues): {wit}")
