import importlib
import json
import logging
import pprint
import re
import uuid

import click
import click_log
import pendulum as pendulum

from dotenv import dotenv_values

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, json_dumper, rdf_dumper
from linkml_runtime.loaders import json_loader, rdf_loader
from pymongo import MongoClient

from python.nmdc import Database

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

# todo update OmicsProcessings to use new Biosample IDs
#   for now, just trust that the collections will be processed in alphabetical order

# todo if there are multiple biosample gold identifiers, then how do we know whether one is more trusted?

# PROBLEM CASE: slot name has been changed since data was saved
# todo right now only works for root-level slots within each document
name_replacements = {
    "Biosample": {
        "INSDC_biosample_identifiers": "insdc_biosample_identifiers",
        # # "part_of": "sample_link",
        "identifier": "samp_name",
        "GOLD_sample_identifiers": "gold_biosample_identifiers",
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

drop = {
    "ReadQcAnalysisActivity": [
        "version",
    ]
}

# PROBLEM CASE: Biosample instances should be identified with an nmdc: identifier
# todo add minting of nmdc: identifiers
#   for now, using uuids as placeholders
# this requires routing whatever currently appears in the id slot to some other slot

#   52 id_prefix: emsl
#  648 id_prefix: gold
#   53 id_prefix: igsn

biosample_id_routing = {
    "emsl": "emsl_biosample_identifiers",
    "gold": "gold_biosample_identifiers",
    "igsn": "igsn_biosample_identifiers",
    "img.taxon": "img_identifiers"
}

slot2coll = {
    'activity_set': 'activity_set',
    'biosample_set': 'biosample_set',
    'data_object_set': 'data_object_set',
    'mags_activity_set': 'mags_activity_set',
    'metabolomics_analysis_activity_set': 'metabolomics_analysis_activity_set',
    'metagenome_annotation_activity_set': 'metagenome_annotation_activity_set',
    'metagenome_assembly_set': 'metagenome_assembly_set',
    'metaproteomics_analysis_activity_set': 'metaproteomics_analysis_activity_set',
    'metatranscriptome_activity_set': 'metatranscriptome_activity_set',
    'nom_analysis_activity_set': 'nom_analysis_activity_set',
    'omics_processing_set': 'omics_processing_set',
    'read_qc_analysis_activity_set': 'read_QC_analysis_activity_set',
    'study_set': 'study_set',
}

coll2slot = {v: k for k, v in slot2coll.items()}

biosample_id_tracking = {}


def determine_routing(id_val, routing_table):
    id_prefix = id_val.split(':')[0]
    if id_prefix in routing_table:
        return routing_table[id_prefix]
    else:
        logger.warning(f"Don't know how to route ids with prefix {id_prefix}")


def do_routing(document, id_route, id_val):
    if id_route not in document:
        document[id_route] = []
    if id_val not in document[id_route]:
        document[id_route].append(id_val)
    return document


def concatenate_additional_biosample_identifiers(biosample):
    concatenateds = set()
    id_sources = list(biosample_id_routing.values())
    for id_source in id_sources:
        if id_source in biosample and biosample[id_source]:
            for id_val in biosample[id_source]:
                concatenateds.add(id_val)
    concatenateds = list(concatenateds)
    concatenateds.sort()
    return concatenateds


# todo add lookup of insdc identifiers from gold api?
def route_document_ids(document, routing_table):
    id_route = determine_routing(document['id'], routing_table)
    if id_route:
        document = do_routing(document, id_route, document['id'])
        # todo use real NMDC minted ids not UUIDs!
        document['id'] = f"nmdc:{str(uuid.uuid4())}"
    if "alternative_identifiers" in document and document["alternative_identifiers"]:
        ais = document["alternative_identifiers"]
        ais.sort()
        for index, ai in enumerate(ais):
            id_route = determine_routing(ai, routing_table)
            if id_route:
                document = do_routing(document, id_route, ai)
    concatenateds = concatenate_additional_biosample_identifiers(document)
    if concatenateds:
        logger.info(f"concatenateds: {concatenateds}")
        if "alternative_identifiers" in document:
            starting_alternatives = document["alternative_identifiers"].copy()
            logger.info(f"starting_alternatives: {starting_alternatives}")
            depleted_alternatives = list(set(starting_alternatives) - set(concatenateds))
            depleted_alternatives.sort()
            logger.info(f"depleted_alternatives: {depleted_alternatives}")
            if depleted_alternatives:
                document["alternative_identifiers"] = depleted_alternatives
                logger.info(f"alternative_identifiers: {document['alternative_identifiers']}")
            else:
                del document["alternative_identifiers"]
                logger.warning(f"deleted empty alternative_identifiers")
        else:
            logger.info("no alternative_identifiers to deplete or delete")
    return document


# todo mongo defined in .env

@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--dotenv_file", type=click.Path(exists=True), default="local/.env")
@click.option("--schema_file", type=click.Path(exists=True), default="src/schema/nmdc.yaml")
@click.option("--json_out", default="target/nmdc_data_for_v7.json")
@click.option("--max_collection_bytes", default=10000000000,
              help="Remote collections larger than this will not be loaded in their entirety into local RAM")
@click.option("--last_doc_num", default=100,
              help="The first <last_doc_num> documents from large remote collections will be loaded into local RAM")
@click.option("--migrate_partial", default=True,
              help="Should the first first <last_doc_num> documents from large remote collections be loaded into the destination mongodb? ")
@click.option("--excluded_collection", multiple=True,
              default=[
                  # todo mongodb has a read_QC_analysis_activity_set
                  "read_qc_analysis_activity_set",
                  "read_QC_analysis_activity_set",
              ])
def cli(dotenv_file: str, schema_file: str, max_collection_bytes: int, last_doc_num: int, migrate_partial: bool,
        excluded_collection, json_out: str):

    database_obj = Database()

    logger.info(f"Loading config from {dotenv_file}")

    config = dotenv_values(dotenv_file)

    logger.info(f"Loading schema from {schema_file}")

    nmdc_view = SchemaView(schema_file)

    database_slots = nmdc_view.class_slots("Database")
    database_slots.sort()

    logger.info(pprint.pformat(database_slots))

    remote_client = MongoClient(
        f"mongodb://{config['SOURCE_MONGO_USER']}:{config['SOURCE_MONGO_PASS']}@{config['SOURCE_MONGO_HOST']}:{config['SOURCE_MONGO_PORT']}/?{config['SOURCE_MONGO_AUTH_SUFFIX']}"
    )

    remote_db = remote_client["nmdc"]

    remote_collections = remote_db.list_collection_names()
    remote_collections.sort()

    logger.info(pprint.pformat(remote_collections))

    collections_intersection = [i for i in remote_collections if i.lower() in database_slots]

    collections_intersection = list(set(collections_intersection) - set(excluded_collection))
    collections_intersection.sort()

    logger.info(pprint.pformat(collections_intersection))

    selected_stats = {}
    for collection_name in collections_intersection:
        for_selected_stats = {}

        collection_stats = remote_db.command("collstats", collection_name)

        for_selected_stats["document_count"] = collection_stats["count"]
        for_selected_stats["size_in_bytes"] = collection_stats["size"]
        for_selected_stats["storageSize"] = collection_stats["storageSize"]

        selected_stats[collection_name] = for_selected_stats

    sorted_selected_stats = sorted(selected_stats.items(), key=lambda x: x[1]['size_in_bytes'])

    logger.info("")
    logger.info("Stats about NMDC Database-related collections, sorted by size in bytes:")
    logger.info(pprint.pformat(sorted_selected_stats))
    logger.info("")

    logger.info("starting dumps from source mongodb")

    data_object_file_type_values = set()

    for collection_name in collections_intersection:
        collection_name_lc = collection_name.lower()

        collection_stats = selected_stats[collection_name]

        collection_range = nmdc_view.get_slot(collection_name_lc).range

        range_class = nmdc_view.get_class(collection_range)

        range_slot_names = nmdc_view.class_slots(range_class.name)
        range_slot_names.sort()

        collection = remote_db[collection_name]
        cursor = None
        if collection_stats["size_in_bytes"] > max_collection_bytes:
            logger.warning(
                f"{collection_name_lc}: {collection_stats}, with range {collection_range} is larger than the limit of {max_collection_bytes} bytes")
            if migrate_partial:
                logger.info(f"But will load the first {last_doc_num} documents anyway")
                cursor = collection.find({}).limit(last_doc_num)
        else:
            logger.info(
                f"{collection_name_lc}: {collection_stats}, with range {collection_range} is within the limit of {max_collection_bytes} bytes")
            cursor = collection.find({})
        if cursor:
            for document in cursor:
                del document["_id"]

                if collection_name_lc in drop:
                    for drop_slot in drop[collection_name_lc]:
                        if drop_slot in document:
                            logger.warning(f"dropping {drop_slot} from {collection_name_lc}")
                            del document[drop_slot]

                if range_class.name in name_replacements:
                    # todo Class 'dict' does not define '__getitem__', so the '[]' operator cannot be used on its instances
                    #  but still works
                    for old_name, new_name in name_replacements[range_class.name].items():
                        if old_name in document:
                            document[new_name] = document[old_name]
                            del document[old_name]

                if collection_name_lc == "data_object_set" and "data_object_type" in document:
                    data_object_file_type_values.add(document["data_object_type"])

                if 'id' in document and document['id']:
                    if ":" not in document['id']:
                        logger.error(f"illegal {collection_name_lc} document id: {document['id']}")
                        document['id'] = f"bare:{document['id']}"
                        document['id'] = document['id'].strip()

                    # todo migrations not handled by name_replacements

                # PROBLEM CASE: improperly formatted dates
                # todo remove need for enumerating date fields
                if 'started_at_time' in document:
                    sadt = str(pendulum.parse(document['started_at_time']))
                    document['started_at_time'] = sadt
                if 'ended_at_time' in document:
                    eadt = str(pendulum.parse(document['ended_at_time']))
                    document['ended_at_time'] = eadt

                if collection_name_lc == "data_object_set" and ("id" not in document or not document["id"]):
                    logger.warning(f"no id in document: {document}")
                    document['id'] = f"nmdc:{document['md5_checksum']}"

                if collection_name_lc == "mags_activity_set" and 'mags_list' in document and document['mags_list']:
                    for i in document['mags_list']:
                        if 'num_tRNA' in i:
                            i['num_t_rna'] = i['num_tRNA']
                            del i['num_tRNA']

                if collection_name_lc == "biosample_set":

                    old = document['id']
                    bs_ids_old_new = [document['id']]
                    # reroute identifiers
                    document = route_document_ids(document, biosample_id_routing)
                    bs_ids_old_new.append(document['id'])
                    biosample_id_tracking[old] = document['id']

                    # PROBLEM CASE: depth2 will be removed from the schema
                    # todo soil samples should have a minimum and maximum depth per Montana
                    if "depth2" in document:
                        if "depth" in document:
                            if document['depth']['has_unit'] != document['depth2']['has_unit']:
                                logger.warning(
                                    f"PROBLEM: depth and depth2 have different units: {document['depth']['has_unit']} and {document['depth2']['has_unit']}")
                            else:
                                if 'has_numeric_value' in document['depth2']:
                                    if 'has_maximum_numeric_value' in document['depth']:
                                        if document['depth']['has_maximum_numeric_value'] != document['depth2'][
                                            'has_numeric_value']:
                                            logger.warning(
                                                f"PROBLEM: depth and depth2 have different maximum values: {document['depth']['has_maximum_numeric_value']} and {document['depth2']['has_maximum_numeric_value']}")
                                        else:
                                            del document['depth2']
                                    else:
                                        # todo any assumptions?
                                        document['depth']['has_maximum_numeric_value'] = document['depth2'][
                                            'has_numeric_value']
                                        if "has_minimum_numeric_value" not in document['depth']:
                                            # todo we could constrain this to "soil samples"
                                            #  if there was a clear indicator of a Biosamples having some soil attribute
                                            logger.warning(
                                                f"Biosample {bs_ids_old_new}: inferring depth's min value = numeric value")
                                            document['depth']["has_minimum_numeric_value"] = document['depth'][
                                                "has_numeric_value"]
                                        else:
                                            if document['depth']["has_numeric_value"] != document['depth'][
                                                "has_minimum_numeric_value"]:
                                                logger.warning(
                                                    f"Biosample {bs_ids_old_new}: depth min value != its numeric value !")
                                        del document['depth2']
                        else:
                            logger.warning("depth2 but no depth")
                            # todo assuming the depth2 object has all of these fields
                            document['depth'] = {'has_numeric_value': document['depth']['has_numeric_value'],
                                                 'has_raw_value': document['depth']['has_raw_value'],
                                                 'has_unit': document['depth']['has_unit']}
                            del document['depth2']

                    # PROBLEM CASE: MIXS env triad objects must include a OntologyTerm id
                    #  ideally would also like to include the name/label
                    #  that requirement would be incompatible with the 'omics_processing_set'[]['omics_type']s
                    # https://microbiomedata.github.io/nmdc-schema/ControlledTermValue/
                    # so creating a new ???
                    # todo this does not address ControlledTermValue objects that are not part of the MIXS env triad
                    for triad_slot in ['env_broad_scale', 'env_local_scale', 'env_medium']:
                        if 'term' not in document[triad_slot]:
                            if 'has_raw_value' not in document[triad_slot]:
                                logger.warning(f"  PROBLEM: no has_raw_value in {triad_slot}")
                            else:
                                # todo how much flexibility for the ontology prefix?
                                m = re.search(r'\b(.*:\d+)', document[triad_slot]['has_raw_value'])
                                if m:
                                    # todo check for multiple matches
                                    document[triad_slot]['term'] = {'id': m.group(0)}
                                else:
                                    logger.warning(f"    don't see any term id in {triad_slot}'s has_raw_value")

                    # todo how would other NMDC components handle biosamples with no alternative_identifiers?
                    if "alternative_identifiers" in document and len(document["alternative_identifiers"]) < 1:
                        del document["alternative_identifiers"]

                if collection_name_lc == "omics_processing_set":
                    if 'has_input' in document:
                        loopable = document['has_input'].copy()
                        for i in loopable:
                            logger.info(f"document {document['id']} has_input {i}")
                            if i in biosample_id_tracking:
                                logger.info(f"will replace {i} with {biosample_id_tracking[i]}")
                                document['has_input'].remove(i)
                                document['has_input'].append(biosample_id_tracking[i])
                            else:
                                logger.info(f"no replacement for {i}")
                    else:
                        logger.warning(f"document {document['id']} has no has_input")

                if collection_name_lc == "metatranscriptome_activity_set":
                    tidy_inputs = [i.strip() for i in document['has_input']]
                    document['has_input'] = tidy_inputs
                    if 'part_of' in document:
                        parents = document['part_of']
                        tidy_parents = [i.replace("_", ":") for i in parents]
                        document['part_of'] = tidy_parents

                # if "type" in document:
                #     # an rdf:type object is assigned on instatiation, as long as there is no nmdc type value
                #     # should also remove internal nmdc type values, esp from Biosamples for geolocation values and ???
                #     document["raw_type"] = document["type"]
                #     del document["type"]

                if "@type" in document:
                    # never appears... inserted during instantiation of the document ?
                    logger.warning(f"Document {document['id']} has rdf type {document['@type']}")

                try:
                    jd = json.dumps(document)

                    dynamic_class = getattr(importlib.import_module("python.nmdc"), collection_range)

                    # # todo validation takes place here so don't need to replicate it
                    # could we just load from the dict document?

                    # logger.info(pprint.pformat(document))
                    instance = json_loader.loads(jd, target_class=dynamic_class)

                    rdfout = rdf_dumper.dumps(instance, "jsonld-context/nmdc.context.jsonld")

                    database_obj[collection_name_lc].append(instance)

                except AttributeError:
                    logger.error(f"no class {collection_name_lc} in nmdc_schema.nmdc")
                    continue

            # KeyError: 'read_qc_analysis_activity_set'
            if collection_name_lc in database_obj:
                if len(database_obj[collection_name_lc]) == 0:
                    del database_obj[collection_name_lc]
            else:
                logger.error(f"no collection {collection_name_lc} in database_obj")

    defined_object_type_pvs = nmdc_view.get_enum("file type enum").permissible_values
    defined_object_type_texts = set([pvv.text for pvk, pvv in defined_object_type_pvs.items()])

    unexpected_object_type_values = list(data_object_file_type_values - defined_object_type_texts)

    unexpected_object_type_values.sort()

    # todo how/where to report unexpected_object_type_values?

    destination_client = MongoClient(
        f"mongodb://{config['DEST_MONGO_USER']}:{config['DEST_MONGO_PASS']}@{config['DEST_MONGO_HOST']}:{config['DEST_MONGO_PORT']}/?{config['DEST_MONGO_AUTH_SUFFIX']}"
    )

    destination_db = destination_client[config['DEST_MONGO_DB']]

    destination_collections = destination_db.list_collection_names()

    for i in collections_intersection:
        ilc = i.lower()
        if ilc in excluded_collection:
            logger.warning(f"Skipping {i}")
        else:
            if ilc in destination_collections:
                logger.warning(f"Dropping destination {ilc}")
                collection = destination_db[i]
                collection.drop()
            if ilc in database_obj and database_obj[ilc]:
                collection = destination_db[ilc]
                logger.info(f"Preparing to populate collection {ilc} in destination database")
                vanilla_list = []
                for inner_obj in database_obj[ilc]:
                    io_json_string = json_dumper.dumps(inner_obj)
                    io_dict = json.loads(io_json_string)
                    vanilla_list.append(io_dict)

                insertion = collection.insert_many(vanilla_list)
                logger.info(f"Inserted {len(insertion.inserted_ids)} documents")
            else:
                logger.warning(f"Skipping {i} because it has no documents")

    # logger.info(biosample_id_tracking)

    logger.info("Finished populating destination mongodb")
    logger.info("Starting to dump to JSON file")
    json_dumper.dump(database_obj, json_out)

    logger.info("Finished dump to JSON file")


if __name__ == "__main__":
    cli()
