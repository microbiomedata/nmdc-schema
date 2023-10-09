import logging

import unittest

from nmdc_schema.get_mixs_slots import MIxSSlotsGetter
from nmdc_schema.get_nmdc_view import ViewGetter
from nmdc_schema.get_slots_from_class import ClassSlotsGetter
from nmdc_schema.get_slots_from_view import SchemaSlotsGetter


class Getters(unittest.TestCase):
    def test_view_getter(self):
        view_getter = ViewGetter()
        nmdc_view = view_getter.get_view()
        self.assertEqual(nmdc_view.schema.name, "NMDC")

    def test_schema_slots_getter(self):
        schema_slots_getter = SchemaSlotsGetter()
        schema_slots = schema_slots_getter.get_schema_slots()
        self.assertIsNotNone(schema_slots)

    def test_get_slots_from_class(self):
        class_name = "Study"
        class_slot_getter = ClassSlotsGetter()
        class_slots = class_slot_getter.get_class_slots(class_name)
        self.assertIsNotNone(class_slots)

    # def test_get_mixs_slots(self): # requires network connection
    #     pass
    #     mg = MIxSSlotsGetter()
    #     mixs_slots = mg.get_unique_slot_names()
    #     self.assertIsNotNone(mixs_slots)


if __name__ == "__main__":
    unittest.main()
