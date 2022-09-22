"""dumps from mongodb, though API? into an NMDC database object
That will contain biosamples, studies and omics processings
at least to start
then dump that to a YAML file"""
import json
import pprint

import requests
from ruamel import yaml

yaml_out_file = "assets/from_mongodb.yaml"
json_out_file = "assets/from_mongodb.json"

nmdc_runtime_api_base = "https://api.dev.microbiomedata.org/"

tasks = {"studies":
             {"api_method": "studies", "database_slot": "study_set"},
         "biosamples":
             {"api_method": "biosamples", "database_slot": "biosample_set"},
         "activities":
             {"api_method": "activities", "database_slot": "activity_set"},
         }

per_page = 100


def get_page(method, inner_params):
    inner_assembled_request = f"{nmdc_runtime_api_base}{method}"
    print(f"URL: {inner_assembled_request}")
    response = requests.get(inner_assembled_request, params=inner_params)
    inner_rjd = response.json()
    return inner_rjd


def get_all(task_dict):
    outer_dict = {}
    for tk, tv in task_dict.items():
        print(f"Processing {tk}")
        expecting_more = True
        page = 1
        while expecting_more:
            params = {"per_page": per_page, "page": page}
            rjd = get_page(method=tv['api_method'], inner_params=params)
            if "results" in rjd and rjd["results"]:
                database_slot = tv['database_slot']
                print(f"There are results to be loaded into the {database_slot}")
                if database_slot not in outer_dict:
                    outer_dict[database_slot] = []
                outer_dict[database_slot].extend(rjd["results"])
                pass
            if "meta" in rjd:
                rjd_meta = rjd["meta"]
                pprint.pprint(rjd_meta)
                if rjd_meta["per_page"] * page >= rjd_meta["count"]:
                    expecting_more = False
                else:
                    page += 1
            else:
                pprint.pprint(rjd)
    return outer_dict


database_dict = get_all(tasks)

with open(yaml_out_file, "w", encoding="utf-8") as yaml_file:
    dump = yaml.dump(database_dict, default_flow_style=False, allow_unicode=True, encoding=None)
    yaml_file.write(dump)

with open(json_out_file, "w", encoding="utf-8") as json_file:
    json.dump(database_dict, json_file, indent=4)
