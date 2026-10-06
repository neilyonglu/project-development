# Implementation Architecture HTML

Use the same diagram for step 2 of [review and delivery](review-delivery.md) and file walkthrough progress. For `zh-TW`, copy [Chinese template](../assets/architecture-diagram.html); for `en`, copy [English template](../assets/architecture-diagram.en.html). Put the view beside its work document, for example `doc/dev/issue-<n>-architecture.html` under Forge conventions. Both templates share CSS/JS behavior and schema; populate data rather than rewriting controls.

## Data sections

| Section | Content |
|---|---|
| `<html lang>` | `zh-Hant` for Traditional Chinese, `en` for English |
| `<title>`, `<h1>` | Work identity and architecture title in the selected language |
| `<script type="text/plain" id="src">` | Mermaid `flowchart TD`; retain template `classDef` |
| `<script type="application/json" id="details">` | Node descriptions keyed by ID |
| `<script type="application/json" id="parts">` | Part tabs and notes |
| Files omitted from diagram | `<li data-file="repository-relative-path"><code>path</code>reason</li>` |

Replace the complete example order content, including legend assumptions, node descriptions, part notes and omission reasons, with this work's facts. Keep IDs/files/API/DB names unchanged; use the selected language for prose and visible controls. Do not retain sample nodes or a Forge-specific layered legend in unrelated projects.

## src: nodes

- Layer top to bottom by real architecture, for example L1 Frontend → L2 Backend → L3 Service → L4 Database. Within layers group entrypoints, pages, shared components, Definitions, Config, Outbound/Inbound as applicable.
- A box represents a real file or endpoint inside a file, not an abstract concept. Shared methods appear on their files' arrows. When a file has multiple boxes, wrap them in a subgraph named after the file.
- Labels hold file/class names; explanations go in details. Technical names match code; edge explanations follow output language.

| Kind | Syntax | class |
|---|---|---|
| Read code file | `id[Name.java]` | `seen` |
| Unread code file | `id[Name.java]` | `todo` |
| Data/config/types/routes, no active behavior | `id[/AgentTypes.ts/]` | `data`, or `datatodo` if unread |
| DB table | `db_id[(table)]` | `seen` |
| External service | `id[External LLM API]` | `ext` |
| Test file | `t_id([test_x.py])` | `test` |

- Every node occurs in exactly one `class` line with one kind above. Test nodes, and only test nodes, start with `t_`; hiding tests removes lines containing test IDs.
- `fresh` (purple border for nodes new in this Part) is added by the page, not handwritten.
- `.scss` files live in the owning tsx node's `styles`/`files`, not separate boxes. Small wrapper-only components without data flow may use the omission list with reason.

## src: edges

- `a -- input → output --> b`: calls/reads/writes; labels describe data/objects rather than method names.
- `a == input ==> b`: cross-layer call, such as frontend/backend or backend/service.
- `a -. result .-> b`: return, read-only definition or callback. Use `-. text .->`, not `-. text -->`, which Mermaid misparses.
- Prefix sequential steps from the same origin with ①②③ (local numbering) rather than suggesting parallel execution.
- Tests use `t_id -. tests behavior .-> target`.
- Avoid `( ) [ ] { } " =` in labels to prevent Mermaid parsing errors.

## src: Part markers

- For stacked branches, a Part represents a branch in merge order.
- Prefix node/subgraph/end lines with `N|`, the Part where they first appear. Do not prefix edge/class lines; edges appear when both endpoints do.
- Part N shows 1..N. For N > 1, new nodes have purple outlines; an entirely new subgraph highlights its outer boundary.
- A single branch uses `1|` everywhere and parts containing the all-parts view and Part 1.

## details

```json
"repo": {
  "meaning": "One plain sentence explaining the file's business role",
  "detail": "Technical notes; separate lines with \n",
  "funcs": [["insert", "One sentence explaining this function"]],
  "styles": ["OrderForm.module.scss：Form and list layout"],
  "files": ["api/order_repo.py"]
}
```

- Every node has `meaning`. Hover shows meaning/detail; the card lists files/functions/styles.
- For new code files list each function; for files already in the comparison baseline list functions changed here. For tests explain each test. Data/DB/endpoint nodes may omit funcs.
- `files` uses repository-relative paths; multiple boxes may reference one file. Include styles, `__init__.py` and other companions under the owner. Coverage reads these and `data-file`.
- Existing DB tables/external services without repository files may omit files.
- `meaning`, `detail`, function explanations and style descriptions follow the output language. Preserve the full-width `：` style separator expected by the template; schema keys and identifiers stay unchanged.

## parts

```json
[
  {"tab": "All", "note": "All parts, without highlighting newly added nodes."},
  {"tab": "Part 1 · #92", "note": "Branch ...: what this layer adds."}
]
```

Index 0 is always the all-parts view: `All` for English or `全部` for Traditional Chinese. Notes explain each branch in one or two sentences. The schema and index semantics do not change with language.

## Walkthrough progress

- After the user actually reads a file, change `todo` to `seen` or `datatodo` to `data`. Solid means read; a later branch edit does not erase this history.
- Merely asking about a file, without reading it, leaves it unread.
- On the next branch, add missing changed files as unread; dashed boxes show remaining walkthrough work.
- Update diagram behavior, edges, states, details/functions and tests together with code changes that affect them. Reading status is separate from verification status.

## Checks

After edits use [automation](automation.md):

```text
python "<skill-dir>/scripts/workflow_check.py" diagram --html <architecture.html>
python "<skill-dir>/scripts/workflow_check.py" inventory --base <base> --output <temporary-directory>/changes.json
python "<skill-dir>/scripts/workflow_check.py" coverage --inventory <changes.json> --html <architecture.html>
```

`diagram` checks structure/unread nodes; coverage accounts for inventory files. Neither proves real call semantics.

Templates load Mermaid 11 and ELK from jsDelivr and need network access. Open with an existing browser/automation capability and check the main graph, Parts, tests, zoom and error presentation. Compare rendered SVG nodes with reported nodes; structural checks do not prove rendering.

Locate the actual browser if using headless CLI; do not fix an OS or Chrome path. Without browser/network preserve editable source and structural results, explicitly record unverified rendering/interactions and do not automatically install a browser.
