import json
import csv


def gen_delete(delete_list: list, key: str, limit: int, del_coll: str):
    r"""
    Generates HTTP request bodies that can be sent to the Runtime API's
    `/queries:run` endpoint in order to delete documents from the database.
    """
    if limit not in (0, 1):
        raise ValueError("limit must be 0 or 1.")
    delete_statement = []
    for record in delete_list:
        delete_statement.append({"q": {key: r"%s" % record}, "limit": limit})
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
# uses regex as a workaround for newline issues double backslash issues
delete_do_list = []
with open("legacy_orphan.nmdc.data_object_set.csv", newline="") as csvfile:
    do_records = csv.reader(csvfile, delimiter=",")
    for row in do_records:
        strip_id = row[1].replace("\\n", "")
        print(strip_id)
        delete_do_list.append({"q": {"id": {"$regex": strip_id}}, "limit": 1})
    request_body_json = {"delete": "data_object_set", "deletes": delete_do_list}
    request_body_file = "data_object_set_request_body.json"
    with open(request_body_file, "w") as f:
        json.dump(request_body_json, f)
