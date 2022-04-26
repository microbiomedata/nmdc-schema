from linkml_runtime.dumpers import yaml_dumper

from nmdc_schema.nmdc import (
    Biosample,
    ControlledTermValue,
    QuantityValue,
    TextValue,
    GeolocationValue,
)

# this is loading the Biosample definition from PyPI?, not from the latest local files
# so bisample has a tot_nitro_content_meth but not a tot_nitro_cont_meth slot

# from python.nmdc import (
#     Biosample,
#     ControlledTermValue,
#     QuantityValue,
#     TextValue,
#     GeolocationValue,
# )


import requests

# todo should also run over omics processings and maybe some others

# from linkml_runtime.loaders import yaml_loader
# import inspect
# import pandas as pd
# import yaml

current_page = 1
cumulative_bs = []
while True:
    url = f"https://api.dev.microbiomedata.org/biosamples?per_page=200&page={current_page}"
    current_page = current_page + 1
    result = requests.get(url)
    res_dict = result.json()
    res_res = res_dict["results"]
    res_len = len(res_res)
    print(f"page {current_page}: {res_len} biosamples")
    if res_len == 0:
        break
    cumulative_bs = cumulative_bs + res_res
    print(f"cumulative biosamples: {len(cumulative_bs)}")

# cumulative_bs.append({"name": "insufficient"})

test_bs = {
    "id": "gold:Gb0239919",
    "name": "ALTERED Anthropogenic terrestrial soil microbial communities from Pennsylvania, USA - Shade23.Cen03.14102015",
    "description": "Anthropogenic terrestrial soil microbial communities from Pennsylvania, USA",
    "part_of": ["gold:Gs0154244"],
    "env_broad_scale": ControlledTermValue(
        has_raw_value="ENVO:01000219", was_generated_by=None, type=None, term=None
    ),
    "env_local_scale": ControlledTermValue(
        has_raw_value="ENVO:00002204", was_generated_by=None, type=None, term=None
    ),
    "env_medium": ControlledTermValue(
        has_raw_value="ENVO:00001998", was_generated_by=None, type=None, term=None
    ),
    "type": "nmdc:Biosample",
    "depth": QuantityValue(
        has_raw_value=None,
        was_generated_by=None,
        type=None,
        has_unit="meter",
        has_numeric_value=None,
        has_minimum_numeric_value=None,
        has_maximum_numeric_value=None,
    ),
    "geo_loc_name": TextValue(
        has_raw_value="USA: Pennsylvania,Borough of Centralia",
        was_generated_by=None,
        type=None,
        language=None,
    ),
    "lat_lon": GeolocationValue(
        has_raw_value="40.798 -76.341133",
        was_generated_by=None,
        type=None,
        latitude=40.798,
        longitude=-76.341133,
    ),
    "ecosystem": "Environmental",
    "ecosystem_category": "Terrestrial",
    "ecosystem_type": "Soil",
    "ecosystem_subtype": "Unclassified",
    "specific_ecosystem": "Unclassified",
    "add_date": "2019-09-03T00:00:00",
    "depth2": QuantityValue(
        has_raw_value=None,
        was_generated_by=None,
        type=None,
        has_unit="meter",
        has_numeric_value=None,
        has_minimum_numeric_value=None,
        has_maximum_numeric_value=None,
    ),
    "habitat": "Anthropogenic terrestrial soil",
    "location": "USA",
    "mod_date": "2022-04-08T00:00:00",
    "GOLD_sample_identifiers": ["gold:Gb0239919"],
    # "UNDEFINED": "UNDEFINED"
    # "tot_nitro_cont_meth": "careful measuring",
    "tot_nitro_content_meth": TextValue(has_raw_value="careful measuring"),
}

cumulative_bs.append(test_bs)

counter = 0
for bsdict in cumulative_bs:
    try:
        bsobj = Biosample(**bsdict)
        # # print(yaml_dumper.dumps(bsobj))
        # bsod = bsobj.__dict__
        # bsod = {k: v for k, v in bsod.items() if v}
        # print(bsod)
        # print("\n")
        print(bsobj.name)
        # print("\n")
        counter = counter + 1
    except Exception as e:
        print(f"  {e} in Biosample {counter}")
