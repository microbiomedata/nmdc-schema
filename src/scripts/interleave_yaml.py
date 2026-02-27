import click
import os
import glob
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from nmdc_schema.nmdc import Database
from collections import defaultdict


@click.command()
@click.option('--directory-path', default='src/data/valid', help='Path to the directory containing YAML files.')
@click.option('--output-file', default='interleaved.yaml', help='Output file to save the interleaved YAML.')
@click.option('--schema-file', default='src/schema/nmdc.yaml', help='Schema file path.')
def process_yaml(directory_path, output_file, schema_file):
    """
    Process and interleave YAML files from the specified directory, excluding the output file.
    Avoids overwriting the existing output file.
    """
    file_paths = glob.glob(os.path.join(directory_path, 'Database-*.yaml'))
    file_paths.sort()
    output_file_path = os.path.abspath(output_file)
    interleaved_file_path = os.path.abspath(os.path.join(directory_path, 'Database-interleaved.yaml'))
    file_paths = [file for file in file_paths if os.path.abspath(file) != output_file_path and os.path.abspath(file) != interleaved_file_path]

    if os.path.exists(output_file_path):
        click.echo(f"Output file {output_file_path} already exists. Please remove it or specify a different file.")
        return

    collector = Database()
    schema_view = SchemaView(schema_file)
    database_slots = schema_view.class_induced_slots('Database')
    database_slot_names = [slot.name for slot in database_slots]
    database_slot_names.sort()

    # Track seen items per slot: id -> (source_file, serialized_item)
    seen_items = defaultdict(dict)
    dedup_count = 0

    for file in file_paths:
        click.echo(f"Processing file: {file}")
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

            database = yaml_loader.load(data, Database)
            for slot in database_slot_names:
                payload = getattr(database, slot)
                if payload:
                    if slot not in collector.__dict__:
                        collector.__dict__[slot] = []

                    items_to_add = []
                    for item in payload:
                        if hasattr(item, 'id') and item.id:
                            item_yaml = yaml_dumper.dumps(item)
                            if item.id in seen_items[slot]:
                                prior_file, prior_yaml = seen_items[slot][item.id]
                                if item_yaml == prior_yaml:
                                    click.echo(
                                        f"  Dedup: identical '{item.id}' in slot '{slot}' "
                                        f"(first in {prior_file}, also in {file})"
                                    )
                                    dedup_count += 1
                                    continue
                                else:
                                    raise click.ClickException(
                                        f"Non-identical duplicate ID '{item.id}' in slot '{slot}': "
                                        f"first seen in {prior_file}, different version in {file}. "
                                        f"Fix the duplicate in the source files by giving one a unique ID."
                                    )
                            seen_items[slot][item.id] = (file, item_yaml)
                        items_to_add.append(item)

                    collector.__dict__[slot].extend(items_to_add)

    if dedup_count:
        click.echo(f"\n{dedup_count} identical duplicate(s) deduplicated.")
    else:
        click.echo("\nNo duplicate IDs found.")

    yaml_dumper.dump(collector, output_file_path)
    click.echo(f"Interleaved YAML saved to: {output_file_path}")


if __name__ == '__main__':
    process_yaml()
