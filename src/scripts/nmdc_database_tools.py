#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/src/scripts/nmdc_database_tools.py
"""
nmdc_database_tools.py:
Command-line tools for extracting data from the NMDC database via the API.
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


# Name:, study ID, legacy study ID
STUDIES = {
    "Stegen": ("nmdc:sty-11-aygzgv51", "gold:Gs0114663"),
}
DEFAULT_STUDY_ID = STUDIES["Stegen"][0]



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
@click.option("--output_dir", default="../../local/", help="Output directory.")

@click.pass_context
def cli(ctx, api_base, output_dir):
    """
    NMDC database command-line tools.
    """
    ctx.ensure_object(dict)
    load_dotenv()
    ctx.obj["API_CLIENT"] = NmdcRuntimeUserApi(api_base=api_base)
    ctx.obj["OUTPUT_DIR"] = output_dir

@cli.command()
@click.option(
    "--study_id",
    default=DEFAULT_STUDY_ID,
    help=f"Optional updated study ID. Default: {DEFAULT_STUDY_ID}",
)
@click.option("--yaml_out", is_flag=True, default=False, help=("Output in YAML "
                                                         "format."))
@click.pass_context
def extract_study(ctx, study_id, yaml_out):
    """
    Extract a study and its associated records from the NMDC database
    via the API, and write the results to a JSON or YAML file.

    The study ID is optional, and defaults to the new (re-IDed) Stegen
    study ID. If you want to extract a different study, you
    can specify it here.

    The output file is named after the study ID, with a .json/.yaml
    extension. For example, the default output file name is
    nmdc:sty-11-aygzgv51.json.

    The output file is written to the current working directory.

    """
    output_dir = ctx.obj["OUTPUT_DIR"]
    logging.basicConfig(
        filename=output_dir + study_id.replace(':', '-') + ".log",
        filemode='w',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
        )

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.info(f"Extracting study {study_id} from the NMDC database.")
    api_client = ctx.obj["API_CLIENT"]
    db = nmdc.Database()

    # Get the study, if it exists
    try:
        study_response = api_client.request("GET", f"studies/{study_id}")
        study = study_response.json()
        logger.info(f"Got study {study['id']} from the NMDC database.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            study = None
            logger.info(f"Study {study_id} not found in the NMDC database.")
        else:
            raise e
    db.study_set.append(study)

    # Get the study's associated records
    # Biosamples part_of the study
    try:
        biosamples = api_client.get_biosamples_part_of_study(study_id)
        logger.info(f"Got {len(biosamples)} biosamples part_of {study_id}.")
        db.biosample_set.extend(biosamples)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.info(f"No biosamples found part_of {study_id}.")
        else:
            raise e

    # OmicsProcessing records part_of the study
    try:
        omics_processing_records = api_client.get_omics_processing_records_part_of_study(study_id)
        logger.info(f"Got {len(omics_processing_records)} OmicsProcessing records part_of {study_id}.")
        db.omics_processing_set.extend(omics_processing_records)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.info(f"No OmicsProcessing records found part_of {study_id}.")
            omics_processing_records = []
        else:
            raise e

    if len(omics_processing_records) > 0:
        # downstream workflow activity records
        (
            read_qc_records,
            read_based_analysis,
            read_based_taxonomy,
            metagenome_assembly_records,
            metagenome_annotation_records,
            mags_records,
            metatranscriptome,
            metabolomics_analysis,
            metaproteomics_analysis,
            nom_analysis,
        ) = ([], [], [], [], [], [], [], [], [], [])
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
        # Workflow Execution Activities and Data Objects for each OmicsProcessing record
        for wf_set_name, wf_records in downstream_workflow_activity_sets.items():
            logger.info(f"Getting {wf_set_name} records informed_by OmicsProcessing records.")
            for omics_processing_record in omics_processing_records:
                omics_processing_id = omics_processing_record["id"]
                # Get the Workflow Execution Activity record for the OmicsProcessing record
                workflow_activity_record = api_client.get_workflow_activity_informed_by(wf_set_name, omics_processing_id)
                logger.info(f"Got {len(workflow_activity_record)} {wf_set_name} record informed_by "
                            f"{omics_processing_id}.")
                wf_records.extend(workflow_activity_record)
                # Get the output data object(s) for the Workflow Execution Activity record
                for record in workflow_activity_record:
                    for data_object_id in record["has_output"]:
                        data_object_response = api_client.request("GET", f"data_objects/{data_object_id}")
                        data_object_response.raise_for_status()
                        data_object = data_object_response.json()
                        logger.info(f"Got data object {data_object['id']} for "
                                    f"{record['id']}.")
                        db.data_object_set.append(data_object)
            db.__setattr__(wf_set_name, wf_records)

    # Write the results to a YAML or JSON file
    if yaml_out:
        output_file_name = f"{output_dir}{study_id.replace(':', '-')}.yaml"
        yaml_data = yaml.load(yaml_dumper.dumps(db), Loader=yaml.FullLoader)
        logger.info(f"Writing results to {output_file_name}.")
        with open(output_file_name, "w") as f:
            f.write(yaml.dump(yaml_data, indent=4))
    else:
        output_file_name = f"{output_dir}{study_id.replace(':', '-')}.json"
        json_data = json.loads(json_dumper.dumps(db, inject_type=False))
        logger.info(f"Writing results to {output_file_name}.")
        with open(output_file_name, "w") as f:
            f.write(json.dumps(json_data, indent=4))

if __name__ == "__main__":
    cli(obj={})