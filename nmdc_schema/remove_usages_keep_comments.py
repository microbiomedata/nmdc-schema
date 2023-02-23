from ruyaml import YAML

with open('src/schema/nmdc.yaml') as f:
    nmdc_yaml_dict = YAML().load(f)

if 'classes' in nmdc_yaml_dict and 'Biosample' in nmdc_yaml_dict['classes'] and 'slot_usage' in \
        nmdc_yaml_dict['classes']['Biosample']:
    print("removing Biosample.slot_usage")
    del nmdc_yaml_dict['classes']['Biosample']['slot_usage']
else:
    print("no Biosample.slot_usage to remove")

with open('src/schema/nmdc_no_bs_usage.yaml', 'w') as f:
    YAML().dump(nmdc_yaml_dict, f)
