import os
import pprint
import unittest

import jsonasobj2
from linkml.validator import validate
from linkml_runtime import SchemaView


def create_schema_view():
    return SchemaView(SCHEMA_FILE)


ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "nmdc_schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc_materialized_patterns.yaml')


class TestReportBiosampleSlotsWithUCUM(unittest.TestCase):

    def test_report_biosample_slots_with_ucum_constraint(self):
        """
        Test to ensure that the report_biosample_slots_with_ucum_constraint function
        correctly identifies and reports biosample slots with UCUM constraints.
        """

        schema_view = create_schema_view()

        print("\n")

        otherwise_schema_valid_biosample_dict = {'associated_studies': ['nmdc:sty-00-abc123'],
                                                 'env_broad_scale': {'term': {'id': 'ENVO:00002030',
                                                                              'type': 'nmdc:OntologyClass'},
                                                                     'type': 'nmdc:ControlledIdentifiedTermValue'},
                                                 'env_local_scale': {'term': {'id': 'ENVO:00002169',
                                                                              'type': 'nmdc:OntologyClass'},
                                                                     'type': 'nmdc:ControlledIdentifiedTermValue'},
                                                 'env_medium': {
                                                     'term': {'id': 'ENVO:00005792', 'type': 'nmdc:OntologyClass'},
                                                     'type': 'nmdc:ControlledIdentifiedTermValue'},
                                                 'id': 'nmdc:bsm-99-dtTMNb',
                                                 'temp': {'has_numeric_value': 20,
                                                          'has_raw_value': '20.0 C',
                                                          'has_unit': 'C',
                                                          'type': 'nmdc:QuantityValue'},
                                                 'type': 'nmdc:Biosample'}

        report = validate(otherwise_schema_valid_biosample_dict, SCHEMA_FILE, "Biosample")

        assert len(report.results) == 0, "Biosample should be valid but has errors: " + pprint.pformat(report)

        biosample_ucum_annotations = {}

        induced_biosample_attributes = schema_view.induced_class("Biosample").attributes

        for k, v in induced_biosample_attributes.items():
            if v.annotations:
                annotations_dict = jsonasobj2.as_dict(v.annotations)
                if "nmdc_mongodb_ucum_symbol" in annotations_dict and annotations_dict["nmdc_mongodb_ucum_symbol"]:
                    biosample_ucum_annotations[k] = annotations_dict["nmdc_mongodb_ucum_symbol"]["value"]

        assert biosample_ucum_annotations["temp"] == "Cel"

        for k, v in biosample_ucum_annotations.items():
            if k in otherwise_schema_valid_biosample_dict:
                assert otherwise_schema_valid_biosample_dict[k]['has_unit'] == v, \
                    f"Expected unit {v} for biosample slot '{k}', but found {otherwise_schema_valid_biosample_dict[k]['has_unit']}"
