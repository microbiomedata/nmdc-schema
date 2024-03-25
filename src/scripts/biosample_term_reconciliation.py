import pprint

import yaml
from linkml_runtime import SchemaView
import requests
import xmltodict
from linkml_runtime.dumpers import yaml_dumper

mixs_module = "../schema/mixs.yaml"

ncbi_biosample_attributes_xml_url = "https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml"

output_file = "../../assets/biosample_term_reconciliation.yaml"

response = requests.get(ncbi_biosample_attributes_xml_url)

# Ensure the request was successful
if response.status_code == 200:
    # Parse the XML response to a dictionary
    ncbi_biosample_attributes_dict = xmltodict.parse(response.content)
else:
    print(f"Failed to fetch data from {ncbi_biosample_attributes_xml_url}. Status code: {response.status_code}")
    ncbi_biosample_attributes_dict = {}

mixs_module_view = SchemaView(mixs_module)

mixs_module_slots = mixs_module_view.all_slots()

ncbi_list = []
for ncbi_attribute in ncbi_biosample_attributes_dict['BioSampleAttributes']['Attribute']:
    ncbi_list.append(ncbi_attribute['HarmonizedName'])

nmdc_mixs_list = []
for nmdc_mixs_slot in list(mixs_module_slots.keys()):
    if len(mixs_module_view.slot_descendants(nmdc_mixs_slot)) == 1:  # ignore parent slots/slot groups
        nmdc_mixs_list.append(nmdc_mixs_slot)
    else:
        print(f"ignoring {mixs_module_view.slot_descendants(nmdc_mixs_slot)}")

        # Convert lists to sets
        ncbi_set = set(ncbi_list)
        nmdc_mix_set = set(nmdc_mixs_list)

        # Find the differences
        only_in_ncbi = ncbi_set - nmdc_mix_set
        only_in_nmdc_mix = nmdc_mix_set - ncbi_set

        # Store in a dictionary and sort the lists
        difference_dict = {
            'only_in_ncbi': sorted(list(only_in_ncbi)),
            'only_in_nmdc_mix': sorted(list(only_in_nmdc_mix))
        }

        # pprint.pprint(difference_dict)

        # Write the dictionary to a YAML file
        with open(output_file, 'w') as file:
            yaml.dump(difference_dict, file)

            # for i in sorted(list(only_in_nmdc_mix)):
            #     slot = mixs_module_view.get_slot(i)
            #     # print(yaml_dumper.dumps(slot))
            #     print(f"{i}: {slot.is_a}")
