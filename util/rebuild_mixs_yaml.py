import pprint

import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition, Annotation
from sqldf import sqldf

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

# this list defines the attributes which will be held back to the legacy values
keep_vals_from_legacy = [
    "is_a",
    "multivalued",
    "range",
]

# and this provides a see_also link for the terms that have held-back attribute values
# might be nice to use something official like an NMDC page
# but for now I am considering a Google Docs page, or just a link to this script via GH
use_legacy_see_also = "http://example.com"

destination_schema_file = "../src/schema/mixs_rebuild.yaml"

mixs_5_file = "../src/schema/mixs.yaml"
mixs_5_view = SchemaView(mixs_5_file)

mixs_6_file = "../mixs/model/schema/mixs.yaml"
mixs_6_view = SchemaView(mixs_6_file)

slot_roster_file = "../reports/slot_roster.tsv"
slot_roster_frame = pd.read_csv(slot_roster_file, sep="\t", low_memory=False)

# todo mixed metaphors of sqldf and .loc indexing

query = """
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

legacy_mixs_usage = sqldf.run(query)

query = """
SELECT
    distinct slot
from
    slot_roster_frame
where
    "schema" = 'MIxS'
    and slot_schema = 'http://w3id.org/mixs/terms';
"""

now_available = sqldf.run(query)
na_set = set(now_available["slot"])

query = """
select
    distinct slot
from
    slot_roster_frame
where
    "schema" = 'nmdc_dh'
    and slot_schema = 'http://w3id.org/mixs/terms'
"""

from_dh = sqldf.run(query)

include_intersection = na_set.intersection(set(legacy_mixs_usage["slot"]))
include_intersection = include_intersection.intersection(set(from_dh["slot"]))
include_intersection = list(include_intersection)
include_intersection.sort()

# print(slot_roster_frame['no_good_match'].value_counts(dropna=False))
# print(slot_roster_frame['schema'].value_counts(dropna=False))
#
# # NaN    36499
# # 1.0       16
# # Name: no_good_match, dtype: int64
# # MIxS       33581
# # nmdc_dh     1853
# # NMDC        1081
# # Name: schema, dtype: int64

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
    > 0 & slot_roster_frame["schema"].eq("NMDC") & slot_roster_frame["mongodb"].isna(),
    ["slot_raw", "match"],
]

rwn_dict = replace_with_new.set_index("slot_raw").to_dict()["match"]
nwr_dict = {v: k for k, v in rwn_dict.items()}

# SchemaDefinition(version=None, default_prefix='https://microbiomedata/schema/mixs/', source_file='../src/schema/mixs.yaml')

# rebuild_mixs_name = mixs_5_view.schema.name
# rebuild_mixs_id = mixs_5_view.schema.id
# rebuild_mixs_prefix = "https://example.com/"
# rebuild_mixs_id = f"{rebuild_mixs_prefix}{rebuild_mixs_name}"

rebuild_mixs_schema = SchemaDefinition(
    name=mixs_5_view.schema.name,
    id=mixs_5_view.schema.id,
    title=mixs_5_view.schema.title,
    imports=mixs_5_view.schema.imports,
)

appended_intersection = include_intersection + list(replace_with_new["match"])

# add source versions
# create mixs version issue
# use mike?!
for current_slot_name in appended_intersection:
    print(current_slot_name)
    temp = mixs_6_view.get_slot(current_slot_name)
    temp.source = temp.from_schema
    if current_slot_name in nwr_dict:
        temp.annotations["mixs_5_name"] = Annotation(
            tag="mixs_5_name", value=nwr_dict[current_slot_name]
        )
    if len(temp.examples) == 1 and temp.examples[0].value == "":
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
    print(current_slot_name)
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

legagacy_schema_slots = mixs_5_view.all_slots()
legagacy_schema_slotnames = list(legagacy_schema_slots.keys())
legagacy_schema_slotnames.sort()

rebuild_mixs_schema_slots = rebuild_mixs_schema.slots
rebuild_mixs_schema_slotnames = list(rebuild_mixs_schema_slots.keys())
rebuild_mixs_schema_slotnames.sort()

# todo also add new see_also
for current_slot_name in rebuild_mixs_schema_slotnames:
    if current_slot_name in legagacy_schema_slotnames:
        legacy_slot_obj = mixs_5_view.get_slot(current_slot_name)
        for current_use_legacy in keep_vals_from_legacy:
            print(f"{current_slot_name} {current_use_legacy}")
            rebuild_mixs_schema.slots[current_slot_name][
                current_use_legacy
            ] = mixs_5_view.schema.slots[current_slot_name][current_use_legacy]
    rebuild_mixs_schema.slots[current_slot_name].see_also.append(use_legacy_see_also)

yaml_dumper.dump(rebuild_mixs_schema, destination_schema_file)
