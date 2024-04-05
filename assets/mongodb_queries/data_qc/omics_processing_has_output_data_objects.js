db.omics_processing_set.aggregate([
  {
    $unwind: "$has_output"
  },
  {
    $lookup: {
      from: "data_object_set",
      localField: "has_output",
      foreignField: "id",
      as: "output_docs"
    }
  },
  {
    $match: {
      output_docs: { $eq: [] }
    }
  }
])

