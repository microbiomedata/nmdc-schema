import pprint

import pandas as pd
import yaml
from deepdiff import DeepDiff

old_file = "../src/schema/mixs.yaml"
new_file = "../src/schema/mixs_6_for_nmdc.yaml"


def y_file_to_dict(y_file_name):
    with open(y_file_name, "r") as stream:
        try:
            dict_from_yaml = yaml.safe_load(stream)
            return dict_from_yaml
        except yaml.YAMLError as exc:
            print(exc)


def get_slots_diff(deep_diff_obj, delta_type):
    # delta type is "added" or "removed"
    slots_diff = set()
    full_delta_type = f"dictionary_item_{delta_type}"
    deep_diff_subset = deep_diff_obj[full_delta_type]
    for current_dds in deep_diff_subset:
        current_path = current_dds.path(output_format="list")
        # print(current_path)
        if (
            len(current_path) == 3
            and current_path[0] == "slots"
            and current_path[2] == "name"
        ):
            slots_diff.add(current_path[1])
        if len(current_path) == 2 and current_path[0] == "slots":
            slots_diff.add(current_path[1])
    return slots_diff


def get_is_a_diff(deep_diff_obj, tsv_file_name):
    lod = []
    vc = deep_diff_obj["values_changed"]
    for current_vc in vc:
        current_path = current_vc.path(output_format="list")
        if len(current_path) == 3 and current_path[0] == "slots":
            lod.append(
                {
                    "slot": current_path[1],
                    "attribute": current_path[2],
                    "old_val": current_vc.t1,
                    "new_val": current_vc.t2,
                }
            )
    df = pd.DataFrame(lod)
    # pprint.pprint(df)
    df.to_csv(tsv_file_name, sep="\t", index=False)


old_dict = y_file_to_dict(old_file)

new_dict = y_file_to_dict(new_file)

mixs_diff = DeepDiff(old_dict, new_dict, view="tree")
# print(mixs_diff.keys())
# # dict_keys(['dictionary_item_removed', 'dictionary_item_added', 'values_changed'])

added_diff = get_slots_diff(mixs_diff, "added")
pprint.pprint(added_diff)

removed_diff = get_slots_diff(mixs_diff, "removed")
pprint.pprint(removed_diff)

get_is_a_diff(mixs_diff, "../reports/attribute_diffs.tsv")
