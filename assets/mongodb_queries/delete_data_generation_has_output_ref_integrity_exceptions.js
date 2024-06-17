// Description: Delete data_generation_set documents that have invalid references in has_output field.
// This script will delete the omics_processing_set documents that have invalid references in has_output field.

db.data_generation_set.aggregate([
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
]).forEach(function(doc) {
    db.data_generation_set.deleteMany({ _id: doc._id }); // Delete the matching documents
});
