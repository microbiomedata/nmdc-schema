"""dumps from mongodb, though API? into an NMDC database object
That will contain biosamples, studies and omics processings
at least to start
then dump that to a YAML file"""
import json
# import pprint

import requests

from ruamel import yaml

yaml_out_file = "assets/from_mongodb.yaml"
json_out_file = "assets/from_mongodb.json"

nmdc_runtime_api_base = "https://api.dev.microbiomedata.org/"

tasks_by_token = {
    "studies": {"api_method": None, "database_slot": "study_set"},
    "biosamples": {"api_method": None, "database_slot": "biosample_set"},
    "omics_processing_set": {"api_method": None, "database_slot": "omics_processing_set"}
}


#
# def get_page(method, inner_params):
#     inner_assembled_request = f"{nmdc_runtime_api_base}{method}"
#     print(f"URL: {inner_assembled_request}")
#     response = requests.get(inner_assembled_request, params=inner_params)
#     inner_rjd = response.json()
#     return inner_rjd


def get_page_by_token(setname="study_set", max_page_size=5, next_page_token=None):
    inner_assembled_request = f"{nmdc_runtime_api_base}nmdcschema/{setname}"
    inner_params = {"max_page_size": max_page_size}
    if next_page_token:
        inner_params["page_token"] = next_page_token
    response = requests.get(inner_assembled_request, params=inner_params)
    inner_rjd = response.json()
    return inner_rjd


def get_all_by_token(task_dict, max_page_size=100):
    # print("will loop over and process task_dict entries")
    outer_dict = {}
    for tk, tv in task_dict.items():
        print(f"Processing {tk}")
        database_slot = tv["database_slot"]
        expecting_more = True
        next_page_token = None
        while expecting_more:
            if database_slot in outer_dict:
                print(f"{database_slot} len: {len(outer_dict[database_slot])}")
            print(f"current page token: {next_page_token}")
            page_by_token = get_page_by_token(setname=tv["database_slot"], max_page_size=max_page_size,
                                              next_page_token=next_page_token)
            # for i in page_by_token["resources"]:
            #     if "has_credit_associations" in i:
            #         del i["has_credit_associations"]
            # pprint.pprint(page_by_token)
            print(page_by_token.keys())
            if "next_page_token" in page_by_token and page_by_token["next_page_token"]:
                next_page_token = page_by_token["next_page_token"]
                print(f"next_page_token: {next_page_token}")
            else:
                expecting_more = False
            if "resources" in page_by_token and page_by_token["resources"]:
                if database_slot not in outer_dict:
                    print(f"Adding {database_slot} to outer_dict")
                    outer_dict[database_slot] = []
                to_extend = page_by_token["resources"]
                for i in to_extend:
                    if "has_credit_associations" in i:
                        del i["has_credit_associations"]
                outer_dict[database_slot].extend(to_extend)
            print("\n")
    return outer_dict


# def get_all(task_dict, per_page=100):
#     outer_dict = {}
#     for tk, tv in task_dict.items():
#         print(f"Processing {tk}")
#         expecting_more = True
#         page = 1
#         while expecting_more:
#             params = {"per_page": per_page, "page": page}
#             rjd = get_page(method=tv['api_method'], inner_params=params)
#             if "results" in rjd and rjd["results"]:
#                 database_slot = tv['database_slot']
#                 print(f"There are results to be loaded into the {database_slot}")
#                 if database_slot not in outer_dict:
#                     outer_dict[database_slot] = []
#                 outer_dict[database_slot].extend(rjd["results"])
#                 pass
#             if "meta" in rjd:
#                 rjd_meta = rjd["meta"]
#                 pprint.pprint(rjd_meta)
#                 if rjd_meta["per_page"] * page >= rjd_meta["count"]:
#                     expecting_more = False
#                 else:
#                     page += 1
#             else:
#                 pprint.pprint(rjd)
#     return outer_dict


database_dict = get_all_by_token(task_dict=tasks_by_token)

print("writing everything to NMDC databases as JSON and YAML")

with open(yaml_out_file, "w", encoding="utf-8") as yaml_file:
    dump = yaml.dump(database_dict, default_flow_style=False, allow_unicode=True, encoding=None)
    yaml_file.write(dump)

with open(json_out_file, "w", encoding="utf-8") as json_file:
    json.dump(database_dict, json_file, indent=4)
