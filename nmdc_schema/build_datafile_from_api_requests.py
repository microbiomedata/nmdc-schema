# need to match destination collection to api_request
# lots of redundancy
# prefer not to rewrite another paging method, so payloads could be large (but no mare than 2000)
# will there be a simple filter for all the collections to be queried?
# nmdc:sty-12-85j6kq06query from https://github.com/microbiomedata/nmdc-schema/issues/1205#issuecomment-1776129426 not working. try nmdc:sty-11-28tm5d36
# works: https://api-napa.microbiomedata.org/biosamples?filter=part_of%3Anmdc:sty-11-28tm5d36&per_page=999
# and https://api-napa.microbiomedata.org/biosamples?filter=part_of%3Anmdc:sty-11-28tm5d36&per_page=99&page=2
# may still require loosening of schema or "migrations" that assert missing data

# 'collection_time': '08:45  - 12:05' !?
# study descriptions with stray whitespace

import requests
import yaml

database_dict = {}

output_file = "database.yaml"


def dump_python_dict_to_yaml_file(python_dict, yaml_file_path):
    """Dumps a Python dict to a YAML file.

    Args:
      python_dict: The Python dict to dump.
      yaml_file_path: The path to the YAML file.
    """

    with open(yaml_file_path, "w") as yaml_file:
        yaml.dump(python_dict, yaml_file)


# hard to implement with a Click CLI
# config file?
# example URL to determine most likely collection?
api_requests = {
    "biosample_set": "https://api-napa.microbiomedata.org/biosamples?filter=part_of%3Anmdc:sty-11-28tm5d36&per_page=999",
    "sample_set": "https://api-napa.microbiomedata.org/studies?filter=ecosystem%3AEnvironmental&per_page=999"
}
for ark, arv in api_requests.items():
    database_dict[ark] = requests.get(arv).json()["results"]

dump_python_dict_to_yaml_file(database_dict, output_file)
