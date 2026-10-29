# Understanding the NMDC Schema

The nmdc-schema is a framework for describing multi-omics microbiome experiments and the data they produce.  We aim 
to answer questions like:

- What samples were included?
- Where were they gathered?
- What qualities do they have?
- How were they prepared, so that they would be suitable for sequencing, LC-MS proteomics, metabolomics, etc?
- How were the results of those analyses interpreted?

All metadata gathered and stored by the NMDC community must validate against the NMDC Schema.

## The NMDC Schema is expressed in the [LinkML](https://linkml.github.io/linkml/) modeling language.

LinkML uses structures like classes, slots (for relationships and properties), types and enumerations to create a 
blueprint of the NMDC data. The schema is used to define the structure of the data, and to ensure that the data is
consistent and interoperable. The schema is expressed in a human-readable format, and with the help of LinkML tooling, 
can be generated in multiple formats, including JSONSchema (used to support validation on ingest to NMDC), 
YAML (for ease of editing), and OWL. LinkML schemas generally make good use of terminology and concepts already modeled 
in external, trusted knowledge centers, especially [ontologies](https://en.wikipedia.org/wiki/Ontology_(information_science)), 
and especially those from the [OBO Foundry](https://obofoundry.org/). 

Reuse of existing terminologies and knowledge can be found in several places in the NMDC schema, including the use of
the [MIxS](https://gensc.org/mixs/) schema, the [EnvO](https://environmentontology.org/) ontology, and the 
[CHEBI](https://www.ebi.ac.uk/chebi/) ontology.  In addition, the NMDC schema elements like slots and classes are
annotated with mappings to these external resources, as described in
[Mapping schema elements to external terms](#mapping-schema-elements-to-external-terms).

For example: 
```yaml
  doi_value:
    description: >-
      A digital object identifier, which is intended to persistently identify some resource on the web.
    required: true
    aliases:
      - DOI
      - digital object identifier
    range: uriorcurie
    pattern: '^doi:10\.\d{2,9}/.*$'
    examples:
      - value: doi:10.46936/10.25585/60000880
        description: The DOI links to an electronic document.
    close_mappings:
      - OBI:0002110
      - edam.data:1188
```

## Asserting element identifiers in the schema with URIs and CURIEs

One consequence of this semantic/linked data orientation is that all schema elements are identified by a URI,
most often in the compact CURIe form: a prefix and a local identifier.
Even if a class isn't decorated with a `class_uri` annotation, it will always have a key (in a JSON, YAML or Python Obj sense), 
which is sometimes reiterated as the `name`. In that case, the class' URI will be `<prefix>:<key>`. 
LinkML schemas should have default prefix assertions, but any element can use a different prefix, as long as an expansion is provided.

## Prefixes in LinkML **schemas**

Prefixes used in a LinkML must be associated with an expansion in the schema (which may include imported modules).
Ideally, the expanded URI should be web resolvable, but that is not required.
The prefixes can be expanded to base URIs owned by a particular resource, or they can be
expanded to base URIs owned by some resolving service, like the bioregistry.

## Mapping schema elements to external terms

A mapping relates a schema element to a term in another vocabulary without making that term the element's
identity. Mappings are one of the most compact ways to say what an element means, so contributors are encouraged
to add them. This section is the NMDC Schema's single statement of how to use them.

### Mappings and the other metaslots that hold external terms

Four other metaslots also hold external terms, and each does a different job:

- `class_uri` and `slot_uri` give the element its own identity in RDF and OWL. Use them only when the element and
  the external term are the same thing.
- `meaning` names the term that a permissible value stands for.
- `see_also` links to pages for human readers, such as specifications and GitHub issues. An ontology CURIE
  belongs in a mapping, not in `see_also`.

### The mapping metaslots

Each LinkML mapping metaslot becomes one SKOS predicate in the generated OWL
([linkml-model mappings.yaml](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/mappings.yaml),
[W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)). In the table, X is the schema element and Y is the
external term.

| Metaslot | SKOS predicate | `X <metaslot> Y` means | How the NMDC Schema uses it |
|---|---|---|---|
| `exact_mappings` | `skos:exactMatch` | X and Y are the same concept. | For identity between elements of the same kind, such as `Biosample` and `OBI:0000747`, or `title` and `dcterms:title`. |
| `close_mappings` | `skos:closeMatch` | X and Y are close enough to treat as the same in some applications. | For near-identity, such as `Organization` and `dcm:Organization`. |
| `related_mappings` | `skos:relatedMatch` | X and Y are associated, and neither subsumes the other. | For adjacent terms, such as the assay that produces a value or the rank of a taxon name. |
| `broad_mappings` | `skos:broadMatch` | Y is broader than X. | For subsumption between elements of the same kind, such as `Study` and `prov:Activity`. |
| `narrow_mappings` | `skos:narrowMatch` | Y is narrower than X. | For subsumption between elements of the same kind, such as `FunctionalAnnotation` and `biolink:GeneToGoTermAssociation`. |
| `mappings` | `skos:mappingRelation` | X and Y are related in an unstated way. | Only for the existing schema.org, QUDT and PROV alignments, such as `latitude` and `schema:latitude`. Use a typed metaslot for anything new. |

The direction of `broad_mappings` and `narrow_mappings` is easy to get backwards. `skos:broadMatch` is a
sub-property of `skos:broader`, and the SKOS Reference says "`A skos:broader B` asserts that B, the object, is a
broader concept than A". So `X broad_mappings Y` says that Y subsumes X, the way "egg-laying animal" subsumes
"platypus".

### Which kinds of element can map to which

A class maps to a class, and a permissible value maps to a class or to a value in another vocabulary. A slot maps
to a property where the other vocabulary has one.

Many ontologies model a data field only as a class, for example GENEPIO fields, OBI data items, PATO qualities,
and MS and TAXRANK terms. When such a class is the best match for a slot, put it in `close_mappings` or
`related_mappings`. `exact_mappings`, `broad_mappings` and `narrow_mappings` would assert identity or subsumption
between a property and a class, which can't hold, and generic `mappings` is kept for the schema.org, QUDT and PROV
alignments.

To choose between the two, ask whether each value of the slot is an instance of what the class describes. If it
is, use `close_mappings`. `number_of_contig` holds a count of contigs, and `GENEPIO:0000093` (contig count) describes
exactly that. If it isn't, use `related_mappings`. `gtdbtk_species` holds a species name,
while `TAXRANK:0000006` is the rank "species" itself.

### Permissible values: `meaning` first

Put the term a permissible value stands for in `meaning`, and use mapping metaslots only for further terms. For
example, `acetic_acid` in `ChemicalEntityEnum` has `meaning: CHEBI:15366` (acetic acid) and
`related_mappings: CHEBI:30089` (acetate). Some older values put their only term in `exact_mappings` and have no
`meaning`, such as the values of `MassAnalyzerEnum`. New values should not follow that pattern.

### Choosing and checking a term

Use `exact_mappings` only when you are sure the two are the same. When the external term is an assay, method or
measurement next to the element rather than the element itself, use `related_mappings`. For example, map a gene
or a process to the sequencing assay that reads it or runs it with `related_mappings`.

An embeddings search, such as the OLS4 `llm_search`, is a good way to find candidates, but a high score is only a
lead. Confirm that the CURIE resolves to the intended term, and read the term's parents, children and axioms in
the [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols4/) before using it.

Prefer prefixes the schema already defines. Before adding a new prefix, assess the whole ontology, not only the
term you want. For an OBO Foundry ontology, the
[OBO Foundry Dashboard](http://dashboard.obofoundry.org/dashboard/index.html) is a good place to start.

## Asserting identifiers in LinkML data

Generally speaking, the smallest atom of LinkML data is an instance of one class. LinkML slots take values, 
but always in the context of some class (on the right hand side). LinkML data files are frequently collections 
of instances of one or more classes. The is no requirement that these classes provide a slot whose value
uniquely identifies the instances, but LinkML provides a mechanism that is broadly followed:
one slot available in each class is annotated with `identifier: true`. (Or at least, that's what it would look like
in a YAML serialization.) That means that the slot is required in all instances of the class, 
and that any collection of instances from that class must have unique values in that slot. 
It is also typical to say that the range of the is type `uriorcurie`.

## Mentioning identifiers in LinkML data

A common pattern in the nmdc-schema is asserting that some identifiable process has inputs and outputs. 

```yaml
pooling_set:
  - id: pooling:1
    inputs:
      - biosample:1
      - biosample:2
      - biosample:3
  - id: pooling:2
    inputs:
      - biosample:4
      - biosample:5
      - biosample:6
```

Here we have declared the existence of two pooling processes. A CURIe identifier is asserted for both of them,
and three inputs are mentioned for each. The example CURIes above don't necessarily follow any nmdc-schema
identifier pattern rules. If these were real CURIes, then the pooling and biosample prefixes would have to be
defined in the schema files.

In this case, let's assume definitions for the biosample inputs should be defined elsewhere in an NMDC data set.
Cases in which biosamples are mentioned without being defined would be considered violations of the referential integrity.
Schema validation does not detect them. See
[Validating a slot that mentions another class's id](#validating-a-slot-that-mentions-another-classs-id) below for
what is checked, what is not, and which tools close the gap.

Another pattern is saying that something defined within a NMDC data set is equivalent to something defined elsewhere.

```yaml
biosample_set:
    - id: biosample:1
      gold_biosample_identifiers:
        - gold:1
        - gold:2
```

In this case, the gold prefix must be defined in the schema. When expanded to URIs via the prefix definitions,
these gold_biosample_identifiers would all be web-resolvable.

## Constraining mentioned identifiers

We can limit the values that go into any slot by using a `pattern` constraint. We can also use the `id_prefixes` constraint
to limit the prefixes that are used in whatever slot has been declared to be the identifier of a class.

Constraints written in a class's `slot_usage` do cascade to subclasses through `is_a`, so there is no need to
restate an inherited value defensively. An earlier version of this page described a belt-and-suspenders practice of
re-declaring the `uriorcurie` range for that reason. No class does that, and restating an inherited value is now
treated as something to remove: `src/scripts/report_redundant_slot_usage.py` finds them and
`tests/test_no_redundant_slot_usage.py` fails CI when a new one appears.

Restating costs something real. A class that repeats a value it already inherits stops tracking the parent, so a
later edit upstream silently does not reach it.

One inheritance path does drop values, and it is not this one: a *slot* that inherits from another slot through
slot-level `is_a` loses a falsy value such as `minimum_value: 0`. That is [linkml issue 3845](https://github.com/linkml/linkml/issues/3845)
and it does not affect class `slot_usage`.

All prefixes used in the `id_prefixes` constraint must be defined in the schema. 
We should have a standing practice of reflecting on the declared `id_prefixes`, and removing prefixes that haven't been used yet
and are not likely to eer be used.

Maintenance of the prefix portions of a `pattern` will generally require more manual checking. We shouldn't be constraining
the values of slots to use a prefix that isn't declared, but no checks are automatically applied.

## Validating a slot that mentions another class's id

When a slot's range is a class that is not inlined, the value in the data is the `id` of an instance of that class.
Two different things could be checked about that value, and only one of them is enforced by the schema.

**The shape of the id is enforced by the schema.** A `structured_pattern` on the slot, or in a class's `slot_usage`,
constrains the value to the id pattern of the intended class. For example, the `associated_studies` slot in
`src/schema/basic_classes.yaml`:

```yaml
associated_studies:
  range: Study
  multivalued: true
  structured_pattern:
    syntax: "{id_nmdc_prefix}:sty-{id_shoulder}-{id_blade}"
    interpolated: true
```

With linkml-runtime 1.12 or later, `SchemaView.induced_slot()` fills in the settings and turns this into
`^(?:(nmdc):sty-([0-9][a-z]{0,6}[0-9])-([A-Za-z0-9]{1,}))$`, so `associated_studies: [xyz]` fails whether you
validate against the source schema or against `nmdc_schema/nmdc_materialized_patterns.yaml`. linkml adds the `^(?:` and
`)$` itself because `partial_match` is not set, so the `syntax` leaves out `^` and `$`
(https://github.com/microbiomedata/nmdc-schema/issues/3539). With an older linkml-runtime, only the materialized
artifact carries the pattern. This is why so many `slot_usage` blocks carry a `structured_pattern`: it is the only
in-schema guard against pointing a slot at an id of the wrong class.

linkml 1.12 deprecates the `--materialize-patterns` option. The Makefile still passes it when it builds
`nmdc_schema/nmdc_materialized_patterns.yaml`. Without it that file holds 42 `pattern` values instead of 356, and tools
that read the file with linkml-runtime older than 1.12, such as submission-schema's build, would not see the rest.

**The existence of the referent is not checked by the schema.** Schema validation is per-document: a value that
matches the pattern but names a record that does not exist will pass. Nothing in LinkML or the generated JSON Schema
can see the rest of the database.

That check happens in `nmdc-runtime`, at submission time. `/metadata/json:submit` and the workflow-execution
endpoints call `validate_json(..., check_inter_document_references=True)`, which uses
[refscan](https://github.com/microbiomedata/refscan) to scan each incoming document's outgoing references and
rejects the payload with HTTP 422 if a target is missing. A reference is satisfied if the target already exists in
the database **or** appears in the same payload, so a submission that creates a study and its biosamples together is
accepted while a dangling reference is not.

The same check also runs outside the API:

- `make check-references` (`src/scripts/check_references.py`) reports dangling references in this repo's own data
  files.
- `refscan` run directly scans the production database, and `refgraph` draws the reference graph it derives.

Runtime behavior verified 2026-08-13 against `nmdc_runtime/api/endpoints/metadata.py`,
`nmdc_runtime/api/endpoints/workflows.py`, and `nmdc_runtime/api/db/mongo.py`. That is a different repository and
can drift, so re-check those files rather than trusting this paragraph if the answer matters.

Two consequences worth knowing when you write a `slot_usage`. A `structured_pattern` whose `syntax` contains `|` is
asserting one pattern per alternative, so `{id_nmdc_prefix}:(bsm|procsm)-...` accepts both `Biosample` and
`ProcessedSample` ids. And an `any_of` range widens rather than narrows: LinkML reads it as a union with the global
range, so `any_of: [Biosample, ProcessedSample]` on a slot whose global range is `NamedThing` does not exclude other
`NamedThing` subclasses.

The fuller discussion of these limitations, including why pattern-plus-class ranges complicate the OWL and RDF
artifacts, is in
[the v10 to v11 retrospective](v10-vs-v11-retrospective.md#challenges-with-the-use-of-structured_patterns-in-slot_usages-for-approximating-referential-integrity-etc).

## Using URIs supports scoping and self-documentation

Any class could use any slot with any range to "link to" something external. A `Person` could have a `place_of_birth` slot,
and that could take unconstrained string or enumerated values like "Switzerland". But that doesn't provide much support for
people looking up more information about the place_of_birth. You could create `wikidata_place_of_birth` and 
`dbpedia_place_of_birth` slots and add annotations to the slot to aid in external lookups, but that isn't a good practice if
supporting several external targets. A better practice is to have one `place_of_birth` slot, with the `uriorcuire` range.
Then users can provide values like `<http://www.wikidata.org/entity/Q39>` or `<http://dbpedia.org/resource/Switzerland>`.
Then there is no ambiguity about the target of the link. 

## Using CURIes makes things more compact and readable

If the schema contains prefix definitions like 
`wd: <http://www.wikidata.org/entity/>` and `dbpedia: <http://dbpedia.org/resource/>`, then the values can be written as 
`wd:Q39` and `dbpedia:Switzerland`. This is more compact and readable, but it requires that the prefixes be defined in the schema.
Then, more constraint can be imposed with a pattern on the `place_of_birth` slot like '^(wd|dbpedia):.+$'

## Where to find a report of NMDC prefixes
* project/jsonld/nmdc.context.jsonld (autogenerated as the jsonldcontext output from `make gen-project`)
* assets/misc/data_prefix_expansions.context.jsonld (curated based on prefixed observed in MongoDB)

----

# PREFIX, id and CURIe notes

* not using `default_curi_maps` any more
  * all prefixes must now be explicit
* prefix definitions have to account for prefixes and base URIs used in the schema and in the data
* look out forthe presence of http://example.org/UNKNOWN/ and "example." in the schema, the data and any SPARQL results
* should prefixes be uppercase or lowercase?
  * it must be consistent. look for precedent
* bogus emsl UUID prefixes handled with `--emsl-biosample-uuid-replacement` in `anyuri-strings-to-iris`
* keep an eye on validation `pattern`s and id_prefixes
* MetaCyc expansion assumes we're talking about metacyc reactions and not genes, compounds etc. The same may hold for other under-qualified prefixes

## see local/lint.log
### use bioregistry, not identifiers.org, BUT

> warning Schema maps prefix 'CHEMBL.COMPOUND' to namespace 'https://bioregistry.io/chembl.compound:' instead of
namespace 'http://identifiers.org/chembl.compound/'  (canonical_prefixes)

>warning Schema maps prefix 'rdf' to namespace 'http://www.w3.org/1999/02/22-rdf-syntax-ns#' instead of using prefix '
RDF'  (canonical_prefixes)
warning Schema maps prefix 'rdfs' to namespace 'http://www.w3.org/2000/01/rdf-schema#' instead of using prefix 'RDFS'  (
canonical_prefixes)

## Typecodes

Not only does NMDC require the use of the `nmdc` prefix in the primary identifier for data instances, 
but we also define a pattern that the local portion of the `id`s must follow. 
For example, an example `id` from the `NamedThing` class is 'nmdc:mgmag-00-x012.1_7_c1'.
The text that comes immediately after the `nmdc` prefix and colon, and before the first hyphen is the typecode, `mgmag` in this case.
Typecodes must correspond 1:1 to a class in the NMDC schema. The typecodes currently in use are available from the
nmdc-runtime API: https://api.microbiomedata.org/nmdcschema/typecodes

Please see [identifiers](identifiers.md) for more information on the minting of identifiers in NMDC directly, and
for more discussion on identifier resolution and harmonization in NMDC.



