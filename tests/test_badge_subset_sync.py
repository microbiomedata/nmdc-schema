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
            try:
                bar = int(annotation.value)
            except (TypeError, ValueError):
                self.fail(
                    f"badge subset '{name}' has a non-integer "
                    f"{BADGE_BAR_ANNOTATION}: {annotation.value!r}"
                )
            member_count = sum(
                1
                for slot in self.schema_view.all_slots().values()
                if name in (slot.in_subset or [])
            )
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


if __name__ == "__main__":
    unittest.main()
