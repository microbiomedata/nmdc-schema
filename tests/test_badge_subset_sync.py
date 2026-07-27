"""Keep the badge enum and the badge-topic subsets in sync.

The MetadataBadgeEnum permissible values are named ``<topic>_<level>``, where
``<topic>`` is the name of a subset whose ``in_subset`` includes ``badge_topic``
and ``<level>`` is one of the recognized badge levels. These tests fail if the
enum and the badge subsets drift apart, for example when a subset is added
without a matching permissible value or vice versa.

See https://github.com/microbiomedata/nmdc-schema/issues/3227 (badges slot and
enum) and https://github.com/microbiomedata/nmdc-schema/issues/3228 (subsets).
"""

import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

BADGE_ENUM = "MetadataBadgeEnum"
BADGE_LEVELS = {"silver", "gold"}
BADGE_TOPIC_SUBSET = "badge_topic"


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


def _split_topic_level(permissible_value):
    """Split ``<topic>_<level>`` into (topic, level), or (value, None) if no level."""
    for level in BADGE_LEVELS:
        suffix = "_" + level
        if permissible_value.endswith(suffix):
            return permissible_value[: -len(suffix)], level
    return permissible_value, None


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

    def test_every_permissible_value_maps_to_a_badge_subset(self):
        subsets = _badge_topic_subsets(self.schema_view)
        for permissible_value in _badge_permissible_values(self.schema_view):
            topic, level = _split_topic_level(permissible_value)
            self.assertIn(
                level,
                BADGE_LEVELS,
                f"badge permissible value '{permissible_value}' has no recognized "
                f"level suffix {sorted(BADGE_LEVELS)}",
            )
            self.assertIn(
                topic,
                subsets,
                f"badge permissible value '{permissible_value}' topic '{topic}' is "
                f"not a badge_topic subset {sorted(subsets)}",
            )

    def test_every_badge_subset_has_a_permissible_value(self):
        pv_topics = {
            _split_topic_level(pv)[0]
            for pv in _badge_permissible_values(self.schema_view)
        }
        for subset in _badge_topic_subsets(self.schema_view):
            self.assertIn(
                subset,
                pv_topics,
                f"badge subset '{subset}' has no permissible value in {BADGE_ENUM}",
            )


if __name__ == "__main__":
    unittest.main()
