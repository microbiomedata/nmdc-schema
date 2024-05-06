import pprint

import click
import click_log
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from linkml_runtime.dumpers import yaml_dumper
import os

from linkml_runtime.utils.schemaview import SchemaView

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


class SchemaHandler:
    def __init__(self, schema_source):
        self.schema_source = schema_source
        self.view = self.load_schema(schema_source)

    def load_schema(self, schema_source):
        """Load schema from a URL or file."""
        return SchemaView(schema_source)

    def get_class_slots(self, class_name, include_scalars=False):
        """Retrieve all slots for a given class with an option to include scalar slots."""
        class_slot_objs = self.view.class_induced_slots(class_name)
        class_slot_obj_dict = {s.name: s for s in class_slot_objs}
        class_slot_names = [s.name for s in class_slot_objs]
        acceptable_slots = []
        for i in class_slot_names:
            slot_obj = class_slot_obj_dict[i]
            if slot_obj.multivalued or include_scalars:
                acceptable_slots.append(i)
            else:
                logger.warning(
                    f"Skipping {class_name} slot {i} because it is not multivalued and include_scalars is False.")
        acceptable_slots.sort()
        return acceptable_slots


def set_arithmetic(set1, set2, set1_name='set 1 only', set2_name='set 2 only', intersection_name='intersection'):
    """
    Perform arithmetic between two sets (or lists) and return a dictionary detailing elements unique to each set and their intersection.

    Parameters:
    set1 (set or list): First set (or list) for comparison.
    set2 (set or list): Second set (or list) for comparison.
    set1_name (str): Label for unique elements in the first set.
    set2_name (str): Label for unique elements in the second set.
    intersection_name (str): Label for the intersection elements.

    Returns:
    dict: A dictionary containing three keys (set1_name, set2_name, intersection_name) mapping to lists of elements.
    """
    # Convert input to sets if they are lists or tuples
    if isinstance(set1, (list, tuple)):
        set1 = set(set1)
    if isinstance(set2, (list, tuple)):
        set2 = set(set2)

    set1_only = set1 - set2
    set2_only = set2 - set1
    intersection = set1.intersection(set2)

    return {
        set1_name: list(set1_only),
        set2_name: list(set2_only),
        intersection_name: list(intersection),
    }


def get_collection_stats(selected_collections, db):
    selected_stats = {}
    for collection_name in selected_collections:
        try:
            for_selected_stats = {}

            collection_stats = db.command("collstats", collection_name)

            document_count = collection_stats["count"]
            if document_count != 0:
                size_in_bytes = collection_stats["size"]
                avg_bytes_per_doc = size_in_bytes / document_count

                for_selected_stats["document_count"] = document_count
                for_selected_stats["size_in_bytes"] = size_in_bytes
                for_selected_stats["storageSize"] = collection_stats["storageSize"]
                for_selected_stats["avg_bytes_per_doc"] = avg_bytes_per_doc

                selected_stats[collection_name] = for_selected_stats
            else:
                logger.info(f"No documents found in collection '{collection_name}'")
        except OperationFailure as e:
            logger.warning(f"Failed to retrieve statistics for collection '{collection_name}': {e}")

    return selected_stats


def fetch_and_log_schema_info(ctx):
    schema_handler = ctx.obj['SCHEMA_HANDLER']
    database_slots = schema_handler.get_class_slots("Database", include_scalars=True)
    sorted_slots = sorted(database_slots)
    formatted_slots = pprint.pformat(sorted_slots)
    logger.info(f"Database slots:\n{formatted_slots}")

    selected_collections = ctx.obj['SELECTED_COLLECTIONS']

    # Determine the relationship between selected_collections and database_slots
    selected_vs_schema = set_arithmetic(set1=selected_collections, set1_name="selected_collections only",
                                        set2=database_slots, set2_name="Database slots only")

    # Sort the dictionary keys
    selected_vs_schema = {key: selected_vs_schema[key] for key in sorted(selected_vs_schema)}

    logger.info("Relationship between selected collections and schema slots:")
    for key, value in selected_vs_schema.items():
        logger.info(f"{key}: {pprint.pformat(value)}")

    return (database_slots, selected_vs_schema)


# Define the main command group and include the global --schema-source option
@click.group()
@click_log.simple_verbosity_option(logger)
@click.option('--schema-source', required=True, help="The source of the schema. Can be a file path or URL.")
@click.option('--selected-collections', multiple=True, type=str,
              help='List of specific collections to fetch data from. If omitted, all collections will be processed.')
@click.option('--output-yaml', type=click.Path(), required=True,
              show_default=True, help="Output file for storing fetched data.")
@click.option('--max-docs-per-coll', default=100, show_default=True,
              help='Maximum number of documents to retrieve per collection')
@click.pass_context
def cli(ctx, schema_source, selected_collections, output_yaml, max_docs_per_coll):
    """Main command group that handles sub-commands for different access methods."""
    ctx.ensure_object(dict)

    ctx.obj['SCHEMA_HANDLER'] = SchemaHandler(schema_source)
    ctx.obj['SELECTED_COLLECTIONS'] = selected_collections
    ctx.obj['OUTPUT_YAML'] = output_yaml
    ctx.obj['MAX_DOCS_PER_COLL'] = max_docs_per_coll


# Sub-command for API access
@cli.command()
@click.option('--client-base-url', default="https://api.microbiomedata.org", show_default=True,
              help='HTTP(S) path to the FastAPI server.')
@click.option('--endpoint-prefix', default="nmdcschema", show_default=True,
              help='FastAPI path component between the URL and the endpoint name')
@click.pass_context
def api_access(ctx, client_base_url, endpoint_prefix):
    """Sub-command to exclusively use API for data fetching."""
    click.echo("Warning: This API access method is under development and not fully operational.")
    logger.warning("This API access method is under development and not fully operational.")

    (database_slots, selected_vs_schema) = fetch_and_log_schema_info(ctx)  # just printing for now

    # # Implement API data fetching logic here
    # # Example: response = requests.get(f"{client_base_url}/{endpoint_prefix}/data")
    # # Process and fetch data here
    # # Output results to a YAML file or similar
    #
    # # Example code to write data to YAML file
    # # data = response.json()
    # # with open(output_yaml, 'w') as file:
    # #     yaml.dump(data, file)


@cli.command()
@click.pass_context
@click_log.simple_verbosity_option(logger)
@click.option('--env-file', default='local/.env', show_default=True,
              help='Path to .env file containing MongoDB credentials.', type=click.Path(exists=True))
@click.option('--mongo-db-name', default="nmdc", show_default=True, help='MongoDB database name')
@click.option('--mongo-host', default="localhost", show_default=True,
              help='MongoDB host name/address.')
@click.option('--mongo-port', default=27777, type=int, show_default=True, help='MongoDB port')
# @click.option('--output-yaml', type=click.Path(), required=True,
#               show_default=True, help="Output file for storing fetched data.")
@click.option('--admin-db', default=None, help='MongoDB authentication source. Leave blank to not specify.')
@click.option('--auth-mechanism', default=None, show_default=True,
              help='Authentication mechanism for MongoDB connection. Leave blank to not specify.')
@click.option('--direct-connection/--no-direct-connection', default=True,
              help='Whether to use a direct connection to MongoDB. Defaults to direct connection.')
# @click.option('--max-docs-per-coll', default=100, show_default=True,
#               help='Maximum number of documents to retrieve per collection')
# @click.option('--selected-collections', multiple=True, type=str,
#               help='List of specific collections to fetch data from. If omitted, all collections will be processed.')
def pymongo_access(ctx, env_file, mongo_db_name, mongo_host, mongo_port,
                   admin_db, auth_mechanism, direct_connection):
    (database_slots, selected_vs_schema) = fetch_and_log_schema_info(ctx)  # just printing for now

    """Sub-command to exclusively use PyMongo for data fetching."""
    logger.info("Starting data fetch using PyMongo...")

    load_dotenv(env_file, verbose=True)
    mongo_user = os.getenv('SOURCE_MONGO_USER')
    mongo_pw = os.getenv('SOURCE_MONGO_PASS')

    # Construct MongoClient parameters dynamically
    client_params = {
        'host': mongo_host,
        'port': mongo_port,
        'directConnection': direct_connection
    }

    # Optional parameters
    if mongo_user:
        client_params['username'] = mongo_user
    if mongo_pw:
        client_params['password'] = mongo_pw
    if auth_mechanism:
        client_params['authMechanism'] = auth_mechanism
    if admin_db:
        client_params['authSource'] = admin_db

    client = MongoClient(**client_params)

    db = client[mongo_db_name]

    data = {}

    max_docs_per_coll = ctx.obj['MAX_DOCS_PER_COLL']
    selected_collections = ctx.obj['SELECTED_COLLECTIONS']

    # Get collection statistics
    collection_stats = get_collection_stats(database_slots, db)
    logger.info("Statistics for applicable collections:")
    for collection_name, stats in collection_stats.items():

        logger.info(f"{collection_name}: {stats}")
        collection = db[collection_name]
        try:
            documents = list(collection.find(limit=max_docs_per_coll))
            # Remove '_id' field from documents to avoid issues with ObjectId
            for document in documents:
                document.pop('_id', None)  # Remove '_id' if it exists in the document
            if collection_name in selected_collections:
                data[collection_name] = documents
            else:
                logger.warning(f"Collection '{collection_name}' was not requested.")
            logger.info(f"Retrieved {len(documents)} documents from collection '{collection_name}'")
        except OperationFailure as e:
            logger.error(f"Failed to fetch from collection {collection_name}: {e}")

    output_yaml = ctx.obj['OUTPUT_YAML']

    yaml_dumper.dump(data, output_yaml)
    logger.info(f"Data successfully written to {output_yaml}")


if __name__ == '__main__':
    cli(obj={})  # Ensure the context object is initialized if needed
