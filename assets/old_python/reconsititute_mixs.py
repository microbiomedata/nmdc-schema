# Any
import pprint
from typing import Dict, Optional, List

import pymongo
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition

import difflib


# id: https://microbiomedata/schema/mixs
# name: mixs-schema
# title: MIxS Schema


class TermBroker:
    recon_schema_name = "mixs_for_nmdc_biosamples"
    recon_schema_prefix = "http://example.com/"
    recon_schema_id = f"{recon_schema_prefix}{recon_schema_name}"
    # todo why aren't I using my dependency resolver?!
    recon_schema_imports = ["core"]
    # horizon is not a parent term
    static_parent_imports = [
        "core field",
        "environment field",
        "investigation field",
        "nucleic acid sequence source field",
        "sequencing field",
    ]
    static_renamed_imports = {
        "tot_nitro_cont_meth": "tot_nitro_content_meth",
        "water_cont_soil_meth": "water_content_soil_meth",
    }

    # todo refactor
    non_mixs_6_slots = {
        "env_package": "lost_in_mixs_6",
        "horizon": "nmdc_mixs_5_and_6",
        "link_addit_analys": "nmdc_mixs_5_and_6",
        "microbial_biomass_meth": "nmdc_mixs_5_and_6",
        "pool_dna_extracts": "nmdc_mixs_5_and_6",
        "previous_land_use_meth": "nmdc_mixs_5_and_6",
        "samp_collect_device": "nmdc_mixs_5_and_6",
        "texture": "nmdc_mixs_5_and_6",
        "texture_meth": "nmdc_mixs_5_and_6",
        "tot_nitro_content_meth": "renamed_in_mixs_6",
        "water_content_soil_meth": "renamed_in_mixs_6",
        "chimera_check": "nmdc_use-omics_processing",
        "nucl_acid_amp": "nmdc_use-omics_processing",
        "nucl_acid_ext": "nmdc_use-omics_processing",
        "pcr_cond": "nmdc_use-omics_processing",
        "pcr_primers": "nmdc_use-omics_processing",
        "samp_vol_we_dna_ext": "nmdc_use-omics_processing",
        "seq_meth": "nmdc_use-omics_processing",
        "seq_quality_check": "nmdc_use-omics_processing",
        "target_gene": "nmdc_use-omics_processing",
        "target_subfragment": "nmdc_use-omics_processing",
    }

    def __init__(self):
        self.term_dol: Optional[Dict[str, List[str]]] = {}
        self.view_dict: Optional[Dict[str, SchemaView]] = {}

    def add_view_from_file(self, view_alias: str, schema_file: str):
        view = SchemaView(schema_file)
        self.view_dict[view_alias] = view

    def add_term_list(self, list_alias: str, term_list: List):
        self.term_dol[list_alias] = term_list

    def get_schema_slot_names(
        self, view_alias: str, incl_imports: bool = True
    ) -> List[str]:
        current_view = self.view_dict[view_alias]
        current_slot_obj = current_view.all_slots(imports=incl_imports)
        current_slot_names = [v.name for k, v in current_slot_obj.items()]
        current_slot_names.sort()
        return current_slot_names

    def get_class_slot_names(self, view_alias: str, class_name: str) -> List[str]:
        current_view = self.view_dict[view_alias]
        # print(current_view.schema.name)
        # print(class_name)
        cis = current_view.class_induced_slots(class_name)
        current_slot_names = [i.name for i in cis]
        current_slot_names.sort()
        return current_slot_names

    def get_mongodb_coll_slot_names(
        self, mongo_client, db_name: str, coll_name: str, query: Dict
    ) -> List[str]:
        mydb = mongo_client[db_name]
        mycol = mydb[coll_name]
        mydocs = mycol.find(query)

        all_mdb_bs_keys = set()
        for current_doc in mydocs:
            current_keys = list(current_doc.keys())
            all_mdb_bs_keys |= set(current_keys)

        all_mdb_bs_keys = list(all_mdb_bs_keys)
        all_mdb_bs_keys.sort()

        return all_mdb_bs_keys

    def list_diff(self, list1: List, list2: List) -> List:
        s1 = set(list1)
        s2 = set(list2)
        s_diff = s1 - s2
        l_diff = list(s_diff)
        l_diff.sort()
        return l_diff

    def do_reconstitution(
        self, view_alias: str, legacy_alias: str, slot_name_list: List[str]
    ) -> SchemaDefinition:
        current_schema = SchemaDefinition(
            name=self.recon_schema_name, id=self.recon_schema_id
        )
        current_view = self.view_dict[view_alias]

        legacy_view = self.view_dict[legacy_alias]

        all_slots = (
            slot_name_list
            + self.static_parent_imports
            + list(self.static_renamed_imports.keys())
        )
        all_slots.sort()

        for current_sn in all_slots:
            print(current_sn)
            current_slot = current_view.get_slot(current_sn)
            if current_sn in self.static_renamed_imports:
                current_slot.annotations["MIxS_5_name"] = self.static_renamed_imports[
                    current_sn
                ]
                # cs_yd = yaml_dumper.dumps(current_slot)
            if current_slot.examples:
                if len(current_slot.examples) == 1:
                    if current_slot.examples[0].value == "":
                        current_slot.examples = None

            # todo use old range at least through April 22 release
            legacy_slot = legacy_view.get_slot(current_sn)
            if legacy_slot:
                current_slot.range = legacy_slot.range
                current_slot.is_a = legacy_slot.is_a
                current_slot.multivalued = legacy_slot.multivalued
                current_slot.see_also.append(
                    "https://docs.google.com/document/d/1Vf8wHrElpvk01rMIdnNDt02bE4L2TyfTVR4QR5i7uEo"
                )

            current_slot.source = current_slot.from_schema
            current_schema.slots[current_sn] = current_slot

        # todo refactor
        for k, v in self.non_mixs_6_slots.items():
            print(f"extra slot {k} ({v})")
            extra_view = self.view_dict["nmdc_mixs_5"]
            extra_slot = extra_view.get_slot(k)
            extra_slot.source = extra_view.schema.id
            current_schema.slots[k] = extra_slot

        # todo why aren't I using my dependency resolver?!
        for current_import in self.recon_schema_imports:
            current_schema.imports.append(current_import)
        current_schema.enums = current_view.all_enums()

        return current_schema


tb = TermBroker()

tb.add_view_from_file(view_alias="nmdc_mixs_5", schema_file="src/schema/mixs.yaml")
tb.add_view_from_file(view_alias="nmdc_root", schema_file="src/schema/nmdc.yaml")
tb.add_view_from_file(view_alias="mixs6", schema_file="mixs/model/schema/mixs.yaml")
tb.add_view_from_file(
    view_alias="nmdc_dh",
    schema_file="https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/issue-100-netlify-linkml-datastructure/artifacts/nmdc_dh.yaml",
)

# print(tb.view_dict['nmdc_dh'].schema.name)

nmdc_mixs_5_slot_names = tb.get_schema_slot_names(
    view_alias="nmdc_mixs_5", incl_imports=False
)
# pprint.pprint(nmdc_mixs_5_slot_names)

mixs_6_slot_names = tb.get_schema_slot_names(view_alias="mixs6", incl_imports=True)
# pprint.pprint(mixs_6_slot_names)

nmdc_biosample_slot_names = tb.get_class_slot_names(
    view_alias="nmdc_root", class_name="biosample"
)
# # ValueError: No such slot: link_addit_analys and no attribute by that name in ancestors of biosample
# # when importing mixs_new into nmdc
# pprint.pprint(nmdc_biosample_slot_names)

with open("local/secrets.yaml", "r") as stream:
    try:
        secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

mongodb_suffix = "@localhost:27027/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

myclient = pymongo.MongoClient(
    f"mongodb://{secrets['nmdc_mongodb']['username']}:{secrets['nmdc_mongodb']['password']}{mongodb_suffix}"
)

# todo make this more general
myquery = {"ncbi_taxonomy_name": "sediment metagenome"}

mongodb_biosample_slot_names = tb.get_mongodb_coll_slot_names(
    mongo_client=myclient, db_name="nmdc", coll_name="biosample_set", query=myquery
)

nmdc_mixs_5_mixs_6_shared_slot_names = list(
    set(nmdc_mixs_5_slot_names).intersection(set(mixs_6_slot_names))
)
nmdc_mixs_5_mixs_6_shared_slot_names.sort()
# pprint.pprint(nmdc_mixs_5_mixs_6_shared_slot_names)

lost_mixs_slots = tb.list_diff(nmdc_mixs_5_slot_names, mixs_6_slot_names)
# pprint.pprint(lost_mixs_slots)

lost_biosample_mixs_slots = list(
    set(lost_mixs_slots).intersection(set(nmdc_biosample_slot_names))
)
lost_biosample_mixs_slots.sort()
# pprint.pprint(lost_biosample_mixs_slots)

lost_biosample_mixs_mongodb_slots = list(
    set(lost_biosample_mixs_slots).intersection(set(mongodb_biosample_slot_names))
)
lost_biosample_mixs_mongodb_slots.sort()
# pprint.pprint(lost_biosample_mixs_mongodb_slots)

nmdc_dh_mixs_6_slotnames = tb.get_schema_slot_names(
    view_alias="nmdc_dh", incl_imports=True
)

# pprint.pprint(nmdc_dh_mixs_6_slotnames)

unwieldly = list(
    set(nmdc_mixs_5_mixs_6_shared_slot_names).intersection(
        set(nmdc_dh_mixs_6_slotnames)
    )
)

unwieldly.sort()

reconstituted = tb.do_reconstitution(
    view_alias="mixs6", legacy_alias="nmdc_mixs_5", slot_name_list=unwieldly
)
# recon_text = yaml_dumper.dumps(reconstituted)
# print(recon_text)

yaml_dumper.dump(reconstituted, "src/schema/mixs_new.yaml")
