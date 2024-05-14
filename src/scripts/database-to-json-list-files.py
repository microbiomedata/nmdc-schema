import yaml
import json


def split_yaml_to_json(yaml_file_path):
    # Open and read the YAML file
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Loop through the keys in the YAML data and write each to a separate JSON file
    for key, value in data.items():
        json_file_name = f"{key}.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(value, json_file, indent=4)  # Writing value directly without key

        print(f"Data for {key} written to {json_file_name}")


# Path to your YAML file
yaml_file_path = '../data/valid/Database-interleaved.yaml'

# Call the function with the path to your YAML file
split_yaml_to_json(yaml_file_path)
