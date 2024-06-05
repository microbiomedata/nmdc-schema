from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """Migrates data from schema X to PR4"""

    _from_version = "X"
    _to_version = "PR4"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(collection_name="omics_processing_set",
                                           pipeline=[self.update_analyte_category_from_omics_type])

    def update_analyte_category_from_omics_type(self, omics_proc: dict):
        r"""
        Transforms values in the 'omics_type.has_raw_value' slot to match the accepted AnalyteCategoryEnum and adds
        a new slot called analyte_category with the accepted value. Removes the omics_type slot.
        
        >>> m = Migrator()
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
            raise ValueError(f"The 'omics_type' value ({omics_type}) of document '{omics_proc['id']}' "
                             f"does not match any 'analyte_category' values.")

        return omics_proc

    