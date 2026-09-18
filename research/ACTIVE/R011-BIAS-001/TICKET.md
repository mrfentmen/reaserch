# TICKET R011-BIAS-001 — independent-sampling bias probe of the |off|=1 P-dominance

- ID: R011-BIAS-001
- AUTHORIZATION: research director (ChatGPT), 2026-09-18 — authorized FIRST, before any other new research.
- QUESTION: Does the P-only phenomenon (|off|=1 near misses all class P, claim C19 UNVERIFIED) survive
  when the sampling process is changed — i.e., is P-dominance real mathematics, or an artifact of the
  generator family (coprime-(A,B) prefilter, nearest-power rounding, base-pair enumeration order)?
- KNOWN: Hunter pipeline forces gcd(A,B)=1 (proven: forces T=∅, does NOT force P over C — R011 Step 4);
  hunter logs single nearest power only (ties up); hunter enumerates by base-pair index, intra-block,
  S>10^6, ratio<999. R013 ran a no-prefilter base-major control (10P/0T, C26 T=∅ proved arithmetically).
  R015 full-cross 2..1000 census: 7 equations, all P, 0 C/T. C19 stays UNVERIFIED regardless of outcome.
- UNKNOWN: Whether changing enumeration order (random / value-sorted / shuffled) and removing ALL
  hunter filters changes the observed P/C/T split among |off|=1 hits.
- HYPOTHESIS: neutral (probe, not confirmation). If P-dominance is sampling artifact, an independent
  generator family should surface class-C hits; if it is mathematical, P-dominance survives.
- FALSIFIER: a verified class-C ±1 from any generator (kills nothing about universality — C19 is already
  UNVERIFIED — but kills the "survives independent sampling" reading); OR: generators yield zero hits
  (probe underpowered → inconclusive, recorded honestly, NOT a falsification of anything).
- METHOD: three NEW scripts, independent of the existing pipeline (NOT "generate A,B, find nearest C,
  classify"), stdlib only, bases ≤150, exponents 3–7, both signs ±1, NO coprime prefilter, NO S>10^6
  filter, NO ratio bound, post-hoc P/C/T classification (naming-invariant: class depends only on prime
  support of bases; canonical display naming = smallest base). Nearest-power lookup via bisect on
  precomputed C^e tables + defensive ±2 guard (mathematically vacuous — any |S−C^e|=1 hit is at the
  UNIQUE nearest power since consecutive e-th powers are ≥7 apart for e≥3; the guard is a bug tripwire,
  documented as such, not an innovation). Dedup on integer-equation key (S,C,e).
  - GenA (R011-BIAS-001_genA.py): N=300,000 random draws, (A,B) uniform in [2,150], x,y uniform in 3..7,
    fixed seed 20260918, sampling WITH replacement from base space. Calibration: fraction of draws with
    gcd(A,B)>1 (the region the hunter excluded outright).
  - GenB (R011-BIAS-001_genB.py): value-sorted census — all distinct S=A^x+B^y (745 power values →
    ~278k sums, deduped), processed in ASCENDING S order. Records value-rank of each hit.
  - GenC (R011-BIAS-001_genC.py): same distinct-S universe as GenB, shuffled with fixed seed 20260919,
    full pass in shuffled order. Records shuffle-position of each hit. (B vs C differ ONLY in traversal
    order; A differs in sampling distribution.)
- SUCCESS CONDITION: per-generator tables (total |off|=1 hits raw + deduped; P / C / T among deduped;
  seeds, commands, runtimes, raw outputs archived) + honest verdict on "does P-dominance survive
  independent sampling", including the underpowered case.
- FAILURE CONDITION: all three generators yield zero |off|=1 hits → probe INCONCLUSIVE (weak result,
  recorded; does not move C19).
- EXPECTED COST: Low (<2 min compute total).
- EXPECTED INFORMATION VALUE: MEDIUM (attacks the sampling process, not the phenomenon; cannot prove
  or disprove C19 by construction).
- LITERATURE CHECK: N/A (methods probe; no mathematical claim).
- DEPENDENCIES: none.
- STATUS: ACTIVE (filed 2026-09-18).

## R018 overlap verdict (folded into this ticket per director)

Read `research/EXPERIMENTS/R018_001_local.py` + `research/NOTES/R018_TRIAGE.md` (no execution — triage
forbids ad-hoc runs).
1. Same distribution as the old pipeline? NO — R018_001_local.py is not a sampler at all. It
   exhaustively enumerates RESIDUE triples per (modulus, exponents) and records forbidden
   (zero-pattern, ±1) combos: finite-exhaustion proof certificates per (m, xa, xb, e) instance.
   It samples no integer equations and produces no hit distribution.
2. Merely rediscovers C18? LARGELY YES on coverage: every INST modulus (2,7,9,11,16,17) is ≤32,
   and C18 (R011) already records "no small-modulus (≤32) obstruction to class-C ±1". A run would
   re-derive that coverage in mechanized form.
3. Anything new? Only presentation: mechanized forbidden-pattern certificates + C-compatible witness
   patterns per zero-pattern. No new mathematical evidence (never executed, zero artifacts).
VERDICT: R018 as a script is SUPERSEDED by R011/C18 for moduli ≤32; its certificate format is a
presentation improvement, not new evidence. Do NOT run ad hoc. A proper R018 ticket is justified
ONLY IF extended to moduli/exponents beyond C18 coverage (e.g. prime moduli >32, mixed-exponent
patterns not in R011_00{1,2,3}) — filed as a future candidate, not executed here.
