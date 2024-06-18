import json
import csv


def gen_delete(delete_list: list, key: str, limit: int, del_coll: str):
    if limit not in (0, 1):
        raise ValueError("limit must be 0 or 1.")
    delete_statement = []
    for record in delete_list:
        delete_statement.append({"q": {key: record}, "limit": limit})
    request_body_json = {"delete": del_coll, "deletes": delete_statement}
    request_body_file = del_coll + "_request_body.json"
    with open(request_body_file, "w") as f:
        json.dump(request_body_json, f)


# delete legacy orphan functional_annotation_agg records
delete_agg_list = []
with open("to_delete_nmdc.functional_annotation_agg.csv", newline="") as csvfile:
    agg_records = csv.reader(csvfile, delimiter=",")
    for row in agg_records:
        delete_agg_list.append(row[0])
del_coll = "functional_annotation_agg"
gen_delete(delete_agg_list, "metagenome_annotation_id", 0, del_coll)

# delete leagacy orphan data_object_set records
delete_do_list = []
with open("legacy_orphan.nmdc.data_object_set.csv", newline="") as csvfile:
    do_records = csv.reader(csvfile, delimiter=",")
    for row in do_records:
        delete_do_list.append(row[0])
del_coll = "data_object_set"
gen_delete(delete_do_list, "id", 1, del_coll)
