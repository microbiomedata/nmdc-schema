import csv
from pprint import pprint

import click
from typing import List, Dict

import os

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, json_dumper


class BooleanUsages:
    schema_files: List[str] = []

    def __init__(self):
        pass

    def get_all_files(self, path, extension):
        all_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(extension):
                    all_files.append(os.path.join(root, file))
        return all_files


@click.command()
@click.option('--schema_file', default='src/schema/nmdc.yaml',
              help='Path to a root schema module',
              type=str, required=True)
@click.option('--out_file', required=True, help='Output file path', type=str)
def cli(schema_file: str, out_file: str):
    schema_view = SchemaView(schema_file, merge_imports=True)

    comparisons = []

    schema_classes = schema_view.all_classes()
    for ck, cv in schema_classes.items():
        if cv.slot_usage:
            for uk, uv in cv.slot_usage.items():
                uv_dict = json_dumper.to_dict(uv)
                for dk, dv in uv_dict.items():
                    if type(dv) == bool:
                        reference_slot = schema_view.get_slot(uk)
                        reference_attribute = reference_slot[dk]
                        comparison = {
                            "class": ck,
                            "slot": uk,
                            "attribute": dk,
                            "value": dv,
                            "reference_value": reference_attribute
                        }
                        comparisons.append(comparison)

    with open(out_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=comparisons[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(comparisons)


if __name__ == '__main__':
    cli()
