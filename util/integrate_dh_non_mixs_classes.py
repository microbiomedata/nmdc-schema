import pprint
import re

import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition, Prefix, EnumDefinition

nmdc_dh_schema_url = "https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/main/artifacts/nmdc_dh.yaml"
# rename that to something about the function and content like NMDC SubmissionPortal Schema

nmdc_dh_schema_view = SchemaView(nmdc_dh_schema_url)

nmdc_dh_schema_slots = nmdc_dh_schema_view.all_slots()

# filesystem? package? GH URL? w3id URL?
nmdc_schema_view = SchemaView(
    "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml"
)
nmdc_schema_slots = nmdc_schema_view.all_slots()

slots_by_group = []
for slot_alias, slot_obj in nmdc_dh_schema_slots.items():
    # if "slot_group" in slot_obj:
    slots_by_group.append({"slot": slot_alias, "slot_group": slot_obj["slot_group"]})
slots_by_group_frame = pd.DataFrame(slots_by_group)

group_counts = slots_by_group_frame["slot_group"].value_counts(dropna=False)

# print(group_counts)

# None                       501
# JGI-Metagenomics            19
# JGI-Metatranscriptomics     19
# MIxS Inspired               16
# EMSL                         6
# Sample ID                    3

nmdc_schema_enums_names = list(nmdc_schema_view.all_enums().keys())

slot_list = []
for i in group_counts.index:
    if i:
        i_ncname = re.sub("[ -]", "_", i.lower())
        groups_slots = list(
            slots_by_group_frame.loc[slots_by_group_frame["slot_group"].eq(i), "slot"]
        )
        groups_slots.sort()
        new_schema = SchemaDefinition(
            name=i_ncname,
            id=f"https://microbiomedata/schema/{i_ncname}",
            title=f"NMDC Schema supplement for Submission Portal: {i}",
            description=f"This file defines terms that appear in the '{i}' section of the NMDC sample metadata submission portal, which is implemented with DataHarmonizer as of Spring 2022",
            license="license: https://creativecommons.org/publicdomain/zero/1.0/",
            default_prefix="nmdc",
            default_range="string",
        )
        new_schema.prefixes = [
            Prefix(
                prefix_prefix="linkml",
                prefix_reference="https://w3id.org/linkml/",
            ),
            Prefix(
                prefix_prefix="nmdc",
                prefix_reference="https://microbiomedata/meta/",
            ),
        ]
        new_schema.imports.append("linkml:types")
        #         default_curi_maps:
        #         - obo_context
        #         - idot_context
        for j in groups_slots:
            if j not in nmdc_schema_slots:
                slot_list.append(j)
                temp = nmdc_dh_schema_slots[j]
                # todo the new /portal schema files include several required biosample fields
                #  switching them to recommended now so that data validation tests will pass
                temp_range_name = temp.range
                if temp.required:
                    temp.required = False
                    temp.recommended = True
                if temp_range_name:
                    temp_obj = nmdc_dh_schema_view.get_element(temp_range_name)
                    if (
                        type(temp_obj) == EnumDefinition
                        and temp_range_name not in nmdc_schema_enums_names
                    ):
                        new_schema.enums[temp_range_name] = temp_obj
                new_schema.slots[j] = temp
        yaml_dumper.dump(new_schema, f"src/schema/portal/{i_ncname}.yaml")
print("Add these slots to the Biosmaple class:")
for i in slot_list:
    print(f"- {i}")
