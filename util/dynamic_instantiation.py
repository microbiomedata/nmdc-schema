from linkml_runtime.dumpers import yaml_dumper, json_dumper
from linkml_runtime.loaders import json_loader

from nmdc_schema.nmdc import Biosample, ControlledTermValue
import importlib

#   "@type": "Biosample"

bs_json = """
{
  "id": "bs:1",
  "part_of": [
    "s:1"
  ],
  "env_broad_scale": {
    "has_raw_value": "term [ontology:id]"
  },
  "env_local_scale": {
    "has_raw_value": "term [ontology:id]"
  },
  "env_medium": {
    "has_raw_value": "term [ontology:id]"
  }
}"""

dynamic_class_name = "Biosample"

# dynamic_class = getattr(importlib.import_module("nmdc_schema.nmdc"), dynamic_class_name)


dynamic_class = getattr(importlib.import_module("target.python.nmdc"), dynamic_class_name)

# dynamic_class = getattr(importlib.import_module(name="../nmdc_schema", package="nmdc"), dynamic_class_name)

instance = json_loader.loads(bs_json, target_class=dynamic_class)

print(json_dumper.dumps(instance))
