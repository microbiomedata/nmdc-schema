import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE


class TestBiosampleSlotsHaveTitles(unittest.TestCase):
    """Every Biosample slot needs a title on its top-level definition.

    The Data Portal (nmdc-server ``formatSlotLabel``) labels Biosample fields with
    ``slots[<name>].title`` from the materialized schema and otherwise capitalizes
    each word of the slot name, which turns acronyms like NCBI into "Ncbi". It does
    not read titles from ``slot_usage``, so the title must be on the slot itself.
    See https://github.com/microbiomedata/nmdc-schema/issues/3444
    """

    def test_biosample_slots_have_titles(self):
        view = SchemaView(SCHEMA_FILE)
        untitled = sorted(
            slot.name
            for slot in view.class_induced_slots("Biosample")
            if not view.get_slot(slot.name).title
        )
        self.assertListEqual(untitled, [], "Biosample slots without a top-level title")
