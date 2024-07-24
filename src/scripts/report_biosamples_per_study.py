import pprint
import click
import requests
from typing import Dict


# Command line entry point
@click.command()
@click.option('--api-server', default="api", help='Hostname of the API server.')
@click.option('--max-page-size', default=10000, type=int,
              help='Maximum number of items per page. Pagination is not currenlty implmented. If there is a next_page_token, this program will terminate without reporting anything.')
def query_biosamples(api_server, max_page_size):
    """
    This script fetches collection stats and biosamples from the specified API,
    computes the counts of biosamples per study, and displays them as objects.
    """

    projection = "part_of"

    url = f"https://{api_server}.microbiomedata.org/nmdcschema/collection_stats"
    collection_stats_response = requests.get(url)
    collection_stats = collection_stats_response.json()

    biosample_count = 0
    for current_collection in collection_stats:
        if current_collection['ns'] == 'nmdc.biosample_set':
            biosample_count = current_collection['storageStats']['count']
            print(f"{biosample_count} Biosamples at '{api_server}'")
            print("\n")

    url = f"https://{api_server}.microbiomedata.org/nmdcschema/biosample_set"
    params = {
        "max_page_size": min(max_page_size, biosample_count + 1),
        "projection": projection
    }

    biosample_part_hood_response = requests.get(url, params=params)
    biosample_part_hood_payload = biosample_part_hood_response.json()
    bsph_keys = biosample_part_hood_payload.keys()

    if 'next_page_token' in bsph_keys:
        click.echo(
            "We didn't get all of the Biosamples and will need to paginate. Yes, I just threw away all of your data.")
        return

    biosample_part_hood = biosample_part_hood_payload['resources']

    # Create a dictionary to store the count for each study
    study_count: Dict[str, int] = {}

    # Iterate through the data
    for item in biosample_part_hood:
        study_ids = item['part_of']
        for study_id in study_ids:
            # Increment the count for each study_id
            study_count[study_id] = study_count.get(study_id, 0) + 1

    sorted_study_count = sorted(study_count.items(), key=lambda x: x[1], reverse=True)

    click.echo("ALPHABETICALLY")
    pprint.pprint(study_count)
    click.echo("\n")
    click.echo("BY COUNT")
    pprint.pprint(sorted_study_count)
    click.echo("\n")

    click.echo(
        f"{len(sorted_study_count)} studies with at least one Biosample part. There may be other studies with no Biosamples.")


if __name__ == '__main__':
    query_biosamples()
