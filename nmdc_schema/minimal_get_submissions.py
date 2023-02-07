# SETUP

# get an ORCID if you don't have one: https://orcid.org/register
# log into https://data.microbiomedata.org or https://data.dev.microbiomedata.org with your ORCID
# get the NMDC session cookie value
#   firefox: open Firefox DevTools. On a Mac, you can use the command-option-c keystroke
#     click the storage tab at the top of the DevTools pane
#     click the "Cookies" button on the left
#     there should be an entry for https://data.microbiomedata.org or https://data.dev.microbiomedata.org, with a globe icon to the left
#     click the globe icon
#     find the session row
#     double click in the value column
#     copy the value with command-c
#     enter the session cookie value into the DATA_MICROBIOMEDATA_ORG_SESSION_COOKIE row in local/.env


import logging
import os
import pprint
import statistics
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

import click
import click_log
import requests
from dotenv import load_dotenv
from linkml_runtime import SchemaView

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@dataclass
class SubmissionsSandbox:
    api_url: Optional[str] = None
    sample_metadata_by_slotname: Optional[Dict[str, List[List[str]]]] = None
    sample_metadata_by_title: Optional[Dict[str, List[List[str]]]] = None
    session_cookie: Optional[str] = None
    study_metadata: Optional[Dict[str, Any]] = None
    submission_schema_view: Optional[SchemaView] = None
    submission_slot_title_to_x: Optional[Dict[str, Dict[str, Any]]] = None
    url_suffix = "api/metadata_submission"

    schemas_dict = {
        # "mixs": "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/model/schema/mixs.yaml",
        "nmdc": "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml",
        "submission_schema": "https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/main/artifacts/nmdc_submission_schema.yaml",
    }

    def get_one_submission_page_from_api(self, start, stop):
        logger.debug(f"session_cookie: {self.session_cookie}")
        logger.info(f"api_url: {self.api_url}")
        metadata_api_url = f"{self.api_url}{self.url_suffix}"
        logger.debug(f"whole_url: {metadata_api_url}")
        params = {"offset": start, "limit": stop}
        cookies = {"session": self.session_cookie}

        submission_response = requests.get(
            metadata_api_url, cookies=cookies, params=params
        )

        logger.debug(f"response received")

        submission_json = submission_response.json()

        # todo might want to check for response code

        logger.debug(f"conversion to JSON complete. About to get submission count.")

        submission_count = get_count_from_response(submission_json)
        logger.info(f"submission_count: {submission_count}")

        results = get_results_from_response(submission_json)
        results_pretty = pprint.pformat(results)
        logger.debug(f"results_pretty: {results_pretty}")

        (
            self.study_metadata,
            self.sample_metadata_by_title,
        ) = self.split_study_and_sample_metadata(results)

    def split_study_and_sample_metadata(self, results):
        study_metadata = {}
        sample_metadata_by_title = {}
        for result in results:
            result_id = result["id"]
            logger.debug(f"{result_id} started")
            logger.debug(f"result_id: {result_id}")
            if "metadata_submission" in result:
                metadata_submission = result["metadata_submission"]
                if "sampleData" in metadata_submission:
                    sample_data_lol = metadata_submission["sampleData"]
                    sample_data_lod = self.make_sample_data_dict(
                        sample_data_lol, result_id
                    )
                    sample_metadata_by_title[result_id] = sample_data_lod
            without_sample_data = self.del_sample_data_from_result(result)
            if without_sample_data:
                study_metadata[result_id] = without_sample_data
        return study_metadata, sample_metadata_by_title

    def make_sample_data_dict(
            self, sample_data: List[List[str]], result_id: str
    ) -> List[Dict[str, str]]:

        logger.debug(f"study_metadata: {self.study_metadata}")
        # todo may need to add or mint study id
        #   reuse the UUID that Kitware assigns to id,
        #   or some study identifier from the metadata_submission.multiOmicsForm or metadata_submission.studyForm paths?
        #   NMDC sample to study relationship expressed with sample_link?
        sample_data_row_count = len(sample_data)
        if result_id:
            if sample_data_row_count > 2:
                # todo make this test more flexible
                provided = set(sample_data[1])
                expected = set(self.submission_slot_title_to_x.keys())
                intersection = provided.intersection(expected)
                purity = len(intersection) / len(provided)
                # purity will almost always be a little lower than 1
                #   due to re-titling of slots in environmental package slot usages
                # but won't we have to resolve that eventually?
                if purity < 0.9:  # todo make this a parameter
                    logger.error(
                        f"study {result_id} doesn't seem to have the expected header rows: {sample_data[0:3]}"
                    )
                    # todo try to infer columns from template? what about versioning?
                    return [{}]
                else:
                    sample_data_headers = sample_data[1]
                    sample_data_body = sample_data[2:sample_data_row_count]
                    # todo the sample_data_headers values are term titles, not names
                    #  lookup with the latest version for now,
                    #  but work on better recording and reporting of schema version
                    body_list = []
                    for body_row in sample_data_body:
                        row_dict = dict(zip(sample_data_headers, body_row))
                        row_dict["sample_link"] = result_id
                        # todo this doesn't seem to work
                        #   would be handy for from_csv, if we want t support nmdc-schema v3 complaint samples
                        # row_dict["part_of"] = [result_id]
                        body_list.append(row_dict)

                    return body_list
            else:
                logger.error(
                    f"study {result_id} has less than three sample data rows (including the expected two headers)"
                )
                return [{}]
        else:
            logger.error(f"Empty result_id")
            return [{}]

    # @staticmethod
    def del_sample_data_from_result(self, result):
        if "metadata_submission" in result:
            metadata_submission = result["metadata_submission"]
            if "sampleData" in metadata_submission:
                for_counting = metadata_submission["sampleData"]
                del metadata_submission["sampleData"]
                if len(for_counting) > 2:
                    result["sample_data_total_rows"] = len(for_counting)
                    result["metadata_submission"] = metadata_submission
                    return result
                else:
                    result["sample_data_total_rows"] = 0
                    return result
        else:
            logger.error(f"no metadata_submission for {result['id']}")
            result["sample_data_total_rows"] = 0
            return result

    def get_submission_titles_and_names(self):
        submission_slots = self.submission_schema_view.schema.slots
        self.submission_slot_title_to_x = {
            v.title: {"title": v.title, "key": k, "alias": v.alias}
            for k, v in submission_slots.items()
            if v.title
        }
        self.submission_slot_key_to_x = {
            k: {"title": v.title, "key": k, "alias": v.alias}
            for k, v in submission_slots.items()
        }
        self.submission_slot_alias_to_x = {
            v.alias: {"title": v.title, "key": k, "alias": v.alias}
            for k, v in submission_slots.items()
            if v.alias
        }

    def view_setup(self, schemas_to_load: List[str] = None) -> None:
        logger.debug(f"will load schemas: {schemas_to_load}")
        if not schemas_to_load:
            logger.debug("will load the nmdc and submission schemas")
            schemas_to_load = ["nmdc", "submission_schema"]
        for schema_key in schemas_to_load:
            logger.info(f"loading schema {schema_key} into {schema_key}_view")
            setattr(self, f"{schema_key}_view", get_view(self.schemas_dict[schema_key]))


def get_session_cookie() -> str:
    return os.getenv("DATA_MICROBIOMEDATA_ORG_SESSION_COOKIE")


def get_count_from_response(api_response):
    logger.debug(f"looking for count in api_response")
    if "count" in api_response:
        return api_response["count"]
    else:
        logger.critical(
            f"api_response count = 0. {api_response} Do you need to refresh your session cookie in the .env file?")
        exit()


def get_results_from_response(api_response):
    return api_response["results"]


def get_view(schema_url):
    logger.info(f"creating a view of {schema_url}")
    try:
        view = SchemaView(schema_url)
        logger.info(f"confirming load of schema '{view.schema.name}'")
        return view
    except Exception as e:
        logger.critical(f"failed to load schema: {e}")
        exit()


def load_vars_from_env_file(env_file) -> None:
    load_dotenv(env_file)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--dotenv_file", type=click.Path(exists=True), default="local/.env")
@click.option("--page_start", default=0)
@click.option("--page_stop", default=999)
@click.option("--study_id", default="ad6a2a03-9229-463c-aeb6-29e1eb90b58f")
@click.option(
    "--data_portal_url",
    type=click.Choice(
        ["https://data.dev.microbiomedata.org/", "https://data.microbiomedata.org/"]
    ),
    default="https://data.microbiomedata.org/",
)
def cli(dotenv_file: str, data_portal_url: str, page_start: int, page_stop: int, study_id: str):
    load_vars_from_env_file(dotenv_file)

    submissions_sandbox = SubmissionsSandbox(api_url=data_portal_url, session_cookie=get_session_cookie())

    submissions_sandbox.view_setup()

    submissions_sandbox.get_submission_titles_and_names()

    submissions_sandbox.get_one_submission_page_from_api(start=page_start, stop=page_stop)

    pprint.pprint(submissions_sandbox.study_metadata[study_id])

    pprint.pprint(submissions_sandbox.sample_metadata_by_title[study_id])


if __name__ == "__main__":
    cli()
