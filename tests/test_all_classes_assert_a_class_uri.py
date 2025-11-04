import unittest

import yaml

from tests import SCHEMA_FILE


# TODO: Follow best practices and switch to SchemaView for consistency,
# though raw YAML access is safe here since class URIs don't involve inheritance
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


class TestAllClassesAssertAClassUri(unittest.TestCase):

    def test_all_classes_assert_a_class_uri(self):
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
