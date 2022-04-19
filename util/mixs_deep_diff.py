import pandas as pd
import yaml
from deepdiff import DeepDiff
from linkml_runtime import SchemaView

from strsimpy.cosine import Cosine

INCLUDE_DESCRIPTIONS = True

shingle_size = 2
cosine_obj = Cosine(shingle_size)

old_file = "../src/schema/mixs.yaml"
new_file = "../src/schema/mixs_new.yaml"

# tsv_out = "../reports/slot.tsv"

anno_tsv_out = "../reports/slot_annotations_diffs.tsv"

slot_diff_yaml_out = "../reports/slot_diffs.yaml"


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
    sd_list = list(slots_diff)
    sd_list.sort()
    return sd_list


def get_anno_diffs(deep_diff_obj, tsv_file_name, incl_descrs=False):
    old_view = SchemaView(old_file)
    new_view = SchemaView(new_file)
    lod = []
    vc = deep_diff_obj["values_changed"]
    for current_vc in vc:
        current_path = current_vc.path(output_format="list")
        if (
            len(current_path) == 3
            and current_path[0] == "slots"
            and (current_path[2] != "description" or incl_descrs)
        ):
            to_append = {
                "slot": current_path[1],
                "attribute": current_path[2],
            }
            if current_path[2] == "description":
                p0 = cosine_obj.get_profile(current_vc.t1)
                p1 = cosine_obj.get_profile(current_vc.t2)
                cos_dist_res = cosine_obj.similarity_profiles(p0, p1)
                to_append["descr_dist"] = 1 - cos_dist_res
                to_append["old_desc"] = current_vc.t1
                to_append["new_desc"] = current_vc.t2
            else:
                to_append["old_val"] = current_vc.t1
                to_append["new_val"] = current_vc.t2
            if current_path[2] == "range":
                old_element = old_view.get_element(current_vc.t1)
                to_append["old_range_type"] = type(old_element).class_name
                new_element = new_view.get_element(current_vc.t2)
                to_append["new_range_type"] = type(new_element).class_name
            lod.append(to_append)

    df = pd.DataFrame(lod)
    # pprint.pprint(df)
    df.to_csv(tsv_file_name, sep="\t", index=False)


old_dict = y_file_to_dict(old_file)

new_dict = y_file_to_dict(new_file)

mixs_diff = DeepDiff(old_dict, new_dict, view="tree")
# print(mixs_diff.keys())
# # dict_keys(['dictionary_item_removed', 'dictionary_item_added', 'values_changed'])

added_diff = get_slots_diff(mixs_diff, "added")

removed_diff = get_slots_diff(mixs_diff, "removed")

slots_diff_dict = {"added": added_diff, "removed": removed_diff}

with open(slot_diff_yaml_out, "w") as outfile:
    yaml.dump(slots_diff_dict, outfile, default_flow_style=False)

get_anno_diffs(mixs_diff, anno_tsv_out, INCLUDE_DESCRIPTIONS)
