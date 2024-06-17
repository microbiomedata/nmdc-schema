import click
import csv
from linkml_runtime import SchemaView


# Command line interface function
@click.command()
@click.option('--schema-file', default='nmdc_schema/nmdc_materialized_patterns.yaml',
              help='Path to the schema YAML file.')
@click.option('--output-file', default='assets/element-scrutiny.tsv', help='Path to the output TSV file.')
def process_schema_elements(schema_file, output_file):
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

        element_dict_list.append(element_dict)

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, delimiter="\t", fieldnames=element_dict_list[0].keys())
        writer.writeheader()
        writer.writerows(element_dict_list)


if __name__ == '__main__':
    process_schema_elements()
