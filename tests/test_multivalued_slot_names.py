"""Check that new NMDC multivalued slots have plural names.

CONTRIBUTING.md says "Multivalued slots should be named as plurals", and
https://github.com/microbiomedata/nmdc-schema/issues/1284 agreed to apply that to new slots.
Imported MIxS slots are exempt. See https://github.com/microbiomedata/nmdc-schema/issues/3467.
"""

import re

import yaml
from linkml_runtime import SchemaView

from tests import ROOT, SCHEMA_FILE

MIXS_MODULE = ROOT / "src" / "schema" / "mixs.yaml"

# Relationship-style names, where a plural doesn't fit: has_input, part_of, was_informed_by.
RELATIONSHIP_NAME = re.compile(r"^(has|is|was)_|_(of|by|used)$")

# Plural nouns that don't end in "s".
IRREGULAR_PLURALS = {"data", "metadata", "media", "criteria"}

# Multivalued slots with singular names that existed when this test was added (2026-10-08).
# Renaming them would need a migrator, so they are grandfathered. Don't add to this list.
GRANDFATHERED = {
    "analysis_type",
    "functional_annotation_agg",
    "host_family_relation",
    "in_manifest",
    "mags_list",
    "members_id",
    "object_set",
    "sample_link",
    "sampled_portion",
    "study_image",
    "submission_portal_identifier",
    "uses_calibration",
}


def is_plural(word: str) -> bool:
    """Return True if a name's last word reads as a plural."""
    return word in IRREGULAR_PLURALS or (word.endswith("s") and not word.endswith("ss"))


def mixs_slot_names() -> set[str]:
    """Return the slots defined in the imported MIxS module."""
    return set(yaml.safe_load(MIXS_MODULE.read_text())["slots"])


def singular_multivalued_slots(view: SchemaView) -> list[str]:
    """Return NMDC multivalued slots whose last word is singular, other than relationship names."""
    imported = mixs_slot_names()
    return sorted(
        name
        for name, slot in view.all_slots().items()
        if slot.multivalued
        and name not in imported
        and not RELATIONSHIP_NAME.search(name)
        and not is_plural(name.split("_")[-1])
    )


def test_new_multivalued_slots_have_plural_names():
    found = singular_multivalued_slots(SchemaView(SCHEMA_FILE))
    new = sorted(set(found) - GRANDFATHERED)
    assert new == [], f"Name these multivalued slots as plurals: {new}"


def test_grandfathered_list_has_no_fixed_entries():
    # Once a grandfathered slot is renamed or removed, drop it from the list.
    found = set(singular_multivalued_slots(SchemaView(SCHEMA_FILE)))
    assert sorted(GRANDFATHERED - found) == []


def test_is_plural():
    assert is_plural("studies") and is_plural("data") and is_plural("inputs")
    assert (
        not is_plural("image") and not is_plural("process") and not is_plural("class")
    )


def test_relationship_names_are_exempt():
    assert RELATIONSHIP_NAME.search("has_input")
    assert RELATIONSHIP_NAME.search("part_of")
    assert RELATIONSHIP_NAME.search("was_informed_by")
    assert RELATIONSHIP_NAME.search("instrument_used")
    assert not RELATIONSHIP_NAME.search("study_image")
