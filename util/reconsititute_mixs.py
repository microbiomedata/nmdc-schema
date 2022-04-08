import pprint
# Any
from typing import Dict, Optional, List

import pymongo
from linkml_runtime import SchemaView

import yaml


class TermBroker:

    def __init__(self):
        self.term_dol: Optional[Dict[str, List[str]]] = {}
        self.view_dict: Optional[Dict[str, SchemaView]] = {}

    def add_view_from_file(self, view_alias: str, schema_file: str):
        view = SchemaView(schema_file)
        self.view_dict[view_alias] = view

    def add_term_list(self, list_alias: str, term_list: List):
        self.term_dol[list_alias] = term_list

    def get_schema_slot_names(self, view_alias: str, incl_imports: bool = True) -> List[str]:
        current_view = self.view_dict[view_alias]
        current_slot_obj = current_view.all_slots(imports=incl_imports)
        current_slot_names = [v.name for k, v in current_slot_obj.items()]
        current_slot_names.sort()
        return current_slot_names

    def get_class_slot_names(self, view_alias: str, class_name: str) -> List[str]:
        current_view = self.view_dict[view_alias]
        cis = current_view.class_induced_slots(class_name)
        current_slot_names = [i.name for i in cis]
        current_slot_names.sort()
        return current_slot_names

    def get_mongodb_coll_slot_names(self, mongo_client, db_name: str, coll_name: str, query: Dict) -> List[str]:
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


tb = TermBroker()

tb.add_view_from_file(view_alias="nmdc_mixs_5", schema_file="../src/schema/mixs.yaml")
tb.add_view_from_file(view_alias="nmdc_root", schema_file="../src/schema/nmdc.yaml")
tb.add_view_from_file(view_alias="mixs6", schema_file="../mixs/model/schema/mixs.yaml")

nmdc_mixs_5_slot_names = tb.get_schema_slot_names(view_alias="nmdc_mixs_5", incl_imports=False)
# pprint.pprint(nmdc_mixs_5_slot_names)

mixs_6_slot_names = tb.get_schema_slot_names(view_alias="mixs6", incl_imports=True)
# pprint.pprint(mixs_6_slot_names)

nmdc_biosample_slot_names = tb.get_class_slot_names(view_alias="nmdc_root", class_name="biosample")
# pprint.pprint(nmdc_biosample_slot_names)

with open("../local/secrets.yaml", 'r') as stream:
    try:
        secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

myclient = pymongo.MongoClient(
    f"mongodb://mam:{secrets['nmdc_mongodb_pw']}@localhost:27027/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

# todo make this more general
myquery = {"ncbi_taxonomy_name": "sediment metagenome"}

mongodb_biosample_slot_names = tb.get_mongodb_coll_slot_names(mongo_client=myclient, db_name="nmdc",
                                                              coll_name="biosample_set", query=myquery)

sample_diff = tb.list_diff(mongodb_biosample_slot_names, mixs_6_slot_names)
pprint.pprint(sample_diff)
