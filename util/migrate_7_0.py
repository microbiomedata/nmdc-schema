import pprint
import re

import pendulum as pendulum
from dotenv import dotenv_values
from linkml.validators import JsonSchemaDataValidator
from linkml_runtime import SchemaView
from pymongo import MongoClient

from nmdc_schema.nmdc import Database

# import yaml
# from linkml_runtime.dumpers import yaml_dumper
# , Biosample, ControlledTermValue, OntologyClass

dotenv_file = "../local/.env"

schema_file = "../src/schema/nmdc.yaml"

remote_mongodb_suffix = \
    "@localhost:27027/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

repaired_file = "../assets/nmdc_7_0.json"

# assuming no user/pw authentication for now
dest_mongo_address = "127.0.0.1"
dest_mongo_port = "27777"
dest_mongo_dbname = "nmdc_7_0_0"
excluded_collections = ['@type']

max_collection_bytes = 10000000000
last_doc_num = 999999

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
        "num_tRNA": "num_trnanum_t_rna",  # inside of mags_list of MagBin instances,
        "lowDepth_contig_num": "low_depth_contig_num",
    },
    "MetagenomeAssembly": {
        "ctg_L50": "ctg_l50",
        "ctg_L90": "ctg_l90",
        "ctg_N50": "ctg_n50",
        "ctg_N90": "ctg_n90",
        "scaf_L50": "scaf_l50",
        "scaf_L90": "scaf_l90",
        "scaf_N50": "scaf_n50",
        "scaf_N90": "scaf_n90",
        "scaf_l_gt50K": "scaf_l_gt50k",
        "scaf_n_gt50K": "scaf_n_gt50k",
        "scaf_pct_gt50K": "scaf_pct_gt50k",
    }
}

database_obj = Database()

print(f"Loading config from {dotenv_file}")

config = dotenv_values(dotenv_file)

print(f"Loading schema from {schema_file}")

nmdc_view = SchemaView(schema_file)

database_slots = nmdc_view.class_slots("Database")

remote_client = MongoClient(
    f"mongodb://{config['MONGO_USER']}:{config['MONGO_PASS']}{remote_mongodb_suffix}"
)

remote_db = remote_client["nmdc"]

ots = remote_db['omics_processing_set'].find().distinct('omics_type.has_raw_value')
ots.sort()
pprint.pprint(ots)

remote_collections = remote_db.list_collection_names()

collections_intersection = set(database_slots).intersection(set(remote_collections))
collections_intersection = list(collections_intersection)
collections_intersection.sort()

print("Gathering mongodb collection stats")

# # todo we should switch to using the collections_intersection
# #  this avoids large and known-problematic collections
#
# collections_to_repair = [
#     'activity_set',
#     'biosample_set',
#     'data_object_set',
#     'functional_annotation_set',
#     'genome_feature_set',
#     'mags_activity_set',
#     'metabolomics_analysis_activity_set',
#     'metagenome_annotation_activity_set',
#     'metagenome_assembly_set',
#     'metaproteomics_analysis_activity_set',
#     'metatranscriptome_activity_set',
#     'nom_analysis_activity_set',
#     'omics_processing_set',
#     'study_set'
# ]

selected_stats = {}
for collection_name in collections_intersection:
    for_selected_stats = {}

    collection_stats = remote_db.command("collstats", collection_name)

    for_selected_stats["document_count"] = collection_stats["count"]
    for_selected_stats["size_in_bytes"] = collection_stats["size"]
    for_selected_stats["storageSize"] = collection_stats["storageSize"]

    selected_stats[collection_name] = for_selected_stats

sorted_selected_stats = sorted(selected_stats.items(), key=lambda x: x[1]['size_in_bytes'])

pprint.pprint(sorted_selected_stats)

print("starting dumps from mongodb")

data_object_file_type_values = set()

for collection_name in collections_intersection:
    print(collection_name)
    collection_stats = selected_stats[collection_name]
    print(collection_stats)
    collection_range = nmdc_view.get_slot(collection_name).range
    print(f"range for {collection_name} = {collection_range}")
    range_class = nmdc_view.get_class(collection_range)
    range_slot_names = nmdc_view.class_slots(range_class.name)
    range_slot_names.sort()

    collection = remote_db[collection_name]
    cursor = None
    if collection_stats["size_in_bytes"] > max_collection_bytes:
        print(f"Over max_collection_bytes limit of {max_collection_bytes} for migration: {collection_stats}")
        cursor = collection.find({}).limit(last_doc_num)
    else:
        print(f"Within max_collection_bytes limit of {max_collection_bytes} for migration:  {collection_stats}")
        cursor = collection.find({})
    for document in cursor:
        del document["_id"]
        if range_class.name in name_replacements:
            for old_name, new_name in name_replacements[range_class.name].items():
                if old_name in document:
                    document[new_name] = document[old_name]
                    del document[old_name]
        if collection_name == "data_object_set" and "data_object_type" in document:
            data_object_file_type_values.add(document["data_object_type"])
        else:
            pass

        # PROBLEM CASE: improperly formatted dates
        # todo remove need for enumerating date fields
        if 'started_at_time' in document:
            sadt = str(pendulum.parse(document['started_at_time']))
            document['started_at_time'] = sadt
        if 'ended_at_time' in document:
            eadt = str(pendulum.parse(document['ended_at_time']))
            document['ended_at_time'] = eadt
        if collection_name == "data_object_set" and ("id" not in document or not document["id"]):
            print(f"no id in document: {document}")
            document['id'] = f"nmdc:{document['md5_checksum']}"
        else:
            pass

        if collection_name == "mags_activity_set" and 'mags_list' in document and document['mags_list']:
            for i in document['mags_list']:
                if 'num_tRNA' in i:
                    i['num_t_rna'] = i['num_tRNA']
                    del i['num_tRNA']

        # PROBLEM CASE: depth2 will be removed from the schema
        if collection_name == "biosample_set":
            if "depth2" in document:
                # print(f"depth: {document['depth']}")
                if "depth" in document:
                    # print(f"depth2: {document['depth2']}")
                    if document['depth']['has_unit'] != document['depth2']['has_unit']:
                        print(
                            f"PROBLEM: depth and depth2 have different units: {document['depth']['has_unit']} and {document['depth2']['has_unit']}")
                    else:
                        # print(f"depth and depth2 have same units: {document['depth']['has_unit']}")
                        if 'has_numeric_value' in document['depth2']:
                            if 'has_maximum_numeric_value' in document['depth']:
                                if document['depth']['has_maximum_numeric_value'] != document['depth2'][
                                    'has_numeric_value']:
                                    print(
                                        f"PROBLEM: depth and depth2 have different maximum values: {document['depth']['has_maximum_numeric_value']} and {document['depth2']['has_maximum_numeric_value']}")
                                else:
                                    del document['depth2']
                            else:
                                # todo any assumptions?
                                document['depth']['has_maximum_numeric_value'] = document['depth2'][
                                    'has_numeric_value']
                                del document['depth2']
                else:
                    print("depth2 but no depth")
                    # todo assuming the depth2 object has all of these fields
                    document['depth'] = {'has_numeric_value': document['depth']['has_numeric_value'],
                                         'has_raw_value': document['depth']['has_raw_value'],
                                         'has_unit': document['depth']['has_unit']}
                    del document['depth2']
            else:
                pass
                # print("SURPRISE: no depth2")
            # PROBLEM CASE: MIXS env triad objects must include a OntologyTerm id
            #  would like to include the name/label, too
            #  this causes breakage in 'omics_processing_set'[]['omics_type']
            # https://microbiomedata.github.io/nmdc-schema/ControlledTermValue/
            for triad_slot in ['env_broad_scale', 'env_local_scale', 'env_medium']:
                if 'term' not in document[triad_slot]:
                    if 'has_raw_value' not in document[triad_slot]:
                        print(f"  PROBLEM: no has_raw_value in {triad_slot}")
                    else:
                        # todo how much flexibility for the ontology prefix?
                        m = re.search(r'\b(.*:\d+)', document[triad_slot]['has_raw_value'])
                        if m:
                            # todo check for multiple matches
                            document[triad_slot]['term'] = {'id': m.group(0)}
                        else:
                            print(f"    no ENVO:(\\d+) in {triad_slot} has_raw_value")

        database_obj[collection_name].append(document)
    if len(database_obj[collection_name]) == 0:
        del database_obj[collection_name]

defined_object_type_pvs = nmdc_view.get_enum("file type enum").permissible_values
defined_object_type_texts = set([pvv.text for pvk, pvv in defined_object_type_pvs.items()])

unexpected_object_type_values = list(data_object_file_type_values - defined_object_type_texts)

unexpected_object_type_values.sort()

local_client = MongoClient(
    f"mongodb://{dest_mongo_address}:{dest_mongo_port}"
)

local_db = local_client[dest_mongo_dbname]

local_collections = local_db.list_collection_names()

print("attempting to validate repaired data")
val_inst = JsonSchemaDataValidator(schema_file)
val_inst.validate_object(database_obj)
print("data validation complete")

for i in collections_intersection:
    if i in excluded_collections:
        print(f"Skipping {i}")
    else:
        if i in local_collections:
            print(f"Dropping local {i}")
            collection = local_db[i]
            collection.drop()
        if i in database_obj and database_obj[i]:
            collection = local_db[i]
            print(f"Inserting {i}")
            insertion = collection.insert_many(database_obj[i])
            print(f"Inserted {len(insertion.inserted_ids)} documents")
        else:
            print(f"Skipping {i} because it has no documents")

print("done")
