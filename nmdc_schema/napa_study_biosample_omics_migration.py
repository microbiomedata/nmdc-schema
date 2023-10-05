import json
import os
from pprint import pprint
import secrets
import time

import requests

import pymongo
from pymongo import MongoClient

#define variables for tables to update, assumes a mongo connection variable 'client'
#set database name
mydb =client['nmdc']
sty_coll=mydb["study_set"]
bsm_coll=mydb["biosample_set"]

#########################
#generalized function to update study identifiers to napa format
#alt slots are already populated in all cases so logic for that is not needed

#mint Class Study IDs using runtime API or manually using the minter endpoint
#if reading minted IDs from a json file
sty_napa_json="XXXXXXXXXX"
with open(sty_napa_json, 'r') as j:
     sty_napa_ids = json.loads(j.read())

#update_studies_to_napa_standards

def update_studies_to_napa_standards():
  study_reid_log=open("napa_sty_update.txt","w")
  napa_sty_counter=0
  get_legacy_sty={ "id" : {"$regex":"^gold" } }
  for sty_doc in sty_coll.find(get_legacy_studies):
    select_legacy_sty = {"id": sty_doc["id"]}
    sty_target_update = {"$set": { "id": napa_sty_ids[napa_sty_count] } }
    if (napa_sty_ids[napa_sty_count].startswith('nmdc:sty')):
      #sty_coll.update_one(select_legacy_sty,sty_target_update)
      sty_class_legacy_napa="Study "+ sty_doc["id"] + " " + napa_sty_ids[napa_study_count]
      print(sty_class_legacy_napa)
      sty_reid_log.write(napa_sty_update.txt)
      napa_sty_counter=napa_sty_counter+1
    else:
     print("Did not update issue updating ",sty_doc["id"])

#########################
#
#function to update biosamples

#mint Class Study IDs using runtime API or manually using the minter endpoint
#if reading minted IDs from a json file
sty_bsm_napa_json="XXXXXXXXXX"
with open(study_bsm_napa_json, 'r') as j:
     bsm_napa_ids = json.loads(j.read())

def update_bsm_by_study(napa_sty_id):
  bsm_reid_log=open(napa_sty_id"_bsm_update.txt","w")
  bsm_counter=0
  legacy_sty=napa_sty_to_legacy(napa_sty_id)
  
  legacy_bsm={"part_of": legacy_sty, "id", {"$ne":"^nmdc:bsm"}}
   for bsm_doc in bsm_coll.find(legacy_bsm):
     #set value for part_of
     sty_napa_list=[]
     sty_napa_list.append(napa_sty_id)
     target_bsm={"id": bsm_doc["id"]} 
     #alt id check function
     #TODO
       if update_alt is True:
         bsm_target_update = { "$set": { "id": bsm_napa_ids[bsm_counter], "part_of":[sty_napa_list], alt_id_slot: [alt_id] }}
       if update_alt is False:
         bsm_target_update = { "$set": { "id": bsm_napa_ids[bsm_counter], "part_of":[sty_napa_list]}}
     bsm_class_legacy_napa="Biosample " + bsm_doc["id"] + " "+ bsm_napa_ids[bsm_counter]
     print(bsm_class_legacy_napa)
     #perform biosample update
     #bsm_coll.update_one(target_bsm,bsm_target_update) 
     bsm_reid_log.write(class_legacy_napa)
     bsm_counter=bsm_counter+1
  else:
    print("study id query returned something other than 1 document",napa_sty_id) 

################

#function to get legacy study id from alt id slot
def napa_sty_to_legacy(napa_sty_id):
  legacy_sty=""
  get_sty_record={"id":napa_sty_id}
  target_sty=sty_coll.find(get_sty_record)
  if target_sty == 1:
    if (len(target_sty["gold_study_identifiers"]) ==1:
      for alt_study in target_sty["gold_study_identifiers"]:
        legacy_sty=alt_sty
    return legacy_sty 
    else:
      print("More than one GOLD study as alt id", target_sty["gold_study_identifiers"])
  
##########################
#function to update omics records
def update_omics_by_study(napa_sty_id):
  
