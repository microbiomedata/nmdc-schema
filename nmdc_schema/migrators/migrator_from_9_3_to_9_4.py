from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """Migrates data between two schema versions."""

    _from_version = "9.3"
    _to_version = "9.4"

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""
        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            metap_gene_function_aggregation_set=[self.rename_best_protein_field],
        )

    def rename_best_protein_field(self, metap_gene_function_aggregation: dict) -> dict:
        """
        Renames the `best_protein` field to `is_best_protein`.

        >>> mig = Migrator()
        >>> mig.rename_best_protein_field({'metaproteomic_analysis_id': 'foo', 'gene_function_id': 'bar', 'count': 1, 'best_protein': True})
        {'metaproteomic_analysis_id': 'foo', 'gene_function_id': 'bar', 'count': 1, 'is_best_protein': True}
        """
        self.logger.info(f"Transforming metap_gene_function_aggregation: {metap_gene_function_aggregation['metaproteomic_analysis_id']}")
        original_best_protein = metap_gene_function_aggregation.get('best_protein')
        metap_gene_function_aggregation['is_best_protein'] = original_best_protein
        del metap_gene_function_aggregation['best_protein']
        return metap_gene_function_aggregation

