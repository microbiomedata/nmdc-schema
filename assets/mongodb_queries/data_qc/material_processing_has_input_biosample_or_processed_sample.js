// Find each material processing has_input value that matches no Sample: not a biosample, a processed
// sample or an organism sample. has_input holds a list, so it is unwound first: one
// result per dangling value.
db.material_processing_set.aggregate([
  {
    $unwind: "$has_input"
  },
  {
    $lookup: {
      from: "biosample_set",
      localField: "has_input",
      foreignField: "id",
      as: "biosamples"
    }
  },
  {
    $lookup: {
      from: "processed_sample_set",
      localField: "has_input",
      foreignField: "id",
      as: "processed_samples"
    }
  },
  {
    $lookup: {
      from: "organism_sample_set",
      localField: "has_input",
      foreignField: "id",
      as: "organism_samples"
    }
  },
  {
    $match: {
      $and: [
        { biosamples: { $eq: [] } },
        { processed_samples: { $eq: [] } },
        { organism_samples: { $eq: [] } }
      ]
    }
  },
  {
    $project: {
      id: 1,
      has_input: 1
    }
  }
])
