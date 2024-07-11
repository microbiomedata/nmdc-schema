import json

# from bson import json_util, ObjectId
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

prod_mongo = "mongodb://aclum:wqNj7hWW*oWmzQ2FsL%40f@localhost:37019/?authMechanism=SCRAM-SHA-256&authSource=admin&directConnection=true"
client = MongoClient(prod_mongo)
mydb = client["nmdc"]

# for db in client.list_database_names():
#    print(db)
# collection names
asm_coll = mydb["metagenome_assembly_set"]
qc_coll = mydb["read_qc_analysis_activity_set"]
rbt_coll = mydb["read_based_taxonomy_analysis_activity_set"]
ann_coll = mydb["metagenome_annotation_activity_set"]
mags_coll = mydb["mags_activity_set"]
omics_coll = mydb["omics_processing_set"]
ann_agg_coll = mydb["functional_annotation_agg"]
data_object_coll = mydb["data_object_set"]

# asm_cursor=asm_coll.find({"was_informed_by":"nmdc:omprc-11-c82tqn53"})
# print(len(list(asm_cursor)))

del_asm_coll = []
del_qc_coll = []
del_rbt_coll = []
del_ann_coll = []
del_mags_coll = []
del_do = []
del_omics = []
collections_dict = {
    asm_coll: del_asm_coll,
    qc_coll: del_qc_coll,
    rbt_coll: del_rbt_coll,
    ann_coll: del_ann_coll,
    mags_coll: del_mags_coll,
}

del_dict = {
    "metagenome_assembly_set": del_asm_coll,
    "read_qc_analysis_activity_set": del_qc_coll,
    "read_based_taxonomy_analysis_activity_set": del_rbt_coll,
    "metagenome_annotation_activity_set": del_ann_coll,
    "mags_activity_set": del_mags_coll,
    "data_object_set": del_do,
    "omics_processing_set": del_omics,
}

neon_omics = open("/Users/aclum/Downloads/neon_omics_to_fail.txt", "r")


img_list = []
omics_list = []
# get workflow activity ID and data object IDs to delete
for omics in neon_omics:
    omics_list.append(omics.strip())
    for coll in collections_dict:
        query = {"was_informed_by": omics.strip()}
        wxa_record = coll.find(query)
        for doc in wxa_record:
            collections_dict[coll].append(doc["id"])
            img_info = [doc["id"], doc["was_informed_by"], doc["type"]]
            list = ",".join(img_info)
            img_list.append(list)
            for output in doc["has_output"]:
                del_do.append(output)

with open("neon_delete_img.csv", "w") as f:
    for line in img_list:
        f.write(f"{line}\n")

# for coll in collections_dict:
#  print(coll)
#  print(collections_dict[coll])
#


for omics in omics_list:
    query = {"id": omics}
    omics_doc = omics_coll.find_one(query)
    del_omics.append(omics_doc["id"])
    for output in omics_doc["has_output"]:
        del_do.append(output)
        print(data_object_coll.find_one({"id": output}))

pipeline = [
    {"$match": {"id": omics}},
    {
        "$lookup": {
            "from": "data_object_set",
            "localField": "has_output",
            "foreignField": "id",
            "as": "seq_files",
        }
    },
    {"$project": {"name": 1, "id": 1, "seq_files.id": 1, "seq_files.url": 1}},
]

omics_full_record = []
for record in omics:
    omics_agg_doc = omics_coll.aggregate(pipeline)
    for doc in omics_agg_doc:
        print(doc)
        omics_full_record.append(doc)

# json_object=json_util.dumps(omics_full_record)
# with open ("20240523_neon_soil_bad_pairs.json", 'w') as f:
#  f.write(json_object)

for del_coll, del_values in del_dict.items():
    request_body_file = del_coll + "request_body.json"
    request_deletes = []
    for value in del_values:
        request_deletes.append({"q": {"id": value}, "limit": 1})
    request_body_json = {"delete": del_coll, "deletes": request_deletes}
    with open(request_body_file, "w") as f:
        json.dump(request_body_json, f)

request_agg_del = []
for ann in del_ann_coll:
    request_agg_del.append({"q": {"metagenome_annotation_id": ann}, "limit": 0})
request_body_json = {"delete": "functional_annotation_agg", "deletes": request_agg_del}
with open("agg_delete_request.json", "w") as f:
    json.dump(request_body_json, f)

neon_omics.close()
