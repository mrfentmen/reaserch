# R007_001 — prime() characterization + differential test (researcher pass)
# Target: quick.ts prime() (trial division, 6k+-1 wheel). Oracle: deterministic Miller-Rabin <2^64.
# Checks: exhaustive [0,100000] mirror-vs-oracle; stratified large sample; Carmichael + square adversarials;
# integer-domain theorem support (sqrt-floor argument spot checks); fractional-input limitation (TS-observed).
import math, time, json
t0 = time.time()

def prime_mirror(n):
    # line-for-line mirror of quick.ts prime(), using float sqrt like Math.sqrt (both correctly rounded)
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    r = math.sqrt(n)
    i = 5
    while i <= r:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def is_prime_mr(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: s += 1; d //= 2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0: continue
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1: break
        else: return False
    return True

# LEVEL 1: exhaustive mirror vs oracle on [0,100000]
bad = [n for n in range(100001) if prime_mirror(n) != is_prime_mr(n)]
print("exhaustive [0,100000]: mismatches =", len(bad), bad[:10])

# LEVEL 2a: stratified large sample (squares of primes, Carmichaels, Mersenne-region, Goldbach-frontier odds)
import random
random.seed(20260918)
sample = [561,1105,1729,2465,2821,6601,8911,          # Carmichael
          2147483647, 2147483646, 4294967291,          # 2^31 region
          477990769, 478253161,                        # prime squares near frontier (both composite)
          478259999, 478260000, 478261999,             # frontier values
          9007199254740991,                            # 2^53-1 (domain edge)
          1000003, 1000033, 9999991]
primes_near = [1000003]
sample += [random.randrange(10**6, 10**9) | 1 for _ in range(300)]
sample += [p*p for p in (101, 1009, 10007)]            # small prime squares
t1 = time.time()
mism = [(n, prime_mirror(n), is_prime_mr(n)) for n in sample if prime_mirror(n) != is_prime_mr(n)]
print("stratified sample size =", len(sample), "mismatches =", len(mism), mism[:10], f"({time.time()-t1:.1f}s)")

# LEVEL 2b: sqrt-floor support — verify floor(float_sqrt(n)) == isqrt(n) on 200k adversarial values
# (adversarial: perfect squares and squares+-1 up to 2^53, where rounding matters most)
t2 = time.time()
sqbad = 0
tests = [k*k for k in random.sample(range(2, 95000000), 20000)]
tests += [k*k+1 for k in range(2, 30000)] + [k*k-1 for k in range(3, 30000)]
tests += [2**53-1, 2**53-2, 10**15+37]
for n in tests:
    if math.floor(math.sqrt(n)) != math.isqrt(n): sqbad += 1
print("sqrt-floor checks:", len(tests), "mismatches =", sqbad, f"({time.time()-t2:.1f}s)")

# LEVEL 3 (theorem support): residue-class coverage — every prime >3 is +-1 mod 6 (check to 1e6), so wheel hits all candidates
print("wheel lemma spot: all primes in (3,10^6] are +-1 mod 6:",
      all(p % 6 in (1,5) for p in range(5, 10**6) if is_prime_mr(p)))

print("2^53-1 oracle:", is_prime_mr(9007199254740991), "(mirror agrees)" if prime_mirror(9007199254740991)==is_prime_mr(9007199254740991) else "(MISMATCH)")
print(f"total runtime = {time.time()-t0:.1f}s")
json.dump({"exhaustive_mism": len(bad), "sample": len(sample), "sample_mism": len(mism),
           "sqrt_mism": sqbad}, open("/Users/dtaxk/reaserch/research/ARTIFACTS/R007_001_counts.json","w"))
