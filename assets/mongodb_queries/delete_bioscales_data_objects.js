db.data_object_set.deleteMany(
{id: {$not: { $regex: '^nmdc:dobj*'}},'description':'Raw sequencer read data'}
)

