import json
import os
import pprint
import re

import yaml
import click
from linkml_runtime import SchemaView
from pymongo import MongoClient
from dotenv import load_dotenv
import urllib.parse

from pymongo.errors import OperationFailure


def access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db):
    # Load MongoDB credentials from .env file
    load_dotenv(env_file)
    print(f"loaded {env_file}")
    mongo_pw = os.getenv('SOURCE_MONGO_PASS')
    mongo_user = os.getenv('SOURCE_MONGO_USER')
    print(f"{mongo_user = }")

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
        set1_name: set1_only,
        set2_name: set2_only,
        'intersection': intersection
    }
    return temp


def get_synonymous_collection_db_slots(mongo_db, schema_view: SchemaView, class_name='Database'):
    class_slots = schema_view.class_induced_slots(class_name)
    class_slot_names = [s.name for s in class_slots]
    class_slot_names.sort()

    # incomplete attempt to fiter out views
    collections = [coll['name'] for coll in mongo_db.list_collections() if 'viewOn' not in coll]

    collections.sort()

    # successful
    filtered_collections = []
    for collection in collections:
        try:
            # Check if the collection is a view
            if mongo_db[collection].count_documents({}) > 0:
                print(f"Collection {collection} is accessible to this user and is not a view.")
                filtered_collections.append(collection)
            else:
                print(f"Collection {collection} is a view.")
        except OperationFailure as e:
            if e.code == 13:  # Unauthorized error code
                print(f"Collection {collection} is unauthorized for this user.")
                continue
            raise e

    synonymous_collection_names = set_arithmetic(set(class_slot_names), set(filtered_collections), set1_name='schema',
                                                 set2_name='mongo')

    return synonymous_collection_names


def get_doc_list(mongodb, collection_name):
    # print(collection_name)

    collection = mongodb[collection_name]

    if collection is None:
        print(f"Could not find collection {collection_name}")

    documents = collection.find()
    doc_list = list(documents)

    prob_key = "_id"
    for doc in doc_list:
        if prob_key in doc:
            del doc[prob_key]

    return doc_list


def get_collection_stats(mongo_db, collection_list):
    selected_stats = {}
    for collection_name in collection_list:
        print(f"retrieving stats for collection {collection_name}")

        for_selected_stats = {}

        collection_stats = mongo_db.command("collstats", collection_name)

        for_selected_stats["document_count"] = collection_stats["count"]
        for_selected_stats["size_in_bytes"] = collection_stats["size"]
        for_selected_stats["storageSize"] = collection_stats["storageSize"]

        selected_stats[collection_name] = for_selected_stats

    return selected_stats


@click.command()
@click.option('--env-file', type=click.Path(), default='local/.env', help='Path to .env file')
@click.option('--mongo-db-name', default="nmdc", help='MongoDB database name')
@click.option('--selected-collections', multiple=True, help='MongoDB collection name')
@click.option('--root-class', default="Database", help='Schema class that corresponds to a Mongo Database')
@click.option('--mongo-host', default="localhost", help='MongoDB host name/address')
@click.option('--mongo-port', default=27777, help='MongoDB port')
@click.option('--admin-db', default="admin", help='MongoDB authentication source')
@click.option('--output-yaml', type=click.Path(), default='local/selected_mongodb_contents.yaml',
              help="Output directory. Exported file's name will be based on the collection name.")
@click.option('--schema-file', type=click.Path(), default='src/schema/nmdc.yaml',
              help='Path to root YAML file in the nmdc-schema')
def export_to_yaml(selected_collections, env_file, mongo_db_name, mongo_host, mongo_port, admin_db, output_yaml,
                   schema_file, root_class):
    apply_latest_repairs = True

    db = access_database(env_file, mongo_db_name, mongo_host, mongo_port, admin_db)

    database = {}

    if len(selected_collections) == 0:
        # just export all of them?
        # use a limit on document_count or size_in_bytes?

        nmdc_view = SchemaView(schema_file)

        collections_to_check = get_synonymous_collection_db_slots(db, nmdc_view, root_class)

        pprint.pprint(collections_to_check)

        mongo_collections = list(collections_to_check['intersection']) + list(collections_to_check['mongo'])

        mongo_collections.sort()

        collection_stats = get_collection_stats(db, mongo_collections)

        # # collection_stats = sorted(collection_stats.items(), key=lambda x: x[1]['size_in_bytes'])

        for coll_stat_k, coll_stat_v in collection_stats.items():
            if coll_stat_k in collections_to_check['intersection']:
                print(f"Collection {coll_stat_k} is defined in the schema.")
                pprint.pprint(coll_stat_v)
            # else:
            #     print(f"Collection {coll_stat_k} is not defined in the schema.")
            #     pprint.pprint(coll_stat_v)

    for selected_collection in selected_collections:
        print(f"Exporting collection {selected_collection}")
        # todo will need some error handling here
        collection_stats = get_collection_stats(db, [selected_collection])

        print(f"You requested an export of collection {selected_collection}.")
        print(f"Its collection stats are {collection_stats}")
        doc_list = get_doc_list(db, selected_collection)

        # # # #

        # extract [] enclosed portion of  'samp_taxon_id': {'has_raw_value': 'lake water metagenome [NCBITaxon:1647806]'},
        #   and assign to samp_taxon_id.term.id
        if apply_latest_repairs and selected_collection == 'biosample_set':
            for doc in doc_list:

                taxon_slot = 'samp_taxon_id'
                if taxon_slot in doc and 'has_raw_value' in doc[taxon_slot]:
                    raw_value = doc[taxon_slot]['has_raw_value']
                    result = re.findall(r'\[(.*?)\]', raw_value)

                    if result:
                        extracted_text = result[0]
                        if 'term' not in doc[taxon_slot]:
                            doc[taxon_slot]['term'] = {'id': extracted_text}
                        else:
                            if 'id' not in doc[taxon_slot]['term']:
                                doc[taxon_slot]['term'] = {'id': extracted_text}
                            else:
                                doc[taxon_slot]['term']['id'] = extracted_text

                taxon_slot = 'host_taxid'
                if taxon_slot in doc and 'has_raw_value' in doc[taxon_slot] and doc[taxon_slot]['has_raw_value'] == str(
                        int(
                            doc[taxon_slot]['has_raw_value'])):
                    extracted_text = doc[taxon_slot]['has_raw_value']
                    replacement_text = f"NCBITaxon:{extracted_text}"
                    if 'term' not in doc[taxon_slot]:
                        doc[taxon_slot]['term'] = {'id': replacement_text}
                    else:
                        if 'id' not in doc[taxon_slot]['term']:
                            doc[taxon_slot]['term'] = {'id': replacement_text}
                        else:
                            doc[taxon_slot]['term']['id'] = replacement_text

                # some mixs triad values have label + id term.ids
                # todo repetitive code
                for slot in ['env_broad_scale', 'env_local_scale', 'env_medium']:
                    if slot in doc and 'term' in doc[slot] and 'id' in doc[slot]['term']:
                        raw_value = doc[slot]['term']['id']
                        result = re.findall(r'\[(.*?)\]', raw_value)
                        if result:
                            extracted_text = result[0]
                            doc[slot]['term']['id'] = extracted_text
                        # some mixs triad term.id values are prefix_local instead of prefix:local
                        if "_" in doc[slot]['term']['id']:
                            extracted_text = ':'.join(doc[slot]['term']['id'].split("_"))
                            doc[slot]['term']['id'] = extracted_text

                # growth_facil.term.id: 'field'
                if 'growth_facil' in doc and 'term' in doc['growth_facil'] and 'id' in doc['growth_facil']['term']:
                    raw_value = doc['growth_facil']['term']['id']
                    if raw_value == 'field':
                        doc['growth_facil'] = {
                            'has_raw_value': 'field',
                            'term': {
                                "name": "field",
                                'id': 'ENVO:01000352'

                            }
                        }
        # eliminate None values
        if apply_latest_repairs:
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
                            del doc[slot]

        #  part ofs require prefix:local CURIEs
        if apply_latest_repairs:
            problem_slots = ['part_of']
            for doc in doc_list:
                for slot in problem_slots:
                    if slot in doc:
                        slotvals = doc[slot]
                        replacements = []
                        for slotval in slotvals:
                            if slotval.count('_') == 1 and ':' not in slotval:
                                modified_string = slotval.replace('_', ':')
                            else:
                                modified_string = slotval
                            replacements.append(modified_string)
                        doc[slot] = replacements

        # ids must be curies
        if apply_latest_repairs:
            problem_slots = ['id']
            for doc in doc_list:
                for slot in problem_slots:
                    if slot in doc:
                        slotval = doc[slot]
                        if ":" not in slotval:
                            doc[slot] = f"generic:{slotval}"

        # if apply_latest_repairs and selected_collection == 'metabolomics_analysis_activity_set':
        #     for doc in doc_list:
        #         id_val = doc['id']
        #         if 'has_metabolite_quantifications' in doc:
        #             metabolite_quantifications = doc['has_metabolite_quantifications']
        #             if type(metabolite_quantifications) != list:
        #                 print(type(metabolite_quantifications))
        #             else:
        #                 for metabolite_quantification in metabolite_quantifications:
        #                     if "alternative_identifiers" in metabolite_quantification:
        #                         for alternative_identifier in metabolite_quantification["alternative_identifiers"]:
        #                             alt_id_parts = alternative_identifier.split(":")
        #                             if alt_id_parts[1] in ['', 'None']:
        #                                 print(
        #                                     f"attempting to remove illegal metabolite_quantifications alternative identifier local portion '{alt_id_parts[1]}' in {id_val}'s {alternative_identifier}")
        #                                 # metabolite_quantification["alternative_identifiers"].remove(
        #                                 #     alternative_identifier)

        database[selected_collection] = doc_list

    # # Save documents to YAML file
    # with open(output_yaml, 'w') as f:
    #     yaml.dump(database, f)

    # save documents to JSON file with pretty printing/indentation
    output_json = output_yaml.replace(".yaml", ".json")
    with open(output_json, 'w') as f:
        json.dump(database, f, indent=2)


if __name__ == '__main__':
    export_to_yaml()
