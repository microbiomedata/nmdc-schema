var workflowActivitySets = [
    "mags_activity_set", "metagenome_assembly_set",
    "metagenome_annotation_activity_set", "metabolomics_analysis_activity_set",
    "metaproteomics_analysis_activity_set", "metatranscriptome_activity_set",
    "nom_analysis_activity_set", "read_based_taxonomy_analysis_activity_set",
    "read_qc_analysis_activity_set", "metagenome_sequencing_activity_set"
];

var results = [];

workflowActivitySets.forEach(function(activitySet) {
    var pipeline = [
        // Match workflowActivity documents where 'part_of' is not empty/null
        {
            $match: {
                part_of: { $exists: true, $ne: null }
            }
        },
        // Match workflowActivity documents where 'part_of' is 'OmicsProcessing.ID'
        {
            $lookup: {
                from: "omics_processing_set",
                localField: "part_of",
                foreignField: "id",
                as: "omics_processing"
            }
        },
        // Match workflowActivity documents where 'part_of' is another workflowActivity.ID of the same type
        {
            $lookup: {
                from: activitySet,
                localField: "part_of",
                foreignField: "id",
                as: "workflow_activity"
            }
        },
        // Filter out workflowActivity documents with no matching OmicsProcessing or workflowActivity of the same type
        {
            $match: {
                $and: [
                    { omics_processing: { $eq: [] } },
                    { workflow_activity: { $eq: [] } }
                ]
            }
        },
        // Project only necessary fields for the result
//        {
//            $project: {
//                id: 1,
//                part_of: 1
//            }
//        }
    ];

    var activityResults = db[activitySet].aggregate(pipeline).toArray();
    results.push({ activitySet: activitySet, activityResults: activityResults });
});

printjson(results);
