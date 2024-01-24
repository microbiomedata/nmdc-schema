import os
from pprint import pprint
import secrets
import time
import pymongo
from pymongo import MongoClient

#connect to napa mongo
#set value of napa_mongo_pw manually interactively
napa_mongo = (
     "mongodb://root:"
     + napa_mongo_pw
     + "@mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017/?authSource=admin")
client = MongoClient(napa_mongo)
mydb = client["nmdc"]


#workaround example for json:submit endpoint
#modified from https://stackoverflow.com/questions/49510049/how-to-import-json-file-to-mongodb-using-python
#read in json file which has target collections and documents to insert
with open('20240118.stegen.metap.SOP01.json') as f:
  file_data = json.load(f)

#loop through target collections and insert documents for each 
for collection,documents in file_data.items():
   target_coll=mydb[collection]
   target_coll.insert_many(documents)


