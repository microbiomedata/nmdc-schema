from nmdc_schema.nmdc import Biosample
import requests

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

cumulative_bs.append({"name": "insufficient"})

counter = 0
for bsdict in cumulative_bs:
    try:
        bsobj = Biosample(**bsdict)
        print(bsobj.name)
        counter = counter + 1
    except Exception as e:
        print(f"  {e} in Biosample {counter}")
