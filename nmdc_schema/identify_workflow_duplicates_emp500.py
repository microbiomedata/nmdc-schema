import json
import pymongo
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import urllib

# this is generating a .json data file that can be used to delete these records by submitting it to the appropriate endpoint (ie queries:run)
# for EMP500 (nmdc:sty-11-547rwq94) which have different base IDs with a .1 version.

envfile_path = "../../.env.client"

load_dotenv(envfile_path)
username = os.environ["MONGO_USER"]
pw = os.environ["MONGO_PW"]
host = os.environ["HOST"]
port = os.environ["PORT"]

prod_mongo = (
    "mongodb://"
    + username
    + ":"
    + urllib.parse.quote(pw)
    + "@"
    + host
    + ":"
    + port
    + "/?authMechanism=SCRAM-SHA-256&authSource=admin&directConnection=true"
)

client = MongoClient(prod_mongo)
mydb = client["nmdc"]


study_id = "nmdc:sty-11-547rwq94"

# collection_names
asm_coll_name = "metagenome_assembly_set"
qc_coll_name = "read_qc_analysis_activity_set"
rbt_coll_name = "read_based_taxonomy_analysis_activity_set"
do_coll_name = "data_object_set"
# collection connections
asm_coll = mydb[asm_coll_name]
qc_coll = mydb[qc_coll_name]
rbt_coll = mydb[rbt_coll_name]
do_coll = mydb[do_coll_name]

# aggregation pipeline varaibles
pipeline = [
    {"$group": {"_id": "$was_informed_by", "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}},
    {
        "$lookup": {
            "from": "omics_processing_set",
            "localField": "_id",
            "foreignField": "id",
            "as": "omics_processing_set",
        }
    },
    {"$match": {"omics_processing_set.part_of": "nmdc:sty-11-547rwq94"}},
]


# look for the newest assembly record, look up upstream filtering record and reads based taxonomy analysis that uses the same record
def pick_records(omics_id):
    pick_records_pipeline = [
        {"$match": {"was_informed_by": omics_id}},
        {"$sort": {"_id": -1}},
        {"$limit": 1},
        {
            "$lookup": {
                "from": "read_qc_analysis_activity_set",
                "localField": "has_input",
                "foreignField": "has_output",
                "as": "upstream_filtering",
            }
        },
        {
            "$lookup": {
                "from": "read_based_taxonomy_analysis_activity_set",
                "localField": "has_input",
                "foreignField": "has_input",
                "as": "rbt_record_to_keep",
            }
        },
    ]
    records = list(asm_coll.aggregate(pick_records_pipeline))
    return records


# if there are multiple read based taxonomy records, only return the oldest


def pick_rbt(input_do):

    pick_oldest_rbt = [
        {"$match": {"has_input": input_do}},
        {"$sort": {"_id": -1}},
        {"$limit": 1},
    ]
    oldest_rbt = list(rbt_coll.aggregate(pick_oldest_rbt))
    return oldest_rbt


# list variables for which WXA should be kept

asm_keep = []
qc_keep = []
rbt_keep = []
asm_delete = []
qc_delete = []
rbt_delete = []
do_delete = []
test_list = list(asm_coll.aggregate(pipeline))


def data_objects_to_delete(output_list):
    for do in output_list:
        do_delete.append(do)


def find_asm_dups(omics_identifier, asm_keep_id):
    asm_duplicate_cursor = asm_coll.find(
        {"was_informed_by": omics_identifier, "id": {"$not": {"$regex": asm_keep_id}}}
    )
    for dup_asm in asm_duplicate_cursor:
        asm_delete.append(dup_asm["id"])
        data_objects_to_delete(dup_asm["has_output"])


def find_qc_dups(omics_identifier, qc_keep_id):
    qc_duplicate_cursor = qc_coll.find(
        {"was_informed_by": omics_identifier, "id": {"$not": {"$regex": qc_keep_id}}}
    )
    for qc_dup in qc_duplicate_cursor:
        qc_delete.append(qc_dup["id"])
        data_objects_to_delete(qc_dup["has_output"])


def find_rbt_dups(omics_identifier, rbt_keep_id):
    rbt_duplicate_cursor = rbt_coll.find(
        {"was_informed_by": omics_identifier, "id": {"$not": {"$regex": rbt_keep_id}}}
    )
    for rbt_dup in rbt_duplicate_cursor:
        rbt_delete.append(rbt_dup["id"])
        data_objects_to_delete(rbt_dup["has_output"])


for doc in test_list:
    omics_id = doc["_id"]
    records = pick_records(omics_id)
    if len(list(records)) == 1:
        for omics in records:
            if (
                len(omics["upstream_filtering"]) == 1
                and len(omics["rbt_record_to_keep"]) == 1
            ):
                asm_keep.append(omics["id"])
                find_asm_dups(doc["_id"], omics["id"])
                for filtering in omics["upstream_filtering"]:
                    qc_keep.append(filtering["id"])
                    find_qc_dups(doc["_id"], filtering["id"])
                for rbt in omics["rbt_record_to_keep"]:
                    rbt_keep.append(rbt["id"])
                    find_rbt_dups(doc["_id"], rbt["id"])
            elif (
                len(omics["upstream_filtering"]) == 1
                and len(omics["rbt_record_to_keep"]) == 0
            ):
                continue
            elif (
                len(omics["upstream_filtering"]) == 1
                and len(omics["rbt_record_to_keep"]) > 1
            ):
                # aggregation to get oldest filtering record
                asm_keep.append(omics["id"])
                for filtering in omics["upstream_filtering"]:
                    qc_keep.append(filtering["id"])
                    find_qc_dups(doc["_id"], filtering["id"])
                find_asm_dups(doc["_id"], omics["id"])
                input_list = omics["has_input"]
                target_do = input_list[0]
                oldest_rbt = pick_rbt(target_do)
                if len(list(oldest_rbt)) == 1:
                    for rbt in oldest_rbt:
                        rbt_keep.append(rbt["id"])
                    find_rbt_dups(doc["_id"], rbt["id"])
                else:
                    print("not sure what to do")
    else:
        print("not sure what to do for " + omics_id)

print(len(rbt_keep))
print(len(asm_keep))
print(len(qc_keep))

print(len(rbt_delete))
print(len(qc_delete))
print(len(asm_delete))
print(len(do_delete))


def make_deletes(delete_list, del_coll):
    request_body_file = del_coll + "_request_body.json"
    delete_statements = []
    for record in delete_list:
        delete_statements.append({"q": {"id": record}, "limit": 1})
    request_body_json = {"delete": del_coll, "deletes": delete_statements}
    with open(request_body_file, "w") as f:
        json.dump(request_body_json, f)


make_deletes(rbt_delete, rbt_coll_name)
make_deletes(qc_delete, qc_coll_name)
make_deletes(asm_delete, asm_coll_name)
make_deletes(do_delete, do_coll_name)
