db.getCollection(
  'functional_annotation_agg'
).aggregate(
  [
    {
      $lookup: {
        from: 'metagenome_annotation_activity_set',
        localField: 'metagenome_annotation_id',
        foreignField: 'id',
        as: 'annotation_activities'
      }
    },
    {
      $match: {
        annotation_activities: { $size: 0 }
      }
    },
    {
      $group: {
        _id: '$metagenome_annotation_id',
        count: { $sum: 1 }
      }
    }
  ],
  { maxTimeMS: 90000, allowDiskUse: true }
);
