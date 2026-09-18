# MASTER HANDOFF — Beal near-miss research project (verified 2026-09-18)

All numbers below were re-verified from primary artifacts during handoff preparation.
Ledger short-codes (C1…) refer to `research/RESEARCH_STATUS_CANONICAL_2026-09-18.md`
(36 rows). Tickets (R001…) live in `research/QUEUE.md`.

## 1. PROJECT PURPOSE
Brute-force + structural investigation of Beal-type exponential Diophantine equations,
grown out of an inherited "conjecture hunter" repo (`beal.ts`, `riemann.ts`, `quick.ts`,
prime-gap and Erdos log-hunters). The work evolved from naive counterexample hunting into
audited computational number theory with honest bounds.

## 2. WHAT WE ARE ACTUALLY TRYING TO SOLVE (plain English)
Find integer solutions to A^x + B^y = C^z (Beal equation) or prove structural facts about
them; in practice the project now studies *near misses* A^x + B^y − C^e = ±1 and asks why
every observed ±1 case shares a prime factor between two bases (the "|off|=1 ⟹ P"
phenomenon, C19). This is NOT a claimed proof of Beal's conjecture or of the phenomenon.

## 3. EXACT MATHEMATICAL TARGET
- Beal equation: A^x+B^y=C^z, bases ≥ 2, exps ≥ 3; counterexample needs gcd(A,B,C)=1.
- Near-miss observable: S=A^xa+B^xb, C^e nearest perfect power (ties up), d=S−C^e.
  |off|=1 ⟺ A^xa+B^xb−C^e=±1. Classes: P (triple-gcd 1 + some pair shares a prime),
  C (fully pairwise coprime), T (triple-gcd > 1).
- Open question (R011, C19 UNVERIFIED): does |off|=1 always imply P? No proof, no counterexample.

## 4. CURRENT OBJECTIVE
Parked open questions only: R011 (phenomenon), R003/R006 (structure/Riemann), R010 (process).
No authorized compute. Next work needs new tickets first.

## 5. LEDGER STATE (one status per claim; novelty/literature separate)
- PROVEN: C4 floorRoot algorithm; C10 prime() on integers [0,2^53) (ulp-lattice + wheel);
  C15 lemma L1 (pairwise→triple prime sharing); C20 residue prefilter necessity;
  C21 FLT-gcd elimination; C26 T=∅ for |off|=1; C29 pruner-census unsafety;
  C30 pair-index math; C35 L2a/L2b divisibility lemmas.
- VERIFIED COMPUTATIONALLY: C3 (Beal ≤100 full-cross clean); C7 Riemann selftest;
  C9 Goldbach/Collatz spot 478,260,000–478,262,000; C11 (44 distinct gap records);
  C16 (3058-line classification P=1530/T=0/C=1528, 2169 unique); C18 (2.7M-pair scope);
  C24 (higher-exp tranche); C27 (R013 stages); C28 (full-cross-1000: 11 lines, all P);
  C31–C33 (index/shard/pipeline/1000-regression); C36 (tower 45,878 pairs, 0 hits).
- REPRODUCIBLE COMPUTATIONAL EVIDENCE: C2 (checkpoint counts); C17 (Erdos source absence);
  C25 (survey negative); C34 (indexer 24× slower enumeration).
- FALSE: C1 (Beal "through 6000" — only 22.2% pairs covered); C5 (Riemann "to 1,095,200" —
  method vacuous ~22.6k, unsound ~30k); C12 ("57 gap records" — 44 unique);
  C14 (near-miss file as supporting evidence); C22/C23 (parity/valuations as pair-pruners).
- UNVERIFIED (do not use): C6 (Riemann prefix scan), C8 (Goldbach/Collatz full bound),
  C13 (Erdos — missing source), C19 (universality).
- Novelty: all mathematics KNOWN except bounded NOT-ESTABLISHED implementation notes and
  C37-class packaged local statements — check per-row novelty fields; never NEW without evidence.

## 6. WHAT FAILED AND WHY
- R008: Erdos/gap hunter source unrecoverable (single-commit history, no dangling objects,
  remote identical, no local traces). Claim stays UNVERIFIED permanently unless source appears.
- R013/R017 falsifications: no counterexample (negative results, kept).
- R014: exact-equality pruners misapplied to nearness census (2 measured false rejections);
  gate caught it pre-tranche. Permanent rule: pipelines stay separate (ARCHITECTURE.md).
- Riemann EM hunter: invalid beyond ~22k (retired, not fixed — R006 open).
- Beal intra-block sharding: 77.8% pairs missed (superseded by R001/R016 pair index).

## 7. METHODOLOGICAL LESSONS (binding)
1. Exact-equality pruners NEVER transfer to nearness questions without a new safety proof.
2. Checkpoints/logs prove nothing by themselves (tag-version mismatch actually found).
3. Deduplicate by integer equation, not by (base,exp) naming (144³=12⁶ etc.).
4. Coverage is pairs, not bases; sharding needs closed-form proof, not counters.
5. Small-modulus residue tables are complete only where zero ⟺ divisibility is exact.
6. Report both raw and unique counts; report machine variance for timings (use ratios).

## 8. CURRENT R011 / R017 STATE
R011 ACTIVE-parked (phenomenon open, C19 UNVERIFIED). R017 COMPLETED (option-8 verdict:
no proof; every divisor lever points away from P; L2a/L2b proven-but-insufficient;
tower regime 0/45,878 null-consistent). Evidence for |off|=1⟹P: 14/14 dataset uniques,
9/9 wide (2.7M pairs), 3/3 higher-exp, R013 stages, R015 full-cross-1000 (11 lines, all P),
tower 0 hits. No C-class ±1 observed anywhere; none proven impossible.

## 9. QUEUE (15 tickets)
DONE: R001, R002, R004, R005, R007, R009, R015, R017. FAILED (honest negatives): R008,
R013, R014. ACTIVE-parked: R011. QUEUED: R003, R010. BLOCKED: R006 (needs prototype).
Latest completed: R017 (+R001/R016 workstream). Next: new tickets required before any compute.

## 10. STRUCTURE / WORKFLOW / EVIDENCE
- `research/`: QUEUE.md, WORKFLOW.md, ARCHITECTURE.md (pipeline separation law),
  EXPERIMENTS/ (54 files: records + runnable scripts; corrected 2026-09-18, was 55), ARTIFACTS/ (44: JSON/stdout/proofs),
  LITERATURE/ (7 records), ACTIVE/, COMPLETED/, FAILED/ (ticket snapshots).
- Roles: researcher proposes, critic attacks, verifier reproduces and can veto upgrades.
- Gates: no status upgrade without evidence pointer (source + execution + validation +
  coverage). Computation alone never proves a theorem.
- Git: single worker on main; snapshots per ticket state change; history never rewritten.

## 11. LITERATURE POSITION (all bounds trail the field — know it)
Goldbach→4e18, Collatz→2^68, RH→3e12, prime gaps→4e18/2^64, Beal GPU search→C=500,000,
danvk→1000³ with probabilistic sieves (stronger raw power than ours), modular method owns
deep theory, Fermat-Catalan 10 known solutions (all with a square). Our contributions are
audit + small verified scopes + two sound pruners + the R011 phenomenon record — nothing more.

## 12. WHAT MUST NOT BE REPEATED
Re-running hunter heartbeats as "progress"; bound-chasing without a ticket; reusing C20/C21
for nearness; trusting logs/checkpoints; duplicate-count inflation; threshold-tweaking the
dead Riemann hunter; re-litigating settled FAILED tickets without new evidence.

## 13. WHAT WOULD CONSTITUTE A REAL DISCOVERY
Verified class-C ±1 triple (kills U); proof of U or a clean subcase; newform-level theory
(not our tools); validated Riemann pipeline (R006); or a pruner with a per-question safety
proof that beats the state of the art at competitive scale.

## 14. PATHS (historical, do not "fix" old evidence)
- Original hunters hardcode `/Users/dtaxk/Desktop/research prize/state` (nonexistent here;
  repo clone lives wherever checked out).
- `research/EXPERIMENTS/*.py` hardcode `/Users/dtaxk/reaserch/...` absolute paths.
  To reproduce elsewhere: check out anywhere and `sed -i 's|/Users/dtaxk/reaserch|<repo>|'`,
  or symlink the repo to `/Users/dtaxk/reaserch`. Record any such adaptation in the run log.
- Bun (`bun`) + Python 3 (`python3`, stdlib only) required; mpmath only for Riemann spot checks.
