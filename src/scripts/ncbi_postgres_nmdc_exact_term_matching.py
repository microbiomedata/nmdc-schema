import os

import xml.etree.ElementTree as ET

import requests
import pandas as pd
import psycopg2
from dotenv import load_dotenv

env_path = os.path.join("local", ".env")
load_dotenv(dotenv_path=env_path)


# ==================================================================================== #
#         Get the names of all fields/columns from the NCBI Postgres view              #
# ==================================================================================== #
def get_column_names_from_view(view_name):
    ncbi_postgres_user = os.getenv("BIOSAMPLES_RDB_USER")
    ncbi_postgres_password = os.getenv("BIOSAMPLES_RDB_PWD")

    conn = psycopg2.connect(
        dbname="ncbi_biosamples_feb26",
        user=ncbi_postgres_user,
        password=ncbi_postgres_password,  # email spatil@lbl.gov / MAM@lbl.gov for the password
        host="localhost",
        port="15432",
    )
    cur = conn.cursor()
    try:
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{view_name}';"
        cur.execute(query)
        column_names = [row[0] for row in cur.fetchall()]
        return column_names
    finally:
        cur.close()
        conn.close()


view_name = "attributes_plus"
column_names = get_column_names_from_view(view_name)
column_names.sort()

with open("assets/ncbi_mappings/ncbi_pg_db_fields.txt", "w") as file:
    for i, column_name in enumerate(column_names):
        file.write(column_name)
        if i != len(column_names) - 1:
            file.write("\n")

# ==================================================================================== #
#                       First round of automated mapping                               #
# Exact term matching of NMDC schema slots with fields/columns from NCBI Postgres view #
# ==================================================================================== #

# Load dataframe of all the slots from the NMDC schema that need to be mapped
# to fields/columns from NCBI Postgres view
df = pd.read_csv("assets/ncbi_mappings/ncbi_pg_db_field_mappings.tsv", delimiter="\t")

# Read the list of all NCBI BioSample attributes that are available
# in the NMDC Postgres dump of the NCBI BioSample database
with open("assets/ncbi_mappings/ncbi_pg_db_fields.txt", "r") as file:
    attributes_list = [line.strip() for line in file]

# Find exact matches between the schema slots and the column names
df.loc[df["NMDC schema slot"].isin(attributes_list), "NCBI postgres field name"] = df[
    "NMDC schema slot"
]

# ==================================================================================== #
#                       Second round of automated mapping                              #
# Exact term matching of NMDC schema slot with display names and synonyms              #
# from ncbi_biosample.xml                                                              #
# ==================================================================================== #


# ncbi_biosample.xml: https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml
# Parse the XML to create a dictionary of attribute harmonized_names and their synonyms
resp = requests.get(
    "https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml"
)
with open("assets/ncbi_mappings/ncbi_biosample.xml", "wb") as foutput:
    foutput.write(resp.content)

tree = ET.parse("assets/ncbi_mappings/ncbi_biosample.xml")
root = tree.getroot()

attribute_dict = {}
for attribute in root.findall(".//Attribute"):
    attribute_name = attribute.find("HarmonizedName").text
    name = attribute.find("Name").text
    synonyms = [synonym.text for synonym in attribute.findall("Synonym")]
    synonyms.append(name)
    attribute_dict[attribute_name] = synonyms


# Function to apply mapping based on the attribute dictionary
def map_attributes(row, attribute_dict):
    for harmonized_name, synonyms in attribute_dict.items():
        if row["NMDC schema slot"] in synonyms:
            return harmonized_name
    return row["NCBI postgres field name"]


# Apply the mapping function only to rows where the "NCBI postgres field name" is NaN
is_null = df["NCBI postgres field name"].isnull()
df.loc[is_null, "NCBI postgres field name"] = df[is_null].apply(
    map_attributes, axis=1, args=(attribute_dict,)
)

# Save the filtered DataFrame to a new TSV file
df.to_csv(
    "assets/ncbi_mappings/ncbi_pg_db_field_mappings_filled.tsv", sep="\t", index=False
)
