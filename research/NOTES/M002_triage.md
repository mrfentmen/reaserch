# M002 — Evidence pointer cleanup (2026-09-18)

## (a) C4 (`floorRoot` returns floor(v^{1/e}), PROVEN) — pointer missing, artifact not found
Searched the repo (all .md/.py/.ts/.js) for a proof artifact: `floorRoot`,
"loop-invariant", "hi-bound". Findings:
- The implementation lives at `research prize/beal.ts:13` (binary-search
  integer e-th root, used at line 85).
- The "hi-bound + loop-invariant argument" exists ONLY as the ledger row's
  one-line basis — there is no standalone written proof artifact in the repo.
- References in `research/ARTIFACTS/R002_001_spacespec.md` and
  `research/ARTIFACTS/R011_004_definitions.md` cite floorRoot's *use*, not a proof.

Per instructions, no pointer was added to the ledger row (nothing invented).
STATUS unchanged (PROVEN). A future worker may write up the argument as a
proper artifact and then add the pointer.

## (b) C3 (/tmp scripts) — pointer broken, recorded in ledger
`/tmp/beal_correct_small.py` and `/tmp/beal_small_v2.py` are both gone
(/tmp is ephemeral, as flagged in the incoming audit). The C3 ledger basis now
carries a 2026-09-18 NOTE recording the pointer as broken. STATUS unchanged
(VERIFIED COMPUTATIONALLY) — it rests on the recorded run outcome
(26,496/26,496 pairs), not on re-runnable scripts.

## (c) Experiment count — fixed
MASTER_HANDOFF.md §10 said EXPERIMENTS/ holds 55 files; actual count is 54
(verified by listing). Corrected to 54 with a dated correction note.
ARTIFACTS/ count of 44 was not rechecked (outside M002 scope).
