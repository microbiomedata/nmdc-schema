from nmdc_schema.migrators.migrator_base import MigratorBase
import sys
from pathlib import Path

# For importing ProductionUnitsValidator and materialized yaml
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from units.validate_production_units import ProductionUnitsValidator





##TODO: CURRENTLY ONLY LOOKS AT BIOSAMPLE

## IM HERE: trying to figure out why all these tests are passing when they shouldn't






class Migrator(MigratorBase):
    r'''Migrates a database between two schemas.'''

    _from_version = '11.11.0.part_2'
    _to_version = '11.11.0.part_3'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the validator with the schema file
        schema_file = Path('nmdc_schema/nmdc_materialized_patterns.yaml')
        self.validator = ProductionUnitsValidator(schema_file)

    def upgrade(self,commit_changes: bool = False) -> None:
        r'''
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        '''
        
        self.adapter.do_for_each_document(
            'biosample_set', self.confirm_units_fit_unitenum_and_storage_units
        )

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
        ValueError: Document test2 has invalid unit 'invalid_unit' for slot 'temp': Unit not in UnitEnum
        
        # Test: unit not allowed for specific slot's storage_units
        >>> invalid_biosample_storage = {
        ...     "id": "test3",
        ...     "type": "nmdc:Biosample", 
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "meter",  # Wrong unit type for temperature
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(invalid_biosample_storage)
        Traceback (most recent call last):
            ...
        ValueError: Document test3 has invalid unit 'meter' for slot 'temp': Unit 'meter' not in allowed storage_units for slot 'temp'

        '''
        
        document_id = document.get("id")
        
        # Find all QuantityValue objects in this document using the imported validator
        for path, qv_data in self.validator.iter_quantity_values(document):
            has_unit = qv_data.get('has_unit')
            if not has_unit:
                continue
                
            # Extract slot name from path using the imported method
            slot_name = self.validator.extract_slot_from_path(path)
            if not slot_name:
                continue
            
            # First validate against UnitEnum using the imported method
            if not self.validator.validate_has_unit_against_enum(has_unit):
                raise ValueError(
                    f"Document {document_id} has invalid unit '{has_unit}' for slot '{slot_name}': Unit not in UnitEnum"
                )
            
            # Then validate against storage_units constraints using the imported method
            is_valid, message = self.validator.validate_has_unit_against_slot(has_unit, slot_name)
            if not is_valid:
                raise ValueError(
                    f"Document {document_id} has invalid unit '{has_unit}' for slot '{slot_name}': {message}"
                )