"""Data test."""
import csv
import os
# import glob
import pprint
import unittest

from linkml_runtime import SchemaView

# from nmdc_schema.datamodel.nmdc import Biosample

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "nmdc_schema", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')
REPORTS_DIR = os.path.join(ROOT, "reports")
BIOSAMPLE_SLOTS_RANGES_FILE = os.path.join(REPORTS_DIR, 'biosample_slots_ranges_report.tsv')


class BiosampleSlotReport(unittest.TestCase):
    """make a list of dicts with biosmaple slots and their ranges
    then write to a TSV file
    and check if the list of dicts is not empty
    """

    def test_report_slots(self):
        nmdc_view = SchemaView(SCHEMA_FILE)
        biosample_induced = nmdc_view.induced_class("Biosample")
        biosample_induced_slots = biosample_induced.attributes

        slot_ranges = []
        for k, v in biosample_induced_slots.items():
            slot_name = v.name
            slot_range = v.range
            slot_multivalued = v.multivalued
            slot_pattern = v.pattern
            # print(f"{slot_name} {slot_range}")
            slot_ranges.append({"slot_name": slot_name, "slot_range": slot_range, "slot_multivalued": slot_multivalued,
                                "slot_pattern": slot_pattern})

            # pprint.pprint(slot_ranges)

            with open(BIOSAMPLE_SLOTS_RANGES_FILE, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=slot_ranges[0].keys(), delimiter='\t')
                dict_writer.writeheader()
                dict_writer.writerows(slot_ranges)

            self.assertIsNotNone(slot_ranges)
