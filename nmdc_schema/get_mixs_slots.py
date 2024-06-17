import csv
import pprint
import urllib.request

import csv
import io
import urllib.request
from typing import List


class MIxSSlotsGetter:
    # switch to retrieving from GSC' mixs.yaml
    def any_mixs_sheet_getter(self, url):
        response = urllib.request.urlopen(url)
        tsv_file = io.StringIO(response.read().decode('utf-8'))

        rows = []

        # Parse the file using DictReader
        reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in reader:
            rows.append(row)

        return rows

    def extract_vals_from_rows(self, rows, var_name):
        slots = []
        for row in rows:
            if var_name in row and row[var_name] != '':
                slots.append(row[var_name])
        slots.sort()
        return slots

    def get_unique_slot_names(self,
                              var_name: str = "Structured comment name",
                              url_list: List[str] = (
                                      "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=178015749&format=tsv",
                                      "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=750683809&format=tsv"
                              )):
        slot_names = set()
        for url in url_list:
            parsed = self.any_mixs_sheet_getter(url)
            per_page_slots = self.extract_vals_from_rows(parsed, var_name)
            slot_names.update(per_page_slots)
        slot_names = list(slot_names)
        slot_names.sort()
        return slot_names
