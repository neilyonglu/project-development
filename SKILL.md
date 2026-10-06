---
name: project-development
license: MIT
description: First integrate the current project's conventions, architecture, workflow and available dependencies, then guide staged development through requirements analysis, framework and DB design, flows, interface contracts, acceptance scenarios, implementation planning, implementation and review. Use for explicit project-development workflows or their requested stages. Select only the requested stage; do not apply the entire process to routine small fixes or reviews.
---

# Project Development

Use the requested stages of the author's development workflow. Read only the stage guidance and dependencies needed for the current task.

## Language modes

Use this English entrypoint and the English guides under `references/` as the shared operating instructions for both output modes. [Traditional Chinese guide](SKILL.zh-TW.md) and `references/zh-TW/` are human-readable translations, not a separately installed skill. Do not load both editions by default.

- Resolve `output_language` from the user's explicit choice for the current work, then the project's recorded preference, then the default `zh-TW`. Supported modes are Traditional Chinese (`zh-TW`) and English (`en`). Carry an explicit selection forward until the user changes it; support another requested language without overriding the user.
- Follow the English operating instructions for analysis and checks. This specifies instruction language, not a guarantee about private reasoning language. Do not request or expose private chain of thought; deliver conclusions, evidence, assumptions and verification results.
- Apply the selected language to replies, profile summaries, analysis/design/planning documents, review records, diagram explanations and visible HTML controls. Preserve code identifiers, API/DB fields, commands, paths and verbatim source quotations. Code comments follow the project's conventions unless the user requests translation.
- Record an explicitly chosen persistent project preference in its context document. Do not infer a project-wide preference from one translated quotation. Do not translate all existing project documents or create a second work document just because the output mode changes.
- Use [Chinese HTML template](assets/architecture-diagram.html) for `zh-TW` and [English HTML template](assets/architecture-diagram.en.html) for `en`; they share the same data schema and behavior. Replace example content in the selected language.
- Maintain both documentation editions when changing workflow requirements. English is the maintained execution edition; resolve translation discrepancies against it without introducing a different workflow.

Examples: "Use project-development with English output"; "使用 project-development，輸出用繁體中文".

## Integrate project context first

On first entry, follow [project context](references/project-context.md) to create or refresh a project-local profile: architecture, module conventions, data and interfaces, requirements/document units, development and delivery flow, verification and tool dependencies. Subsequent stages use that profile and its primary sources to preserve the user's development logic.

Reuse an existing profile and check only relevant rules and changes. Context integration permits reading and documentation, not product construction or external actions. Missing unrelated information does not block the requested stage.

## Stages

| Stage | When to use | Guide | Deliverable |
|---|---|---|---|
| Issue / requirements analysis | Clarify requirements, intended architecture and implementation impact | [issue-analysis](references/issue-analysis.md) | Five-part analysis under the project's document unit |
| Project scaffolding | Understand the framework and DB design or build an agreed skeleton | [project-scaffold](references/project-scaffold.md) | Framework/table design; skeleton, config, migration and basic verification when construction is requested |
| Operations and data flow | Explain how an operation connects requirements, modules and DB | [operation-flow](references/operation-flow.md) | Editable flow/sequence diagrams, reads/writes, states, failure branches and open questions |
| Interface contracts | Confirm cross-module inputs, outputs, errors and UI Props mappings | [interface-contract](references/interface-contract.md) | Field/validation tables, result/error contracts, UI mappings and discrepancies |
| Business acceptance | Confirm expected behavior for data, operations and boundaries | [business-acceptance](references/business-acceptance.md) | Source-backed concrete acceptance cases, data changes and unresolved questions |
| Implementation planning | Turn confirmed design and acceptance into executable work | [implementation-plan](references/implementation-plan.md) | Gaps, tasks, dependencies, completion conditions and first step |
| Implementation and validation | Implement the authorized scope and verify acceptance behavior | [implementation-validation](references/implementation-validation.md) | Code changes, verification evidence, limitations and remaining work |
| Review and delivery | Clean up, perform two review passes and complete architecture/test mapping | [review-delivery](references/review-delivery.md) | Review/verification record and implementation/test HTML view |

Add further delivery stages only when needed and confirmed; do not create empty workflows or assumed policies.

Build implementation diagrams, including file walkthrough progress, from the selected language template using [architecture diagram](references/architecture-diagram.md). For repeated inventory, coverage, structure and local-link checks, use [automation](references/automation.md) when needed; scripts cannot replace requirements or semantic code review.

## Selection and handoffs

- Analysis-only requests use issue-analysis; construction requests use project-scaffold with sufficient requirements/architecture evidence.
- Continue across stages within existing authorization. Completing one stage does not independently authorize the next, and prior authorization does not need to be requested again.
- Requests to understand or discuss a design stay in explanation/proposal mode. Do not infer construction permission from a discussion or preview.
- Unresolved choices affecting the framework, core model, permissions or writes block their dependent work, not independent work.
- Reuse the real framework and upgrade mechanism in existing projects. Evaluate frameworks for new projects; this skill does not imply rebuilding, adding tables or expanding scope.
- Document units follow project context. Forge uses one document per issue, updated throughout the work. A guide's "issue/work document" means the current project's chosen unit; other projects need not adopt Forge's platform, numbering or directory.
- Reuse confirmed unchanged design; do not reanalyze the whole issue or demand every preceding artifact at each stage.
- Maintain requirements → design/tasks → implementation locations → acceptance cases/results in the original work document. Each in-scope requirement has a destination; each change has a requirement or necessary technical basis. Address omissions and scope drift without inventing requirements.
- Shared checks are defined in the relevant guide and referenced elsewhere. Keep responsibility, authorization and links consistent. Design confirmed, code written, tests passed and ready to publish are different states.

Examples: use issue-analysis for #92; use project-scaffold to build the modules and migration files needed by confirmed requirements.

Locate this skill's scripts and assets from its actual loaded directory, not a fixed `.claude/skills` path. See [README](README.md) for packaging and evaluation.
