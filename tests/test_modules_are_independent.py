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
            print(schema_module)
            view = SchemaView(schema_module)
            print(view.schema.name)
            # save the json representation of view.schema into a string
            generated = jsg.JsonSchemaGenerator(schema=view.schema)
            generated_text = generated.serialize()

            assert generated_text is not None


class TestModulesForOwl(unittest.TestCase):
    """Test that modules can be independently converted to OWL."""

    def test_modules_are_independent(self):
        """Test that modules are independent."""

        schema_modules = [
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/basic_slots.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/chemical_converion_process.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/core.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/external_identifiers.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/mixs.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/nmdc_types.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/portal_emsl.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/portal_jgi_metagenomics.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/portal_jgi_metatranscriptomics.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/portal_mixs_inspired.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/portal_sample_id.yaml',
            '/home/mark/gitrepos/berkeley-schema-fy24/tests/../src/schema/workflow_execution_activity.yaml'  # warnings
        ]

        for schema_module in schema_modules:
            print(schema_module)
            view = SchemaView(schema_module)
            print(view.schema.name)
            generated = og.OwlSchemaGenerator(schema=view.schema)
            generated_text = generated.serialize()

            assert generated_text is not None
