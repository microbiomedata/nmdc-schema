import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE


class TestEnums(unittest.TestCase):
    """Test suite for enum-related validations."""

    def test_ProtocolForEnum_should_have_PlannedProcess_permissible_values(self):
        """Test that the permissible values of ProtocolForEnum are the non-abstract class
        descendants of PlannedProcess."""
        schema_view = SchemaView(SCHEMA_FILE)


        non_abstract_planned_process_class_names = set()
        for class_name in schema_view.class_descendants("PlannedProcess"):
            class_def = schema_view.get_class(class_name, strict=True)
            if not class_def.abstract:
                non_abstract_planned_process_class_names.add(class_name)

        protocol_for_enum = schema_view.get_enum("ProtocolForEnum", strict=True)
        protocol_for_permissible_value_names = set(protocol_for_enum.permissible_values.keys())

        self.assertEqual(protocol_for_permissible_value_names, non_abstract_planned_process_class_names)
