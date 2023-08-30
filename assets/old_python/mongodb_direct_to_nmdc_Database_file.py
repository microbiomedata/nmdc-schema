import json
import os
import pprint
import re

import click
import click_log
from dotenv import load_dotenv
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from pymongo import MongoClient
from pymongo.errors import OperationFailure

import logging

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

# make this a configuration file, or think of a better way to discover it in real time
#  the uniprot id mapping tool is manual and queued
uniprot_mnemonic_to_id = {
    "ALBU_BOVIN": "P02769",
    "ALBU_HUMAN": "P02768",
    "CTRA_BOVIN": "P00766",
    "K1C10_HUMAN": "P13645",
    "K1C9_HUMAN": "P35527",
    "K22E_HUMAN": "P35908",
    "K2C1_HUMAN": "P04264",
    "TRYP_BOVIN": "P00760",  # todo not sure about this
    "TRYP_PIG": "P00761",
}

intersection_key = "collections that contain instances of nmdc-schema classes"


# todo: in general, don't just change the id, also change referents

# def remove_carriage_returns_and_line_feeds(string):
#     return string.replace('\r', '').replace('\n', '')


def fix_curie(raw_curie):
    if ':' not in raw_curie:
        if raw_curie.count('_') > 0:
            modified_string = raw_curie.replace('_', ':', 1)
        else:
            modified_string = f"generic:{raw_curie}"
    else:
        curie_parts = raw_curie.split(':')
        if len(curie_parts) == 1 or curie_parts[1] == '' or curie_parts[1] == 'None' or curie_parts[1] == 'none':
            # if this is a term id, there may be an appropriate root term
            #   should be handled downstream
            logger.debug(f"Warning: {raw_curie} is essentially prefix-only")
            pass
        modified_string = raw_curie
    # or urlencoding?
    tidied_string = re.sub(r'[^a-zA-Z0-9\-_.,:]', '', modified_string)
    return tidied_string


def access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db):
    # Load MongoDB credentials from .env file
    load_dotenv(env_file)
    logger.info(f"loaded {env_file}")
    mongo_pw = os.getenv('SOURCE_MONGO_PASS')
    mongo_user = os.getenv('SOURCE_MONGO_USER')
    logger.info(f"{mongo_user = }")

    client = MongoClient(mongo_host,
                         port=mongo_port,
                         username=mongo_user,
                         password=mongo_pw,
                         authSource=admin_db,
                         authMechanism='SCRAM-SHA-256',  # todo should be an option
                         directConnection=True
                         )

    db = client[mongo_db_name]

    return db


def get_collection_names(mongo_db):
    collections = mongo_db.list_collection_names()
    return list(collections)


def set_arithmetic(set1, set2, set1_name='set 1 only', set2_name='set 2 only'):
    set1_only = set1 - set2
    set2_only = set2 - set1
    intersection = set1.intersection(set2)
    temp = {
        f"{set1_name} only": set1_only,
        f"{set2_name} only": set2_only,
        intersection_key: intersection
    }
    return temp


def get_synonymous_collection_db_slots(mongo_db, schema_view: SchemaView, class_name='Database'):
    class_slots = schema_view.class_induced_slots(class_name)
    class_slot_names = [s.name for s in class_slots]
    class_slot_names.sort()

    # incomplete attempt to fiter out views
    collections = [coll['name']
                   for coll in mongo_db.list_collections() if 'viewOn' not in coll]

    collections.sort()

    # successful
    filtered_collections = []
    for collection in collections:
        try:
            # Check if the collection is a view
            if mongo_db[collection].count_documents({}) > 0:
                logger.info(
                    f"Collection {collection} is accessible to this user and is not a view.")
                filtered_collections.append(collection)
            else:
                logger.info(f"Collection {collection} is a view.")
        except OperationFailure as e:
            if e.code == 13:  # Unauthorized error code
                logger.info(
                    f"Collection {collection} is unauthorized for this user.")
                continue
            raise e

    synonymous_collection_names = set_arithmetic(set(class_slot_names), set(filtered_collections), set1_name='schema',
                                                 set2_name='mongo')

    return synonymous_collection_names


def get_doc_list(mongodb, collection_name, max_docs_per_coll):
    collection = mongodb[collection_name]

    if collection is None:
        logger.info(f"Could not find collection {collection_name}")

    documents = collection.find().limit(max_docs_per_coll)
    doc_list = list(documents)

    prob_key = "_id"
    for doc in doc_list:
        if prob_key in doc:
            del doc[prob_key]

    return doc_list


def get_collection_stats(mongo_db, collection_list):
    selected_stats = {}
    for collection_name in collection_list:
        for_selected_stats = {}

        collection_stats = mongo_db.command("collstats", collection_name)

        for_selected_stats["document_count"] = collection_stats["count"]
        for_selected_stats["size_in_bytes"] = collection_stats["size"]
        for_selected_stats["storageSize"] = collection_stats["storageSize"]

        selected_stats[collection_name] = for_selected_stats

    return selected_stats


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option('--env-file', type=click.Path(), default='local/.env', help='Path to .env file')
@click.option('--mongo-db-name', default="nmdc", help='MongoDB database name')
@click.option('--selected-collections', multiple=True, help='MongoDB collection name')
@click.option('--root-class', default="Database", help='Schema class that corresponds to a Mongo Database')
@click.option('--mongo-host', default="localhost", help='MongoDB host name/address')
@click.option('--mongo-port', default=27777, help='MongoDB port')
@click.option('--admin-db', default="admin", help='MongoDB authentication source')
# @click.option('--output-json', type=click.Path(), default='local/selected_mongodb_contents.json',
#               help="Output directory. Exported file's name will be based on the collection name.")
@click.option('--output-json', type=click.Path(), help="Output file.")
@click.option('--schema-file', type=click.Path(), default='src/schema/nmdc.yaml',
              help='Path to root YAML file in the nmdc-schema')
@click.option('--max-docs-per-coll', default=100_000, help='Maximum number of documents to retrieve per collection')
@click.option('--non-nmdc-id-fixes/--no-non-nmdc-id-fixes', default=True,
              help="Apply repairs that don't alter ids for nmdc-schema instances")
@click.option('--curie-fix/--no-curie-fix', default=False,
              help='Remove end-of-line characters from nmdc-schema ids')
def export_to_yaml(selected_collections, env_file, mongo_db_name, mongo_host, mongo_port, admin_db, output_json,
                   schema_file, root_class, max_docs_per_coll, non_nmdc_id_fixes, curie_fix):
    db = access_database(env_file, mongo_db_name,
                         mongo_host, mongo_port, admin_db)

    database = {}

    # no collections selected, so just summarize all of them
    if len(selected_collections) == 0:
        # just export all of them?
        # use a limit on document_count or size_in_bytes?
        # for now, just report the all (schema-relevant?) collection stats

        nmdc_view = SchemaView(schema_file)

        collections_to_check = get_synonymous_collection_db_slots(
            db, nmdc_view, root_class)

        logger.info(pprint.pformat(collections_to_check))

        mongo_collections = list(collections_to_check[intersection_key]) + list(collections_to_check['mongo only'])

        mongo_collections.sort()

        collection_stats = get_collection_stats(db, mongo_collections)

        # # collection_stats = sorted(collection_stats.items(), key=lambda x: x[1]['size_in_bytes'])

        for coll_stat_k, coll_stat_v in collection_stats.items():
            if coll_stat_k in collections_to_check[intersection_key]:
                logger.info(f"Collection {coll_stat_k} is defined in the schema.")

                logger.info(pprint.pformat(coll_stat_v))
            else:
                logger.debug(
                    f"Collection {coll_stat_k} is not defined in the schema.")
                # pprint.pprint(coll_stat_v)

    # now start exporting
    for selected_collection in selected_collections:
        # todo will need some error handling here
        collection_stats = get_collection_stats(db, [selected_collection])
        logger.info(
            f"Exporting collection {selected_collection}, with the following stats: {collection_stats}")
        doc_list = get_doc_list(db, selected_collection, max_docs_per_coll)

        # # # # REPAIRS # # # #

        # extract [] enclosed portion of  'samp_taxon_id': {'has_raw_value': 'lake water metagenome [NCBITaxon:1647806]'},
        #   and assign to samp_taxon_id.term.id
        if non_nmdc_id_fixes and selected_collection == 'biosample_set':
            for doc in doc_list:

                # REPAIR: extract Biosample samp_taxon_id term id from raw value if necessary
                #   these are external terms and don't require referential integrity withing the database
                taxon_slot = 'samp_taxon_id'
                if taxon_slot in doc and 'has_raw_value' in doc[taxon_slot]:
                    raw_value = doc[taxon_slot]['has_raw_value']
                    result = re.findall(r'\[(.*?)\]', raw_value)

                    if result:
                        extracted_text = result[0]
                        if 'term' not in doc[taxon_slot]:
                            logger.info(
                                f"for {doc['id']}, setting the term id of {taxon_slot} to {extracted_text}")
                            doc[taxon_slot]['term'] = {'id': extracted_text}
                        else:
                            if 'id' not in doc[taxon_slot]['term']:
                                logger.info(
                                    f"for {doc['id']}, setting the term id of {taxon_slot} to {extracted_text}")
                                doc[taxon_slot]['term'] = {
                                    'id': extracted_text}
                            else:
                                if extracted_text != doc[taxon_slot]['term']['id']:
                                    logger.info(
                                        f"for {doc['id']}, replacing the previous {taxon_slot} term id of {doc[taxon_slot]['term']['id']} with {extracted_text}")
                                    doc[taxon_slot]['term']['id'] = extracted_text
                    else:
                        # if there was a value in the taxon slot, wwe should report it
                        logger.debug(
                            f"for {doc['id']}, no term id found in {taxon_slot}")

                # REPAIR: extract Biosample host_taxid term id from raw value if necessary
                #   not using fix_curie
                #   these are external terms and don't require referential integrity withing the database
                taxon_slot = 'host_taxid'
                if taxon_slot in doc and 'has_raw_value' in doc[taxon_slot] and doc[taxon_slot]['has_raw_value'] == str(
                        int(
                            doc[taxon_slot]['has_raw_value'])):
                    extracted_text = doc[taxon_slot]['has_raw_value']
                    replacement_text = f"NCBITaxon:{extracted_text}"
                    if 'term' not in doc[taxon_slot]:
                        logger.info(
                            f"for {doc['id']}, setting the term id of {taxon_slot} to {replacement_text}")
                        doc[taxon_slot]['term'] = {'id': replacement_text}
                    else:
                        if 'id' not in doc[taxon_slot]['term']:
                            logger.info(
                                f"for {doc['id']}, setting the term id of {taxon_slot} to {replacement_text}")
                            doc[taxon_slot]['term'] = {'id': replacement_text}
                        else:
                            if replacement_text != doc[taxon_slot]['term']['id']:
                                logger.info(
                                    f"for {doc['id']}, replacing the previous {taxon_slot} term id of {doc[taxon_slot]['term']['id']} with {extracted_text}")
                                doc[taxon_slot]['term']['id'] = replacement_text
                else:
                    # if there was a value in the taxon slot, wwe should logger.info it out
                    logger.debug(
                        f"for {doc['id']}, no term id found in {taxon_slot}")

                # REPAIR: Biosample 'env_broad_scale', 'env_local_scale' and 'env_medium' ids must be id only,
                #   not label + value, like you would find in has_raw_value
                #   not using fix_curie
                #   these are external terms and don't require referential integrity withing the database
                # todo repetitive code
                for slot in ['env_broad_scale', 'env_local_scale', 'env_medium']:
                    # logger.info(f"checking {slot} in {doc['id']}")
                    if slot in doc and 'term' in doc[slot] and 'id' in doc[slot]['term']:
                        raw_value = doc[slot]['term']['id']
                        # logger.info(f"raw_value is {raw_value}")
                        # case 1: raw_value includes a label, and the id is enclosed in square brackets
                        result = re.findall(r'\[(.*?)\]', raw_value)
                        if result:
                            extracted_text = result[0]
                        else:
                            extracted_text = raw_value
                        # case 2: the raw text is delimited with an underscore instead of a colon
                        if "_" in extracted_text:
                            colonified = ':'.join(extracted_text.split("_"))
                        else:
                            colonified = extracted_text
                    if slot in doc:
                        if 'term' in doc[slot]:
                            if 'id' in doc[slot]['term']:
                                # carefully check these replacements. maybe we want to keep the original ids
                                if colonified != doc[slot]['term']['id']:
                                    logger.info(
                                        f"for {doc['id']}, replacing {slot} term id of {doc[slot]['term']['id']} with {colonified}")
                                    doc[slot]['term']['id'] = colonified
                            else:
                                logger.info(
                                    f"for {doc['id']}, setting {slot} term id to {colonified}")
                                doc[slot]['term']['id'] = colonified
                        else:
                            logger.info(
                                f"for {doc['id']}, setting {slot} term id to {colonified}")
                            doc[slot]['term'] = {'id': colonified}
                    else:
                        logger.info(
                            f"checking {doc['id']} does not have a {slot}")

                # REPAIR: Biosample growth_facil.term.id: must be an id, not a string like 'field'
                #   not using fix_curie
                #   these are external terms and don't require referential integrity withing the database
                if 'growth_facil' in doc and 'term' in doc['growth_facil'] and 'id' in doc['growth_facil']['term']:
                    raw_value = doc['growth_facil']['term']['id']
                    if raw_value == 'field':
                        logger.info(
                            f"for {doc['id']}, replacing growth_facil term id of {raw_value} with ENVO:01000352")
                        doc['growth_facil'] = {
                            'has_raw_value': 'field',
                            'term': {
                                "name": "field",
                                'id': 'ENVO:01000352'

                            }
                        }

        # REPAIR: Biosample eliminate None value assertions for any slot from the root of any document in any collection
        #   not using fix_curie
        if non_nmdc_id_fixes:
            slots_to_del_if_none = [
                'asm_score',
                'binned_contig_num',
                'contig_bp',
                'contigs',
                'ctg_l50',
                'ctg_l90',
                'ctg_logsum',
                'ctg_max',
                'ctg_n50',
                'ctg_n90',
                'ctg_powsum',
                'gap_pct',
                'gc_avg',
                'gc_std',
                'input_base_count',
                'input_contig_num',
                'input_read_bases',
                'input_read_count',
                'low_depth_contig_num',
                'num_aligned_reads',
                'num_input_reads',
                'output_base_count',
                'output_read_bases',
                'output_read_count',
                'scaf_bp',
                'scaf_l50',
                'scaf_l90',
                'scaf_l_gt50k',
                'scaf_logsum',
                'scaf_max',
                'scaf_n50',
                'scaf_n90',
                'scaf_n_gt50k',
                'scaf_pct_gt50k',
                'scaf_powsum',
                'scaffolds',
                'too_short_contig_num',
                'unbinned_contig_num',
                "insdc_assembly_identifiers",
                "compression_type",
                "was_generated_by",
            ]
            for doc in doc_list:
                for slot in slots_to_del_if_none:
                    if slot in doc:
                        if not doc[slot]:
                            logger.debug(
                                f"for {doc['id']}, deleting {slot} because it is None")
                            del doc[slot]

        # REPAIR: Biosample eliminate None value assertions for any slot from the root of any document in any collection
        #  fix_curie() is a more aggressive fix than remove_carriage_returns_and_line_feeds()
        if curie_fix:
            for doc in doc_list:
                problem_slots = [
                    'has_input',
                    'has_output',
                    'id',
                    'part_of',
                ]
                for slot in problem_slots:
                    if slot in doc and type(doc[slot]) == list:
                        slotvals = doc[slot]
                        replacements = []
                        for raw_slotval in slotvals:
                            fixed_slotval = fix_curie(raw_slotval)
                            if fixed_slotval != raw_slotval:
                                logger.info(
                                    f"{selected_collection} {doc['id']} {slot} [{raw_slotval}] -> {fixed_slotval}")
                            replacements.append(fixed_slotval)
                        doc[slot] = replacements
                    elif slot in doc:
                        raw_slotval = doc[slot]
                        fixed_slotval = fix_curie(raw_slotval)
                        if raw_slotval != fixed_slotval:
                            logger.info(
                                f"{selected_collection} {doc['id']} {slot} {raw_slotval} -> {fixed_slotval}")
                        doc[slot] = fixed_slotval

        # REPAIR: metabolite quantification alternative identifiers must use prefix:local CURIEs
        #   these are external terms and don't require referential integrity withing the database
        # why are the objects of nmdc:alternative_identifiers typed like "cas:3685-26-5"^^xsd:anyURI ?
        if non_nmdc_id_fixes and selected_collection == 'metabolomics_analysis_activity_set':
            for doc in doc_list:
                id_val = doc['id']
                if 'has_metabolite_quantifications' in doc:
                    accepted_mqs = []
                    for mq in doc['has_metabolite_quantifications']:
                        if 'alternative_identifiers' in mq:
                            raw_ais = mq['alternative_identifiers']
                            accepted_ais = []
                            for ai in raw_ais:
                                alt_id_parts = ai.split(":")
                                if alt_id_parts[1] in ['', 'None']:
                                    logger.debug(
                                        f"{selected_collection} {id_val} has_metabolite_quantifications.alternative_identifiers has un-redeemable metabolite identifier: [{ai}]")
                                else:
                                    # not even using fix_curie yet
                                    raw_slotval = ai
                                    fixed_slotval = fix_curie(raw_slotval)
                                    if raw_slotval != fixed_slotval:
                                        logger.info(
                                            f"{selected_collection} {id_val} has_metabolite_quantifications.alternative_identifiers [{raw_slotval}] -> {fixed_slotval}")
                                    accepted_ais.append(fixed_slotval)
                            mq['alternative_identifiers'] = accepted_ais
                        accepted_mqs.append(mq)
                    doc['has_metabolite_quantifications'] = accepted_mqs

        # REPAIR: slots that refer to instances of another class,
        #   even if that class is never instantiated, must use prefix:local CURIEs
        def convert_contam_string_to_curie(value):
            # if ":" not in value and value.startswith("Contaminant"):
            parts = value.split("_")
            if len(parts) == 3:  # Change to 3 if you want exactly three parts
                local_mnenomic_id = '_'.join(parts[1:3])
                local_unprot_id = uniprot_mnemonic_to_id[local_mnenomic_id]
                curie = "UniProtKB:" + local_unprot_id
                return curie
            return None

        if non_nmdc_id_fixes and selected_collection == 'metaproteomics_analysis_activity_set':
            for doc in doc_list:
                if 'has_peptide_quantifications' in doc:
                    repaired_pqs = []
                    for pq in doc['has_peptide_quantifications']:
                        if 'all_proteins' in pq:
                            repaired_aps = []
                            for ap in pq['all_proteins']:
                                if ":" not in ap:
                                    if ap.startswith("Contaminant_"):
                                        as_up_contam = convert_contam_string_to_curie(
                                            ap)
                                        # log the original collection, id, and value plus the repaired value
                                        if as_up_contam != ap:
                                            logger.info(
                                                f"{selected_collection} {doc['id']} has_peptide_quantifications.all_proteins [{ap}] -> {as_up_contam}")
                                        repaired_aps.append(as_up_contam)
                                    else:
                                        repaired_aps.append(ap)
                                pq['all_proteins'] = repaired_aps
                        if 'best_protein' in pq:
                            bp = pq['best_protein']
                            if ":" not in bp:
                                if bp.startswith("Contaminant_"):
                                    as_up_contam = convert_contam_string_to_curie(
                                        bp)
                                    pq['best_protein'] = as_up_contam
                                    logger.info(
                                        f"{selected_collection} {doc['id']} has_peptide_quantifications.best_proteins {bp} -> {as_up_contam}")
                            else:
                                pq['best_protein'] = bp
                        repaired_pqs.append(pq)
                    doc['has_peptide_quantifications'] = repaired_pqs

        # MAM most of these comments are about poor decisions I made in the overall design of this script
        # everything after the first `if` this should be a function
        # the first `if` constrains the repair to one collection form MongoDB,
        #   which corresponds to one clas from the schema
        if non_nmdc_id_fixes and selected_collection == 'study_set':

            # # why does this have to be recreated here?
            # nmdc_view = SchemaView(schema_file)
            #
            # # get range and multivalued from slot as used in class
            # # from nmdc_view
            # current_slot = nmdc_view.get_slot(selected_collection)
            # current_range = current_slot.range
            # print(current_range)

            # next we iterate over all documents in the collection ie all instances of the class
            for doc in doc_list:
                # doi_slot = 'doi'
                # making that more generalizable
                target_slot = 'doi'

                # this could also be a separate function

                # we want to extract the legacy `doi` values and assert them in one of the new `dois` subproperties
                # matching the expectation of that new slot

                # how will we know which of the `dois` subproperties it should go into?
                # here we are assuming all legacy Study.dois are award_dois
                # how could we confirm that?
                destination_slot = 'award_dois'

                # # do not leave this slow step in production
                # # it does illustrate the required destination format
                # cis = nmdc_view.induced_slot(destination_slot, current_range)

                # print(f"{cis.multivalued = }")
                # print(f"{cis.pattern = }")
                # print(f"{cis.range = }")

                # cis.multivalued = True
                # cis.pattern = '^doi:10.\\d{2,9}/.*$'
                # cis.range = 'uriorcurie'

                if target_slot in doc and 'has_raw_value' in doc[target_slot]:
                    source_data_structure = doc[target_slot]['has_raw_value']

                    # print(type(source_data_structure)) # all appear to be strings
                    logger.info(f"{source_data_structure = }")

                    # https://doi.org/10.25585/1487763
                    # https://doi.org/10.25585/1488099
                    # https://doi.org/10.25585/1487765
                    # https://doi.org/10.25585/1488160
                    # https://doi.org/10.46936/10.25585/60001061
                    # https://doi.org/10.46936/10.25585/60001198
                    # https://doi.org/10.46936/10.25585/60001289
                    # https://doi.org/10.25585/1488224
                    # https://doi.org/10.25585/1488096
                    # https://doi.org/10.46936/10.25585/60000762
                    # https://doi.org/10.46936/10.25585/60000017
                    # https://dx.doi.org/10.46936/intm.proj.2021.60141/60000423

                    # we want to extract everything after the following pattern
                    # and add the /10. prefix back on

                    pattern = r'^https?:\/\/[a-zA-Z\.]+\/10\.'
                    match = re.search(pattern, source_data_structure)
                    if match:
                        start_index = match.end()
                        as_curie = f"doi:10.{source_data_structure[start_index:]}"
                        logger.info(f"{as_curie = }")

                        # the schema now expects `dois` subproperties to be multivalues,
                        #   so assert it as a list of length one
                        doc[destination_slot] = [as_curie]

                    else:
                        logger.warning(
                            "doi URL not found in {source_data_structure} from Study {doc['id']}")

                    del doc[target_slot]

        database[selected_collection] = doc_list

    # # save documents to JSON file with pretty formatting/indentation
    # # avoids complaints about 64-bit numbers in YAML?
    # output_json = output_yaml.replace(".yaml", ".json")
    if output_json:
        with open(output_json, 'w') as f:
            json.dump(database, f, indent=2)


if __name__ == '__main__':
    export_to_yaml()
