"""
Test that validates has_unit values in YAML data files against UnitEnum
and checks unit appropriateness for their slots.
"""

import os
import unittest
from pathlib import Path
from typing import Any, Optional

import yaml
from linkml_runtime import SchemaView

from tests import ROOT, SCHEMA_FILE

DATA_DIR = os.path.join(ROOT, "src", "data", "valid")


def iter_example_quantity_values():
    """Iterate over example QuantityValue objects in example YAML files."""

    def _yield_quantity_value(data: Any, path: Optional[list[str]] = None):
        """Recursively yield QuantityValue objects from data."""
        if path is None:
            path = []
        if isinstance(data, dict):
            if data.get("type") == "nmdc:QuantityValue":
                yield path, data
            else:
                # Recursively search nested dictionaries
                for key, value in data.items():
                    yield from _yield_quantity_value(value, path + [key])
        elif isinstance(data, list):
            # Handle lists of objects
            for i, item in enumerate(data):
                yield from _yield_quantity_value(item, path + [str(i)])

    data_dir = Path(DATA_DIR)
    for yaml_file in data_dir.glob("*.yaml"):
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)

        for data_path, quantity_value in _yield_quantity_value(data):
            yield yaml_file, data_path, quantity_value


class HasUnitValidator:
    """Utility class to validate has_unit values in YAML data files."""

    def __init__(self, schema_view: SchemaView):
        self.schema_view = schema_view
        self.unit_enum = schema_view.get_enum("UnitEnum")
        self.allowed_units = (
            set(self.unit_enum.permissible_values.keys()) if self.unit_enum else set()
        )
        self._slot_storage_units_cache = {}

    def get_slot_storage_units(self, slot_name: str) -> Optional[list[str]]:
        """Get allowed storage_units for a slot, with caching."""
        if slot_name in self._slot_storage_units_cache:
            return self._slot_storage_units_cache[slot_name]

        slot = self.schema_view.get_slot(slot_name)
        if not slot or not slot.annotations:
            self._slot_storage_units_cache[slot_name] = None
            return None

        storage_units = None
        if "storage_units" in slot.annotations:
            annotation_obj = slot.annotations["storage_units"]
            if annotation_obj and hasattr(annotation_obj, "value"):
                # Split on pipes for multiple units
                storage_units = str(annotation_obj.value).split("|")

        self._slot_storage_units_cache[slot_name] = storage_units
        return storage_units

    def validate_has_unit_against_enum(self, has_unit: str) -> bool:
        """Check if a has_unit value exists in UnitEnum."""
        return has_unit in self.allowed_units

    def validate_has_unit_against_slot(
        self, has_unit: str, slot_name: str
    ) -> tuple[bool, str]:
        """
        Check if a has_unit value is appropriate for the given slot.
        Returns (is_valid, message).
        """
        storage_units = self.get_slot_storage_units(slot_name)

        if storage_units is None:
            # No storage_units constraint, any valid unit is acceptable
            return True, f"No storage_units constraint for slot '{slot_name}'"

        if has_unit in storage_units:
            return True, f"Unit matches storage_units for slot '{slot_name}'"
        else:
            return (
                False,
                f"Unit '{has_unit}' not in allowed storage_units {storage_units} for slot '{slot_name}'",
            )


class TestHasUnitValidation(unittest.TestCase):
    """Test has_unit validation across YAML data files."""

    def setUp(self):
        """Set up test with schema view and validator."""
        self.schema_view = SchemaView(SCHEMA_FILE)
        self.validator = HasUnitValidator(self.schema_view)
        self.data_dir = Path(DATA_DIR)

    def test_has_unit_enum_validation(self):
        """Test that all has_unit values exist in UnitEnum."""
        violations = []

        for file, data_path, quantity_value in iter_example_quantity_values():
            has_unit = quantity_value.get("has_unit")
            if not has_unit:
                violations.append(
                    f"{file}:{data_path} - QuantityValue is missing has_unit"
                )
            elif not self.validator.validate_has_unit_against_enum(has_unit):
                violations.append(
                    f"{file}:{data_path} - Unit '{has_unit}' not found in UnitEnum"
                )

        self.assertEqual(
            [], violations, f"Found {len(violations)} has_unit values not in UnitEnum"
        )

    def test_has_unit_slot_appropriateness(self):
        """Test that has_unit values are appropriate for their slots."""
        violations = []

        for file, data_path, quantity_value in iter_example_quantity_values():
            has_unit = quantity_value.get("has_unit")
            if not has_unit:
                violations.append(
                    f"{file}:{data_path} - QuantityValue is missing has_unit"
                )
            else:
                # Get last part of path as slot name
                slot_name = data_path[-1] if data_path else None
                if not slot_name:
                    # Edge case: direct QuantityValue instantiation without clear slot ownership
                    continue
                is_valid, message = self.validator.validate_has_unit_against_slot(
                    has_unit, slot_name
                )
                if not is_valid:
                    violations.append(
                        f"{file}:{data_path} (slot: {slot_name}) - {message}"
                    )

        self.assertEqual(
            [],
            violations,
            f"Found {len(violations)} has_unit values inappropriate for their slots",
        )


if __name__ == "__main__":
    unittest.main()
