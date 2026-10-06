# Project Context Integration

Understand how this project is developed before applying the stage workflow. Preserve the user's development logic. The profile is an evidence-backed summary and source index, not a replacement rulebook.

## Create or reuse

1. Identify the repository and task scope. Read applicable AGENTS.md, CLAUDE.md and project conventions; check the nearest real module, manifests, build scripts and CI.
2. Reuse an existing profile or equivalent document and its location. Otherwise use the customary project documentation directory, for example `docs/development/project-development-profile.md`. Keep real project data in the project, outside the distributed skill.
3. Integrate enough context for the current task, mark unchecked areas and extend as needed. Refresh only relevant or changed facts; do not require a complete repository survey before proceeding.

## Content

| Category | Project characteristics | Effect on the workflow |
|---|---|---|
| Architecture/modules | Technologies, actual paths, responsibilities, cross-layer calls and nearest examples | Reuse locations and companion files; avoid a second architecture |
| Data/contracts | DB/migration, access, permissions, errors, precision/time and metadata conventions | Point to the project's design and correctness checks |
| Requirements/documents | Platform/sources, issue or feature unit, names and document locations | Identify the document updated at each stage and trace requirements |
| Work/delivery | Branches, comparison base, review, QA, CI triggers and upgrade/release order | Define handoffs; documented procedures do not authorize external actions |
| Verification | Build/lint/typecheck/test commands, fixtures, target environment and side effects | Choose meaningful executable checks rather than generic examples |
| Available dependencies | CLIs, skills, plugins, browser, runtime, network and access | Record needed capability, available/unchecked/missing/not-applicable status, alternatives and dependent blockers |
| Output language | Explicit user choice or recorded `output_language`, `zh-TW` or `en` | English operating instructions in both modes; selected language for deliverables |

Include sources, applicable modules, verification date and status. Separate confirmed user conventions, normative rules, actual implementation, proposals and unresolved questions. Verify versions against relevant manifests/results; newer documentation is not automatic business approval. Never store credentials, secrets or production records.

## Use in stages

- Link the profile from the work document. Keep the five-part analysis and reference shared context rather than copying it into each issue. Without an issue, identify the work by requirements title and source.
- Follow the actual project's domain handlers, services, hosting platform and document conventions. For example, a sample shop application may use an order API, a notification service and one document per issue. Do not transplant another project's APIs or fields.
- At entry, check sufficient inputs, authorization and required capabilities. At exit, record artifacts, evidence, unresolved questions and next executable work. Continue under existing cross-stage authorization without asking for it again.
- Backfill affected designs/cases when contracts or requirements are incomplete. Return to affected implementation for test/review findings. Recheck only affected scope while preserving the document and traceability.
- Prefer applicable available external review skills, otherwise perform both [review passes](review-delivery.md) locally and identify the method. If remote requirements cannot be accessed, use provided material without claiming complete reading. Missing necessary runtime/DB means verification remains unperformed.
- Before adding a layer, package, table or tool, state the current requirement, why existing capability is insufficient and the simpler alternative. Record necessary deviations and reasons in the work document without a mandatory extra report.
- Resolve output language using the entrypoint's precedence. A mode change changes requested deliverables, not source semantics, workflow, permissions or technical identifiers. Preserve existing documents unless their translation is requested; do not make parallel documents for the same issue by default.

## Refresh

Refresh relevant sections when architecture, paths, conventions, CI, tools or delivery practices change. Retain significant decisions and sources; reuse unchanged items. A profile's existence proves neither that all dependencies were verified nor that product acceptance passed.

Use fictional or neutral names in public documentation, templates and demonstrations. Do not publish company-internal names, real internal issues or implementation examples. Keep actual project context in its project, outside this public skill.
