"""Keep the badge enum and the badge-topic subsets in sync.

Badges are awarded in two ways, so the enum has two kinds of permissible value:

- A completeness badge is named for a subset whose ``in_subset`` includes
  ``badge_topic``. It is awarded when a record populates at least that subset's
  ``badge_minimum_slots`` slots. These must correspond one-to-one with the badge
  subsets, which is what most of these tests check.
- A provenance badge is awarded from a recorded fact about where the metadata
  came from rather than from slot completeness, so it has no subset. There is
  one today, ``expert_curation``, awarded from
  ``ProvenanceMetadata.source_system_of_record``.

There are no levels or tiers: a badge is present or absent (metadata quality
squad decision, 2026-08-05).

See https://github.com/microbiomedata/nmdc-schema/issues/3227 (badges slot and
enum), https://github.com/microbiomedata/nmdc-schema/issues/3228 (subsets) and
https://github.com/microbiomedata/nmdc-schema/issues/3326 (qualifying bar).

Badge-topic subsets carry created_on, last_updated_on and modified_by so a
re-evaluation job can tell that a badge definition changed and score every
record against it again, instead of re-running badge logic over every
biosample on every release. See
https://github.com/microbiomedata/nmdc-schema/issues/3374, and
https://github.com/microbiomedata/issues/issues/1820 for the job that reads
them.
"""

import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

BADGE_ENUM = "MetadataBadgeEnum"
BADGE_TOPIC_SUBSET = "badge_topic"
BADGE_BAR_ANNOTATION = "badge_minimum_slots"

# Badges awarded from provenance rather than slot completeness. These have no
# badge subset by design. Adding one here is a deliberate act: it exempts the
# value from the subset correspondence the other badges must satisfy.
PROVENANCE_BADGES = {"expert_curation"}

# The nmdc-runtime Dagster job that awards badges reads the subsets defined
# here, so the tests below keep them within what that job can read. See
# https://github.com/microbiomedata/nmdc-schema/issues/3440.
BADGE_JOB = (
    "nmdc_runtime/site/ops/badges.py in https://github.com/microbiomedata/nmdc-runtime"
)

# Slot ranges the badge job has an emptiness rule for, in addition to enums.
BADGE_JOB_RANGES = {
    "ControlledIdentifiedTermValue",
    "ControlledTermValue",
    "QuantityValue",
    "TextValue",
    "float",
    "string",
}

# The badge job awards expert_curation when a biosample's
# provenance_metadata.source_system_of_record equals this literal value.
EXPERT_CURATION_SOURCE = "NMDC_Submission_Portal"


def _badge_topic_subsets(schema_view):
    """Names of subsets that belong to the badge_topic group (via in_subset).

    The badge_topic group subset itself is not a member, so it is excluded.
    """
    return {
        name
        for name, subset in schema_view.all_subsets().items()
        if BADGE_TOPIC_SUBSET in (subset.in_subset or [])
    }


def _badge_permissible_values(schema_view):
    return set(schema_view.get_enum(BADGE_ENUM, strict=True).permissible_values.keys())


def _completeness_badges(schema_view):
    return _badge_permissible_values(schema_view) - PROVENANCE_BADGES


def _badge_subset_members(schema_view, subset_name):
    """Names of the slots whose in_subset includes the given subset."""
    return sorted(
        name
        for name, slot in schema_view.all_slots().items()
        if subset_name in (slot.in_subset or [])
    )


class TestBadgeSubsetSync(unittest.TestCase):
    """Validate the badge enum and badge-topic subsets stay aligned."""

    @classmethod
    def setUpClass(cls):
        cls.schema_view = SchemaView(SCHEMA_FILE)

    def test_badge_topic_subsets_exist(self):
        self.assertTrue(
            _badge_topic_subsets(self.schema_view),
            "no subsets have in_subset including badge_topic",
        )

    def test_every_completeness_badge_has_a_subset(self):
        subsets = _badge_topic_subsets(self.schema_view)
        for permissible_value in _completeness_badges(self.schema_view):
            self.assertIn(
                permissible_value,
                subsets,
                f"badge permissible value '{permissible_value}' is not a "
                f"badge_topic subset {sorted(subsets)}. If it is awarded from "
                f"provenance rather than slot completeness, add it to "
                f"PROVENANCE_BADGES and say so in its description.",
            )

    def test_every_badge_subset_has_a_permissible_value(self):
        permissible_values = _badge_permissible_values(self.schema_view)
        for subset in _badge_topic_subsets(self.schema_view):
            self.assertIn(
                subset,
                permissible_values,
                f"badge subset '{subset}' has no permissible value in {BADGE_ENUM}",
            )

    def test_provenance_badges_are_declared_in_the_enum(self):
        """PROVENANCE_BADGES must not drift away from the enum it exempts."""
        permissible_values = _badge_permissible_values(self.schema_view)
        for badge in PROVENANCE_BADGES:
            self.assertIn(
                badge,
                permissible_values,
                f"'{badge}' is exempted as a provenance badge but is not a "
                f"permissible value of {BADGE_ENUM}",
            )

    def test_provenance_badges_have_no_subset(self):
        """No subset of that name at all, not merely no badge_topic subset.

        Checking only badge_topic membership would let a same-named subset be
        declared outside the group, which is the drift this guards against.
        """
        all_subsets = set(self.schema_view.all_subsets().keys())
        for badge in PROVENANCE_BADGES:
            self.assertNotIn(
                badge,
                all_subsets,
                f"'{badge}' is exempted as a provenance badge but a subset of "
                f"that name is declared; it is one or the other",
            )

    def test_every_badge_subset_declares_provenance(self):
        """Each badge topic records its dates and modifier (issue 3374).

        The datetime format needs no assertion here because LinkML refuses to
        generate the schema when a datetime metaslot holds a value it cannot parse.
        """
        for name in _badge_topic_subsets(self.schema_view):
            subset = self.schema_view.get_subset(name)
            for metaslot in ("created_on", "last_updated_on", "modified_by"):
                value = getattr(subset, metaslot)
                self.assertTrue(
                    value,
                    f"badge subset '{name}' has no {metaslot}; add {metaslot} "
                    f"to record the subset's provenance.",
                )

    def test_every_badge_subset_declares_a_qualifying_bar(self):
        """Each completeness badge records how many slots earn it (issue 3326).

        The bar is an absolute count of populated slots, never a proportion of
        the subset's size, so that adding a slot to a subset can never revoke a
        badge a record has already earned.
        """
        for name in _badge_topic_subsets(self.schema_view):
            subset = self.schema_view.get_subset(name)
            annotation = (subset.annotations or {}).get(BADGE_BAR_ANNOTATION)
            self.assertIsNotNone(
                annotation,
                f"badge subset '{name}' has no {BADGE_BAR_ANNOTATION} annotation",
            )
            bar = annotation.value
            # An unquoted YAML integer. "2" and 2.0 would convert with int(),
            # but the badge job requires an integer and fails on either.
            self.assertTrue(
                isinstance(bar, int) and not isinstance(bar, bool),
                f"badge subset '{name}' has {BADGE_BAR_ANNOTATION} {bar!r} "
                f"({type(bar).__name__}); write it as an unquoted integer, "
                f"because {BADGE_JOB} requires one",
            )
            member_count = len(_badge_subset_members(self.schema_view, name))
            self.assertGreaterEqual(
                bar,
                1,
                f"badge subset '{name}' has {BADGE_BAR_ANNOTATION} {bar}; a bar "
                f"below 1 would award the badge to every record",
            )
            self.assertLessEqual(
                bar,
                member_count,
                f"badge subset '{name}' has {BADGE_BAR_ANNOTATION} {bar} but only "
                f"{member_count} member slots, so no record could ever earn it",
            )

    def test_badge_subset_members_are_biosample_slots(self):
        """Badges are awarded to biosamples, so every member must be a Biosample slot.

        SchemaView.induced_slot does not fail for a slot the class lacks; it
        returns the slot with the default range, so the badge job would quietly
        check a slot no biosample can have.
        """
        biosample_slots = set(self.schema_view.class_slots("Biosample"))
        for name in _badge_topic_subsets(self.schema_view):
            outside = [
                slot
                for slot in _badge_subset_members(self.schema_view, name)
                if slot not in biosample_slots
            ]
            self.assertEqual(
                outside,
                [],
                f"badge subset '{name}' has members that are not Biosample slots",
            )

    def test_badge_subset_ranges_are_readable_by_the_badge_job(self):
        """Every member's range must be one the badge job has an emptiness rule for."""
        enums = set(self.schema_view.all_enums())
        for name in _badge_topic_subsets(self.schema_view):
            unreadable = {}
            for slot in _badge_subset_members(self.schema_view, name):
                slot_range = self.schema_view.induced_slot(slot, "Biosample").range
                if slot_range not in BADGE_JOB_RANGES and slot_range not in enums:
                    unreadable[slot] = slot_range
            self.assertEqual(
                unreadable,
                {},
                f"badge subset '{name}' has members with ranges the badge job "
                f"has no rule for; add a rule to {BADGE_JOB} and to "
                f"BADGE_JOB_RANGES here, or drop the slot from the subset",
            )

    def test_expert_curation_source_value_exists(self):
        """The badge job matches this permissible value by its literal name."""
        source_range = self.schema_view.induced_slot(
            "source_system_of_record", "ProvenanceMetadata"
        ).range
        self.assertTrue(
            source_range in self.schema_view.all_enums(),
            f"source_system_of_record now has range {source_range!r}, not an "
            f"enum; {BADGE_JOB} compares it against {EXPERT_CURATION_SOURCE} "
            f"to award expert_curation, so change both together",
        )
        permissible_values = self.schema_view.get_enum(
            source_range, strict=True
        ).permissible_values
        self.assertIn(
            EXPERT_CURATION_SOURCE,
            permissible_values,
            f"{source_range} no longer has {EXPERT_CURATION_SOURCE}, which "
            f"{BADGE_JOB} compares against to award expert_curation; change "
            f"both together",
        )


if __name__ == "__main__":
    unittest.main()
