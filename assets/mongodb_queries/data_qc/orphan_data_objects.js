var workflowActivitySets = ["metagenome_assembly_set", "metagenome_annotation_set", "metabolomics_analysis_activity_set",
"metaproteomics_analysis_activity_set", "metatranscriptome_activity_set", "nom_analysis_activity_set"];

var dataObjectIds = db.data_object_set.distinct("id");

var pipeline = [
    {
        $lookup: {
            from: "data_object_set",
            localField: "has_output",
            foreignField: "id",
            as: "output_docs"
        }
    },
    {
        $match: {
            output_docs: { $eq: [] }
        }
    },
    {
        $project: {
            _id: 1,
            has_output: 1
        }
    }
];

var results = db[workflowActivitySets[0]].aggregate(pipeline).toArray();

printjson(results);
