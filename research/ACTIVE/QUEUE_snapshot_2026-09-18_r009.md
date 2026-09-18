# Research queue — populated 2026-09-18

State machine: QUEUED → ACTIVE → EXPERIMENTAL → UNDER_REVIEW → VERIFYING → COMPLETED | FAILED | BLOCKED.
A ticket moves to COMPLETED only on its SUCCESS CONDITION + evidence gate (see `WORKFLOW.md`).
Canonical STATUS per claim (PROVEN / VERIFIED COMPUTATIONALLY / REPRODUCIBLE COMPUTATIONAL EVIDENCE / PARTIAL / HEURISTIC / UNVERIFIED / FALSE); literature + novelty separate.

---

## R001: BEAL CROSS-PAIR COVERAGE

- ID: R001
- QUESTION: Can the Beal search be redesigned with pair-index sharding that covers every required base pair exactly once (or with verified controlled overlap)?
- KNOWN: Current `beal.ts` shards by base range; full 2–6000 space needs 273,429,100 coprime power-pairs; design covers 60,753,825 (22.2%); claim C1 is FALSE.
- UNKNOWN: Cheapest complete-index scheme (linear pair index vs by-C^z parametrization) that stays practical in this repo's environment.
- HYPOTHESIS: A pair-index (k-th coprime pair) shard over the sorted power list gives exact, countable, resumable coverage with negligible overhead.
- FALSIFIER: Prototype shows overlap/gaps under independent counting, or overhead >3× vs current per-pair cost on the ≤100 test domain.
- METHOD: (1) Formalize power list P (|P|=B·E) and coprime-pair enumeration order; (2) implement `pair_index(i,j)` sharding + independent counter model; (3) run on 2–100 exps 3–5, compare coverage count vs 26,496 ground truth from two implementations.
- SUCCESS CONDITION: Scheme derived; test-domain run covers every required pair exactly once with independently counted coverage + reproducible evidence.
- FAILURE CONDITION: Indexing cannot guarantee exact coverage, or overhead unacceptable with no compensating advantage.
- EXPECTED COST: Low (prototype <1 min on test domain; design doc).
- EXPECTED INFORMATION VALUE: HIGH (converts FALSE coverage claim into a correctable method).
- LITERATURE CHECK: by-base (Norvig/Vanderkam) vs by-C^z (pscamillo/beal_bigint) parametrizations; record before claiming novelty.
- DEPENDENCIES: none.
- STATUS: QUEUED.
- NEXT ACTION: Write pair-index spec + prototype on 2–100 domain.
- EVIDENCE: none yet (this file is the ticket, not evidence).

## R002: BEAL PRUNING THEOREMS

- ID: R002
- QUESTION: Does a rigorously proven necessary condition beyond coprimality eliminate a measurable candidate fraction?
- KNOWN: Coprimality skip is valid (divisibility lemma). No other pruning is currently justified in-repo.
- UNKNOWN: Whether parity/modular/valuation/exponent constraints yield a proven, non-trivial cut.
- HYPOTHESIS: met and exceeded — RESIDUE removes 69.9% of exact checks (2.79× net), FLT-gcd removes 8.8% at ~zero cost; parity/valuation candidates PROVEN worthless as pair-pruners (recorded rejections).
- FALSIFIER: not triggered (two rules proven + measured; two candidates disproven with proof).
- METHOD: Enumerate candidate necessary conditions (mod 3/4/7/8/9, parity of exponents, LTE-type valuation constraints); attempt proof for each; test survivors against exhaustive 2–100 domain measuring cut fraction + zero false exclusions of planted exact solutions (e.g. known parametric families with gcd>1).
- SUCCESS CONDITION: ≥1 proven necessary condition + measured cut + domain test + correctness preserved.
- FAILURE CONDITION: Systematic sweep yields no valid rule after documented attempts.
- EXPECTED COST: Medium (math + small compute).
- EXPECTED INFORMATION VALUE: HIGH (a real lemma beats any bound increase).
- LITERATURE CHECK: Tijdeman–Zagier / Darmon–Granville type restrictions; Catalan-adjacent results; record before novelty claim.
- DEPENDENCIES: R001 (coverage model) helpful, not blocking.
- STATUS: COMPLETED 2026-09-18 (SUCCESS: 2 proven necessary conditions + measured cuts + safety equality 24=24 with planted survivors + independent Bun validation + critic review; no R013+ created — Step-18 gate: residue-strengthening is engineering optimization, FLT is final, R011-B is pruner-useless; recorded decision, not omission).
- NEXT ACTION: done. Next per priority: R009/R005 differential survey to govern any future compute.
- EVIDENCE: `research/EXPERIMENTS/R002_00{1,2,3}.md` + scripts; `research/ARTIFACTS/R002_RULE_RESIDUE.md`, `R002_RULE_FLT.md`, `R002_REJECTED_parity_valuation.md`, `R002_001_spacespec.md`, `R002_001_baseline.json`, `R002_002_bench.json`, `R002_00{1,2,3}_stdout.txt`; `research/LITERATURE/flt_wiles_wikipedia.md`; ledger C20–C23.

## R003: BEAL STRUCTURAL REDUCTION

- ID: R003
- QUESTION: Is there a rigorous reduction (factorization, valuations, gcd structure, primitive normalization, exponent reduction) that shrinks or restructures the Beal search?
- KNOWN: Pairwise→triple gcd lemma (see R004). Primitive-solution literature exists externally.
- UNKNOWN: Whether a repo-usable reduction (e.g. normalize to primitive triple + exponent gcd classes) is both proven and computationally effective here.
- HYPOTHESIS: Normalizing by g=gcd of bases + classifying by gcd(x,y,z) yields disjoint subcases with at least one subcase reducible to a smaller search.
- FALSIFIER: Reductions either fail proof or give <2× effective shrinkage on test domain.
- METHOD: State candidate reductions precisely; prove; test against valid (gcd>1 parametric) and invalid cases; measure shrinkage on 2–100 domain.
- SUCCESS CONDITION: Precise reduction/lemma + proof + case tests.
- FAILURE CONDITION: No reduction survives verification.
- EXPECTED COST: Medium (mostly math).
- EXPECTED INFORMATION VALUE: HIGH.
- LITERATURE CHECK: Beal/X–Y–Z generalized Fermat literature; primitive-solution reductions.
- DEPENDENCIES: none blocking.
- STATUS: QUEUED.
- NEXT ACTION: Draft primitive-normalization statement.
- EVIDENCE: none yet.

## R004: NEAR-MISS OBSTRUCTION LEMMA

- ID: R004
- QUESTION: Can the near-miss dataset be compressed into a proven obstruction explaining the pairwise-factor cases?
- KNOWN: `beal_near.txt` 3058 lines; all 19 |off|=1 cases have triple-gcd 1 with a pairwise factor (mod-p impossibility). Full-dataset classification pending at ticket creation.
- UNKNOWN: Exact class fractions (P/T/C) over all 3058 lines; whether any fully-coprime small-|off| cases survive (genuinely interesting).
- HYPOTHESIS: Lemma L1 (equation ⇒ pair-share iff triple-share; contrapositive blocks triple-1/non-pairwise triples mod p) explains class P, likely the majority; class C is small.
- FALSIFIER: Classification shows class P empty/small, or a fully-coprime exact solution appears (would be a counterexample — check immediately), or lemma proof fails.
- METHOD: Parse all 3058 lines (repo-relative path); compute triple + pairwise gcds with pure-integer arithmetic; classify P (triple 1 + some pair shares), T (triple >1), C (fully pairwise coprime); dedupe duplicate (base,exp) namings; list smallest-|off| class-C survivors; prove L1; attack L1 with planted valid/invalid triples.
- SUCCESS CONDITION: L1 stated + proved + tested; full classification table produced from executed code; survivors (if any) listed.
- FAILURE CONDITION: Pattern does not generalize (statement false or vacuous).
- EXPECTED COST: Low (<1 min compute).
- EXPECTED INFORMATION VALUE: HIGH (replaces 3058-line file with one lemma + counts).
- LITERATURE CHECK: Elementary (divisibility); no novelty claimed beyond compression — verify no prior "near-miss" misreading needs rebuttal.
- DEPENDENCIES: none.
- STATUS: COMPLETED 2026-09-18 (SUCCESS CONDITION met: L1 stated+proved+tested; full 3058-line classification executed, dual-implementation agree; hypothesis refined to even split + |off|=1⟹P 19/19).
- NEXT ACTION: done — class-C list feeds R002; next ticket per priority: R008.
- EVIDENCE: `research/EXPERIMENTS/R004_001.md`, `research/EXPERIMENTS/R004_001_classify.py`, `research/ARTIFACTS/R004_001_counts.json`, `research/ARTIFACTS/R004_001_lemma.md`, `research/ARTIFACTS/R004_001_stdout.txt`; ledger C15/C16.

## R005: BEAL LITERATURE GAP

- ID: R005
- QUESTION: What precise non-"search farther" gap remains between this repo and Beal literature?
- KNOWN: Published GPU searches (500k bound, exps 3–15); partial theoretical results exist.
- UNKNOWN: Which subcase/method in-repo could add information (exponent restrictions, primitive reductions, alternative parametrization).
- HYPOTHESIS: partly confirmed — exactly one OPEN mathematical gap found (G-e, R011 universality); bound/method gaps closed as REDUNDANT; implementation instances UNCLEAR (insufficient evidence).
- FALSIFIER: not triggered (genuine OPEN gap G-e identified; no new ticket needed — R011 already owns it).
- METHOD: Targeted literature survey with records in `LITERATURE/` (no fabricated entries); diff table: our range vs known range, method vs method; convert best gap into a new ticket or close.
- SUCCESS CONDITION: Precise gap + new ticket, or documented close.
- FAILURE CONDITION: (same as falsifier — honest close counts as completion).
- EXPECTED COST: Medium (reading + writing).
- EXPECTED INFORMATION VALUE: MEDIUM-HIGH (prevents redundant compute).
- LITERATURE CHECK: this IS the literature check.
- DEPENDENCIES: none.
- STATUS: COMPLETED 2026-09-18 (differential survey executed; verdicts: bound-chasing REDUNDANT; deep theory REDUNDANT-for-us; G-b/G-c UNCLEAR; G-e OPEN under R011; G-f OPEN under R006; no new ticket — R011 owns the gap).
- NEXT ACTION: done. Next per evidence: R011 tranche OR C20/C21 port design (both require new tickets before compute).
- EVIDENCE: `research/EXPERIMENTS/R009_001.md`; `research/LITERATURE/norvig_beal2000.md`, `danvk_beal2006.md`, `darmon_granville_fermatcatalan.md`, `beal_bigint_readme.md`; ledger novelty fields.

## R006: RIEMANN METHOD REPLACEMENT

- ID: R006
- QUESTION: Can the EM hunter be replaced by a validated high-accuracy method (Riemann–Siegel style + explicit error + Turing/zero-count check) over a stated range?
- KNOWN: Fixed-n EM vacuous ~22.6k, unsound ~30k; current logs to 1,095,200 unvalidated; no Turing verification.
- UNKNOWN: Cheapest validated stack reproducible here (mpmath interval? Arb? documented Riemann–Siegel implementation) and its feasible range.
- HYPOTHESIS: A small-range (e.g. t≤1000) validated pipeline with explicit bounds + Turing check is implementable and reproducible in-repo.
- FALSIFIER: No candidate stack validates against known zeros/values within resource budget, or error bounds cannot be made explicit.
- METHOD: Prototype on t≤200 against known zeros (14.1347, 21.0220) + mpmath dps=50; require explicit bound < detection threshold; add zero-count consistency; only then extend range. Never restore old claim by threshold-tweaking.
- SUCCESS CONDITION: Justified method + explicit bounds + known-value reproduction + validity over stated range + independent check.
- FAILURE CONDITION: Cannot validate rigorously → document and retire direction.
- EXPECTED COST: Medium–High.
- EXPECTED INFORMATION VALUE: HIGH (only path to a non-HEURISTIC Riemann result).
- LITERATURE CHECK: Platt–Trudgian (3e12), Gourdon/Odlyzko–Schönhage, Turing's method references.
- DEPENDENCIES: none.
- STATUS: QUEUED (BLOCKED for large runs until prototype validates).
- NEXT ACTION: Prototype t≤200 validator.
- EVIDENCE: prior EM-vs-mpmath tables (in protocol audit) are background, not the new method.

## R007: PRIME IMPLEMENTATION VALIDATION

- ID: R007
- QUESTION: Over exactly which domain is `prime()` guaranteed correct, and does an independent implementation agree?
- KNOWN: Exhaustive vs sieve to 100,000 clean; large squares + 2³¹−1 sampled clean; general claim PARTIAL.
- UNKNOWN: Whether a complete domain characterization (with sqrt-rounding argument formalized) + full agreement holds to the Goldbach frontier.
- HYPOTHESIS: `prime()` is correct for integers 0 ≤ n < 2⁵³ (IEEE exactness + ulp-lattice sqrt-floor lemma + 6k±1 wheel); fractional inputs out of contract. (Stronger domain than the ticket's draft 2³¹ — established by proof, not assumed.)
- FALSIFIER: A mismatch found at any n, or rounding argument fails for some range.
- METHOD: Formalize algorithm + domain argument; differential-test vs deterministic Miller–Rabin on exhaustive small + stratified large sample (squares, primes±1, composites with large factors); document exact domain.
- SUCCESS CONDITION: Domain characterization + agreement record; limitations explicit.
- FAILURE CONDITION: Remains domain-limited → document exact domain (still completes as documented limitation).
- EXPECTED COST: Low–Medium.
- EXPECTED INFORMATION VALUE: MEDIUM (closes PARTIAL, unblocks honest Goldbach scoping).
- LITERATURE CHECK: Trial-division correctness folklore; Miller–Rabin deterministic bases for <2^64.
- DEPENDENCIES: none.
- STATUS: COMPLETED 2026-09-18 (domain characterization PROVEN for integers [0,2⁵³): ulp-lattice sqrt-floor lemma + wheel proof; exhaustive [0,100k] + 322 stratified + 80k sqrt adversarial, 0 mismatches; fractional misbehavior exhibited and excluded by contract; call sites integer-checked).
- NEXT ACTION: done. Next: R011.
- EVIDENCE: `research/EXPERIMENTS/R007_001.md`, `research/EXPERIMENTS/R007_001_prime.py`, `research/ARTIFACTS/R007_001_theorem.md`, `research/ARTIFACTS/R007_001_stdout.txt`, `research/ARTIFACTS/R007_001_counts.json`.

## R008: ERDOS PROVENANCE RECOVERY

- ID: R008
- QUESTION: Can the missing Erdos source/provenance be recovered without guessing?
- KNOWN: Logs only (`scan n=…done=…` step 25 from 1000024; frontiers 1159620/test 1000924); no source in repo or git history (single squashed commit).
- UNKNOWN: Whether source exists in backups/branches/remotes/Desktop remnants.
- HYPOTHESIS: (neutral) Source may exist outside repo; search first, conclude second.
- FALSIFIER: Exhaustive search of `git log --all`, branches, stashes, remotes, filesystem backups finds nothing → close as unrecoverable (honest completion).
- METHOD: Search git objects/branches/remotes + documented backup locations only; never invent source; on failure leave UNVERIFIED with missing-provenance record.
- SUCCESS CONDITION: Source recovered + independently verified, or documented unrecoverable.
- FAILURE CONDITION: (documented-unrecoverable counts as ticket completion with FAILED-provenance status, not as result).
- EXPECTED COST: Low.
- EXPECTED INFORMATION VALUE: MEDIUM (unblocks or buries an entire line).
- LITERATURE CHECK: N/A until predicate known.
- DEPENDENCIES: none.
- STATUS: FAILED 2026-09-18 (failure condition met: source unrecoverable from all legitimate local avenues — single-commit history, no dangling objects, no branches/stashes, remote identical, no Desktop/shell-history/system traces, applet decompiles to relaunch.sh only. Log forensics: 5 runs, 6385 scans, zero mathematical content. Time Machine/off-machine backups the only unsearched avenue, stated as limitation).
- NEXT ACTION: done — C13 stays UNVERIFIED; C17 recorded. Next: R007.
- EVIDENCE: `research/EXPERIMENTS/R008_001.md`.

## R009: LITERATURE DIFFERENTIAL TABLE

- ID: R009
- QUESTION: Across Beal/Riemann/Goldbach/Collatz/gaps/Erdos, where (if anywhere) can this project add information beyond literature?
- KNOWN: All current bounds trail literature by ~8–10 orders where comparable.
- UNKNOWN: Whether any methodological niche (not bound) remains.
- HYPOTHESIS: At least one niche (method variant, obstruction lemma, validated pipeline) is actionable.
- FALSIFIER: Completed table shows no actionable niche → record honestly, redirect effort to lemmas/methods.
- METHOD: Build table (project range / validated range / literature range / method diff / what's new / gap / next experiment) with sourced `LITERATURE/` records; no fabricated entries.
- SUCCESS CONDITION: Table + ≥1 actionable direction, or honest no-niche record.
- FAILURE CONDITION: (honest no-niche also completes).
- EXPECTED COST: Medium.
- EXPECTED INFORMATION VALUE: HIGH (governs all compute spending).
- LITERATURE CHECK: this IS the check (Oliveira e Silva, Platt–Trudgian, Barina, gap tables, Beal GPU work).
- DEPENDENCIES: benefits from R005/R006 progress but can start now.
- STATUS: QUEUED.
- NEXT ACTION: Draft table skeleton from canonical ledger.
- EVIDENCE: none yet.

## R010: PRIORITY RANKING MECHANISM

- ID: R010
- QUESTION: Can next-ticket selection run on explicit operational criteria (cost, value, uncertainty reduction, overlap, reproducibility, dependencies, feasibility)?
- KNOWN: Ad-hoc selection used so far.
- UNKNOWN: Whether a lightweight scoring rule is actually predictive/useful here.
- HYPOTHESIS: A simple documented score (value×feasibility/(cost×overlap)) ranks R004 > R008 > R007 > R002 … and its picks survive review.
- FALSIFIER: Scores are unstable under small input changes or recommend low-value compute.
- METHOD: Define fields + formula in `WORKFLOW.md`; score R001–R009; use for one real selection; review outcome; keep or drop mechanism.
- SUCCESS CONDITION: Mechanism selects next ticket with documented reasons; review recorded.
- FAILURE CONDITION: Mechanism discarded after documented poor performance (also a result).
- EXPECTED COST: Low.
- EXPECTED INFORMATION VALUE: LOW-MEDIUM (process, not mathematics).
- LITERATURE CHECK: N/A.
- DEPENDENCIES: needs this queue (done).
- STATUS: QUEUED.
- NEXT ACTION: Implement scoring section + first ranking.
- EVIDENCE: none yet.

---

## R011: OFF-BY-ONE OBSTRUCTION GENERALIZATION

- ID: R011
- QUESTION: Does |off|=1 ⟹ P hold universally, and if so why?
- KNOWN: off = signed nearest-e-th-power difference (S−C^e, ties up); hunter constraints ((A,B)=1 prefilter, S>10^6, ratio<999, exps 3–7, intra-block pairs).
- UNKNOWN: proof of universality OR counterexample outside bases ≤600/exps 3–7.
- HYPOTHESIS: open — universal implication unproven; dataset+wide-scope pattern verified but unexplained (gap/size/modulus mechanisms all falsified).
- FALSIFIER (still open): one fully-coprime triple with A^x+B^y−C^z=±1 kills universality.
- METHOD: definitions → algebra/parity/valuation/moduli → counterexample hunts → mechanism measurements → proof attempt (all executed 2026-09-18, see evidence).
- SUCCESS CONDITION: proof of general obstruction (NOT MET).
- FAILURE CONDITION: proven un-generalizable / counterexample (NOT MET).
- EXPECTED COST: spent ~4 min compute total (73.7 s + seconds + 122 s).
- EXPECTED INFORMATION VALUE: HIGH (open phenomenon with p≈8e-5 dataset significance + 2.7M-pair scope).
- LITERATURE CHECK: Pillai/Catalan adjacent (consecutive-power scarcity) — noted, not yet surveyed; required before any universality claim.
- DEPENDENCIES: none.
- STATUS: ACTIVE (parked; phenomenon verified in scope, proof idea missing; feeds R002 as constraint data).
- NEXT ACTION: R002 pruning (use class-C list + 22k pairs/s cost data); revisit R011 only on new proof idea or wider-search budget.
- EVIDENCE: `research/EXPERIMENTS/R011_001.md`, `R011_002.md`, `R011_003.md` (+ scripts `R011_001_attack.py`, `R011_002_sizebias.py`, `R011_003_wide.py`); `research/ARTIFACTS/R011_001_stdout.txt`, `R011_002_stdout.txt`, `R011_003_stdout.txt`, `R011_001_counts.json`, `R011_003_counts.json`. No R012 (Phase-4 gate not met).

---

## Priority (operational, not mathematical importance)

1. R004 DONE → 2. R008 FAILED (documented) → 3. R007 DONE → 4. R011 ACTIVE-parked (open phenomenon) → 5. next: R002 pruning (constraint data ready) → 6. R009/R005 (govern spending) → 7. R001/R003 (methods) → 8. R006 (expensive, last) → 9. R010 (process).
