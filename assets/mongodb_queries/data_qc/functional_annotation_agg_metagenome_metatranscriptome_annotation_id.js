db.functional_annotation_agg.aggregate([
  {
    $lookup: {
      from: "metagenome_annotation_activity_set",
      localField: "metagenome_annotation_id",
      foreignField: "id",
      as: "metagenome_annotation_activities"
    }
  },
  {
    $lookup: {
      from: "metatranscriptome_annotation_activity_set",
      localField: "metatranscriptome_annotation_id",
      foreignField: "id",
      as: "metatranscriptome_annotation_activities"
    }
  },
  {
    $match: {
      $and: [
        { metagenome_annotation_activities: { $eq: [] } },
        { metatranscriptome_annotation_activities: { $eq: [] } }
      ]
    }
  }
])

