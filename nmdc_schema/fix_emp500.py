import pymongo

db="nmdc"

study_id=""
def get_omics_sharing_was_informed_by(study_id):
   pipeline =[
    {      "$group": {        "_id": "$was_informed_by",        "count": { "$sum": 1 }      }    },
    { "$match": { "count": { "$gt": 1 } } },
    {      "$lookup": {        "from": "omics_processing_set",        "localField": "_id",        "foreignField": "id",        "as": "omics_processing_set"      }    },
    {      "$match": {        "omics_processing_set.part_of":          study_id      }
]

  coll="metagenome_assembly_set"
  multiple_workflow_results=db.coll.aggregate(pipeline)
  return(multiple_workflow_results) 

def get_records_to_keep(multiple_workflow_results):


  asm_coll="metagenome_assembly_set""
  qc_coll="read_qc_analysis_activity_set"
  rbt_coll="read_based_taxonomy_analysis_activity_set"
  omics_project=""
  #look for the newest assembly record, look up upstream filtering record and reads based taxonomy analysis that uses the same record
  #to do: add logic to make sure qc and reads based taxonomy exist
  pick_records_pipeline = [
  { "$match": {
    "was_informed_by": omics_project}
  },
  { "$sort": { "_id": -1 } },
  { "$limit": 1 },
  { "$lookup": {
    "from": "read_qc_analysis_activity_set",
    "localField": "has_input",
    "foreignField": "has_output",
    "as": "upstream_filtering"
   }
  },
  { "$lookup": {
    "from": "read_based_taxonomy_analysis_activity_set",
    "localField": "has_input",
    "foreignField": "has_input",
    "as": "rbt_record_to_keep" }
 }
 ]
  asm_keep=[]
  qc_keep=[]
  rbt_keep=[]
  for doc in multiple_workflow_results:
    omics_record=doc["_id"]
    records=db.asm_coll.aggregate(pick_records_pipeline)
    if len(records) == 1:
      asm_keep.append(records["id"])
      qc_keep.append(records["upstream_filtering.id"])
      rbt_keep.append(records["rbt_record_to_keep.id"])


