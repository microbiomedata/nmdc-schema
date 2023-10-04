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

biosample_coll=mydb["biosample_set"]

##needed only in testing, update values in gold alt id slots to lowercase. This has been updated in the production version of the schema already
biosample_fix_gold_case={"gold_biosample_identifiers":{"$regex":"^GOLD*"}}
for doc in biosample_coll.find(biosample_fix_gold_case):
   if (len(doc["gold_biosample_identifiers"]) == 1):
     gold_id_list=doc["gold_biosample_identifiers"]
     case_fixed=gold_id_list[0].replace('GOLD','gold')
     gold_fix_target_biosample={"id": doc["id"]}
     gold_case_update={ "$set": { "gold_biosample_identifiers": case_fixed}}
     #print("Set operation on ",gold_fix_target_biosample,gold_case_update)
     biosample_coll.update_one(gold_fix_target_biosample,gold_case_update)
   else:
     print("There is more than one gold biosample for",doc["id"])

#fix the fact you did updated the gold biosample ids as a string and not a list
biosample_fix_gold_type={"gold_biosample_identifiers":{"$regex":"^gold*"}}
for doc in biosample_coll.find(biosample_fix_gold_type):
  if(isinstance(doc["gold_biosample_identifiers"],str)):
#     print("need to fix", doc["gold_biosample_identifiers"])
     update_gold_biosample=[]
     update_gold_biosample.append(doc["gold_biosample_identifiers"])
     fix_gold_biosample_type_target={"id": doc["id"]}
     gold_biosample_type_update={"$set": { "gold_biosample_identifiers": update_gold_biosample}}
     biosample_coll.update_one(fix_gold_biosample_type_target,gold_biosample_type_update) 
  elif(isinstance(doc["gold_biosample_identifiers"],list)):
     print("already the correct type ",doc["gold_biosample_identifiers"])
  else:
     print("this record is type ", doc["gold_biosample_identifiers"],type(doc["gold_biosample_identifiers"]))
  
study_fix_gold_case={"gold_study_identifiers":{"$regex":"^GOLD*"}}

for doc in study_coll.find(study_fix_gold_case):
   update_gold_study=[]
   for gold_study in doc["gold_study_identifiers"]:
       gold_study=gold_study.replace('GOLD','gold')
       gold_study_target={"id": doc["id"]}
       update_gold_study.append(gold_study)
   #print(update_gold_study)    
   gold_fix_target_study={ "$set": {"gold_study_identifiers": update_gold_study}}
   #print(gold_fix_target_study) 
   study_coll.update_one(gold_study_target,gold_fix_target_study)

omics_coll=mydb["omics_processing_set"]
omics_processing_fix_gold_case={"gold_sequencing_project_identifiers":{"$regex":"^GOLD*"}}
for doc in omics_coll.find(omics_processing_fix_gold_case):
    update_gold_project=[]
    for gold_project in doc["gold_sequencing_project_identifiers"]:
        gold_project=gold_project.replace('GOLD','gold')
        update_gold_project.append(gold_project)
    gold_project_target={"id": doc["id"]}
    gold_fix_target_omics={ "$set": {"gold_sequencing_project_identifiers":update_gold_project}}
    #print(gold_project_target,gold_fix_target_omics)
    omics_coll.update_one(gold_project_target,gold_fix_target_omics)

#end section only needed for testing
##################################################################################
#for x in mydoc:
#  print(x)

select_biosample_part_of = {"part_of": {"$regex" :"Gs0114663$"}}
napa_biosample_part_of = { "$set": { "part_of": "nmdc:sty-12-85j6kq06"}}
part_of_biosample_update=biosample_coll.update_many(select_biosample_part_of,napa_biosample_part_of)

print(part_of_biosample_update.modified_count, "documents_updated.")

#fix part_of for study Gs0114663, this needs to be an array
fix_select_biosample_part_of ={"part_of":"nmdc:sty-12-85j6kq06"}
fix_napa_biosample_part_of= { "$set": { "part_of": ["nmdc:sty-12-85j6kq06"]}}
fix_part_of_biosample_update=biosample_coll.update_many(fix_select_biosample_part_of,fix_napa_biosample_part_of)
print(fix_part_of_biosample_update.modified_count, "documents_updated.")

#mint 85 biosample identifiers
#manually created this file when testing for Gs0114663

#update alt biosample ids
biosample_alt_emsl= {"part_of": "nmdc:sty-12-85j6kq06","emsl_biosample_identifiers":{"$exists":False},"id":{"$regex":"^emsl*"}}


  


for doc in biosample_coll.find(biosample_alt_emsl):
#  print(doc["id"])
  target_biosample={"id": doc["id"]}
  target_update = { "$set": { "emsl_biosample_identifiers": doc["id"] } }
  biosample_coll.update_one(target_biosample,target_update)

#fix updates to setting emsl biosample id slot as string instead of list
fix_type_emsl_alt_biosample={"part_of": "nmdc:sty-12-85j6kq06","emsl_biosample_identifiers":{"$exists":True}}

for doc in biosample_coll.find(fix_type_emsl_alt_biosample):
    if(isinstance(doc["emsl_biosample_identifiers"],str)):
#     print("need to fix", doc["emsl_biosample_identifiers"])
      update_emsl_biosample=[]
      update_emsl_biosample.append(doc["emsl_biosample_identifiers"])
      fix_emsl_biosample_type_target={"id": doc["id"]}
      emsl_biosample_type_update={"$set": { "emsl_biosample_identifiers": update_emsl_biosample}}
      biosample_coll.update_one(fix_emsl_biosample_type_target,emsl_biosample_type_update)
      #print(fix_emsl_biosample_type_target,emsl_biosample_type_update)
    else:
      print("this record is type ", doc["emsl_biosample_identifiers"],type(doc["emsl_biosample_identifiers"]))


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


#update omics_processing_set records for gold:Gs0114663
omics_coll=mydb["omics_processing_set"]

Gs0114663_legacy_omics={"part_of":"gold:Gs0114663"}

#mint 479 napa omics ids manually

#read omics_ids into a python list
with open("napa_omics_test.json", 'r') as j:
     omics_napa_ids = json.loads(j.read())

omics_counter=0
f_omics_id_mapping = open("Gs0114663_omics_reid.txt", "w")
f_omics_set_operation =open("Gs0114663_omics_set","w")

#TODO update the omics collection fixes to use arrays for part_of, has_input, alt identifiers
for doc in omics_coll.find(Gs0114663_legacy_omics):
  #determine what has_input should be
  if (len(doc["has_input"]) > 1):
    print("Too many inputs for ",doc["id"])
  elif(len(doc["has_input"]) == 1):
    for biosample in doc["has_input"]: 
      if (biosample.startswith('GOLD')):
        b_alt_id=biosample.replace('GOLD','gold')
      else:
        b_alt_id=biosample
  else:
    print("has_input not specified for ", doc["id"])
  target_has_input={"$or":[ {"emsl_biosample_identifiers":b_alt_id}, {"gold_biosample_identifiers":b_alt_id},{"insdc_biosample_identifiers":b_alt_id}]}
  get_biosample=biosample_coll.find_one(target_has_input)
  replace_has_input=get_biosample["id"]
  #set id
  target_omics={"id": doc["id"]}
  if (doc["id"].startswith('gold')):
     alt_id_slot="gold_sequencing_project_identifiers"
  elif  (doc["id"].startswith('GOLD')):
     alt_id_slot="gold_sequencing_project_identifiers"
     doc["id"].replace('gold','GOLD')   
  elif (doc["id"].startswith(('emsl', 'EMSL'))): 
     alt_id_slot="alternative_identifiers"
  else:
     print("Not sure how to re-id omics_processing_set id ",doc["id"]) 
  target_update = { "$set": { "id": omics_napa_ids[omics_counter], "part_of":"nmdc:sty-12-85j6kq06", alt_id_slot:doc["id"],"has_input": replace_has_input }}
  class_legacy_napa="OmicsProcessing " + doc["id"] + " "+ omics_napa_ids[omics_counter]
  print(class_legacy_napa)
  print(target_update)
  f_omics_id_mapping.write(class_legacy_napa)
  #f_omics_set_operation.write(target_update)  
  omics_counter=omics_counter+1

#f.close()
#example regex
#myquery = { "id": {"$regex" :"^gold*"}}

#mydatabase = client.nmdc
#print(mydatabase)
#collection =nmdc["study_set"]
#study_count=nmdc.study_set.count()
#print("The study count is:", study_count)


