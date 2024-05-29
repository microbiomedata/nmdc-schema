db.getCollection("data_object_set").find({
    "id": {
        "$not": /^nmdc:dobj/
    }
}).forEach(function (doc) {
    db.data_object_set.deleteOne({
        "_id": doc._id
    });
});