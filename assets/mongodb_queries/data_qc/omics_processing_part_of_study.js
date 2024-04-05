db.omics_processing_set.aggregate([
  {
    $lookup: {
      from: "study_set",
      localField: "part_of",
      foreignField: "id",
      as: "studies"
    }
  },
  {
    $match: {
      studies: { $eq: [] }
    }
  }
])
