"""Check that no two schema elements have names that are spelled or pronounced alike.

Two names collide when they are the same once case, underscores, hyphens, spaces and a plural
ending are ignored, such as the `provenance_metadata` slot and the `ProvenanceMetadata` class.
See https://github.com/microbiomedata/nmdc-schema/issues/3466.
"""

import re
from collections import defaultdict

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

# Pairs that existed when this test was added (2026-10-08). Don't add to this list.
GRANDFATHERED = {
    frozenset({"provenance_metadata", "ProvenanceMetadata"}),
}


def normalize(name: str) -> str:
    """Return a name lowercased, without separators, and without a final plural "s"."""
    flat = re.sub(r"[_\s-]", "", name).lower()
    return flat[:-1] if flat.endswith("s") and not flat.endswith("ss") else flat


def colliding_names(view: SchemaView) -> set[frozenset[str]]:
    """Return each group of two or more element names that normalize to the same string."""
    groups = defaultdict(set)
    for getter in (
        view.all_classes,
        view.all_slots,
        view.all_enums,
        view.all_types,
        view.all_subsets,
    ):
        for name in getter():
            groups[normalize(name)].add(name)
    return {frozenset(names) for names in groups.values() if len(names) > 1}


def test_no_new_element_names_collide():
    new = colliding_names(SchemaView(SCHEMA_FILE)) - GRANDFATHERED
    assert new == set(), f"Rename one element in each group: {[sorted(g) for g in new]}"


def test_grandfathered_list_has_no_fixed_entries():
    assert GRANDFATHERED - colliding_names(SchemaView(SCHEMA_FILE)) == set()


def test_normalize():
    assert normalize("provenance_metadata") == normalize("ProvenanceMetadata")
    assert normalize("isotopolog_additions") == normalize("IsotopologAddition")
    assert normalize("ctg_n50") != normalize("ctg_l50")
    assert normalize("nitrate_nitrogen") != normalize("nitrite_nitrogen")
    assert normalize("process") == "process"
