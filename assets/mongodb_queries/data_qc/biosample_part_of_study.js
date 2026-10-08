// Find each biosample associated_studies value that matches no study_set id.
// associated_studies holds a list, so it is unwound first: one result per dangling value.
db.biosample_set.aggregate([
  {
    $unwind: "$associated_studies"
  },
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
  },
  {
    $project: {
      id: 1,
      associated_studies: 1
    }
  }
])
