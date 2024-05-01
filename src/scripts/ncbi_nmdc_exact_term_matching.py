import xml.etree.ElementTree as ET

import requests
import pandas as pd

from linkml_runtime.utils.schemaview import SchemaView


# ==================================================================================== #
#                                 Automated mapping                                    #
# Exact term matching of NMDC schema slots with NCBI BioSample Attribute names         #
# ==================================================================================== #

# Load dataframe containing all the slots from the NMDC schema that need to be mapped
# to "names" of NCBI BioSample Attributes. The slots that are being mapped belong to
# the following classes: Biosample, Extraction, LibraryPreparation, OmicsProcessing,
# DataObject. The "names" of the NCBI BioSample Attributes can be either the
# harmonized name, synonym, or attribute name (display name)
df = pd.read_csv("assets/ncbi_mappings/ncbi_attribute_mappings.tsv", delimiter="\t")

# ncbi_biosample.xml: https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml
# Parse the XML to create a dictionary of Attribute harmonized_names and their synonyms
resp = requests.get(
    "https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml"
)
with open("assets/ncbi_mappings/ncbi_biosample.xml", "wb") as foutput:
    foutput.write(resp.content)

tree = ET.parse("assets/ncbi_mappings/ncbi_biosample.xml")
root = tree.getroot()

# Read in the list of all NCBI BioSample Attribute names that are available in the
# NCBI BioSample database
attribute_dict = {}
for attribute in root.findall(".//Attribute"):
    harmonized_name = attribute.find("HarmonizedName").text
    attribute_name = attribute.find("Name").text
    synonyms = [synonym.text for synonym in attribute.findall("Synonym")]
    synonyms.append(attribute_name)
    attribute_dict[harmonized_name] = synonyms


# Function to apply mapping based on the attribute dictionary
def map_attributes(row, attribute_dict):
    for harmonized_name, aliases in attribute_dict.items():
        if (
            row["NMDC schema slot"].lower()
            in [harmonized_name.lower() for harmonized_name in aliases]
            or row["NMDC schema slot"].lower() == harmonized_name.lower()
        ):
            return harmonized_name
    return row["NCBI BioSample Attribute name"]


df["NCBI BioSample Attribute name"] = df.apply(
    map_attributes, axis=1, args=(attribute_dict,)
)

# Save the filtered DataFrame to a new TSV file
df.to_csv(
    "assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv", sep="\t", index=False
)

# ==================================================================================== #
#                               Post mapping reporting                                 #
# Reporting on the number of slots that were successfully mapped and those that were   #
# not mapped.                                                                          #
# ==================================================================================== #

df = pd.read_csv(
    "assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv", delimiter="\t"
)

def unmapped_slots(df, schema_class, attribute_name):
    filtered_df = df[df["NMDC schema class"] == schema_class]
    unmapped_slots = filtered_df[filtered_df[attribute_name].isna()]
    return unmapped_slots["NMDC schema slot"].tolist()

unmapped_biosample_slots = unmapped_slots(df, "Biosample", "NCBI BioSample Attribute name")

sv = SchemaView("src/schema/nmdc.yaml")

classes_to_be_reported = ["Biosample", "Extraction", "LibraryPreparation", "OmicsProcessing", "DataObject"]
imports_to_be_ignored = ["https://w3id.org/nmdc/portal/emsl", 
                         "https://w3id.org/nmdc/portal/jgi_metagenomics",
                         "https://w3id.org/nmdc/portal/jgi_metatranscriptomics",
                         "https://w3id.org/nmdc/portal/mixs_inspired",
                         "https://w3id.org/nmdc/portal/sample_id",
                        ]

for class_name in classes_to_be_reported:
    class_slots = sv.class_induced_slots(class_name)
    unmapped_slot_names = unmapped_slots(df, class_name, "NCBI BioSample Attribute name")

    for slot in class_slots:
        if slot.from_schema in imports_to_be_ignored and slot.name in unmapped_slot_names:
            df.loc[df["NMDC schema slot"] == slot.name, "NCBI BioSample Attribute name"] = "IGNORE"

df.to_csv(
    "assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv", sep="\t", index=False
)