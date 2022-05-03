
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition, Annotation

# from sqldf import sqldf
from pandasql import sqldf

import click
import click_log
import logging

import yaml

# TODO add click documentation etc

# this script, in combination with slot_roster.py, creates a MIxS-subset import file
# for use with the NMDC schema
# the output (can) include the slots from the latest MIxS model,
# as long as that has been pulled into the local submodule

# todo we also import slots that are used in the NMDC's DataHarmonizer templates
#  even if they we never imported into the NMDC schema before

# and we are NOT importing MIxS slots that were included in the legacy NMDC MIxS import
# but were never associated with any class

# This script can overwrite some of the attributes based on legacy NMDC usage
# ie, it doesn't make sense to change the schema if the data backend
# or downstream data consumers still expect legacy ranges, etc.

pd.set_option("display.max_columns", None)

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
# use_legacy defines the attributes which will be held back to the legacy values
@click.option("--use_legacy", "-u", multiple=True)
@click.option("--output_yaml", "-o", required=True)
# and this provides a see_also link for the terms that have held-back attribute values
# might be nice to use something official like an NMDC page
# but for now I am considering a Google Docs page, or just a link to this script via GH
@click.option("--legacy_see_also", "-s", required=True)
# make this (and others?) click file paths
@click.option("--slot_roster_tsv_in", "-r", required=True)
@click.option("--legacy_mixs_module_in", "-l", required=True)
@click.option("--current_mixs_root_in", "-c", required=True)
@click.option("--current_nmdc_root_in", "-c", required=True)
def cli(
        use_legacy,
        output_yaml,
        legacy_see_also,
        slot_roster_tsv_in,
        legacy_mixs_module_in,
        current_mixs_root_in,
        current_nmdc_root_in
):
    logger.info("getting started")
    mixs_5_view = SchemaView(legacy_mixs_module_in)
    mixs_6_view = SchemaView(current_mixs_root_in)
    # nmdc_view = SchemaView(current_nmdc_root_in)
    slot_roster_frame = pd.read_csv(slot_roster_tsv_in, sep="\t", low_memory=False)

    # todo mixed metaphors of sqldf and .loc indexing

    lmu_q = """
    SELECT
        distinct class, slot
    from
        slot_roster_frame
    where
        "schema" = 'NMDC'
        and slot_schema = 'https://microbiomedata/schema/mixs'
        and class is not NULL
        and class != ''
    """

    legacy_mixs_usage = sqldf(lmu_q)
    # legacy_mixs_usage.to_csv("legacy_mixs_usage.csv")

    fdh_q = """
    select
        distinct slot
    from
        slot_roster_frame
    where
        "schema" = 'nmdc_dh'
        and slot_schema = 'http://w3id.org/mixs/terms'
    """

    from_dh = sqldf(fdh_q)
    # from_dh.to_csv("from_dh.csv")

    na_q = """
    SELECT
        distinct slot
    from
        slot_roster_frame
    where
        "schema" = 'MIxS'
        and slot_schema = 'http://w3id.org/mixs/terms';
    """

    now_available = sqldf(na_q)
    # now_available.to_csv("now_available.csv")
    na_set = set(now_available["slot"])

    legacy_or_dh = set(legacy_mixs_usage['slot']).union(set(from_dh['slot']))

    l_o_d_available = legacy_or_dh.intersection(na_set)
    # l_o_d_available = l_o_d_available - set('air_particulate_matter_concentration')
    l_o_d_available = list(l_o_d_available)
    l_o_d_available = [i for i in l_o_d_available if
                       i != 'air_particulate_matter_concentration' and i != 'air particulate matter concentration']
    l_o_d_available.sort()

    #     # print(slot_roster_frame['no_good_match'].value_counts(dropna=False))
    #     # # NaN    36499
    #     # # 1.0       16
    #     # # Name: no_good_match, dtype: int64

    #     # print(slot_roster_frame['schema'].value_counts(dropna=False))
    #     # # MIxS       33581
    #     # # nmdc_dh     1853
    #     # # NMDC        1081
    #     # # Name: schema, dtype: int64

    # no_good_match is supposed to be boolean, but might have been cast to a string at some point,
    # but why is it a float now?
    # ---
    # these slots are already being used in mongodb, but are no longer defined in MIxS 6 or later
    # just salvage them from MIxS 5
    salvage_from_legacy = slot_roster_frame.loc[
        slot_roster_frame["no_good_match"].eq(1)
        & slot_roster_frame["schema"].eq("NMDC")
        & slot_roster_frame["mongodb"].eq(1),
        ["slot_raw"],
    ]

    salvage_from_legacy.drop_duplicates(inplace=True)
    salvage_from_legacy = list(salvage_from_legacy["slot_raw"])

    replace_with_new = slot_roster_frame.loc[
        slot_roster_frame["match"].str.len()
        > 0
        & slot_roster_frame["schema"].eq("NMDC")
        & slot_roster_frame["mongodb"].isna(),
        ["class", "slot_raw", "match"],
    ]

    rwn_lod = replace_with_new.to_dict(orient='records')

    # todo opening with SchemaView description.
    #  do this manually, with yq, or glom?
    with open(current_nmdc_root_in, "r") as stream:
        try:
            nmdc_dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger.warning(exc)

    for i in rwn_lod:
        try:
            logger.info(i)
            temp = nmdc_dict['classes'][i['class']]['slots']
            temp.remove(i['slot_raw'])
            temp.append(i['match'])
            nmdc_dict['classes'][i['class']]['slots'] = temp
        except ValueError:
            logger.error(f"'slot_row' not in {i}")

    # todo save to a different file?
    #  flow style?
    with open(current_nmdc_root_in, 'w') as outfile:
        yaml.dump(nmdc_dict, outfile, default_flow_style=False, sort_keys=False)

    # shoot, that mangles the schema description, too
    # FROM
    #   Schema for National Microbiome Data Collaborative (NMDC).
    #
    #   This schema is organized into distinct modules:
    #
    #    * a set of core types for representing data values
    #    * the mixs schema (auto-translated from mixs excel)
    #    * annotation schema
    #    * the NMDC schema itself
    # TO
    # "Schema for National Microbiome Data Collaborative (NMDC).\n  \nThis\
    #   \ schema is organized into distinct modules:\n  \n * a set of core types for representing\
    #   \ data values\n * the mixs schema (auto-translated from mixs excel)\n * annotation\
    #   \ schema\n * the NMDC schema itself"
    # anything else?

    rwn_dict = replace_with_new.set_index("slot_raw").to_dict()["match"]

    nwr_dict = {v: k for k, v in rwn_dict.items()}

    rebuild_mixs_schema = SchemaDefinition(
        name=mixs_5_view.schema.name,
        id=mixs_5_view.schema.id,
        title=mixs_5_view.schema.title,
        imports=mixs_5_view.schema.imports,
    )

    all_but_salvage = l_o_d_available + list(replace_with_new["match"])

    # todo add source versions
    #  create mixs version issue
    #  use mike?!
    for current_slot_name in all_but_salvage:
        logger.info(current_slot_name)
        temp = mixs_6_view.get_slot(current_slot_name)
        temp.source = temp.from_schema
        if current_slot_name in nwr_dict:
            temp.annotations["mixs_5_name"] = Annotation(
                tag="mixs_5_name", value=nwr_dict[current_slot_name]
            )
        if temp.examples and len(temp.examples) == 1 and temp.examples[0].value == "":
            temp.examples = None
        rebuild_mixs_schema.slots[current_slot_name] = temp
        range_obj = mixs_6_view.get_element(temp.range)
        range_type = type(range_obj)
        range_type_name = range_type.class_name
        if range_type_name == "enum_definition":
            rebuild_mixs_schema.enums[temp.range] = range_obj
        if temp.is_a:
            is_a_obj = mixs_6_view.get_slot(temp.is_a)
            rebuild_mixs_schema.slots[temp.is_a] = is_a_obj

    for current_slot_name in salvage_from_legacy:
        logger.info(current_slot_name)
        temp = mixs_5_view.get_slot(current_slot_name)
        temp.source = temp.from_schema
        rebuild_mixs_schema.slots[current_slot_name] = temp
        # todo refactor
        if len(temp.examples) == 1 and temp.examples[0].value == "":
            temp.examples = None
        rebuild_mixs_schema.slots[current_slot_name] = temp
        range_obj = mixs_5_view.get_element(temp.range)
        range_type = type(range_obj)
        range_type_name = range_type.class_name
        if range_type_name == "enum_definition":
            rebuild_mixs_schema.enums[temp.range] = range_obj

    legacy_schema_slots = mixs_5_view.all_slots()
    legacy_schema_slotnames = list(legacy_schema_slots.keys())
    legacy_schema_slotnames.sort()

    rebuild_mixs_schema_slots = rebuild_mixs_schema.slots
    rebuild_mixs_schema_slotnames = list(rebuild_mixs_schema_slots.keys())
    rebuild_mixs_schema_slotnames.sort()

    for current_slot_name in rebuild_mixs_schema_slotnames:
        if current_slot_name in legacy_schema_slotnames:
            for current_use_legacy in use_legacy:
                rebuild_mixs_schema.slots[current_slot_name][
                    current_use_legacy
                ] = mixs_5_view.schema.slots[current_slot_name][current_use_legacy]
        rebuild_mixs_schema.slots[current_slot_name].see_also.append(legacy_see_also)

    yaml_dumper.dump(rebuild_mixs_schema, output_yaml)


if __name__ == "__main__":
    cli()
