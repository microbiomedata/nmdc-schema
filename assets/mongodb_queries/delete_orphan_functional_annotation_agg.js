db.functional_annotation_agg.aggregate([
  {
    $lookup: {
      from: "metagenome_annotation_activity_set",
      localField: "metagenome_annotation_id",
      foreignField: "id",
      as: "annotation_activities"
    }
  },
  {
    $match: {
      annotation_activities: { $eq: [] }
    }
  }
]).forEach(function(doc) {
    db.functional_annotation_agg.deleteMany({ _id: doc._id });
});