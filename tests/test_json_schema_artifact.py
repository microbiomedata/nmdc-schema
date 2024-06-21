import json
import pkgutil
import unittest
import fastjsonschema

from nmdc_schema import nmdc_data


class TestJsonSchemaArtifact(unittest.TestCase):
    def test_artifact_compiles_with_fastjsonschema(self):
        """Test that the NMDC JSON Schema compiles with fastjsonschema

        This is an important use case because nmdc-runtime uses fastjsonschema to validate data
        against the schema. fastjsonschema has slightly different behavior than the jsonschema,
        which underlies the linkml-validate command.
        """
        json_schema = nmdc_data.get_nmdc_jsonschema_dict()
        validate = fastjsonschema.compile(json_schema)
        data = validate({})
        assert data == {}

    def test_materialized_pattern_artifact_compiles_with_fastjsonschema(self):
        """Test that the NMDC JSON Schema with materialized patterns compiles with fastjsonschema"""
        json_schema_bytes = pkgutil.get_data("nmdc_schema",
                                             "nmdc_materialized_patterns.schema.json")
        json_schema = json.loads(json_schema_bytes)
        validate = fastjsonschema.compile(json_schema)
        data = validate({})
        assert data == {}
