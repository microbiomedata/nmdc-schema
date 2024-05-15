import pprint
import csv

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

from linkml_runtime.linkml_model.meta import SlotDefinition, ClassDefinition

# schema_file = "../schema/nmdc.yaml"
schema_file = "../../nmdc_schema/nmdc_materialized_patterns.yaml"
schema_view = SchemaView(schema_file)

schema_elements = schema_view.all_elements()

element_dict_list = []

for ek, ev in schema_elements.items():
    element_dict = {
        "key": ek,
        "abstract": None,
        "class_class_curie": ev.class_class_curie,
        "class_uri": None,
        "in_subset": '|'.join(ev.in_subset),
        "is_a": None,
        "is_grouping_slot": None,
        "name": ev.name,
        "slot_group": None,
        "slot_uri": None,
        "whitespace": " " in ev.name,
    }

    if ev.class_class_curie == "linkml:SlotDefinition":
        element_dict["slot_uri"] = ev.slot_uri
        element_dict["is_grouping_slot"] = ev.is_grouping_slot
        element_dict["slot_group"] = ev.slot_group

    if ev.class_class_curie not in ["linkml:TypeDefinition", "linkml:SubsetDefinition"]:
        element_dict["is_a"] = ev.is_a
        element_dict["abstract"] = ev.abstract

    if ev.class_class_curie == "linkml:ClassDefinition":
        element_dict["class_uri"] = ev.class_uri
        # as_class: ClassDefinition = schema_view.get_class(ek)
        # print(yaml_dumper.dumps(as_class))
        # # # element_dict["uri"] = as_slot

    element_dict_list.append(element_dict)

output_file = "schema_elements.tsv"
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, delimiter="\t", fieldnames=element_dict_list[0].keys())
    writer.writeheader()
    writer.writerows(element_dict_list)

dg_id = schema_view.induced_slot("id", "DataGeneration")
print(yaml_dumper.dumps(dg_id))

ns_id = schema_view.induced_slot("id", "NucleotideSequencing")
print(yaml_dumper.dumps(ns_id))

ms_id = schema_view.induced_slot("id", "MassSpectrometry")
print(yaml_dumper.dumps(ms_id))

dg_set_range = schema_view.induced_slot("data_generation_set", "Database").range
print(yaml_dumper.dumps(dg_set_range))

