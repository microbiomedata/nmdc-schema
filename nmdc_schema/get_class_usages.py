import csv

import click
from linkml_runtime.linkml_model.meta import ElementName, PatternExpression, Example
from linkml_runtime.utils.yamlutils import extended_str

import get_nmdc_view

import logging

from nmdc_schema.get_mixs_slots import MIxSSlotsGetter

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class Usages:
    view_getter = get_nmdc_view.ViewGetter()
    view = view_getter.get_view()

    mixs_slots_getter = MIxSSlotsGetter()
    mixs_slots = mixs_slots_getter.get_unique_slot_names()

    def get_class(self, class_name):
        selected_class = self.view.induced_class(class_name)
        return selected_class

    def get_class_usages(self, class_name):
        selected_class = self.get_class(class_name)
        selected_usages = selected_class.slot_usage
        return selected_usages

    def make_usage_rows(self, class_name):
        usage_rows = list()
        class_usages = self.get_class_usages(class_name)
        for uk, slotdef in class_usages.items():
            if uk in self.mixs_slots:
                from_mixs = True
            else:
                from_mixs = False
            slotdef_dict = slotdef.__dict__
            for k, v in slotdef_dict.items():
                if v and k != "name":
                    if type(v) == bool:
                        usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k, "value": str(v)}
                        usage_rows.append(usage_dict)
                    elif type(v) == dict:
                        if k == "annotations":
                            for ak, av in v.items():
                                usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": f"{k}:{ak}",
                                              "value": str(av.value)}
                                usage_rows.append(usage_dict)
                        else:
                            logger.warning(f"for {uk}, {k} is a dict with unknown type")
                    elif type(v) == ElementName:
                        usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k, "value": str(v)}
                        usage_rows.append(usage_dict)
                    elif type(v) == PatternExpression:
                        usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k, "value": str(v.syntax)}
                        usage_rows.append(usage_dict)
                    elif type(v) == extended_str:
                        usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k, "value": str(v)}
                        usage_rows.append(usage_dict)
                    elif type(v) == list:
                        if type(v[0]) == Example:
                            processed = [i.value for i in v]
                            processed = '|'.join(processed)
                            usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k,
                                          "value": str(processed)}
                            usage_rows.append(usage_dict)
                        elif type(v[0]) == extended_str:
                            processed = [i for i in v]
                            processed = '|'.join(processed)
                            usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k,
                                          "value": str(processed)}
                            usage_rows.append(usage_dict)
                        else:
                            logger.warning(f"for {uk}, {k}[0] has type {type(v)}")
                    elif type(v) == str:
                        usage_dict = {"slot": uk, "from_mixs": from_mixs, "slot_attribute": k, "value": v}
                        usage_rows.append(usage_dict)
                    else:
                        logger.warning(f"for {uk}, {k} has type {type(v)}")
        return usage_rows

    def write_usage_rows(self, class_name, report_file):
        usage_rows = self.make_usage_rows(class_name)
        with open(report_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["slot", "from_mixs", "slot_attribute", "value"], delimiter='\t')
            writer.writeheader()
            writer.writerows(usage_rows)


@click.command()
@click.option('--class_name', default='Biosample', help='Name of the class to generate the report for')
@click.option('--report_file', required=True, help='Name of the report file to be generated')
def generate_usage_report(class_name, report_file):
    usage_inst = Usages()
    usage_inst.write_usage_rows(class_name, report_file)


if __name__ == "__main__":
    generate_usage_report()
