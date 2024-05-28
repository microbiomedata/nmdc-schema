import unittest
import linkml.generators.jsonschemagen as jsg
import linkml.generators.owlgen as og
import os
from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")

schema_modules = []

for root, dirs, files in os.walk(SCHEMA_DIR):
    for file in files:
        if file.endswith(".yaml"):
            schema_modules.append(os.path.join(root, file))


class TestModulesAreIndependent(unittest.TestCase):
    """Test that modules can be independently converted to JSON schema."""

    def test_modules_are_independent(self):
        """Test that modules are independent."""

        schema_modules.sort()

        for schema_module in schema_modules:
            if schema_module.endswith("deprecated.yaml"):
                continue
            view = SchemaView(schema_module)
            generated = jsg.JsonSchemaGenerator(schema=view.schema)
            generated_text = generated.serialize()

            assert generated_text is not None


class TestModulesForOwl(unittest.TestCase):
    """Test that modules can be independently converted to OWL."""

    def test_modules_are_independent(self):
        """Test that modules are independent."""

        # schema_modules = [
        # ] # could test a defined subset

        for schema_module in schema_modules:
            if schema_module.endswith("deprecated.yaml"):
                continue
            view = SchemaView(schema_module)
            generated = og.OwlSchemaGenerator(schema=view.schema)
            generated_text = generated.serialize()

            assert generated_text is not None
