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
      $or: [
        { output_docs: { $exists: false } },  // Check if output_docs doesn't exist
        { output_docs: { $size: 0 } }         // Check if output_docs is an empty array
      ]
    }
  }
])

