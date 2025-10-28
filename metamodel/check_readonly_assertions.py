#!/usr/bin/env python3
"""
Check if any readonly metaslots are asserted in a LinkML schema file.

Readonly metaslots should only be set by the schema loader/viewer,
not by schema authors in the source schema.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any, Set
import yaml
from linkml_runtime.linkml_model import SchemaDefinition

# Readonly metaslots (from no_orphans_materialized.yaml analysis)
READONLY_SLOTS = {
    'definition_uri',
    'from_schema',
    'imported_from',
    'metamodel_version',
    'source_file',
    'source_file_date',
    'source_file_size',
    'generation_date',
    'owner',
    'domain_of',
    'is_usage_slot',
    'usage_slot_name',
}


def check_element_for_readonly(element_name: str, element_data: Dict[str, Any],
                                 element_type: str) -> List[str]:
    """Check if an element has any readonly metaslots asserted."""
    violations = []

    if not isinstance(element_data, dict):
        return violations

    for readonly_slot in READONLY_SLOTS:
        if readonly_slot in element_data:
            violations.append(
                f"{element_type} '{element_name}' has readonly slot '{readonly_slot}' "
                f"set to: {element_data[readonly_slot]}"
            )

    return violations


def check_schema_file(schema_path: Path) -> Dict[str, List[str]]:
    """
    Check a schema file for readonly slot assertions.

    Returns a dict mapping element types to lists of violation messages.
    """
    with open(schema_path) as f:
        schema_dict = yaml.safe_load(f)

    violations = {
        'classes': [],
        'slots': [],
        'enums': [],
        'types': [],
        'subsets': [],
        'schema': [],
    }

    # Check schema-level metadata
    for readonly_slot in READONLY_SLOTS:
        if readonly_slot in schema_dict:
            violations['schema'].append(
                f"Schema has readonly slot '{readonly_slot}' set to: {schema_dict[readonly_slot]}"
            )

    # Check classes
    if 'classes' in schema_dict and schema_dict['classes']:
        for class_name, class_data in schema_dict['classes'].items():
            class_violations = check_element_for_readonly(class_name, class_data, 'Class')
            violations['classes'].extend(class_violations)

            # Check slot_usage within classes
            if isinstance(class_data, dict) and 'slot_usage' in class_data:
                for slot_name, slot_usage_data in class_data['slot_usage'].items():
                    usage_violations = check_element_for_readonly(
                        f"{class_name}.slot_usage.{slot_name}",
                        slot_usage_data,
                        'SlotUsage'
                    )
                    violations['classes'].extend(usage_violations)

            # Check attributes within classes
            if isinstance(class_data, dict) and 'attributes' in class_data:
                for attr_name, attr_data in class_data['attributes'].items():
                    attr_violations = check_element_for_readonly(
                        f"{class_name}.attributes.{attr_name}",
                        attr_data,
                        'Attribute'
                    )
                    violations['classes'].extend(attr_violations)

    # Check slots
    if 'slots' in schema_dict and schema_dict['slots']:
        for slot_name, slot_data in schema_dict['slots'].items():
            slot_violations = check_element_for_readonly(slot_name, slot_data, 'Slot')
            violations['slots'].extend(slot_violations)

    # Check enums
    if 'enums' in schema_dict and schema_dict['enums']:
        for enum_name, enum_data in schema_dict['enums'].items():
            enum_violations = check_element_for_readonly(enum_name, enum_data, 'Enum')
            violations['enums'].extend(enum_violations)

    # Check types
    if 'types' in schema_dict and schema_dict['types']:
        for type_name, type_data in schema_dict['types'].items():
            type_violations = check_element_for_readonly(type_name, type_data, 'Type')
            violations['types'].extend(type_violations)

    # Check subsets
    if 'subsets' in schema_dict and schema_dict['subsets']:
        for subset_name, subset_data in schema_dict['subsets'].items():
            subset_violations = check_element_for_readonly(subset_name, subset_data, 'Subset')
            violations['subsets'].extend(subset_violations)

    return violations


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_readonly_assertions.py <schema_file.yaml>")
        print("\nChecks if any readonly metaslots are asserted in a schema file.")
        print("\nReadonly metaslots checked:")
        for slot in sorted(READONLY_SLOTS):
            print(f"  - {slot}")
        sys.exit(1)

    schema_path = Path(sys.argv[1])

    if not schema_path.exists():
        print(f"Error: Schema file not found: {schema_path}")
        sys.exit(1)

    print(f"Checking {schema_path} for readonly slot assertions...")
    print()

    violations = check_schema_file(schema_path)

    total_violations = sum(len(v) for v in violations.values())

    if total_violations == 0:
        print("✓ No readonly slot assertions found!")
        return 0

    print(f"Found {total_violations} readonly slot assertion(s):\n")

    for element_type, violation_list in violations.items():
        if violation_list:
            print(f"{element_type.upper()}:")
            for violation in violation_list:
                print(f"  ✗ {violation}")
            print()

    return 1


if __name__ == '__main__':
    sys.exit(main())
