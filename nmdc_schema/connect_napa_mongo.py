from datetime import datetime, timezone
import csv
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


# nersc ssh tunnel required to connect to mongo
# ssh -L 37020:mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

napa_mongo_pw = os.environ["MONGO_NAPA_PW"]
# print("napa_mongo_pw:", os.environ['MONGO_NAPA_PW'])

napa_mongo = (
    "mongodb://root:"
    + napa_mongo_pw
    + "@mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017/?authSource=admin"
)
# connection = MongoClient()
# db = connection.napa_mongo
print(napa_mongo)

# connect to mongo
client = MongoClient(napa_mongo)

# set mongo database name to nmdc'
mydb = client["nmdc"]

# list database names
for db in client.list_database_names():
    print(db)

# list collections
# for coll in mydb.list_collection_names():
#    print(coll)

study_coll = mydb["study_set"]

select_legacy_study = {"id": "gold:Gs0114663"}
napa_study_update = {"$set": {"id": "nmdc:sty-12-85j6kq06"}}


study_coll.update_one(select_legacy_study, napa_study_update)

check_study_update = {"id": "nmdc:sty-12-85j6kq06"}
mydoc = study_coll.find(check_study_update)


#########################
# generalized function to update study identifiers to napa format
# alt slots are already populated in all cases so logic for that is not needed

# mint Class Study IDs using runtime API or manually using the minter endpoint
# if reading minted IDs from a json file
study_napa_json = "XXXXXXXXXX"
with open(study_napa_json, "r") as j:
    study_napa_ids = json.loads(j.read())

# update_studies_to_napa_standards


def update_studies_to_napa_standards():
    study_reid_log = open("napa_study_update".txt, "w")
    napa_study_counter = 0
    get_legacy_studies = {"id": {"$regex": "^gold"}}
    for doc in study_coll.find(get_legacy_studies):
        select_legacy_study = {"id": doc["id"]}
        study_target_update = {"$set": {"id": napa_study_ids[napa_study_count]}}
        if napa_study_ids[napa_study_count].startswith("nmdc:sty"):
            # study_coll.update_one(select_legacy_study,study_target_update)
            study_class_legacy_napa = (
                "Study " + doc["id"] + " " + napa_study_ids[napa_study_count]
            )
            print(study_class_legacy_napa)
            study_reid_log.write(napa_study_update.txt)
            napa_study_counter = napa_study_counter + 1
        else:
            print("Did not update issue updating ", doc["id"])


#########################


biosample_coll = mydb["biosample_set"]

##needed only in testing, update values in gold alt id slots to lowercase. This has been updated in the production version of the schema already
biosample_fix_gold_case = {"gold_biosample_identifiers": {"$regex": "^GOLD*"}}
for doc in biosample_coll.find(biosample_fix_gold_case):
    if len(doc["gold_biosample_identifiers"]) == 1:
        gold_id_list = doc["gold_biosample_identifiers"]
        case_fixed = gold_id_list[0].replace("GOLD", "gold")
        gold_fix_target_biosample = {"id": doc["id"]}
        gold_case_update = {"$set": {"gold_biosample_identifiers": case_fixed}}
        # print("Set operation on ",gold_fix_target_biosample,gold_case_update)
        biosample_coll.update_one(gold_fix_target_biosample, gold_case_update)
    else:
        print("There is more than one gold biosample for", doc["id"])

# fix the fact you did updated the gold biosample ids as a string and not a list
biosample_fix_gold_type = {"gold_biosample_identifiers": {"$regex": "^gold*"}}
for doc in biosample_coll.find(biosample_fix_gold_type):
    if isinstance(doc["gold_biosample_identifiers"], str):
        #     print("need to fix", doc["gold_biosample_identifiers"])
        update_gold_biosample = []
        update_gold_biosample.append(doc["gold_biosample_identifiers"])
        fix_gold_biosample_type_target = {"id": doc["id"]}
        gold_biosample_type_update = {
            "$set": {"gold_biosample_identifiers": update_gold_biosample}
        }
        biosample_coll.update_one(
            fix_gold_biosample_type_target, gold_biosample_type_update
        )
    elif isinstance(doc["gold_biosample_identifiers"], list):
        print("already the correct type ", doc["gold_biosample_identifiers"])
    else:
        print(
            "this record is type ",
            doc["gold_biosample_identifiers"],
            type(doc["gold_biosample_identifiers"]),
        )

study_fix_gold_case = {"gold_study_identifiers": {"$regex": "^GOLD*"}}

for doc in study_coll.find(study_fix_gold_case):
    update_gold_study = []
    for gold_study in doc["gold_study_identifiers"]:
        gold_study = gold_study.replace("GOLD", "gold")
        gold_study_target = {"id": doc["id"]}
        update_gold_study.append(gold_study)
    # print(update_gold_study)
    gold_fix_target_study = {"$set": {"gold_study_identifiers": update_gold_study}}
    # print(gold_fix_target_study)
    study_coll.update_one(gold_study_target, gold_fix_target_study)

omics_coll = mydb["omics_processing_set"]
omics_processing_fix_gold_case = {
    "gold_sequencing_project_identifiers": {"$regex": "^GOLD*"}
}
for doc in omics_coll.find(omics_processing_fix_gold_case):
    update_gold_project = []
    for gold_project in doc["gold_sequencing_project_identifiers"]:
        gold_project = gold_project.replace("GOLD", "gold")
        update_gold_project.append(gold_project)
    gold_project_target = {"id": doc["id"]}
    gold_fix_target_omics = {
        "$set": {"gold_sequencing_project_identifiers": update_gold_project}
    }
    # print(gold_project_target,gold_fix_target_omics)
    omics_coll.update_one(gold_project_target, gold_fix_target_omics)

# end section only needed for testing
##################################################################################
# for x in mydoc:
#  print(x)

select_biosample_part_of = {"part_of": {"$regex": "Gs0114663$"}}
napa_biosample_part_of = {"$set": {"part_of": "nmdc:sty-12-85j6kq06"}}
part_of_biosample_update = biosample_coll.update_many(
    select_biosample_part_of, napa_biosample_part_of
)

print(part_of_biosample_update.modified_count, "documents_updated.")

# fix part_of for study Gs0114663, this needs to be an array
fix_select_biosample_part_of = {"part_of": "nmdc:sty-12-85j6kq06"}
fix_napa_biosample_part_of = {"$set": {"part_of": ["nmdc:sty-12-85j6kq06"]}}
fix_part_of_biosample_update = biosample_coll.update_many(
    fix_select_biosample_part_of, fix_napa_biosample_part_of
)
print(fix_part_of_biosample_update.modified_count, "documents_updated.")

# mint 85 biosample identifiers
# manually created this file when testing for Gs0114663

# update alt biosample ids
biosample_alt_emsl = {
    "part_of": "nmdc:sty-12-85j6kq06",
    "emsl_biosample_identifiers": {"$exists": False},
    "id": {"$regex": "^emsl*"},
}


for doc in biosample_coll.find(biosample_alt_emsl):
    #  print(doc["id"])
    target_biosample = {"id": doc["id"]}
    target_update = {"$set": {"emsl_biosample_identifiers": doc["id"]}}
    biosample_coll.update_one(target_biosample, target_update)

# fix updates to setting emsl biosample id slot as string instead of list
fix_type_emsl_alt_biosample = {
    "part_of": "nmdc:sty-12-85j6kq06",
    "emsl_biosample_identifiers": {"$exists": True},
}

for doc in biosample_coll.find(fix_type_emsl_alt_biosample):
    if isinstance(doc["emsl_biosample_identifiers"], str):
        #     print("need to fix", doc["emsl_biosample_identifiers"])
        update_emsl_biosample = []
        update_emsl_biosample.append(doc["emsl_biosample_identifiers"])
        fix_emsl_biosample_type_target = {"id": doc["id"]}
        emsl_biosample_type_update = {
            "$set": {"emsl_biosample_identifiers": update_emsl_biosample}
        }
        biosample_coll.update_one(
            fix_emsl_biosample_type_target, emsl_biosample_type_update
        )
        # print(fix_emsl_biosample_type_target,emsl_biosample_type_update)
    else:
        print(
            "this record is type ",
            doc["emsl_biosample_identifiers"],
            type(doc["emsl_biosample_identifiers"]),
        )


with open("napa_biosample_test.json", "r") as j:
    biosample_napa_ids = json.loads(j.read())


Gs0114663_legacy_biosamples = {"part_of": "nmdc:sty-12-85j6kq06"}
# f = open("Gs0114663_reid.txt", "a")

biosample_counter = 0
for doc in biosample_coll.find(Gs0114663_legacy_biosamples):
    target_biosample = {"id": doc["id"]}
    target_update = {"$set": {"id": biosample_napa_ids[biosample_counter]}}
    print("Biosample ", target_biosample, target_update)
    biosample_coll.update_one(target_biosample, target_update)
    biosample_counter = biosample_counter + 1
#  f.write("Biosample "+ doc["id"]+ " "+ biosample_napa_ids[biosample_counter])


# update omics_processing_set records for gold:Gs0114663
omics_coll = mydb["omics_processing_set"]

Gs0114663_legacy_omics = {"part_of": "gold:Gs0114663"}

# mint 479 napa omics ids manually

# read omics_ids into a python list
with open("napa_omics_test.json", "r") as j:
    omics_napa_ids = json.loads(j.read())

omics_counter = 0
f_omics_id_mapping = open("Gs0114663_omics_reid.txt", "w")
f_omics_set_operation = open("Gs0114663_omics_set", "w")

napa_study = "nmdc:sty-11-aygzgv51"
for doc in omics_coll.find(Gs0114663_legacy_omics):
    # set list with value of napa study for part_of
    study_napa_list = []
    study_napa_list.append(napa_study)
    # determine what has_input should be
    if isinstance(doc["has_input"], list):
        napa_biosample_inputs = []
        for biosample in doc["has_input"]:
            if biosample.startswith("GOLD"):
                biosample = biosample.replace("GOLD", "gold")
            target_has_input = {
                "$or": [
                    {"emsl_biosample_identifiers": biosample},
                    {"gold_biosample_identifiers": biosample},
                    {"insdc_biosample_identifiers": biosample},
                ]
            }
            get_biosample = biosample_coll.find_one(target_has_input)
            napa_biosample_inputs.append(get_biosample["id"])
    # set id and alternative ids
    target_omics = {"id": doc["id"]}
    # deal with gold omics identifiers, for all 485 legacy records all already list gold projects in the gold_sequencing_project_identifiers slot
    if doc["id"].startswith("gold"):
        update_alt = False
    # deal with emsl omics identifiers
    elif doc["id"].startswith(("emsl")):
        alt_id_slot = "alternative_identifiers"
        alt_id = []
        alt_id.append(doc["id"])
        update_alt = True
    else:
        print("Not sure how to re-id omics_processing_set id ", doc["id"])
    # set target update depending on if alt slot exists already or not
    if update_alt is True:
        target_omics_update = {
            "$set": {
                "id": omics_napa_ids[omics_counter],
                "part_of": study_napa_list,
                "has_input": napa_biosample_inputs,
                alt_id_slot: alt_id,
            }
        }
    if update_alt is False:
        target_omics_update = {
            "$set": {
                "id": omics_napa_ids[omics_counter],
                "part_of": study_napa_list,
                "has_input": napa_biosample_inputs,
            }
        }
    omics_coll.update_one(target_omics, target_omics_update)
    class_legacy_napa = (
        "OmicsProcessing " + doc["id"] + " " + omics_napa_ids[omics_counter]
    )
    # print(class_legacy_napa)
    # print(target_update)
    f_omics_id_mapping.write(class_legacy_napa + "\n")
    # f_omics_set_operation.write(target_update + '\n')
    omics_counter = omics_counter + 1

f_omics_id_mapping.close()
f_omics_set_operation.close()

# update gold project ids for omics_records
Gs0114663_mgs = open("Gs0114663_mg_omics.txt", "r")
for gold_sp_updates in Gs0114663_mgs:
    gold_sp_info = gold_sp_updates.split()
    gold_sp_list = []
    gold_sp_list.append(gold_sp_info[1])
    gold_sp_target_id = {"id": gold_sp_info[2]}
    gold_sp_target_update = {
        "$set": {"gold_sequencing_project_identifiers": gold_sp_list}
    }
    omics_coll.update_one(gold_sp_target_id, gold_sp_target_update)
# f.close()
# example regex
# myquery = { "id": {"$regex" :"^gold*"}}

# mydatabase = client.nmdc
# print(mydatabase)
# collection =nmdc["study_set"]
# study_count=nmdc.study_set.count()
# print("The study count is:", study_count)
output_file = open("new_studies_brynn.txt", "w")
for sty in studies:
    get_sty = study_coll.find_one({"id": sty})
    print(get_sty)

##get details on metap records with invalid urls
missing_urls = open("metap_missing_data_object_records.txt", "r")
Lines = missing_urls.readlines()
missing_url_list = []
for line in Lines:
    #  print(line.strip())
    select_dobj_target = {"url": line.strip()}
    print(select_dobj_target)
    dobj_doc = dobj_coll.find_one(select_dobj_target)
    print(dobj_doc)
    missing_url_list.append(dobj_doc)
json_data = dumps(missing_url_list, indent=2)

with open("missing_data_objects.json", "w") as file:
    file.write(json_data)

# update test biosample records to (Gs0114663)  use prod minted IDs, not dev
with open("biosample_prod_Gs0114663.json", "r") as j:
    biosample_prod_napa_ids = json.loads(j.read())
napa_study = "nmdc:sty-12-85j6kq06"
f_biosample_prod_id_mapping = open("Gs0114663_biosample_reid.txt", "w")
Gs0114663_legacy_emsl_biosample = {
    "part_of": "nmdc:sty-12-85j6kq06",
    "emsl_biosample_identifiers": {"$exists": True},
}
Gs0114663_legacy_gold_biosample = {
    "part_of": "nmdc:sty-12-85j6kq06",
    "emsl_biosample_identifiers": {"$exists": False},
}
biosample_prod_counter = 0
for doc in biosample_coll.find(Gs0114663_legacy_emsl_biosample):
    target_prod_update = {
        "$set": {"id": biosample_prod_napa_ids[biosample_prod_counter]}
    }
    target_prod_biosample = {"id": doc["id"]}
    biosample_coll.update_one(target_prod_biosample, target_prod_update)
    class_legacy_napa_Gs0114663 = (
        "Biosample "
        + biosample_prod_napa_ids[biosample_prod_counter]
        + " "
        + doc["emsl_biosample_identifiers"][0]
    )
    f_biosample_prod_id_mapping.write(class_legacy_napa_Gs0114663 + "\n")
    biosample_prod_counter = biosample_prod_counter + 1

for doc in biosample_coll.find(Gs0114663_legacy_gold_biosample):
    target_prod_update = {
        "$set": {"id": biosample_prod_napa_ids[biosample_prod_counter]}
    }
    target_prod_biosample = {"id": doc["id"]}
    biosample_coll.update_one(target_prod_biosample, target_prod_update)
    class_legacy_napa = (
        "Biosample "
        + biosample_prod_napa_ids[biosample_prod_counter]
        + " "
        + doc["gold_biosample_identifiers"][0]
    )
    f_biosample_prod_id_mapping.write(class_legacy_napa + "\n")
    print(class_legacy_napa)
    biosample_prod_counter = biosample_prod_counter + 1

f_biosample_prod_id_mapping.close()
# end dev to prod ids for nmdc:sty-12-85j6kq06/gold:Gs0114663

# update nmdc:sty-12-85j6kq06 to a prod id
study_coll = mydb["study_set"]
select_dev_napa_study = {"id": "nmdc:sty-12-85j6kq06"}
napa_prod_study_update = {"$set": {"id": "nmdc:sty-11-aygzgv51"}}


study_coll.update_one(select_dev_napa_study, napa_prod_study_update)


Gs0114663_dev_biosample = {"part_of": "nmdc:sty-12-85j6kq06"}
for doc in biosample_coll.find(Gs0114663_dev_biosample):
    target_prod_biosample = {"id": doc["id"]}
    fix_Gs0114663_biosample_part_of = {"$set": {"part_of": ["nmdc:sty-11-aygzgv51"]}}
    biosample_coll.update_one(target_prod_biosample, fix_Gs0114663_biosample_part_of)

# check lenght of gold project arrays
gold_project_array_lengths = []
omics_with_gold_projects = {
    "id": {"$regex": "^gold"},
    "gold_sequencing_project_identifiers": {"$exists": True},
}
for doc in omics_coll.find(omics_with_gold_projects):
    if (len(doc["gold_sequencing_project_identifiers"])) < 1:
        print(doc["id"] + " has an empty  array: part of " + doc["part_of"][0])
    elif (len(doc["gold_sequencing_project_identifiers"])) == 1:
        len_array = 1
    else:
        print("length unclear")

###############
# track down records WorkflowExecutionActivity (WEA) records that need to be deleted and their associated data objects

seq_based_collection_list = [
    "read_qc_analysis_activity_set",
    "read_based_taxonomy_analysis_activity_set",
    "metagenome_assembly_set",
    "metagenome_annotation_activity_set",
    "mags_activity_set",
    "metatranscriptome_activity_set",
]

# open file with list of omics records to delete, this list is derived from a rdf query to check for data refs
# that list was manually reviewed to determine which WEA to delete vs repair upstream records

data_object_coll = mydb["data_object_set"]

target_gp_for_del = open("omics_records_to_delete.txt", "r")
# Track deleted record identifiers as (collection, id) tuples
deleted_record_identifiers = []
for gp in target_gp_for_del:
    gold_project_id = gp.strip()
    gold_proj_curie = "gold:" + gold_project_id
    # check to make sure omics_processing_set record doesn't exist
    if omics_coll.find_one({"id": gold_proj_curie}):
        print("omics processing set record exists for " + gold_proj_curie)
    else:
        for collection in seq_based_collection_list:
            wea_coll = mydb[collection]
            doc = wea_coll.find_one({"was_informed_by": gold_proj_curie})
            if doc:
                print("found " + doc["id"] + " in collection " + collection)
                deleted_record_identifiers.append((collection, doc["id"]))
                # wea_to_delete.append(doc)
                wea_coll.delete_one({"was_informed_by": gold_proj_curie})
            # this method should not be used as there are data objects that need to be removed that are not listed in has_output for the WEA records
            # if "has_input" in doc.keys():
            #  for input in doc["has_input"]:
            #    dobj_to_delete.append(input)
            # if "has_output" in doc.keys():
            #  for output in doc["has_output"]:
            #    dobj_to_delete.append(output)
            else:
                print(
                    "Could not find WEA records informed by "
                    + gold_project_id
                    + " in collection "
                    + collection
                )
        # Fetch documents matching the regex pattern
        matching_docs = data_object_coll.find({"description": {"$regex": gold_project_id}})
        # Delete each matching document
        for doc in matching_docs:
            deleted_record_identifiers.append(("data_object_set", doc["id"]))
            data_object_coll.delete_one({"_id": doc["_id"]})

# Print the list of deleted record identifiers to a tsv file
with open("deleted_record_identifiers.tsv", "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["collection", "id"])
    for record in deleted_record_identifiers:
        writer.writerow(record)


def make_deletion_descriptors(collection_names_and_document_ids: list) -> dict:
    r"""
    Creates a deletion descriptor for each collection name-document ID pair in
    the specified list.

    A deletion descriptor is a dictionary that, when converted into JSON, can
    be used within the body of a request to the `/queries:run` endpoint of the
    Runtime API. The deletion descriptors are grouped by collection, since the
    `/queries:run` endpoint only processes documents in a single collection
    per HTTP request.
    """

    deletion_descriptors = dict()
    for collection_name_and_document_id in collection_names_and_document_ids:

        # Extract the elements of the tuple.
        (collection_name, document_id) = collection_name_and_document_id

        # Initialize this collection's list of deletion descriptors.
        if collection_name not in deletion_descriptors:
            deletion_descriptors[collection_name] = []

        # Create and append a deletion descriptor for this document.
        deletion_descriptor = dict(q=dict(id=document_id), limit=1)
        deletion_descriptors[collection_name].append(deletion_descriptor)

    return deletion_descriptors


def dump_request_body(collection_name: str, its_deletion_descriptors: list) -> str:
    r"""
    Creates a request body into which the specified deletion descriptors are
    incorporated, and writes them to a JSON file. That request body can then be
    submitted to the `/queries:run` endpoint of the Runtime API.
    """

    file_path = f"./{collection_name}.deletion_api_request_body.json"
    with open(file_path, "w") as json_file:
        api_request_body = dict(delete=collection_name, deletes=its_deletion_descriptors)
        json.dump(api_request_body, json_file)

    return file_path


# Create JSON files, each of which contains a request body for the `/queries:json` endpoint.
deletion_descriptors = make_deletion_descriptors(deleted_record_identifiers)
for collection_name in deletion_descriptors.keys():
    dump_request_body(collection_name, deletion_descriptors[collection_name])


###
# end cleanup of omics records that don't exist
