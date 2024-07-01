from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR2 and PR24, namely renames all renamed collections.
    """
    _from_version = "X"
    _to_version = "PR2_and_PR24"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        old_to_new_names = {
            "omics_processing_set": "data_generation_set",
            "mags_activity_set": "mags_set",
            "metabolomics_analysis_activity_set": "metabolomics_analysis_set",
            "metagenome_annotation_activity_set": "metagenome_annotation_set",
            "metagenome_sequencing_activity_set": "metagenome_sequencing_set",
            "metaproteomics_analysis_activity_set": "metaproteomics_analysis_set",
            "metatranscriptome_activity_set": "metatranscriptome_analysis_set",
            "nom_analysis_activity_set": "nom_analysis_set",
            "read_based_taxonomy_analysis_activity_set": "read_based_taxonomy_analysis_set",
            "read_qc_analysis_activity_set": "read_qc_analysis_set",
            "activity_set": "workflow_execution_set"
            }

        for current_collection_name, new_collection_name in old_to_new_names.items():
            try:
                self.adapter.rename_collection(current_name=current_collection_name, new_name=new_collection_name)
            except KeyError:
                raise KeyError(f"Error: Collection '{current_collection_name}' does not exist.")
