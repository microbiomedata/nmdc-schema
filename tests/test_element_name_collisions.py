"""Check that no two schema elements have names that are spelled or pronounced alike.

Two names collide when they are the same once case, underscores, hyphens, spaces and a plural
ending are ignored, such as the `provenance_metadata` slot and the `ProvenanceMetadata` class.
See https://github.com/microbiomedata/nmdc-schema/issues/3466.
"""

import re
from collections import defaultdict

from linkml_runtime import SchemaView

from tests import ROOT

# The source schema, not the generated nmdc_materialized_patterns.yaml, so the check sees
# edits under src/schema/ before `make all` regenerates the artifact.
SOURCE_SCHEMA = ROOT / "src" / "schema" / "nmdc.yaml"

# Groups that existed when this test was added (2026-10-08), as (kind, name). Don't add to this list.
GRANDFATHERED = {
    frozenset({("slot", "provenance_metadata"), ("class", "ProvenanceMetadata")}),
}

ELEMENT_KINDS = {
    "class": SchemaView.all_classes,
    "slot": SchemaView.all_slots,
    "enum": SchemaView.all_enums,
    "type": SchemaView.all_types,
    "subset": SchemaView.all_subsets,
}


def singular(word: str) -> str:
    """Return a lowercase word without a regular English plural ending."""
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith(("sses", "xes", "zes", "ches", "shes")):
        return word[:-2]
    if word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def normalize(name: str) -> str:
    """Return a name lowercased, without separators, and without a plural ending."""
    return singular(re.sub(r"[_\s-]", "", name).lower())


def colliding_names(view: SchemaView) -> set[frozenset[tuple[str, str]]]:
    """Return each group of two or more elements whose names normalize to the same string.

    Elements are (kind, name), so a class and a slot with the identical name count as a pair.
    """
    groups = defaultdict(set)
    for kind, getter in ELEMENT_KINDS.items():
        for name in getter(view):
            groups[normalize(name)].add((kind, name))
    return {frozenset(members) for members in groups.values() if len(members) > 1}


def test_no_new_element_names_collide() -> None:
    new = colliding_names(SchemaView(SOURCE_SCHEMA)) - GRANDFATHERED
    assert new == set(), f"Rename one element in each group: {[sorted(g) for g in new]}"


def test_grandfathered_list_has_no_fixed_entries() -> None:
    assert GRANDFATHERED - colliding_names(SchemaView(SOURCE_SCHEMA)) == set()


def test_normalize() -> None:
    assert normalize("provenance_metadata") == normalize("ProvenanceMetadata")
    assert normalize("isotopolog_additions") == normalize("IsotopologAddition")
    assert normalize("processes") == normalize("Process")
    assert normalize("categories") == normalize("Category")
    assert normalize("boxes") == normalize("box")
    assert normalize("ctg_n50") != normalize("ctg_l50")
    assert normalize("nitrate_nitrogen") != normalize("nitrite_nitrogen")
    assert normalize("process") == "process"
    assert normalize("status") == "status"
    assert normalize("analysis") == "analysis"


TOY_SCHEMA = """
id: https://example.org/toy
name: toy
prefixes:
  linkml: https://w3id.org/linkml/
default_prefix: toy
imports:
  - linkml:types
classes:
  Sample: {}
  Process: {}
slots:
  Sample: {}
  processes: {}
  depth: {}
"""


def test_identical_and_plural_names_of_different_kinds_collide() -> None:
    found = colliding_names(SchemaView(TOY_SCHEMA))
    assert found == {
        frozenset({("class", "Sample"), ("slot", "Sample")}),
        frozenset({("class", "Process"), ("slot", "processes")}),
    }
