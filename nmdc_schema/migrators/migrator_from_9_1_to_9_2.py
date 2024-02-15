from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "9.1"
    _to_version = "9.2"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("study_set", [self.move_doi_from_websites])

    def move_doi_from_websites(self, study: dict):
        r"""
        Transforms `websites` values that are dois into curies and moves them into the `associated_dois slot
        Removes the doi website values from the `websites slot.
        
        >>> m = Migrator()
        >>> m.move_doi_from_websites({'id': 123, 'websites': ['a', 'https://doi.org/10.25982/109073.30/1895615'], 'associated_dois': 
        ...     [{'doi_value': 'j', 'doi_provider': 'k', 'doi_category': 'i'}]})
        {'id': 123, 'websites': ['a'], 'associated_dois': [{'doi_value': 'j', 'doi_provider': 'k', 'doi_category': 'i'}, {'doi_value': 'doi:10.25982/109073.30/1895615', 'doi_category': 'dataset_doi', 'doi_provider': 'kbase'}]}
        """

        doi_updates = load_yaml_asset('migrator_from_9_1_to_9_2/websites_dois.yaml')

         # transform websites into doi curies and add to associated_dois slot
        if 'websites' in study:
            websites = study['websites']
            for doi_update in doi_updates:
                if doi_update['doi_website'] in websites:
                    doi_value = 'doi:' + doi_update['doi_website'][doi_update['doi_website'].find('10'):]
                    new_doi = {
                        'doi_value': doi_value,
                        'doi_category': doi_update['doi_cat'],
                        'doi_provider': doi_update['doi_prov']
                    }
                    study.setdefault('associated_dois', []).append(new_doi)

                    # remove doi website from websites slot
                    websites.remove(doi_update['doi_website'])
        
        return study

    