import pprint

import pendulum as pendulum
from dotenv import dotenv_values
import pymongo
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, json_dumper

from nmdc_schema.nmdc import Database

dotenv_file = "../local/.env"

schema_file = "../src/schema/nmdc.yaml"

mongodb_suffix = "@localhost:27027/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

max_collection_bytes = 10000000000

database_obj = Database()

print(f"Loading config from {dotenv_file}")

config = dotenv_values(dotenv_file)

print(f"Loading schema from {schema_file}")

nmdc_view = SchemaView(schema_file)

database_slots = nmdc_view.class_slots("Database")

myclient = pymongo.MongoClient(
    f"mongodb://{config['MONGO_USER']}:{config['MONGO_PASS']}{mongodb_suffix}"
)

mydb = myclient["nmdc"]

mongo_collections = mydb.list_collection_names()

collections_to_repair = set(database_slots).intersection(set(mongo_collections))

print("Gathering mongodb collection stats")

collections_to_repair = [
    'activity_set',
    'biosample_set',
    'data_object_set',  # ValueError: Unknown FileTypeEnum enumeration code: Metagenome Raw Reads
    # 'functional_annotation_set',
    # 'genome_feature_set',
    # 'mags_activity_set',
    # 'metabolomics_analysis_activity_set',
    # 'metagenome_annotation_activity_set',
    # 'metagenome_assembly_set',
    'metaproteomics_analysis_activity_set',
    'metatranscriptome_activity_set',
    'nom_analysis_activity_set',
    'omics_processing_set',
    'study_set'
]

selected_stats = {}
for collection_name in collections_to_repair:
    for_selected_stats = {}

    collection_stats = mydb.command("collstats", collection_name)

    for_selected_stats["document_count"] = collection_stats["count"]
    for_selected_stats["size_in_bytes"] = collection_stats["size"]
    for_selected_stats["storageSize"] = collection_stats["storageSize"]

    selected_stats[collection_name] = for_selected_stats

sorted_selected_stats = sorted(selected_stats.items(), key=lambda x: x[1]['storageSize'])

# PROBLEM CASE: slot name has been changed since data was saved
# todo right now only works for root-level slots within each document
name_replacements = {
    "Biosample": {
        "GOLD_sample_identifiers": "gold_sample_identifiers",
        "INSDC_biosample_identifiers": "insdc_biosample_identifiers",
        "part_of": "sample_link",
    },
    "Study": {
        "GOLD_study_identifiers": "gold_study_identifiers",
    },
    "OmicsProcessing": {
        "GOLD_sequencing_project_identifiers": "gold_sequencing_project_identifiers",
    },
    "MagsAnalysisActivity": {
        "num_tRNA": "num_trna",  # inside of mags_list
    },
    "MetagenomeAssembly": {
        "ctg_L50": "contig_L50",
        "ctg_L90": "contig_L90",
        "ctg_N50": "contig_N50",
        "ctg_N90": "contig_N90",
        "scaf_L50": "scaffold_L50",
        "scaf_L90": "scaffold_L90",
        "scaf_N50": "scaffold_N50",
        "scaf_N90": "scaffold_N90",
        "scaf_l_gt50K": "scaffold_l_gt50K",
        "scaf_n_gt50K": "scaffold_n_gt50K",
        "scaf_pct_gt50K": "scaffold_pct_gt50K",
    }
}

# todo this doesn't do the following yet:
#  - break raw values from env_broad_scale etc into the term name and the term id
#  - collapse depth2 into depth

print("starting dumps from mongodb")

data_object_file_type_values = set()

for collection_name in collections_to_repair:
    print(collection_name)
    collection_stats = selected_stats[collection_name]
    print(collection_stats)
    collection_range = nmdc_view.get_slot(collection_name).range
    print(f"range for {collection_name} = {collection_range}")
    range_class = nmdc_view.get_class(collection_range)
    range_slot_names = nmdc_view.class_slots(range_class.name)
    range_slot_names.sort()

    if collection_stats["size_in_bytes"] > max_collection_bytes:
        print(f"Over max_collection_bytes limit of {max_collection_bytes} for migration: {collection_stats}")
    else:
        print(f"Within max_collection_bytes limit of {max_collection_bytes} for migration:  {collection_stats}")
        collection = mydb[collection_name]
        cursor = collection.find({})
        for document in cursor:
            del document["_id"]
            if range_class.name in name_replacements:
                for old_name, new_name in name_replacements[range_class.name].items():
                    # print(f"Replacing {old_name} with {new_name}")
                    if old_name in document:
                        document[new_name] = document[old_name]
                        del document[old_name]
            if collection_name == "data_object_set" and "data_object_type" in document:
                # print(document["data_object_type"])
                data_object_file_type_values.add(document["data_object_type"])

            else:
                pass
                # print(f"no name replacements for {range_class.name}")
            # PROBLEM CASE: improperly formatted dates
            # todo remove need for enumerating date fields
            if 'started_at_time' in document:
                sadt = str(pendulum.parse(document['started_at_time']))
                # print(sadt)
                document['started_at_time'] = sadt
            if 'ended_at_time' in document:
                eadt = str(pendulum.parse(document['ended_at_time']))
                document['ended_at_time'] = eadt
            database_obj[collection_name].append(document)
        if len(database_obj[collection_name]) == 0:
            del database_obj[collection_name]

used_object_type_values = data_object_file_type_values
print(f"data_object_file_type_values values: {used_object_type_values}")

defined_object_type_pvs = nmdc_view.get_enum("file type enum").permissible_values
defined_object_type_texts = set([pvv.text for pvk, pvv in defined_object_type_pvs.items()])

unexpected_object_type_values = list(used_object_type_values - defined_object_type_texts)

unexpected_object_type_values.sort()

print(unexpected_object_type_values)

print("dumping to json")

json_dumper.dump(database_obj, "mongo_dump.json")

print("done")
