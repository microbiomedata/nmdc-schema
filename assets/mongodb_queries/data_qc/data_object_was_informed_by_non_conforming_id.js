db.getCollection('data_object_set').aggregate(

[
{
$match: { id : { $regex: 'nmdc:dobj' } }
},
{
$match: { was_generated_by: { $ne: null } }
},
{
$match: {
$and: [
{
was_generated_by: {
$not: { $regex: 'nmdc:wf' }
}
},
{
was_generated_by: {
$not: { $regex: 'nmdc:omprc' }
}
}
]
}
}
],
{ maxTimeMS: 60000, allowDiskUse: true }
);
