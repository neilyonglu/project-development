# Executable Workflow Checks

`<skill-dir>` is the actual absolute directory of the loaded skill; substitute its real location, including quotes for spaces. Product paths are repository-relative and skill resources are skill-relative. Python 3.9+ and local Git are required; verify the existing runtime rather than installing dependencies.

`scripts/workflow_check.py` uses Python's standard library and Git. It does not read product contents/full diffs, fetch, mutate Git/DB or call models. Only inventory `--output` writes the requested JSON. Run from the repository root.

## 1. Change inventory

```text
python "<skill-dir>/scripts/workflow_check.py" inventory --base <confirmed-commit-or-ref> --output <temporary-directory>/changes.json
```

Confirm the base first. It compares `base..HEAD` plus staged, unstaged and unignored untracked files. It does not guess main/merge-base. Include old/new rename paths and source layers rather than treating them as one final state. Write outside the repository so future inventories do not include their own output.

Repeat `--exclude <exact-repository-relative-path>` for confirmed unrelated changes. JSON retains exclusions and reports unmatched paths; the script does not infer issue scope. Ignored files are absent. Submodule entries cover the root repository only; run separately inside an affected submodule.

## 2. Architecture file coverage

Pages from the [diagram guide](architecture-diagram.md) expose paths in node `files`. A file can appear in multiple nodes. Files not drawn as nodes need a visible list with repository-relative `data-file` and a reason/related node/removal explanation:

```html
<li data-file="src/service.py">Service node: handles requests</li>
<li data-file="tests/test_service.py">Test node: checks error responses</li>
```

```text
python "<skill-dir>/scripts/workflow_check.py" coverage --inventory <changes.json> --html <architecture.html>
```

Checks inventory declarations, including old rename paths, and reports gaps/duplicates. Extra paths may be reused dependencies and need review. Refresh inventory before comparison to include fixes. Coverage proves declaration only, not correct nodes/edges/test targets or renderability.

## 3. Diagram structure

```text
python "<skill-dir>/scripts/workflow_check.py" diagram --html <architecture.html>
```

Checks `src`/`details`/`parts`, exactly one valid class per node, details with `meaning`, test/t_ consistency, declared edge endpoints, valid Part tabs, dotted-edge syntax and path existence against `--repo` (current directory by default). `todo` lists unread nodes. It does not establish actual calls or render the page. Both language templates use this same schema/checker.

## 4. Local skill links

```text
python "<skill-dir>/scripts/workflow_check.py" links
```

By default checks this skill's Markdown inline local file links, skipping fenced examples, remote URLs and pure anchors. It does not validate heading anchors, reference-style links or remote accessibility. Use `--root <directory>` for other scoped documentation, not an automatic full-repository scan.

## Interpretation and self-tests

Exit 0 means no mechanical gaps, 1 means gaps/duplicates/unmatched exclusions, and 2 means execution error. After relevant script/rule changes use isolated-repository self-tests:

```text
python "<skill-dir>/scripts/test_workflow_check.py"
```

Use structured output to locate problems and read necessary files. Scripts do not decide requirements, useful parameters, naming, data flow or test quality. Use existing lint/typecheck/build as appropriate; do not add a generic test runner.

Technical keys, diagnostics and paths remain stable across output modes. Explain findings in the selected language rather than changing the machine-readable schema.
