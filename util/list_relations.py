import csv

# from linkml_runtime.dumpers import yaml_dumper
# import pprint
from linkml_runtime import SchemaView

# todo may need to interrogate subclasses

schema_file = "../src/schema/nmdc.yaml"
output_tsv = "../list_relations.tsv"

fieldnames = ['subject_class', 'slot', 'object_class']

print("loading schema")

schema_view = SchemaView(schema_file)

schema_database_attribs = schema_view.induced_class('Database').attributes
database_ables = [v.range for k, v in schema_database_attribs.items()]
database_ables.sort()

with open(output_tsv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for current_class_name in database_ables:
        for akk, akv in schema_view.induced_class(current_class_name).attributes.items():
            if akv.range in database_ables:
                # print(f"{current_class_name} {akk} {akv.range}")
                writer.writerow({'subject_class': current_class_name, 'slot': akk, 'object_class': akv.range})
