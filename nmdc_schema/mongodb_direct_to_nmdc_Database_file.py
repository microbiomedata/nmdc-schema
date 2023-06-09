import os
import pprint

import yaml
import click
from pymongo import MongoClient
from dotenv import load_dotenv
import urllib.parse


def access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db):
    # Load MongoDB credentials from .env file
    load_dotenv(env_file)
    print(f"loaded {env_file}")
    mongo_pw = os.getenv('MONGO_PW')
    mongo_user = os.getenv('MONGO_USER')

    client = MongoClient(mongo_host,
                         port=mongo_port,
                         username=mongo_user,
                         password=mongo_pw,
                         authSource=admin_db,
                         authMechanism='SCRAM-SHA-256',  # todo should be an option
                         directConnection=True
                         )

    db = client[mongo_db_name]

    return db


@click.command()
@click.option('--env-file', type=click.Path(), default='local/.env', help='Path to .env file')
@click.option('--mongo-db-name', default="nmdc", help='MongoDB database name')
@click.option('--mongo-collection', prompt='Collection name', help='MongoDB collection name')
@click.option('--mongo-host', default="localhost", help='MongoDB host name/address')
@click.option('--mongo-port', default=27777, help='MongoDB port')
@click.option('--admin-db', default="admin", help='MongoDB authentication source')
@click.option('--output-dir', type=click.Path(), default='.',
              help="Output directory. Exported file's name will be based on the collection name.")
def export_to_yaml(mongo_collection, env_file, mongo_db_name, mongo_host, mongo_port, admin_db, output_dir):
    db = access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db)

    # Load MongoDB credentials from .env file

    collection = db[mongo_collection]

    if collection is None:
        print(f"Could not find collection {mongo_collection} in database {mongo_db_name}")
    # else:
    #     pprint.pprint(collection.find_one())

    # filter = {"_id": 0}

    documents = collection.find()
    doc_list = list(documents)

    prob_key = "_id"
    for doc in doc_list:
        if prob_key in doc:
            del doc[prob_key]

    wrapped = {mongo_collection: doc_list}

    # Save documents to YAML file
    with open(f"{output_dir}/{mongo_collection}.yaml", 'w') as f:  # todo should use a path operation
        yaml.dump(wrapped, f)


if __name__ == '__main__':
    export_to_yaml()
