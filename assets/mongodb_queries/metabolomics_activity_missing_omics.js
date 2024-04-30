//find metabolomics activites where the omics record doesn't exist

db.getCollection(
  'metabolomics_analysis_activity_set'
).aggregate(
  [
    {
      $lookup: {
        from: 'omics_processing_set',
        localField: 'was_informed_by',
        foreignField: 'id',
        as: 'omics_processing_set'
      }
    },
    {
      $match: {
        omics_processing_set: { $size: 0 }
      }
    }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);
