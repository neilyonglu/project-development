# project-development

English | [繁體中文](README.zh-TW.md)

Preserve the author's development logic: integrate the current project's characteristics, workflow and dependencies first, then select requirements analysis, design, planning, implementation, validation and two review passes. Includes requirement-to-implementation/acceptance traceability and editable HTML architecture/test views.

## Language modes

The agent uses the English [SKILL.md](SKILL.md) and English stage guides under `references/` for both modes. [Traditional Chinese workflow](SKILL.zh-TW.md) and `references/zh-TW/` are reading/maintenance translations. Install one skill, not separate language variants.

Default output is `zh-TW`; request `en` for English. An explicit current user choice takes precedence over recorded project preference, then the default. Carry the choice forward until changed. English operating instructions cannot guarantee the language of private reasoning; the workflow does not request private chain of thought.

- Chinese: "使用 project-development，先整合此專案脈絡，輸出用繁體中文。"
- English: "Use project-development. Integrate this project's context first and produce all deliverables in English."
- Switch: "Use English output from now on and keep the existing work document."

The mode applies to replies, work documents, reviews and visible diagram prose/controls. Preserve code/API/DB identifiers, commands, paths and quotations. Code comments follow project conventions. Do not translate the entire existing project or create duplicate work documents just because a mode changes.

## Installation and use

Copy the complete `project-development/` directory into your agent's supported skills directory, retaining SKILL.md, references, scripts and assets. Claude Code project installation can use `.claude/skills/project-development/`; other agents use their own supported paths/invocation. To uninstall, remove only the installed skill directory; retain project profiles/work documents.

Ask to integrate project context and analyze provided requirements, or implement/verify an agreed plan. Requesting one stage runs that stage only. Reuse existing context, refreshing relevant changes.

Keep project profiles/documents in their repositories. Distribute only this skill directory, excluding `__pycache__`, `*.pyc`, local temporary files, real private issues/project data and credentials. This change does not imply publication, installation in other agents or completed cross-agent evaluation.

## Dependencies and alternatives

- Instructions need a coding agent able to read project files. Product runtimes, DB and build dependencies come from project context.
- Checks need Python 3.9+ standard library and Git. Resolve scripts from the actual skill directory; see [automation](references/automation.md).
- Prefer applicable available `/code-review` and `/ponytail-review`; otherwise use the local two-pass review without automatic installation.
- HTML templates load Mermaid/ELK from CDN and need browser/network. Mark rendering unverified if unavailable while continuing independent analysis/structure checks.
- Both output modes share scripts/schema/behavior; choose `architecture-diagram.html` for Chinese or `architecture-diagram.en.html` for English.

## Validation and evaluation

Run local links and `scripts/test_workflow_check.py`. Links validates local targets only; self-tests use temporary repositories for inventory/structure without product DB operations.

For real agent evaluations record agent/version, inputs, fixture, artifacts, actual changes and verdict. Use isolated projects/mock issues without production access. The following are evaluation cases, not claims that they have been executed:

| Scenario | Expected observation |
|---|---|
| Forge-like, analysis only | Integrate Domo/GitLab/document rules; five-part analysis without product/DB changes |
| Different stack, no issue | Use actual project context, not Forge APIs/platform or fabricated issues |
| Existing context/partial design, implementation authorized | Check relevant changes/gaps and reuse work document without recreating every artifact |
| Review skills missing | Complete and identify two local review passes |
| Rules/manifest conflict, missing requirements | Preserve sources/questions; block dependent work only, without invented policy |
| Chinese/English mode or mid-work switch | Selected language in replies, work docs and diagrams; same work unit/identifiers |
| User edits, missing DB/browser | Preserve unrelated edits; mark unverified scope, not mock/structure as actual acceptance |

## References and license

Design references, without copying their code/full instructions: [Superpowers](https://github.com/obra/superpowers) for evidence and proportional workflow; [Spec Kit](https://github.com/github/spec-kit) for technical context and complexity justification; [create-feature](https://github.com/garethrhughes/skills/blob/main/create-feature/SKILL.md) for shared/project rules and review handoffs.

[MIT License](LICENSE). A first publication can use `v0.1.0`; no public repository URL is set, so no fictional install URL is provided. Maintain both documentation editions when changing workflow requirements; English is the execution edition.
