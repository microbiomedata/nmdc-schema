import unittest

from linkml_runtime import SchemaView

meta_url = "https://w3id.org/linkml/meta"


class SlotDefTestCase(unittest.TestCase):
    def test_access_meta_schema(self):
        # how to do this without a network connection?
        meta_view = SchemaView(meta_url)
        self.assertEqual(meta_view.schema.name, "meta")

    # def test_slot_definition_defined(self):
    #     meta_view = SchemaView(meta_url)
    #     metaclasses = meta_view.all_classes()
    #     metaclass_names = [i for i in metaclasses.keys()]
    #     metaclass_names.sort()
    #     self.assertIn("slot_definition", metaclass_names)
    #
    # def test_report_slotdef_slots(self):
    #     meta_view = SchemaView(meta_url)
    #     slotdef = meta_view.induced_class("type_definition")
    #     slotdef_slots = slotdef.attributes
    #     slotsdef_slot_names = [i for i in slotdef_slots.keys()]
    #     slotsdef_slot_names.sort()
    #     print(slotsdef_slot_names)
