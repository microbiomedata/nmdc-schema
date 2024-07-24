import click
import yaml
import json
import os


@click.command()
@click.option('--yaml-input', type=click.Path(exists=True))
@click.option('--output-dir', type=click.Path(), default='.', help='Directory to save the JSON files')
def split_yaml_to_json(yaml_input, output_dir):
    """
    This script takes a YAML file path as an argument and splits its contents into separate JSON files,
    each named after the top-level keys in the YAML file. The JSON files are saved to the specified directory.
    """
    # Open and read the YAML file
    with open(yaml_input, 'r') as file:
        data = yaml.safe_load(file)

    # Ensure output directory exists, create if it does not
    os.makedirs(output_dir, exist_ok=True)

    # Loop through the keys in the YAML data and write each to a separate JSON file in the specified directory
    for key, value in data.items():
        json_file_name = f"{key}.json"
        json_file_path = os.path.join(output_dir, json_file_name)
        with open(json_file_path, 'w') as json_file:
            json.dump(value, json_file, indent=4)  # Writing value directly without key

        print(f"Data for {key} written to {json_file_path}")


if __name__ == '__main__':
    split_yaml_to_json()
