import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE


class TestEnums(unittest.TestCase):
    """Test suite for enum-related validations."""

    def test_ProtocolForEnum_should_have_PlannedProcess_permissible_values(self):
        """Test that the permissible values of ProtocolForEnum are the class descendants of
        PlannedProcess."""
        schema_view = SchemaView(SCHEMA_FILE)


        planned_process_class_names = set(schema_view.class_descendants("PlannedProcess"))

        protocol_for_enum = schema_view.get_enum("ProtocolForEnum", strict=True)
        protocol_for_permissible_value_names = set(protocol_for_enum.permissible_values.keys())

        self.assertEqual(protocol_for_permissible_value_names, planned_process_class_names)
