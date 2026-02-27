from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "11.13.0.part_2"
    _to_version = "11.13.0.part_3"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """
        self.adapter.do_for_each_document("biosample_set", self.confirm_igsn_prefix)

    def confirm_igsn_prefix(self, biosample: dict) -> None:
        r"""
        If a biosample  has a igsn_biosample_identifiers prefix of 'IGSN' raise an exception.

        >>> m = Migrator()

        # Test: igsn_biosample_identifiers matching "IGSN:"
        >>> m.confirm_igsn_prefix({"id": 1, "type": "nmdc:Biosample", "igsn_biosample_identifiers": ["IGSN:AU124"]})
        Traceback (most recent call last):
            ...
        ValueError: Biosample 1 'igsn_biosample_identifiers' list includes: IGSN:AU124

        # Test: igsn_biosample_identifiers with another non-confirming prefix
        >>> m.confirm_igsn_prefix({"id": 1, "type": "nmdc:Biosample", "igsn_biosample_identifiers": ["isng:AU124"]})
        Traceback (most recent call last):
            ...
        ValueError: Biosample 1 'igsn_biosample_identifiers' list includes: isng:AU124

        # Test: valid Biosample
        >>> m.confirm_igsn_prefix({"id": 3, "type": "nmdc:Biosample", "igsn_biosample_identifiers": ["igsn:AU124"]}) is None
        True
        """
        prefix = "igsn:"
        igsn_values = biosample.get("igsn_biosample_identifiers", [])
        biosample_id = biosample.get("id")
        for record in igsn_values:
            if not record.startswith(prefix):
                raise ValueError(
                    f"Biosample {biosample_id} 'igsn_biosample_identifiers' list includes: {record}"
                )
