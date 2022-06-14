# from linkml_runtime.dumpers import yaml_dumper
# import inspect
# import pandas as pd
# import yaml

# QuantityValue, GeolocationValue
from python.nmdc import (
    Biosample,
    ControlledTermValue,
    TextValue
)

import requests

# todo make me a test

test_bs = {
    "id": "gold:Gb0239919",
    "name": "ALTERED Anthropogenic terrestrial soil microbial communities from Pennsylvania, USA - Shade23.Cen03.14102015",
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
    # "UNDEFINED": "UNDEFINED"
    "tot_nitro_cont_meth": TextValue(has_raw_value="careful measuring"),
    # "tot_nitro_content_meth": TextValue(has_raw_value="careful measuring"),
}

# todo should also run over omics processings and maybe some others


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
