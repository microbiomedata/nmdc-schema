"""
Simplified migration reporting framework for NMDC schema migrators.

This module provides a streamlined reporting system that generates three specific tables:
1. Records updated table: class_processed, slot_processed, subclass_type, records_updated, source_value, target_value
2. Unmapped values table: class.slot, unmapped_value, total_count
3. Missing values table: class.slot, total_missing
"""

from collections import defaultdict
import logging
from typing import List, Optional

class MigrationReporter:
    """
    Simplified migration reporter that tracks and generates three specific summary tables.
    """
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        
        # Data structures for the three tables
        # {(class, slot, subclass_type, source_value, target_value): {'conformant': count, 'non_conformant': count, 'updated': count}}
        self.records_updated = defaultdict(lambda: {'conformant': 0, 'non_conformant': 0, 'updated': 0})
        # {class_slot: {value: count}}
        self.unmapped_values = defaultdict(lambda: defaultdict(int))
        # {class_slot: count}
        self.missing_values = defaultdict(int)
    
    
    def track_record_updated(self, class_name: str, slot_name: str, subclass_type: str, 
                           source_value: str, target_value: str, count: int = 1) -> None:
        """Track a record update for the first table."""
        key = (class_name, slot_name, subclass_type, source_value, target_value)
        self.records_updated[key]['non_conformant'] += count
        self.records_updated[key]['updated'] += count
    
    def track_record_processed(self, class_name: str, slot_name: str, subclass_type: str, 
                             value: str, count: int = 1) -> None:
        """Track a record that was processed but didn't need updating (already conformant)."""
        key = (class_name, slot_name, subclass_type, value, value)
        self.records_updated[key]['conformant'] += count
    
    def track_unmapped_value(self, class_name: str, slot_name: str, value: str, count: int = 1) -> None:
        """Track an unmapped value that should cause validation failure."""
        class_slot = f"{class_name}.{slot_name}"
        self.unmapped_values[class_slot][value] += count
    
    def track_missing_value(self, class_name: str, slot_name: str, count: int = 1) -> None:
        """Track a missing value that should cause validation failure."""
        class_slot = f"{class_name}.{slot_name}"
        self.missing_values[class_slot] += count
    
    def generate_final_report(self) -> None:
        """Generate the final migration report with three tables."""
        self.logger.info("=" * 80)
        self.logger.info("MIGRATION SUMMARY")
        self.logger.info("=" * 80)
        
        self._generate_records_updated_table()
        self._generate_unmapped_values_table()
        self._generate_missing_values_table()
        
        self.logger.info("=" * 80)
    
    def _generate_records_updated_table(self) -> None:
        """Generate the records updated table."""
        self.logger.info("RECORDS UPDATED")
        self.logger.info("-" * 40)
        
        if not self.records_updated:
            self.logger.info("No records were updated.")
            self.logger.info("")
            return
        
        # Table header with source value before count columns
        header = (f"{'Class':<30} {'SubClassType':<25} {'Slot':<25} "
                 f"{'Source Value':<15} {'Conformant':<12} {'Not':<12} {'Updated':<8} {'Target Value':<15}")
        self.logger.info(header)
        self.logger.info(f"{'':<30} {'':<25} {'':<25} {'':<15} {'':<12} {'Conformant':<12} {'':<8} {'':<15}")
        self.logger.info("-" * 155)
        
        # Sort by class, then slot, then total records (descending)
        sorted_updates = sorted(self.records_updated.items(), 
                              key=lambda x: (x[0][0], x[0][1], -(x[1]['conformant'] + x[1]['non_conformant'])))
        
        for (class_name, slot_name, subclass_type, source_value, target_value), counts in sorted_updates:
            conformant_count = counts['conformant']
            non_conformant_count = counts['non_conformant']
            updated_count = counts['updated']
            
            # If subclass type is the same as class, leave it blank
            display_subclass = "" if subclass_type == class_name else subclass_type
            
            row = (f"{class_name:<30} {display_subclass:<25} {slot_name:<25} "
                   f"{source_value:<15} {conformant_count:<12} {non_conformant_count:<12} {updated_count:<8} {target_value:<15}")
            self.logger.info(row)
        
        self.logger.info("")
    
    def _generate_unmapped_values_table(self) -> None:
        """Generate the unmapped values table."""
        self.logger.info("UNMAPPED VALUES")
        self.logger.info("-" * 40)
        
        if not self.unmapped_values:
            self.logger.info("No unmapped values found.")
            self.logger.info("")
            return
        
        # Table header
        self.logger.info(f"{'Class.Slot':<35} {'Unmapped Value':<20} {'Total Count':<12}")
        self.logger.info("-" * 67)
        
        # Sort by class.slot, then by count (descending)
        for class_slot in sorted(self.unmapped_values.keys()):
            values = self.unmapped_values[class_slot]
            sorted_values = sorted(values.items(), key=lambda x: -x[1])
            
            for value, count in sorted_values:
                self.logger.info(f"{class_slot:<35} {value:<20} {count:<12}")
        
        self.logger.info("")
    
    def _generate_missing_values_table(self) -> None:
        """Generate the missing values table."""
        self.logger.info("MISSING VALUES")
        self.logger.info("-" * 40)
        
        if not self.missing_values:
            self.logger.info("No missing values found.")
            self.logger.info("")
            return
        
        # Table header
        self.logger.info(f"{'Class.Slot':<35} {'Total Missing':<12}")
        self.logger.info("-" * 47)
        
        # Sort by class.slot
        for class_slot in sorted(self.missing_values.keys()):
            count = self.missing_values[class_slot]
            self.logger.info(f"{class_slot:<35} {count:<12}")
        
        self.logger.info("")
    
    def validate_migration_success(self) -> None:
        """
        Validates that the migration was successful by checking for unmapped and missing values.
        Raises a comprehensive exception if any validation issues are found.
        
        Raises:
            ValueError: If unmapped values or missing values are found, indicating migration failure
        """
        errors = []
        
        # Check for unmapped values
        if self.unmapped_values:
            errors.append("UNMAPPED VALUES (units that could not be normalized):")
            for class_slot in sorted(self.unmapped_values.keys()):
                values = self.unmapped_values[class_slot]
                sorted_values = sorted(values.items(), key=lambda x: -x[1])
                for value, count in sorted_values:
                    errors.append(f"  {class_slot}: '{value}' ({count} occurrences)")
        
        # Check for missing values  
        if self.missing_values:
            errors.append("MISSING VALUES (required units that could not be inferred):")
            for class_slot in sorted(self.missing_values.keys()):
                count = self.missing_values[class_slot]
                errors.append(f"  {class_slot}: {count} missing units")
        
        # If any validation errors found, raise exception
        if errors:
            error_message = "Migration validation failed with the following issues:\n\n" + "\n".join(errors)
            error_message += "\n\nAll validation issues must be resolved before the migration can succeed."
            raise ValueError(error_message)


# Generic schema path utilities for migration reporting
def parse_schema_path(path: str) -> List[str]:
    """
    Parses a document path into schema-relevant components, filtering out array indices.

    Args:
        path: Path like "substances_used[0].volume" or "extraction.input_mass"

    Returns:
        List of schema slot names: ["substances_used", "volume"] or ["extraction", "input_mass"]

    >>> parse_schema_path("extraction.input_mass")  # no array
    ['extraction', 'input_mass']
    >>> parse_schema_path("substances_used[0].volume")  # 1-D array
    ['substances_used', 'volume']
    """
    if not path:
        return []

    parts = []
    for part in path.split('.'):
        if '[' in part:
            # Extract slot name, ignore array index
            slot_name = part.split('[')[0]
            if slot_name:  # Only add non-empty slot names
                parts.append(slot_name)
        else:
            parts.append(part)

    return parts


def get_clean_schema_path(path: str) -> str:
    """
    Converts a document path with array indices to a clean schema path for reporting.
    
    Args:
        path: Path like "substances_used[0].volume" or "extraction.input_mass"
        
    Returns:
        Clean schema path: "substances_used.volume" or "extraction.input_mass"

    >>> get_clean_schema_path("extraction.input_mass")  # no array
    'extraction.input_mass'
    >>> get_clean_schema_path("substances_used[0].volume")  # 1-D array
    'substances_used.volume'
    """
    if not path:
        return "root"
    
    # Parse and rejoin without array indices
    schema_parts = parse_schema_path(path)
    return '.'.join(schema_parts) if schema_parts else "root"


def resolve_class_from_schema_path(schema_view, root_class: str, slot_path: List[str]) -> Optional[str]:
    """
    Uses schema definitions to resolve the target class for a nested slot path.
    
    Args:
        schema_view: SchemaView instance
        root_class: Starting class name (without "nmdc:" prefix)
        slot_path: List of slot names leading to the target field
        
    Returns:
        str or None: The resolved class name (without nmdc: prefix), or None if not found
    """
    if not slot_path:
        return root_class
    
    current_class = root_class
    
    try:
        for slot_name in slot_path:
            # Get the slot definition for this class
            slot_def = schema_view.induced_slot(slot_name, current_class)
            if not slot_def or not slot_def.range:
                return None
            
            # Move to the range class
            current_class = slot_def.range
            
        return current_class
        
    except (AttributeError, KeyError, TypeError, ValueError):
        # If schema traversal fails due to invalid class/slot names or missing schema definitions
        return None


def get_most_specific_class_for_reporting(schema_view, document_root: dict, path: str) -> str:
    """
    Determines the most specific class type for reporting purposes.
    For nested objects, use schema resolution to find the immediate parent class.
    
    Args:
        schema_view: SchemaView instance  
        document_root: The root document for fallback context
        path: Path to a QuantityValue-ranged slot within the document
        
    Returns:
        str: The most specific class URI (e.g., "nmdc:PortionOfSubstance")
    """
    # Parse path to get components leading to the QuantityValue
    path_parts = parse_schema_path(path)
    if not path_parts:
        return document_root.get('type', 'unknown')
    
    # Remove the final field name to get the path to the containing object
    container_path = path_parts[:-1] if len(path_parts) > 1 else []
    
    # Start with document's root class
    doc_type = document_root.get('type', 'nmdc:Unknown')
    root_class = doc_type.replace('nmdc:', '') if doc_type.startswith('nmdc:') else doc_type
    
    # Use schema to resolve the class context for the container
    if container_path:
        target_class = resolve_class_from_schema_path(schema_view, root_class, container_path)
        if target_class:
            return f"nmdc:{target_class}"
    
    # Fallback to document type
    return doc_type


