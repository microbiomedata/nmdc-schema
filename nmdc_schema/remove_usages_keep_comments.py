from linkml_runtime.linkml_model import SlotDefinition
from ruyaml import YAML

yaml = YAML()

with open('src/schema/nmdc.yaml') as f:
    nmdc_yaml_dict = yaml.load(f)

if 'classes' in nmdc_yaml_dict and 'Biosample' in nmdc_yaml_dict['classes'] and 'slot_usage' in \
        nmdc_yaml_dict['classes']['Biosample']:
    print("removing Biosample.slot_usage")
    del nmdc_yaml_dict['classes']['Biosample']['slot_usage']
else:
    print("no Biosample.slot_usage to remove")

# print("adding blank Biosample.slot_usage")
# nmdc_yaml_dict['classes']['Biosample']['slot_usage'] = {}

with open('src/schema/nmdc_no_bs_usage.yaml', 'w') as f:
    yaml.dump(nmdc_yaml_dict, f)

sd = SlotDefinition(name='slot_usage', range='string', multivalued=True, description='A slot usage')

