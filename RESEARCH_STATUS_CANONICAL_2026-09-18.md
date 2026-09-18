# Canonical status ledger — 2026-09-18 (protocol pass 2)

One STATUS per claim. Literature and novelty recorded separately.
Prior combined labels (e.g. "VERIFIED … SUPERSEDED") are withdrawn and
replaced below. Evidence: files re-read + fresh executions recorded in
RESEARCH_AUDIT_PROTOCOL_2026-09-18.md; nothing new executed for this
relabel except where noted.

| # | Claim (narrow) | STATUS | Literature | Novelty | One-line basis |
|---|---|---|---|---|---|
| C1 | Beal search covered ALL coprime pairs bases ≤6000, exps 3–7, none found | FALSE | ALREADY KNOWN (no counterexample known to far larger bounds) | KNOWN | Design covers 60,753,825/273,429,100 = 22.2%; 77.8% inter-block missing by construction (`beal.ts:62-68,72-78`) |
| C2 | Beal intra-block checkpoint counts equal combinatorial totals | REPRODUCIBLE COMPUTATIONAL EVIDENCE | KNOWN (elementary combinatorics) | REPRODUCTION | File contents vs fresh enumeration agree; shows consistency, not execution |
| C3 | No Beal counterexample, bases ≤100, exps 3–5, full cross coverage | VERIFIED COMPUTATIONALLY | ALREADY KNOWN (covered by published searches to 500k, exps 3–15) | REPRODUCTION | Two independent runs today, 26,496/26,496 pairs, scripts kept (`/tmp/beal_correct_small.py`, `/tmp/beal_small_v2.py`) |
| C4 | `floorRoot` returns floor(v^{1/e}) | PROVEN | KNOWN (standard binary search) | KNOWN | hi-bound + loop-invariant argument; tests confirm |
| C5 | Riemann off-line zeros sampled/verified to 1,095,200 | FALSE | ALREADY KNOWN (RH rigorously verified to 3e12; no off-line zero known) | KNOWN | Gate vacuous past ~22.6k, unsound near ~30k (true err 0.227 vs gate 0.192); logs beyond are unvalidated |
| C6 | Riemann prefix scan (t≲22k, 6 σ, step 0.25) found no SUSPECT | UNVERIFIED | ALREADY KNOWN | KNOWN | Full prefix re-run not witnessed here; logs alone insufficient per LOG INTEGRITY; method is sampling in any case |
| C7 | Riemann selftest → TRUST-HIGH (3 points) | VERIFIED COMPUTATIONALLY | ALREADY KNOWN (zeros at 14.13/21.02 known) | REPRODUCTION | Re-ran today; passes; mpmath cross-check agrees |
| C8 | Goldbach+Collatz clean from 1M to 478,260,000 | UNVERIFIED | ALREADY KNOWN (Goldbach to 4e18; Collatz to ~2^68) | KNOWN | Full re-run not performed (~20 h); checkpoint alone proves nothing; no counterevidence found |
| C9 | Spot 478,260,000–478,262,000 (1001 evens + odds) clean | VERIFIED COMPUTATIONALLY | ALREADY KNOWN | REPRODUCTION | Independent sieve (13.1 s) + exact Collatz re-ran today |
| C10 | `prime()` correct in general | PARTIAL | KNOWN | KNOWN | Defined subset [0,100000] exhaustively verified vs sieve (that subclaim alone: VERIFIED COMPUTATIONALLY); large squares sampled; general proof not machine-checked |
| C11 | 44 distinct window-local gap records valid | VERIFIED COMPUTATIONALLY | ALREADY KNOWN (gaps tabulated to 4e18/2^64) | REPRODUCTION | Deterministic Miller–Rabin on all 44: endpoints prime, interiors empty, merit formula (0.1 s) |
| C12 | "57 gap records" (as 57 distinct) | FALSE | ALREADY KNOWN | KNOWN | File has 57 lines, 44 unique; 13 duplicates (restart artifacts) |
| C13 | Any substantive Erdos-hunter result | UNVERIFIED | UNKNOWN (predicate unknown — source missing, assessment impossible) | not assessable (no predicate; forced label would be false) | MISSING SOURCE; logs only |
| C14 | Near-miss file as Beal-supporting evidence/progress | FALSE | KNOWN (elementary gcd obstruction) | KNOWN | All 19 \|off\|=1 cases carry a pairwise factor forbidding equality; filter lacks C-coprimality; duplicates (144³=12⁶) |

Notes & corrections to earlier drafts:
- SUPERSEDED never appears as STATUS above (only under Literature, as
  ALREADY KNOWN). Earlier combined labels are superseded by this table.
- C10's general claim is PARTIAL, not VERIFIED: the exhaustive part covers a
  defined subset only. Do not quote C10 as full correctness.
- C6 is UNVERIFIED rather than HEURISTIC: execution was not witnessed here,
  which is the binding limitation; the method's sampling nature is recorded
  as a limitation, not the status.
- C13's novelty is explicitly left outside the four-value scheme with reason
  stated, rather than forcing a false label.
- Smallest-true statements per claim are in
  RESEARCH_AUDIT_PROTOCOL_2026-09-18.md §B; this file governs STATUS only.
