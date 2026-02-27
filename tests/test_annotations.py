import unittest
from collections.abc import Iterator
from typing import Any

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import Element

from tests import SCHEMA_FILE

# Allowed annotation keys based on the provided whitelist
# Note: Expected_value and Preferred_unit use GSC MIxS v6.2.2 capitalization
ALLOWED_ANNOTATION_KEYS = {
    "Expected_value",
    "file_name_pattern",
    "units_alignment_excuse",
    "occurrence",
    "originally",
    "Preferred_unit",
    "source",
    "storage_units",
    "tooltip",
}


def iter_annotations(schema_view: SchemaView) -> Iterator[tuple[str, str, Any]]:
    """Iterate over all annotations in the schema."""

    def _element_annotations(element_path: str, element: Element):
        """Yield annotations for a given element."""
        if element.annotations:
            for annotation in element.annotations.values():
                yield element_path, annotation.tag, annotation.value

    for element_name, element in schema_view.all_elements().items():
        element_type = type(element).__name__

        # Yield the annotations for the element itself
        yield from _element_annotations(f"{element_type}.{element_name}", element)

        # Descend into certain meta-slots that can contain other elements and yield their
        # annotations. This isn't totally generic, but it works for cases where annotations
        # commonly appear.
        meta_slots = ["slot_usage", "permissible_values"]
        for meta_slot in meta_slots:
            if hasattr(element, meta_slot):
                for sub_element_name, sub_element in getattr(
                    element, meta_slot
                ).items():
                    yield from _element_annotations(
                        f"{element_type}.{element_name}.{meta_slot}.{sub_element_name}",
                        sub_element,
                    )


class TestAnnotations(unittest.TestCase):
    """Tests for schema annotations."""

    def test_annotation_keys_whitelist(self):
        """Check all annotations in schema against whitelist."""
        view = SchemaView(SCHEMA_FILE)

        violations = []
        for schema_path, tag, value in iter_annotations(view):
            # Check if the annotation tag is in the allowed keys
            if tag not in ALLOWED_ANNOTATION_KEYS:
                violations.append(f"{schema_path}: {tag}")

        self.assertEqual(
            [], violations, f"Found {len(violations)} annotation key violations"
        )

    def test_storage_units_from_unit_enum(self):
        """Check that all storage_units annotation values come from UnitEnum."""
        view = SchemaView(SCHEMA_FILE)

        # Get allowed units from UnitEnum
        unit_enum = view.get_enum("UnitEnum")
        if not unit_enum or not unit_enum.permissible_values:
            self.fail("UnitEnum not found or has no permissible values")
        allowed_units = set(unit_enum.permissible_values.keys())

        violations = []
        for schema_path, tag, value in iter_annotations(view):
            if tag == "storage_units":
                if not isinstance(value, str):
                    violations.append(
                        f"{schema_path}: storage_units value '{value}' is not a string"
                    )
                    continue
                # Split on pipes and check each unit
                for unit in value.split("|"):
                    if unit not in allowed_units:
                        violations.append(
                            f"{schema_path}: storage_units value '{unit}' not in UnitEnum"
                        )

        self.assertEqual(
            [], violations, f"Found {len(violations)} storage_units violations"
        )


if __name__ == "__main__":
    unittest.main()
