var workflowActivitySets = ["metagenome_assembly_set", "metagenome_annotation_set", "metabolomics_analysis_activity_set",
"metaproteomics_analysis_activity_set", "metatranscriptome_activity_set", "nom_analysis_activity_set", "mags_activity_set"];

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
