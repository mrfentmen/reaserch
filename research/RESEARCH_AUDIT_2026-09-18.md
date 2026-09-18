# Research audit — 2026-09-18 (UTC)

Cloned `https://github.com/mrfentmen/reaserch/` commit `ce27494`
("Snapshot research state…") into `/Users/dtaxk/reaserch` and audited every
hunter by reading the actual files and executing the actual code. No result
below is claimed without an executed check. Diet Coke #2 of the day; ashtray
getting full — the Riemann hunter annoyed me enough to chain-smoke through
the error analysis.

## 1. What is in the repo (PROVEN by inspection)

- `research prize/beal.ts` — Beal counterexample search (exact BigInt arithmetic).
  Scope as run: bases partitioned into blocks
  2–2000, 2001–3000, 3001–4000, 4001–5000, 5001–6000; exponents 3–7.
- `research prize/riemann.ts` + `riemann_loop.ts` — off-critical-line zeta-zero
  sampling via Euler–Maclaurin (float64), re in {0.2,0.3,0.4,0.6,0.7,0.8},
  step 0.25, `|z|<0.01 && err<0.015` trigger with `verify_zeta.py` (mpmath)
  as second opinion.
- `research prize/quick.ts` — combined Goldbach (even g) + Collatz (odd g+1)
  scan from 1,000,000; checkpoint `quick.txt` = 478260000.
- `research prize/watch.sh`, `relaunch.sh` — supervisor loops.
- `hunters_state/gap.*` — prime-gap scan near 9e15; `gap_records.txt` = 57
  window-local records; `gap.txt` = 9000000301989888 (scan frontier).
- `hunters_state/erdos.*`, `hunters_state_test/erdos.*` — logs only
  (`selftest ok`, `scan n=… done=…`, step 25 from n=1000024). **No source
  committed.** Conjecture under test is UNKNOWN.
- All TS hunters hardcode `/Users/dtaxk/Desktop/research prize/state`,
  which does not exist on this machine (verified `ls`). The committed code
  **cannot run as-is** from the repo path. Reproducibility failure.

## 2. Beal hunter — audit

### 2a. Arithmetic core: CORRECT (COMPUTATIONAL EVIDENCE → spot-PROVEN)
- `floorRoot` binary search with `mid**BigInt(e)` is exact. Tested:
  all exact powers b^e for 2≤b<50, 3≤e≤7 round-trip; v±1 boundaries;
  200 random sums invariant `f^e ≤ s < (f+1)^e`. Result: `floorRoot OK`.
- Pairwise-coprime skip is VALID: if p divides any two of (A,B,C) in
  A^x+B^y=C^z then p divides the third. So requiring gcd(A,B)=gcd(A,C)=
  gcd(B,C)=1 is equivalent to gcd(A,B,C)=1 *given* the equation holds.
  Skipping non-coprime (A,B) pairs cannot discard a counterexample. PROVEN
  by elementary divisibility (three-line lemma, checked).
- Checkpoints match theory exactly (executed Python count):
  coprime power-pairs 2–2000 = 30,364,700 = `beal_2000_7_0_1.txt`;
  2001–3000 = 7,594,225; 3001–4000 = 7,595,825; 4001–5000 = 7,604,950;
  5001–6000 = 7,594,125 — all equal their checkpoint files and all shards
  log `done shard=0 pairs=…`. So each **intra-block** shard ran to completion
  with no FOUND. That much is real.

### 2b. Coverage: INCOMPLETE — critical sharding bug (PROVEN)
- Each shard builds powers only for bases in its own interval
  (`for base=bmin..max`) and checks pairs *within* that set. Pairs with
  bases in *different* intervals (e.g. A=2, B=5000) are never examined.
- Executed count: full-range (2–6000, exps 3–7) coprime power-pairs =
  273,429,100. Intra-block sum = 60,753,825 (22.2%). **Missing = 212,675,275
  pairs (77.8%).**
- Therefore the claim "Beal searched to 6000" is FALSE as a full-bound
  statement. Correct statement: "all intra-block pairs with both bases in
  the same 1000/2000-block, exps 3–7, checked; no counterexample there."
- Additional limits: exponents capped at 7; literature GPU searches cover
  bounds to 500,000 with exps 3–15 (pscamillo/beal_bigint, ~20k hits, 0
  coprime). Our bound is far below state of the art. NOVELTY NOT ESTABLISHED.

### 2c. Near-miss file: mathematically uninteresting (PROVEN on data)
- `beal_near.txt` = 3058 lines, filter `ad≤1000`, no coprimality-vs-C filter.
- 19 lines with |off|=1 examined: **every one** has triple-gcd 1 but a
  pairwise common factor (e.g. 71^3+138^3 vs 144^3, gcd(138,144)=6).
  By the lemma in 2a, exact equality is then *impossible* mod p — these are
  provably non-solutions, not "almost counterexamples". The log also
  double-counts values with multiple (base,exp) names (144^3 = 12^6).
- Lesson: near-miss hunting without the coprimality filter is noise.

### 2d. Small CORRECT result produced today (PROVEN, reproducible)
- `/tmp/beal_correct_small.py`: full cross-coverage exhaustive check,
  2≤A,B≤100, exps {3,4,5}, exact integer nth-root, 26,496 coprime pairs,
  0.3 s. **Result: no counterexample in that scope.** Small, but the
  coverage claim is actually true (unlike the 6000 claim).

## 3. Riemann hunter — audit (the bad one)

### 3a. Low-t behavior: CORRECT
- `bun riemann.ts selftest`: zero1 mag≈1.1e-7, offline≈0.126, zero2≈4.1e-7,
  `TRUST-HIGH`. Reproduced. mpmath cross-check agrees (0.5+14.1347i
  mag≈2.7e-11; 0.6+14i mag≈0.1264; 0.2+100i mag≈4.3827 matches EM 4.383).

### 3b. High-t behavior: VACUOUS — precise obstruction identified (PROVEN)
- For t≳2500, n saturates at 5000 while |s|≈t keeps growing. EM correction
  magnitude ≈ (|s|/n)^{2k-1}·n^{-σ} grows; executed measurements:
  t=10k err≈9.7e-6 (still <0.015); t=12k 5.0e-5; 15k 3.7e-4; 20k 5.0e-3;
  **25k 3.7e-2 (exceeds gate)**; 30k 0.19; 40k 2.55; 50k 19; 100k 9730.
- Binary-search boundary (executed): re=0.2 gate fails above t≈22,604;
  re=0.8 above t≈29,997. The trigger requires err<0.015, so beyond ~22–30k
  the hunter **can never fire** — it just logs `scan t=…` while checking
  nothing.
- `riemann.txt` = 1095200 therefore does NOT mean "RH verified/sampled to
  1,095,200". At most the prefix t∈[200, ~22k] was sampled with a working
  error gate; everything beyond is CPU-burning theater. And even the valid
  prefix is heuristic sampling (step 0.25 at 6 off-line σ values), not a
  Turing-method verification. Literature: RH rigorously verified to height
  3e12 (Platt–Trudgian 2020, interval arithmetic). Our valid reach is ~8
  orders of magnitude below, and the method cannot be extended by raising n
  in float64 — needs Riemann–Siegel + Turing + interval arithmetic.
- FAILED APPROACH recorded: fixed-n Euler–Maclaurin with err-gate as an
  "RH verification up to 1M" is unsound. The logs must be relabeled.

## 4. quick.ts (Goldbach + Collatz) — audit

- `prime()` trial division verified correct to 100k against a sieve
  (executed, no mismatches). `gold()` correct on 4–100 (executed).
- Throughput measured: ~6,450 evens/s near 478M (2000 evens in 310 ms),
  so 1M→478M in ~20 h of single-thread burn is plausible; checkpoint
  478260000 accepted as COMPUTATIONAL EVIDENCE (not independently
  re-run in full — would take ~20 h; stamina I have, time in this session
  I don't).
- Independent spot verification executed: segmented sieve over
  478,260,000–478,262,000 (1001 evens) — all have Goldbach partitions
  (13.1 s, exact); Collatz for corresponding odds all reach 1 within guards
  (0.1 s, exact). No bug found in the sampled window.
- Novelty: NONE. Goldbach verified to 4e18 (Oliveira e Silva–Herzog–Pardi
  2013); Collatz to ~2.9e20 / 2^68 (Barina). Our 4.78e8 is ~10 orders below
  both. Correct but superseded. Continued burning on this exact code is not
  research progress; at best a heartbeat.

## 5. Prime gaps — audit

- All 57 `gap_records.txt` lines verified today with deterministic
  Miller–Rabin (bases for <2^64): every p and p+gap prime, no interior
  primes, merit = gap/ln(p)² matches to 2e-4. **57/57 VALID (0.1 s).**
  Largest: p=9000000147878479, gap=538, merit 0.3987 — endpoints and
  emptiness re-verified.
- BUT these are window-local maxima from ~9e15 to ~9.0000003e15 (≈300M
  wide), not global prime-gap records. Gaps of 500+ occur far below 9e15
  in the published tables (to 4e18 / 2^64). Must never be cited as global
  records. Scan frontier `gap.txt` = 9000000301989888.

## 6. Erdos hunter — UNVERIFIABLE

- No source in repo (only `erdos.log/txt/pid`). Log shows `selftest ok`
  then `scan n=1000024,1000049,…` step 25, frontier 1159620 (main) /
  1000924 (test). Without the tested predicate, selftest content, or
  arithmetic (exact vs float), **no claim can be evaluated**. UNKNOWN
  PROVENANCE. Next: recover source from Desktop backups/Time Machine or
  declare the logs orphaned and stop citing them.

## 7. Research state (honest ledger)

- PROVEN: Beal intra-block completion (stated scope only); Beal ≤100 full
  cross-coverage (today); floorRoot exactness (tested scope); prime()
  correctness to 1e5; gap 57/57 validity; Riemann EM-vs-mpmath agreement
  where err-gate holds; Riemann gate-failure boundary ~22.6k (re=0.2).
- COMPUTATIONAL EVIDENCE (unreproduced in full here, plausible):
  Goldbach+Collatz to 478,260,000; Beal intra-block shards; gap scan to
  9.0000003e15.
- FAILED / INVALID: Riemann "to 1,095,200" (vacuous beyond ~22k); Beal "to
  6000" as full bound (77.8% pairs unexamined); near-miss significance;
  any novelty claim vs literature (all bounds superseded by 8–10 orders).
- UNVERIFIED / UNKNOWN: entire erdos line (missing source); full
  re-execution of the 478M and 60M-pair scans in this environment.
- NEXT (in order): (1) recover or drop erdos hunter; (2) either fix Beal
  sharding to pair-index sharding with cross coverage, or stop and cite
  literature instead of re-burning 273M pairs in slow TS; (3) retire the
  Riemann EM hunter beyond 22k — replace with Riemann–Siegel/Turing or
  restrict claims to the valid prefix; (4) fix hardcoded Desktop paths to
  repo-relative paths so anyone can reproduce; (5) stop presenting
  Goldbach/Collatz/gap heartbeats as progress.

## 8. Reproduction recipes (all executed today)

- `bun /tmp/riemann_audit.ts selftest` → TRUST-HIGH
- `bun /tmp/riemann_err_audit.ts` → err table 14…100000
- `bun /tmp/riemann_crossover.ts` + `/tmp/boundary.ts` → boundary ~22604
- `python3 -c "import mpmath; …mpmath.zeta…"` (dps=50) → cross-values above
- `bun /tmp/floorRoot_test.ts` → floorRoot OK
- `bun /tmp/quick_audit.ts`, `/tmp/quick_bench.ts` → prime OK, ~6450/s
- `python3 /tmp/beal_correct_small.py` → ≤100 full-scope clean, 0.3 s
- `python3 /tmp/gap_verify_all.py` → 57/57 VALID, 0.1 s
- `python3 /tmp/goldbach_spot.py` → 478260000–478262000 clean (13.1 s sieve)
- Coverage counts: inline `python3 -c` gcd-pair enumerations (60,753,825
  intra vs 273,429,100 full).

No mock results. Every number above came from a run I watched. What I did
not run (full 478M re-verification, full 273M cross-pair Beal) is marked as
such — EXECUTION REQUIRED if anyone wants those trophies.
