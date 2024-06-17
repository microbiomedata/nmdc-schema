import pprint
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
    # Ensure output file does not get processed if it exists in the same directory
    file_paths = glob.glob(os.path.join(directory_path, 'Database-*.yaml'))
    file_paths.sort()
    output_file_path = os.path.abspath(output_file)  # Ensure the path is absolute
    file_paths = [file for file in file_paths if file != output_file_path]

    if os.path.exists(output_file_path):
        click.echo(f"Output file {output_file_path} already exists. Please remove it or specify a different file.")
        return  # Exit the function if output file already exists

    collector = Database()
    schema_view = SchemaView(schema_file)
    database_slots = schema_view.class_induced_slots('Database')
    database_slot_names = [slot.name for slot in database_slots]
    database_slot_names.sort()

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
                    collector.__dict__[slot].extend(payload)

    # Dump the interleaved content into YAML format
    interleaved_content = yaml_dumper.dumps(collector)
    # print(interleaved_content)
    yaml_dumper.dump(collector, output_file_path)


if __name__ == '__main__':
    process_yaml()
