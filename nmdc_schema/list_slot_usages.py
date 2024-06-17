import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = '../nmdc_schema/nmdc_schema_merged.yaml'

ignored_slots = [
    'aliases',
    'annotations',
    'comments',
    'examples',
    'maximum_cardinality',
    'minimum_cardinality',
    'multivalued',
    'name',
    'notes',
    'pattern',
    'range',
    'required',
    'structured_pattern',
    'title',
    'todos',
]  # todo which of these are reasonable as slot_usage?

schema_view = SchemaView(schema_file)

schema_classes = schema_view.all_classes()

for ck, cv in schema_classes.items():
    if "slot_usage" in cv and cv["slot_usage"]:
        su = cv["slot_usage"]
        for suk, suv in su.items():
            suv_dict = suv.__dict__
            for uk, uv in suv_dict.items():
                useful_dict = {}
                if uk not in ignored_slots and uv:
                    useful_dict[uk] = uv
                if useful_dict:
                    print(f"{suk} used in {ck}")
                    pprint.pprint(useful_dict)
