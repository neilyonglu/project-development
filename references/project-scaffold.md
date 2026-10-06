# Project Scaffolding

Turn confirmed intended architecture into code structure ready for implementation. Include required data models/schema change files where DB work is involved.

## Input and scope

Read the work analysis, project conventions and nearest module. Confirm intended architecture, module changes, scope and construction blockers. Without an issue use provided requirements/architecture rather than creating an issue.

A construction request authorizes necessary local skeleton/config/migration files. A design-only request delivers a proposal, not construction. Actual DB application requires target, authorization and side-effect checks; a written migration does not mean tables exist.

Requests to understand the project, framework or DB design remain explanation/design without construction, tests or DB operations. Match requested depth; perform steps 2/4/5 only when actual construction is requested.

## 1. Framework and module boundaries

- For new projects choose from requirements, deployment and constraints. For existing projects verify/reuse actual framework, versions, paths and module conventions.
- Map intended parts to modules, entrypoints, calls and interfaces. Separate reuse/change/add; avoid skeleton abstractions unused by requirements.
- Wait only on choices affecting construction; record evidence rather than presenting agent preference as a requirement.

## 2. Necessary skeleton

Create required directories, entrypoints, contracts, configuration and startup using existing naming, errors, identity and data access. Check cross-layer companions such as UI routes/calls, backend entrypoints, service/Domo and metadata.

Label pending business algorithms. Never disguise incomplete flows with fixed success responses. Extend necessary structure for existing features rather than creating another project.

## 3. Data models, if applicable

Check real schema/semantics and list reused/changed/new tables with requirement purpose. Without DB changes record why tables are unnecessary rather than adding empty tables.

Explain every in-scope table, including reused tables: business purpose, row meaning, read/write ownership and creation/update/history timing. Use a concrete scenario to explain collaboration between tables.

| Field | Business meaning/reason | Type/length/precision | Nullable/NULL semantics | Default/generation | Constraints/relationships |
|---|---|---|---|---|---|

- Specify primary keys, ID/sequence source, unique combinations/business reasons and query-backed indexes.
- Identify related fields/cardinality; distinguish logical relationships from physical FKs. Explain consistency without FKs or mark it unchecked.
- Enumerate valid states/transitions; distinguish recommendation, human decision and execution, avoiding one state that falsely implies whole-process completion.
- Check applicable dataset/tenant, timezones/business dates, lifecycle/audit without adding unrequested model features.
- Label design/model/metadata/migration declarations versus actual DB verification. Record discrepancies/missing definitions; Python types do not establish DB length/default/constraints.

When asked to explain table by table, explain one and wait for the next request. Keep formal design in the original work document; this guide does not fix an issue's field names.

Add ER diagrams if needed. For changes to existing data types, required fields, uniqueness or relationships explain conversion, backfill and compatibility; do not convert NULL to zero without confirmed semantics.

For connecting tables/modules in an operation, use [operation flow](operation-flow.md) before construction as appropriate to existing authorization.

## 4. Schema changes and companions

Reuse migration, metadata or appUpgrade; do not introduce a second upgrade process. Prepare reviewable files, model declarations and fixtures; explain application order, existing-data handling and failure recovery without promising impossible lossless rollback.

Record designed, change files written, applied to named DB and schema verified separately. Apply upgrades only to authorized targets. If application is not authorized, finish files/verification plan before requesting necessary approval for the concrete action.

## 5. Minimal executable path

Verify required modules start, interfaces connect and settings load. Verify schema/access in an appropriate authorized environment if DB is involved. Do not accidentally connect to production, clear schema or call paid models.

Not every skeleton needs UI or DB; choose a meaningful requirements path. Startup/compilation is not business completion. Record missing environments, unverified scope and reproducible steps.

## Delivery and handoff

Update original analysis with construction progress, retaining five parts: framework decisions, actual changes, DB declaration/application, startup/check results and next business capability. Resolve discrepancies between intended architecture and skeleton locations with evidence.

Use the selected output language for explanations. Deliver reviewable results without automatically starting unauthorized feature implementation, deployment, remote comments or DB operations.
