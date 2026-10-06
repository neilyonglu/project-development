# Review and Delivery

The workflow covers (1) cleanup and two review passes, and (2) implementation architecture/test mapping. Add further delivery stages when the user needs them; this stage does not authorize merge, deployment or publication.

## Step 1: Cleanup and two review passes

Run when code review/cleanup is requested, not when discussing or editing workflow rules alone.

### 1. Scope and cleanup

Confirm work identity, comparison base and actual diff; preserve unrelated edits. Improve naming, structure, duplication and unused code in scope using existing capability while preserving requirements/contracts, not rewriting the project to personal preference.

Apply [code quality requirements](implementation-validation.md#code-quality-requirements), especially unused/pass-through arguments/Props, vague names and inconsistent units/terms. Ask only necessary semantic questions; signature/rename changes check callers/external contracts.

Apply [correctness checks](implementation-validation.md#correctness-checks) for applicable consistency, concurrency, freshness, backend permissions, errors/resources, scale, tests, compatibility, UI states, precision/time and external contracts. Record real risk/evidence as handled, unverified or unresolved; readable code is not proof of correctness. Check requirements traceability for omissions, unjustified changes and stale docs, using the shared definitions rather than duplicated checklists.

### 2. Correctness: prefer `/code-review`

Resolve the actual command/skill in this environment, read its rules and invoke it for the current scope; similar names are not interchangeable.

If it reviews GitHub PRs, verify applicability to this platform and PR/MR/local diff. Do not claim a GitHub command was performed on GitLab/local work. If unavailable/inapplicable, record that and perform an equivalent authorized local review: map requirements/cases to the complete relevant changes, inspect failure paths/project rules, and report locations, evidence, severity and fixes. Missing the command does not stop local review; do not automatically install or post remote comments. Remote-comment behavior remains subject to authorization.

### 3. Simplification: prefer `/ponytail-review`

Resolve its actual name/SKILL.md and applicability. If unavailable/inapplicable, perform equivalent local simplification after correctness and identify it honestly as local review.

Look for unnecessary abstractions/dependencies, reinvention of standard capabilities, unused flexibility and reducible logic. Record locations, reductions, requirement evidence and alternatives. General review owns correctness/permission/performance findings. First produce recommendations; apply justified changes within authorized cleanup scope.

### 4. Findings and re-verification

Evaluate evidence/requirement impact of both passes. Fix valid in-scope problems; record rejection reasons and unresolved impact. Simplification must preserve business rules, permissions, constraints and meaningful verification.

Recheck behavior affected by cleanup/fixes using [validation](implementation-validation.md). Re-review affected scope after significant fixes; do not loop without new findings.

### Step 1 delivery

Record scope, actual command/skill/method, both passes, fixes/rejections and verification in the original work document. Identify missing/inapplicable/incomplete external review without pretending it ran.

Each pass reports proceed, needs fixes or blocked, with locations/evidence; speculation is unverified. Unresolved critical requirements/correctness block dependent delivery; low-risk suggestions can be consciously rejected/deferred. No findings is not acceptance/publication. Continue within existing authorization; ask only if the next action exceeds it or needs a consequential unresolved choice.

## Step 2: Implementation architecture and test mapping

After cleanup/fixes update the final implementation view. Retain intended architecture from analysis; record discrepancies instead of treating code as approved requirements.

### 1. Account for changes

Use confirmed base and final diff, including relevant committed/staged/unstaged/untracked changes; exclude unrelated user edits. Account for additions, modifications, deletions and renames in nodes or companion lists.

Use [inventory](automation.md) first, verify scope, map node `files`/omitted-file `data-file`, then run coverage/diagram. Semantic responsibility for nodes, calls and tests remains with the reviewer.

Show execution-path files as nodes; group config, metadata/schema, types, builds and docs by supported flow. Explain removal/replacement of deleted/renamed files rather than depicting them as live. Mark unchanged dependencies reused, not changed. Never invent a call merely to connect a diagram.

### 2. File and data flow

- Group actual layers/responsibilities: UI entry/pages/shared components, backend entry/business/config, data/external services.
- Label real file/class and provide paths; explain responsibility without confusing same-name files.
- Trace trigger to outcome; label calls/events/important data. Emphasize cross-layer calls and distinguish async, configuration and reads/writes with a legend.
- Include relevant identity, dataset, settings origin/precedence and consequential failure/blocker branches. Split overview/details while keeping complete file accounting.
- Keep modification state, reading/review progress and test results distinct; read is not implemented/verified.

### 3. Tests

Show added/changed/directly applicable tests separately with dotted links to tested modules/contracts and rules/boundaries/failures. Distinguish mock/unit, integration and end-to-end; tests are not product execution.

Separate exists, executed, passed, failed and unexecuted with step 1 evidence. Identify verification/gaps without adding ceremonial tests to make the diagram complete.

### 4. Readable HTML

Use the language-selected template under `assets/` and [diagram guide](architecture-diagram.md) for source, details, parts and omitted files. Templates provide layers, collapsible legend, Part tabs, test visibility, zoom/reset/Ctrl-wheel, hover, file/function/style cards, edge highlighting and readable light/dark colors. Hide only test nodes/edges without breaking the main flow or Mermaid.

Reduce crossings; split dense diagrams instead of shrinking text. Show rendering errors and disclose external-resource network needs. Saved view preferences do not determine content correctness. All visible descriptions/controls use the selected output language; paths/identifiers retain their original spelling.

### 5. Completeness and delivery

Map final inventory to nodes/companions and verify real calls, DB reads/writes and test targets. Check actual rendering, test toggle and zoom; explicitly identify unperformed checks.

Link HTML from the original work document with base, coverage and discrepancies. It is a companion view, not another analysis document. Guidelines remain usable without disposable example HTML.
