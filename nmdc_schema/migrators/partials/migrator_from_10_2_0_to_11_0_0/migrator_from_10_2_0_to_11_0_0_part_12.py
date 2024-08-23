from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR176, namely changes the permissible values of the failure_where slot in the read_qc_analysis_set collection.

    Should be run after migrator_from_10_2_0_to_11_0_0_part_09.py.
    """
    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        # Populate the "collection-to-transformers" map for this specific migration.
        agenda = dict(
            # We can assume that all the documents in the read_qc_analysis_set collection are of the type ReadQcAnalysisActivity, and any OmicsProcessing failures should be mapped to NucleotideSequencing
            read_qc_analysis_set=[self.standardize_failure_where_enum_ns], 
        )

        for collection_name, pipeline in agenda.items():
            self.adapter.process_each_document(collection_name=collection_name, pipeline=pipeline)


    def standardize_failure_where_enum_ns(self, read_qc_analysis: dict):
        r"""
        Transforms the values of the qc_failure_where slot to the new permissible values of the FailureWhereEnum, for sets related to NucleatideSequencing
        
        >>> m = Migrator()
        >>> m.standardize_failure_where_enum_ns({'id': 123, 'has_failure_categorization': [{'qc_failure_where': 'OmicsProcessing'}]})
        {'id': 123, 'has_failure_categorization': [{'qc_failure_where': 'NucleotideSequencing'}]}
        """

        failure_where_translation_dict = {
            "OmicsProcessing": "NucleotideSequencing",
            "Pooling": "Pooling",
            "Extraction": "Extraction",
            "LibraryPreparation": "LibraryPreparation",
            "MetagenomeAssembly": "MetagenomeAssembly",
            "MetatranscriptomeActivity": "MetatranscriptomeExpressionAnalysis",
            "MagsAnalysisActivity": "MagsAnalysis",
            "ReadQcAnalysisActivity": "ReadQcAnalysis",
            "ReadBasedTaxonomyAnalysisActivity": "ReadBasedTaxonomyAnalysis",
            "MetagenomeAnnotationActivity": "MetagenomeAnnotation",
        }

        if 'has_failure_categorization' in read_qc_analysis:
            for failure_categorization in read_qc_analysis['has_failure_categorization']:
                og_value = None  # ensure the variable is defined, since we use it in the error message
                if 'qc_failure_where' in failure_categorization:
                    og_value = failure_categorization.get('qc_failure_where')
                    if og_value in failure_where_translation_dict:
                        failure_categorization['qc_failure_where'] = failure_where_translation_dict.get(og_value)
                else:
                    raise ValueError(f"Invalid 'qc_failure_where' value: {og_value}")
        return read_qc_analysis