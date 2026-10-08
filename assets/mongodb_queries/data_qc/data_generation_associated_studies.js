db.data_generation_set.aggregate([
  {
    $lookup: {
      from: "study_set",
      localField: "associated_studies",
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
