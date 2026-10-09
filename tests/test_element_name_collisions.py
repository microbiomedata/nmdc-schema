"""Check that no two schema elements have names that are spelled or pronounced alike.

Two names collide when they are the same once case, underscores, hyphens, spaces and a plural
ending are ignored, such as the `provenance_metadata` slot and the `ProvenanceMetadata` class.
See https://github.com/microbiomedata/nmdc-schema/issues/3466.
"""

import re
from collections import defaultdict

from linkml_runtime import SchemaView

import yaml

from tests import ROOT

# The source schema, not the generated nmdc_materialized_patterns.yaml, so the check sees
# edits under src/schema/ before `make all` regenerates the artifact.
SOURCE_SCHEMA = ROOT / "src" / "schema" / "nmdc.yaml"
MIXS_MODULE = ROOT / "src" / "schema" / "mixs.yaml"

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


def singular_forms(word: str) -> set[str]:
    """Return every form a lowercase word could have without a regular English plural ending.

    Endings are ambiguous (`houses` is `house` + s, `buses` is `bus` + es), so every reading is
    kept, and two names collide if any of their forms match. The endings are the ones
    CONTRIBUTING.md names: -s, -es, -ies and -yses.
    """
    forms = {word}
    if word.endswith("s") and not word.endswith("ss"):
        forms.add(word[:-1])
    if word.endswith("es"):
        forms.add(word[:-2])
    if word.endswith("ies") and len(word) > 4:
        forms.add(word[:-3] + "y")
    if word.endswith("yses"):
        forms.add(word[:-4] + "ysis")
    return forms


def name_forms(name: str) -> set[str]:
    """Return a name's possible singular forms, lowercased and without separators."""
    return singular_forms(re.sub(r"[_\s-]", "", name).lower())


def mixs_elements() -> frozenset[tuple[str, str]]:
    """Return (kind, name) for the classes, slots and enums defined in the imported MIxS module."""
    doc = yaml.safe_load(MIXS_MODULE.read_text())
    kinds = {"classes": "class", "slots": "slot", "enums": "enum"}
    return frozenset(
        (kind, name)
        for section, kind in kinds.items()
        for name in doc.get(section) or {}
    )


def colliding_names(
    view: SchemaView, imported: frozenset[tuple[str, str]] = frozenset()
) -> set[frozenset[tuple[str, str]]]:
    """Return each group of two or more elements that share a possible singular form.

    Elements are (kind, name), so a class and a slot with the identical name count as a pair.
    A group made up only of imported elements, matched by kind and name, is skipped, because CONTRIBUTING.md exempts imported
    elements from the naming conventions. A new NMDC name that collides with an imported one still counts.
    """
    groups = defaultdict(set)
    for kind, getter in ELEMENT_KINDS.items():
        for name in getter(view):
            for form in name_forms(name):
                groups[form].add((kind, name))
    return {
        frozenset(members)
        for members in groups.values()
        if len(members) > 1 and not members <= imported
    }


def test_no_new_element_names_collide() -> None:
    new = colliding_names(SchemaView(SOURCE_SCHEMA), mixs_elements()) - GRANDFATHERED
    assert new == set(), f"Rename one element in each group: {[sorted(g) for g in new]}"


def test_grandfathered_list_has_no_fixed_entries() -> None:
    assert (
        GRANDFATHERED - colliding_names(SchemaView(SOURCE_SCHEMA), mixs_elements())
        == set()
    )


def collide(a: str, b: str) -> bool:
    return bool(name_forms(a) & name_forms(b))


def test_name_forms() -> None:
    assert collide("provenance_metadata", "ProvenanceMetadata")
    assert collide("isotopolog_additions", "IsotopologAddition")
    assert collide("processes", "Process")
    assert collide("categories", "Category")
    assert collide("statuses", "Status")
    assert collide("buses", "Bus")
    assert collide("analyses", "Analysis")
    assert collide("houses", "House")
    assert collide("causes", "Cause")
    assert collide("phases", "Phase")
    assert collide("boxes", "box")
    assert not collide("ctg_n50", "ctg_l50")
    assert not collide("nitrate_nitrogen", "nitrite_nitrogen")
    assert not collide("status", "statue")


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


def test_groups_of_only_imported_elements_are_skipped() -> None:
    view = SchemaView(TOY_SCHEMA)
    both_processes = frozenset({("class", "Process"), ("slot", "processes")})
    both_samples = frozenset({("class", "Sample"), ("slot", "Sample")})
    # Both Process elements imported: skipped.
    assert colliding_names(view, both_processes) == {both_samples}
    # Only the Sample slot imported, and a new Sample class with the exact same spelling: still a collision.
    assert both_samples in colliding_names(view, frozenset({("slot", "Sample")}))


def test_identical_and_plural_names_of_different_kinds_collide() -> None:
    found = colliding_names(SchemaView(TOY_SCHEMA))
    assert found == {
        frozenset({("class", "Sample"), ("slot", "Sample")}),
        frozenset({("class", "Process"), ("slot", "processes")}),
    }
