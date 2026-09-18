# M001 — Ledger canonicalization (2026-09-18)

Maintenance record. No MAINTENANCE log exists in the repo and QUEUE.md is
ticket-only, so this note + the commit message are the record.

## What was wrong
Two copies of the claim-status ledger existed:
- `RESEARCH_STATUS_CANONICAL_2026-09-18.md` (repo root) — STALE: only C1–C14,
  C10 listed as PARTIAL (upgraded to PROVEN 2026-09-18), missing C15–C36.
- `research/RESEARCH_STATUS_CANONICAL_2026-09-18.md` — canonical (36 rows, C1–C36).

Diff confirmed the root copy is a strict stale subset of the research/ copy
(diff shows only: C10 row difference + 22 added rows C15–C36 + notes updates).

## What was done
1. `git mv RESEARCH_STATUS_CANONICAL_2026-09-18.md research/ARCHIVE/RESEARCH_STATUS_CANONICAL_STALE_ARCHIVE.md`
   (new `research/ARCHIVE/` directory; history preserved via rename).
2. Prepended an archive header: SUPERSEDED BY the canonical path, reason
   (stale duplicate — missing C15–C36, outdated statuses), "Do not use."
3. WORKER_PROTOCOL.md BEFORE WORKING: added one explicit line naming the
   canonical ledger and declaring the archived duplicate historical / not for use.
4. This note written as the M001 maintenance record.

No claim statuses were changed. No evidence deleted (rename, not deletion).
