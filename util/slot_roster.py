import difflib

from linkml_runtime import SchemaView
from typing import Dict, Optional, List
import pandas as pd
import pprint
import requests

import sqldf

# using 'True' for True and None/'' for False

# todo: indicate borrowed
#  use see also s to indicate related mixs term?
#  indicate as_is, modified or inspired with something in addition to a dh_section (slot group?)

# todo from mixs annotation should also include version

pd.set_option("display.max_columns", None)

# get from...
# local filesystem?
# w3id?
# other URL?
# submodule?

input_paths = [
    "../mixs/model/schema/mixs.yaml",
    "../src/schema/nmdc.yaml",
    "https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/issue-100-netlify-linkml-datastructure/artifacts/nmdc_dh.yaml",
]

# todo how to do this programmatically
class_to_api_bit = {
    "biosample": "biosamples",
    "omics processing": "activities?filter=type%3Anmdc%3AOmicsProcessing",
}

api_bit_to_class = {v: k for k, v in class_to_api_bit.items()}


# print(api_bit_to_class)


class SlotRoster:
    def __init__(self):
        self.frame_dict: Optional[Dict[str, pd.DataFrame]] = {}
        self.slots_dict: Optional[Dict[str, List[str]]] = {}
        self.view_dict: Optional[Dict[str, SchemaView]] = {}

    def add_view_from_file(self, schema_file: str) -> str:
        print(f"opening {schema_file}")
        view = SchemaView(schema_file)
        sn = view.schema.name
        print(f"adding {schema_file} as {sn}")
        self.view_dict[sn] = view
        return sn

    def add_schema_slot_names(self, sn: str, incl_imports: bool = True) -> None:
        print(f"recording slots from {sn}")
        # had returned List[str]
        current_view = self.view_dict[sn]
        current_slot_obj = current_view.all_slots(imports=incl_imports)
        current_slot_names = [v.name for k, v in current_slot_obj.items()]
        current_slot_names.sort()
        self.slots_dict[sn] = current_slot_names

    def add_schema_class_slots(self, sn: str, incl_imports: bool = True) -> None:
        print(f"recording class-slot relationships from {sn}")
        current_view = self.view_dict[sn]
        schema_classes = current_view.all_classes(imports=incl_imports)
        sc_names = list(schema_classes.keys())
        sc_names.sort()
        lod = []
        for current_class in sc_names:
            jit_class = current_view.get_class(current_class)
            # todo oops, wrap after 80 chars or so
            print(".", end="")
            cis = current_view.class_induced_slots(current_class)
            for current_slot in cis:
                # if current_slot.see_also:
                #     print(f"{current_slot.name} see_also {current_slot.see_also}")
                smbs = None
                if current_slot.mixin:
                    smbs = "True"
                sabs = None
                if current_slot.abstract:
                    sabs = "True"
                cmbs = None
                if jit_class.mixin:
                    cmbs = "True"
                cabs = None
                if jit_class.abstract:
                    cabs = "True"
                lod.append(
                    {
                        "schema": sn,
                        "class": current_class,
                        "slot": current_slot.name,
                        "slot_schema": current_slot.from_schema,
                        "source": current_slot.source,
                        "slot_title": current_slot.title,
                        "slot_group": current_slot.slot_group,
                        "slot_see_also": "|".join(current_slot.see_also),
                        "slot_mixin": smbs,
                        "slot_abstract": sabs,
                        "slot_is_a": current_slot.is_a,
                        "class_mixin": cmbs,
                        "class_abstract": cabs,
                        "class_is_a": jit_class.is_a,
                    }
                )
        print("")
        df = pd.DataFrame(lod)
        all_slots = set(self.slots_dict[sn])
        class_slots = set(df["slot"])
        no_class = list(all_slots - class_slots)
        no_class.sort()
        lod = []
        for current_nc in no_class:
            jit_slot = current_view.get_slot(current_nc)
            # if jit_slot.see_also:
            #     print(f"{jit_slot.name} see_also {jit_slot.see_also}")
            smbs = None
            if jit_slot.mixin:
                smbs = "True"
            sabs = None
            if jit_slot.abstract:
                sabs = "True"
            lod.append(
                {
                    "schema": sn,
                    "class": None,
                    "slot": current_nc,
                    "slot_schema": jit_slot.from_schema,
                    "source": jit_slot.source,
                    "slot_title": jit_slot.title,
                    "slot_group": jit_slot.slot_group,
                    "slot_see_also": "|".join(jit_slot.see_also),
                    "slot_mixin": smbs,
                    "slot_abstract": sabs,
                    "slot_is_a": jit_slot.is_a,
                }
            )
        df2 = pd.DataFrame(lod)
        print(df2)
        df3 = pd.concat([df, df2])
        self.frame_dict[sn] = df3

    def get_mongodb_collection_fields(self, coll_type):
        current_page = 1
        cumulative_bs = []
        while True:
            url = f"https://api.dev.microbiomedata.org/{coll_type}"
            # print(url)
            current_page = current_page + 1
            result = requests.get(url, params={"per_page": 200, "page": current_page})
            res_dict = result.json()
            res_res = res_dict["results"]
            res_len = len(res_res)
            print(f"page {current_page}: {res_len} from {coll_type}")
            if res_len == 0:
                break
            cumulative_bs = cumulative_bs + res_res
        as_df = pd.DataFrame(cumulative_bs)
        inferred_slots = list(as_df.columns)
        lod = []
        for current_inferred in inferred_slots:
            lod.append(
                {
                    "class": api_bit_to_class[coll_type],
                    "slot": current_inferred,
                    "mongodb": "True",
                }
            )
        df = pd.DataFrame(lod)
        return df


print("getting started")

sr = SlotRoster()

for current_path in input_paths:
    schema_name = sr.add_view_from_file(schema_file=current_path)
    sr.add_schema_slot_names(sn=schema_name)
    sr.add_schema_class_slots(sn=schema_name)

catted = pd.concat(sr.frame_dict.values(), ignore_index=True)

query = """
SELECT
    distinct class
from
    catted
where
    "schema" = 'NMDC'
    and slot_schema = 'https://microbiomedata/schema/mixs'
    and class != '' and class is not null
order by class
"""

mixs_slot_assoc_classes = sqldf.run(query)

mongo_frame_list = []
for current_associated in mixs_slot_assoc_classes["class"]:
    api_bit = class_to_api_bit[current_associated]
    inferred = sr.get_mongodb_collection_fields(api_bit)
    mongo_frame_list.append(inferred)

mongo_frame = pd.concat(mongo_frame_list)

# todo create underscored replacements for slot names

catted["slot_no_ws"] = catted["slot"].str.replace(" ", "_")

catted.rename(columns={"slot": "slot_raw", "slot_no_ws": "slot"}, inplace=True)

recat = catted.merge(right=mongo_frame, how="outer", on=["class", "slot"])

# todo are the recat slots used for biosamples?
#  do they already have any data in mongodb?
#  if yes/no, then just replace the old term with the new term?

# ---

# TODO should also be doing this with with nmdc_dh slots
#  schema = nmdc_dh, from_schema = https://example.com/nmdc_dh
#  would first want to remove anything that we know we added, like the EMSL and JGI slots...
#    emsl_mixin
#    jgi_mg_mixin
#    jgi_mt_mixin
#  BUT REVIEW expected new terms, wrt related MIxS terms? Do we shave see_also s?
#    samp_id_new_terms_mixin
#    soil_mixs_inspired_mixin

query = """
SELECT
    distinct class, slot
from
    recat
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
    recat
where
    "schema" = 'MIxS'
    and slot_schema = 'http://w3id.org/mixs/terms';
"""

now_available = sqldf.run(query)

na_set = set(now_available["slot"])

lost = list(set(legacy_mixs_usage["slot"]) - na_set)
lost.sort()

match_lod = []
for current_lost in lost:
    matches = difflib.get_close_matches(current_lost, na_set, n=3, cutoff=0.9)
    i = 1
    if len(matches) == 0:
        match_lod.append({"slot": current_lost, "no_good_match": True})
    for current_match in matches:
        match_lod.append({"slot": current_lost, "match": current_match, "rank": i})
match_frame = pd.DataFrame(match_lod)

include_intersection = list(na_set.intersection(set(legacy_mixs_usage["slot"])))
include_intersection.sort()

pprint.pprint(include_intersection)

merged = recat.merge(right=match_frame, how="left", on="slot")
temp = merged.loc[
    merged["slot_raw"].isin(list(match_frame["slot"])) & merged["schema"].eq("NMDC"),
    ["schema", "slot_raw", "match", "rank", "mongodb"],
]
temp.drop_duplicates(inplace=True)

print(temp)

merged.to_csv("../reports/slot_roster.tsv", sep="\t", index=False)
