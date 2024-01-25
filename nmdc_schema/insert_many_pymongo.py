import json
import logging

import click_log
import click  # not currently a top-level dependency of `nmdc-schema`
import pymongo  # not currently a top-level dependency of `nmdc-schema`
import requests  # not currently a top-level dependency of `nmdc-schema`


logger = logging.getLogger(__name__)
click_log.basic_config(logger)



@click.command()
@click_log.simple_verbosity_option(logger)
@click.option(
    "--input-file",
    "--in",
    type=click.File(),
    required=True,
    help=r"Path to JSON file containing input data",
    prompt=r"Path to JSON file",
)
@click.option(
    "--mongo-uri",
    type=str,
    required=True,
    envvar="TEMP_MONGO_URI",
    help=r"MongoDB connection string (can be specified via an environment variable named `TEMP_MONGO_URI`)",
    prompt=r"MongoDB connection string",
)
@click.option(
    "--is-direct-connection",
    type=bool,
    required=False,
    default=True,
    help=f"Whether to use the `directConnection` parameter for the MongoDB connection",
    prompt=f"Whether to use the `directConnection` parameter for the MongoDB connection",
)
@click.option(
    "--database-name",
    type=str,
    required=False,
    default="nmdc",
    help=f"MongoDB database name",
    prompt=f"MongoDB database name",
)
@click.option(
    "--validator-uri",
    type=str,
    required=False,
    default="https://api.microbiomedata.org/metadata/json:validate",
    help=f"URI of NMDC Schema-based validator",
    prompt=f"URI of NMDC Schema-based validator",
)
def insert_many_pymongo(
    input_file,
    mongo_uri: str,
    is_direct_connection: bool,
    database_name: str,
    validator_uri: str,
) -> None:
    r"""
    Reads data from an NMDC Schema-conformant JSON file and inserts that data into a MongoDB database.
    """
    r"""
    References:
    - Topic: Specifying a file path via a CLI option (and `click` providing a file handle to the function).
      https://click.palletsprojects.com/en/8.1.x/api/#click.File
    - Topic: `click` populating function parameters from environment variables.
      https://click.palletsprojects.com/en/8.1.x/options/#values-from-environment-variables
    - Topic: `click_log`.
      https://click-log.readthedocs.io/en/stable/
    """

    # Validate the JSON data with respect to the NMDC schema.
    #
    # Note: The validation endpoint currently returns `{"result": "All Okay!"}`
    #       when data is valid.
    #
    logger.debug(f"Validating the JSON data.")
    json_data = json.load(input_file)
    response = requests.post(validator_uri, json=json_data)
    assert response.status_code == 200, f"Failed to access validator at {validator_uri}"
    validation_result = response.json()
    if validation_result.get("result") == "All Okay!":
        logger.debug(f"The JSON data is valid.")
    else:
        logger.error(f"Validation result: {validation_result}")
        raise ValueError(f"The JSON data is not valid.")

    # Validate the MongoDB connection string and database name.
    mongo_client = pymongo.MongoClient(host=mongo_uri, directConnection=is_direct_connection)
    with pymongo.timeout(5):  # stop trying after 5 seconds
        assert (database_name in mongo_client.list_database_names()), f'The database named "{database_name}" does not exist.'

    # Insert the JSON data into the MongoDB database.
    db = mongo_client[database_name]
    logger.info(f'Processing the {len(json_data.keys())} collection(s) provided.')
    for collection_name, documents in json_data.items():
        if len(documents) > 0:
            logger.info(f'Inserting {len(documents)} documents into the "{collection_name}" collection.')
            result = db[collection_name].insert_many(documents)
            num_documents_inserted = len(result.inserted_ids)
            num_documents_provided = len(documents)
            logger.info(f"Inserted {num_documents_inserted} of {num_documents_provided} documents.")
            if num_documents_inserted < num_documents_provided:
                logger.warning(f"Not all of the provided documents were inserted.")
        else:
            logger.warning(f'Skipping collection "{collection_name}" because no documents were provided for it.')

    return None


if __name__ == "__main__":
    insert_many_pymongo()  # `click` will prompt the user for options
