#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/src/scripts/db_tool.py
"""
db_tool.py: Provide command-line tools for interacting with the NMDC database.
"""
import click
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import json
from linkml_runtime.dumpers import yaml_dumper, json_dumper
import logging
import nmdc_schema.nmdc as nmdc
import os
from pydantic import BaseModel
import requests
import time
import yaml


STEGEN_STUDY_ID = "nmdc:sty-11-aygzgv51"

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )
logging.basicConfig(filename=STEGEN_STUDY_ID + '.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger()

# TODO: Move API client to a common library that can be shared across projects.
def expiry_dt_from_now(days=0, hours=0, minutes=0, seconds=0):
    return datetime.now(timezone.utc) + timedelta(days=days, hours=hours,
                                          minutes=minutes,
                              seconds=seconds)

class NmdcRuntimeUserApi:
    """
    Basic Runtime API Client with user/password authentication.
    """
    def __init__(self, api_base="NAPA"):
        self.api_base = api_base
        if api_base == "NAPA":
            self.base_url = os.getenv("NAPA_BASE_URL")
            self.username = os.getenv("NAPA_USERNAME")
            self.password = os.getenv("NAPA_PASSWORD")
            self.headers = {}
            self.token_response = None
            self.refresh_token_after = None
        else:
            raise NotImplementedError(f"API base {api_base} not implemented.")

    def ensure_token(self):
        if (self.refresh_token_after is None or datetime.now(timezone.utc) >
                self.refresh_token_after):
            self.get_token()
    def get_token(self):
        token_request_body = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "scope": '',
            "client_id": "",
            "client_secret": "",
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        rv = requests.post(
            self.base_url + "token", data=token_request_body
            )
        self.token_response = rv.json()
        if "access_token" not in self.token_response:
            raise Exception(f"Getting token failed: {self.token_response}")

        self.headers[
            "Authorization"] = f'Bearer {self.token_response["access_token"]}'
        self.refresh_token_after = expiry_dt_from_now(
            **self.token_response["expires"]
        ) - timedelta(seconds=5)

    def request(self, method, url_path, params_or_json_data=None):
        self.ensure_token()
        kwargs = {"url": self.base_url + url_path, "headers": self.headers}
        if isinstance(params_or_json_data, BaseModel):
            params_or_json_data = params_or_json_data.dict(exclude_unset=True)
        if method.upper() == "GET":
            kwargs["params"] = params_or_json_data
        else:
            kwargs["json"] = params_or_json_data
        rv = requests.request(method, **kwargs)
        rv.raise_for_status()
        return rv

    def get_biosamples_part_of_study(self, study_id):
        """
        Get the biosamples that are part of a study.
        """
        url = "queries:run"
        params = {"find": "biosample_set",
                  "filter": {"part_of": {"$elemMatch": {"$eq": study_id}}}}
        response = self.request("POST", url, params)
        response.raise_for_status()
        biosample_records = response.json()["cursor"]["firstBatch"]
        return biosample_records

    def get_omics_processing_records_part_of_study(self, study_id):
        """
        Get the OmicsProcessing records that are part of a study.
        """
        url = "queries:run"
        params = {"find": "omics_processing_set",
                  "filter": {"part_of": {"$elemMatch": {"$eq": study_id}}}}
        response = self.request("POST", url, params)
        response.raise_for_status()
        omics_processing_records = response.json()["cursor"]["firstBatch"]
        return omics_processing_records

    def get_workflow_activity_informed_by(self, workflow_activity_set: str,
                                          informed_by_id: str):
        """
        Retrieve a workflow activity record for the given workflow activity set
        and informed by a given OmicsProcessing ID.
        """
        url = "queries:run"
        params = {"find": workflow_activity_set,
                  "filter": {"was_informed_by": informed_by_id}}
        response = self.request("POST", url, params_or_json_data=params)
        if response.status_code != 200:
            raise Exception(
                f"Error retrieving {workflow_activity_set} record informed by {informed_by_id}"
                )
        workflow_activity_record = response.json()["cursor"]["firstBatch"]
        return workflow_activity_record


@click.group()
@click.option("--api_base", default="NAPA", help="API base to use.")

@click.pass_context
def cli(ctx, api_base):
    """
    NMDC database command-line tools.
    """
    ctx.ensure_object(dict)
    load_dotenv()
    ctx.obj["API_CLIENT"] = NmdcRuntimeUserApi(api_base=api_base)

@cli.command()
@click.option(
    "--study_id",
    default=STEGEN_STUDY_ID,
    help=f"Optional updated study ID. Default: {STEGEN_STUDY_ID}",
)
@click.option("--yaml", is_flag=True, default=False, help=("Output in YAML "
                                                         "format."))
@click.pass_context
def extract_study(ctx, study_id, yaml):
    """
    Extract a study and its associated records from the NMDC database
    via the API, and write the results to a YAML file.

    The study ID is optional, and defaults to the value of
    STEGEN_STUDY_ID. If you want to extract a different study, you
    can specify it here.

    The output file is named after the study ID, with a .yaml
    extension. For example, the default output file name is
    nmdc:sty-11-aygzgv51.yaml.

    The output file is written to the current working directory.

    """
    logger.info(f"Extracting study {study_id} from the NMDC database.")
    api_client = ctx.obj["API_CLIENT"]
    db = nmdc.Database()

    # Get the study
    study_response = api_client.request("GET", f"studies/{study_id}")
    study_response.raise_for_status()
    study = study_response.json()
    logger.info(f"Got study {study['id']} from the NMDC database.")
    db.study_set.append(study)

    # Get the study's associated records
    # Biosamples part_of the study
    biosamples = api_client.get_biosamples_part_of_study(study_id)
    logger.info(f"Got {len(biosamples)} biosamples part_of {study_id}.")
    db.biosample_set.extend(biosamples)

    # OmicsProcessing records part_of the study
    omics_processing_records = api_client.get_omics_processing_records_part_of_study(study_id)
    logger.info(f"Got {len(omics_processing_records)} OmicsProcessing records part_of {study_id}.")
    db.omics_processing_set.extend(omics_processing_records)

    # Workflow Execution Activities and Data Objects for each OmicsProcessing record
    for omics_processing_record in omics_processing_records:
        omics_processing_id = omics_processing_record["id"]
        # Get the output data object(s) for the OmicsProcessing record
        for data_object_id in omics_processing_record["has_output"]:
            data_object_response = api_client.request("GET", f"data_objects/{data_object_id}")
            data_object_response.raise_for_status()
            data_object = data_object_response.json()
            logger.info(f"Got data object {data_object['id']} for "
                        f"{omics_processing_record['id']}.")
            db.data_object_set.append(data_object)

            # Get Workflow Execution Activities informed_by the omics_processing
            # record

        # downstream metagenomic workflow activity sets
        (
            read_qc_records,
            read_based_analysis,
            read_based_taxonomy,
            metagenome_assembly_records,
            metagenome_annotation_records,
            mags_records,
            metatranscriptome,
        ) = ([], [], [], [], [], [], [])
        # downstream metatranscriptomic and metabolomic workflow activity sets
        (
            metabolomics_analysis,
            metaproteomics_analysis,
            nom_analysis,
        ) = ([], [], [])
        downstream_workflow_activity_sets = {
            "read_qc_analysis_activity_set": read_qc_records,
            "read_based_analysis_activity_set": read_based_analysis,
            "read_based_taxonomy_analysis_activity_set": read_based_taxonomy,
            "metagenome_assembly_set": metagenome_assembly_records,
            "metagenome_annotation_activity_set": metagenome_annotation_records,
            "mags_activity_set": mags_records,
            "metatranscriptome_activity_set": metatranscriptome,
            "metabolomics_analysis_activity_set": metabolomics_analysis,
            "metaproteomics_analysis_activity_set": metaproteomics_analysis,
            "nom_analysis_activity_set": nom_analysis,
        }
        for set_name, records in downstream_workflow_activity_sets.items():
            records = api_client.get_workflow_activity_informed_by(set_name, omics_processing_id)
            db.__setattr__(set_name, records)
            logger.info(f"Got {len(records)} {set_name} records informed_by "
                        f"{omics_processing_id}.")
            # Get the has_output data object(s) for each workflow activity
            # record
            for record in records:
                for data_object_id in record["has_output"]:
                    data_object_response = api_client.request("GET", f"data_objects/{data_object_id}")
                    data_object_response.raise_for_status()
                    data_object = data_object_response.json()
                    logger.info(f"Got data object {data_object['id']} for "
                                f"{record['id']}.")
                    db.data_object_set.append(data_object)

    # Write the results to a YAML or JSON file
    if yaml:
        output_file_name = f"{study_id.replace(':', '-')}.yaml"
        yaml_data = yaml.load(yaml_dumper.dumps(db), Loader=yaml.FullLoader)
        logger.info(f"Writing results to {output_file_name}.")
        with open(output_file_name, "w") as f:
            f.write(yaml.dump(yaml_data, indent=4))
    else:
        output_file_name = f"{study_id.replace(':', '-')}.json"
        json_data = json.loads(json_dumper.dumps(db, inject_type=False))
        logger.info(f"Writing results to {output_file_name}.")
        with open(output_file_name, "w") as f:
            f.write(json.dumps(json_data, indent=4))

if __name__ == "__main__":
    cli(obj={})