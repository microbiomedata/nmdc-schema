import re
import unittest

from linkml_runtime import SchemaView
from ucumvert import get_ucum_parser

from tests import SCHEMA_FILE

# Regex patterns that catch invalid UCUM codes that ucumvert does not catch
INVALID_UNIT_OVERRIDE_PATTERNS = {
    # https://github.com/dalito/ucumvert/issues/50
    "/Cel": "Attempt to divide by non-ratio unit degree Celsius"
}


class TestHasUnitEnum(unittest.TestCase):

    def test_valid_ucum_permissible_values(self):
        """Test that the permissible values of UnitEnum are valid UCUM codes.

        Validation is done using the ucumvert library, which is known to be slightly incomplete. If
        additional checks are needed to compensate for this, they can be added to the
        INVALID_UNIT_OVERRIDE_PATTERNS dictionary. Please also add an issue to the ucumvert
        repository in that case.
        """

        schema_view = SchemaView(SCHEMA_FILE)
        unit_enum = schema_view.get_enum("UnitEnum")
        if not unit_enum:
            self.fail("UnitEnum not found in schema")

        if not unit_enum.permissible_values:
            self.fail("UnitEnum has no permissible values")

        ucum_parser = get_ucum_parser()
        for permissible_value in unit_enum.permissible_values.values():
            try:
                ucum_parser.parse(permissible_value.text)
            except Exception:
                self.fail(f"Failed to parse UCUM code '{permissible_value.text}'")

            for pattern, message in INVALID_UNIT_OVERRIDE_PATTERNS.items():
                if re.search(pattern, permissible_value.text):
                    self.fail(
                        f"Invalid UCUM code '{permissible_value.text}': {message}"
                    )
