"""Data test."""
import os
import pprint
import unittest

from linkml_runtime import SchemaView
from linkml_runtime.utils.schemaview import OrderedBy

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')

allowed_typeless_classes = set()

allowed_typeless_classes.add('Database')


class TestAllClassesCanUseTypeSlot(unittest.TestCase):
    """Test data and datamodel."""

    def test_all_classes_can_use_type_slot(self):
        view = SchemaView(SCHEMA_FILE)
        print("\n")
        all_classes_dict = view.all_classes(ordered_by=OrderedBy.LEXICAL)
        all_classes = set()
        classes_using_type_slot = set()
        for current_class_name, _ in all_classes_dict.items():
            all_classes.add(str(current_class_name))
            current_induced_class = view.induced_class(current_class_name)
            current_induced_slots = current_induced_class.attributes
            current_induced_slot_names = [str(sk) for sk, sv in current_induced_slots.items()]
            current_induced_slot_names.sort()
            if 'type' in current_induced_slot_names:
                classes_using_type_slot.add(str(current_class_name))

        typeless_classes = all_classes - classes_using_type_slot
        # pprint.pprint(typeless_classes)

        # pprint.pprint(allowed_typeless_classes)

        forbidden_typeless_classes = typeless_classes - allowed_typeless_classes
        # pprint.pprint(forbidden_typeless_classes)

        self.assertListEqual(list(forbidden_typeless_classes), [],
                             msg="Classes not using type slot: " + str(forbidden_typeless_classes))
