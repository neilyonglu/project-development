# project-development

English | [繁體中文](README.zh-TW.md)

A project-aware development skill for requirements, design, implementation and traceable review. Preserve the author's development logic: integrate the current project's characteristics, workflow and dependencies first, then select requirements analysis, design, planning, implementation, validation and two review passes. Includes requirement-to-implementation/acceptance traceability and editable HTML architecture/test views.

## Language modes

The agent uses the English [SKILL.md](SKILL.md) and English stage guides under `references/` for both modes. [Traditional Chinese workflow](SKILL.zh-TW.md) and `references/zh-TW/` are reading/maintenance translations. Install one skill, not separate language variants.

Default output is `zh-TW`; request `en` for English. An explicit current user choice takes precedence over recorded project preference, then the default. Carry the choice forward until changed. English operating instructions cannot guarantee the language of private reasoning; the workflow does not request private chain of thought.

- Chinese: "使用 project-development，先整合此專案脈絡，輸出用繁體中文。"
- English: "Use project-development. Integrate this project's context first and produce all deliverables in English."
- Switch: "Use English output from now on and keep the existing work document."

The mode applies to replies, work documents, reviews and visible diagram prose/controls. Preserve code/API/DB identifiers, commands, paths and quotations. Code comments follow project conventions. Do not translate the entire existing project or create duplicate work documents just because a mode changes.

## Quick install

Requires Node.js/npm and Git. Run in the project that should use this skill:

```bash
npx skills add neilyonglu/project-development --skill project-development
```

Select your agent when prompted. For a non-interactive project install:

```bash
# Codex
npx skills add neilyonglu/project-development --skill project-development --agent codex --yes

# Claude Code
npx skills add neilyonglu/project-development --skill project-development --agent claude-code --yes
```

Add `--global` to either command for a personal installation across projects. Use `--copy` if symbolic links are unavailable. These commands use the [Skills CLI](https://github.com/vercel-labs/skills).

Inspect available skills, update installed skills or remove this skill:

```bash
npx skills add neilyonglu/project-development --list
npx skills update project-development
npx skills remove project-development
```

If you prefer direct download, get the [main ZIP](https://github.com/neilyonglu/project-development/archive/refs/heads/main.zip), or clone into your agent's supported skills directory:

```bash
git clone https://github.com/neilyonglu/project-development.git project-development
```

Keep the complete directory, including `references/`, `scripts/`, `assets/` and `agents/`. To update a direct Git installation, run `git -C project-development pull --ff-only`; it stops rather than overwriting divergent local history.

## First use

In Codex:

```text
Use $project-development to integrate this project's architecture, conventions and available tools, then analyze the provided requirements. Output in Traditional Chinese.
```

In Claude Code:

```text
/project-development Integrate this project's context, then analyze the provided requirements. Output in English.
```

English instructions drive both language modes. Change only the requested output language; the skill preserves your project's workflow. Request one stage or authorize a sequence; existing context is reused.

## Installation scope and packaging

Project profiles and work documents stay in their own repositories. This repository contains the reusable skill only. Exclude `__pycache__`, `*.pyc`, local temporary files, private issue/project data and credentials from distributions. Installation does not prove product behavior or full cross-agent workflow evaluation.

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
| Sample multi-module project, analysis only | Integrate domain/service/platform/document conventions; five-part analysis without product/DB changes |
| Different stack, no issue | Use actual project context, not another project's APIs/platform or fabricated issues |
| Existing context/partial design, implementation authorized | Check relevant changes/gaps and reuse work document without recreating every artifact |
| Review skills missing | Complete and identify two local review passes |
| Rules/manifest conflict, missing requirements | Preserve sources/questions; block dependent work only, without invented policy |
| Chinese/English mode or mid-work switch | Selected language in replies, work docs and diagrams; same work unit/identifiers |
| User edits, missing DB/browser | Preserve unrelated edits; mark unverified scope, not mock/structure as actual acceptance |

## References and license

Design references, without copying their code/full instructions: [Superpowers](https://github.com/obra/superpowers) for evidence and proportional workflow; [Spec Kit](https://github.com/github/spec-kit) for technical context and complexity justification; [create-feature](https://github.com/garethrhughes/skills/blob/main/create-feature/SKILL.md) for shared/project rules and review handoffs.

[MIT License](LICENSE). Skill version: `0.1.0`. Source: [neilyonglu/project-development](https://github.com/neilyonglu/project-development). Maintain both documentation editions when changing workflow requirements; English is the execution edition.
