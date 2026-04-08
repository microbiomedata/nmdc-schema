from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.17.1"
    _to_version = "11.18.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.validate_biosample_name,
        )

    def validate_biosample_name(self, biosample: dict) -> None:
        r"""
        Validates the name of the specified biosample.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'biosample_set': [{'id': 'b1', 'name': 'sample1'}, {'id': 'b2', 'name': 123}, {'id': 'b3'}]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.validate_biosample_name(database['biosample_set'][0])  # valid
        >>> m.validate_biosample_name(database['biosample_set'][1])  # invalid: non-string
        Traceback (most recent call last):
        ...
        ValueError: Biosample b2 lacks a string name
        >>> m.validate_biosample_name(database['biosample_set'][2])  # invalid: missing
        Traceback (most recent call last):
        ...
        ValueError: Biosample b3 lacks a string name
        """
        if "name" not in biosample or not isinstance(biosample["name"], str):
            raise ValueError(f"Biosample {biosample['id']} lacks a string name")
