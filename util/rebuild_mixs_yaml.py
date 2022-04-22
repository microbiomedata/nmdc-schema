import pprint

import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition, Annotation
from sqldf import sqldf

mixs_5_file = "../src/schema/mixs.yaml"
mixs_5_view = SchemaView(mixs_5_file)

mixs_6_file = "../mixs/model/schema/mixs.yaml"
mixs_6_view = SchemaView(mixs_6_file)

slot_roster_file = "../reports/slot_roster.tsv"
slot_roster_frame = pd.read_csv(slot_roster_file, sep="\t", low_memory=False)

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

include_intersection = list(na_set.intersection(set(legacy_mixs_usage["slot"])))
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
    imports=mixs_5_view.schema.imports
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
    if range_type_name == 'enum_definition':
        rebuild_mixs_schema.enums[temp.range] = range_obj
    if temp.is_a:
        print(temp.is_a)
        is_a_obj = mixs_6_view.get_slot(temp.is_a)
        print(is_a_obj)
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
    if range_type_name == 'enum_definition':
        rebuild_mixs_schema.enums[temp.range] = range_obj

yaml_dumper.dump(rebuild_mixs_schema, "../src/schema/mixs_rebuild.yaml")
