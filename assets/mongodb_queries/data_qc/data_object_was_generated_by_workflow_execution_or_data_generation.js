var applicableClasses = ["data_object_set", ] // what other sets go here?

var results = [];

applicableClasses.forEach(function(applicableClass) {
    var pipeline = [
        {
            $unwind: "$was_generated_by"
        },
        {
            $lookup: {
                from: "workflow_execution_set",
                localField: "was_generated_by",
                foreignField: "id",
                as: "was_generated_by_docs"
            }
        },
        {
            $lookup: {
                from: "data_generation_set",
                localField: "was_generated_by",
                foreignField: "id",
                as: "generated_by_omics_processing_docs"
            }
        },
        {
            $match: {
                $and: [
                    {was_generated_by_docs: { $eq: [] }},
                    {generated_by_omics_processing_docs: { $eq: [] }}
                ]
            }
        },
        {
            $project: {
                id: 1,
                was_generated_by: 1
            }
        }
    ];

    var applicableClassResults = db[applicableClass].aggregate(pipeline).toArray();
    results.push({applicableClass: applicableClass, applicableClassResults: ApplicableClassResults})
}
);

printjson(results);
