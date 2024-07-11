var workflowActivitySets = ["mags_activity_set","metagenome_assembly_set",
    "metagenome_annotation_activity_set", "metabolomics_analysis_activity_set",
    "metaproteomics_analysis_activity_set", "metatranscriptome_activity_set",
    "nom_analysis_activity_set", "read_based_taxonomy_analysis_activity_set",
    "read_qc_analysis_activity_set"
    ];
var results = [];

workflowActivitySets.forEach(function(activitySet) {
    var pipeline = [
        {
            $unwind: "$has_input"
        },
        {
            $lookup: {
                from: "data_object_set",
                localField: "has_input",
                foreignField: "id",
                as: "input_docs"
            }
        },
        {
            $match: {
                input_docs: { $eq: [] }
            }
        },
        {
            $project: {
                id: 1,
                has_input: 1
            }
        }
    ];

    var activityResults = db[activitySet].aggregate(pipeline).toArray();
    results.push({ activitySet: activitySet, activityResults: activityResults });
});

printjson(results);
