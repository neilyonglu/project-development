# Implementation and Validation

When development is requested, implement and verify the authorized scope using the confirmed plan. Understanding/design/planning-only requests do not activate implementation. Persist through the scope without asking for routine reversible edits; deployment, publication and actual DB application follow their own authorization.

## Select work and verify current state

Read plan, requirements, relevant design and acceptance; select by dependencies. Check conventions, actual code and uncommitted user edits, preserving unrelated changes. A clear scope without a formal plan needs sufficient checks, not every preliminary artifact.

## Implementation

- Implement concrete behavior using existing modules, interfaces, access patterns, errors and upgrade mechanisms; do not rebuild available capability.
- Check needed UI, backend entrypoints, config, models and metadata/migration companions so a finished layer is actually usable.
- Never substitute fixed success, swallowed errors or bypassed permission/data constraints for an incomplete flow.
- Record requirement conflicts/design gaps and impact in the original work document. Resolve routine details from requirements/conventions; ask consequential business-policy questions, blocking only their dependencies and continuing independent work.

## Code quality requirements

Check while writing, for added/changed code only; do not expand into whole-project refactoring.

- **Parameters have purpose:** verify arguments, React Props, settings and transmitted fields are read and affect intended behavior. Remove unnecessary parameters/pass-through and update callers/types/docs; no unused future switches.
- **Verify before removing:** trace callers, callbacks/framework contracts and dynamic use; local absence alone does not justify breaking signatures. Mark intentional unused required parameters using project conventions.
- **Names explain meaning:** variables, functions, classes and files communicate business role/behavior. Avoid vague abbreviations/generic labels; short local loop variables may follow conventions. Understand source/use before renaming rather than guessing semantics.
- **Terminology is consistent:** reuse confirmed terms/conventions; distinct concepts do not share confusing names. Make ratios, percentages, time and counts/units identifiable. Boolean conditions avoid hard-to-read double negatives.
- **Signatures/defaults are clear:** distinguish required/optional/NULL/default. Avoid multiple positional booleans. Excessive parameters warrant responsibility checks before restructuring, not an empty abstraction just to shorten a signature.
- **Structure is readable:** focused functions, controlled nesting, existing tools for repetition. Remove unused imports/variables/functions, unreachable branches and stale comments. Comments explain business reasons/constraints, not restate code.
- **Renaming preserves contracts:** update internal uses. API/DB/config/public-interface renames require consumer/data/compatibility checks, not blind text replacement. Preserve external names with explicit internal mapping where needed.

Use existing lint/typecheck/compiler and manual semantics checks. Passing tooling does not prove clear naming or useful parameters.

## Correctness checks

Select by actual operations, data and risk. Record applicable handling/questions; do not add locks, versions, retries or monitoring to every issue. Check existing mechanisms first.

- **Consistency/transactions:** identify writes and commit boundaries, which must succeed together and recognizable partial state. Across services distinguish committed/pending execution and recovery instead of claiming absent atomicity. Check keys/uniqueness/relationships preserve invariants.
- **Concurrency/repeated operations:** check simultaneous edits, duplicate submissions, overlapping schedules/retries for lost updates/duplicate effects. UI disabling or check-then-insert alone does not guarantee consistency. Evaluate real transactions/constraints/locks/version checks. Retry only safe operations under confirmed policy with error classes/bounds/outcomes; no unsupported exactly-once claim.
- **Freshness:** distinguish UI snapshots, decision-time and execution-time data. Recheck applicable permissions/restrictions before writes. Reject/reconfirm/use approved policy on changed data; do not choose newer values that override intent.
- **Permissions/trust:** check identity, dataset/tenant and authorization in backend and actual write paths. Client user ID/dataset/state/target is not authorization evidence; check batch items where needed. Service identity is distinct from the original operator's rights. Token validity does not grant every operation.
- **Errors/resources:** check timeouts, cancellation, exceptions, connection/session/file cleanup and rollback. Retain identifiable failures/traceability, not swallowed errors with success. Show completed/pending items for partial execution. No tokens, secrets or unnecessary sensitive logs; avoid redundant error abstractions.
- **Scale/performance:** examine query count, N+1, justified indexes, unbounded loads, batches/memory at expected scale. Avoid blocking inappropriate async environments; paging/batch changes preserve semantics. Locate real paths/data volume before speculative caches/complex systems.
- **Meaningful tests:** distinguish correct/incorrect outputs, data changes, constraints and side effects rather than only mock calls/formulas. Identify DB/transaction/concurrency/cross-layer behavior hidden by mocks; use real integration where risk warrants. Make data/time reproducible. Existing passes do not cover missing cases.
- **Upgrade/compatibility:** check old data/settings and mixed service versions for schema/contracts/config/states. Explain deployment/upgrade order, backfill/recovery. Compatibility needs real consumers, not permanent unused dual contracts. State unsafe rollback limits.
- **UI states:** check loading, empty, failed, unsaved and partial-success presentation/actions. Retain inputs and recovery on submission failure where required. Older responses must not overwrite newer actions. Use existing labeling/keyboard/status conventions, not success-screen-only verification.
- **Precision/time:** keep units, precision, rounding, thresholds and date/timezone/period boundaries consistent across DB/backend/UI. Display rounding does not decide business results. Use confirmed calendars/date semantics, not guessed ID meaning.
- **External data/dependencies:** verify shape, required fields, values and compatibility; HTTP success is not usable data. Identify missing/unknown/unsupported results; fallback follows confirmed policy without fabricated business data. Check project versions/existing capability before new packages.

Map checks to contracts, data design and acceptance. Undefined transaction/concurrency/freshness policy is unresolved rather than a technical preference. Label unverified mechanisms/results; neat structure is not reliability evidence.

## Verification

Choose checks against confirmed acceptance, prioritizing changed behavior, boundaries and failures. Run necessary build/type/unit/integration checks by impact. Do not require new tests for low-impact reversible edits or tests mirroring implementation.

Check fixtures, target and external side effects before execution. Live DB, schema recreation or paid models require suitable authorization/environment. Mock/offline success is not actual DB/end-to-end success.

Classify failures as change-related, pre-existing or environmental; fix in-scope problems and rerun affected checks. Once necessary checks pass, do not repeatedly expand testing without new changes, failures or unresolved concerns.

## Completion and delivery

Update tasks/results in the original work document using project units. Record changes, executed checks/results, unverified scope/reasons and remaining work. Keep schema declaration/application/verification separate.

After final edits synchronize affected contracts, fields, settings, acceptance and diagrams. Final code establishes current state; preserve requirement/implementation differences rather than rewriting requirements to conceal noncompliance. Verification evidence identifies time, branch/HEAD and relevant uncommitted state, command, exit code and result. If tested behavior changes after evidence, rerun affected checks.

Explain completed behavior, verification and limitations in the selected output language. Code/test existence is not completion; mark complete only when conditions are satisfied. Do not start unauthorized stages/deployments/publications.

When cleanup/review is requested, use [review and delivery](review-delivery.md) for cleanup and the two review passes.
