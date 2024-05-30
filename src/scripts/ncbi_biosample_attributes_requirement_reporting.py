import pprint
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import yaml

# URLs and filenames
url = "https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml"

output_xml_file = 'ncbi_biosample_attributes_rewrite.xml'
tsv_output_file = 'ncbi_biosample_attributes_requirement.tsv'
group_data_tsv_output_file = 'ncbi_biosample_attribute_group_requirement.tsv'
value_counts_tsv_output_file = 'attribute_requirement_counts.tsv'
yaml_output_file = 'attribute_group_members.yaml'

# Fetch the XML content from the URL
response = requests.get(url)
xml_content = response.text

# Parse the XML content
root = ET.fromstring(xml_content)

# Write the ElementTree to a well-formed XML file
tree = ET.ElementTree(root)
tree.write(output_xml_file, encoding='utf-8', xml_declaration=True)

# Set to collect unique node names
unique_nodes = set()

# Iterate through all Attribute nodes and collect unique node names
for attribute in root.findall('Attribute'):
    for child in attribute:
        unique_nodes.add(child.tag)

# Print all unique node names
print("Unique node names:")
for node in unique_nodes:
    print(node)

# Initialize dictionaries to hold the data
attribute_data = {}
group_data = {}
attribute_groups = {}

# Iterate through all Attribute nodes
for attribute in root.findall('Attribute'):
    harmonized_name = attribute.find('HarmonizedName').text
    if harmonized_name not in attribute_data:
        attribute_data[harmonized_name] = {}

    # Iterate through all Package nodes within the Attribute node
    for package in attribute.findall('Package'):
        package_name = package.text
        use_value = package.attrib.get('use')
        attribute_data[harmonized_name][package_name] = use_value

        if use_value == 'either_one_mandatory':
            group_name = package.attrib.get('group_name')

            if group_name not in group_data:
                group_data[group_name] = {}
            if group_name not in attribute_groups:
                attribute_groups[group_name] = set()

            group_data[group_name][package_name] = 'true'
            attribute_groups[group_name].add(harmonized_name)

# Convert the dictionaries to DataFrames
attribute_df = pd.DataFrame.from_dict(attribute_data, orient='index').fillna('')
group_data_df = pd.DataFrame.from_dict(group_data, orient='index').fillna('')

# Convert attribute_groups to a readable format with sorted lists
attribute_groups_dict = {k: sorted(list(v)) for k, v in attribute_groups.items()}

# Save the attribute DataFrame to a TSV file
attribute_df.to_csv(tsv_output_file, sep="\t", index_label='harmonized_name')

# Save the group data DataFrame to a TSV file
group_data_df.to_csv(group_data_tsv_output_file, sep="\t", index_label='group_name')

# Save the attribute groups dictionary to a YAML file
with open(yaml_output_file, 'w') as yaml_file:
    yaml.dump(attribute_groups_dict, yaml_file, sort_keys=True)

# Get value counts for the entire DataFrame, including NaNs
use_value_counts = attribute_df.stack().value_counts(dropna=False)

# Save the value counts to a TSV file
use_value_counts.to_csv(value_counts_tsv_output_file, sep="\t", header=['count'])

# Inform the user of the saved files
print(f"Data saved to the following files:\n"
      f"{output_xml_file}\n"
      f"{tsv_output_file}\n"
      f"{group_data_tsv_output_file}\n"
      f"{value_counts_tsv_output_file}\n"
      f"{yaml_output_file}")
