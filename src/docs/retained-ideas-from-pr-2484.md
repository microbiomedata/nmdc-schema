# Retained Ideas From PR #2484

This page preserves the durable ideas from historical exploratory notes while
removing stale, host-specific, and one-off artifacts.

## 1) Validation and migration strategy

- Prefer forward migration over schema relaxation when production data fails validation.
- Use `migration-recursion` and versioned migrators as the primary compatibility path.
- Keep fixes traceable: document what was changed, why, and which records/fields were affected.
- Validate after migration against the target schema version before downstream conversion steps.

## 2) Data quality and schema hygiene

- Keep LinkML structural checks and linting in regular workflows.
- Maintain clear examples and counter-examples for constraints.
- Favor categorical slots as enums where value sets are finite.
- Reuse existing classes/slots before introducing new schema elements.

## 3) Reproducible OWL generation

- Keep OWL generation commands explicit and reproducible (flags, profile, output path).
- Treat OLS-oriented OWL generation as an experimental profile unless promoted to release workflow.
- If promoted, add a dedicated Makefile target and CI validation.

See also: [OWL generation experiments](owl-generation-experiments.md).

## 4) Contributor workflow principles

- Use issue-linked, atomic PRs with CI passing before merge.
- Keep generated/bulk artifacts out of long-lived review branches unless they are release artifacts.
- Prefer purpose-based output destinations (`docs/`, `local/`, `project/`, package artifacts).

## 5) What was intentionally not retained

- Time-specific operational notes tied to one run/session.
- Host-local details and large generated data dumps.
- Proposals that weaken schema constraints as a default path.
