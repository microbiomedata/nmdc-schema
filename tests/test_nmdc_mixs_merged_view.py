import logging

import unittest

from linkml_runtime import SchemaView


class TestNmdcMixsMergedView(unittest.TestCase):
    def test_create_nmdc_mixs_view(self):
        nmdc_mixs_url = "https://raw.githubusercontent.com/microbiomedata/mixs/main/model/schema/mixs.yaml"
        nmdc_mixs_merged_view = SchemaView(nmdc_mixs_url)
        # print(nmdc_mixs_merged_view.schema.name)
        self.assertEqual(nmdc_mixs_merged_view.schema.name, "MIxS")

    def test_is_merged(self):
        nmdc_mixs_url = "https://raw.githubusercontent.com/microbiomedata/mixs/main/model/schema/mixs.yaml"
        nmdc_mixs_merged_view = SchemaView(nmdc_mixs_url)
        soil = nmdc_mixs_merged_view.get_element("soil")
        self.assertIsNotNone(soil)


if __name__ == "__main__":
    unittest.main()
