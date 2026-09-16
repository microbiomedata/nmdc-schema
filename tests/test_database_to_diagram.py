"""Exercise instance provenance rather than just validating record shapes."""

from copy import deepcopy
from graphlib import TopologicalSorter

import pytest
import yaml

from src.scripts.database_to_diagram import build_graph, render_graph
from tests import ROOT


@pytest.fixture
def lifecycle() -> dict:
    """Load the authored lifecycle used to generate the published diagram."""
    return yaml.safe_load(
        (ROOT / "src/data/valid/Database-sip-lifecycle.yaml").read_text()
    )


def test_lifecycle_provenance_and_manifests(lifecycle: dict) -> None:
    """Every sequence file traces through preparation to exactly one gradient."""
    nodes, edges = build_graph(lifecycle)
    parents = {identifier: set() for identifier in nodes}
    for source, target, relation in edges:
        if relation != "in_manifest":
            parents[target].add(source)
    ancestors = {}
    for identifier in TopologicalSorter(parents).static_order():
        ancestors[identifier] = set(parents[identifier])
        for parent in parents[identifier]:
            ancestors[identifier].update(ancestors[parent])

    gradient_members = {}
    for record in lifecycle["data_object_set"]:
        lineage = [nodes[identifier] for identifier in ancestors[record["id"]]]
        classes = [item["type"] for item in lineage]
        for required in (
            "Biosample",
            "IsotopeLabelingProcess",
            "DensityGradientFractionationProcess",
            "LibraryPreparation",
            "NucleotideSequencing",
        ):
            assert classes.count("nmdc:" + required) == 1
        assert (
            classes.count("nmdc:Extraction") == 2
        )  # bulk extraction and fraction recovery
        assert record["was_generated_by"] in ancestors[record["id"]]
        gradient = next(
            item["id"]
            for item in lineage
            if item["type"] == "nmdc:DensityGradientFractionationProcess"
        )
        (manifest,) = record["in_manifest"]
        assert nodes[manifest]["manifest_category"] == "fractions"
        gradient_members.setdefault(manifest, set()).add(gradient)
    assert len(gradient_members) == 2
    assert all(len(gradients) == 1 for gradients in gradient_members.values())
    assert len(set.union(*gradient_members.values())) == 2


def test_missing_reference_is_explicit(lifecycle: dict) -> None:
    """A schema-valid ID alone must not look like a defined sample in a diagram."""
    missing = lifecycle["biosample_set"].pop()["id"]
    with pytest.raises(ValueError, match=missing):
        build_graph(lifecycle)
    nodes, edges = build_graph(lifecycle, allow_external=True)
    assert nodes[missing] == {}
    assert "External reference" in render_graph(nodes, edges, "mermaid")


def test_duplicate_identifier_is_rejected(lifecycle: dict) -> None:
    """Do not silently overwrite one of two conflicting instance definitions."""
    lifecycle["biosample_set"].append(deepcopy(lifecycle["biosample_set"][0]))
    with pytest.raises(ValueError, match="Duplicate record id"):
        build_graph(lifecycle)


def test_renderers_keep_relations_and_escape_labels(lifecycle: dict) -> None:
    """Both outputs distinguish grouping from flow and quote untrusted labels."""
    lifecycle["biosample_set"][0]["name"] = 'sample "quoted" <tag> [bracket]'
    nodes, edges = build_graph(lifecycle)
    mermaid = render_graph(nodes, edges, "mermaid")
    dot = render_graph(nodes, edges, "dot")
    assert "#34;quoted#34;" in mermaid
    assert "<tag>" not in mermaid
    assert '\\"quoted\\"' in dot
    assert mermaid.count("-.->|in_manifest|") == 6
    assert dot.count("style=dashed") == 6
    assert mermaid.count("-->|has_input|") == 24
