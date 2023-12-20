from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator_from_9_3_to_9_4(MigratorBase):
    """
    Migrates data from schema 9.3 to 9.4
    """

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""
        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            metap_gene_function_aggregation_set=[self.transform_best_protein],
        )

    def transform_best_protein(self, metap_gene_function_aggregation: dict) -> (
            dict):
        """
        >>> mig = Migrator_from_9_3_to_9_4()  # creates a class instance on
        >>> mig.transform_best_protein({'metaproteomic_analysis_id': 'foo', 'gene_function_id': 'bar', 'count': 1, 'best_protein': True})
        {'metaproteomic_analysis_id': 'foo', 'gene_function_id': 'bar', 'count': 1, 'is_best_protein': True}
        """
        self.logger.info(f"Transforming metap_gene_function_aggregation: {metap_gene_function_aggregation['metaproteomic_analysis_id']}")
        original_best_protein = metap_gene_function_aggregation.get('best_protein')
        metap_gene_function_aggregation['is_best_protein'] = original_best_protein
        del metap_gene_function_aggregation['best_protein']
        return metap_gene_function_aggregation

