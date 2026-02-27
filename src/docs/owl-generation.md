# OWL Generation

This page documents how nmdc-schema generates OWL, configuration options,
portal submission guidance, and upcoming changes.

---

## Current OWL generation

The Makefile `gen-project` target runs `linkml generate project` with `--include owl`:

```makefile
$(RUN) linkml generate project \
    --exclude excel --exclude graphql --exclude jsonld \
    --exclude markdown --exclude proto --exclude shacl \
    --exclude shex --exclude sqlddl \
    --include jsonldcontext --include jsonschema \
    --include owl \
    --include python --include rdf \
    --config-file gen-project-config.yaml \
    -d $(DEST) $(SOURCE_SCHEMA_PATH)
```

This produces `project/owl/nmdc.owl.ttl` (~1.3 MB). The config file
(`gen-project-config.yaml`) currently has **no OWL-specific settings** -- only a
JSON Schema option:

```yaml
generator_args:
  jsonschema:
    include_range_class_descendants: true
```

The OWL output is gitignored, not included in the PyPI package, and not published
in the docs. Per [#2749](https://github.com/microbiomedata/nmdc-schema/issues/2749),
nobody appears to consume it. There is no standalone `linkml generate owl`
Makefile target -- OWL is only produced as a side effect of `gen-project`.

---

## Recommended OWL config

The following config is used by Biolink, Biostride, NAMO, COMET, and MIxS
(established in [linkml-project-copier PR #96](https://github.com/linkml/linkml-project-copier/pull/96)):

```yaml
generator_args:
  owl:
    mergeimports: true
    metaclasses: false
    type_objects: false
    add_root_classes: true
    mixins_as_expressions: true
```

Key settings explained:

| Setting | Purpose |
|---------|---------|
| `mergeimports: true` | Inlines imported schemas so the OWL is self-contained (portals won't resolve import chains) |
| `metaclasses: false` | Avoids OWL punning from LinkML metamodel classes |
| `type_objects: false` | Don't model types as class shadows |
| `add_root_classes: true` | Adds metamodel supertypes for a browsable hierarchy in portals |
| `mixins_as_expressions: true` | Mixins become existential restrictions instead of subClassOf |

PR #2484's experimental profile diverges from this standard in two ways:
it sets `metaclasses: true` (adds metamodel categorization at the cost of
OWL punning) and `mixins_as_expressions: false` (keeps mixin subClassOf
relationships). For portal submission, the standard config above is the
safer starting point.

---

## Configuring OWL: config YAML vs CLI flags

OWL generation options can be passed two ways:

1. **`gen-project-config.yaml`** -- per-generator settings under `generator_args`
   (preferred for `linkml generate project`)
2. **CLI flags** -- required for standalone `linkml generate owl`

The `generator_args` dictionary maps generator names to keyword arguments passed
to each generator's class constructor. For OWL, the key is `owl`. Internally,
the project generator merges default args with config args and passes them as
`**kwargs` to `OwlSchemaGenerator(schema, **all_gen_args)`.

CLI dashes become underscores. Boolean `--flag/--no-flag` pairs become
`flag: true/false`.

### OWL-specific options

| CLI Flag | Config YAML Key | Type | Default |
|----------|----------------|------|---------|
| `--metadata-profile` | `metadata_profile` | `str` (`linkml`, `rdfs`, `ols`) | `linkml` |
| `--add-root-classes / --no-add-root-classes` | `add_root_classes` | `bool` | `false` |
| `--metaclasses / --no-metaclasses` | `metaclasses` | `bool` | `false` |
| `--add-ols-annotations / --no-add-ols-annotations` | `add_ols_annotations` | `bool` | `true` |
| `--type-objects / --no-type-objects` | `type_objects` | `bool` | `false` |
| `--assert-equivalent-classes / --no-...` | `assert_equivalent_classes` | `bool` | `false` |
| `--mixins-as-expressions / --no-...` | `mixins_as_expressions` | `bool` | `false` |
| `--use-native-uris / --no-use-native-uris` | `use_native_uris` | `bool` | `true` |
| `--default-permissible-value-type` | `default_permissible_value_type` | `str` | `owl:Class` |
| `--enum-iri-separator` | `enum_iri_separator` | `str` | `#` |
| `--ontology-uri-suffix` | `ontology_uri_suffix` | `str` | `.owl.ttl` |
| `--enum-inherits-as-subclass-of` | `enum_inherits_as_subclass_of` | `bool` | `false` |
| *(no CLI flag)* | `simplify` | `bool` | `true` |
| *(no CLI flag)* | `use_swrl` | `bool` | `false` |
| *(no CLI flag)* | `target_profile` | `str` (`dl`, `full`) | `dl` |

### Cross-generator common options (also work under `owl:`)

| CLI Flag | Config YAML Key | Type |
|----------|----------------|------|
| `--format` | `format` | `str` |
| `--metadata / --no-metadata` | `metadata` | `bool` |
| `--mergeimports / --no-mergeimports` | `mergeimports` | `bool` |
| `--useuris / --metauris` | `useuris` | `bool` |
| `--log_level` | `log_level` | `str` |

### Options that can ONLY be passed via CLI (not config YAML)

| CLI Flag | Reason |
|----------|--------|
| `--include / --exclude` | Project-level generator selection, not per-generator |
| `--config-file` | The config file path itself |
| `-d` (output directory) | Project-level setting |
| `-o` (output file) | Passed to `serialize()`, not constructor |

### Example: equivalent config for the PR #2484 experimental profile

The experimental CLI command from PR #2484:

```bash
poetry run linkml generate owl \
  --add-ols-annotations --metadata-profile ols --add-root-classes \
  --metaclasses --mergeimports --use-native-uris --useuris \
  --default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
  --enum-iri-separator "#" --format owl --metadata \
  --no-assert-equivalent-classes --no-mixins-as-expressions \
  --no-type-objects --no-stacktrace \
  --ontology-uri-suffix .owl.ttl --log_level WARNING \
  src/schema/nmdc.yaml > local/nmdc-schema.ols.owl.ttl
```

Could instead be expressed in `gen-project-config.yaml` as:

```yaml
generator_args:
  jsonschema:
    include_range_class_descendants: true
  owl:
    metadata_profile: ols
    add_ols_annotations: true
    add_root_classes: true
    metaclasses: true
    mergeimports: true
    use_native_uris: true
    useuris: true
    metadata: true
    type_objects: false
    assert_equivalent_classes: false
    mixins_as_expressions: false
    default_permissible_value_type: "http://www.w3.org/2002/07/owl#Class"
    enum_iri_separator: "#"
    ontology_uri_suffix: ".owl.ttl"
    format: owl
    log_level: WARNING
```

No CLI changes to the Makefile `gen-project` target would be needed -- just
updating the config YAML would change the OWL output.

---

## Submitting to ontology portals

```
LinkML YAML schema (src/schema/nmdc.yaml)
    |
    v
linkml generate owl (with OLS-tuned config)
    |
    v
OWL file (nmdc-schema.ols.owl.ttl)
    |
    +---> BioPortal (self-service upload or pull URL)
    |       - Low barrier, immediate
    |
    +---> OLS4 (GitHub issue + spreadsheet at EBISPOT/ols4)
            - Curated, weeks-to-months review
            - Embeddings, semantic search, AI integration
            - Fill spreadsheet carefully (learn from MIxS mistakes)
            - May eventually separate schemas from ontologies (#1039)
```

### BioPortal

Self-service submission at [bioportal.bioontology.org](https://bioportal.bioontology.org/).
Upload the OWL file or point to a stable URL. Display is immediate after
processing.

### OLS4

Curated submission via [EBISPOT/ols4](https://github.com/EBISPOT/ols4). Requires
filling the [OLS submission spreadsheet](https://github.com/EBISPOT/ols4/blob/dev/New%20OLS%20ontology%20request.xlsx)
and opening a GitHub issue.

Recommended spreadsheet values for nmdc-schema:

| Field | Value | Notes |
|-------|-------|-------|
| `id` | `nmdcschema` (or similar, 5+ chars, lowercase) | Must be unique across OLS |
| `preferredPrefix` | `nmdc` or `NMDC` | Controls CURIE display. Match your actual CURIE pattern. |
| `base_uri` | `https://w3id.org/nmdc/` | **Full URI, NOT a CURIE** (MIxS got this wrong) |
| `ontology_purl` | Stable URL where OLS fetches the OWL | Could be raw GitHub URL or w3id redirect |
| `definition_property` | `skos:definition` or `IAO:0000115` | Whichever your OWL uses |
| `label_property` | `rdfs:label` | **Only annotation properties** |

### Schemas vs ontologies in OLS4

[EBISPOT/ols4#1039](https://github.com/EBISPOT/ols4/issues/1039) proposes
separating schema-like artifacts (schema.org, biolink, MIxS) from ontologies in
OLS4, potentially with a separate "Schemas" tab and lower search boosting.
This doesn't block submission but is worth tracking.

---

## MIxS as a worked example

MIxS is the closest precedent for getting a LinkML schema into ontology portals.

### Submission timeline

MIxS was submitted to OLS4 via [EBISPOT/ols4#951](https://github.com/EBISPOT/ols4/issues/951)
(Aug 2025, by Peter Woollard / EBI). The OWL file is published at a stable GitHub
raw URL from the MIxS repository (`https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/project/owl/mixs.owl.ttl`).

### What went right

- OWL file at a stable URL with 625 DatatypeProperty terms
- Permanent URL at `https://w3id.org/mixs`
- Labels via `rdfs:label`, definitions via `skos:definition`

### Configuration mistakes to avoid

The OWL file itself was correct -- the OLS4 intake spreadsheet had wrong values
([EBISPOT/ols4#1136](https://github.com/EBISPOT/ols4/issues/1136)):

| Problem | Cause | Fix |
|---------|-------|-----|
| CURIEs show as bare numbers (`0001107` not `MIXS:0001107`) | `preferredPrefix` set to `gscmixs` instead of `MIXS` | Use uppercase prefix matching your CURIE pattern |
| Labels/definitions not displaying | `base_uri` used CURIE (`MIXS:`) instead of full URI (`https://w3id.org/mixs/`) | Always use full URI |
| Wrong label_property | Array included `owl:DatatypeProperty` (an RDF type, not a label property) | Use `rdfs:label` only |

### Zero Named Individuals requirement

OLS and other ontology browsers expect schemas to have zero Named Individuals.
If individuals are present, the OWL may be treated as instance data rather than
a schema/TBox. Verify this in Protege before submission.

### OLS display bugs

Chris Mungall and Nico Matentzoglu identified that display bugs in OLS for MIxS
([EBISPOT/ols4#1136](https://github.com/EBISPOT/ols4/issues/1136)) were all
OLS configuration problems, not OWL generation problems. Nico contributed an
`owl:Class` syntax fix upstream.

---

## Validation checklist

Before submitting to portals:

- [ ] **Protege**: Open the OWL file, check for parse errors, confirm zero Named Individuals
- [ ] **ROBOT report**: Run if pursuing OBO Foundry compliance
- [ ] **Automated checks**: Compare class/property counts against expectations, review warnings from gen-owl
- [ ] **Known nmdc-schema OWL issues**:
    - [#2771](https://github.com/microbiomedata/nmdc-schema/issues/2771): `equals_string` warnings, "Multiple owl types" error
    - [#2614](https://github.com/microbiomedata/nmdc-schema/issues/2614): Un-escaped UCUM unit brackets break OWL syntax
    - [#1728](https://github.com/microbiomedata/nmdc-schema/issues/1728): MIxS slot URIs use names instead of numeric IDs
    - [#1467](https://github.com/microbiomedata/nmdc-schema/issues/1467): Long-standing goal to produce error-free OWL

---

## Upcoming LinkML changes

Three open PRs (all by @mgskjaeveland, updated 2026-02-26) will change OWL
generation behavior in the next LinkML release:

| PR | What | Impact | Default |
|----|------|--------|---------|
| [#3187](https://github.com/linkml/linkml/pull/3187) | `children_are_mutually_disjoint` implemented | Previously silently ignored. Will emit `owl:AllDisjointClasses`. If any nmdc-schema class uses this flag, OWL output changes. | Respects existing flag |
| [#3219](https://github.com/linkml/linkml/pull/3219) | Covering axiom for abstract classes | Every `abstract: true` class with children gets `AbstractClass rdfs:subClassOf (Child1 or Child2 or ...)`. Significant change for nmdc-schema which has abstract classes. | **On by default**. Suppress with `--skip-abstract-class-as-unionof-subclasses`. |
| [#3221](https://github.com/linkml/linkml/pull/3221) | `xsd:anyURI` emitted as URIRef instead of typed literal | Changes RDF serialization of URI-typed slots. nmdc-schema has many URI-typed identifiers. | N/A -- behavior change (by Corey Cox) |

Already available in v1.10.0 (nmdc-schema's current version):

| Change | PR |
|--------|----|
| `--enum-inherits-as-subclass-of` flag | [#3189](https://github.com/linkml/linkml/pull/3189) |
| `subproperty_of` support in generators | [#3065](https://github.com/linkml/linkml/pull/3065) |

---

## Open questions and next steps

- **Should `--include owl` stay in gen-project?**
  [#2749](https://github.com/microbiomedata/nmdc-schema/issues/2749) asks whether
  anyone uses the current OWL output. If submitting to portals, the OLS-tuned
  profile should be a separate Makefile target rather than the `gen-project` side
  effect.

- **Should the OLS-tuned config go into gen-project-config.yaml?**
  Adding an `owl:` block to the existing config would change the default OWL
  output without any Makefile changes. This is the lowest-friction path but
  conflates the "build" OWL with the "portal submission" OWL.

- **Portal submission timeline**: BioPortal first (low barrier, iterate), then
  OLS4 using the MIxS submission as a template. Resolve existing OWL issues
  ([#2771](https://github.com/microbiomedata/nmdc-schema/issues/2771),
  [#2614](https://github.com/microbiomedata/nmdc-schema/issues/2614)) before
  submitting.

- **Wait for LinkML PRs #3187 and #3219 to merge** before generating a
  portal-ready OWL -- they will change output for abstract classes and disjoint
  children.

- **Test `--enum-inherits-as-subclass-of`** (available now in v1.10.0) to see
  if enum hierarchies improve portal browsability.

---

## References

| Resource | URL |
|----------|-----|
| LinkML OWL generator docs | <https://linkml.io/linkml/generators/owl.html> |
| linkml-project-copier standard config | [PR #96](https://github.com/linkml/linkml-project-copier/pull/96) |
| MIxS OLS submission | [EBISPOT/ols4#951](https://github.com/EBISPOT/ols4/issues/951) |
| MIxS OLS display bugs | [EBISPOT/ols4#1136](https://github.com/EBISPOT/ols4/issues/1136) |
| Schemas vs ontologies in OLS | [EBISPOT/ols4#1039](https://github.com/EBISPOT/ols4/issues/1039) |
| nmdc-schema OWL usage question | [#2749](https://github.com/microbiomedata/nmdc-schema/issues/2749) |
| OWL generation warnings | [#2771](https://github.com/microbiomedata/nmdc-schema/issues/2771) |
| OLS submission spreadsheet | [New OLS ontology request.xlsx](https://github.com/EBISPOT/ols4/blob/dev/New%20OLS%20ontology%20request.xlsx) |
