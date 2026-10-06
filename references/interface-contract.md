# Interface Contracts

Once operations are clear, confirm cross-module calls and frontend data exchange. This stage delivers explanation/design, not feature edits, test execution or DB operations merely because contracts are being discussed.

## Evidence and scope

Read requirements, operation flow and relevant data models. Select the interfaces the flow needs. For existing interfaces inspect callers, receivers, types and validation; propose new contracts from requirements. Separate implementation, proposed design and unresolved items. Type declarations do not prove runtime validation.

## Explain each interface

Identify caller, receiver, purpose, trigger and actual entrypoint: API method/path, RPC method, function or component Props. Follow the project's calling conventions rather than converting every interface to REST.

Provide input and output field tables:

| Field | Meaning | Type/allowed values/unit | Required/default/NULL semantics | Source/calculation owner | Validation |
|---|---|---|---|---|---|

- Identify sources and enforcement of identity, dataset, permissions and configuration; client-provided identity is not inherently trusted.
- Specify success, empty results, validation/permission failures and realistic blockers, including error shape and caller handling.
- For batch/async operations distinguish request accepted, decision saved and execution completed. Define per-item results and partial success.
- Check existing repeat-submission, retry and compatibility behavior where relevant. Unconfirmed policy remains a question; do not automatically add versions or retry mechanisms.
- Define units, precision/rounding, timezones and boundaries. For external data identify missing fields, unknown values and incompatible formats/versions, not only successful connections.

## UI data and Props mapping

Map returned data to component values, options, enabled states and indicators; identify transformation/calculation ownership and callback actions. Verify optional Props, defaults and disabling against real components; identify comment/behavior discrepancies.

DB fields, API fields and Props need not map one to one. Explain transformations and responsibility to avoid duplicated business decisions across layers.

Confirm data/actions for loading, empty, failed, unsaved and partially successful states using applicable [correctness checks](implementation-validation.md#correctness-checks).

## Delivery and handoff

Update the original work document according to project context. Map contracts to flows, modules, DB fields and UI; identify agreements, missing definitions and conflicts. Explain one interface at a time when requested. Contract confirmation alone does not authorize construction/implementation.

For expected outcomes across conditions, use [business acceptance](business-acceptance.md). Write explanations in the selected output language while preserving contract identifiers.
