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
def class_report(model_path, tsv_output_file):
    print("reading meta model")
    meta_view = SchemaView('https://w3id.org/linkml/meta')
    cis = meta_view.class_induced_slots('class_definition')
    cis_names = [i.name for i in cis]
    cis_names.sort()

    print(f"reading {model_path}")
    my_view = SchemaView(model_path)
    my_classes = my_view.all_classes()
    my_class_names = list(my_classes.keys())
    my_class_names.sort()

    table_rows = []
    for current_class_name in my_class_names:
        row_dict = {'class_name': current_class_name}
        for current_cis in cis_names:
            current_class_def = my_classes[current_class_name]
            if current_cis in current_class_def:
                current_val = current_class_def[current_cis]
                if current_val == [] or current_val == {} or current_val == jsonasobj2._jsonobj.JsonObj():
                    current_val = ""
                row_dict[current_cis] = current_val
        temp = row_dict.copy()
        table_rows.append(temp)

    schema_frame = pd.DataFrame(table_rows)
    sf_cols = list(schema_frame.columns)
    first_col = sf_cols[0:1]
    to_remove = first_col + ['name']
    after_removal = [x for x in sf_cols if x not in to_remove]
    after_removal.sort()
    reordered_cols = first_col + after_removal
    reordered_frame = schema_frame[reordered_cols]

    reordered_frame.to_csv(tsv_output_file, index=False, sep="\t")


if __name__ == '__main__':
    class_report()
