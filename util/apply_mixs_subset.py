import logging
from typing import Optional, Dict, List  # Any

import click
import click_log
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model.meta import SlotDefinition
from linkml_runtime.utils.schemaview import SchemaView

# import pprint

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


class ViewClass:

    def __init__(self):
        self.view: Optional[SchemaView] = None
        self.element_subset_report: Optional[List[Dict]] = None
        self.schema_path: Optional[str] = None

    def populate_view(self):
        self.view = SchemaView(self.schema_path)

    # todo only reporting terms that are in at least one subset
    def get_element_subset_report(self):
        elements = self.view.all_elements()
        report = []
        for k, v in elements.items():
            if len(v.in_subset):
                elem_type_label = 'unknown'
                elem_type = type(v)
                if elem_type == SlotDefinition:
                    elem_type_label = 'slot'
                report.append({'element_type': elem_type_label, 'element_name': v.name, 'subsets': v.in_subset})
        self.element_subset_report = report

    def dump_element_subset_report(self):
        temp = yaml_dumper.dumps(self.element_subset_report)
        return temp

    def apply_subsets_to_slots(self, desired_subset: str) -> None:
        slots = self.view.all_slots()
        slot_names = list(slots.keys())
        slot_names.sort()
        for i in slot_names:
            logger.debug(i)
            current_subsets = slots[i].in_subset
            current_subsets.append(desired_subset)
        #     print(current_subsets)
        #     try:
        #         temp = yaml_dumper.dumps(slots[i])
        #         print(temp)
        #     except Exception as e:
        #         print(e)
        # print(yaml_dumper.dumps(self.view.schema))

    def dump_schema(self, yaml_file: str):
        yaml_dumper.dump(self.view.schema, yaml_file)


# mixs_path = "../src/schema/mixs.yaml"
# "mixs_with_mixs_subset.yaml")
@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--model_file", type=click.Path(exists=True), required=True)
@click.option("--yaml_output", type=click.Path(), required=True)
@click.option("--desired_subset", required=True)
def apply_mixs_subset(model_file: str, desired_subset: str, yaml_output: str):
    """
    Gets slots, listed in config_tsv, from source_model and puts them in recipient_model
    :param model_file:
    :param desired_subset:
    :param yaml_output:
    :return:
    """

    mixs_view = ViewClass()
    mixs_view.schema_path = model_file
    mixs_view.populate_view()

    # mixs_view.get_element_subset_report()
    # dumped = mixs_view.dump_element_subset_report()
    # pprint.pprint(dumped)

    mixs_view.apply_subsets_to_slots(desired_subset)

    mixs_view.dump_schema(yaml_output)


if __name__ == "__main__":
    apply_mixs_subset()
