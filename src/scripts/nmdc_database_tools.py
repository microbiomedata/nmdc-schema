#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/src/scripts/nmdc_database_tools.py
"""
nmdc_database_tools.py:
Command-line tools for extracting data from the NMDC database via the API.
"""
import click
import json
from linkml_runtime.dumpers import yaml_dumper, json_dumper
import logging
import nmdc_schema.nmdc as nmdc

from pathlib import Path
import requests
import yaml


SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent.parent

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


def _write_db_to_file(db, output_file_name, yaml_out):
    # Write the results to a YAML or JSON file
    if yaml_out:
        yaml_data = yaml.load(yaml_dumper.dumps(db), Loader=yaml.FullLoader)
        with open(output_file_name, "w") as f:
            f.write(yaml.dump(yaml_data, indent=4))
    else:
        json_data = json.loads(json_dumper.dumps(db, inject_type=False))
        with open(output_file_name, "w") as f:
            f.write(json.dumps(json_data, indent=4))

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
@click.option("--study-id",  help="Study ID to extract.")

@click.option("--output-dir", help="Output directory, relative to project "
                                   "root.")
@click.option("--json-out", is_flag=True, default=False, help=("Output in JSON "
                                                               "format."))
@click.pass_context
def extract_study(ctx, study_id, output_dir, json_out):
    """
    Extract a study and its associated records from the NMDC database
    via the API, and write the results to a YAML or JSON file.

    The study-id option is optional.  If not provided, will try to infer the
    study ID from the output-dir option, provided that the output directory
    uses the modified study ID format (nmdc-sty-<number>-<string>). e.g.,
    nmdc-sty-1-1.

    The output-dir option is optional. If not provided, will use
    local/nmdc-sty-<number>-<string> as the output directory, provided that
    the study ID follows NMDC format (nmdc:sty-<number>-<string>). e.g.,
    nmdc:sty-1-1.

    If both study-id and output-dir are provided, the output-dir option will
    be relative to the project root.

    if neither study-id nor output-dir are provided, will raise an error.

    The json option is optional. Default is to output in YAML format.
    """
    # Check that we have a study ID OR an output directory
    if study_id is None and output_dir is None:
        raise click.UsageError("Must provide either a study ID or an output "
                               "directory.")
    # If no study ID provided, try to infer it from the output directory
    if study_id is None:
        study_id = output_dir.split("/")[-1].replace("-", ":", 1)
        output_dir = PROJECT_ROOT / output_dir
    # If no output directory provided, make one based on the study ID
    elif output_dir is None:
        output_dir = PROJECT_ROOT / "local" / study_id.replace(':', '-')
    # both study ID and output directory provided, make output directory relative to project root
    else:
        output_dir = PROJECT_ROOT / output_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    if json_out:
        output_file_name = f"{output_dir}/{study_id.replace(':', '-')}.json"
    else:
        output_file_name = f"{output_dir}/{study_id.replace(':', '-')}.yaml"

    logfile_name = f"{output_dir}/{study_id.replace(':', '-')}.log"



    logging.basicConfig(
        filename=logfile_name,
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

    # if len(omics_processing_records) > 0:
    #     # downstream workflow activity records
    #     (
    #         read_qc_records,
    #         read_based_analysis,
    #         read_based_taxonomy,
    #         metagenome_assembly_records,
    #         metagenome_annotation_records,
    #         mags_records,
    #         metatranscriptome,
    #         metabolomics_analysis,
    #         metaproteomics_analysis,
    #         nom_analysis,
    #     ) = ([], [], [], [], [], [], [], [], [], [])
    #     downstream_workflow_activity_sets = {
    #         "read_qc_analysis_activity_set": read_qc_records,
    #         "read_based_taxonomy_analysis_activity_set": read_based_taxonomy,
    #         "metagenome_assembly_set": metagenome_assembly_records,
    #         "metagenome_annotation_activity_set": metagenome_annotation_records,
    #         "mags_activity_set": mags_records,
    #         "metatranscriptome_activity_set": metatranscriptome,
    #         "metabolomics_analysis_activity_set": metabolomics_analysis,
    #         "metaproteomics_analysis_activity_set": metaproteomics_analysis,
    #         "nom_analysis_activity_set": nom_analysis,
    #     }
    #     # Workflow Execution Activities and Data Objects for each OmicsProcessing record
    #     for wf_set_name, wf_records in downstream_workflow_activity_sets.items():
    #         logger.info(f"Getting {wf_set_name} records informed_by OmicsProcessing records.")
    #         for omics_processing_record in omics_processing_records:
    #             omics_processing_id = omics_processing_record["id"]
    #             # Get the Workflow Execution Activity record for the OmicsProcessing record
    #             workflow_activity_record = api_client.get_workflow_activity_informed_by(wf_set_name,
    #                                                                                     omics_processing_id)
    #             logger.info(f"Got {len(workflow_activity_record)} {wf_set_name} record informed_by "
    #                         f"{omics_processing_id}.")
    #             wf_records.extend(workflow_activity_record)
    #             # Get the output data object(s) for the Workflow Execution Activity record
    #             for record in workflow_activity_record:
    #                 for data_object_id in record["has_output"]:
    #                     data_object_response = requests.get(f"{api_client.base_url}data_objects/{data_object_id}")
    #                     data_object_response.raise_for_status()
    #                     data_object = data_object_response.json()
    #                     logger.info(f"Got data object {data_object['id']} for "
    #                                 f"{record['id']}.")
    #                     db.data_object_set.append(data_object)
    #         db.__setattr__(wf_set_name, wf_records)

    # Write the results to a YAML or JSON file
    logger.info(f"Writing results to {output_file_name}.")
    _write_db_to_file(db, output_file_name, json_out)


if __name__ == "__main__":
    cli(obj={})
