# R018 triage (2026-09-18)

## The file
`research/EXPERIMENTS/R018_001_local.py` (2,253 bytes) — "R018 mechanized local
classification for A^x+B^y-C^e=±1 (finite exhaustion = proof per instance)".
For each (modulus m, exponents xa, xb, e) it enumerates ALL residue triples and,
for each zero-pattern (which of A, B, C vanish mod the modulus), records the
achievable D = (a+b−c) mod m values; a (pattern, eps) with eps unreachable is
proven impossible at that modulus. It then asserts observed integer-equation
hits comply and reports C-compatible witness patterns. INST table: moduli
2, 7, 9, 11, 16, 17 with assorted exponent patterns (10 cases).

## Origin evidence
- Added in the single initial commit b6e0b4e ("Create complete research handoff
  and worker protocol") — no separate commit, so no commit-message provenance.
- No R018 ticket in `research/QUEUE.md` (highest ticket: R017).
- No snapshot in `research/ACTIVE/`, `research/COMPLETED/`, or `research/FAILED/`.
- No experiment record (.md), no artifacts in `research/ARTIFACTS/`, no stdout.
- No mention in MASTER_HANDOFF.md or the canonical ledger.
- The header pre-numbers the ticket ("R018"), suggesting the author intended to
  file an R018 ticket but never did.

## Execution evidence
None found. No stdout artifact, no output/counts file, no run log references the
script. (A computed `npat` variable is never used — consistent with a script
written but never finalized/observed, though that alone proves nothing.)

## Thematic overlap
C18 (R011) already records "no small-modulus (≤32) obstruction to class-C ±1",
evidenced by `EXPERIMENTS/R011_00{1,2,3}.md`. Every modulus in the R018 INST
table (2, 7, 9, 11, 16, 17) is ≤32, so a plain run of this script would largely
REPRODUCE C18's modulus coverage rather than add new evidence.

## Verdict: Case B — meaningful research, out of protocol
The script is coherent, complete, and directly on the R011 question (mechanized
residue-obstruction classification) — not test scaffolding or abandoned junk,
so Case A (discard to ARCHIVE) is rejected. Its content is fully legible, so
Case C (unknown/quarantine) is rejected.

Finding: discovered UNREGISTERED research script. R018 was never filed as a
ticket and no execution artifacts exist. No claims may reference R018, and
there are no R018 results to use, until the work is reproduced under ticket
controls (question, method, falsifier, success condition, snapshot, artifacts).

## Recommended next step (for the director — NOT executed here)
1. Critic first checks overlap: does R018's mechanized forbidden-pattern output
   add anything beyond R011_00{1,2,3} (C18)? If not, record R018 in QUEUE.md as
   superseded by R011 without running it.
2. If it adds something (extends moduli/exponents, or yields mechanized
   forbidden-pattern certificates), file a proper R018 ticket with
   QUESTION / METHOD / FALSIFIER / SUCCESS CONDITION, then execute under the
   standard state machine with snapshot + artifacts.
3. Do NOT execute the script ad hoc, do NOT backfill a ticket from memory, do
   NOT cite R018 in any ledger claim row.

File left in place (Case B: document only, no move).
