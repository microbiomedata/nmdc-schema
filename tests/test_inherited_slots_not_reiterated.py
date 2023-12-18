"""Data test."""
import os
import pprint
import unittest

from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')


class TestInheritedSlotsNotReiterated(unittest.TestCase):

    def test_inherited_slots_not_reiterated(self):
        class_parents = {}

        view = SchemaView(SCHEMA_FILE)
        print("\n")
        all_classes = view.all_classes()
        for ck, cv in all_classes.items():
            if "is_a" in cv and cv["is_a"] is not None:
                class_parents[ck] = cv["is_a"]

        for class_name, parent_name in class_parents.items():
            parent_induced_class = view.induced_class(parent_name)
            parent_induced_slots = parent_induced_class.attributes
            parent_induced_slot_names = [str(sk) for sk, sv in parent_induced_slots.items()]

            current_asserted_slot_names = view.get_class(class_name).slots

            reiterated_slots = set(parent_induced_slot_names).intersection(set(current_asserted_slot_names))
            if len(reiterated_slots) > 0:
                # print(f"{class_name = }; {parent_name = }")
                # print(f"{reiterated_slots = }")
                reiterated_slots_list = list(reiterated_slots)
                self.assertListEqual(reiterated_slots_list, [],
                                     f"{class_name = }; {parent_name = }; {reiterated_slots_list = }")
