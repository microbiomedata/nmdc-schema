# need to match destination collection to api_request
# lots of redundancy
# prefer not to rewrite another paging method, so payloads could be large (but no mare than 2000)
# will there be a simple filter for all the collections to be queried?
# nmdc:sty-12-85j6kq06query from https://github.com/microbiomedata/nmdc-schema/issues/1205#issuecomment-1776129426 not working. try nmdc:sty-11-28tm5d36
# works: https://api-napa.microbiomedata.org/biosamples?filter=part_of%3Anmdc:sty-11-28tm5d36&per_page=999
# and https://api-napa.microbiomedata.org/biosamples?filter=part_of%3Anmdc:sty-11-28tm5d36&per_page=99&page=2
# may still require loosening of schema or "migrations" that assert missing data
import re

# 'collection_time': '08:45  - 12:05' !?
# study descriptions with stray whitespace

import click
import requests
import yaml


def dump_python_dict_to_yaml_file(python_dict, yaml_file_path):
    """Dumps a Python dict to a YAML file.

    Args:
      python_dict: The Python dict to dump.
      yaml_file_path: The path to the YAML file.
    """

    with open(yaml_file_path, "w") as yaml_file:
        yaml.dump(python_dict, yaml_file)


def read_python_dict_from_yaml_file(yaml_file_path):
    """Reads a Python dict from a YAML file.

    Args:
      yaml_file_path: The path to the YAML file.

    Returns:
      A Python dict.
    """

    with open(yaml_file_path, "r") as yaml_file:
        yaml_string = yaml_file.read()

    python_dict = yaml.load(yaml_string, Loader=yaml.SafeLoader)

    return python_dict


def extract_collection(string):
    """Extracts the text from a string after 'https://api-napa.microbiomedata.org/nmdcschema/' but before the first '?'.

    Args:
      string: The string to extract the text from.

    Returns:
      A string containing the extracted text.
    """

    regex = r'https:\/\/api-napa.microbiomedata.org\/nmdcschema\/(.*?)\?'
    match = re.search(regex, string)
    if match:
        return match.group(1)
    else:
        return None


@click.command()
@click.option("--api-url", multiple=True)
@click.option("--output-file", required=True, type=click.Path())
def main(output_file, api_url):
    database_dict = {}

    for current_url in api_url:
        collection_name = extract_collection(current_url)
        print(f"Populating the {collection_name} from {current_url}")
        if collection_name in database_dict:
            # append to existing list
            database_dict[collection_name].extend(requests.get(current_url).json()["resources"])
        else:
            database_dict[collection_name] = requests.get(current_url).json()["resources"]

    dump_python_dict_to_yaml_file(database_dict, output_file)


if __name__ == "__main__":
    main()
