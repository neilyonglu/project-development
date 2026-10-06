# Operations and Data Flow

After understanding the framework, modules and tables, start from a user action or system event and explain how requirements are achieved through code and data. This stage delivers explanation/design, not construction, tests or DB operations merely because a flow was discussed.

## Inputs and evidence

Read the work's analysis, module locations and relevant table design. Trace actual entrypoints, calls and reads/writes for existing flows; propose new flows from requirements. Separate expected behavior, current implementation and open questions. Existing code does not resolve conflicting requirements.

## Explain a concrete scenario

| Step/trigger | Entrypoint/responsible module | Input/identity/config | Rule/processing | Data read | Data written and timing | Output/state | Failure/blocker behavior |
|---|---|---|---|---|---|---|---|

- Identify who triggers manual, scheduled or other events and module responsibilities.
- Put table fields into the scenario: when IDs are generated, which record is added/updated, how the same item is recognized and which fields retain snapshots.
- Distinguish query results, recalculation, submitting a decision and actual execution where those stages exist; do not force every feature into them.
- For writes, check permissions, dataset boundaries and applicable restrictions. Mark commit/transaction boundaries; partial success is not complete success.
- For async, repeat operations or retries, explain state transitions, deduplication policy and traceable outcomes. Mark unconfirmed behavior as open; do not invent retry or compensation policies.

When the user requests explanations one segment at a time, explain one operation/stage and wait for their request to continue.

## Diagrams and checks

Use editable Mermaid flow/sequence diagrams with actors, modules, data layers and boundary-crossing calls. Explain transmitted data/actions, async behavior and failure paths. Split complex flows while retaining a readable main scenario.

Map each step to requirements, code locations and tables. Distinguish available, unimplemented and unconfirmed parts. Record differences and impact when diagrams, steps and table design disagree.

## Delivery

Update the original work document with operation/data flow, preserving the analysis and DB design; document units follow project context. The user should understand modules, reads/writes, completion and residual state after failure. Flow confirmation is not implementation authorization.

For the data and error formats exchanged across layers, continue to [interface contracts](interface-contract.md) within the authorized scope. All explanatory content follows the selected output language; identifiers remain unchanged.
