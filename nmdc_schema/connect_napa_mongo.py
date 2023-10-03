from datetime import datetime, timezone
import json
import os
from pprint import pprint
import secrets
import time

from dotenv import load_dotenv
import requests

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

envfile_path = "../../.env.client"

load_dotenv(envfile_path)


#nersc ssh tunnel required to connect to mongo
#ssh -L 37020:mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

napa_mongo_pw = os.environ['MONGO_NAPA_PW']
#print("napa_mongo_pw:", os.environ['MONGO_NAPA_PW'])

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

study_coll=mydb["study_set"]

select_legacy_study = {"id":"gold:Gs0114663"}
napa_study_update = { "$set": { "id": "nmdc:sty-12-85j6kq06" } }


study_coll.update_one(select_legacy_study, napa_study_update)

check_study_update = { "id":"nmdc:sty-12-85j6kq06"}
mydoc=study_coll.find(check_study_update)

#for x in mydoc:
#  print(x)

biosample_coll=mydb["biosample_set"]
select_biosample_part_of = {"part_of": {"$regex" :"Gs0114663$"}}
napa_biosample_part_of = { "$set": { "part_of": "nmdc:sty-12-85j6kq06"}}
part_of_biosample_update=biosample_coll.update_many(select_biosample_part_of,napa_biosample_part_of)

print(part_of_biosample_update.modified_count, "documents_updated.")

#mint 85 biosample identifiers
#manually created this file when testing for Gs0114663

#update alt biosample ids
biosample_alt_emsl= {"part_of": "nmdc:sty-12-85j6kq06","emsl_biosample_identifiers":{"$exists":False},"id":{"$regex":"^emsl*"}}
  


for doc in biosample_coll.find(biosample_alt_emsl):
#  print(doc["id"])
  target_biosample={"id": doc["id"]}
  target_update = { "$set": { "emsl_biosample_identifiers": doc["id"] } }
  biosample_coll.update_one(target_biosample,target_update)


with open("napa_biosample_test.json", 'r') as j:
     biosample_napa_ids = json.loads(j.read())



Gs0114663_legacy_biosamples={"part_of": "nmdc:sty-12-85j6kq06"}
#f = open("Gs0114663_reid.txt", "a")

biosample_counter=0
for doc in biosample_coll.find(Gs0114663_legacy_biosamples):
  target_biosample={"id": doc["id"]}
  target_update = { "$set": { "id": biosample_napa_ids[biosample_counter]}}
  print("Biosample ",target_biosample,target_update)
  biosample_coll.update_one(target_biosample,target_update)
  biosample_counter=biosample_counter+1
#  f.write("Biosample "+ doc["id"]+ " "+ biosample_napa_ids[biosample_counter]) 

omics_coll=mydb["omics_processing_set"]

Gs0114663_legacy_omics={"part_of":"gold:Gs0114663"}

omics_counter=0
for doc in omics_coll.find(Gs0114663_legacy_omics):


#f.close()
#example regex
#myquery = { "id": {"$regex" :"^gold*"}}

#mydatabase = client.nmdc
#print(mydatabase)
#collection =nmdc["study_set"]
#study_count=nmdc.study_set.count()
#print("The study count is:", study_count)
