#!/usr/bin/env python3
"""
Consolidated MIxS Unit Processing Pipeline

This script replaces the chain of individual scripts:
- add_has_problem.py
- add_slot_count.py  
- find_storage_units.py
- generate_multi_unit_storage_units.py

Usage:
    python process_mixs_units.py INPUT_FILE [--output-dir OUTPUT_DIR]

Input file should contain columns:
- slot: The schema slot name
- ucum_notation: UCUM-compatible unit notation
- problem: 1 if problematic unit, 0 if clean

Outputs:
- storage-units-single.txt: yq commands for single-unit slots
- storage-units-multi.txt: yq commands for multi-unit slots
"""

import sys
from pathlib import Path
from typing import List
import pandas as pd
import click


def validate_input_file(file_path: Path) -> bool:
    """Validate that input file exists and has required columns."""
    if not file_path.exists():
        print(f"Error: Input file '{file_path}' not found")
        return False
    
    try:
        df = pd.read_csv(file_path, sep='\t', nrows=1)
        required_cols = {'slot', 'ucum_notation', 'problem'}
        missing_cols = required_cols - set(df.columns)
        if missing_cols:
            print(f"Error: Missing required columns: {missing_cols}")
            print(f"Available columns: {list(df.columns)}")
            return False
        return True
    except Exception as e:
        print(f"Error reading input file: {e}")
        return False


def process_mixs_data(input_file: Path) -> pd.DataFrame:
    """
    Process MIxS data through the complete pipeline:
    1. Add has_problem flags (slot-level)
    2. Add slot_row_count (count units per slot)
    3. Filter and prepare for yq command generation
    """
    print(f"Reading input file: {input_file}")
    df = pd.read_csv(input_file, sep='\t')
    
    print(f"Loaded {len(df)} rows with {len(df['slot'].unique())} unique slots")
    
    # Step 1: Add has_problem column (slot-level problem flag)
    problem_slots = df[df['problem'] == 1]['slot'].unique()
    df['has_problem'] = df['slot'].isin(problem_slots).astype(int)
    print(f"Found {len(problem_slots)} slots with problem units")
    
    # Step 2: Add slot_row_count (units per slot)
    slot_counts = df['slot'].value_counts().to_dict()
    df['slot_row_count'] = df['slot'].map(slot_counts)
    
    # Summary statistics
    single_unit_slots = df[df['slot_row_count'] == 1]['slot'].nunique()
    multi_unit_slots = df[df['slot_row_count'] > 1]['slot'].nunique()
    print(f"Slots with single unit: {single_unit_slots}")
    print(f"Slots with multiple units: {multi_unit_slots}")
    
    return df


def generate_single_unit_commands(df: pd.DataFrame) -> List[str]:
    """Generate yq commands for slots with single UCUM-compatible units."""
    # Filter: no problems AND exactly one unit per slot
    valid_slots = df[(df['problem'] != 1) & (df['slot_row_count'] == 1)].copy()
    
    commands = []
    commands.append("# Add storage_units annotations for slots with single UCUM-compatible preferred units")
    
    for _, row in valid_slots.iterrows():
        slot_name = row['slot']
        ucum_notation = row['ucum_notation']
        commands.append(f"'.slots.{slot_name}.annotations.storage_units.tag |= \"storage_units\"'")
        commands.append(f"'.slots.{slot_name}.annotations.storage_units.value |= \"{ucum_notation}\"'")
    
    commands.append(f"\n# Generated {len(valid_slots) * 2} yq commands for {len(valid_slots)} single-unit slots")
    return commands


def generate_multi_unit_commands(df: pd.DataFrame) -> List[str]:
    """Generate yq commands for slots with multiple UCUM-compatible units."""
    # Filter: no problems AND multiple units per slot
    multi_unit_slots = df[(df['problem'] != 1) & (df['slot_row_count'] > 1)].copy()
    
    # Group by slot and create pipe-separated UCUM notation lists
    slot_groups = multi_unit_slots.groupby('slot')['ucum_notation'].apply(
        lambda x: '|'.join(sorted(x.unique()))
    ).reset_index()
    
    commands = []
    commands.append("# Add storage_units annotations for slots with multiple UCUM-compatible preferred units")
    
    for _, row in slot_groups.iterrows():
        slot_name = row['slot']
        ucum_list = row['ucum_notation']
        commands.append(f"'.slots.{slot_name}.annotations.storage_units = {{\"tag\": \"storage_units\", \"value\": \"{ucum_list}\"}}'")
    
    total_rows = len(multi_unit_slots)
    unique_slots = len(slot_groups)
    commands.append(f"\n# Generated {len(slot_groups)} yq commands for multi-unit storage_units annotations")
    commands.append(f"# Summary: {total_rows} total rows across {unique_slots} slots with multiple units")
    
    return commands


def write_output_files(single_commands: List[str], multi_commands: List[str], output_dir: Path):
    """Write yq commands to output files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    single_file = output_dir / "single.txt"
    multi_file = output_dir / "multi.txt"
    
    with open(single_file, 'w') as f:
        f.write('\n'.join(single_commands))
    print(f"Written single-unit commands to: {single_file}")
    
    with open(multi_file, 'w') as f:
        f.write('\n'.join(multi_commands))
    print(f"Written multi-unit commands to: {multi_file}")


@click.command()
@click.option('--input', type=click.Path(exists=True, path_type=Path), required=True,
              help='TSV file with columns: slot, ucum_notation, problem')
@click.option('--output-dir', type=click.Path(path_type=Path), default=Path('.'),
              help='Output directory for generated files')
def main(input: Path, output_dir: Path):
    """Process MIxS unit data and generate storage_units yq commands."""
    
    input_file = input
    
    # Validate input
    if not validate_input_file(input_file):
        sys.exit(1)
    
    try:
        # Process the data through the complete pipeline
        df = process_mixs_data(input_file)
        
        # Generate yq commands
        click.echo("Generating yq commands...")
        single_commands = generate_single_unit_commands(df)
        multi_commands = generate_multi_unit_commands(df)
        
        # Write output files
        write_output_files(single_commands, multi_commands, output_dir)
        click.echo(f"Processing complete! Files written to: {output_dir}")
    
    except Exception as e:
        click.echo(f"Error during processing: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()