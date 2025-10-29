from linkml.validator import Validator

from nmdc_schema.migrators.migrator_base import MigratorBase
import sys
from pathlib import Path
from nmdc_schema.migrators.helpers import create_schema_view, get_classes_with_slots_by_range, \
    get_database_collections_for_class
from nmdc_schema import NmdcSchemaValidationPlugin

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class Migrator(MigratorBase):
    r"""A check-only migrator that raises an exception if any QuantityValue's has_unit slot
    is not valid against the slot's storage_unit or UnitEnum constraints."""

    _from_version = '11.13.0.part_1'
    _to_version = '11.13.0.part_2'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.schema_view = create_schema_view()
        self.validator = Validator(
            self.schema_view.schema,
            # This is intentionally *only* using the NMDC plugin, because this migrator is *only*
            # concerned with validating the QuantityValue-related constraints that the plugin
            # implements.
            validation_plugins=[
                NmdcSchemaValidationPlugin()
            ]
        )

    def upgrade(self, commit_changes: bool = False) -> None:
        r'''
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        '''

        # Get the schema classes which have slots with range QuantityValue
        classes_with_qv_slots = get_classes_with_slots_by_range(self.schema_view, 'QuantityValue')

        # Get the Database collection names that can hold these classes
        eligible_collection_names = set()
        for class_name in classes_with_qv_slots.keys():
            collection_names = get_database_collections_for_class(self.schema_view, class_name)
            eligible_collection_names.update(collection_names)

        # Apply migrator through collections
        self.logger.info("Checking QuantityValue units against UnitEnum and storage_units constraints")
        for collection_name in eligible_collection_names:
            self.logger.info(f"  Checking collection '{collection_name}'")
            self.adapter.do_for_each_document(collection_name, self.confirm_units_fit_unitenum_and_storage_units)

    def confirm_units_fit_unitenum_and_storage_units(self, document: dict) -> None:
        r'''
        Raise an exception if the QuantityValue's has_unit slot is not valid against slot's storage_unit or UnitEnum constraints.

        >>> m = Migrator()

        # Test: valid QuantityValue with proper units in biosample
        >>> valid_biosample = {
        ...     "id": "test1",
        ...     "type": "nmdc:Biosample",
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "Cel",
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(valid_biosample)  # Should not raise

        # Test: invalid unit not in UnitEnum
        >>> invalid_biosample_enum = {
        ...     "id": "test2",
        ...     "type": "nmdc:Biosample",
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "invalid_unit",
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(invalid_biosample_enum)
        Traceback (most recent call last):
            ...
        ValueError: In test2:
          QuantityValue at /temp has unit 'invalid_unit' which is not allowed for slot 'temp' (allowed: Cel)

        # Test: unit not allowed for specific slot's storage_units
        >>> invalid_biosample_storage = {
        ...     "id": "test3",
        ...     "type": "nmdc:Biosample",
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "m",  # Wrong unit type for temperature
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(invalid_biosample_storage)
        Traceback (most recent call last):
            ...
        ValueError: In test3:
          QuantityValue at /temp has unit 'm' which is not allowed for slot 'temp' (allowed: Cel)
        '''

        document_id = document.get('id', '<unknown id>')
        document_type = document.get('type')
        if not document_type:
            raise ValueError(f"Unable to infer target_class for document with id '{document_id}'")
        target_class = document_type.replace('nmdc:', '')
        report = self.validator.validate(document, target_class)
        if report.results:
            raise ValueError(f"In {document_id}:\n" + "\n".join("  " + result.message for result in report.results))
