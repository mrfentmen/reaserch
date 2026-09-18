# Research workflow — state machine, loop, roles, evidence gates

## 1. Ticket states

QUEUED → ACTIVE → EXPERIMENTAL → UNDER_REVIEW → VERIFYING → COMPLETED
Any state → FAILED | BLOCKED as appropriate. VERIFYING failing returns the
ticket to ACTIVE (or FAILED/BLOCKED) — never to COMPLETED.

- QUEUED: ticket written with all fields; no work started.
- ACTIVE: researcher assigned; plan + falsifier written.
- EXPERIMENTAL: code running / ran; raw output inspected.
- UNDER_REVIEW: critic attacking (coverage, bugs, counterexamples, literature).
- VERIFYING: verifier reproducing independently; gates checked.
- COMPLETED: SUCCESS CONDITION met + evidence gate passed + ledger updated.
- FAILED: FAILURE CONDITION met, or approach exhausted (record lesson).
- BLOCKED: dependency or missing provenance stops work (record what unblocks).

Completion never follows from "code executed" alone.

## 2. Researcher loop (persistent)

READ QUEUE → SELECT TICKET (priority §6) → READ STATE/LITERATURE →
PLAN + FALSIFIER → CHEAPEST INFORMATIVE TEST → INSPECT OUTPUT →
ATTACK → INDEPENDENT CHECK → UPDATE EVIDENCE → UPDATE LEDGER →
UPDATE TICKET → NEXT ACTION. Repeat. Blocked → immediately pick next
unblocked ticket.

## 3. Roles (three logical passes; verifier has veto on upgrades)

- RESEARCHER: hypotheses, literature, design, code, run, structures.
- CRITIC: invalidate — coverage holes, bugs, counterexamples, prior art,
  selection bias, numerical artifacts. Must attempt at least one concrete
  falsification per important result.
- VERIFIER: independent reproduction (different language/method/order where
  practical), evidence + reproducibility + status check. No upgrade without
  verifier sign-off + evidence pointer.

## 4. Evidence gates (hard)

Computational upgrade requires: source pointer + execution record (command,
params, inputs, env, runtime) + output + validation + coverage analysis
(total/actual/covered/uncovered, sharding, boundaries, duplicates).
Mathematical upgrade requires: formal statement + assumptions + proof +
independent review. Literature claim requires: source + date + passage/bound.
An LLM statement is never its own evidence. No pointer → no upgrade.

## 5. Records

- Experiments: `research/EXPERIMENTS/<TICKET>_<NNN>.md` (ID, ticket, date,
  question, hypothesis, code pointer, command, inputs, params, env, ACTUAL
  output, runtime, coverage, validation, failure check, interpretation,
  status, next action). No fictional output.
- Artifacts: `research/ARTIFACTS/` (datasets, checksums, tables, plots, proof
  drafts, verification outputs). Junk is not evidence.
- Literature: `research/LITERATURE/<key>.md` (title, authors, year, source,
  problem, result, method, relevance, known bound, relation, notes). No
  fabricated entries — websearch/fetch or local inspection only.
- Tickets live: `research/ACTIVE/` (symlink or copy of queue entry in play);
  done: `research/COMPLETED/` / `research/FAILED/`.

## 6. Next-ticket priority (operational)

score = (information_value × feasibility) / (cost × (1 + literature_overlap))
Fields scored 1–5 per ticket; ties → fewer dependencies first. Current ranking
recorded in QUEUE.md tail. The score recommends; the researcher justifies the
pick in one line. Review after each use; drop the mechanism if it misleads
(R010).
