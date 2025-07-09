import pprint
import click
import os
import glob
import yaml
import re

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from nmdc_schema.nmdc import Database
from collections import defaultdict


def increment_id(original_id, slot_id_tracker):
    """
    Increment an ID by one digit or letter to make it unique.
    
    Args:
        original_id: The original ID that needs to be incremented
        slot_id_tracker: Set of existing IDs to avoid collisions
    
    Returns:
        A new unique ID
    """
    # Try incrementing the last character
    if original_id and len(original_id) > 0:
        last_char = original_id[-1]
        base_id = original_id[:-1]
        
        # If last character is a digit, increment it
        if last_char.isdigit():
            new_digit = str(int(last_char) + 1)
            new_id = base_id + new_digit
        # If last character is a letter, increment it
        elif last_char.isalpha():
            if last_char.lower() == 'z':
                # If 'z' or 'Z', append 'a' or 'A' 
                new_id = original_id + ('a' if last_char.islower() else 'A')
            else:
                new_char = chr(ord(last_char) + 1)
                new_id = base_id + new_char
        else:
            # If last character is neither digit nor letter, append '1'
            new_id = original_id + '1'
        
        # Check if the new ID is still unique, if not, recursively increment
        if new_id in slot_id_tracker:
            return increment_id(new_id, slot_id_tracker)
        else:
            return new_id
    else:
        # If original_id is empty, return a default
        return original_id + '1'


@click.command()
@click.option('--directory-path', default='src/data/valid', help='Path to the directory containing YAML files.')
@click.option('--output-file', default='interleaved.yaml', help='Output file to save the interleaved YAML.')
@click.option('--schema-file', default='src/schema/nmdc.yaml', help='Schema file path.')
def process_yaml(directory_path, output_file, schema_file):
    """
    Process and interleave YAML files from the specified directory, excluding the output file.
    Avoids overwriting the existing output file.
    """
    # Ensure output file does not get processed if it exists in the same directory
    file_paths = glob.glob(os.path.join(directory_path, 'Database-*.yaml'))
    file_paths.sort()
    output_file_path = os.path.abspath(output_file)  # Ensure the path is absolute
    interleaved_file_path = os.path.join(directory_path, 'Database-interleaved.yaml')
    file_paths = [file for file in file_paths if os.path.abspath(file) != output_file_path and os.path.abspath(file) != interleaved_file_path]

    if os.path.exists(output_file_path):
        click.echo(f"Output file {output_file_path} already exists. Please remove it or specify a different file.")
        return  # Exit the function if output file already exists

    collector = Database()
    schema_view = SchemaView(schema_file)
    database_slots = schema_view.class_induced_slots('Database')
    database_slot_names = [slot.name for slot in database_slots]
    database_slot_names.sort()

    # Track duplicate IDs for reporting and resolution
    duplicate_ids = defaultdict(list)
    slot_id_tracker = defaultdict(set)
    id_modifications = defaultdict(list)

    # pprint.pprint(database_slot_names)
    # print(schema_view.schema.name)

    for file in file_paths:
        click.echo(f"Processing file: {file}")
        with open(file, 'r') as f:
            # Load the YAML data
            data = yaml.safe_load(f)

            database = yaml_loader.load(data, Database)
            for slot in database_slot_names:
                payload = getattr(database, slot)
                # Extend the list in the collector for each slot
                if payload:
                    if slot not in collector.__dict__:
                        collector.__dict__[slot] = []
                    
                    # Check for duplicate IDs within this slot and resolve them
                    for item in payload:
                        if hasattr(item, 'id') and item.id:
                            original_id = item.id
                            if original_id in slot_id_tracker[slot]:
                                # Record the original duplicate
                                duplicate_ids[slot].append(original_id)
                                # Generate a new unique ID
                                new_id = increment_id(original_id, slot_id_tracker[slot])
                                # Update the item's ID
                                item.id = new_id
                                # Track the modification
                                id_modifications[slot].append(f"{original_id} -> {new_id}")
                                # Add the new ID to the tracker
                                slot_id_tracker[slot].add(new_id)
                            else:
                                slot_id_tracker[slot].add(original_id)
                    
                    collector.__dict__[slot].extend(payload)

    # Report duplicate IDs found and resolved
    if duplicate_ids:
        click.echo("\n⚠️  Duplicate IDs found and resolved:")
        for slot, ids in duplicate_ids.items():
            click.echo(f"  {slot}: {sorted(set(ids))}")
        
        click.echo("\n🔧 ID modifications made:")
        for slot, modifications in id_modifications.items():
            click.echo(f"  {slot}:")
            for modification in modifications:
                click.echo(f"    {modification}")
    else:
        click.echo("\n✅ No duplicate IDs found")

    # Dump the interleaved content into YAML format
    interleaved_content = yaml_dumper.dumps(collector)
    # print(interleaved_content)
    yaml_dumper.dump(collector, output_file_path)
    
    click.echo(f"\nInterleaved YAML saved to: {output_file_path}")


if __name__ == '__main__':
    process_yaml()
