# Business Rules and Acceptance Scenarios

Once flows, models and contracts are clear, turn business rules and constraints into concrete expected outcomes. This stage produces acceptance cases, not feature edits, test authoring/execution or DB operations merely to document cases.

## Evidence and scope

Read core algorithms, constraints, open questions, flows and contracts in the work document. Requirements determine expected behavior; existing code is evidence of current behavior only. Keep conflicts and undefined policies unresolved rather than using implementation as the acceptance standard.

## Rules and cases

List in-scope rules and sources, then cases that distinguish correct from incorrect behavior:

| Case | Rule/requirements evidence | Preconditions/data | Operation/input | Expected outcome | Confirmation/open question |
|---|---|---|---|---|---|

- Use concrete values/data for normal flows; include calculations, units and comparison operators where useful, not just "correct result".
- Choose meaningful boundaries such as exact/above/below thresholds, NULL versus zero, missing data and rule precedence. Do not enumerate irrelevant combinations mechanically.
- For writes identify records added, changed or unchanged and observable outcomes. Separate recommendations, human decisions and actual execution.
- Include relevant permission, lock, state-change, partial-success, repeated-submission or retry scenarios. Undefined policy remains a question, not invented behavior.
- Across modules check UI, response and data-state consistency. Identify required acceptance data/environment; an unexecuted case cannot be marked passed.
- Include applicable UI states, precision/time boundaries and missing/malformed external data using [correctness checks](implementation-validation.md#correctness-checks), without converting undefined policy into confirmed expected results.

Label cases confirmed, observed in existing implementation or awaiting requirements confirmation. Identify the specific implementation/acceptance work each unresolved question blocks rather than stopping everything.

## Delivery and handoff

Update business rules/cases in the original work document under project context. Link cases to rules, flows and interfaces rather than creating a conflicting requirements copy. Explain one rule and its cases at a time when requested.

The user should understand triggers, non-trigger conditions, resulting data changes and identifiable failures. Continue to implementation/tests only under authorization; written cases are not passed acceptance.

For scheduling work, use [implementation planning](implementation-plan.md). Use the selected output language for descriptions; preserve technical names and source quotations.
