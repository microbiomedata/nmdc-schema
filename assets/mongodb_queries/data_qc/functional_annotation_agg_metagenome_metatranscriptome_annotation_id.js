// Find functional_annotation_agg records whose was_generated_by does not match any
// workflow_execution_set id. The schema requires was_generated_by and ranges it to
// AnnotatingWorkflow, which is stored in workflow_execution_set.
// The collection holds tens of millions of records, so this lookup is slow; add a
// $match on was_generated_by first to check one workflow's records.
db.functional_annotation_agg.aggregate([
  {
    $lookup: {
      from: "workflow_execution_set",
      localField: "was_generated_by",
      foreignField: "id",
      as: "annotating_workflows"
    }
  },
  {
    $match: {
      annotating_workflows: { $eq: [] }
    }
  }
])
