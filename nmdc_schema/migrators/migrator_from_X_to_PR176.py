from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR129, namely changes the permissible values of the failure_where slot in the read_qc_analysis_set collection.
    """
    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        # Populate the "collection-to-transformers" map for this specific migration.
        agenda = dict(
            read_qc_analysis_activity_set=[self.standardize_failure_where_enum], 
            # QUESTION: Should this be read_qc_analysis_activity_set or read_qc_analysis_set?  
        )

        for collection_name, pipeline in agenda.items():
            self.adapter.process_each_document(collection_name=collection_name, pipeline=pipeline)


    def standardize_failure_where_enum(self, read_qc_analysis: dict):
        r"""
        Transforms the values of the qc_failure_where slot to the new permissible values of the FailureWhereEnum.
        
        >>> m = Migrator()
        >>> m.standardize_failure_where_enum({'id': 123, 'has_failure_categorization': {'qc_failure_where': 'OmicsProcessing'}})
        {'id': 123, 'has_failure_categorization': {'qc_failure_where': 'DataGeneration'}})
        """

        failure_where_translation_dict = {
            "OmicsProcessing": "DataGeneration",
            "Pooling": "Pooling",
            "Extraction": "Extraction",
            "LibraryPreparation": "LibraryPreparation",
            "MetagenomeAssembly": "MetagenomeAssembly",
            "MetatranscriptomeActivity": "MetatranscriptomeAnalysis",
            "MagsAnalysisActivity": "MagsAnalysis",
            "ReadQcAnalysisActivity": "ReadQcAnalysis",
            "ReadBasedTaxonomyAnalysisActivity": "ReadBasedTaxonomyAnalysis",
            "MetagenomeAnnotationActivity": "MetagenomeAnnotation",
        }

        if 'has_failure_categorization' in read_qc_analysis.keys():
            if 'qc_failure_where' in read_qc_analysis['has_failure_categorization'].keys():
                og_value = read_qc_analysis['has_failure_categorization']['qc_failure_where']
                if og_value in failure_where_translation_dict.keys():
                    read_qc_analysis['has_failure_categorization']['qc_failure_where'] = failure_where_translation_dict[og_value]
                else:
                    raise ValueError(f"Value {og_value} is not a valid value for the qc_failure_where slot.")
        return read_qc_analysis