"""Data test."""
import os
import pprint
import unittest

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import OrderedBy
from linkml_runtime.linkml_model.meta import ClassDefinition

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "nmdc_schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc_materialized_patterns.yaml')


class TestAllMultivaluedClassRangeSlotsAreInlinedAsList(unittest.TestCase):
    """Test data and datamodel."""

    def test_all_multivalued_class_range_slots_are_inlined_as_list(self):
        view = SchemaView(SCHEMA_FILE)
        print("\n")

        all_class_names = list(view.all_classes(ordered_by=OrderedBy.LEXICAL).keys())

        all_class_names.sort()

        for current_class in all_class_names:
            current_induced_class = view.induced_class(current_class)
            current_induced_slots = current_induced_class.attributes

            for sk, sv in sorted(current_induced_slots.items()):

                if isinstance(view.get_element(sv.range), ClassDefinition) and sv.multivalued:

                    # check if the class in the range has an identifiers slot
                    range_identifier = view.get_identifier_slot(sv.range)

                    if range_identifier is not None:
                        pass
                    else:
                        print(
                            f"{current_class}.{sk} is multivalued and has range {sv.range}, which does not have an identifying slot, so must be inlined_as_list")
                        print(yaml_dumper.dumps(sv))
                        self.assertTrue(sv.inlined_as_list,
                                        f"{current_class}.{sk} is multivalued and has range {sv.range}, which does not have an identifying slot, so must be inlined_as_list")