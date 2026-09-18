# Adversarial research audit — 2026-09-18, protocol pass

This pass treats the previous audit (`RESEARCH_AUDIT_2026-09-18.md` in this
repo) as a suspect, not a source. Every claim below was re-derived from the
files and from fresh executions today. Where the prior report overstated,
that is recorded as counterevidence against my own work. Fourth Diet Coke;
the ashtray situation is worse.

## A. Corrections to the prior report (counterevidence found)

1. **Gap records: not 57 distinct.** `gap_records.txt` has 57 lines but only
   **44 unique** (13 duplicates, e.g. every line of the first window appears
   twice — restart re-append artifact). Prior "57/57 VALID" is corrected to:
   44 distinct records, each valid; file contains 13 duplicate lines.
2. **Beal checkpoints: mixed code versions.** `beal_2000_7_0_1.txt` contains
   tag `2000_7_0_1` (4 parts) while current `beal.ts` (line 35) builds a
   5-part tag (`max_emax_shard_shards_bmin`) and `load()` (line 52) returns 0
   on tag mismatch. So the 30,364,700 checkpoint is **orphaned under current
   code** — a legacy artifact, not a resumable state. Newer shards
   (`3000_7_0_1_2001` etc.) are 5-part and consistent. Prior report did not
   flag this. Consequence: "shards ran to completion under current code" is
   withdrawn (see B1).
3. **Riemann failure has two boundaries, not one.** Prior report gave only
   the gate-crossing (~22.6k, re=0.2). Fresh EM-vs-mpmath comparison shows:
   gate is conservative (~7–40×) through 20k (true errors 4e-5…6.5e-4 vs
   gates 3.9e-4…5e-3), gate refuses (vacuous-but-safe) from ~22.6k, and gate
   becomes **unsound** near ~30k: at t=30000, re=0.2 true error ≈0.227 vs
   gate 0.192; re=0.5 true error ≈0.030 vs gate 0.015. So: vacuity boundary
   ≈22.6k (re=0.2) / ≈30k (re=0.8); unsoundness boundary ≈30k.

## B. Claim-by-claim audit

### B1. "Beal searched through base 6000" — STATUS: FALSE (as full bound)
- CLAIM: all A,B ≤ 6000, exps 3–7 examined, no counterexample.
- COVERAGE: required full-range coprime power-pairs = **273,429,100**
  (executed enumeration). Design of current code (bmin..max per shard, pairs
  within shard only) covers intra-block **60,753,825 = 22.2%**; missing
  inter-block **212,675,275 = 77.8%**. Pair coverage, not base coverage, is
  the correct denominator — independent intervals do not imply pair coverage.
- EXECUTION: not witnessed here; checkpoints/logs are legacy-mixed (see A2);
  per LOG INTEGRITY, `done … pairs=` lines and checkpoint equality to
  combinatorial totals show *consistency*, not execution under current code.
- SOURCE: `beal.ts` lines 60–68, 72–78 (shard loop); checkpoint files (mixed
  tags); `beal2–6.log`.
- VALIDATION: combinatorial recount matches checkpoint numbers — necessary,
  not sufficient.
- LIMITATIONS: 77.8% pairs unexamined by design; exps capped at 7; legacy tag
  orphan.
- LITERATURE: GPU by-C^z searches to bound 500,000, exps 3–15, ~20k hits, 0
  coprime (pscamillo/beal_bigint). Ours is orders below even if completed.
- FAILURE: INCOMPLETE COVERAGE + MISSING SOURCE (version provenance).
- VALUE: NEGATIVE RESULT (intra-block consistency only) + HEARTBEAT logs.
- SMALLEST TRUE: "Checkpoint counts equal intra-block combinatorial totals;
  execution under current code unwitnessed."

### B2. "No Beal counterexample ≤100, exps 3–5" (today's small result) — STATUS: VERIFIED COMPUTATIONALLY
- CLAIM: full cross-coverage clean in stated scope.
- COVERAGE: 297 powers, 26,496 coprime pairs — 100% of stated scope, cross
  pairs included. M/N = 26496/26496.
- EXECUTION: ran twice today: `/tmp/beal_correct_small.py` (0.3 s, float-seeded
  hi) and adversarial `/tmp/beal_small_v2.py` (10.4 s, pure-integer `iroot`,
  independently implemented). Both agree: count 26496, no counterexample.
- SOURCE: both scripts (this machine); scope parameters recorded.
- VALIDATION: two independent nth-root implementations + `iroot` selftest
  (all b<200 exact/v±1 boundaries).
- LIMITATIONS: trivial scope vs literature; lemma (pairwise→triple gcd
  propagation) used to skip — proof sketched (divisibility), accepted.
- LITERATURE: SUPERSEDED as a bound (far below published searches), but
  methodologically sound.
- VALUE: SANITY CHECK / REQUIRED VALIDATION of method, not new mathematics.

### B3. `floorRoot` in `beal.ts` — STATUS: PROVEN (algorithm) + tested
- CLAIM: returns floor(v^{1/e}).
- Argument: hi=2^{ceil(bitlen/e)+1} ≥ 2·v^{1/e} > root (since v<2^bitlen);
  standard binary-search invariant; exact `mid**BigInt(e)` comparisons; cap
  `hi=min(hi,v)` safe. Tested: all b^e (b<50, e≤7) round-trip, v±1
  boundaries, 200 random-sum invariants — all pass (`/tmp/floorRoot_test.ts`).
- LIMITATIONS: `v.toString(2)` allocates a huge string for giant v (perf, not
  correctness); `Number(f)` at FOUND site safe only while f<2^53 (true for
  stated scope: f≤~8e8).

### B4. "Riemann sampled/verified to 1,095,200" — STATUS: FALSE (as validated search)
- CLAIM: off-line zeros sampled to `riemann.txt`=1095200 with working gate.
- COVERAGE: intended ~4.38M t-points × 6 σ ≈ 26M evaluations. Validated
  region (gate holds AND true error small, confirmed vs mpmath dps=50 at
  5k/10k/15k/20k): only t ≲ 22.6k (re=0.2) — roughly **2% of claimed range**.
  From ~22.6k the gate refuses (vacuous); near ~30k the gate underestimates
  true error (unsound). `riemann_loop.ts` line 29 also passes a third arg
  ("1200") that `riemann.ts` line 72 ignores — dead parameter, further
  provenance sloppiness.
- EXECUTION: `selftest` re-ran → TRUST-HIGH (reproduced); err table, boundary
  binary search, and EM-vs-mpmath comparisons all re-ran today
  (`/tmp/riemann_err_audit.ts`, `/tmp/boundary.ts`, `/tmp/em_vs_mpmath.ts`,
  `/tmp/em_beyond.ts`).
- SOURCE: `riemann.ts` lines 18–37 (EM, p=5, n≤5000, err=last×5 — a
  heuristic, not a proven bound); `riemann_loop.ts`; `riemann_loop.log`.
- VALIDATION: mpmath cross-check where gate holds (true error < gate by
  ~7–40×); gate-failure demonstrated, not assumed.
- LIMITATIONS: even the valid prefix is HEURISTIC sampling (step 0.25, 6 σ
  values — narrow dips could fall between samples); no Turing method, no
  interval arithmetic, no proof of absence.
- LITERATURE: rigorous verification to 3e12 (Platt–Trudgian 2020). Ours is
  ~8 orders below at best, unsound beyond.
- FAILURE: NUMERICAL FAILURE (fixed-n EM outside domain) + INVALID
  ASSUMPTION (gate as validation; logs as verification).
- SMALLEST TRUE: "EM sampling with working (conservative) gate only to
  ~22k; logs beyond are unvalidated; no SUSPECT found where the gate holds."

### B5. "Goldbach+Collatz verified to 478,260,000" — STATUS: UNVERIFIED (full bound); spot interval VERIFIED COMPUTATIONALLY; bound SUPERSEDED regardless
- CLAIM: all even g (Goldbach) and odd g+1 (Collatz) from 1M to 478260000 clean.
- COVERAGE: full re-run not performed here (~20 h estimated at measured
  ~6,450/s); checkpoint `quick.txt`=478260000 exists but per LOG INTEGRITY
  proves nothing by itself.
- EXECUTION: `prime()` exhaustive vs sieve to 100k — no mismatches
  (`/tmp/quick_audit.ts`); large-square adversarial samples
  (21863², 21869², 2³¹−1 prime, companions) agree with Miller–Rabin;
  independent segmented-sieve spot check 478,260,000–478,262,000 (1001 evens)
  all partitioned + Collatz odds all reach 1 (`/tmp/goldbach_spot.py`, 13.1 s).
- SOURCE: `quick.ts` (hardcodes `/Desktop/...` — NOT REPRODUCIBLE as
  committed on this machine); checkpoint/log files.
- LIMITATIONS: `prime()` sqrt-rounding argument sketched, not machine-proved
  → correctness beyond tested range is REPRODUCIBLE EVIDENCE, not PROVEN;
  Collatz guards (200k steps, 2^72·1000) never approached in range (max
  excursion ≪ bound) — guards untested by data.
- LITERATURE: Goldbach to 4e18 (Oliveira e Silva–Herzog–Pardi 2013); Collatz
  to ~2^68. Ours ~10 orders below. Even if true, REDUNDANT WITH KNOWN RESULTS.
- FAILURE (for continued running): ALREADY SUPERSEDED.
- REPRODUCIBILITY: NOT REPRODUCIBLE as committed (absolute Desktop path;
  no relative-path config).
- SMALLEST TRUE: "Spot interval 478,260,000–478,262,000 independently clean;
  full bound unwitnessed here and superseded."

### B6. Prime-gap records — STATUS: VERIFIED COMPUTATIONALLY (44 distinct); file REDUNDANT in 13 lines
- CLAIM (corrected): 44 distinct window-local maximal gaps near 9e15 valid.
- COVERAGE: 44/44 unique verified (deterministic Miller–Rabin <2^64 bases;
  endpoints prime, interiors empty, merit=gap/ln(p)² to 2e-4)
  (`/tmp/gap_verify_all.py`, 0.1 s). 13 duplicate lines are restart artifacts,
  not distinct records.
- LIMITATIONS: window-local (≈300M wide at 9e15, frontier `gap.txt`=
  9000000301989888), not global records; gaps 500+ occur far below 9e15 in
  published tables to 4e18/2^64.
- LITERATURE: SUPERSEDED as records; value is NEGATIVE RESULT / SANITY CHECK
  for the scanner, not new information.
- SMALLEST TRUE: "44 distinct window-local gap records valid; largest
  9000000147878479+538 (merit 0.3987) re-verified."

### B7. Erdos hunter — STATUS: UNVERIFIED + NOT REPRODUCIBLE
- CLAIM: none statable (predicate unknown).
- SOURCE: MISSING SOURCE (logs only: `selftest ok`, `scan n=…done=…` step 25
  from 1000024, frontiers 1159620 / test 1000924). No reconstruction attempted
  (guessing forbidden).
- FAILURE: MISSING SOURCE. NEXT: recover from backups or declare orphaned.

### B8. Near misses as Beal evidence — STATUS: HEURISTIC at best; stored set EXPLAINED (collapsed, not progress)
- All 19 |off|=1 cases have triple-gcd 1 but a pairwise common factor;
  by the B2 lemma exact equality is then impossible mod p. The 3058-line file
  (filter ad≤1000, no C-coprimality filter, duplicate (base,exp) namings like
  144³=12⁶) is therefore structured noise. Obstruction recorded; file should
  not grow as "progress". VALUE: HEARTBEAT.

## C. Checklist answers (before any future major report)

1. Claimed code executed? Only B2–B6 spot scopes witnessed here; B1/B5-full/B7
   not witnessed. 2. Intended objects examined? Only B2 fully; B1 22.2% by
   design; B4 ~2% validated. 3. Coverage complete? No (B1, B4). 4. Numerics in
   validated range? Only B4 prefix. 5. Inputs traceable? No for B1-legacy/B7.
   6. Reproducible? B2–B4-spots/B6 yes; B1-full/B5-full/B7 no (absolute paths,
   missing source). 7. Independent checks? Yes where claimed above. 8.
   Counterexamples attacked? Yes (Beal exact search; zeta SUSPECT logic probed
   vs mpmath; Goldbach sieve; gap interiors). 9. Failures recorded? Here.
   10. Literature stronger? Yes for every bound. 11. Claim stronger than
   evidence? Corrected to smallest-true above. 12. Smallest true results: see
   each SMALLEST TRUE line.

## D. Resource discipline / next

Do not extend B1 in slow TS (273M pairs × 5 roots) or B4 beyond 22k or B5/B6
heartbeats to make numbers larger — all are REDUNDANT WITH KNOWN RESULTS or
INVALID. If anything runs: (1) recover or drop erdos; (2) repo-relative paths;
(3) Beal only via pair-index sharding or by-C^z parametrization with a stated
   novel scope; (4) Riemann only via Riemann–Siegel+Turing+interval arithmetic
   or not at all. An obstruction list is the valid output of this session.
