# Implementation Breakdown and Order

Turn requirements, models, flows, contracts and acceptance into executable work. This stage delivers a plan; it does not imply feature edits, DB operations or test execution.

Reuse [project context](project-context.md) for boundaries, work documents and verification. Explain requirement-based reasons and simpler alternatives for dependencies or architectural deviations.

## Current state and gaps

Read analysis/design and check actual workspace code. Distinguish available, to change, to add and unconfirmed capability. Code/test files do not prove verified completion. Record evidence and verification status to avoid redoing existing capability.

## Work items

Break down independently implementable/verifiable behavior, not merely files or an entire unassessable feature:

| Item | Current/target behavior | Reused/modified/new module or file | Dependencies | Completion/acceptance cases | Blockers |
|---|---|---|---|---|---|

- Explain purpose, change boundary and requirement/gap. Proposed file locations are proposals, not existing files.
- Reference concrete acceptance in the original document; code written or compilation passed does not replace functional completion.
- Include prerequisite schema, config, permissions and cross-layer contracts; state compatibility order for existing data and mixed versions.
- Open questions block only dependent items. Keep independent work visible without choosing unconfirmed business policies.

## Order and first step

Order by real dependencies and current progress, favoring a complete verifiable path. Do not mandate DB/backend first. Identify independent tasks without automatically launching parallel agents.

State the first executable item, locations, reason for the order and completion conditions. If nothing is executable, identify the specific decisions required.

## Delivery and handoff

Update breakdown/order in the original work document under project context; reference existing designs/cases. Separate planned tasks from completed/verified results. Explain one work item at a time when requested.

Plan approval alone is not execution authorization. When the user requests development, continue to [implementation and validation](implementation-validation.md), persist through authorized scope and record acceptance results. Present the plan in the selected output language without translating paths or identifiers.
