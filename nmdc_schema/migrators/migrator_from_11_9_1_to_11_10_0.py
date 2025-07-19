from adapters.adapter_base import AdapterBase
from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import create_schema_view, logger
from nmdc_schema.migrators.utils.migration_reporter import create_migration_reporter
from pymongo.client_session import ClientSession
from typing import Optional, Set, Dict, List
from functools import lru_cache
import logging
import copy

# Constants for schema traversal
DATABASE_CLASS_NAME = "Database"
# Configure logging and initialize generic reporter
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger.setLevel(logging.INFO)

@lru_cache
def get_collection_names_from_schema() -> List[str]:
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

        # Filter out any hypothetical (future) slots that don't correspond to a collection (e.g. `db_version`).
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
    if not range_class:
        return False
    
    try:
        # Check if this class has any QuantityValue slots
        class_slots = schema_view.class_induced_slots(range_class)
        for slot_def in class_slots:
            if slot_def.range == "QuantityValue":
                return True
        
        # Check if any of its descendants have QuantityValue slots
        try:
            descendants = schema_view.class_descendants(range_class)
            for desc_class in descendants:
                desc_slots = schema_view.class_induced_slots(desc_class)
                for slot_def in desc_slots:
                    if slot_def.range == "QuantityValue":
                        return True
        except:
            # If class_descendants doesn't exist, skip descendant checking
            pass
            
    except Exception:
        # If anything goes wrong, err on the side of caution and include it
        return True
    
    return False


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.9.1"
    _to_version = "11.10.0"

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
            "chlorophyll": "ug/L"
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

    def __init__(self, adapter: AdapterBase = None, logger=None):
        super().__init__(adapter, logger)
        self._unit_alias_map = None
        self.reporter = None
        self._schema_view = None  # Cache schema view to avoid repeated creation

    def upgrade(self) -> None:
        """
        Migrates all QuantityValue instances in records to have non-null has_unit values conformant to enumeration PVs.

        All operations are wrapped in a MongoDB transaction for atomicity and rollback capability.
        All actions are logged in a reporter class so that we can see some statistics at the end of the migration.
        """
        self.reporter = create_migration_reporter(self.logger)
        
        # Get schema view to find all classes and their slots with QuantityValue range
        self._schema_view = create_schema_view()
        
        # Build unit alias map from UnitEnum (an enumeration of possible UCUM units that we use to harmonize units
        # that already exist in the database).
        self._unit_alias_map = self._build_unit_alias_map(self._schema_view)
        
        # Find all classes that have slots with QuantityValue range
        classes_with_quantity_value_slots = self._get_classes_with_quantity_value_slots(self._schema_view)
        
        # Use MongoDB transactions for atomicity
        db = self.adapter.get_database()
        with db.client.start_session() as session:
            with session.start_transaction():
                try:
                    self._process_collections_with_transaction(classes_with_quantity_value_slots, session)
                    self.reporter.generate_final_report()
                    # Rollback by default after generating report
                    self.logger.info("Rolling back transaction (no changes will be committed)")
                    session.abort_transaction()
                except Exception as e:
                    self.logger.error(f"Migration failed, transaction will be rolled back: {e}")
                    raise
    
    def _process_collections_with_transaction(self, classes_with_quantity_value_slots: dict, session: ClientSession) -> None:
        r"""
        Process collections within a MongoDB transaction session.
        Only processes collections that actually exist in the Database class slots.
        
        Args:
            classes_with_quantity_value_slots: Dictionary mapping class names to their QuantityValue slots
            session: MongoDB session for transaction support
        """
        # Get the actual collection names from the Database class slots
        real_collection_names = get_collection_names_from_schema()
        
        # Process each real collection
        for collection_name in real_collection_names:
            # Get the collection and process documents within the transaction
            db = self.adapter.get_database()
            collection = db.get_collection(collection_name)
            
            # Process each document in the collection
            for document in collection.find({}, session=session):
                original_document = copy.deepcopy(document)
                
                # The recursive traversal will handle all nested QuantityValue objects
                # regardless of their class type, so we don't need to pass specific slots
                modified_document = self.ensure_quantity_value_has_unit(document, [], "", document)
                
                # Only update if the document was actually modified
                if modified_document != original_document:
                    collection.replace_one(
                        {"_id": document["_id"]}, 
                        modified_document, 
                        session=session
                    )

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
                quantity_value_slots = []
                
                for slot_def in induced_slots:
                    if slot_def.range == "QuantityValue":
                        quantity_value_slots.append(slot_def.name)
                
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

    def ensure_quantity_value_has_unit(self, document: dict,
                                       quantity_value_slots: list,
                                       class_uri: str,
                                       full_document: dict = None) -> dict:
        r"""
        Ensures that all QuantityValue instances in a document have non-null has_unit values.
        
        This function recursively traverses the document to find all QuantityValue instances
        and adds appropriate units based on the class/slot mapping.
        
        Args:
            document (dict): A document from the database
            quantity_value_slots (list): List of slot names that have QuantityValue range (unused in new approach)
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            full_document (dict): The full document for context
            
        Returns:
            dict: The modified document with has_unit values added to QuantityValue instances
        """
        
        # Recursively traverse the entire document to find all QuantityValue instances
        self._traverse_and_fix_quantity_values(document, full_document)
        
        return document
    
    def _traverse_and_fix_quantity_values(self,
                                          obj: any,
                                          full_document: dict,
                                          path: str = "") -> None:
        r"""
        Recursively traverses an object to find and fix QuantityValue instances.
        
        Args:
            obj: The object to traverse (dict, list, or other)
            full_document: The full document for context
            path: Current path in the document (for debugging)
        """
        if isinstance(obj, dict):
            # Check if this is a QuantityValue instance
            if obj.get('type') == 'nmdc:QuantityValue':
                # This is a QuantityValue, try to add/fix its unit AND track it
                self._fix_quantity_value_unit(obj, full_document, path)
                self._track_quantity_value_processed(obj, full_document, path)
            else:
                # Quick optimization: only recurse into values that could contain QuantityValue objects
                # Skip simple string/number values and common metadata fields
                for key, value in obj.items():
                    if key in ['_id', 'id', 'name', 'description', 'type'] and isinstance(value, str):
                        continue  # Skip simple string metadata
                    if isinstance(value, (int, float, bool)) or value is None:
                        continue  # Skip simple scalar values
                    
                    new_path = f"{path}.{key}" if path else key
                    self._traverse_and_fix_quantity_values(value, full_document, new_path)
        elif isinstance(obj, list):
            # Recurse into list items
            for i, item in enumerate(obj):
                new_path = f"{path}[{i}]"
                self._traverse_and_fix_quantity_values(item, full_document, new_path)
    
    def _track_quantity_value_processed(self, quantity_value: dict, full_document: dict, path: str) -> None:
        """Track all QuantityValue instances for the summary table."""
        doc_type = full_document.get('type', 'unknown')
        field_name = path.split('.')[-1]
        current_unit = quantity_value.get('has_unit', '<missing>')
        
        # Only track if we have a valid unit (not missing and not unmapped)
        if current_unit != '<missing>':
            # Check if this unit is valid (either canonical or has a mapping)
            if current_unit in self._unit_alias_map:
                # This is a valid unit - track as processed
                self.reporter.track_record_processed(doc_type, field_name, doc_type, current_unit)
    
    def _fix_quantity_value_unit(self, quantity_value: dict, full_document: dict, path: str) -> None:
        r"""
        Attempts to fix a QuantityValue instance by adding or normalizing its unit.
        
        Args:
            quantity_value: The QuantityValue instance to fix
            full_document: The full document for context
            path: Path to this QuantityValue in the document
        """
        # Get context information for reporting
        doc_type = full_document.get('type', 'unknown')
        field_name = path.split('.')[-1]
        
        # Check if `has_unit` is missing or is None
        if 'has_unit' not in quantity_value or quantity_value['has_unit'] is None:
            # Check for special cases where we can extract unit from raw_value
            unit = self._handle_one_off_unit_cases(quantity_value, doc_type, field_name, None)
            
            # If no special case, try to infer unit from document type and path
            if not unit:
                unit = self._infer_unit_from_context(full_document, path)
            
            if unit:
                quantity_value['has_unit'] = unit
                # Track record update: missing → unit
                self.reporter.track_record_updated(
                    class_name=doc_type,
                    slot_name=field_name, 
                    subclass_type=doc_type,
                    source_unit="<missing>",
                    target_unit=unit
                )
            else:
                # Report missing unit
                self.reporter.track_missing_unit(doc_type, field_name)
        else:
            # has_unit exists, check if it needs normalization
            current_unit = quantity_value['has_unit']
            
            # Check if current unit is an alias that should be normalized
            if current_unit in self._unit_alias_map:
                canonical_unit = self._unit_alias_map[current_unit]
                
                # Only update if the canonical form is different
                if current_unit != canonical_unit:
                    quantity_value['has_unit'] = canonical_unit
                    # Track unit normalization
                    self.reporter.track_record_updated(
                        class_name=doc_type,
                        slot_name=field_name,
                        subclass_type=doc_type,
                        source_unit=current_unit,
                        target_unit=canonical_unit
                    )
            else:
                # Check for special one-off cases first
                if self._handle_one_off_unit_cases(quantity_value, doc_type, field_name, current_unit):
                    # One-off case was handled, nothing more to do
                    pass
                elif current_unit in self._unit_alias_map and self._unit_alias_map[current_unit] == current_unit:
                    # Unit is already valid canonical form - track as processed but not updated
                    self.reporter.track_record_processed(doc_type, field_name, doc_type, current_unit)
                else:
                    # Unit is not in the alias map - report it for analysis
                    self.reporter.track_unmapped_unit(doc_type, field_name, current_unit)
    
    def _infer_unit_from_context(self, full_document: dict, path: str) -> Optional[str]:
        r"""
        Attempts to infer the appropriate unit for a QuantityValue based on document context.
        
        Args:
            full_document: The full document for context
            path: Path to the QuantityValue in the document
            
        Returns:
            str or None: The inferred unit, or None if not found
        """
        # Get the document type for context
        doc_type = full_document.get('type', 'nmdc:Unknown')
        
        # Extract the field name from the path
        # e.g., "substances_used[0].volume" -> "volume"
        field_name = path.split('.')[-1]
        
        # Try to find unit mapping
        unit = self._get_unit_for_class_slot(doc_type, field_name, None)
        
        # If not found with document type, try with nested object types
        if not unit:
            # Look for nested object types in the path
            parts = path.split('.')
            for i, part in enumerate(parts):
                if '[' in part:  # This is a list access
                    # Try to find the type of objects in this list
                    list_path = '.'.join(parts[:i+1])
                    obj_type = self._get_nested_object_type(full_document, list_path)
                    if obj_type:
                        unit = self._get_unit_for_class_slot(obj_type, field_name, None)
                        if unit:
                            break
        
        return unit
    
    def _get_nested_object_type(self, document: dict, path: str) -> Optional[str]:
        r"""
        Attempts to get the type of the nested object from a path.
        
        Args:
            document: The document to search
            path: Path to the object (e.g., "substances_used[0]")
            
        Returns:
            str or None: The type of the object, or None if not found
        """
        try:
            # Simple path traversal - could be made more robust
            parts = path.split('.')
            current = document
            
            for part in parts:
                if '[' in part:
                    # Handle array access
                    field_name = part.split('[')[0]
                    index = int(part.split('[')[1].split(']')[0])
                    current = current[field_name][index]
                else:
                    current = current[part]
            
            return current.get('type')
        except (KeyError, IndexError, ValueError):
            return None
    
    def _add_unit_to_quantity_value(self, quantity_value: dict, class_uri: str, slot_name: str, full_document: dict = None) -> None:
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
    
    def _handle_one_off_unit_cases(self, quantity_value: dict, class_uri: str, slot_name: str, current_unit: str) -> Optional[str]:
        """
        Handle special one-off unit conversion cases.

        In particular, this method handles cases where the unit is missing and we have already looked at the records
        ahead of time to determine what the unit should be, or where we need to convert a specific unit.
        
        Args:
            quantity_value (dict): The QuantityValue instance to potentially modify
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "nitrate")
            current_unit (str): The current unit value (None if missing)
            
        Returns:
            str or None: The extracted/converted unit, or None if not handled
        """
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
        Also checks parent classes in the inheritance hierarchy if no direct mapping is found.
        
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
        
        # Remove the nmdc: prefix to get the class name
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
