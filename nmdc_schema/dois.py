import yaml
import pprint
import pandas as pd
from doi_dicts import award_doi_prov, new_award_dois, award_move_to_data


def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


def fix_massive(study):
    """Change the one massive_study_identifiers value to a doi and move under new associated_dois slot"""

    mass_id = 'MASSIVE:MSV000090886'
    mass_doi = 'doi:10.25345/C58K7520G'
    study.setdefault('associated_dois', []).extend({'doi': mass_doi, 'doi_category': 'dataset_doi', 'doi_provider': 'massive'}
                                                   for id in study.get('massive_study_identifiers', []) if id == mass_id)

    # remove the massive_study_identifiers slot if the id matches the one to be removed in associated_dois slot
    for doi_group in study['associated_dois']:
        if doi_group['doi'] == mass_doi:
            study.pop('massive_study_identifiers', None)


def fix_ess_dive(study):
    """Move ess_dive_datasets values to associated_dois slot"""

    study.setdefault('associated_dois', []).extend(
        {'doi': dataset_doi, 'doi_category': 'dataset_doi', 'doi_provider': 'ess_dive'}
        for dataset_doi in study.get('ess_dive_datasets', [])
    )


def process_doi(study, doi_list, doi_category):
    id_value = study['id']
    for doi_updates in doi_list:
        if id_value == doi_updates['id']:
            new_doi = {
                'doi': doi_updates['doi'],
                'doi_category': doi_category,
                'doi_provider': doi_updates['doi_prov']
            }
            study.setdefault('associated_dois', []).append(new_doi)

def fix_award_dois(study):
    process_doi(study, award_move_to_data, 'dataset_doi')
    process_doi(study, new_award_dois, 'award_doi')
    process_doi(study, award_doi_prov, 'award_doi')


def fix_pub_dois(study):
    """Move publication_dois values to new associated_dois slot"""
  
    study.setdefault('associated_dois', []).extend(
        {'doi': pub_doi, 'doi_category': 'publication_doi'}
        for pub_doi in study.get('publication_dois', [])
    )

def remove_slots(study):
    """Remove slots that are no longer needed because their values have been moved to the associated_dois slot"""

    removal_slots = ['publication_dois', 'dataset_dois',
                     'award_dois', 'ess_dive_datasets', 'massive_study_identifiers']
    
    # Get dois from associated_dois
    associated_dois = {entry['doi'] for entry in study.get('associated_dois', [])}
    
    # Remove the old dois from the old doi slots
    for slot_name in removal_slots:
        study[slot_name] = [doi for doi in study.get(slot_name, []) if doi not in associated_dois]
        
        # Remove old doi slots if values are empty
        if not study[slot_name]:
            del study[slot_name]

def schema_changes(study_collection):
    # will need to remove this for loop when adding as it is in the py script as "for document in tdv"
    for study in study_collection['study_set']:

        fix_massive(study)
        fix_ess_dive(study)
        fix_award_dois(study)
        fix_pub_dois(study)
        remove_slots(study)

    with open('final_yaml.yaml', 'w') as f:
        yaml.dump(study_collection, f)
    pprint.pprint(study_collection)

data = load_yaml_file('all_studies.yaml')
schema_changes(data)
