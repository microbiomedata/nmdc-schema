from nmdc_schema.migrators.adapters.adapter_base import AdapterBase
from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import create_schema_view, logger
from nmdc_schema.migrators.migration_reporter import (
    MigrationReporter, 
    get_most_specific_class_for_reporting,
    parse_schema_path,
    get_clean_schema_path,
    resolve_class_from_schema_path
)
from typing import Optional, List, Any
from functools import lru_cache
import logging

# Constants for schema traversal
DATABASE_CLASS_NAME = "Database"
# Configure logging and initialize generic reporter
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger.setLevel(logging.INFO)

@lru_cache
def get_collection_names_with_qv_slots_from_schema() -> List[str]:
    """
    Returns the names of the slots of the `Database` class that describe database collections
    and whose range classes could potentially contain QuantityValue objects.

    This method is vendored in from nmdc-runtime because we would rather not introduce a circular dependency.
    # TODO: consider moving migrators to runtime.

    Source: https://github.com/microbiomedata/refscan/blob/af092b0e068b671849fe0f323fac2ed54b81d574/refscan/lib/helpers.py#L31
    """
    collection_names = []

    schema_view = create_schema_view()
    for slot_name in schema_view.class_slots(DATABASE_CLASS_NAME):
        slot_definition = schema_view.induced_slot(slot_name, DATABASE_CLASS_NAME)

        if slot_definition.multivalued and slot_definition.inlined_as_list:
            # Only include collections whose range classes could contain QuantityValue objects
            if _collection_could_contain_quantity_values(schema_view, slot_definition.range):
                collection_names.append(slot_name)

    collection_names = list(set(collection_names))

    return collection_names


def _collection_could_contain_quantity_values(schema_view, range_class: str) -> bool:
    """
    Determines if a collection's range class could contain QuantityValue objects.
    
    Args:
        schema_view: SchemaView instance
        range_class: The range class name (e.g., "Biosample", "MaterialProcessing")
        
    Returns:
        bool: True if the class or any of its subclasses have QuantityValue slots
    """

    # Check if this class has any QuantityValue slots
    class_slots = schema_view.class_induced_slots(range_class)
    for slot_def in class_slots:
        if slot_def.range == "QuantityValue":
            return True

        # Check if any of its descendants have QuantityValue slots
        descendants = schema_view.class_descendants(range_class)
        for desc_class in descendants:
            desc_slots = schema_view.class_induced_slots(desc_class)
            for slot_def in desc_slots:
                if slot_def.range == "QuantityValue":
                    return True
    return False


class Migrator(MigratorBase):
    r"""
    Migrates a database between schemas 11.9.1 and 11.10.0.
    
    This migrator ensures that all QuantityValue instances have proper UCUM units.
    It handles missing units, normalizes existing units, and applies special case conversions.
    
    Examples:
    
    >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
    >>> import logging
    >>> logging.basicConfig(level=logging.WARNING)  # Suppress output for doctest
    >>> 
    >>> # Test missing unit addition
    >>> database = {
    ...     "biosample_set": [
    ...         {
    ...             "id": "nmdc:bsm-test1",
    ...             "type": "nmdc:Biosample", 
    ...             "temp": {"type": "nmdc:QuantityValue", "has_raw_value": "25"}
    ...         }
    ...     ]
    ... }
    >>> m = Migrator(DictionaryAdapter(database))
    >>> # Initialize required dependencies for standalone testing
    >>> from nmdc_schema.migrators.helpers import create_schema_view
    >>> from nmdc_schema.migrators.migration_reporter import MigrationReporter
    >>> from nmdc_schema.migrators.migration_reporter import get_most_specific_class_for_reporting
    >>> from nmdc_schema.migrators.migration_reporter import parse_schema_path
    >>> from nmdc_schema.migrators.migration_reporter import get_clean_schema_path
    >>> from nmdc_schema.migrators.migration_reporter import resolve_class_from_schema_path
    >>> m._schema_view = create_schema_view()
    >>> m._unit_alias_map = m._build_unit_alias_map(m._schema_view)
    >>> m.reporter = MigrationReporter(m.logger)
    >>> doc = m.ensure_quantity_value_has_unit(database["biosample_set"][0])
    >>> doc["temp"]["has_unit"]
    'Cel'
    
    >>> # Test unit normalization (Celsius -> Cel)
    >>> database2 = {
    ...     "biosample_set": [
    ...         {
    ...             "id": "nmdc:bsm-test2",
    ...             "type": "nmdc:Biosample",
    ...             "temp": {"type": "nmdc:QuantityValue", "has_raw_value": "30", "has_unit": "Celsius"}
    ...         }
    ...     ]
    ... }
    >>> m2 = Migrator(DictionaryAdapter(database2))
    >>> # Initialize required dependencies for standalone testing
    >>> m2._schema_view = create_schema_view()
    >>> m2._unit_alias_map = m2._build_unit_alias_map(m2._schema_view)
    >>> m2.reporter = MigrationReporter(m2.logger)
    >>> doc2 = m2.ensure_quantity_value_has_unit(database2["biosample_set"][0])
    >>> doc2["temp"]["has_unit"]
    'Cel'
    
    >>> # Test carb_nitro_ratio special case (dimensionless)
    >>> database3 = {
    ...     "biosample_set": [
    ...         {
    ...             "id": "nmdc:bsm-test3", 
    ...             "type": "nmdc:Biosample",
    ...             "carb_nitro_ratio": {"type": "nmdc:QuantityValue", "has_raw_value": "12.5"}
    ...         }
    ...     ]
    ... }
    >>> m3 = Migrator(DictionaryAdapter(database3))
    >>> # Initialize required dependencies for standalone testing
    >>> m3._schema_view = create_schema_view()
    >>> m3._unit_alias_map = m3._build_unit_alias_map(m3._schema_view)
    >>> m3.reporter = MigrationReporter(m3.logger)
    >>> doc3 = m3.ensure_quantity_value_has_unit(database3["biosample_set"][0])
    >>> doc3["carb_nitro_ratio"]["has_unit"]
    '1'
    
    >>> # Test nested QuantityValue (PortionOfSubstance)
    >>> database4 = {
    ...     "biosample_set": [
    ...         {
    ...             "id": "nmdc:bsm-test4",
    ...             "type": "nmdc:Biosample",
    ...             "substances_used": [
    ...                 {
    ...                     "type": "nmdc:PortionOfSubstance",
    ...                     "volume": {"type": "nmdc:QuantityValue", "has_raw_value": "10"}
    ...                 }
    ...             ]
    ...         }
    ...     ]
    ... }
    >>> m4 = Migrator(DictionaryAdapter(database4))
    >>> # Initialize required dependencies for standalone testing
    >>> m4._schema_view = create_schema_view()
    >>> m4._unit_alias_map = m4._build_unit_alias_map(m4._schema_view)
    >>> m4.reporter = MigrationReporter(m4.logger)
    >>> doc4 = m4.ensure_quantity_value_has_unit(database4["biosample_set"][0])
    >>> doc4["substances_used"][0]["volume"]["has_unit"]
    'mL'
    """

    _from_version = "11.9.1"
    _to_version = "11.10.0.part_1"

    # Mapping of class/slot combinations to their appropriate UCUM units
    QUANTITY_VALUE_UNITS = {
        "nmdc:PortionOfSubstance": {
            "final_concentration": "%",
            "volume": "mL"
        },
        "nmdc:Biosample": {
            "humidity": "%",
            "tot_carb": "%",
            "tot_nitro_content": "%",
            "samp_store_temp": "Cel",
            "temp": "Cel",
            "avg_temp": "Cel",
            "host_height": "cm",
            "host_age": "d",
            "host_dry_mass": "g",
            "samp_size": "g",
            "abs_air_humidity": "kPa",
            "depth": "m",
            "wind_speed": "m/s",
            "subsurface_depth": "m",
            "ammonium_nitrogen": "mg/kg",
            "calcium": "mg/kg",
            "magnesium": "mg/kg",
            "manganese": "mg/kg",
            "nitrate_nitrogen": "mg/kg",
            "nitrite_nitrogen": "mg/g",
            "potassium": "mg/kg",
            "zinc": "mg/kg",
            "ammonium": "mg/L",
            "chloride": "mg/L",
            "diss_inorg_carb": "mg/L",
            "diss_inorg_nitro": "mg/L",
            "diss_iron": "mg/L",
            "diss_org_carb": "mg/L",
            "diss_oxygen": "mg/L",
            "sodium": "mg/L",
            "soluble_react_phosp": "mg/L",
            "sulfate": "mg/L",
            "tot_org_carb": "mg/L",
            "tot_phosp": "mg/L",
            "nitro": "%",
            "org_carb": "%",
            "tot_nitro": "%",
            "lbc_thirty": "[ppm]",
            "lbceq": "[ppm]",
            "photon_flux": "[arb'U]{micro_Einsteins}/m2/s",
            "conduc": "uS/cm",
            "solar_irradiance": "W/m2",
            "chlorophyll": "micromol/L"
        },
        "nmdc:ChemicalConversionProcess": {
            "temperature": "Cel",
            "duration": "h"
        },
        "nmdc:ChromatographyConfiguration": {
            "temperature": "Cel"
        },
        "nmdc:Extraction": {
            "input_mass": "g"
        },
        "nmdc:SubSamplingProcess": {
            "mass": "g"
        },
        "nmdc:MobilePhaseSegment": {
            "duration": "min"
        }
    }

    def __init__(self, adapter: Optional[AdapterBase] = None, logger=None):
        super().__init__(adapter, logger)
        self._unit_alias_map = None
        self.reporter: Optional[MigrationReporter] = None
        self._schema_view = None  # Cache schema view to avoid repeated creation

    def upgrade(self, commit_changes: bool = False) -> None:
        """
        Migrates all QuantityValue instances in records to have non-null has_unit values conformant to enumeration PVs.

        All operations are wrapped in a MongoDB transaction for rollback capability.
        All actions are logged in a reporter class so that we can see some statistics at the end of the migration.
        
        Args:
            commit_changes: If True, commits the transaction. If False (default), rolls back the transaction.
        """
        self.reporter = MigrationReporter(self.logger)
        
        # Get schema view to find all classes and their slots with QuantityValue range
        self._schema_view = create_schema_view()
        
        # Build unit alias map from UnitEnum (an enumeration of possible UCUM units that we use to harmonize units
        # that already exist in the database).
        self._unit_alias_map = self._build_unit_alias_map(self._schema_view)
        
        # Get the actual collection names from the Database class slots
        real_collection_names = get_collection_names_with_qv_slots_from_schema()
        
        # Warn user if commit_changes parameter is being ignored
        self._warn_if_commit_ignored(commit_changes)
        
        # Use adapter's transaction-aware processing method
        if isinstance(self.adapter, MongoAdapter):
            # MongoDB adapter - use transaction support
            try:
                self.adapter.process_collections_in_transaction(
                    collection_names=real_collection_names,
                    document_processor=self.ensure_quantity_value_has_unit,
                    commit_changes=False  # Always process without committing first
                )
                
                self.reporter.generate_final_report()
                
                # Validate migration success - raises exception if issues found
                self.reporter.validate_migration_success()
                
                # If validation passes and commit requested, commit the transaction
                if commit_changes:
                    # Re-run with commit=True since validation passed
                    self.adapter.process_collections_in_transaction(
                        collection_names=real_collection_names,
                        document_processor=self.ensure_quantity_value_has_unit,
                        commit_changes=True
                    )
                    self.logger.info("Migration validation passed. Transaction committed (changes have been saved)")
                else:
                    self.logger.info("Migration validation passed. Transaction rolled back (no changes were committed)")
                    
            except Exception as e:
                # Log rollback message with commit context
                if commit_changes:
                    self.logger.info("Migration validation failed. Transaction automatically rolled back (no changes were saved, despite commit request)")
                else:
                    self.logger.info("Migration validation failed. Transaction rolled back (no changes were committed)")
                self.logger.error(f"Migration failed: {e}")
                raise
        else:
            # Non-MongoDB adapter - process collections directly without transactions
            try:
                for collection_name in real_collection_names:
                    self.adapter.process_each_document(collection_name, [self.ensure_quantity_value_has_unit])
                
                self.reporter.generate_final_report()
                
                # Validate migration success - raises exception if issues found
                self.reporter.validate_migration_success()
                
                if not commit_changes:
                    self.logger.info("Migration validation passed. Note: Non-MongoDB adapter doesn't support rollback - changes are applied immediately")
                else:
                    self.logger.info("Migration validation passed.")
                    
            except Exception as e:
                # from S&E - raise exceptions if the has_unit can not be set.
                # both for when it can't map, and when it can't assign or has_unit
                self.logger.error(f"Migration failed: {e}")
                raise
    

    @staticmethod
    def _get_classes_with_quantity_value_slots(view) -> dict:
        r"""
        Returns a dictionary mapping class names to lists of their slot names that have QuantityValue range.
        For each class, includes slots from the class AND all its subclasses to handle polymorphic storage.
        
        Args:
            view: SchemaView instance
            
        Returns:
            dict: {class_name: [slot_names_with_quantity_value_range]}
        """
        classes_with_quantity_value_slots = {}
        
        # Get all classes in the schema
        for class_name in view.all_classes():
            class_def = view.get_class(class_name)
            if class_def:
                # Get all slots for this class
                induced_slots = view.class_induced_slots(class_name)
                quantity_value_slots = set()
                
                for slot_def in induced_slots:
                    if slot_def.range == "QuantityValue":
                        quantity_value_slots.add(slot_def.name)
                
                # Also get QuantityValue slots from all subclasses
                # This handles polymorphic storage where subclass records are stored in parent collections in mongodb
                subclass_slots = set()
                try:
                    descendants = view.class_descendants(class_name)
                    for subclass_name in descendants:
                        subclass_induced_slots = view.class_induced_slots(subclass_name)
                        for slot_def in subclass_induced_slots:
                            if slot_def.range == "QuantityValue":
                                subclass_slots.add(slot_def.name)
                except:
                    # If class_descendants doesn't exist, skip subclass processing
                    pass
                
                # Combine parent and subclass slots
                all_slots = set(quantity_value_slots) | subclass_slots
                
                if all_slots:
                    classes_with_quantity_value_slots[class_name] = list(all_slots)
        
        return classes_with_quantity_value_slots

    @staticmethod
    def _build_unit_alias_map(view) -> dict:
        r"""
        Builds a mapping from unit aliases to their canonical UCUM values using the schema.
        
        Args:
            view: SchemaView instance
            
        Returns:
            dict: {alias -> canonical_unit} mapping
        """
        alias_to_canonical = {}
        
        # Get UnitEnum from the provided schema view
        unit_enum = view.get_enum('UnitEnum')
        
        if unit_enum and unit_enum.permissible_values:
            for canonical_unit, unit_def in unit_enum.permissible_values.items():
                # The canonical unit maps to itself
                alias_to_canonical[canonical_unit] = canonical_unit
                
                # Add aliases that map to canonical unit
                if hasattr(unit_def, 'aliases') and unit_def.aliases:
                    for alias in unit_def.aliases:
                        alias_to_canonical[alias] = canonical_unit
        
        return alias_to_canonical

    def ensure_quantity_value_has_unit(self, document: dict) -> dict:
        r"""
        Ensures that all QuantityValue instances in a document have non-null has_unit values.
        
        This function recursively traverses the document to find all QuantityValue instances
        and adds appropriate units based on the class/slot mapping.
        
        Args:
            document (dict): A document from the database
            
        Returns:
            dict: The modified document with has_unit values added to QuantityValue instances
        """
        
        # Recursively traverse the entire document to find all QuantityValue instances
        self._traverse_and_fix_quantity_values(document, document_root=document)
        
        return document
    
    def _traverse_and_fix_quantity_values(self,
                                          obj: Any,
                                          document_root: dict,
                                          path: str = "") -> None:
        """
        Recursively traverses an object to find and fix QuantityValue instances.
        
        Args:
            obj: The object to traverse (dict, list, or other)
            document_root: The root document for context (e.g., to get document type)
            path: Current path in the document (for debugging)
        """
        if isinstance(obj, dict):
            # Check if this is a QuantityValue instance
            if obj.get('type') == 'nmdc:QuantityValue':
                # This is a QuantityValue, try to add/fix its unit
                self._fix_quantity_value_unit(obj, document_root, path)
            else:
                # Quick optimization: only recurse into values that could contain QuantityValue objects
                # Skip simple string/number values and common metadata fields
                for key, value in obj.items():
                    if key in ['_id', 'id', 'name', 'description', 'type'] and isinstance(value, str):
                        continue  # Skip simple string metadata
                    if isinstance(value, (int, float, bool)) or value is None:
                        continue  # Skip simple scalar values
                    
                    new_path = f"{path}.{key}" if path else key
                    # Recursively traverse into nested objects to find QuantityValue instances
                    # value: the nested object/dict at this key (e.g., {"type": "nmdc:QuantityValue", "has_raw_value": "25"})
                    # document_root: original document for context (e.g., {"id": "biosample1", "type": "nmdc:Biosample", "temp": {...}})
                    # new_path: current location path (e.g., "temp" or "substances_used[0].volume")
                    self._traverse_and_fix_quantity_values(value, document_root, new_path)
        elif isinstance(obj, list):
            # Recurse into list items
            for i, item in enumerate(obj):
                new_path = f"{path}[{i}]"
                self._traverse_and_fix_quantity_values(item, document_root, new_path)
    
    def _fix_quantity_value_unit(self, quantity_value: dict, document_root: dict, path: str) -> None:
        r"""
        Attempts to fix a QuantityValue instance by adding or normalizing its unit.
        
        Args:
            quantity_value: The QuantityValue instance to fix
            document_root: The full document for context
            path: Path to this QuantityValue in the document
        """
        # Get root collection class for reporting (the class that has a MongoDB collection)
        root_collection_class = document_root.get('type', 'nmdc:Unknown')
        # Get clean schema path without array indices for reporting
        clean_schema_path = get_clean_schema_path(path)
        
        # Check if `has_unit` is missing or is None
        if 'has_unit' not in quantity_value or quantity_value['has_unit'] is None:
            # Get most specific class for unit lookup
            most_specific_class = get_most_specific_class_for_reporting(self._schema_view, document_root, path)
            
            # Check for special cases where we can extract unit from raw_value
            unit = self._handle_one_off_unit_cases(quantity_value, most_specific_class, path, None)
            
            # If no special case, try to infer unit from document type and path
            if not unit:
                unit = self._infer_unit_from_context(document_root, path)
            
            if unit:
                quantity_value['has_unit'] = unit
                # Track record update: missing → unit
                self.reporter.track_record_updated(
                    class_name=root_collection_class,
                    slot_name=clean_schema_path, 
                    subclass_type=most_specific_class,
                    source_value="<missing>",
                    target_value=unit
                )
            else:
                # Report missing unit
                self.reporter.track_missing_value(root_collection_class, clean_schema_path)
        else:
            # has_unit exists, check if it needs normalization
            current_unit = quantity_value['has_unit']
            # Get most specific class for unit lookup (for special cases)
            most_specific_class = get_most_specific_class_for_reporting(self._schema_view, document_root, path)
            
            # Check if current unit is an alias that should be normalized
            if current_unit in self._unit_alias_map:
                canonical_unit = self._unit_alias_map[current_unit]
                
                # Only update if the canonical form is different
                if current_unit != canonical_unit:
                    quantity_value['has_unit'] = canonical_unit
                    # Track unit normalization
                    self.reporter.track_record_updated(
                        class_name=root_collection_class,
                        slot_name=clean_schema_path,
                        subclass_type=most_specific_class,
                        source_value=current_unit,
                        target_value=canonical_unit
                    )
                else:
                    # Unit is already in canonical form - track as conformant
                    self.reporter.track_record_processed(
                        class_name=root_collection_class,
                        slot_name=clean_schema_path,
                        subclass_type=most_specific_class,
                        value=current_unit
                    )
            else:
                # Check for special one-off cases
                handled_unit = self._handle_one_off_unit_cases(quantity_value, most_specific_class, path, current_unit)
                if handled_unit:
                    # One-off case was handled - track the change
                    self.reporter.track_record_updated(
                        class_name=root_collection_class,
                        slot_name=clean_schema_path,
                        subclass_type=most_specific_class,
                        source_value=current_unit or "<missing>",
                        target_value=handled_unit
                    )
                else:
                    # Unit is not in the alias map - report it for analysis
                    self.reporter.track_unmapped_value(root_collection_class, clean_schema_path, current_unit)
    
    def _infer_unit_from_context(self, full_document: dict, path: str) -> Optional[str]:
        r"""
        Infers the appropriate unit for a QuantityValue .
        
        Args:
            full_document: The full document for context
            path: Path to the QuantityValue in the document
            
        Returns:
            str or None: The inferred unit, or None if not found
        """
        # Parse path into components, filtering out array indices
        path_parts = parse_schema_path(path)
        if not path_parts:
            return None
        
        field_name = path_parts[-1]
        slot_path = path_parts[:-1]  # All parts except the final field name
        
        # Start with document's root class
        doc_type = full_document.get('type', 'nmdc:Unknown')
        root_class = doc_type.replace('nmdc:', '') if doc_type.startswith('nmdc:') else doc_type
        
        # Use schema to resolve the class context for this field
        target_class = resolve_class_from_schema_path(self._schema_view, root_class, slot_path)
        if target_class:
            return self._get_unit_for_class_slot(f"nmdc:{target_class}", field_name, None)
        
        # Fallback to document type if schema resolution fails
        return self._get_unit_for_class_slot(doc_type, field_name, None)
    
    def _add_unit_to_quantity_value(self, quantity_value: dict, class_uri: str, slot_name: str, full_document: Optional[dict] = None) -> None:
        r"""
        Adds an appropriate unit to a QuantityValue instance if it doesn't have one,
        or normalizes existing unit values using UnitEnum aliases.
        
        Args:
            quantity_value (dict): A QuantityValue instance that may be missing a has_unit field
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
        """
        # Check if the slot has_unit is missing or is None
        if 'has_unit' not in quantity_value or quantity_value['has_unit'] is None:
            # Get the appropriate unit from the mapping
            # Check if document has a specific type that should be used for unit lookup
            lookup_class_uri = class_uri
            if full_document and 'type' in full_document:
                lookup_class_uri = full_document['type']
            
            unit = self._get_unit_for_class_slot(lookup_class_uri, slot_name, None)
            if unit:  # Only update if we found a valid mapping
                quantity_value['has_unit'] = unit
                # Track the unit addition using the generic reporter
                self.reporter.track_operation('units_added', unit, 1)
            
        else:
            # has_unit exists, check if it needs normalization
            current_unit = quantity_value['has_unit']
            
            # Check if current unit is an alias that should be normalized
            if current_unit in self._unit_alias_map:
                canonical_unit = self._unit_alias_map[current_unit]
                
                # Only update if the canonical form is different
                if current_unit != canonical_unit:
                    quantity_value['has_unit'] = canonical_unit
                    
                    # Track the unit normalization using the generic reporter
                    self.reporter.track_operation('units_normalized', f"{current_unit} → {canonical_unit}", 1)
            else:
                # Current unit is not in our alias map
                # Check for special one-off cases first
                if self._handle_one_off_unit_cases(quantity_value, class_uri, slot_name, current_unit):
                    # One-off case was handled, continue to next
                    pass
                elif current_unit in self._unit_alias_map and self._unit_alias_map[current_unit] == current_unit:
                    # Unit is already a valid canonical enum value, no action needed
                    pass
                else:
                    # Current unit is not a valid enum value, check if it can be mapped
                    # Check if document has a specific type that should be used for unit lookup
                    lookup_class_uri = class_uri
                    if full_document and 'type' in full_document:
                        lookup_class_uri = full_document['type']
                    
                    self._get_unit_for_class_slot(lookup_class_uri, slot_name, current_unit)
                    # If no mapping found, just report it but don't change the value
    
    def _handle_one_off_unit_cases(self, quantity_value: dict, class_uri: str, path: str, current_unit: Optional[str]) -> Optional[str]:
        """
        Handle special one-off unit conversion cases.

        In particular, this method handles cases where the unit is missing, and we have already looked at the records
        ahead of time to determine what the unit should be, or where we need to convert a specific unit.
        
        Args:
            quantity_value (dict): The QuantityValue instance to potentially modify
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            path (str): The full path to the QuantityValue field (e.g., "substances_used[0].volume")
            current_unit (str): The current unit value (None if missing)
            
        Returns:
            str or None: The extracted/converted unit, or None if not handled
        """
        # Extract the field name from the path
        slot_name = path.split('.')[-1] if path else ""
        # Handle missing units by extracting from has_raw_value
        if current_unit is None:
            # Special case: Biosample salinity - extract specific units from has_raw_value
            if class_uri == "nmdc:Biosample" and slot_name == "salinity":
                raw_value = quantity_value.get('has_raw_value')
                if raw_value and isinstance(raw_value, str):
                    extracted_unit = self._extract_salinity_unit(raw_value)
                    if extracted_unit:
                        return extracted_unit

            # Special case: Biosample carb_nitro_ratio - set unit to "1" (dimensionless)
            if class_uri == "nmdc:Biosample" and slot_name == "carb_nitro_ratio":
                return "1"
        
        # Handle existing units that need conversion
        else:
            # Special case: Biosample nitrate with "detection" unit should become "umol/L"
            if class_uri == "nmdc:Biosample" and slot_name == "nitrate" and current_unit == "detection":
                quantity_value['has_unit'] = "umol/L"
                return "umol/L"  # Return the unit to indicate it was handled

        return None
    
    def _extract_salinity_unit(self, raw_value: str) -> Optional[str]:
        """
        Extract specific salinity units from a raw value string.
        Only looks for: mgL → mg/L, mg/L → mg/L, % → %
        
        Args:
            raw_value: The raw value string that may contain salinity units
            
        Returns:
            str or None: The normalized unit, or None if not found
        """
        # Look for specific salinity units only
        if 'mgL' in raw_value:
            return 'mg/L'
        elif 'mg/L' in raw_value:
            return 'mg/L'  
        elif '%' in raw_value:
            return '%'
        
        return None
    
    def _get_unit_for_class_slot(self, class_uri: str, slot_name: str, current_unit_value: str = None) -> Optional[str]:
        r"""
        Gets the appropriate unit for a given class and slot combination.
        Also check parent classes in the inheritance hierarchy if no direct mapping is found.
        
        Args:
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
            current_unit_value (str, optional): The current unit value that couldn't be mapped
            
        Returns:
            str or None: The appropriate unit, or None if no mapping is found

        """
        # Look up the unit in the mapping
        class_units = self.QUANTITY_VALUE_UNITS.get(class_uri, {})
        unit = class_units.get(slot_name)
        
        if unit:
            return unit
        
        # If not found, check parent classes in the inheritance hierarchy
        unit = self._get_unit_from_inheritance_chain(class_uri, slot_name)
        if unit:
            return unit
        
        # Only track as unmapped if the current unit value is not already valid
        if current_unit_value is not None and current_unit_value not in self._unit_alias_map:
            # Track unmapped slots and values using the generic reporter
            slot_key = f"{class_uri}.{slot_name}"
            self.reporter.track_item('unmapped_slots', slot_key)
            self.reporter.track_value_set('unmapped_values', slot_key, current_unit_value)
        
        # Return None instead of a fallback unit - just report and don't update
        return None
    
    def _get_unit_from_inheritance_chain(self, class_uri: str, slot_name: str) -> Optional[str]:
        r"""
        Checks parent classes in the inheritance hierarchy for unit mappings.
        
        Args:
            class_uri (str): The class URI (e.g., "nmdc:DissolvingProcess")
            slot_name (str): The slot name (e.g., "volume")
            
        Returns:
            str or None: The appropriate unit from a parent class, or None if not found
        """
        # Use cached schema view to traverse inheritance
        view = self._schema_view
        
        # Remove the "nmdc:" prefix to get the class name
        class_name = class_uri.replace('nmdc:', '')
        
        try:
            # Get the class definition
            class_def = view.get_class(class_name)
            if not class_def:
                return None
                
            # Get all ancestor classes
            ancestors = view.class_ancestors(class_name)
            
            # Check each ancestor for unit mappings
            for ancestor_name in ancestors:
                ancestor_uri = f"nmdc:{ancestor_name}"
                ancestor_units = self.QUANTITY_VALUE_UNITS.get(ancestor_uri, {})
                unit = ancestor_units.get(slot_name)
                if unit:
                    return unit
                    
        except Exception:
            # If anything goes wrong with schema traversal, just return None
            pass
            
        return None
