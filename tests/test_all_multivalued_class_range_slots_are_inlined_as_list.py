import unittest

from linkml_runtime import SchemaView
from linkml_runtime.utils.schemaview import OrderedBy
from linkml_runtime.linkml_model.meta import ClassDefinition

from tests import SCHEMA_FILE


class TestAllMultivaluedClassRangeSlotsAreInlinedAsList(unittest.TestCase):
    """Test data and datamodel."""

    def test_all_multivalued_class_range_slots_are_inlined_as_list(self):
        view = SchemaView(SCHEMA_FILE)

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
                        self.assertTrue(sv.inlined_as_list,
                                        f"{current_class}.{sk} is multivalued and has range {sv.range}, which does not have an identifying slot, so must be inlined_as_list")