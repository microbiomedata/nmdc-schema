import csv
import pprint

from pymongo import MongoClient

m_pass = ""

client = MongoClient(
    f"mongodb://mam:{m_pass}@localhost:27027/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
)

id_inst_file ="../target/omics_processing_id_inst.tsv"

# on the verbose side for just retrieving a collection
result_filter = {}
result = client["nmdc"]["omics_processing_set"].find(filter=result_filter)

# print(type(result))
# <class 'pymongo.cursor.Cursor'>

# ['GOLD_sequencing_project_identifiers',
#  '_id',
#  'add_date',
#  'has_input',
#  'has_output',
#  'id',
#  'mod_date',
#  'name',
#  'ncbi_project_name',
#  'omics_type',
#  'part_of',
#  'principal_investigator',
#  'processing_institution',
#  'type']

id_inst = []
for i in result:
    id_inst.append(
        {"id": i["id"], "processing_institution": i["processing_institution"]}
    )

with open(id_inst_file, 'w') as f:
    csv_writer = csv.DictWriter(f, list(id_inst[0].keys()), delimiter="\t")
    csv_writer.writeheader()
    csv_writer.writerows(id_inst)
