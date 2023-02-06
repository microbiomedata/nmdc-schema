import csv

from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv("../../local/.env")

id_inst_file = "../omics_processing_id_inst.tsv"

mongo_pw = os.getenv("MONGO_PW")

client = MongoClient(
    f"mongodb://mam:{mongo_pw}@localhost:27027/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
)

# on the verbose side for just retrieving a collection
result_filter = {}
result = client["nmdc"]["omics_processing_set"].find(filter=result_filter)

id_inst = []
for i in result:
    id_inst.append(
        {"id": i["id"], "processing_institution": i["processing_institution"]}
    )

with open(id_inst_file, 'w') as f:
    csv_writer = csv.DictWriter(f, list(id_inst[0].keys()), delimiter="\t")
    csv_writer.writeheader()
    csv_writer.writerows(id_inst)
