import os
import pprint

import yaml
from linkml_runtime import SchemaView

# set the directory path here (relative path)
source_directory = "src/data/valid"

schema_file = 'src/schema/nmdc.yaml'

schema_view = SchemaView(schema_file)


def find_type_keys(data):
    """
    Recursively searches for all "type" key values within a YAML structure.

    Args:
        data: The YAML data structure (dict or list).

    Returns:
        A dictionary where keys are type values and values are their counts.
    """
    tc = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "type":
                tc[value] = tc.get(value, 0) + 1  # Increment count
            else:
                tc.update(find_type_keys(value))  # Recursively call on values (objects or lists)
    elif isinstance(data, list):
        for item in data:
            tc.update(find_type_keys(item))  # Recursively call on list items
    return tc


def process_all_files(directory):
    """
    Processes all YAML files in a directory, finding all "type" key values and accumulating counts in a dictionary.

    Args:
        directory: The directory containing YAML files.

    Returns:
        A dictionary where keys are type values from all files and values are their total counts.
    """
    tc = {}
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
                file_tc = find_type_keys(data)

                def accumulate_counts(target_dict, source_dict):
                    for key, value in source_dict.items():
                        target_dict[key] = target_dict.get(key, 0) + value

                accumulate_counts(tc, file_tc)  # Accumulate counts from each file
    return tc


# Process all files and get the combined type counts
type_counts = process_all_files(source_directory)

print("Types asserted in any src/data/valid YAML file:")
print("")
pprint.pprint(type_counts)
print("\n")

schema_classes = schema_view.all_classes()

available_classes = {}
for ck, cv in schema_classes.items():
    available_classes[ck] = {
        "declared_uri": schema_view.get_uri(cv, native=False),
        "native_uri": schema_view.get_uri(cv, native=True),
    }

lacks_example = {"abstract": {}, "concrete": {}}
for k, v in available_classes.items():
    if v["declared_uri"] not in type_counts and v["native_uri"] not in type_counts:

        if schema_view.get_class(k).abstract:
            lacks_example["abstract"][k] = v
        else:
            lacks_example["concrete"][k] = v

print("Classes that are not instantiated in any src/data/valid YAML file:")
print("")
pprint.pprint(lacks_example)
