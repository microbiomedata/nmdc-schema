"""Data test."""
import os
import glob
import unittest

from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from attributes_of_biosamples.datamodel import Collection

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        for path in EXAMPLE_FILES:
            print(path)
            obj = yaml_loader.load(path, target_class=Collection)
            print(yaml_dumper.dumps(obj))
            assert obj
