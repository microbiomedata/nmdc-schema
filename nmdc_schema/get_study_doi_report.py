from pymongo import MongoClient
import click
import click_log
from dotenv import load_dotenv
import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

def access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db):
    # Load MongoDB credentials from .env file
    load_dotenv(env_file)
    logger.info(f"loaded {env_file}")
    mongo_pw = os.getenv('SOURCE_MONGO_PASS')
    mongo_user = os.getenv('SOURCE_MONGO_USER')
    logger.info(f"{mongo_user = }")

    client = MongoClient(mongo_host,
                         port=mongo_port,
                         username=mongo_user,
                         password=mongo_pw,
                         authSource=admin_db,
                         authMechanism='SCRAM-SHA-256',  # todo should be an option
                         directConnection=True
                         )

    db = client[mongo_db_name]

    study_collection = db['study_set']
    result = study_collection.aggregate([
  { "$group": { "_id": { "name": "$name", "id": "$id", "doi": "$doi.has_raw_value" } 
            } 
   }
])


    return result

@click.command()
@click_log.simple_verbosity_option(logger)
@click.option('--env-file', type=click.Path(), default='local/.env', help='Path to .env file')
@click.option('--mongo-db-name', default="nmdc", help='MongoDB database name')
@click.option('--mongo-host', default="localhost", help='MongoDB host name/address')
@click.option('--mongo-port', default=27777, help='MongoDB port')
@click.option('--admin-db', default="admin", help='MongoDB authentication source')


def get_dois(env_file, mongo_db_name, mongo_host, mongo_port, admin_db):

    doi_data = access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db)

    data_list = []
    count = 0
    for data in doi_data:
        count+=1
        study = data['_id']
        df = pd.DataFrame(study, index=[count,])
        data_list.append(df)
        
    df = pd.concat(data_list)
    df.to_csv('doi_report.tsv', sep='\t', index=False)
    
  
if __name__ == '__main__':
    get_dois()
