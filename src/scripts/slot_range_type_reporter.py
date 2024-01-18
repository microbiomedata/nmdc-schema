import click
import pprint
from linkml_runtime import SchemaView
import csv


@click.command()
@click.option('-s', '--schema', default='src/schema/nmdc.yaml', help='Path to schema file')
@click.option('-o', '--output', default='slot-range-type-report.tsv', help='Output TSV file path')
@click.option('-c', '--schema-class', default='Biosample', help='Class name to analyze')
def cli(schema, output, schema_class):
    field_names = [
        "slot_name",
        "range",
        "metatype",
        "asserted_inlined",
        "asserted_inlined_as_list",
        "multivalued",
        "asserted_range_uri",
        "inferred_range_uri",
        "ranges_identifying_slot",
        "inferred_inlined",
    ]

    schema_view = SchemaView(schema)

    induced_class = schema_view.induced_class(schema_class)

    induced_slots = induced_class.attributes

    slot_rows = []

    for sk, sv in induced_slots.items():
        current_range = sv.range
        current_element = schema_view.get_element(current_range)
        current_metatype = type(current_element).class_name
        current_inlined = sv.inlined
        current_inlined_as_list = sv.inlined_as_list
        current_multivalued = sv.multivalued
        class_identifying_name = None
        asserted_range_uri = None
        inferred_range_uri = None
        inferred_inlined = False
        if current_metatype == "class_definition":
            asserted_range_uri = current_element.class_uri
            inferred_range_uri = f"{schema_view.schema.default_prefix}:{current_element.name}"
            class_identifying_slot = schema_view.get_identifier_slot(sv.range)
            if class_identifying_slot:
                class_identifying_name = class_identifying_slot.name
            else:
                inferred_inlined = True
        temp_dict = {
            "slot_name": sk,
            "range": current_range,
            "metatype": current_metatype,
            "asserted_inlined": current_inlined,
            "asserted_inlined_as_list": current_inlined_as_list,
            "multivalued": current_multivalued,
            "asserted_range_uri": asserted_range_uri,
            "inferred_range_uri": inferred_range_uri,
            "ranges_identifying_slot": class_identifying_name,
            "inferred_inlined": inferred_inlined,
        }
        slot_rows.append(temp_dict)

    with open(output, 'w', newline='') as tsv_file:
        writer = csv.DictWriter(tsv_file, fieldnames=field_names, delimiter='\t')

        writer.writeheader()
        writer.writerows(slot_rows)


if __name__ == '__main__':
    cli()
