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


def _yield_ontology_class_objects(
    data: Any,
    ontology_class_types: set[str],
    target_is_ontology_class: bool = False,
    path: Optional[list[Union[str, int]]] = None,
) -> Iterator[tuple[list[Union[str, int]], dict[str, Any]]]:
    """Recursively yield OntologyClass (and subclass) objects from data."""
    if path is None:
        path = []
    if isinstance(data, dict):
        if data.get("type") in ontology_class_types or (not path and target_is_ontology_class):
            yield path, data
        for key, value in data.items():
            yield from _yield_ontology_class_objects(
                value, ontology_class_types, False, path + [key]
            )
    elif isinstance(data, list):
        for i, item in enumerate(data):
            yield from _yield_ontology_class_objects(
                item, ontology_class_types, False, path + [i]
            )


class NmdcSchemaValidationPlugin(ValidationPlugin):
    """A validation plugin which validates instances using NMDC-specific validation logic.

    This plugin is designed to be used as a part of LinkML's validation framework and in conjunction
    with the `JsonSchemaValidationPlugin` provided by LinkML. This plugin performs the following
    additional checks:

      1. Ensure that values for slots with range `QuantityValue` have a `unit` property that is in
         agreement with the `storage_unit` annotation on the slot
      2. Ensure that `OntologyClass` (and subclass) `id` values use a prefix declared by the schema
         and do not repeat that prefix with an underscore at the start of the local part
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._slot_storage_units_cache = {}
        self._declared_prefixes_cache: dict[int, set[str]] = {}
        self._ontology_class_names_cache: dict[int, set[str]] = {}
        self._ontology_class_types_cache: dict[int, set[str]] = {}

    def _declared_prefixes(self, schema_view: SchemaView) -> set[str]:
        """Return the set of prefix names explicitly declared by the schema and its imports."""
        cache_key = id(schema_view.schema)
        if cache_key not in self._declared_prefixes_cache:
            prefixes: set[str] = set()
            for schema in schema_view.all_schema():
                if schema.prefixes:
                    prefixes.update(schema.prefixes.keys())
            self._declared_prefixes_cache[cache_key] = prefixes
        return self._declared_prefixes_cache[cache_key]

    def _ontology_class_info(self, schema_view: SchemaView) -> tuple[set[str], set[str]]:
        """Return (class_names, class_type_curies) for OntologyClass and its descendants."""
        cache_key = id(schema_view.schema)
        if cache_key not in self._ontology_class_names_cache:
            names = set(schema_view.class_descendants("OntologyClass"))
            type_curies: set[str] = set()
            for name in names:
                cls = schema_view.get_class(name)
                if cls and cls.class_uri:
                    type_curies.add(str(cls.class_uri))
                else:
                    type_curies.add(f"nmdc:{name}")
            self._ontology_class_names_cache[cache_key] = names
            self._ontology_class_types_cache[cache_key] = type_curies
        return (
            self._ontology_class_names_cache[cache_key],
            self._ontology_class_types_cache[cache_key],
        )

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

        declared_prefixes = self._declared_prefixes(context.schema_view)
        ontology_class_names, ontology_class_types = self._ontology_class_info(
            context.schema_view
        )
        target_is_ontology_class = context.target_class in ontology_class_names
        for data_path, term_obj in _yield_ontology_class_objects(
            instance, ontology_class_types, target_is_ontology_class
        ):
            term_id = term_obj.get("id")
            if not isinstance(term_id, str) or ":" not in term_id:
                continue
            prefix, local_id = term_id.split(":", 1)
            str_data_path = "/".join(str(p) for p in data_path)
            if prefix not in declared_prefixes:
                yield ValidationResult(
                    type="nmdc-schema validation",
                    severity=Severity.ERROR,
                    instance=instance,
                    instantiates=context.target_class,
                    message=(
                        f"OntologyClass at /{str_data_path} has id '{term_id}' "
                        f"with undeclared prefix '{prefix}'"
                    ),
                )
            if local_id.lower().startswith(f"{prefix.lower()}_"):
                yield ValidationResult(
                    type="nmdc-schema validation",
                    severity=Severity.ERROR,
                    instance=instance,
                    instantiates=context.target_class,
                    message=(
                        f"OntologyClass at /{str_data_path} has id '{term_id}' "
                        f"whose local part repeats its prefix '{prefix}'"
                    ),
                )
