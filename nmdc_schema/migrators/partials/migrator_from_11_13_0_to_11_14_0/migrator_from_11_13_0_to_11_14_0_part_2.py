from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "11.14.0_part_1"
    _to_version = "11.14.0_part_2"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """
        self.adapter.do_for_each_document("processed_sample_set", self.confirm_empty)

    def confirm_empty(self, processedsample: dict) -> None:
        r"""
        If a processedsample has a value for 'biomaterial_purity' raise an exception.

        >>> m = Migrator()

        # Test: processed sample has biomaterial_purity value
        >>> m.confirm_empty({"id": 1, "type": "nmdc:ProcessedSample", "biomaterial_purity": ["Test_Value"]})
        Traceback (most recent call last):
            ...
        ValueError: Biosample 1 'biomaterial_purity' values include: ['Test_Value']

        # Test: valid processedsample
        >>> m.confirm_empty({"id": 3, "type": "nmdc:ProcessedSample"}) is None
        True
        """
        bp_values = processedsample.get("biomaterial_purity", [])
        biosample_id = processedsample.get("id")

        if len(bp_values)>0:
            raise ValueError(
                f"Biosample {biosample_id} 'biomaterial_purity' values include: {bp_values}"
            )
