"""Exercise validation, schema-derived references, and generated example diagrams."""

from copy import deepcopy
from graphlib import TopologicalSorter
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

from src.scripts.database_to_diagram import DiagramSchema, build_graph, render_graph
from tests import ROOT


@pytest.fixture(scope="module")
def diagram_schema() -> DiagramSchema:
    """Validate directly against source, including SIP classes not yet released."""
    return DiagramSchema()


@pytest.fixture
def lifecycle() -> dict:
    """Load the authored lifecycle used to generate the published diagram."""
    return yaml.safe_load(
        (ROOT / "src/data/valid/Database-sip-lifecycle.yaml").read_text()
    )


def test_lifecycle_provenance_and_manifests(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """Every sequence file traces through preparation to exactly one gradient."""
    nodes, edges = build_graph(lifecycle, schema=diagram_schema)
    parents = {identifier: set() for identifier in nodes}
    for source, target, relation in edges:
        if relation == "has_input":
            parents[source].add(target)
        elif relation == "has_output":
            parents[target].add(source)
    ancestors = {}
    for identifier in TopologicalSorter(parents).static_order():
        ancestors[identifier] = set(parents[identifier])
        for parent in parents[identifier]:
            ancestors[identifier].update(ancestors[parent])
    gradient_members = {}
    for record in lifecycle["data_object_set"]:
        lineage = [nodes[identifier] for identifier in ancestors[record["id"]]]
        classes = [item.class_name for item in lineage]
        for required in (
            "Biosample",
            "IsotopeLabelingProcess",
            "DensityGradientFractionationProcess",
            "LibraryPreparation",
            "NucleotideSequencing",
        ):
            assert classes.count(required) == 1
        assert classes.count("Extraction") == 2
        assert record["was_generated_by"] in ancestors[record["id"]]
        gradient = next(
            item.record["id"]
            for item in lineage
            if item.class_name == "DensityGradientFractionationProcess"
        )
        (manifest,) = record["in_manifest"]
        assert nodes[manifest].record["manifest_category"] == "fractions"
        gradient_members.setdefault(manifest, set()).add(gradient)
    assert len(gradient_members) == 2
    assert all(len(gradients) == 1 for gradients in gradient_members.values())
    assert len(set.union(*gradient_members.values())) == 2


@pytest.mark.parametrize(
    "example",
    sorted((ROOT / "src/data/valid").glob("Database*.yaml")),
    ids=lambda p: p.stem,
)
def test_every_valid_database_example(
    example: Path, diagram_schema: DiagramSchema
) -> None:
    """All existing Database examples, including annotations without IDs, work."""
    database = yaml.safe_load(example.read_text())
    nodes, edges = build_graph(database, allow_external=True, schema=diagram_schema)
    assert nodes
    for records in database.values():
        if isinstance(records, list):
            for record in records:
                if isinstance(record, dict) and "id" in record:
                    assert record["id"] in nodes
    assert all(source in nodes and target in nodes for source, target, _ in edges)
    assert "flowchart TB" in render_graph(nodes, edges)


def test_missing_reference_is_explicit(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """A valid ID alone must not look like a defined sample in a diagram."""
    missing = lifecycle["biosample_set"].pop()["id"]
    with pytest.raises(ValueError, match=missing):
        build_graph(lifecycle, schema=diagram_schema)
    nodes, edges = build_graph(lifecycle, allow_external=True, schema=diagram_schema)
    assert nodes[missing].kind == "external"
    assert "External reference" in render_graph(nodes, edges)


def test_duplicate_identifier_is_rejected(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """Do not silently overwrite conflicting collection records."""
    lifecycle["biosample_set"].append(deepcopy(lifecycle["biosample_set"][0]))
    with pytest.raises(ValueError, match="Duplicate record id"):
        build_graph(lifecycle, schema=diagram_schema)


@pytest.mark.parametrize(
    "defect", ["invalid_id", "unknown_field", "wrong_unit", "invalid_type"]
)
def test_allow_external_does_not_disable_validation(
    lifecycle: dict, diagram_schema: DiagramSchema, defect: str
) -> None:
    """Partial examples still need valid shapes, patterns and storage units."""
    record = lifecycle["material_processing_set"][0]
    if defect == "invalid_id":
        record["id"] = "nmdc:labp-BAD"
    elif defect == "unknown_field":
        record["invented_slot"] = "value"
    elif defect == "wrong_unit":
        record["isotopolog_incu_time"]["has_unit"] = "s"
    else:
        record["type"] = "nmdc:InventedProcess"
    with pytest.raises(ValueError, match="Invalid Database"):
        build_graph(lifecycle, allow_external=True, schema=diagram_schema)


def test_organisms_and_nested_taxa(diagram_schema: DiagramSchema) -> None:
    """The previously empty viral graph includes both host and focal taxa."""
    database = yaml.safe_load(
        (ROOT / "src/data/valid/Database-viral-isolate-with-host.yaml").read_text()
    )
    nodes, edges = build_graph(database, allow_external=True, schema=diagram_schema)
    assert ("nmdc:osm-99-vqkvad", "nmdc:orgn-99-pgw8nq", "expected_organism") in edges
    for identifier, path in [
        ("NCBITaxon:511145", "host_taxid.term"),
        ("NCBITaxon:10665", "classified_as[0]"),
    ]:
        (key,) = [
            key for key, node in nodes.items() if node.record.get("id") == identifier
        ]
        assert any(target == key and relation == path for _, target, relation in edges)
        assert nodes[key].kind == "ontology"


def test_schema_reference_discovery_and_isolated_records(
    diagram_schema: DiagramSchema,
) -> None:
    """Study.part_of is discovered without a slot list; a lone study is retained."""
    study = {
        "id": "nmdc:sty-99-first",
        "type": "nmdc:Study",
        "study_category": "research_study",
    }
    other = {**study, "id": "nmdc:sty-99-second", "part_of": [study["id"]]}
    nodes, edges = build_graph({"study_set": [study, other]}, schema=diagram_schema)
    assert (other["id"], study["id"], "part_of") in edges
    nodes, edges = build_graph({"study_set": [study]}, schema=diagram_schema)
    assert list(nodes) == [study["id"]]
    assert edges == []


def test_repeated_inline_ids_remain_distinct(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """Do not merge differently annotated occurrences of the same ontology ID."""
    biosample = lifecycle["biosample_set"][0]
    biosample["env_local_scale"] = deepcopy(biosample["env_broad_scale"])
    biosample["env_local_scale"]["term"]["name"] = "Different submitted label"
    nodes, _ = build_graph(lifecycle, schema=diagram_schema)
    terms = [
        node for node in nodes.values() if node.record.get("id") == "ENVO:00002030"
    ]
    assert len(terms) == 2
    assert (
        sum(node.record.get("name") == "Different submitted label" for node in terms)
        == 1
    )


def test_directions_and_escaped_labels(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """Relationship arrows preserve predicates; workflow arrows name inverses."""
    lifecycle["biosample_set"][0]["name"] = 'sample "quoted" <tag> [bracket]'
    nodes, edges = build_graph(lifecycle, schema=diagram_schema)
    relationships = render_graph(nodes, edges)
    workflow = render_graph(nodes, edges, view="workflow")
    names = {identifier: f"n{index}" for index, identifier in enumerate(nodes)}
    source, target, _ = next(edge for edge in edges if edge[2] == "has_input")
    assert f'{names[source]} -->|"has_input"| {names[target]}' in relationships
    assert (
        f'{names[target]} -->|"input to (inverse has_input)"| {names[source]}'
        in workflow
    )
    assert "#34;quoted#34;" in relationships
    assert "<tag>" not in relationships
    assert relationships.count('-.->|"in_manifest"|') == 6
    assert "has_output / generates" not in relationships
    assert "generates (inverse was_generated_by) / has_output" in workflow


def test_generic_metadata_paths_keep_isotope_pairing(
    lifecycle: dict, diagram_schema: DiagramSchema
) -> None:
    """List positions stay explicit when callers select nested label metadata."""
    nodes, edges = build_graph(lifecycle, schema=diagram_schema)
    diagram = render_graph(
        nodes,
        edges,
        label_slots=("isotopolog_additions.isotope", "gradient_pos_density"),
    )
    assert "isotopolog_additions[0].isotope: 13C" in diagram
    assert "gradient_pos_density: 1.735 g/mL" in diagram


def test_cli_invalid_input_preserves_existing_output(tmp_path: Path) -> None:
    """Validation must finish before an existing diagram can be overwritten."""
    database = tmp_path / "invalid.yaml"
    database.write_text('study_set: [{type: "nmdc:Study"}]')
    output = tmp_path / "diagram.mmd"
    output.write_text("existing diagram")
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "src/scripts/database_to_diagram.py"),
            str(database),
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    assert "Invalid Database" in result.stderr
    assert output.read_text() == "existing diagram"


SIP_LABELS = (
    "gradient_position",
    "gradient_pos_density",
    "gradient_pos_rel_am",
    "manifest_category",
    "isotopolog_additions.isotope",
    "isotopolog_additions.isotopolog_label",
)
GALLERY = [
    ("sip-lifecycle", "sip-lifecycle", "TB", False, SIP_LABELS),
    (
        "use-case-1-environmental-isolation",
        "isolate-from-soil-workflow",
        "LR",
        True,
        (),
    ),
    (
        "use-case-2-culture-collection",
        "isolate-from-culture-collection",
        "LR",
        True,
        (),
    ),
    ("use-case-3-leaf-clip", "leaf-clip", "LR", True, ()),
    ("use-case-4-mushroom-cap", "mushroom-cap", "LR", True, ()),
    (
        "use-case-5-viral-isolate-with-host",
        "viral-isolate-with-host",
        "LR",
        True,
        ("host_genus", "host_species", "host_strain"),
    ),
]


@pytest.mark.parametrize("output,example,direction,allow_external,label_slots", GALLERY)
def test_gallery_mermaid_matches_its_database(
    output: str,
    example: str,
    direction: str,
    allow_external: bool,
    label_slots: tuple[str, ...],
    diagram_schema: DiagramSchema,
) -> None:
    """CI catches diagrams that drift from the YAML or the shared generator."""
    source = f"src/data/valid/Database-{example}.yaml"
    database = yaml.safe_load((ROOT / source).read_text())
    nodes, edges = build_graph(database, allow_external, diagram_schema)
    expected = render_graph(nodes, edges, direction, "workflow", label_slots, source)
    saved = ROOT / f"src/docs/images/{output}.mmd"
    assert saved.read_text() == expected, "Regenerate with make example-diagrams"


def test_check_mode_and_unchanged_output_timestamp(tmp_path: Path) -> None:
    """Check mode detects stale diagrams and repeat writes avoid rerendering."""
    database = tmp_path / "study.yaml"
    database.write_text(
        'study_set: [{id: "nmdc:sty-99-example", type: "nmdc:Study", study_category: research_study}]'
    )
    output = tmp_path / "study.mmd"
    command = [
        sys.executable,
        str(ROOT / "src/scripts/database_to_diagram.py"),
        str(database),
        str(output),
    ]
    subprocess.run(command, check=True, capture_output=True)
    timestamp = output.stat().st_mtime_ns
    subprocess.run(command, check=True, capture_output=True)
    assert output.stat().st_mtime_ns == timestamp
    subprocess.run(command + ["--check"], check=True, capture_output=True)
    output.write_text("stale diagram")
    result = subprocess.run(
        command + ["--check"], text=True, capture_output=True, check=False
    )
    assert result.returncode != 0
    assert "out of date" in result.stderr
    assert output.read_text() == "stale diagram"


def test_reference_checker_accepts_shared_refscan_catalog(
    diagram_schema: DiagramSchema,
) -> None:
    """The existing checker consumes refscan's catalog after removing its copy."""
    from src.scripts.check_references import build_reference_lookup, identify_references

    references = identify_references(diagram_schema.view, diagram_schema.collections)
    lookup = build_reference_lookup(references)
    assert lookup[("organism_sample_set", "OrganismSample", "expected_organism")] == {
        "organism_set"
    }
    assert lookup[("data_object_set", "DataObject", "in_manifest")] == {"manifest_set"}
