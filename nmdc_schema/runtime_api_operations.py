from datetime import datetime, timezone
import json
import os
from pprint import pprint
import secrets
import time

from dotenv import load_dotenv
import requests

# modified from nmdc-runtime how-to guide https://microbiomedata.github.io/nmdc-runtime/nb/queue_and_trigger_data_jobs/

# relative path to file with format
# ```
# NMDC_RUNTIME_HOST=fixme
# NMDC_RUNTIME_USER=fixme
# NMDC_RUNTIME_PASS=fixme
# NMDC_RUNTIME_SITE_ID=fixme  # Okay if you don't have yet
# NMDC_RUNTIME_SITE_CLIENT_ID=fixme  # Okay if you don't have yet
# NMDC_RUNTIME_SITE_CLIENT_SECRET=fixme  # Okay if you don't have yet
# ```
envfile_path = "../../.env.client"

load_dotenv(envfile_path)

ENV = {k: v for k, v in os.environ.items() if k.startswith("NMDC_RUNTIME_")}

assert ENV["NMDC_RUNTIME_HOST"] == "https://api.microbiomedata.org"

HOST = ENV["NMDC_RUNTIME_HOST"]


def request_and_return_json(method, path, host=HOST, **kwargs):
    r = requests.request(method, host + path, **kwargs)
    r.raise_for_status()
    return r.json()


def get_json(path, host=HOST, **kwargs):
    return request_and_return_json("GET", path, host=host, **kwargs)


def post_and_return_json(path, host=HOST, **kwargs):
    return request_and_return_json("POST", path, host=host, **kwargs)


def patch_and_return_json(path, host=HOST, **kwargs):
    return request_and_return_json("PATCH", path, host=host, **kwargs)


def put_and_return_json(path, host=HOST, **kwargs):
    return request_and_return_json("PUT", path, host=host, **kwargs)


def auth_header(bearer_token):
    return {"Authorization": f"Bearer {bearer_token}"}


def get_token_for_user():
    response = post_and_return_json(
        "/token",
        data={
            "grant_type": "password",
            "username": ENV["NMDC_RUNTIME_USER"],
            "password": ENV["NMDC_RUNTIME_PASS"],
        },
    )
    expires_minutes = response["expires"]["minutes"]
    print(f"Bearer token expires in {expires_minutes} minutes")
    return response["access_token"]


def get_token_for_site_client():
    response = post_and_return_json(
        "/token",
        data={
            "grant_type": "client_credentials",
            "client_id": ENV["NMDC_RUNTIME_SITE_CLIENT_ID"],
            "client_secret": ENV["NMDC_RUNTIME_SITE_CLIENT_SECRET"],
        },
    )
    expires_minutes = response["expires"]["minutes"]
    print(f"Bearer token expires in {expires_minutes} minutes")
    return response["access_token"]


def mint_ids(schema_class, how_many, formatted_token):
    url = HOST + "/pids/mint"
    data = {"schema_class": {"id": schema_class}, "how_many": how_many}
    headers = formatted_token
    #  print(headers)
    response = requests.post(url, headers=headers, json=data)
    print("JSON Response ", response.json())

    minted_ids = response.json()
    return minted_ids
    # print(minted_ids)


# def mint_ids(schema_class,how_many,TOKEN_C):
#  response = post_and_return_json(
#    "/pids/mint",
#      data={
#            "schema_class": {"id": schema_class},
#            "how_many": how_many
#  }
#  headers = TOKEN_C
#  return response
#  )


def now(as_str=False):
    dt = datetime.now(timezone.utc)
    return dt.isoformat() if as_str else dt


TOKEN_C = get_token_for_site_client()


print(TOKEN_C)
formatted_token = auth_header(TOKEN_C)
napa_ids = mint_ids("nmdc:Study", 2, formatted_token)
print(napa_ids)
