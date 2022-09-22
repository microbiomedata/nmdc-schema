import json
import pprint

import yaml
from pathlib import Path

mongodb_dump_yaml = "assets/from_mongodb.yaml"
updated_mongodb_dump_json = "assets/from_mongodb_updated.json"
updated_mongodb_dump_yaml = "assets/from_mongodb_updated.yaml"

mongodb_dump = yaml.safe_load(Path(mongodb_dump_yaml).read_text())

study_set = mongodb_dump["study_set"]

actions = {
    "study_set":
        {"GOLD_study_identifiers": "gold_study_identifiers", },
    "biosample_set":
        {"GOLD_sample_identifiers": "gold_sample_identifiers",
         "INSDC_biosample_identifiers": "insdc_biosample_identifiers",
         "part_of": "sample_link", },
}


def rename_key(d, old_key, new_key):
    if old_key in d:
        d[new_key] = d.pop(old_key)
    return d


for coll_name, coll in mongodb_dump.items():
    print(f"Processing {coll_name}")
    if coll_name in actions:
        for col_item in coll:
            for old_key, new_key in actions[coll_name].items():
                rename_key(col_item, old_key, new_key)

with open(updated_mongodb_dump_yaml, "w", encoding="utf-8") as yaml_file:
    dump = yaml.dump(mongodb_dump, default_flow_style=False, allow_unicode=True, encoding=None)
    yaml_file.write(dump)

with open(updated_mongodb_dump_json, "w", encoding="utf-8") as json_file:
    json.dump(mongodb_dump, json_file, indent=4)
