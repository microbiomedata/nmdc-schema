// Check referential integrity for pooling has_input biosample or processed sample
db.pooling_set.aggregate([
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
