import sys
import mpmath
mpmath.mp.dps = 50
re = mpmath.mpf(sys.argv[1])
t = mpmath.mpf(sys.argv[2])
z = mpmath.zeta(mpmath.mpc(re, t))
print(f"mag={abs(z)}")
print("ZERO-CANDIDATE" if abs(z) < mpmath.mpf("1e-6") else "not-zero")
