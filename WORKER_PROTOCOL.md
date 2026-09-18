# WORKER PROTOCOL — single worker, evidence-first (read before touching anything)

## BEFORE WORKING
1. `git pull` (main branch; confirm you are the only active worker).
2. Read `MASTER_HANDOFF.md` (full orientation; numbers verified 2026-09-18).
3. Read `research/QUEUE.md` (ticket states) + `research/RESEARCH_STATUS_CANONICAL_2026-09-18.md`
   (claim statuses — exactly one STATUS per claim; novelty/literature separate).
4. Inspect the latest COMPLETED/FAILED snapshot in `research/COMPLETED/` / `research/FAILED/`.
5. Inspect active work (`research/ACTIVE/`) and recent failures before retrying anything FAILED.

## WHILE WORKING
- Researcher/critic/verifier are three passes, not one: propose, attack, independently reproduce.
  The verifier can veto any status upgrade.
- Exact-equality and near-miss pipelines stay SEPARATE (`research/ARCHITECTURE.md` is law).
- No pruner reuse across questions without a new per-question safety proof.
- Exact integers only where exactness is claimed; record seeds, commands, runtimes, hashes.
- Small exact tests before any scale; close forms for every coverage claim.

## AFTER WORKING
1. Save source + scripts, raw outputs, parameters, environment notes under `research/`.
2. Update the ticket (QUEUE.md) through the state machine (QUEUED→ACTIVE→EXPERIMENTAL→
   UNDER_REVIEW→VERIFYING→COMPLETED/FAILED/BLOCKED; execution alone never completes).
3. Update the canonical ledger (one STATUS per claim + evidence pointer, or no upgrade).
4. Update MASTER_HANDOFF.md only when the project-level picture actually changes.
5. `git status` → review diff → `git add` (never secrets) → `git commit` (clear message) → `git push`.
6. Never delete evidence; never overwrite artifacts in place (new files, or preserve old versions).
7. Never fabricate data/execution/literature; never upgrade without evidence.

## HARD RULES
- C19 (R011 universality) stays UNVERIFIED until proof or verified counterexample — no exceptions.
- No large compute without a ticket whose SUCCESS/FAILURE conditions name the information target.
- One worker on main at a time; stale clones rebase via pull before pushing.
