from linkml_runtime.utils.schemaview import SchemaView
import pandas as pd

import logging

import click
import click_log

import jsonasobj2

logger = logging.getLogger(__name__)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--model_path", type=click.Path(exists=True), help="")
@click.option("--tsv_output_file", type=click.Path(), required=True)
def enum_report(model_path, tsv_output_file):
    print("reading meta model")
    meta_view = SchemaView('https://w3id.org/linkml/meta')
    cis = meta_view.class_induced_slots('class_definition')
    cis_names = [i.name for i in cis]
    cis_names.sort()

    print(f"reading {model_path}")
    my_view = SchemaView(model_path)
    my_enums = my_view.all_enums()
    my_enum_names = list(my_enums.keys())
    my_enum_names.sort()

    table_rows = []
    for current_enum in my_enum_names:
        for current_pv in my_enums[current_enum].permissible_values:
            table_rows.append({'enum_name': current_enum, "pv_name": current_pv})

    schema_frame = pd.DataFrame(table_rows)

    schema_frame.to_csv(tsv_output_file, index=False, sep="\t")


if __name__ == '__main__':
    enum_report()
