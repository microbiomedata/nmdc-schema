#!/usr/bin/env python3
"""
MongoDB Unit Validation Analysis

This script analyzes production MongoDB data to validate actual units against 
schema-acceptable units. Part of the legacy MongoDB-based workflow.

Input CSV format (from SPARQL query over RDF-converted MongoDB data):
- sc: schema class (e.g., https://w3id.org/nmdc/Biosample)
- p: property (e.g., https://w3id.org/mixs/0000110) 
- l: label (e.g., samp_store_temp)
- su: schema-acceptable units, pipe-separated (e.g., Cel|K)
- u: actual unit found in production data (e.g., Cel)
- count: number of occurrences in production data

Processing logic:
1. Splits pipe-separated acceptable units (su column)
2. Checks if actual unit (u) exists in acceptable list
3. Assigns validation status: valid/invalid/no_spec

Output: Original CSV with added 'valid' column showing validation results.
Provides summary statistics of unit validation across production data.

Note: This is part of the legacy MongoDB workflow. The current schema-only 
approach (analyze.py → extract.py → process.py) eliminates this dependency.
"""

import csv
import sys
import click

@click.command()
@click.option('--input', type=click.Path(exists=True, path_type=str), required=True,
              help='MongoDB slots-to-units CSV from SPARQL query')
@click.option('--output', type=click.Path(path_type=str),
              help='Output file path (default: INPUT_analyzed.csv)')
def main(input: str, output: str = None):
    """Analyze MongoDB unit validation data."""
    
    csv_file = input
    if output is None:
        output = csv_file.replace('.csv', '_analyzed.csv')
    
    try:
        with open(csv_file, 'r') as infile, open(output, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            
            # Add 'valid' column to fieldnames
            fieldnames = reader.fieldnames + ['valid']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                su = row['su'].strip()  # acceptable units
                u = row['u'].strip()    # actual unit used
                
                if not su:  # No acceptable units specified
                    row['valid'] = 'no_spec'
                else:
                    # Split pipe-separated acceptable units
                    acceptable_units = [unit.strip() for unit in su.split('|')]
                    if u in acceptable_units:
                        row['valid'] = 'valid'
                    else:
                        row['valid'] = 'invalid'
                
                writer.writerow(row)
        
        click.echo(f"Analysis complete. Output written to: {output}")
        
        # Print summary
        with open(output, 'r') as f:
            reader = csv.DictReader(f)
            valid_count = 0
            invalid_count = 0
            no_spec_count = 0
            total = 0
            
            for row in reader:
                total += 1
                if row['valid'] == 'valid':
                    valid_count += 1
                elif row['valid'] == 'invalid':
                    invalid_count += 1
                else:
                    no_spec_count += 1
            
            click.echo(f"\nSummary:")
            click.echo(f"Total rows: {total}")
            click.echo(f"Valid: {valid_count} ({valid_count/total*100:.1f}%)")
            click.echo(f"Invalid: {invalid_count} ({invalid_count/total*100:.1f}%)")
            click.echo(f"No specification: {no_spec_count} ({no_spec_count/total*100:.1f}%)")
            
    except FileNotFoundError:
        click.echo(f"Error: File '{csv_file}' not found", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    main()