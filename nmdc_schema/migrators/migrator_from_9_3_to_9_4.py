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
            study_set=[self.is_best_protein_no_op],
        )

    def is_best_protein_no_op(self, metap_gene_function_aggregation: dict) -> (
            dict):
        """
        >>> mig = Migrator_from_9_3_to_9_4()  # creates a class instance on
        which we can call this function (method)
        """
        return metap_gene_function_aggregation

