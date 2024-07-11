var workflowActivitySets = ["mags_activity_set","metagenome_assembly_set",
    "metagenome_annotation_activity_set", "metabolomics_analysis_activity_set",
    "metaproteomics_analysis_activity_set", "metatranscriptome_activity_set",
    "nom_analysis_activity_set", "read_based_taxonomy_analysis_activity_set",
    "read_qc_analysis_activity_set", "metagenome_sequencing_activity_set"
    ];

var results = [];

workflowActivitySets.forEach(function (activitySet) {
    var pipeline = [{
        $unwind: "$has_output"
    }, {
        $lookup: {
            from: "data_object_set", localField: "has_output", foreignField: "id", as: "output_docs"
        }
    }, {
        $match: {
            output_docs: {$eq: []}
        }
    }, {
        $project: {
            _id: 1, has_output: 1
        }
    }];

    var activityResults = db[activitySet].aggregate(pipeline).toArray();
    results.push({activitySet: activitySet, activityResults: activityResults});
});

printjson(results);
