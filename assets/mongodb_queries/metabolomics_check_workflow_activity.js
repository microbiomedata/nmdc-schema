// Check that all metabolomics omics records have associated workflow activities.

db.getCollection(
  'omics_processing_set'
).aggregate(
  [
    {
      $match: {
        'omics_type.has_raw_value': 'Metabolomics'
      }
    },
    {
      $lookup: {
        from: 'metabolomics_analysis_activity_set',
        localField: 'id',
        foreignField: 'was_informed_by',
        as: 'metab_activity'
      }
    },
    { $match: { metab_activity: { $size: 0 } } }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);
