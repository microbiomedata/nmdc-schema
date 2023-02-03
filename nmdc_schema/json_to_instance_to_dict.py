import pprint
import urllib.request

from linkml_runtime.dumpers import json_dumper
from linkml_runtime.loaders import json_loader

from nmdc_schema.nmdc import Database

study_database_url = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/assets/test/data/study_test.json"
response = urllib.request.urlopen(study_database_url)
response_text = response.read().decode("utf-8")

study_database_instance = json_loader.load(source=response_text, target_class=Database)

study_database_dict = json_dumper.to_dict(study_database_instance)

pprint.pprint(study_database_dict)
