"""Data test."""
import os
import pprint
import unittest

import yaml


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error reading YAML file {file_path}: {e}")
            return None


ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "nmdc_schema")

SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc_schema_merged.yaml')


class TestAllClassesAssertAClassUri(unittest.TestCase):

    def test_all_classes_assert_a_class_uri(self):
        print("\n")

        schema_class_names = set()
        schema_classes_asserting_uri_names = set()

        schema_dict_from_merged = read_yaml(SCHEMA_FILE)
        schema_classes = schema_dict_from_merged['classes']
        for ck, cv in schema_classes.items():
            schema_class_names.add(ck)
            if 'class_uri' in cv:
                schema_classes_asserting_uri_names.add(ck)

        class_names_not_asserting_class_uri = list(schema_class_names - schema_classes_asserting_uri_names)

        self.assertListEqual(class_names_not_asserting_class_uri, [],
                             msg="Classes not asserting a class_uri: " + str(class_names_not_asserting_class_uri))
