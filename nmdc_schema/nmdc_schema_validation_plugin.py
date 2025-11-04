from typing import Any, Optional, Iterator, Union

from linkml.validator.plugins import ValidationPlugin
from linkml.validator.report import ValidationResult, Severity
from linkml.validator.validation_context import ValidationContext
from linkml_runtime import SchemaView


def _yield_quantity_value_objects(data: Any, path: Optional[list[Union[str, int]]] = None):
    """Recursively yield QuantityValue objects from data."""
    if path is None:
        path = []
    if isinstance(data, dict):
        if data.get("type") == "nmdc:QuantityValue":
            yield path, data
        else:
            # Recursively search nested dictionaries
            for key, value in data.items():
                yield from _yield_quantity_value_objects(value, path + [key])
    elif isinstance(data, list):
        # Handle lists of objects
        for i, item in enumerate(data):
            yield from _yield_quantity_value_objects(item, path + [i])


class NmdcSchemaValidationPlugin(ValidationPlugin):
    """A validation plugin which validates instances using NMDC-specific validation logic.

    This plugin is designed to be used as a part of LinkML's validation framework and in conjunction
    with the `JsonSchemaValidationPlugin` provided by LinkML. This plugin performs the following
    additional checks:

      1. Ensure that values for slots with range `QuantityValue` have a `unit` property that is in
         agreement with the `storage_unit` annotation on the slot
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._slot_storage_units_cache = {}

    def _slot_storage_units(self, schema_view: SchemaView, slot_name: str) -> Optional[list[str]]:
        """Get allowed storage_units for a slot."""
        if slot_name in self._slot_storage_units_cache:
            return self._slot_storage_units_cache[slot_name]

        slot = schema_view.get_slot(slot_name)
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

    def process(self, instance: Any, context: ValidationContext) -> Iterator[ValidationResult]:
        """Perform NMDC-specific schema validation on the provided instance

        :param instance: The instance to validate
        :param context: The validation context which provides a SchemaView artifact
        :return: Iterator over validation results
        :rtype: Iterator[ValidationResult]
        """
        for data_path, quantity_value in _yield_quantity_value_objects(instance):
            # Get the `has_unit` property from the QuantityValue instance. If it is missing, yield a
            # validation error and continue. This is slightly redundant with JSON Schema validation,
            # but it ensures that we do not attempt further validation on the instance.
            unit = quantity_value.get("has_unit")
            str_data_path = '/'.join(str(p) for p in data_path)
            if unit is None:
                yield ValidationResult(
                    type="nmdc-schema validation",
                    severity=Severity.ERROR,
                    instance=instance,
                    instantiates=context.target_class,
                    message=f"QuantityValue at /{str_data_path} is missing required 'has_unit' property",
                )
                continue

            # Find the slot name by looking for the last string in the data path. If one cannot be
            # found, skip further validation because we cannot determine the relevant slot.
            try:
                slot_name = next(key for key in reversed(data_path) if isinstance(key, str))
            except StopIteration:
                continue

            storage_units = self._slot_storage_units(context.schema_view, slot_name)
            if storage_units and unit not in storage_units:
                yield ValidationResult(
                    type="nmdc-schema validation",
                    severity=Severity.ERROR,
                    instance=instance,
                    instantiates=context.target_class,
                    message=(
                        f"QuantityValue at /{str_data_path} has unit '{unit}' which is not allowed for "
                        f"slot '{slot_name}' (allowed: {', '.join(storage_units)})"
                    )
                )
