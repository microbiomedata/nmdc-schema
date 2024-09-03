db.getCollection('data_object_set').aggregate(
  [
    {
      $match: {
        id: {
          $not: { $regex: RegExp('nmdc:dobj-') }
        }
      }
    }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);
