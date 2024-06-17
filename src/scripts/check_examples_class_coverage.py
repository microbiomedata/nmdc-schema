import os
import pprint
import click
import yaml
from linkml_runtime import SchemaView

@click.command()
@click.option('--source_directory', default='src/data/valid', help='Directory containing YAML files to process.')
@click.option('--schema_file', default='src/schema/nmdc.yaml', help='Schema file path.')
def main(source_directory, schema_file):
    schema_view = SchemaView(schema_file)

    def find_type_keys(data):
        tc = {}
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "type":
                    tc[value] = tc.get(value, 0) + 1
                else:
                    tc.update(find_type_keys(value))
        elif isinstance(data, list):
            for item in data:
                tc.update(find_type_keys(item))
        return tc

    def process_all_files(directory):
        tc = {}
        for filename in os.listdir(directory):
            if filename.endswith(".yaml"):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as f:
                    data = yaml.safe_load(f)
                    file_tc = find_type_keys(data)
                    for key, value in file_tc.items():
                        tc[key] = tc.get(key, 0) + value
        return tc

    type_counts = process_all_files(source_directory)
    print("Types asserted in any src/data/valid YAML file:")
    pprint.pprint(type_counts)
    print("\n")

    schema_classes = schema_view.all_classes()
    available_classes = {ck: {
        "declared_uri": schema_view.get_uri(cv, native=False),
        "native_uri": schema_view.get_uri(cv, native=True),
    } for ck, cv in schema_classes.items()}

    lacks_example = {"abstract": {}, "concrete": {}}
    for k, v in available_classes.items():
        if v["declared_uri"] not in type_counts and v["native_uri"] not in type_counts:
            if schema_view.get_class(k).abstract:
                lacks_example["abstract"][k] = v
            else:
                lacks_example["concrete"][k] = v

    print("Classes that are not instantiated in any src/data/valid YAML file:")
    pprint.pprint(lacks_example)

if __name__ == '__main__':
    main()
