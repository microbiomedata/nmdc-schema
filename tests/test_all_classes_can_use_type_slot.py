"""Data test."""
import os
import unittest

from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')

allowed_typeless_classes = set(
    'Database',
)


class TestAllClassesCanUseTypeSlot(unittest.TestCase):
    """Test data and datamodel."""

    def test_all_classes_can_use_type_slot(self):
        view = SchemaView(SCHEMA_FILE)
        print("\n")
        all_classes = view.all_classes()
        all_class_names = [ck for ck, cv in all_classes.items()]
        classes_using_type_slot = set()
        for current_class_name in all_class_names:
            current_induced_class = view.induced_class(current_class_name)
            current_induced_alots = current_induced_class.attributes
            current_induced_slot_names = [str(sk) for sk, sv in current_induced_alots.items()]
            current_induced_slot_names.sort()
            if 'type' in current_induced_slot_names:
                classes_using_type_slot.add(str(current_class_name))
        classes_using_type_slot = set(classes_using_type_slot)
        un_allowed_typeless_classes = classes_using_type_slot - allowed_typeless_classes
        classes_not_using_type_slot = list(un_allowed_typeless_classes - classes_using_type_slot)
        classes_not_using_type_slot.sort()

        self.assertListEqual(classes_not_using_type_slot, [],
                             msg="Classes not using type slot: " + str(classes_not_using_type_slot))
