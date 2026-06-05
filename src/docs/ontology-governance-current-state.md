# Ontology Governance — Current State

This document describes how nmdc-schema currently handles ontology references:
what is declared, what is enforced, what is advisory, and what is known
technical debt. It is descriptive, not prescriptive.

**The end-state policy has not yet been written.** Two open issues have been
tracking this gap since 2023–2024:

- [#1132](https://github.com/microbiomedata/nmdc-schema/issues/1132) — "ongoing review of preferred ontologies and other external namespaces"
- [#1848](https://github.com/microbiomedata/nmdc-schema/issues/1848) — "NMDC guidelines for usage of available ontologies"

The closest thing to a formal policy statement is from closed issue
[#1099](https://github.com/microbiomedata/nmdc-schema/issues/1099):
**"a real OBO Foundry ontology with axioms is always best."**

---

## How prefixes work in this schema

The `prefixes:` block in `src/schema/nmdc.yaml` is the **operational allowlist**.
Any CURIE used in a `meaning:`, mapping, or `id_prefixes:` declaration must resolve
through a declared prefix. There is no `default_curi_maps:` — resolution depends
entirely on what is explicitly declared.

There are three separate enforcement contexts:

| Context | What is checked | What happens with undeclared prefix |
|---|---|---|
| **Schema-level CURIEs** (meanings, mappings) | IRI expansion via `SchemaView.expand_curie()` | Silently returns raw CURIE string; broken IRIs in OWL output |
| **Data validation** (biosample records, etc.) | String pattern only (`^prefix:local_id$`) | Passes — no prefix lookup |
| **JSON-LD context / RDF** | Prefix must be declared to expand to an IRI | Undeclared prefix → CURIE treated as opaque string, won't resolve |

**Implication for data:** A biosample field value of `FMA:12345` will pass
schema validation even if `FMA` were removed from the prefix block. But it
would not resolve to an IRI in RDF serialization without the prefix declaration.

**Implication for schema authoring:** A `meaning:` or mapping referencing
an undeclared prefix will not cause a build failure, but it will produce
broken output in OWL generation. `linkml lint` does not catch this.

Also relevant: [GitHub Discussion #2003](https://github.com/microbiomedata/nmdc-schema/discussions/2003)
states that `meaning:` values "must come from vocabularies that are already
known to the nmdc-schema, via a `prefixes` block."

---

## The prefix block

The schema declares ~95 prefixes, falling into four functional categories.

### Category 1 — Ontology terms (semantic grounding)

These are used in `meaning:` fields, mappings, and `class_uri:`/`slot_uri:`.
They are the primary interest for ontology alignment work.

#### Broadly used (no scoping comments)

These prefixes are used throughout the schema without documented restrictions.

| Prefix | IRI base | OBO Foundry | Usage in schema |
|---|---|---|---|
| `OBI` | `http://purl.obolibrary.org/obo/OBI_` | Yes | 26 `meaning:` + 19 mappings — planned processes, assays, instruments |
| `CHEBI` | `http://purl.obolibrary.org/obo/CHEBI_` | Yes | 23 `meaning:` — chemical substances |
| `ENVO` | `http://purl.obolibrary.org/obo/ENVO_` | Yes | env triad guidance (prose); ~1,319 rows in OLS4 results |
| `NCBITaxon` | `http://purl.obolibrary.org/obo/NCBITaxon_` | Yes | Taxonomy; used in MIxS `structured_patterns` and `ControlledIdentifiedTermValue` examples |
| `GO` | `http://purl.obolibrary.org/obo/GO_` | Yes | `has_function` pattern (enforced via regex) |
| `UBERON` | `http://purl.obolibrary.org/obo/UBERON_` | Yes | Accepted alongside ENVO for env triad (anatomy) |
| `PATO` | `http://purl.obolibrary.org/obo/PATO_` | Yes | 1 `meaning:` — quality/attribute terms |
| `PO` | `http://purl.obolibrary.org/obo/PO_` | Yes | Accepted for plant-associated env triad |
| `SO` | `http://purl.obolibrary.org/obo/SO_` | Yes | 1 mapping — sequence features |
| `RO` | `http://purl.obolibrary.org/obo/RO_` | Yes | Relation ontology |
| `PR` | `http://purl.obolibrary.org/obo/PR_` | Yes | Protein Ontology; `id_prefixes` on GeneProduct |
| `UO` | `http://purl.obolibrary.org/obo/UO_` | Yes | 1 mapping — units |
| `CHMO` | `http://purl.obolibrary.org/obo/CHMO_` | Yes | 3 mappings — chemical methods |
| `BFO` | `http://purl.obolibrary.org/obo/BFO_` | Yes | Declared; ~3 indirect references via OBI |
| `MS` | `http://purl.obolibrary.org/obo/MS_` | Yes | 8 `meaning:` + 11 mappings — mass spectrometry terms |
| `TAXRANK` | `http://purl.obolibrary.org/obo/TAXRANK_` | Yes | 7 mappings — taxonomic ranks |

#### Scoped (inline comments limit where they may be used)

These prefixes have documented restrictions in the prefix block itself.

| Prefix | Documented scope | OBO Foundry |
|---|---|---|
| `NCIT` | Biosample, Study, StudyCategoryEnum PVs, doi_provider, funding_sources, extraction_targets, 'BAI File' | Yes |
| `GENEPIO` | `library_preparation_kit`, contig identifier and count only | Yes |
| `FBcv` | Biosample only | Yes |
| `OMIT` | RNA subtypes only | Yes |
| `SIO` | Study, StudyCategoryEnum PVs, objective | No (semanticscience.org) |
| `EFO` | 1 mapping (undocumented scope) | No (EBI) |
| `MCO` | (no comment; declared for microbial conditions) | Candidate |
| `MISO` | 1 mapping on ChemicalConversionProcess | Yes |
| `MESH` | 2 mappings (undocumented scope) | No (NLM) |

**Note:** The scoping comments are advisory only. There is no schema mechanism
that prevents using NCIT outside the listed contexts. Enforcement is by convention.

#### Needed but not yet declared

| Prefix | Reason | Status |
|---|---|---|
| `COB` | OBI:0000011 (PlannedProcess) is deprecated; replacement is COB:0000035 | See [#2843](https://github.com/microbiomedata/nmdc-schema/issues/2843), [#2906](https://github.com/microbiomedata/nmdc-schema/issues/2906) |

#### Explicitly rejected

| Prefix | Reason |
|---|---|
| `CFo` (ChemFOnt) | No BFO/COB grounding; uses OBO namespace without being OBO Foundry; Protege parsing errors. See [#1848](https://github.com/microbiomedata/nmdc-schema/issues/1848) |

One `meaning: CFo000000033` reference survived in a commented-out slot — not active.

---

### Category 2 — Functional annotation databases

These are identifier namespaces used in `has_function` and related slots.
They are not ontologies in the semantic grounding sense.
The `has_function` slot enforces these prefixes via an explicit regex pattern
(the only place in the schema where ontology prefix is actually machine-enforced).

`KEGG_PATHWAY`, `KEGG.REACTION`, `RHEA`, `MetaCyc`, `EC`, `GO`, `MetaNetX`,
`SEED`, `KEGG.ORTHOLOGY`, `EGGNOG`, `PFAM`, `TIGRFAM`, `SUPFAM`, `CATH`,
`PANTHER.FAMILY`

---

### Category 3 — Data source identifiers

These identify external databases, sample repositories, and institutional systems.
They are not used for semantic grounding — only for identifying entities.

`gold`, `bioproject`, `biosample`, `insdc.sra`, `img.taxon`, `jgi.analysis`,
`jgi.proposal`, `gnps.task`, `MASSIVE`, `emsl.project`, `ORCID`, `ror`, `doi`,
`HMDB`, `PUBCHEM.COMPOUND`, `CHEMBL.COMPOUND`, `DRUGBANK`, `KEGG.COMPOUND`,
`UniProtKB`, `CATH`, `PFAM`, `PFAM.CLAN`, `PANTHER.FAMILY`, `SUPFAM`,
`TIGRFAM`, `EGGNOG`, `COG`, `SEED`

---

### Category 4 — Technical debt / placeholders

These use `example.org` URIs, are marked "temporary," or exist only because
data already in MongoDB uses them. They do not resolve to any real namespace.

| Prefix | Comment in schema |
|---|---|
| `Contaminant` | "only because it is present in MongoDB" |
| `NCBI` | "temporary. see https://github.com/microbiomedata/issues/issues/893" |
| `ISA` | no comment |
| `MetaNetX` | no comment (also appears in functional annotation pattern) |
| `RetroRules` | no comment |
| `emsl` | `emsl_in_mongodb` |
| `emsl_uuid_like` | no comment |
| `generic` | no comment |
| `gtpo` | no comment; used as `id_prefixes` on GeneProduct |
| `jgi` | no comment |
| `neon.identifier` | no comment |
| `neon.schema` | no comment |

---

### Special case: FMA

`FMA` (Foundational Model of Anatomy) is declared but **never used as a CURIE**
anywhere in the schema. Two MIxS slots (`host_body_site`, `host_body_product`)
describe "FMA or UBERON" as acceptable values in free-text annotations, but
no schema CURIE references FMA. The prefix is retained to populate the
JSON-LD context so that FMA CURIEs in biosample data correctly expand to IRIs
during RDF serialization. See [#2920](https://github.com/microbiomedata/nmdc-schema/issues/2920).

---

## What the schema enforces vs. what is advisory

| Mechanism | Enforcement level | Example |
|---|---|---|
| Prefix block | Hard — CURIEs with undeclared prefixes produce broken OWL IRIs | Must declare a prefix before using it in `meaning:` |
| `has_function` regex pattern | Hard — data validation rejects non-matching CURIEs | `PFAM:PF11779` passes; `METACYC:RXN-123` fails |
| `structured_pattern` on env triad | Medium — enforces `label [CURIE]` format; does NOT constrain which prefix | `forest biome [ENVO:01000174]` passes; `forest biome` fails |
| Scoping comments on prefixes | Advisory only — no enforcement | Nothing stops using NCIT outside its documented scope |
| `id_prefixes` on classes | Medium — some validators check this; not universally enforced | `OrthologyGroup` constrains identifiers to its declared prefixes |
| OBO Foundry preference | Advisory only — no automated check | Anything with a declared prefix compiles |

---

## Where ontology terms appear

Different placement contexts have different implications:

| Placement | Purpose | Resolution required | Example |
|---|---|---|---|
| `meaning:` on permissible value | Canonical semantic identity of a PV | Yes — must resolve to an IRI | `meaning: OBI:0000366` |
| `class_uri:` / `slot_uri:` | Schema element identity in RDF/OWL | Yes | `class_uri: OBI:0000011` |
| `exact_mappings:` | This element IS that term | Yes (for OWL generation) | `exact_mappings: - TAXRANK:0000006` |
| `close_mappings:` / `related_mappings:` / `broad_mappings:` / `narrow_mappings:` | Looser alignment, informative | Yes (for OWL) | `close_mappings: - NCIT:C16551` |
| `id_prefixes:` on a class | What CURIE prefixes valid instances may use | Advisory/conditional | `id_prefixes: - PR` |
| Value in a CURIE-typed slot (data) | Instance identifier | String pattern only | `type: ENVO:00002030` |
| Free-text description or annotation | Documentation only | No — just a string | `Expected_value: FMA or UBERON` |

---

## NMDC-specific ontology usage notes

### env triad (`env_broad_scale`, `env_local_scale`, `env_medium`)

MIxS slots with the strongest documented ontology guidance. Descriptions
mandate ENVO subclasses and explicitly accept UBERON and PO for
host-associated or plant-associated samples. The `structured_pattern`
enforces `label [CURIE]` format but does not constrain the prefix.

Related: the data portal's `envo.py` ingest loads terms from ENVO, BFO, GO,
UBERON, and PO into a shared `envo_term` table for faceted search — the
"envo" name is historical.

### Functional annotations (`has_function`)

The most strictly enforced ontology constraint in the schema. A regex pattern
explicitly lists the 15 permitted prefixes. This is the model for how
enforcement *could* work elsewhere.

### PlannedProcess and OBI

`OBI:0000011` (planned process) is used as the `class_uri` for
`PlannedProcess` but is deprecated in OBI; the recommended replacement is
`COB:0000035`. COB is not yet declared in the schema. See [#2843](https://github.com/microbiomedata/nmdc-schema/issues/2843).

---

## Active work on ontology alignment

The following open issues and PRs are doing systematic inventory and discovery
work. They are landscape surveys, not policy decisions.

| Issue/PR | What it does | Policy dependency |
|---|---|---|
| [#2906](https://github.com/microbiomedata/nmdc-schema/issues/2906) | Audits all OBI, PROV, BFO, COB references | None — pure inventory |
| [#2907](https://github.com/microbiomedata/nmdc-schema/issues/2907) / [PR #2909](https://github.com/microbiomedata/nmdc-schema/pull/2909) | OLS4 embeddings search over all 2,298 schema elements | None — data collection |
| [#2908](https://github.com/microbiomedata/nmdc-schema/issues/2908) / [PR #2910](https://github.com/microbiomedata/nmdc-schema/pull/2910) | LinkML-store comparison backend | None — data collection |
| [#2915](https://github.com/microbiomedata/nmdc-schema/issues/2915) / [PR #2916](https://github.com/microbiomedata/nmdc-schema/pull/2916) | Registry counts (OLS, BioPortal, OBO Foundry, semantic-sql) | None — data collection |
| [#2912](https://github.com/microbiomedata/nmdc-schema/issues/2912) | Ground MS/chromatography enums in OBI | **Needs policy** — which ontologies are in scope for this domain? |
| [#2913](https://github.com/microbiomedata/nmdc-schema/issues/2913) | OWL axiom decomposition for refinement | **Needs policy** — which ontologies are worth decomposing? |
| [#2917](https://github.com/microbiomedata/nmdc-schema/issues/2917) | Filter short/generic PV labels from embeddings | **Needs policy** — which ontologies should PVs even align to? |
| [#2918](https://github.com/microbiomedata/nmdc-schema/issues/2918) | Property-oriented retrieval for property_like slots | **Needs policy** — should property-like slots map to ontology properties? |
| [#2843](https://github.com/microbiomedata/nmdc-schema/issues/2843) | Migrate PlannedProcess from OBI to COB | None — follows OBI deprecation notice |

---

## Open questions for a future policy

The following questions are unresolved. They need input from schema maintainers
and the broader NMDC team before the grounding work above can be completed
in a principled way.

1. **Criteria for adding a new ontology.** Is OBO Foundry membership required?
   What about OBO-adjacent ontologies (MS, EFO, GENEPIO)? Should OBO Dashboard
   score be a factor?

2. **Scope declaration requirement.** Should every prefix have a documented
   scope (as some already do via inline comments)? Where should that live —
   inline comments, this document, or a machine-readable registry?

3. **SNOMED and NCIT policy.** These dominate OLS4 results (12K and 7K rows
   respectively) but have different licensing and governance than OBO. Are they
   acceptable for `meaning:` values? For `close_mappings:`? For data values?

4. **Mapping predicate standards.** When is a match `exact_mappings` vs
   `close_mappings` vs just `meaning:`? What level of review is required?

5. **Property-like slot alignment.** 302 of 851 NMDC slots have scalar ranges
   and should arguably align to ontology *properties*, not classes. Is that
   a goal? Which property ontologies are in scope?

6. **Enforcement ambition.** The `has_function` regex is the only hard
   enforcement. Should other high-priority fields (e.g. env triad, biosample
   type) have similar pattern enforcement? At what maintenance cost?

7. **Placeholder prefix retirement.** The `example.org` prefixes are known
   technical debt. What is the path to replacing them with real IRIs?

8. **Governance process.** Who approves adding a new prefix or changing a
   scoping comment? Is this a schema PR with maintainer review, or does it
   need broader sign-off?
