from .migrator_base import MigratorBase
from .helpers import load_yaml_asset


class Migrator_from_8_1_to_9_0(MigratorBase):
    """previously: Migrates data from schema 8.1.0 to 9.0.0"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.fix_award_dois, self.fix_pub_dois,
                       self.fix_massive, self.fix_ess_dive, self.remove_doi_slots],
        )

    def process_doi(self, study: dict, doi_list: list, doi_category: str):
        id_value = study['id']
        for doi_updates in doi_list:
            if id_value == doi_updates['id']:
                new_doi = {
                    'doi_value': doi_updates['doi'],
                    'doi_category': doi_category,
                    'doi_provider': doi_updates['doi_prov']
                }
                study.setdefault('associated_dois', []).append(new_doi)

        return study

    def fix_award_dois(self, study: dict):
        """Moves current DOIs in the award_dois slot to the new associated_dois slot.
         It also changes some DOIs that were incorrectly labeled as award to dataset DOIs.
         It also adds three new award DOIs from JGI"""

        study_doi_data = load_yaml_asset('migrator_from_8_1_to_9_0/study_dois_changes.yaml')

        self.process_doi(
            study, study_doi_data['award_move_to_data'], 'dataset_doi')
        self.process_doi(study, study_doi_data['new_award_dois'], 'award_doi')
        self.process_doi(study, study_doi_data['award_doi_prov'], 'award_doi')

        return study

    def fix_pub_dois(self, study: dict):
        """Move publication_dois values to new associated_dois slot"""

        study.setdefault('associated_dois', []).extend(
            {'doi_value': pub_doi, 'doi_category': 'publication_doi'}
            for pub_doi in study.get('publication_dois', [])
        )

        return study

    def fix_massive(self, study: dict):
        """Change the one massive_study_identifiers value to a doi and move under new associated_dois slot"""

        mass_id = 'MASSIVE:MSV000090886'
        mass_doi = 'doi:10.25345/C58K7520G'
        study.setdefault('associated_dois', []).extend(
            {'doi_value': mass_doi, 'doi_category': 'dataset_doi', 'doi_provider': 'massive'}
            for id in study.get('massive_study_identifiers', []) if id == mass_id)

        # remove the massive_study_identifiers slot if the id matches the one to be removed in associated_dois slot
        for doi_group in study['associated_dois']:
            if doi_group['doi_value'] == mass_doi:
                study.pop('massive_study_identifiers', None)

        return study

    def fix_ess_dive(self, study: dict):
        """Move ess_dive_datasets values to associated_dois slot"""

        study.setdefault('associated_dois', []).extend(
            {'doi_value': dataset_doi, 'doi_category': 'dataset_doi',
             'doi_provider': 'ess_dive'}
            for dataset_doi in study.get('ess_dive_datasets', []))

        return study

    def remove_doi_slots(self, study: dict):
        """Remove slots that are no longer needed because their values have been moved to the associated_dois slot"""

        removal_slots = ['publication_dois', 'dataset_dois',
                         'award_dois', 'ess_dive_datasets', 'massive_study_identifiers']

        # Get dois from associated_dois
        associated_dois = [entry['doi_value']
                           for entry in study.get('associated_dois', [])]

        # Remove the old dois from the old doi slots
        for slot_name in removal_slots:
            study[slot_name] = [doi for doi in study.get(
                slot_name, []) if doi not in associated_dois]

            # Remove old doi slots if values are empty
            if not study[slot_name]:
                del study[slot_name]
            else:
                self.logger.error(
                    f'ERROR: Unexpected value in {slot_name} of {study["id"]} skipping slot deletion')

        # Remove associated_dois if empty (no dois were moved over and the slot is unnecessary)
        if not study['associated_dois']:
            del study['associated_dois']

        return study
