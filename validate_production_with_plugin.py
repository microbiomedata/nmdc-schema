#!/usr/bin/env python3
"""
Production validation using the new NmdcSchemaValidationPlugin.

This script validates production MongoDB data using the new validation plugin,
providing similar reporting to the old production_validate_units.py script.

Usage:
    python validate_production_with_plugin.py \
        --input local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
        --output validation_report_plugin.tsv \
        --schema-file nmdc_schema/nmdc_materialized_patterns.yaml
"""

import click
import yaml
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import csv

from linkml.validator import Validator
from nmdc_schema.nmdc_schema_validation_plugin import NmdcSchemaValidationPlugin


@click.command()
@click.option('--input', 'input_file', type=click.Path(exists=True, path_type=Path), required=True,
              help='MongoDB production data YAML file')
@click.option('--output', type=click.Path(path_type=Path), required=True,
              help='Output TSV file for validation report')
@click.option('--schema-file', type=click.Path(exists=True, path_type=Path),
              default=Path('nmdc_schema/nmdc_materialized_patterns.yaml'),
              help='Schema file for validation')
def main(input_file: Path, output: Path, schema_file: Path):
    """Validate production MongoDB data using NmdcSchemaValidationPlugin."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(f"[{timestamp}] Production Validation with Plugin")
    click.echo("=" * 70)
    click.echo(f"  Input:  {input_file}")
    click.echo(f"  Output: {output}")
    click.echo(f"  Schema: {schema_file}")
    click.echo()

    # Load data
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(f"[{timestamp}] Loading production data...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Create validator with plugin
    click.echo(f"[{timestamp}] Creating validator with NMDC validation plugin...")
    validator = Validator(
        schema=str(schema_file),
        validation_plugins=[NmdcSchemaValidationPlugin()]
    )

    # Statistics
    stats = {
        'total_collections': 0,
        'total_objects': 0,
        'total_errors': 0,
        'errors_by_collection': Counter(),
        'errors_by_type': Counter(),
        'all_errors': []
    }

    # Validate the entire database as a Database object
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(f"[{timestamp}] Validating database...")
    click.echo()

    try:
        # Validate entire database as Database class
        report = validator.validate(data, target_class='Database')

        # Count collections
        if isinstance(data, dict):
            for collection_name in data.keys():
                if collection_name.endswith('_set'):
                    stats['total_collections'] += 1
                    if isinstance(data[collection_name], list):
                        stats['total_objects'] += len(data[collection_name])

        click.echo(f"  Collections found: {stats['total_collections']}")
        click.echo(f"  Total objects:     {stats['total_objects']}")
        click.echo()

        # Collect errors from validation report
        for result in report.results:
            stats['total_errors'] += 1

            # Try to extract collection from error message path
            collection_name = 'unknown'
            if '/' in result.message:
                path_part = result.message.split('/')[1].split()[0] if '/' in result.message else ''
                if path_part.endswith('_set'):
                    collection_name = path_part

            stats['errors_by_collection'][collection_name] += 1
            stats['errors_by_type'][result.type] += 1

            # Store error details
            stats['all_errors'].append({
                'collection': collection_name,
                'object_id': 'N/A',
                'object_type': result.instantiates or 'Database',
                'error_type': result.type,
                'severity': result.severity.value,
                'message': result.message
            })

        click.echo(f"  Validation complete: {stats['total_errors']} errors found")

    except Exception as e:
        click.echo(f"ERROR during validation: {e}", err=True)
        import traceback
        traceback.print_exc()

    # Write report
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo()
    click.echo(f"[{timestamp}] Writing validation report to {output}...")

    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')

        # Header
        writer.writerow(['collection', 'object_id', 'object_type', 'error_type', 'severity', 'message'])

        # Write all errors
        for error in stats['all_errors']:
            writer.writerow([
                error['collection'],
                error['object_id'],
                error['object_type'],
                error['error_type'],
                error['severity'],
                error['message']
            ])

    # Print summary
    click.echo()
    click.echo("=" * 70)
    click.echo("VALIDATION SUMMARY")
    click.echo("=" * 70)
    click.echo(f"  Collections processed: {stats['total_collections']}")
    click.echo(f"  Objects validated:     {stats['total_objects']}")
    click.echo(f"  Total errors:          {stats['total_errors']}")
    click.echo()

    if stats['errors_by_collection']:
        click.echo("Errors by collection:")
        for collection, count in stats['errors_by_collection'].most_common():
            click.echo(f"  {collection:40s} {count:5d}")
        click.echo()

    if stats['errors_by_type']:
        click.echo("Errors by type:")
        for error_type, count in stats['errors_by_type'].most_common():
            click.echo(f"  {error_type:40s} {count:5d}")
        click.echo()

    if stats['total_errors'] > 0:
        click.echo(f"⚠️  {stats['total_errors']} validation errors found - see {output}")
    else:
        click.echo(f"✅ All data validated successfully!")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo()
    click.echo(f"[{timestamp}] Validation complete.")


if __name__ == "__main__":
    main()