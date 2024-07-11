import json
import unittest

from nmdc_data import get_nmdc_file_type_enums, get_nmdc_yaml_bytes, get_nmdc_yaml_string, \
    get_materialized_nmdc_yaml_string, get_nmdc_jsonschema_bytes, get_nmdc_jsonschema_string, \
    get_nmdc_jsonschema_dict, get_nmdc_jsonschema, get_nmdc_schema_definition, \
    get_nmdc_file_type_enums_json, get_gold_sssom


class TestNmdcData(unittest.TestCase):

    def test_get_nmdc_yaml_bytes(self):
        assert b'NMDC Schema' in get_nmdc_yaml_bytes()

    def test_get_nmdc_yaml_string(self):
        assert 'NMDC Schema' in get_nmdc_yaml_string()

    def test_get_materialized_nmdc_yaml_string(self):
        assert 'NMDC Schema' in get_materialized_nmdc_yaml_string()

    def test_get_nmdc_jsonschema_bytes(self):
        json_schema = json.loads(get_nmdc_jsonschema_bytes())
        assert json_schema["title"] == "NMDC"

    def test_get_nmdc_jsonschema_string(self):
        json_schema = json.loads(get_nmdc_jsonschema_string())
        assert json_schema["title"] == "NMDC"

    def test_get_nmdc_jsonschema_dict(self):
        json_schema = get_nmdc_jsonschema_dict()
        assert json_schema["title"] == "NMDC"

    def test_get_nmdc_jsonschema(self):
        assert "NMDC" in get_nmdc_jsonschema()

    def test_get_nmdc_schema_definition(self):
        schema_definition = get_nmdc_schema_definition()
        assert schema_definition.title == "NMDC Schema"

    def test_get_nmdc_file_type_enums(self):
        file_types = get_nmdc_file_type_enums()
        for file_type in file_types:
            assert file_type["name"]
            assert file_type["description"]

    def test_get_nmdc_file_type_enums_json(self):
        assert len(get_nmdc_file_type_enums_json()) > 100

    def test_get_gold_sssom(self):
        assert len(get_gold_sssom()) > 100
