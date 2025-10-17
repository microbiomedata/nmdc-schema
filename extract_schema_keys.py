#!/usr/bin/env python3
"""
Extract and classify all keys from LinkML schema files.

Outputs TSV with: filename, key, count, classification (metamodel|application)
"""
import yaml
import argparse
import sys
from pathlib import Path
from typing import Set, Dict, Counter
from collections import Counter as CounterClass
from linkml_runtime.utils.schemaview import SchemaView
from urllib.parse import urljoin
import requests


def get_all_metamodel_terms(metamodel_view: SchemaView) -> Set[str]:
    """
    Extract ALL valid metamodel terms including aliases.

    Returns a set of all slot names, class names, enum names, type names,
    and their aliases that are valid in the LinkML metamodel.
    """
    terms = set()

    # Get all slot names and aliases
    for slot_name in metamodel_view.all_slots():
        slot = metamodel_view.get_slot(slot_name)
        terms.add(slot_name)
        if slot.aliases:
            terms.update(slot.aliases)

    # Get all class names and aliases
    for class_name in metamodel_view.all_classes():
        cls = metamodel_view.get_class(class_name)
        terms.add(class_name)
        if cls.aliases:
            terms.update(cls.aliases)

    # Get all enum names and aliases
    for enum_name in metamodel_view.all_enums():
        enum = metamodel_view.get_enum(enum_name)
        terms.add(enum_name)
        if enum.aliases:
            terms.update(enum.aliases)

    # Get all type names and aliases
    for type_name in metamodel_view.all_types():
        type_def = metamodel_view.get_type(type_name)
        terms.add(type_name)
        if type_def.aliases:
            terms.update(type_def.aliases)

    return terms


def extract_all_keys(obj, keys_counter: CounterClass):
    """Recursively extract all dictionary keys from a YAML structure."""
    if isinstance(obj, dict):
        for key in obj.keys():
            keys_counter[key] += 1
        for value in obj.values():
            extract_all_keys(value, keys_counter)
    elif isinstance(obj, list):
        for item in obj:
            extract_all_keys(item, keys_counter)


def load_yaml_from_path_or_url(path_or_url: str) -> dict:
    """Load YAML from local file or URL."""
    if path_or_url.startswith('http://') or path_or_url.startswith('https://'):
        response = requests.get(path_or_url)
        response.raise_for_status()
        return yaml.safe_load(response.text)
    else:
        with open(path_or_url, 'r') as f:
            return yaml.safe_load(f)


def get_imports(schema_data: dict) -> list:
    """Extract imports list from schema."""
    return schema_data.get('imports', [])


def resolve_import_path(import_name: str, base_path: str) -> str:
    """
    Resolve an import name to a full path.

    For URLs: join with base URL
    For local files: resolve relative to base directory
    """
    if base_path.startswith('http://') or base_path.startswith('https://'):
        # Web-based schema
        base_url = base_path.rsplit('/', 1)[0] + '/'
        if not import_name.endswith('.yaml'):
            import_name = import_name + '.yaml'
        return urljoin(base_url, import_name)
    else:
        # Local file system
        base_dir = Path(base_path).parent
        import_path = base_dir / import_name
        if not import_path.suffix:
            import_path = import_path.with_suffix('.yaml')
        return str(import_path)


def analyze_schema_file(
    path_or_url: str,
    metamodel_terms: Set[str],
    visited: Set[str] = None,
    follow_imports: bool = True
) -> Dict[str, Dict[str, tuple]]:
    """
    Analyze a schema file and optionally its imports.

    Returns:
        Dict mapping filename to dict of {key: (count, classification)}
    """
    if visited is None:
        visited = set()

    if path_or_url in visited:
        return {}

    visited.add(path_or_url)
    results = {}

    try:
        # Load schema
        schema_data = load_yaml_from_path_or_url(path_or_url)

        # Extract keys and count them
        keys_counter = CounterClass()
        extract_all_keys(schema_data, keys_counter)

        # Classify each key
        classified_keys = {}
        for key, count in keys_counter.items():
            classification = 'metamodel' if key in metamodel_terms else 'application'
            classified_keys[key] = (count, classification)

        # Use just the filename for display
        if path_or_url.startswith('http'):
            display_name = path_or_url.split('/')[-1]
        else:
            display_name = Path(path_or_url).name

        results[display_name] = classified_keys

        # Follow imports if requested
        if follow_imports:
            imports = get_imports(schema_data)
            for import_name in imports:
                try:
                    import_path = resolve_import_path(import_name, path_or_url)
                    import_results = analyze_schema_file(
                        import_path,
                        metamodel_terms,
                        visited,
                        follow_imports=True
                    )
                    results.update(import_results)
                except Exception as e:
                    print(f"Warning: Could not load import '{import_name}': {e}",
                          file=sys.stderr)

    except Exception as e:
        print(f"Error analyzing {path_or_url}: {e}", file=sys.stderr)

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Extract and classify keys from LinkML schema files'
    )
    parser.add_argument(
        'schema',
        help='Path or URL to schema file, or directory of schema files'
    )
    parser.add_argument(
        '--output', '-o',
        default='schema_keys.tsv',
        help='Output TSV file (default: schema_keys.tsv)'
    )
    parser.add_argument(
        '--no-imports',
        action='store_true',
        help='Do not follow imports'
    )
    parser.add_argument(
        '--metamodel',
        default='https://w3id.org/linkml/meta.yaml',
        help='LinkML metamodel URL or path (default: https://w3id.org/linkml/meta.yaml)'
    )

    args = parser.parse_args()

    # Load metamodel and extract all valid terms
    print(f"Loading LinkML metamodel from {args.metamodel}...", file=sys.stderr)
    metamodel_view = SchemaView(args.metamodel)
    metamodel_terms = get_all_metamodel_terms(metamodel_view)
    print(f"Found {len(metamodel_terms)} metamodel terms", file=sys.stderr)

    # Analyze schema(s)
    results = {}

    # Check if input is a directory
    if not args.schema.startswith('http') and Path(args.schema).is_dir():
        print(f"Analyzing directory {args.schema}...", file=sys.stderr)
        for yaml_file in Path(args.schema).glob('*.yaml'):
            file_results = analyze_schema_file(
                str(yaml_file),
                metamodel_terms,
                follow_imports=not args.no_imports
            )
            results.update(file_results)
    else:
        print(f"Analyzing {args.schema}...", file=sys.stderr)
        results = analyze_schema_file(
            args.schema,
            metamodel_terms,
            follow_imports=not args.no_imports
        )

    # Write TSV output
    with open(args.output, 'w') as out:
        out.write("filename\tkey\tcount\tclassification\n")
        for filename in sorted(results.keys()):
            for key in sorted(results[filename].keys()):
                count, classification = results[filename][key]
                out.write(f"{filename}\t{key}\t{count}\t{classification}\n")

    print(f"\nResults written to {args.output}", file=sys.stderr)
    print(f"Analyzed {len(results)} file(s)", file=sys.stderr)


if __name__ == '__main__':
    main()
