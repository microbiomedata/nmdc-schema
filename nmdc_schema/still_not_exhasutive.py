import pprint

import yaml

with open("src/schema/nmdc.yaml", 'r') as stream:
    try:
        schema_dict = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)

with open("src/data/valid/Biosample-exhaustive.yaml", 'r') as stream:
    try:
        big_data_dict = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)

biosample_slots = schema_dict['classes']['Biosample']['slots']
big_data_slots = list(big_data_dict.keys())

slots_missing_from_big_data = [x for x in biosample_slots if x not in big_data_slots]

pprint.pprint(slots_missing_from_big_data)
