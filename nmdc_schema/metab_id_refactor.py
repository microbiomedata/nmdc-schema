from dataclasses import dataclass, field, asdict
import hashlib
from pathlib import Path
import os
from pprint import pprint
from typing import List
from json import dumps

from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import oauthlib
import requests_oauthlib

from linkml_runtime.dumpers import json_dumper
import yaml
import nmdc_schema.nmdc as nmdc


envfile_path = "../../.env.client"

load_dotenv(envfile_path)
#nersc ssh tunnel required to connect to mongo
#ssh -L 37020:mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

napa_mongo_pw = os.environ.get('MONGO_NAPA_PW') or "safeguard-wipe-scanner-78"
#print("napa_mongo_pw:", os.environ['MONGO_NAPA_PW'])
print(napa_mongo_pw)
napa_mongo='mongodb://root:'+napa_mongo_pw+'@mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017/?authSource=admin'
#connection = MongoClient()
#db = connection.napa_mongo
print(napa_mongo)

#connect to mongo
client = MongoClient(napa_mongo)

#set mongo database name to nmdc'
mydb =client['nmdc']

#list database names
#for db in client.list_database_names():
#   print(db)

#list collections
#for coll in mydb.list_collection_names():
#    print(coll)

# omicsProcessing update, has_output --> raw data 
# omicsProcessing update, alternative_identifier --> nom_analysis_activity.was_informed_by

# nom_analysis_activity --> has_input (new raw file or update ID) 
# nom_analysis_activity --> has_output (data product file, update ID)
# nom_analysis_activity --> replace ids
# nom_analysis_activity --> was_informed_by -- id from alternative indetifier omics Processing
# dataObject --> replace id, and add alternative identifier, emsl:60592345
@dataclass
class NMDC_Mint:
    
    schema_class: dict = field(default_factory= lambda: {
        'schema': None,
    })
    how_many:int = 1

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)
    
@dataclass
class DataObject:
    nom_raw_data_object_type:str = "Direct Infusion FT ICR-MS Raw Data"
    nom_raw_data_object_description:str = "Raw 21T Direct Infusion Data"
    nom_dp_data_object_type:str = "FT ICR-MS Analysis Results"
    nom_dp_data_object_description:str = "EnviroMS FT ICR-MS natural organic matter workflow molecular formula assignment output details"

@dataclass
class NMDC_Types: 
    
    BioSample:str = "nmdc:Biosample"
    OmicsProcessing:str = "nmdc:OmicsProcessing"
    NomAnalysisActivity:str = "nmdc:NomAnalysisActivity"
    DataObject:str = "nmdc:DataObject"

def update_data_products(nom_activities_doc, new_raw_file_id:str, 
                         new_data_product_id:str, omics_prcessing_id:str, raw_file_path:Path=None):
   
  raw_file_id = nom_activities_doc.has_input[0]

  dataproduct_id = nom_activities_doc.has_input[0]

  data_object_set = mydb['data_object_set']

  get_raw_file_data_object = { "id" : raw_file_id }
  get_data_product_data_object = { "id" : dataproduct_id }

  raw_object_docs = [raw_objectdata_doc for raw_objectdata_doc in data_object_set.find(get_raw_file_data_object)] 

  if raw_object_docs:
     
     raw_object_update = { "$set": { "id": new_raw_file_id, 'alternative_identifier': [omics_prcessing_id]} }    
     
     data_object_set.update_one(raw_object_docs[0], raw_object_update )

  else:
     
     new_raw_data_object = get_raw_data_object(raw_file_path,
                                    was_generated_by=omics_prcessing_id, 
                                    data_object_type =DataObject.nom_raw_data_object_type,
                                    description =DataObject.nom_raw_data_object_description)

     data_object_set.insert_one(new_raw_data_object)
     
  for data_product_objectdata_doc in data_object_set.find(get_data_product_data_object):
      
      data_product_object_update = { "$set": { "id": new_data_product_id}}

      data_object_set.update_one(data_product_objectdata_doc, data_product_object_update )

def update_omics_processing(nom_new_id, new_data_product_id, new_raw_file_id, raw_file_path=None):

  omics_processing_set = mydb['omics_processing_set']

  nom_activities_set = mydb['nom_analysis_activity_set']
  
  get_old_activities={ "id" : {"$regex":"^emsl" } }
  
  for nom_activities_doc in nom_activities_set.find(get_old_activities):
    
    get_parent_omics_processing ={ "has_output" : nom_activities_doc["has_input"] }

    '''always going to be one omics processing''' 
    for omics_processing_doc in omics_processing_set.find(get_parent_omics_processing):   

        omics_processing_update = { "$set": { "has_output": [new_raw_file_id]} }    

        omics_processing_set.update_one(omics_processing_doc, omics_processing_update)

        new_omics_processing_id = omics_processing_doc['id']

        update_data_products( nom_activities_doc, new_data_product_id,  new_data_product_id,
                             new_omics_processing_id, raw_file_path)
        
        nom_activity_update = { "$set": { "id": nom_new_id , "has_output":[new_data_product_id],
                                "has_input":[new_raw_file_id], "was_informed_by": [new_omics_processing_id]} }
    
        nom_activities_set.update_one(nom_activities_doc, nom_activity_update)

def mint_nmdc_id(type:NMDC_Types, how_many:int = 1) -> List[str]: 
    
    config = yaml.safe_load(open('./config.yaml','r'))
    client = oauthlib.oauth2.BackendApplicationClient(client_id=config['client_id'])
    oauth = requests_oauthlib.OAuth2Session(client=client)
    
    token = oauth.fetch_token(token_url='https://api.microbiomedata.org/token',
                              client_id=config['client_id'], 
                              client_secret=config['client_secret'])

    nmdc_mint_url = "https://api.microbiomedata.org/pids/mint"
    
    payload = NMDC_Mint(type, how_many)
    
    #response = s.post(nmdc_mint_url, data=payload.json, )
    #list_ids = response.json()
    print(payload.json)
    response = oauth.post(nmdc_mint_url, data=payload.json)
    list_ids = response.json()
    print(list_ids)
    return list_ids
    
def get_raw_data_object(file_path:Path, was_generated_by:str,
                data_object_type:str, description:str) -> nmdc.DataObject:
    
    nmdc_id = mint_nmdc_id({'id': NMDC_Types.DataObject})[0]

    data_dict = {
                'id': nmdc_id,
                "name": file_path.name,
                "file_size_bytes": file_path.stat().st_size,
                "md5_checksum": hashlib.md5(file_path.open('rb').read()).hexdigest(),
                "was_generated_by": was_generated_by, #omics processing id
                "data_object_type": data_object_type,
                "description": description,
                "type": "nmdc:DataObject"
                } 
    
    data_object = nmdc.DataObject(**data_dict)

    return data_object