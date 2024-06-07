db.functional_annotation_agg.aggregate([
 
 {
  {
    $match: {"type":{"$in":[ "nmdc:MetagenomeAnnotation","nmdc:MetatranscriptomeAnnotation"]}}
  },
  {
    $lookup: {
      from: "workflow_exeuction_set",
      localField: "metagenome_annotation_id",
      foreignField: "id",
      as: "metagenome_annotation_activities"
    }
  },
  {
    $match: {
        { metagenome_annotation_activities: { $eq: [] } }
    }
  }
])

