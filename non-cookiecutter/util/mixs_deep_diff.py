import pprint

import pandas as pd
import yaml
from deepdiff import DeepDiff
from linkml_runtime import SchemaView

from strsimpy.cosine import Cosine

import click
import click_log
import logging

pd.set_option("display.max_columns", None)

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


def y_file_to_dict(y_file_name):
    with open(y_file_name, "r") as stream:
        try:
            dict_from_yaml = yaml.safe_load(stream)
            return dict_from_yaml
        except yaml.YAMLError as exc:
            logger.warning(exc)


def get_slots_diff(deep_diff_obj, delta_type):
    # delta type is "added" or "removed"
    slots_diff = set()
    full_delta_type = f"dictionary_item_{delta_type}"
    if full_delta_type in deep_diff_obj:
        deep_diff_subset = deep_diff_obj[full_delta_type]
        for current_dds in deep_diff_subset:
            current_path = current_dds.path(output_format="list")
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


def get_anno_diffs(
    deep_diff_obj, tsv_file_name, old_view, new_view, cosine_obj, incl_descrs=False
):
    lod = []
    if "values_changed" in deep_diff_obj:
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
                # if current_path[2] == "range":
                #     old_element = old_view.get_element(current_vc.t1)
                #     to_append["old_range_type"] = type(old_element).class_name
                #     new_element = new_view.get_element(current_vc.t2)
                #     to_append["new_range_type"] = type(new_element).class_name
                lod.append(to_append)

        df = pd.DataFrame(lod)
        df.to_csv(tsv_file_name, sep="\t", index=False)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--include_descriptions", "-d", default=True)
@click.option("--shingle_size", "-o", default=2)
@click.option("--slot_diff_yaml_out", "-y", required=True)
@click.option("--anno_diff_tsv_out", "-t", required=True)
@click.option("--legacy_mixs_module_in", "-l", required=True)
@click.option("--current_mixs_module_in", "-c", required=True)
def cli(
    include_descriptions,
    shingle_size,
    slot_diff_yaml_out,
    anno_diff_tsv_out,
    legacy_mixs_module_in,
    current_mixs_module_in,
):
    logger.info("getting started")
    cosine_obj = Cosine(shingle_size)
    old_dict = y_file_to_dict(legacy_mixs_module_in)
    new_dict = y_file_to_dict(current_mixs_module_in)

    mixs_diff = DeepDiff(old_dict, new_dict, view="tree")

    # print(mixs_diff.keys())
    # # dict_keys(['dictionary_item_removed', 'dictionary_item_added', 'values_changed'])

    added_diff = get_slots_diff(mixs_diff, "added")

    removed_diff = get_slots_diff(mixs_diff, "removed")

    slots_diff_dict = {"added": added_diff, "removed": removed_diff}

    with open(slot_diff_yaml_out, "w") as outfile:
        yaml.dump(slots_diff_dict, outfile, default_flow_style=False)

    new_view = SchemaView(current_mixs_module_in)
    old_view = SchemaView(legacy_mixs_module_in)
    get_anno_diffs(
        mixs_diff,
        anno_diff_tsv_out,
        old_view,
        new_view,
        cosine_obj,
        include_descriptions,
    )


if __name__ == "__main__":
    cli()
