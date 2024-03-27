db.sample_set.aggregate([
  {
    $lookup: {
      from: "study_set",
      localField: "part_of_study",
      foreignField: "study_id",
      as: "studies"
    }
  },
  {
    $match: {
      studies: { $eq: [] }
    }
  }
])