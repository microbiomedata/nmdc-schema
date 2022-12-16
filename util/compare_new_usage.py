import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

import ruamel.yaml

from deepdiff import DeepDiff \
# print_diff

schema_file = "../src/schema/nmdc.yaml"
slots_added_in_induction = ['owner','domain_of']
schema_view = SchemaView(schema_file)

global_extreme_event = schema_view.get_slot("extreme_event")
biosample_extreme_event = schema_view.induced_slot("extreme_event", "Biosample")

# refactor
# or better yet, direct element -> text dict conversion
# and vice versa
gee_yaml = yaml_dumper.dumps(global_extreme_event)
gee_dict = ruamel.yaml.load(gee_yaml, Loader=ruamel.yaml.RoundTripLoader)

bee_yaml = yaml_dumper.dumps(biosample_extreme_event)
bee_dict = ruamel.yaml.load(bee_yaml, Loader=ruamel.yaml.RoundTripLoader)
for i in slots_added_in_induction:
    del bee_dict[i]

print("Global extreme event")
pprint.pprint(gee_dict)

print("\n")
print("Biosample extreme event")
pprint.pprint(bee_dict)

diff = DeepDiff(gee_dict, bee_dict)

print("\n")
pprint.pprint(diff)
