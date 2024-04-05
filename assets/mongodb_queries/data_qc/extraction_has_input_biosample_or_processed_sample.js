// Check referential integrity for extraction has_input biosample
db.extraction_set.aggregate([
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
        $match: {
        $and: [
            { biosamples: { $eq: [] } },
            { processed_samples: { $eq: [] } }
        ]
        }
    }
])