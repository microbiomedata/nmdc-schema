# Database example diagrams

`src/scripts/database_to_diagram.py` is the shared generator for NMDC Database
instances. It validates YAML or JSON, discovers relationships from the source
schema, and writes Mermaid. All example SVGs are rendered from those Mermaid
files by the same rule in `makefiles/diagrams.Makefile`.

This complements the schema class/collection diagrams: each node here represents
a record or an identified object actually present in an example, rather than a
class or collection that the schema defines.

## Existing tools and choice of approach

Several established tools cover parts of this task:

| Tool | Coverage and fit |
| --- | --- |
| [LinkML diagram generators](https://linkml.io/linkml/cli/generate) | Generate class/ER diagrams from a schema. Useful alongside these instance diagrams. |
| [linkml-renderer](https://github.com/linkml/linkml-renderer) | The closest prior art: LinkML instance data to HTML, Markdown and Mermaid. The project describes itself as experimental. |
| [PlantUML JSON](https://plantuml.com/json) and [YAML](https://plantuml.com/yaml), [JSON Crack](https://github.com/AykutSarac/jsoncrack.com) | Visualize document structure. Turning an NMDC identifier value into an edge to another collection record still requires interpreting the schema. |
| [LinkML RDF conversion](https://linkml.io/linkml/data/rdf) with [RDFLib rdf2dot](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.tools.rdf2dot/) | An existing route from instance data to a semantic graph and Graphviz. A useful alternative for RDF-oriented work; the example-specific label selection and workflow presentation still need configuration or code. |
| [Cytoscape.js](https://js.cytoscape.org/) | An established interactive graph renderer. It takes explicit nodes and edges; the schema-aware extraction step would still be needed. |

On 2026-09-16, we exercised `linkml-renderer` at commit
[`867cb5c`](https://github.com/linkml/linkml-renderer/tree/867cb5c75a03bb82f6d4d3f9185be858450b6b87)
using its `MermaidRenderer.render` API, the source NMDC schema, and the SIP and
leaf-clip examples. It generated Mermaid, but the SIP output did not draw
`has_input`, `has_output` or `in_manifest` edges. The leaf-clip output likewise
omitted the `expected_organism` edge. Its traversal draws inline containment;
non-inline identifier references remain attributes. This matches the inspected
[renderer](https://github.com/linkml/linkml-renderer/blob/867cb5c75a03bb82f6d4d3f9185be858450b6b87/src/linkml_renderer/renderers/mermaid_renderer.py)
and [object-context logic](https://github.com/linkml/linkml-renderer/blob/867cb5c75a03bb82f6d4d3f9185be858450b6b87/src/linkml_renderer/paths/context.py).

We therefore retain a focused NMDC adapter: LinkML validates and interprets the
schema, shared `refscan` helpers discover reference ranges, and Mermaid/ELK
handles drawing and layout. The adapter adds reference resolution, presentation
choices and reproducible repository outputs. It is not a general replacement for
LinkML rendering tools. Support for reference edges in `linkml-renderer` would
make it worth reevaluating as an upstream implementation.

## Commands

Use the repository's Poetry environment with development dependencies installed
(`poetry install --with dev,deps`) and Node.js/npm on PATH. The Makefile pins
Mermaid CLI; its first use downloads the renderer and a headless browser.
Graphviz and a full schema build are not required.

```sh
make sip-diagram       # SIP example
make example-diagrams # All six Database example diagrams
make diagrams         # Also render the hand-authored class hierarchy diagram
```

For any other valid Database example:

```sh
make database-diagram \
  DATABASE=src/data/valid/Database-leaf-clip.yaml \
  DIAGRAM_OPTIONS="--allow-external --view workflow --direction LR"
```

This writes `local/Database-leaf-clip.mmd` and `.svg`. To save another diagram for
review and commit, set `DIAGRAM_OUTPUT=src/docs/images/my-example` (no extension).
The target does not commit or push files. `MERMAID_CLI` can be overridden to use
an already installed renderer; use the pinned version for consistent output.

To generate only Mermaid, without Node.js or a browser:

```sh
poetry run python src/scripts/database_to_diagram.py \
  src/data/valid/Database-sip-lifecycle.yaml local/sip.mmd --view workflow
```

Append `--check` to compare with an existing Mermaid file without writing it.
The command fails if the file is absent or stale. Input validation always runs
before output is written. Existing output is preserved on a validation failure.

## Relationship and workflow views

The default `--view relationships` preserves the direction of each recorded
property: a process points to a sample through `has_input`.

`--view workflow` reverses `has_input` and `was_generated_by` to show material/data
moving forward. Their labels explicitly name the inverse relationship:
`input to (inverse has_input)` and `generates (inverse was_generated_by)`.
All other relationships retain their recorded direction. Multiple labels between
the same nodes are combined, so the graph can show both `has_output` and the
inverse of `was_generated_by` without overlapping arrows.

Solid arrows represent inputs, outputs and generation; dashed arrows represent
other relationships. Node colors distinguish material entities, processes,
DataObjects, Manifests, ontology objects, other records and external references.
External nodes additionally have dashed outlines. `--direction TB` (default)
and `--direction LR` control layout independently of edge meaning.

## Validation and graph coverage

The generator reads `src/schema/nmdc.yaml` and its imports, materializes patterns
in memory, and runs both closed JSON Schema validation and the NMDC unit plugin.
It never relies on the packaged schema artifacts being up to date. `--schema`
can select another NMDC schema source.

Collection membership, class URIs and effective slot ranges are discovered with
the same `refscan` helpers used by the reference checker. There is no fixed list
of reference slots. The graph includes:

- Every collection record, including isolated records and annotation records
  without identifiers. Anonymous collection records use their source path as
  their graph identity and label.
- References in class-ranged slots, including `expected_organism`, `part_of`,
  `associated_studies`, `in_manifest` and process inputs/outputs. A URL or CURIE
  in an ordinary scalar slot is not inferred to be a relationship.
- Identified inline objects, including taxa under `classified_as` and ontology
  terms nested in wrappers. Edge paths such as `host_taxid.term` preserve the
  wrapper relationship. List indices distinguish individual embedded entries.

Anonymous wrapper objects are traversed rather than drawn as extra boxes.
Occurrences of an identified inline object have separate graph identities;
different annotations on the same ontology ID are not silently combined.
Duplicate IDs among collection records are rejected.

By default, a reference to a missing collection record is an error. For examples
that deliberately omit supporting records, `--allow-external` retains an explicit
external node. This option does not relax schema or unit validation. The five
organism/isolate examples use it because their Study records are not included.
The SIP lifecycle remains self-contained and does not use it. Links to resources
whose classes have no Database collection can be represented as external IDs.

This checks submitted metadata and reference consistency; it does not infer
missing laboratory steps or establish experimental correctness. Large examples
can yield correspondingly large diagrams.

## Metadata in node labels

The default label contains the class, name and identifier. Repeat `--label-slot`
to add relevant scalar or quantity values:

```sh
poetry run python src/scripts/database_to_diagram.py \
  src/data/valid/Database-sip-lifecycle.yaml local/sip.mmd --view workflow \
  --label-slot gradient_position --label-slot gradient_pos_density \
  --label-slot isotopolog_additions.isotope
```

Dotted paths descend into anonymous objects and lists; displayed indices keep
different additions distinguishable. Quantities include their units, and
interval quantities include both bounds. Label selection changes presentation,
not which relationships are discovered or validated.

## Maintained example gallery

Edit the Database YAML and rerun Make; do not edit generated Mermaid or SVG
files. The recipes select the source example and presentation options only.
Each invocation rechecks the current schema, while preserving Mermaid timestamps
when content is unchanged. Renderer/configuration changes also trigger SVG
regeneration.

| Example | Source under `src/data/valid/` | Diagram |
| --- | --- | --- |
| Paired DNA-SIP lifecycle | `Database-sip-lifecycle.yaml` | [SVG](images/sip-lifecycle.svg) |
| Environmental isolation | `Database-isolate-from-soil-workflow.yaml` | [SVG](images/use-case-1-environmental-isolation.svg) |
| Culture collection | `Database-isolate-from-culture-collection.yaml` | [SVG](images/use-case-2-culture-collection.svg) |
| Leaf clip | `Database-leaf-clip.yaml` | [SVG](images/use-case-3-leaf-clip.svg) |
| Mushroom cap | `Database-mushroom-cap.yaml` | [SVG](images/use-case-4-mushroom-cap.svg) |
| Viral isolate and host | `Database-viral-isolate-with-host.yaml` | [SVG](images/use-case-5-viral-isolate-with-host.svg) |

`poetry run pytest tests/test_database_to_diagram.py -q` exercises all valid
Database fixtures and checks the saved gallery's Mermaid sources, together with
validation failures, external references, taxonomy links and arrow semantics.
