from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator_from_8_1_to_9_0(MigratorBase):
    """previously: Migrates data from schema 8.1.0 to 9.0.0"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.move_doi_from_websites],
        )

    def move_doi_from_websites(study: dict):

        doi_updates = load_yaml_asset('migrator_from_9_1_to_9_2/websites_dois.yaml')

        # transform websites into doi curies and add to associated_dois slot
        if 'websites' in study:
            websites = study['websites']
            for site in websites:
                for doi_update in doi_updates:
                    if site == doi_update['doi_website']:
                        doi_value = 'doi:' + site[site.find('10'):]
                        new_doi = {
                            'doi_value': doi_value,
                            'doi_category': doi_update['doi_cat'],
                            'doi_provider': doi_update['doi_prov']
                        }
                        print(new_doi)
                        study.setdefault('associated_dois', []).append(new_doi)
            
            # remove doi websites from websites slot
            for update in doi_updates:
                if update['doi_website'] in websites:
                    websites.remove(update['doi_website'])

        return study

    