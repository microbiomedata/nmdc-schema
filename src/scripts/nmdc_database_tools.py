#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/src/scripts/nmdc_database_tools.py
"""
nmdc_database_tools.py:
Command-line tools for extracting data from the NMDC database via the API.
"""
import sys

import click
import logging
from pathlib import Path
import requests
from datetime import datetime
import yaml
from typing import Union
import os

from linkml_runtime.dumpers import yaml_dumper
import nmdc_schema.nmdc as nmdc

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent.parent
LOCAL_DIR = PROJECT_ROOT / "local"


# TODO: Move NmdcApi class to the nacent nmdc-common/client package
# TODO: Add unit tests for NmdcApi class
class NmdcApi:
    """
    Basic API Client for GET requests.
    """

    def __init__(self, api_base_url):
        if not api_base_url.endswith("/"):
            api_base_url += "/"
        self.base_url = api_base_url
        self.headers = {'accept': 'application/json', 'Content-Type': 'application/json'}


    def get_biosamples_part_of_study(self, study_id: str) -> list[dict]:
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

    def get_omics_processing_records_part_of_study(self, study_id: str) -> list[dict]:
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

    def get_workflow_activities_informed_by(self, workflow_activity_set: str,
                                            informed_by_id: str) -> list[dict]:
            """
            Retrieve workflow activity record(s) for the given workflow
            activity set and informed by a given OmicsProcessing ID.
            """
            params = {
                'filter': '{"was_informed_by": "'+informed_by_id+'"}',
            }
            url = self.base_url + "nmdcschema/" + workflow_activity_set
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            workflow_activity_record = response.json()["resources"]
            return workflow_activity_record

    def get_data_object(self, data_object_id: str) -> dict:
        """
        Retrieve a data object record by ID.
        """
        url = self.base_url + "nmdcschema/data_object_set/" + data_object_id
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data_object_record = response.json()
        return data_object_record

    def get_data_objects_by_description(self, description: str):
        """
        Retrieve data object records by description.
        """
        params = {
            'filter': '{"description.search": "'+description+'"}',
        }
        url = self.base_url + "data_objects"
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        data_object_records = response.json()["results"]
        return data_object_records


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
@click.option("--study-id", required=True, )
@click.option(
    "--output-file",
    help="Path to output file, relative to project root."
)
@click.option(
    "--quick-test",
    is_flag=True,
    default=False,
    help=("Quick test mode, Biosamples and OmicsProcessing records only")
)
@click.option(
    "--search-orphaned-data-objects", is_flag=True, default=False,
    help=("Search for orphaned data objects by description.")
)
@click.option(
    "--search-legacy-identifiers", is_flag=True, default=False,
    help=("Search for legacy IDs for Study and OmicsProcessing.")
    )
@click.pass_context
def extract_study(ctx, study_id: str, output_file: Union[str, bytes, os.PathLike], quick_test: bool, 
                  search_orphaned_data_objects: bool, search_legacy_identifiers: bool) -> None:
    """
    Extract a study and its associated records from the NMDC database
    via the API, and write the results to a YAML or JSON file.

    The study-id option is required. e.g., nmdc:sty-1-abcde.

    The output-file option is optional. If not provided, will use the study ID
    and schema version to name the output file and write it to the local
    directory.

    The quick-test option is optional. This will stop the search at
    OmicsProcessing records. Default is to extract all records.

    The search-orphaned-data-objects option is optional. This will search for
    data objects that are not referenced in has_output, but contain a workflow
    activity ID in their description. Default is to not search for orphaned
    data objects.

    The search-legacy-identifiers option is optional. This will search for:
     - Biosamples and OmicsProcessing records that are part_of the Study's legacy
        gold_study_identifier
     - Workflow Activities and Data Objects that was_informed_by the OmicsProcessing's legacy
        gold_sequencing_project_identifier(s)
    Default is to not search for legacy identifiers.
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
        output_file_path = (f"{LOCAL_DIR}/{study_id}.yaml")
        logfile_path = f"{LOCAL_DIR}/{study_id}.log"


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
            logger.error(f"Study {study_id} not found in the NMDC database.")
            sys.exit(1)
        else:
            raise e
    db.study_set.append(study)

    # Get the study's associated records
    # Biosamples part_of the study
    search_identifiers = []
    if search_legacy_identifiers:
        # add legacy study IDs to search
        logger.info("Searching using current and legacy identifiers")
        legacy_identifiers = (study.get("gold_study_identifiers", []))
        if legacy_identifiers:
            logger.info(f"SearchLegacyIdentifiers: also using IDs: {legacy_identifiers}")
            search_identifiers.extend(legacy_identifiers)

    search_identifiers.append(study_id)
    for study_id in search_identifiers:
        try:
            biosamples = api_client.get_biosamples_part_of_study(study_id)
            logger.info(f"Got {len(biosamples)} biosamples part_of {study_id}.")
            db.biosample_set.extend(biosamples)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.warning(f"No biosamples found part_of {study_id}.")
                continue
            else:
                raise e
        # OmicsProcessing records part_of the study
        try:
            omics_processing_records = api_client.get_omics_processing_records_part_of_study(study_id)
            logger.info(f"Got {len(omics_processing_records)} OmicsProcessing records part_of {study_id}.")
            db.omics_processing_set.extend(omics_processing_records)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.warning(f"No OmicsProcessing records found part_of {study_id}.")
                continue
            else:
                raise e

    orphaned_data_object_count = 0
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
                search_omics_ids = [omics_processing_record["id"]]
                if search_legacy_identifiers:
                    # add legacy OmicsProcessing IDs to search
                    search_omics_ids.extend(omics_processing_record.get("gold_sequencing_project_identifiers", []))
                    search_omics_ids.extend(omics_processing_record.get("alternative_identifiers", []))
                    logger.info(f"Using OmicsProcessing IDs: {search_omics_ids}")

                # Get the Workflow Execution Activity record(s) for the OmicsProcessing record
                for omics_id in search_omics_ids:
                    logger.info(f"Searching for {wf_set_name} record informed_by {omics_id}.")
                    workflow_activity_records = api_client.get_workflow_activities_informed_by(wf_set_name,
                                                                                            omics_id)
                    logger.info(f"Got {len(workflow_activity_records)} {wf_set_name} record informed_by "
                                f"{omics_id}.")
                    wf_records.extend(workflow_activity_records)
                    # Get the output data object(s) for the Workflow Execution Activity record
                    for workflow_record in workflow_activity_records:
                        logger.info(f"Searching for data objects for {workflow_record['id']} "
                                    f"{workflow_record['type']}.")
                        search_data_object_ids = workflow_record["has_output"] + workflow_record["has_input"]
                        for data_object_id in search_data_object_ids:
                            try:
                                data_object_url = f"{api_client.base_url}data_objects/{data_object_id}"
                                data_object_response = requests.get(data_object_url)
                                data_object = data_object_response.json()
                            except requests.exceptions.HTTPError as e:
                                if e.response.status_code == 404:
                                    data_object = None
                                    logger.error(f"OrphanDataObject {data_object_id} not found in the NMDC database.")
                                else:
                                    raise e
                            if data_object and data_object not in db.data_object_set:
                                logger.info(f"Adding data object {data_object_id}: {data_object.get('name')}")
                                db.data_object_set.append(data_object)

                        # Check for orphaned data objects - data objects that are not
                        # referenced in has_output / has_input, but contain a workflow activity ID
                        # in their description
                        if search_orphaned_data_objects:
                            logger.info(f"Searching for orphaned data objects for {omics_id} by description.")
                            orphan_data_objects = (
                                api_client.get_data_objects_by_description(omics_id))
                            logger.info(f"Got {len(orphan_data_objects)} orphaned data object records.")
                            for orphan_data_object in orphan_data_objects:
                                if orphan_data_object not in db.data_object_set:
                                    orphaned_data_object_count += 1
                                    logger.info(f"Found orphaned data object {orphan_data_object['id']} : "
                                                f"{orphan_data_object['description']}.")
                                    db.data_object_set.append(orphan_data_object)


            db.__setattr__(wf_set_name, wf_records)

    elapsed_time = datetime.now() - start_time
    logger.info(f"Extracted studies: {search_identifiers} from the NMDC database in {elapsed_time}.")
    logger.info(f"Found {orphaned_data_object_count} orphaned data objects.")
    # Write the results to a YAML file
    logger.info(f"Writing results to {output_file_path}.")
    yaml_data = yaml.load(yaml_dumper.dumps(db), Loader=yaml.FullLoader)
    with open(output_file_path, "w") as f:
        f.write(yaml.dump(yaml_data, indent=4))


if __name__ == "__main__":
    cli(obj={})
