db.getCollection('metabolomics_analysis_activity_set').aggregate(
[
{
$match: { has_calibration: { $ne: null } }
},
{
$lookup: {
from: 'data_object_set',
localField: 'has_calibration',
foreignField: 'id',
as: 'data_object'
}
},
{
$match: {
$and: [{ data_object: { $eq: [] } }]
}
},
{
$match: {
has_calibration: {
$not: { $regex: RegExp('False', 'i') }
}
}
}
],
{ maxTimeMS: 60000, allowDiskUse: true }
);