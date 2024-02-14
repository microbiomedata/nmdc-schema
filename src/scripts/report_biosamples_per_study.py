# THIS IS ALL IRRELEVANT FOR NOW SINCE THE AGGREGATION QUERY IS NOT YET AVAILABLE ON THE NAPA API

# visit https://api-dev.microbiomedata.org/docs
#   todo: when will  aggregation query running be available on the production or napa APIs?
# click authorize
# for now, enter username and password in the OAuth2PasswordOrClientCredentialsBearer (OAuth2, password) form
#  some additional authentication methods are already available and still more are to be added
#  then it will all be simplified and documented better
# todo MAM add notes about who can provide credentials to new contributors
#  ??? how do we programmatically get the token? Or view it on a dashboard?
# for now, we probably have to inspect the site's cookies in a browser
# or use the Swagger UI to run a post query. After it is run, copy the Authorization: Bearer value
# from the rendered Curl command

import pprint
from typing import Dict

import requests

url_base = "api-napa"

# do we want to try paginating here or just trust that we can get the whole collection in one go?
url = f"https://{url_base}.microbiomedata.org/nmdcschema/collection_stats"
collection_stats_response = requests.get(url)
collection_stats = collection_stats_response.json()

biosample_count = 0
for current_collection in collection_stats:
    if current_collection['ns'] == 'nmdc.biosample_set':
        biosample_count = current_collection['storageStats']['count']
        print(f"{biosample_count} Biosamples in {url_base}")
        print("\n")

url = f"https://{url_base}.microbiomedata.org/nmdcschema/biosample_set"
params = {
    "max_page_size": biosample_count + 1,
    "projection": "part_of"
}

biosample_part_hood_response = requests.get(url, params=params)
biosample_part_hood_payload = biosample_part_hood_response.json()
bsph_keys = biosample_part_hood_payload.keys()

if 'next_page_token' in bsph_keys:
    exit("We didn't get all of the Biosamples and will need to paginate. Yes, I just threw away all of your data.")

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

print("ALPHABETICALLY")
pprint.pprint(study_count)
print("\n")
print("BY COUNT")
pprint.pprint(sorted_study_count)
print("\n")

print(f"{len(sorted_study_count)} studies with at least one Biosample part")

# # Extract suffix portion from each key and join them into a string
# suffix_list = ' '.join(key.split(':')[1] for key in study_count.keys())
