import json
import os
from pprint import pprint
import secrets
import time

import requests

import pymongo
from pymongo import MongoClient

#connect to napa mongo
napa_mongo_pw = os.environ['MONGO_NAPA_PW']
napa_mongo='mongodb://root:'+napa_mongo_pw+'@mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017/?authSource=admin'
client = MongoClient(napa_mongo)

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
##function to update biosamples

#mint Class Study IDs using runtime API or manually using the minter endpoint
#if reading minted IDs from a json file

def update_bsm_by_study(napa_sty_id):
  bsm_counter=0
  bsm_alt_id_dict={'gold_biosample_identifiers':'gold:','igsn_biosample_identifiers':'igsn:','emsl_biosample_identifiers':'emsl:'}
  legacy_sty=napa_sty_to_legacy(napa_sty_id) 
  bsm_reid_log=open(legacy_sty + "_bsm_reid.txt","w")
  with open(legacy_sty + "_bsm_napa.json", 'r') as j:
     bsm_napa_ids = json.loads(j.read()) 
  legacy_bsm={"part_of": legacy_sty, "id": {"$ne":"^nmdc:bsm"}}
  for bsm_doc in bsm_coll.find(legacy_bsm):
    #set value for part_of
    sty_napa_list=[]
    sty_napa_list.append(napa_sty_id)
    target_bsm={"id": bsm_doc["id"]} 
    #alt id check function
    alt_id=[]
    alt_id_slot_name=''
    for alt_id_slot in bsm_alt_id_dict:
      if bsm_doc["id"].startswith(bsm_alt_id_dict[alt_id_slot]):
        alt_id_slot_name=alt_id_slot 
        if alt_id_slot_name in bsm_doc.keys():
          if len(bsm_doc[alt_id_slot_name]) == 0:
            update_alt=True
            alt_id.append(bsm_doc["id"])
            print ("will update alt id slot is empty"+alt_id_slot_name)
          elif (len(bsm_doc[alt_id_slot_name]) == 1 and bsm_doc[alt_id_slot_name][0] == bsm_doc["id"]):
            print(alt_id_slot+" already set for "+bsm_doc["id"])
            update_alt=False
          else:
            print("length of array for "+ alt_id_slot +"exists and is greater than 1")
            update_alt=False
        else:
          update_alt=True
          alt_id.append(bsm_doc["id"])
          print ("will update alt id b/c could not fine alt id")
      break;  
    if update_alt:
      bsm_target_update = { "$set": { "id": bsm_napa_ids[bsm_counter], "part_of":sty_napa_list, alt_id_slot_name: alt_id }}
    elif not update_alt:
      bsm_target_update = { "$set": { "id": bsm_napa_ids[bsm_counter], "part_of":sty_napa_list}}
    else:
      print("not sure how to make the biosample update for" + bsm_doc["id"])
    bsm_class_legacy_napa="Biosample " + bsm_doc["id"] + " "+ bsm_napa_ids[bsm_counter]
    print(bsm_class_legacy_napa)
    print(target_bsm)
    print(bsm_target_update)
    #perform biosample update
    bsm_coll.update_one(target_bsm,bsm_target_update) 
    bsm_reid_log.write(bsm_class_legacy_napa + '\n')
    bsm_counter=bsm_counter+1
  bsm_reid_log.close()
################

#function to get legacy study id from alt id slot
def napa_sty_to_legacy(napa_sty_id):
  legacy_sty=""
  get_sty_record={"id":napa_sty_id}
  target_sty=sty_coll.find_one(get_sty_record)
  if len(target_sty["gold_study_identifiers"]) ==1:
    legacy_sty=target_sty["gold_study_identifiers"][0]
  else:
    print("More than one GOLD study as alt id", target_sty["gold_study_identifiers"])
  return legacy_sty  
##########################
#function to update omics records
def update_omics_by_study(napa_sty_id):
  omics_coll=mydb["omics_processing_set"]
  omics_counter=0
  omics_alt_id_dict={'gold_sequencing_project_identifiers':'gold:','alternative_identifiers':'emsl:'}
  legacy_sty=napa_sty_to_legacy(napa_sty_id)
  legacy_omics={"part_of": legacy_sty, "id": {"$ne":"^nmdc:omprc"}}
  f_omics_id_mapping = open(legacy_sty+"_omics_reid.txt", "w")
  with open(legacy_sty+"_omics_napa.json", 'r') as j:
     omics_napa_ids = json.loads(j.read())
  for omics_doc in omics_coll.find(legacy_omics):
    #set list with value of napa study for part_of
    study_napa_list=[]
    study_napa_list.append(napa_sty_id)
    #determine what has_input should be
    if(isinstance(omics_doc["has_input"],list)):
      napa_biosample_inputs=[]
      for biosample in omics_doc["has_input"]:
        biosample=biosample.replace('GOLD','gold')
        target_has_input={"$or":[ {"emsl_biosample_identifiers":biosample}, {"gold_biosample_identifiers":biosample},{"insdc_biosample_identifiers":biosample}]}
        get_biosample=bsm_coll.find_one(target_has_input)
        napa_biosample_inputs.append(get_biosample["id"])
    #set id and alternative ids
    target_omics={"id": omics_doc["id"]}
    #deal with gold omics identifiers, for all 485 legacy records all already list gold projects in the gold_sequencing_project_identifiers slot
    alt_omics_id=[]
    for alt_omics_id_slot in omics_alt_id_dict:
      if omics_doc["id"].startswith(omics_alt_id_dict[alt_omics_id_slot]):
        if alt_omics_id_slot in omics_doc.keys():
          if len(omics_doc[alt_omics_id_slot]) == 0:
            update_alt_omics=True
            alt_omics_id.append(omics_doc["id"])
            target_alt_omics_slot=alt_omics_id_slot
            print ("will update alt id slot is empty"+alt_id_slot_name)
          elif (len(omics_doc[alt_omics_id_slot]) == 1 and omics_doc[alt_omics_id_slot][0] == omics_doc["id"]):
            print(alt_omcs_id_slot+" already set for "+omics_doc["id"])
            update_alt_omics=False
          else:
            print("length of array for "+ alt_omics_id_slot +"exists and is greater than 1")
            update_alt_omics=False
        else:
          update_alt_omics=True
          alt_omics_id.append(omics_doc["id"])
          target_alt_omics_slot=alt_omics_id_slot
          print ("will update alt id b/c could not find alt id")
    #set target update depending on if alt slot exists already or not 
    if update_alt_omics is True:
      target_omics_update = { "$set": { "id": omics_napa_ids[omics_counter], "part_of":study_napa_list, "has_input": napa_biosample_inputs, target_alt_omics_slot: alt_omics_id }}
    if update_alt_omics is False:
      target_omics_update = { "$set": { "id": omics_napa_ids[omics_counter], "part_of":study_napa_list, "has_input": napa_biosample_inputs}}
    print(target_omics_update)
    omics_coll.update_one(target_omics,target_omics_update)
    class_legacy_napa="OmicsProcessing " + omics_doc["id"] + " "+ omics_napa_ids[omics_counter]
    #print(class_legacy_napa)
    #print(target_update)
    f_omics_id_mapping.write(class_legacy_napa + '\n')
    omics_counter=omics_counter+1
  f_omics_id_mapping.close()


