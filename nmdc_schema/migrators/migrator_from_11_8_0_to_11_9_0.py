from adapters.adapter_base import AdapterBase
from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import create_schema_view
from nmdc_schema.migrators.utils.migration_reporter import create_immediate_reporter
from pymongo.client_session import ClientSession
from typing import Optional
import logging


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0"
    _to_version = "11.9.0"

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
            "nitrite_nitrogen": "mg/kg",
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
        self._valid_enum_values = None
        self.reporter = None

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        
        This migration ensures that all QuantityValue instances in records have non-null has_unit values.
        All operations are wrapped in a MongoDB transaction for atomicity and rollback capability.
        """
        # Configure logging and initialize generic reporter
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger.setLevel(logging.INFO)
        self.reporter = create_immediate_reporter(self.logger)
        
        # Build unit alias lookup from schema
        self._unit_alias_map = self._build_unit_alias_map()
        
        # Build valid enum values set for quick lookup
        self._valid_enum_values = self._build_valid_enum_values()
        
        # Get schema view to find all classes and their slots with QuantityValue range
        view = create_schema_view()
        
        # Find all classes that have slots with QuantityValue range
        classes_with_quantity_value_slots = self._get_classes_with_quantity_value_slots(view)
        
        self.logger.info(f"Found {len(classes_with_quantity_value_slots)} classes with QuantityValue slots")
        
        # Use MongoDB transactions for atomicity
        db = self.adapter.get_database()
        with db.client.start_session() as session:
            with session.start_transaction():
                try:
                    self.logger.info("Starting migration with transaction support")
                    self._process_collections_with_transaction(classes_with_quantity_value_slots, session)
                    self.reporter.generate_final_report()
                    self.logger.info("Migration completed successfully!")
                except Exception as e:
                    self.logger.error(f"Migration failed, transaction will be rolled back: {e}")
                    raise
    
    def _process_collections_with_transaction(self, classes_with_quantity_value_slots: dict, session: ClientSession) -> None:
        r"""
        Process collections within a MongoDB transaction session.
        
        Args:
            classes_with_quantity_value_slots: Dictionary mapping class names to their QuantityValue slots
            session: MongoDB session for transaction support
        """
        for class_name, slots in classes_with_quantity_value_slots.items():
            collection_name = f"{class_name.lower()}_set"
            class_uri = f"nmdc:{class_name}"
            
            # Get the collection and process documents within the transaction
            db = self.adapter.get_database()
            collection = db.get_collection(collection_name)
            
            # Start collection reporting
            self.reporter.start_collection(collection_name)
            self._current_collection = collection_name
            
            # Process each document in the collection
            docs_in_collection = 0
            docs_updated_in_collection = 0
            
            for document in collection.find({}, session=session):
                docs_in_collection += 1
                original_document = document.copy()
                
                modified_document = self.ensure_quantity_value_has_unit(document, slots, class_uri)
                
                # Only update if the document was actually modified
                if modified_document != original_document:
                    collection.replace_one(
                        {"_id": document["_id"]}, 
                        modified_document, 
                        session=session
                    )
                    docs_updated_in_collection += 1
            
            # End collection reporting
            self.reporter.end_collection(collection_name, docs_in_collection, docs_updated_in_collection)
    

    @staticmethod
    def _get_classes_with_quantity_value_slots(view) -> dict:
        r"""
        Returns a dictionary mapping class names to lists of their slot names that have QuantityValue range.
        
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
                
                if quantity_value_slots:
                    classes_with_quantity_value_slots[class_name] = quantity_value_slots
        
        return classes_with_quantity_value_slots

    @staticmethod
    def _build_unit_alias_map() -> dict:
        r"""
        Builds a mapping from unit aliases to their canonical UCUM values using the schema.
        
        Returns:
            dict: {alias -> canonical_unit} mapping
        """
        alias_to_canonical = {}
        
        # Get schema view to access UnitEnum
        view = create_schema_view()
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

    @staticmethod
    def _build_valid_enum_values() -> set:
        r"""
        Builds a set of valid enum values for quick lookup.
        
        Returns:
            set: Set of valid enum values
        """
        valid_values = set()
        
        # Get schema view to access UnitEnum
        view = create_schema_view()
        unit_enum = view.get_enum('UnitEnum')
        
        if unit_enum and unit_enum.permissible_values:
            for canonical_unit in unit_enum.permissible_values.keys():
                valid_values.add(canonical_unit)
        
        return valid_values

    def ensure_quantity_value_has_unit(self, document: dict, quantity_value_slots: list, class_uri: str) -> dict:
        r"""
        Ensures that all QuantityValue instances in a document have non-null has_unit values.
        
        This function iterates through the specified slots that contain QuantityValue instances
        and adds appropriate units based on the class/slot mapping.
        
        Args:
            document (dict): A document from the database
            quantity_value_slots (list): List of slot names that have QuantityValue range
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            
        Returns:
            dict: The modified document with has_unit values added to QuantityValue instances
            
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> m = Migrator(DictionaryAdapter({}))
        >>> m.reporter = type('MockReporter', (), {
        ...     'track_operation': lambda *args: None,
        ...     'track_item': lambda *args: None, 
        ...     'track_value_set': lambda *args: None
        ... })()
        >>> m._unit_alias_map = {"Celsius": "Cel"}
        >>> m._valid_enum_values = {"Cel", "Celsius"}
        >>> doc = {"temp": {"type": "nmdc:QuantityValue", "has_numeric_value": 25.0}}
        >>> result = m.ensure_quantity_value_has_unit(doc, ["temp"], "nmdc:Biosample")
        >>> result["temp"]["has_unit"]
        'Cel'
        >>> doc_with_unit = {"temp": {"type": "nmdc:QuantityValue", "has_numeric_value": 25.0, "has_unit": "Celsius"}}
        >>> result = m.ensure_quantity_value_has_unit(doc_with_unit, ["temp"], "nmdc:Biosample")
        >>> result["temp"]["has_unit"]
        'Cel'
        """
        
        # Iterate through only the slots that are known to have QuantityValue range
        for slot_name in quantity_value_slots:
            if slot_name in document:
                field_value = document[slot_name]
                
                if isinstance(field_value, dict):
                    # Check if this is a QuantityValue instance
                    if field_value.get('type') == 'nmdc:QuantityValue':
                        self._add_unit_to_quantity_value(field_value, class_uri, slot_name)
                elif isinstance(field_value, list):
                    # Handle lists that might contain QuantityValue instances
                    for item in field_value:
                        if isinstance(item, dict) and item.get('type') == 'nmdc:QuantityValue':
                            self._add_unit_to_quantity_value(item, class_uri, slot_name)
        
        return document
    
    def _add_unit_to_quantity_value(self, quantity_value: dict, class_uri: str, slot_name: str) -> None:
        r"""
        Adds an appropriate unit to a QuantityValue instance if it doesn't have one,
        or normalizes existing unit values using UnitEnum aliases.
        
        Args:
            quantity_value (dict): A QuantityValue instance that may be missing a has_unit field
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
        """
        # Check if has_unit is missing or is None
        if 'has_unit' not in quantity_value or quantity_value['has_unit'] is None:
            # Get the appropriate unit from the mapping
            unit = self._get_unit_for_class_slot(class_uri, slot_name, None)
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
                # Check if it's already a valid enum value using cached values
                if current_unit in self._valid_enum_values:
                    # Unit is already a valid enum value, no action needed
                    pass
                else:
                    # Current unit is not a valid enum value, check if it can be mapped
                    self._get_unit_for_class_slot(class_uri, slot_name, current_unit)
                    # If no mapping found, just report it but don't change the value
    
    def _get_unit_for_class_slot(self, class_uri: str, slot_name: str, current_unit_value: str = None) -> Optional[str]:
        r"""
        Gets the appropriate unit for a given class and slot combination.
        
        Args:
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
            current_unit_value (str, optional): The current unit value that couldn't be mapped
            
        Returns:
            str or None: The appropriate unit, or None if no mapping is found
            
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> m = Migrator(DictionaryAdapter({}))
        >>> m.reporter = type('MockReporter', (), {
        ...     'track_item': lambda *args: None, 
        ...     'track_value_set': lambda *args: None
        ... })()
        >>> m._get_unit_for_class_slot("nmdc:Biosample", "temp")
        'Cel'
        >>> m._get_unit_for_class_slot("nmdc:Biosample", "calcium")
        'mg/kg'
        >>> m._get_unit_for_class_slot("nmdc:Biosample", "unknown_slot") is None
        True
        >>> m._get_unit_for_class_slot("nmdc:UnknownClass", "temp") is None
        True
        """
        # Look up the unit in the mapping
        class_units = self.QUANTITY_VALUE_UNITS.get(class_uri, {})
        unit = class_units.get(slot_name)
        
        if unit:
            return unit
        else:
            # Only track as unmapped if the current unit value is not already valid
            if current_unit_value is not None and current_unit_value not in self._valid_enum_values:
                # Track unmapped slots and values using the generic reporter
                slot_key = f"{class_uri}.{slot_name}"
                self.reporter.track_item('unmapped_slots', slot_key)
                self.reporter.track_value_set('unmapped_values', slot_key, current_unit_value)
            
            # Return None instead of a fallback unit - just report and don't update
            return None
