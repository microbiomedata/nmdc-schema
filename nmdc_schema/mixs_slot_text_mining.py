import csv
import logging
import os
import pprint
import re
from typing import List, Dict, Set, Any

import click
import click_log

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


def replace_underscores(string):
    return string.replace("_", " ")


def split_string(string):
    return re.findall(r'\b\w+\b', string)


def lowercase_strings_in_list(string_list):
    return [s.lower() for s in string_list]


def trim_strings_in_list(string_list):
    return [s.strip() for s in string_list]


class MixsSlotTextMining:
    def __init__(self, label_file_mapping: Dict[str, str], tsv_file_root: str, dtm_tsv: str) -> None:
        self.label_file_mapping = label_file_mapping
        self.tsv_file_root = tsv_file_root
        self.dtm_tsv: str = os.path.join(tsv_file_root, dtm_tsv)
        self.token_set_dict: Dict[str, Set[str]] = {}
        self.token_list_dict: Dict[str, List[str]] = {}
        self.dtm_list: List[Dict[str, Any]] = []

    @staticmethod
    def tsv_file_to_dict_list(tsv_file):
        with open(tsv_file) as f:
            reader = csv.DictReader(f, delimiter="\t")
            return list(reader)

    def tsv_files_to_dict_list(self):
        for label, tsv_file in self.label_file_mapping.items():
            tsv_path = os.path.join(self.tsv_file_root, tsv_file)
            print(f"Reading {label} file: {tsv_path}")
            row_list = self.tsv_file_to_dict_list(tsv_path)
            for row in row_list:
                sc_name = row['Structured comment name']
                self.token_set_dict.setdefault(sc_name, set())
                for key in ('Structured comment name', 'Package item', 'Item (rdfs:label)'):
                    if key in row:
                        no_underscores = replace_underscores(row[key])
                        splitted = split_string(no_underscores)
                        lowercased = lowercase_strings_in_list(splitted)
                        trimmed = trim_strings_in_list(lowercased)
                        self.token_set_dict[sc_name].update(trimmed)

    def change_set_to_sorted_list(self):
        for key, value in self.token_set_dict.items():
            self.token_list_dict[key] = sorted(list(value))

    def make_document_term_matrix(self):
        self.dtm_list = []
        for slot_name, sorted_tokens in self.token_list_dict.items():
            row = {'slot_name': slot_name}
            for token in sorted_tokens:
                row[token] = 1
            self.dtm_list.append(row)
        # print(self.dtm_list)

    def write_dtm_tsv(self):
        tsv_cols = list(set().union(*(d.keys() for d in self.dtm_list)))
        tsv_cols.remove('slot_name')
        tsv_cols.sort()
        tsv_cols.insert(0, 'slot_name')

        with open(self.dtm_tsv, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=tsv_cols, delimiter="\t")
            writer.writeheader()
            for row in self.dtm_list:
                writer.writerow(row)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--core_file", required=True)
@click.option("--packages_file", required=True)
@click.option("--output_file", required=True)
def cli(
        core_file,
        packages_file,
        output_file,
):
    MIxS_6_term_updates_tabs = {"core": core_file, "packages": packages_file}
    MIxS_6_term_updates_prefix = ""
    MIxS_6_term_updates_dtm_tsv = output_file
    mining_instance = MixsSlotTextMining(MIxS_6_term_updates_tabs, MIxS_6_term_updates_prefix,
                                         MIxS_6_term_updates_dtm_tsv)
    mining_instance.tsv_files_to_dict_list()
    mining_instance.change_set_to_sorted_list()
    mining_instance.make_document_term_matrix()
    mining_instance.write_dtm_tsv()


if __name__ == "__main__":
    cli()
