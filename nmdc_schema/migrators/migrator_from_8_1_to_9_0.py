from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "8.1"
    _to_version = "9.0"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("study_set", [
            self.fix_award_dois,
            self.fix_pub_dois,
            self.fix_massive,
            self.fix_ess_dive,
            self.remove_doi_slots
        ])

    def process_doi(self, study: dict, doi_list: list, doi_category: str):
        r"""
        For each update descriptor in the `doi_list` list; if the specified study's `id` matches that descriptor's `id`,
        this function appends a DOI dictionary to the study's `associated_dois` list (creating the list if necessary).

        >>> m = Migrator()
        >>> m.process_doi({'id': 123}, [{'id': 123, 'doi': 'a', 'doi_prov': 'b'}], 'c')  # `id` matches
        {'id': 123, 'associated_dois': [{'doi_value': 'a', 'doi_category': 'c', 'doi_provider': 'b'}]}
        >>> m.process_doi({'id': 123}, [{'id': 555, 'doi': 'a', 'doi_prov': 'b'}], 'c')  # `id` does not match
        {'id': 123}
        >>> m.process_doi(
        ...     {'id': 123, 'associated_dois': [{'doi_value': 'x', 'doi_category': 'y', 'doi_provider': 'z'}]},
        ...     [{'id': 123, 'doi': 'a', 'doi_prov': 'b'}], 'c'
        ... )  # study already has an `associated_dois` field
        {'id': 123, 'associated_dois': [{'doi_value': 'x', 'doi_category': 'y', 'doi_provider': 'z'}, {'doi_value': 'a', 'doi_category': 'c', 'doi_provider': 'b'}]}
        """

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
        r"""
        Copies `publication_dois` values into a new slot named `associated_dois`.

        >>> m = Migrator()
        >>> m.fix_pub_dois({'id': 1, 'publication_dois': ['a']})  # test: a single DOI
        {'id': 1, 'publication_dois': ['a'], 'associated_dois': [{'doi_value': 'a', 'doi_category': 'publication_doi'}]}
        """

        study.setdefault('associated_dois', []).extend(
            {'doi_value': pub_doi, 'doi_category': 'publication_doi'}
            for pub_doi in study.get('publication_dois', [])
        )

        return study

    def fix_massive(self, study: dict):
        r"""
        Changes the one `massive_study_identifiers` value into a DOI and moves it to a new `associated_dois` slot.

        >>> m = Migrator()
        >>> m.fix_massive({'id': 123})
        {'id': 123, 'associated_dois': []}
        >>> m.fix_massive({'id': 123, 'massive_study_identifiers': ['not-the-one']})
        {'id': 123, 'massive_study_identifiers': ['not-the-one'], 'associated_dois': []}
        >>> m.fix_massive({'id': 123, 'massive_study_identifiers': ['MASSIVE:MSV000090886']})  # this is the one!
        {'id': 123, 'associated_dois': [{'doi_value': 'doi:10.25345/C58K7520G', 'doi_category': 'dataset_doi', 'doi_provider': 'massive'}]}
        """

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
        r"""
        Copies `ess_dive_datasets` values into a new slot named `associated_dois`.

        >>> m = Migrator()
        >>> m.fix_ess_dive({'id': 1, 'ess_dive_datasets': ['a']})  # test: a single DOI
        {'id': 1, 'ess_dive_datasets': ['a'], 'associated_dois': [{'doi_value': 'a', 'doi_category': 'dataset_doi', 'doi_provider': 'ess_dive'}]}
        """

        study.setdefault('associated_dois', []).extend(
            {'doi_value': dataset_doi, 'doi_category': 'dataset_doi',
             'doi_provider': 'ess_dive'}
            for dataset_doi in study.get('ess_dive_datasets', []))

        return study

    def remove_doi_slots(self, study: dict):
        r"""
        Removes slots that are no longer needed because their values have been moved to the `associated_dois` slot.

        >>> m = Migrator()
        >>> m.remove_doi_slots({'id': 123, 'associated_dois': []})  # empty `associated_dois` list gets removed
        {'id': 123}
        >>> m.remove_doi_slots({
        ...    'id': 123,
        ...    'associated_dois': [{'doi_value': 'a', 'doi_category': 'c', 'doi_provider': 'b'}],
        ...    'publication_dois': ['a'],
        ... })  # lists in which all values match an `associated_dois[].doi_value` get removed
        {'id': 123, 'associated_dois': [{'doi_value': 'a', 'doi_category': 'c', 'doi_provider': 'b'}]}
        """

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
                self.logger.error(f'Field {slot_name} of Study {study["id"]} was not falsy. Skipped slot deletion.')
                raise ValueError(f'Field {slot_name} of Study ({study["id"]}) is not empty.')

        # Remove associated_dois if empty (no dois were moved over and the slot is unnecessary)
        if not study['associated_dois']:
            del study['associated_dois']

        return study
