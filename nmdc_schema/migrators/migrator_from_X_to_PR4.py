from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator_from_X_to_PR4(MigratorBase):
    """Migrates data from schema X to PR4"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            omics_processing_set=[self.update_analyte_category_from_omics_type],
        )

    def update_analyte_category_from_omics_type(self, omics_proc: dict):
        r"""
        Transforms values in the 'omics_type.has_raw_value' slot to match the accepted AnalyteCategoryEnum and adds
        a new slot called analyte_category with the accepted value. Removes the omics_type slot.
        
        >>> m = Migrator_from_X_to_PR4()
        >>> m.update_analyte_category_from_omics_type({'id': 123, 'omics_type': {'has_raw_value': 'Organic Matter Characterization'}})
        {'id': 123, 'analyte_category': 'nom'}
        """

        # Maps all the existing values for omics_type.has_raw_value to the allowed values for 
        # analyte category. Used Mongodb distinct in a separate query to get all the existing values.
        omics_type_to_analyte_category_mapping = {"Metagenome": "metagenome",
                                                  "metagenome": "metagenome",
                                                  "Metatranscriptome": "metatranscriptome",
                                                  "Proteomics": "metaproteome",
                                                  "Metabolomics": "metabolome",
                                                  "Lipidomics": "lipidome",
                                                  "Organic Matter Characterization": "nom"
                                              }
        
        omics_type = omics_proc.get("omics_type").get("has_raw_value")

        # If the value for omics type is a key in the mapping dictionary, then create a slot
        # analyte_cateogry with the value, the value from the mapping dictionary.
        if omics_type in omics_type_to_analyte_category_mapping:
            omics_proc["analyte_category"] = omics_type_to_analyte_category_mapping[omics_type]

            # remove omics_type slot
            del omics_proc["omics_type"]
    
        else: 
            self.logger.error(f"omics type does not match any analyte categories for {omics_proc['id']}")
        
        return omics_proc

    