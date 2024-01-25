#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/src/scripts/nmdc_database_tools.py
"""
nmdc_database_tools.py:
Command-line tools for extracting data from the NMDC database via the API.
"""
import click
import logging
from pathlib import Path
import requests
from datetime import datetime
import yaml

from linkml_runtime.dumpers import yaml_dumper
import nmdc_schema.nmdc as nmdc

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent.parent
LOCAL_DIR = PROJECT_ROOT / "local"

# Studies with non-compliant IDs that have been re-IDed
# Name:, study ID, legacy study ID
STUDIES = {
    "Stegen": ("nmdc:sty-11-aygzgv51", "gold:Gs0114663"),
    "SPRUCE": (None, "gold:Gs0110138"),
    "EMP": (None, "gold:Gs0154244"),
    "Luquillo": (None, "gold:Gs0128850"),
    "CrestedButte": (None, "gold:Gs0135149"),
}
# Update study IDs after re-IDing
DEFAULT_STUDY_ID = STUDIES["Stegen"][0]


class NmdcApi:
    """
    Basic API Client for GET requests.
    """

    def __init__(self, api_base_url):
        if not api_base_url.endswith("/"):
            api_base_url += "/"
        self.base_url = api_base_url
        self.headers = {'accept': 'application/json', 'Content-Type': 'application/json'}


    def get_biosamples_part_of_study(self, study_id):
        """
        Get the biosamples that are part of a study.
        """
        biosample_records = []
        params = {
            'filter': '{"part_of": "'+study_id+'"}',
            'max_page_size': '1000',
        }
        url = self.base_url + "nmdcschema/biosample_set"
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        biosample_records.extend(response.json()["resources"])
        # Get the next page of results, if any
        while response.json().get("next_page_token") is not None:
            params['page_token'] = response.json()["next_page_token"]
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            biosample_records.extend(response.json()["resources"])


        return biosample_records

    def get_omics_processing_records_part_of_study(self, study_id):
        """
        Get the OmicsProcessing records that are part of a study.
        """
        omics_processing_records = []
        params = {
            'filter': '{"part_of": "'+study_id+'"}',
            'max_page_size': '1000',
        }
        url = self.base_url + "nmdcschema/omics_processing_set"
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        omics_processing_records.extend(response.json()["resources"])
        # Get the next page of results, if any
        while response.json().get("next_page_token") is not None:
            params['page_token'] = response.json()["next_page_token"]
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            omics_processing_records.extend(response.json()["resources"])
        return omics_processing_records

    def get_workflow_activity_informed_by(self, workflow_activity_set: str,
                                            informed_by_id: str):
            """
            Retrieve a workflow activity record for the given workflow activity set
            and informed by a given OmicsProcessing ID.
            """
            params = {
                'filter': '{"was_informed_by": "'+informed_by_id+'"}',
            }
            url = self.base_url + "nmdcschema/" + workflow_activity_set
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            workflow_activity_record = response.json()["resources"]
            return workflow_activity_record


@click.group()
@click.option(
    "--api-base-url", help="API base URL to use.")
@click.pass_context
def cli(ctx, api_base_url):
    """
    NMDC database command-line tools.
    """
    ctx.ensure_object(dict)
    ctx.obj["API_CLIENT"] = NmdcApi(api_base_url=api_base_url)


@cli.command()
@click.option("--study-id", required=True,  help="Study ID to extract.")
@click.option("--output-file", help="Path to output file, relative to project "
                                   "root.")
@click.option("--quick-test", is_flag=True, default=False, help=("Quick test "
                                                                 "mode - "
                                                                 "biosamples "
                                                                 "and omics "
                                                                 "only "))
@click.option("--search-orphaned-data-objects", is_flag=True, default=False,
              help=("Search for orphaned data objects by description."))
@click.option("--search-legacy-identifiers", is_flag=True, default=False,
              help=("Search for legacy IDs for Study and OmicsProcessing."))
@click.pass_context
def extract_study(ctx, study_id, output_file, quick_test, search_orphaned_data_objects, search_legacy_identifiers):
    """
    Extract a study and its associated records from the NMDC database
    via the API, and write the results to a YAML or JSON file.

    The study-id option is required. e.g., nmdc:sty-1-abcde.

    The output-file option is optional. If not provided, will use the study ID
    and schema version to name the output file and write it to the local
    directory.

    The quick-test option is optional. Default is to extract all records.
    """
    api_client = ctx.obj["API_CLIENT"]
    start_time = datetime.now()
    # Get the schema version
    schema_version_url = f"{api_client.base_url}nmdcschema/version"
    schema_version_response = requests.get(schema_version_url)
    schema_version_response.raise_for_status()
    schema_version =  schema_version_response.text.replace('"', "")
    # Set the output and log file names
    if output_file:
        output_file_path = f"{PROJECT_ROOT}/{output_file}"
        logfile_path = f"{PROJECT_ROOT}/{output_file.replace('.yaml', '.log')}"
    else:
        normalized_study_id = study_id.replace(":", "-")
        output_file_path = (f"{LOCAL_DIR}/{normalized_study_id}.yaml")
        logfile_path = f"{LOCAL_DIR}/{normalized_study_id}.log"


    logging.basicConfig(
        filename=logfile_path,
        filemode='w',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.info(f"STUDY-ID: {study_id}")
    logger.info(f"SCHEMA-VERSION: {schema_version}")
    db = nmdc.Database()

    try:
        study_url = f"{api_client.base_url}studies/{study_id}"
        study_response = requests.get(study_url)
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
    search_ids = [study_id]
    if search_legacy_identifiers:
        # add legacy study IDs to search
        search_ids.extend(study.get("gold_study_identifiers", []))

    for study_id in search_ids:
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
            else:
                raise e



    if len(db.omics_processing_set) > 0 and not quick_test:
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
            logger.info(f"Workflow: {wf_set_name}")
            for omics_processing_record in db.omics_processing_set:
                search_ids = [omics_processing_record["id"]]
                if search_legacy_identifiers:
                    # add legacy OmicsProcessing IDs to search
                    search_ids.extend(omics_processing_record.get("gold_sequencing_project_identifiers", []))

                # Get the Workflow Execution Activity record(s) for the OmicsProcessing record
                for search_id in search_ids:
                    logger.info(f"Searching for {wf_set_name} record informed_by {search_id}.")
                    workflow_activity_record = api_client.get_workflow_activity_informed_by(wf_set_name,
                                                                                            search_id)
                    logger.info(f"Got {len(workflow_activity_record)} {wf_set_name} record informed_by "
                                f"{search_id}.")
                    wf_records.extend(workflow_activity_record)
                    # Get the output data object(s) for the Workflow Execution Activity record
                    for record in workflow_activity_record:
                        for data_object_id in record["has_output"]:
                            try:
                                data_object_url = f"{api_client.base_url}data_objects/{data_object_id}"
                                data_object_response = requests.get(data_object_url)
                                data_object = data_object_response.json()
                                logger.info(f"Got data object {data_object_id} from the NMDC database.")
                            except requests.exceptions.HTTPError as e:
                                if e.response.status_code == 404:
                                    data_object = None
                                    logger.info(f"Data object {data_object_id} not found in the NMDC database.")
                                else:
                                    raise e
                            if data_object:
                                db.data_object_set.append(data_object)

            db.__setattr__(wf_set_name, wf_records)

    elapsed_time = datetime.now() - start_time
    logger.info(f"Extracted study {study_id} from the NMDC database in {elapsed_time}.")
    # Write the results to a YAML file
    logger.info(f"Writing results to {output_file_path}.")
    yaml_data = yaml.load(yaml_dumper.dumps(db), Loader=yaml.FullLoader)
    with open(output_file_path, "w") as f:
        f.write(yaml.dump(yaml_data, indent=4))


if __name__ == "__main__":
    cli(obj={})
