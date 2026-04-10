# Schema Developer FAQs

Some frequently asked questions about developing the NMDC Schema.

### What are some effective strategies for collaborative schema development?

[LinkML Collaborative Development](https://linkml.io/linkml/howtos/collaborative-development.html)
[Google Slides Presentation](https://docs.google.com/presentation/d/1ZH41QAoESUwAkdHyUxlrmSKS5M-bT0TOulBgX4rBx2A/edit#slide=id.g26390794265_0_693)

### How do I migrate from one version of the NMDC schema to another?

[Version 10 to 11 migration](v10-vs-v11-retrospective.md)

### How do I view the NMDC schema programmatically?

[NMDC SchemaView Documentation](schemaview.md)
[SchemaView Documentation](https://linkml.github.io/linkml/schemaview.html)

### Where is the OWL generation documentation?

[OWL Generation](owl-generation.md) -- covers current build process, recommended
config, CLI/YAML flag mapping, portal submission guidance, and upcoming LinkML changes.

### Where should I put hand-written documentation?

The `docs/` directory is a **build output directory** — `make clean` deletes
`docs/*.md` and `docs/*.html`. Tracked files in `docs/` that have no
counterpart in `src/docs/` will trigger a warning during `make clean`, but
untracked files will be silently removed. Place all hand-written documentation
in `src/docs/` instead; the build copies it into `docs/` automatically.

### What are LinkML readonly metaslots and why shouldn't I assert them?

The LinkML metamodel defines 12 **readonly** slots that are automatically populated
by the schema loader or generators: `definition_uri`, `domain_of`, `from_schema`,
`generation_date`, `imported_from`, `is_usage_slot`, `metamodel_version`, `owner`,
`source_file`, `source_file_date`, `source_file_size`, `usage_slot_name`.

**Do not add these to hand-edited schema YAML files** under `src/schema/`. The
loader fills them in at runtime, so asserting them is redundant and can cause
confusion when values drift from what the loader would compute.

For generated files like `src/schema/mixs.yaml`, the MIxS build pipeline
(`makefiles/mixs.Makefile`) strips all 12 readonly slots via `yq eval` as part
of the dematerialization step
([PR #2696](https://github.com/microbiomedata/nmdc-schema/pull/2696)).

### What architectural changes were made between Oct 2025 and Feb 2026?

| Date | PR | Change |
|------|----|--------|
| 2026-02-26 | [#2848](https://github.com/microbiomedata/nmdc-schema/pull/2848) | **Makefile reorganization**: MIxS pipeline moved to `makefiles/mixs.Makefile`, migrator targets to `makefiles/migrators.Makefile`. RDF conversion tooling removed. |
| 2026-02-26 | [#2849](https://github.com/microbiomedata/nmdc-schema/pull/2849) | **LinkML 1.10.0 upgrade**: new OWL flags (`--enum-inherits-as-subclass-of`), Python 3.9 dropped. |
| 2026-02-26 | [#2846](https://github.com/microbiomedata/nmdc-schema/pull/2846) | **Dead code removal**: `about.yaml` and experimental scripts removed. |
| 2026-02-21 | [#2302](https://github.com/microbiomedata/nmdc-schema/pull/2302) | **Downloads page**: schema-derived JSON and YAML files downloadable via docs website. |
| 2026-02-20 | [#2839](https://github.com/microbiomedata/nmdc-schema/pull/2839) | **Unified LinkML CLI**: build uses `linkml generate owl`, `linkml generate json-schema`, etc. instead of legacy `gen-owl`, `gen-json-schema`. |
| 2025-10-28 | [#2696](https://github.com/microbiomedata/nmdc-schema/pull/2696) | **Dematerialize mixs.yaml**: all 12 readonly metaslots stripped from generated `mixs.yaml` (35% line reduction). |
