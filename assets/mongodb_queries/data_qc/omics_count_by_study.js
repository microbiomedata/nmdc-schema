db.getCollection(
  'omics_processing_set'
).aggregate(
  [
    {
      $group: {
        _id: {
          study: '$part_of',
          type: '$omics_type.has_raw_value'
        },
        count: { $sum: 1 }
      }
    },
    {
      $lookup: {
        from: 'study_set',
        localField: '_id.study',
        foreignField: 'id',
        as: 'study_set'
      }
    },
    {
      $project: {
        count: 1,
        'study_set.id': 1,
        'study_set.title': 1
      }
    }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);
