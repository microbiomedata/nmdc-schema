from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import create_schema_view
from pymongo.client_session import ClientSession


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

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        
        This migration ensures that all QuantityValue instances in records have non-null has_unit values.
        All operations are wrapped in a MongoDB transaction for atomicity and rollback capability.
        """
        # Get schema view to find all classes and their slots with QuantityValue range
        view = create_schema_view()
        
        # Find all classes that have slots with QuantityValue range
        classes_with_quantity_value_slots = self._get_classes_with_quantity_value_slots(view)
        
        # Use MongoDB transactions for atomicity
        with self.adapter._db.client.start_session() as session:
            with session.start_transaction():
                try:
                    self.logger.info("Starting migration with transaction support")
                    self._process_collections_with_transaction(classes_with_quantity_value_slots, session)
                    self.logger.info("Migration completed successfully")
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
            collection = self.adapter._db.get_collection(collection_name)
            
            # Process each document in the collection
            for document in collection.find({}, session=session):
                original_document = document.copy()
                modified_document = self.ensure_quantity_value_has_unit(document, slots, class_uri)
                
                # Only update if the document was actually modified
                if modified_document != original_document:
                    collection.replace_one(
                        {"_id": document["_id"]}, 
                        modified_document, 
                        session=session
                    )
    

    def _get_classes_with_quantity_value_slots(self, view) -> dict:
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
        Adds an appropriate unit to a QuantityValue instance if it doesn't have one.
        
        Args:
            quantity_value (dict): A QuantityValue instance that may be missing a has_unit field
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
        """
        # Check if has_unit is missing or is None
        if 'has_unit' not in quantity_value or quantity_value['has_unit'] is None:
            # Get the appropriate unit from the mapping
            unit = self._get_unit_for_class_slot(class_uri, slot_name)
            quantity_value['has_unit'] = unit
            
            # Log the modification for tracking
            self.logger.info(f"Added unit '{unit}' to QuantityValue in {class_uri}.{slot_name}: "
                             f"{quantity_value.get('has_raw_value', 'no raw value')}")
    
    def _get_unit_for_class_slot(self, class_uri: str, slot_name: str) -> str:
        r"""
        Gets the appropriate unit for a given class and slot combination.
        
        Args:
            class_uri (str): The class URI (e.g., "nmdc:Biosample")
            slot_name (str): The slot name (e.g., "temp")
            
        Returns:
            str: The appropriate unit, or a generic unit if no mapping is found
        """
        # Look up the unit in the mapping
        class_units = self.QUANTITY_VALUE_UNITS.get(class_uri, {})
        unit = class_units.get(slot_name)
        
        if unit:
            return unit
        else:
            # Fallback to a generic unit if no mapping is found
            self.logger.warning(f"No unit mapping found for {class_uri}.{slot_name}, using generic unit")
            return "UO:0000000"  # Generic unit ontology term
