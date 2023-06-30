import os
import sqlite3

import requests
import pandas as pd
import click
import requests_cache
from dotenv import load_dotenv


# https://en.wikipedia.org/wiki/USDA_soil_taxonomy


def remove_trailing_char(string, removal_char):
    if string.endswith(removal_char):
        return string.rstrip(removal_char)
    else:
        return string


def load_vars_from_env_file(env_file) -> None:
    load_dotenv(env_file)


def get_neon_token() -> str:
    return os.getenv("NEON_TOKEN")


@click.command()
@click.option('--envo-sqlite', default='local/envo.db', help='Path to ENVO SQLite database file')
@click.option("--dotenv-file", type=click.Path(exists=True), default="local/.env", help="Path to .env file")
@click.option('--soil-core-collection-csv-in', default='local/sls_soilCoreCollection.csv',
              help='Path to sls_soilCoreCollection.csv')
@click.option('--neon-site-envo-soil-mappings-tsv', default='local/neon-site-envo-soil-mappings.tsv',
              help='Path to output TSV file')
def generate_soil_order_envo_mappings(envo_sqlite, soil_core_collection_csv_in, dotenv_file,
                                      neon_site_envo_soil_mappings_tsv):
    load_vars_from_env_file(dotenv_file)

    url_base = "https://data.neonscience.org/api/v0/locations"

    token = get_neon_token()

    headers = {'X-API-Token': token}

    requests_cache.install_cache('neon_cache', backend='sqlite', expire_after=43200)  # 12 hours

    sls_soilCoreCollection_frame = pd.read_csv(soil_core_collection_csv_in, low_memory=False)
    named_location_counts = sls_soilCoreCollection_frame['namedLocation'].value_counts()
    # print(named_location_counts)

    named_locations_unique_list = named_location_counts.index.tolist()
    named_locations_unique_list.sort()

    location_count = len(named_locations_unique_list)

    soil_types_lod = []
    for idx, i in enumerate(named_locations_unique_list):
        print(f"{i} = {idx + 1} of {location_count}")

        soil_type_dict = {
            "envo_label_style": "soil",
            "site": i,
        }

        url = f"{url_base}/{i}"

        response = requests.get(url, headers=headers).json()

        if 'data' not in response:
            print("Skipping", i)
            continue

        location_properties_list = response['data']['locationProperties']
        for location_property in location_properties_list:

            if location_property['locationPropertyName'] == 'Value for Soil type order':
                neon_style = location_property['locationPropertyValue']
                envo_label_style = remove_trailing_char(neon_style.lower(), 's')
                soil_type_dict = {
                    "envo_label_style": envo_label_style,
                    "site": i,
                    "site_soil_type_order": location_property['locationPropertyValue'],
                }
                continue
        soil_types_lod.append(soil_type_dict)

    # pprint.pprint(soil_types_lod)

    site_soil_types_frame = pd.DataFrame(soil_types_lod)

    soil_types_frame = site_soil_types_frame[['envo_label_style', 'site_soil_type_order']].copy()
    soil_types_frame.drop_duplicates(inplace=True)

    envo_nlcd_alt_mappings_q = """
select
	ee.subject , s.value 
from
	entailed_edge ee
join statements s on
	s.subject = ee.subject
where
	ee."object" = "ENVO:00001998"
	and ee.predicate = "rdfs:subClassOf"
	and s.predicate = "rdfs:label"
    """

    conn = sqlite3.connect(envo_sqlite)
    c = conn.cursor()
    c.execute(envo_nlcd_alt_mappings_q)
    envo_soil_labels = c.fetchall()
    conn.close()

    # turn the sqlite results into a pandas dataframe
    envo_soil_labels_frame = pd.DataFrame(envo_soil_labels,
                                          columns=['envo_term', 'envo_label'])

    merged_df = pd.merge(soil_types_frame, envo_soil_labels_frame, left_on='envo_label_style', right_on='envo_label',
                         how='outer')

    merged_df.to_csv(neon_site_envo_soil_mappings_tsv, index=False, sep='\t')


if __name__ == '__main__':
    generate_soil_order_envo_mappings()
