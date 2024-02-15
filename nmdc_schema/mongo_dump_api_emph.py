import logging
import os
import pprint

import click
import click_log
import requests
from dotenv import load_dotenv
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from pymongo import MongoClient
from pymongo.errors import OperationFailure

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


# todo: add a collection report only mode
# todo balance extensiveness of reporting with speed of execution, even in a degraded state?


# Get NERSC sshproxy app. See https://docs.nersc.gov/connect/mfa/#sshproxy.
#   Documentation may not be completely up-to-date.
# scp <NERSC_USER_NAME>@dtn01.nersc.gov:/global/cfs/cdirs/mfa/NERSC-MFA/sshproxy.sh .
#   Requires that you have a NERSC account. See ???
#   May require entering your NERSC password and MFA token
# <PATH_TO>/sshproxy.sh -u <NERSC_USER_NAME>
#   Make a note of the location where your key has been saved. Default = ~/.ssh/nersc
# ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 <NERSC_USER_NAME>@dtn01.nersc.gov
#  You can use a local port other than 27777 if you want. Just be consistent in the rest of this setup.


def set_arithmetic(set1, set2, set1_name='set 1 only', set2_name='set 2 only'):
    set1_only = set1 - set2
    set2_only = set2 - set1
    intersection = set1.intersection(set2)
    temp = {
        f"{set1_name} only": list(set1_only),
        f"{set2_name} only": list(set2_only),
        'intersection': list(intersection),  # todo should the name of the intersection be a parameter?
    }
    return temp


class FastAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_collection_stats_from_fastapi(self):
        pass

    def get_docs_from_fastapi(self, method, endpoint, params=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.warning(f"{e}")

    def get_paginated_data(self, endpoint, params, max_docs=None, results_key='resources',
                           continuation_key='next_page_token', continuation_parameter='page_token'):
        params = params or {}
        data = []

        while True:
            response = self.get_docs_from_fastapi('GET', endpoint, params=params)
            if response and results_key in response:
                temp = response[results_key]
                data.extend(temp)
                data_len = len(data)
                logger.info(f"Retrieved {data_len} entries out of {max_docs} from {endpoint}")
                if data_len >= max_docs:
                    break

                if continuation_key in response:
                    params[continuation_parameter] = response[continuation_key]
                else:
                    break
            else:
                # logger.warning(f"FastAPI request to {endpoint} failed. Might work as a pymongo query.")
                break

        return data


class PyMongoClient:

    def __init__(self, env_file, mongo_db_name, mongo_host, mongo_port, admin_db, auth_mechanism='SCRAM-SHA-256',
                 direct_connection=True):
        self.admin_db = admin_db
        self.auth_mechanism = auth_mechanism
        self.direct_connection = direct_connection
        self.env_file = env_file
        self.mongo_db_name = mongo_db_name
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.selected_collections = []

        logger.debug("Attempting to create a MongoDB database object")
        self.db = self.create_database_obj()
        logger.debug(pprint.pformat(self.__dict__))
        logger.info("MongoDB database object created. Now attempting to get collection names.")
        self.collections = self.get_collection_names_from_pymongo()
        logger.info(f"Found {len(self.collections)} collections in MongoDB database {self.mongo_db_name}")

    def create_database_obj(self):
        # Load MongoDB credentials from .env file
        load_dotenv(self.env_file)
        logger.info(f"loaded {self.env_file}")
        mongo_pw = os.getenv('SOURCE_MONGO_PASS')
        mongo_user = os.getenv('SOURCE_MONGO_USER')
        logger.info(f"{mongo_user = }")

        client = MongoClient(host=self.mongo_host,
                             port=self.mongo_port,
                             username=mongo_user,
                             password=mongo_pw,
                             authSource=self.admin_db,
                             authMechanism=self.auth_mechanism,
                             directConnection=self.direct_connection
                             )

        db = client[self.mongo_db_name]

        return db

    def get_collection_names_from_pymongo(self):

        collections = self.db.list_collections()

        filtered_collections = []

        for collection_info in collections:
            if collection_info["type"] == "view":
                logger.warning(f"Collection '{collection_info['name']}' is a view.")
            else:
                logger.debug(f"Collection '{collection_info['name']}' is a collection.")
                collection_name = collection_info['name']
                logger.debug(f"Checking permissions for collection '{collection_name}'...")
                collection = self.db[collection_name]
                try:
                    document = collection.find_one()  # max_time_ms=1000 ?
                    if document is not None:
                        logger.debug(f"You have read permission for collection '{collection_name}'.")
                        filtered_collections.append(collection_name)
                except OperationFailure as e:
                    if "not authorized" in str(e):
                        logger.warning(f"You do not have read permission for collection '{collection_name}'.")

        return filtered_collections

    def get_collection_stats(self):
        selected_stats = {}
        for collection_name in self.selected_collections:
            for_selected_stats = {}

            collection_stats = self.db.command("collstats", collection_name)

            for_selected_stats["document_count"] = collection_stats["count"]
            for_selected_stats["size_in_bytes"] = collection_stats["size"]
            for_selected_stats["storageSize"] = collection_stats["storageSize"]
            for_selected_stats["avg_bytes_per_doc"] = collection_stats["size"] / collection_stats["count"]

            selected_stats[collection_name] = for_selected_stats

        return selected_stats

    def get_docs_from_pymongo(self, collection_name, max_docs_per_coll):
        collection = self.db[collection_name]

        if collection is None:
            logger.info(f"Could not find collection {collection_name}")

        documents = collection.find().limit(max_docs_per_coll)
        doc_list = list(documents)

        prob_key = "_id"
        for doc in doc_list:
            if prob_key in doc:
                del doc[prob_key]

        return doc_list


class ViewHelper:
    def __init__(self, schema_path):
        self.view = SchemaView(schema_path)

    def get_class_slots(self, class_name, include_scalars=False):
        class_slot_objs = self.view.class_induced_slots(class_name)
        class_slot_obj_dict = {s.name: s for s in class_slot_objs}
        class_slot_names = [s.name for s in class_slot_objs]
        acceptable_slots = []
        for i in class_slot_names:
            slot_obj = class_slot_obj_dict[i]
            # logger.info(f"{i = } {slot_obj.multivalued = }")
            if slot_obj.multivalued or include_scalars:
                # logger.info(f"Adding {i} to ")
                acceptable_slots.append(i)
            else:
                logger.warning(
                    f"Skipping {class_name} slot {i} because it is not multivalued and include_scalars is False.")
        class_slot_names.sort()
        return acceptable_slots


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option('--admin-db', default="admin", show_default=True, help='MongoDB authentication source')
@click.option('--env-file', type=click.Path(exists=True), default='local/.env',
              show_default=True, help='Path to .env file')
@click.option('--max-docs-per-coll', default=100,
              show_default=True, help='Maximum number of documents to retrieve per collection')  # was 100_000
@click.option('--mongo-db-name', default="nmdc", show_default=True, help='MongoDB database name')
@click.option('--mongo-host', default="localhost", show_default=True,
              help='MongoDB host name/address. Use "localhost" if using an ssh tunnel to ' +
                   'mongo-loadbalancer.nmdc.production.svc.spin.nersc.org ' +
                   'or mongo-loadbalancer.nmdc-dev.production.svc.spin.nersc.org')
@click.option('--mongo-port', default=27777, show_default=True, help='MongoDB port')
@click.option('--output-yaml', required=True, type=click.Path(),
              show_default=True, help="Output file.")
@click.option('--root-class', default="Database",
              show_default=True, help='Schema class that corresponds to a Mongo Database')
@click.option('--schema-file', type=click.Path(exists=True), default='src/schema/nmdc.yaml',
              show_default=True,
              help='Path to root YAML file in the nmdc-schema. ' +
                   'For determining structure only. No validation in this step.')
@click.option('--selected-collections', multiple=True, show_default=True, help='MongoDB collection name')
@click.option('--page-size', default=10,
              show_default=True,
              help='Number of documents retrieved per FastAPI GET request')  # how many is too many? for what reason? seems like there's some overhead
@click.option('--client-base-url', default="https://api.microbiomedata.org",
              show_default=True,
              help='HTTP(S) path to the FastAPI server. ' +
                   'https://api-dev.microbiomedata.org/docs or https://api.microbiomedata.org/docs')
@click.option('--endpoint-prefix', default="nmdcschema",
              show_default=True, help='FastAPI path component between the URL and the endpoint name')
@click.option('--collection-check/--skip-collection-check', default=True)
def cli(
        admin_db,
        env_file,
        mongo_db_name,
        mongo_host,
        mongo_port,
        root_class,
        schema_file,
        selected_collections,
        client_base_url,
        endpoint_prefix,
        max_docs_per_coll,
        page_size,
        output_yaml,
        collection_check,

):
    # selected_collections = []
    est_doc_count = 0
    if collection_check:
        nmdc_pymongo_client = PyMongoClient(
            admin_db=admin_db,
            auth_mechanism='SCRAM-SHA-256',
            direct_connection=True,
            env_file=env_file,
            mongo_db_name=mongo_db_name,
            mongo_host=mongo_host,
            mongo_port=mongo_port,
        )
        # logger.info(f"{nmdc_pymongo_client.collections = }")

        nmdc_helper = ViewHelper(schema_file)

        # logger.info(f"{nmdc_helper.view.schema.name = }")

        root_class_slots = nmdc_helper.get_class_slots(root_class)

        # logger.info(f"{root_class_slots = }")

        schema_vs_mongo_collections = set_arithmetic(set(root_class_slots), set(nmdc_pymongo_client.collections),
                                                     set1_name='schema',
                                                     set2_name='mongo')

        logger.info(f"schema_vs_mongo_collections = ")
        logger.info(pprint.pformat(schema_vs_mongo_collections))

        available_selected_collections = []
        if len(selected_collections) > 0:
            available_vs_selected_collections = set_arithmetic(set(schema_vs_mongo_collections['intersection']),
                                                               set(selected_collections), set1_name='available',
                                                               set2_name='selected')
            logger.debug(f"available_vs_selected_collections = ")
            logger.debug(pprint.pformat(available_vs_selected_collections))
            available_selected_collections = available_vs_selected_collections['intersection']
            if available_vs_selected_collections['selected only']:
                logger.warning(
                    f"Some requested collections are not available: {available_vs_selected_collections['selected only']}")
        else:
            available_selected_collections = schema_vs_mongo_collections['intersection']
        available_selected_collections.sort()
        logger.info(f"available_selected_collections = ")
        logger.info(pprint.pformat(available_selected_collections))

        selected_collections = available_selected_collections
    else:
        selected_collections = selected_collections
        logger.info(f"{selected_collections = }")

    # collection_stats = nmdc_pymongo_client.get_collection_stats()

    nmdc_fastapi_client = FastAPIClient(client_base_url)

    if max_docs_per_coll < page_size:
        page_size = max_docs_per_coll

    nmdc_database_object = {}
    for current_collection in selected_collections:

        if collection_check:
            logger.info(f"Attempting to get collection stats from {current_collection}")

            current_coll_obj = nmdc_pymongo_client.db[current_collection]
            est_doc_count = current_coll_obj.estimated_document_count()

            logger.info(
                f"estimated_document_count = {est_doc_count}")  # it would also be nice to report collection size or avg size/doc but I haven't figured how to do that quickly yet

        #     # collection_stats = current_coll_obj.estimated_document_count()
        #     collection_stats = current_coll_obj.stats()
        #
        #     # collection = db[collection_name]
        #     #
        #     # # Get statistics for the collection
        #     # collection_stats = collection.stats()

        endpoint_name = f"{endpoint_prefix}/{current_collection}"
        params_string = {
            "max_page_size": page_size
        }
        max_docs = max_docs_per_coll

        if max_docs_per_coll > est_doc_count:
            max_docs = est_doc_count

        logger.info(
            f"Attempting to get {max_docs} documents from {endpoint_name} in pages of {page_size}.")

        paginated_data = nmdc_fastapi_client.get_paginated_data(endpoint=endpoint_name, params=params_string,
                                                                max_docs=max_docs)

        if paginated_data:
            nmdc_database_object[current_collection] = paginated_data
        else:  # todo needs safer programming like try/except
            logger.warning(f"FastAPI request to {endpoint_name} appears to have failed. Trying as a PyMongo query.")
            try:
                direct_data_all = nmdc_pymongo_client.get_docs_from_pymongo(current_collection, max_docs)
                if direct_data_all:
                    logger.info(
                        f"Successfully retrieved {len(direct_data_all)} documents from {current_collection} via PyMongo")
                    nmdc_database_object[current_collection] = direct_data_all
            except Exception as e:
                logger.warning(
                    f"PyMongo request to {endpoint_name} appears to have failed, probably because you specified {collection_check = }. Error = {e}.")

    logger.info(f"Writing {output_yaml}")
    yaml_dumper.dump(nmdc_database_object, output_yaml)


if __name__ == '__main__':
    cli()
