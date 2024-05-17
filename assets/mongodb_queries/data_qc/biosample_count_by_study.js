db.getCollection('biosample_set').aggregate(
  [
    {
      $group: {
        _id: '$part_of',
        count: { $sum: 1 }
      }
    },
    {
      $lookup: {
        from: 'study_set',
        localField: '_id',
        foreignField: 'id',
        as: 'study_set'
      }
    },
    {
      $project: {
        'study_set.id': 1,
        'study_set.title': 1,
        count: 1
      }
    }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);

