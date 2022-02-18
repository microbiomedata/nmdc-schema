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
def slot_report(model_path, tsv_output_file):
    print("reading meta model")
    meta_view = SchemaView('https://w3id.org/linkml/meta')
    sis = meta_view.class_induced_slots('slot_definition')
    sis_names = [i.name for i in sis]
    sis_names.sort()

    # nmdc_schema_file = '../src/schema/nmdc.yaml'
    print(f"reading {model_path}")
    my_view = SchemaView(model_path)
    my_classes = my_view.all_classes()
    my_class_names = list(my_classes.keys())
    my_class_names.sort()

    table_rows = []
    for current_class_name in my_class_names:
        row_dict = {'class_name': current_class_name}
        cc_ind_slots = my_view.class_induced_slots(current_class_name)
        ccis_names = [i.name for i in cc_ind_slots]
        ccis_dict = dict(zip(ccis_names, cc_ind_slots))
        ccis_names.sort()
        for current_is_name in ccis_names:
            row_dict['slot_name'] = current_is_name
            current_is = ccis_dict[current_is_name]
            for current_sis_name in sis_names:
                if current_sis_name in current_is:
                    current_value = current_is[current_sis_name]
                    if current_value == [] or current_value == jsonasobj2._jsonobj.JsonObj():
                        current_value = ""
                    row_dict[current_sis_name] = current_value
            temp = row_dict.copy()
            table_rows.append(temp)

    schema_frame = pd.DataFrame(table_rows)
    sf_cols = list(schema_frame.columns)
    first_two = sf_cols[0:2]
    to_remove = first_two + ['name']
    after_removal = [x for x in sf_cols if x not in to_remove]
    after_removal.sort()
    reordered_cols = first_two + after_removal
    reordered_frame = schema_frame[reordered_cols]

    reordered_frame.to_csv(tsv_output_file, index=False, sep="\t")


if __name__ == '__main__':
    slot_report()
