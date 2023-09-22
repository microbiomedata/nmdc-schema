import re

import yaml
import sqlite3
import pandas as pd
import click


# Hugh has already provided a partial, highly curated mapping
# Harry is looking into oaklib/ontogpt solutions


# nlcd metadata is included in each release from the
#   Multi-Resolution Land Characteristics (MRLC) Consortium
# this page highlights the MRLC land cover releases for the Continental US
#   https://www.mrlc.gov/data?f%5B0%5D=category%3ALand%20Cover&f%5B1%5D=region%3Aconus
# make sure we are using the same version an NEON
# Here I will illustrate the use of "NLCD 2019 Land Cover (CONUS)"
# click on the faint "More" link in the lower right-hand corner of the  "NLCD 2019 Land Cover (CONUS)" tile
# click on the "Metadata" link
# that will take you to an XML document wth sections like

# what's edom?
# are there any other authorities on this subject?
# envthes?

# <attrdomv>
#   <edom>
#     <edomv>43</edomv>
#       <edomvd>Mixed Forest - Areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. Neither deciduous nor evergreen species are greater than 75 percent of total tree cover.</edomvd>
#       <edomvds>NLCD Legend Land Cover Class Descriptions</edomvds>
#   </edom>
# </attrdomv>

# have not been able to parse that file with newbie style XML parsing
# so start by downloading and converting to YAML with local/nlcd_2019_land_cover_l48_20210604.yaml
#   in project.Makefile

# ABBY_002.basePlot.bgc
# namedLocation in sls_soilCoreCollection.csv -> location lookup
#   https://data.neonscience.org/api/v0/locations/ABBY_002.basePlot.bgc
# locationProperties
#       {
#         "locationPropertyName": "Value for Soil type order",
#         "locationPropertyValue": "Andisols"
#       },


@click.command()
@click.option('--nlcd-yaml', default='local/nlcd_2019_land_cover_l48_20210604.yaml', help='Path to NLCD YAML file')
@click.option('--envo-sqlite', default='local/envo.db', help='Path to ENVO SQLite database file')
@click.option('--neon-nlcd-envo-mappings-tsv', default='local/neon-nlcd-envo-mappings.tsv',
              help='Path to output TSV file')
def generate_nlcd_envo_mappings(nlcd_yaml, envo_sqlite, neon_nlcd_envo_mappings_tsv):
    with open(nlcd_yaml, "r") as stream:
        try:
            nlcd_dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    detailed_attrs = nlcd_dict['metadata']['eainfo']['detailed']['attr']

    edoms = []
    for detailed_attr in detailed_attrs:
        if detailed_attr['attrdefs'] == 'NLCD Legend Land Cover Class Descriptions':
            edoms = detailed_attr['attrdomv']
            break

    edom_lod = []
    for edom in edoms:
        extracted_portion = edom['edom']['edomvd'].split(' -')[0]

        # Remove whitespace and punctuation, and split into words
        words = re.findall(r'\w+', extracted_portion)

        # Convert to lower camel case
        lower_camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

        envo_style_alt_id = f"NLCD:{edom['edom']['edomv']}"

        edom_dict = {
            "envo_style_alt_id": envo_style_alt_id,
            "full_desc": edom['edom']['edomvd'],
            "num_key": edom['edom']['edomv'],
            'extractedPortion': extracted_portion,
            'lowerCamelCase': lower_camel_case,
        }
        edom_lod.append(edom_dict)

    # Define the field names based on the keys in the dictionaries
    fieldnames = edom_lod[0].keys()

    # convert that list of dictionaries into a pandas dataframe
    edom_df = pd.DataFrame(edom_lod)

    envo_nlcd_alt_mappings_q = """
    select
        s1.subject, s1.value, s2.value
    from
        statements s1
    join statements s2 on s1.subject = s2.subject 
    where
        s1.predicate  = 'oio:hasAlternativeId' and s1.value like 'NLCD:%'
        and s2.predicate = "rdfs:label"
    """

    conn = sqlite3.connect(envo_sqlite)
    c = conn.cursor()
    c.execute(envo_nlcd_alt_mappings_q)
    envo_nlcd_alt_mappings = c.fetchall()
    conn.close()

    # turn the sqlite results into a pandas dataframe
    envo_nlcd_alt_mappings_df = pd.DataFrame(envo_nlcd_alt_mappings,
                                             columns=['envo_term', 'nlcd_mapping', 'envo_label'])

    merged_df = pd.merge(edom_df, envo_nlcd_alt_mappings_df, left_on='envo_style_alt_id', right_on='nlcd_mapping',
                         how='outer')

    merged_df.to_csv(neon_nlcd_envo_mappings_tsv, index=False, sep='\t')


if __name__ == '__main__':
    generate_nlcd_envo_mappings()
