// Find data_generation_set has_output values that do not match any data_object_set id.
// Returns one result per dangling has_output value, not one per data generation record.
db.data_generation_set.aggregate([
  {
    $unwind: "$has_output"
  },
  {
    $lookup: {
      from: "data_object_set",
      localField: "has_output",
      foreignField: "id",
      as: "output_data_objects"
    }
  },
  {
    $match: {
      output_data_objects: { $eq: [] }
    }
  },
  {
    $project: {
      id: 1,
      has_output: 1
    }
  }
])
