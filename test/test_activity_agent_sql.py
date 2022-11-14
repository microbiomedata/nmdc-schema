import logging
import unittest

from linkml.generators.linkmlgen import LinkmlGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
# MetadataProfile
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper
# from linkml_runtime.loaders.yaml_loader import YAMLLoader
from linkml_runtime.loaders import yaml_loader

from was_associated_with import Database

SCHEMA = "../was_associated_with.yaml"
DATA = "../concrete_thing_set.yaml"


class TestActivityAgent(unittest.TestCase):
    def test_view(self):
        schemaview = SchemaView(SCHEMA)
        assert schemaview.schema.name == "was_associated_with"

    def test_generated(self):
        generator = LinkmlGenerator(SCHEMA, format='yaml')
        generated = generator.serialize()
        assert generated

    def test_schema_owl(self):
        generated = OwlSchemaGenerator(
            SCHEMA,
            mergeimports=False,
            metaclasses=False,
            type_objects=False,
            ontology_uri_suffix=".owl.ttl",
        ).serialize()
        assert generated

    def test_load_yaml(self):
        ly = yaml_loader.load(DATA, Database)  # instantiates Database
        assert ly

    def test_dump_json(self):
        log = logging.getLogger("TestActivityAgent.test_schema_ttl")
        ly = yaml_loader.load(DATA, Database)
        jd = json_dumper.dumps(ly)  # creates a JSON string
        log.warning(jd)
