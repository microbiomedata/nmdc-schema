"""Remove the deprecated ``collection_date_inc`` slot from Biosample records.

The harvest date is the harvested sample's own ``collection_date``; an
incubation is recorded as a MaterialProcessing that links the input and output
samples and carries ``start_date`` and ``end_date``.

See https://github.com/microbiomedata/nmdc-schema/issues/2658 and the example
``src/data/valid/Database-incubation-as-culturing.yaml``.
"""

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase

FIELD_NAME = "collection_date_inc"


class Migrator(MigratorBase):
    r"""Drop ``collection_date_inc`` from every ``biosample_set`` document.

    The slot was already treated as removed by
    ``partials/migrator_from_11_10_0_to_11_11_0/migrator_from_11_10_0_to_11_11_0_part_1.py``,
    which raises if any biosample carries it, so no production record is
    expected to have one. This partial removes the field anyway rather than
    raising, because the slot stayed valid in the schema through 11.23.0 and
    could have been populated since that check ran.
    """

    _from_version = "11.24.0.part_2"
    _to_version = "11.24.0.part_3"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "biosample_set": [
        ...         {"id": "nmdc:bsm-1", "type": "nmdc:Biosample",
        ...          "collection_date": {"type": "nmdc:TimestampValue", "has_raw_value": "2021-04-15"},
        ...          "collection_date_inc": "2021-04-22"},
        ...         {"id": "nmdc:bsm-2", "type": "nmdc:Biosample"},
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> "collection_date_inc" in db["biosample_set"][0]
        False
        >>> db["biosample_set"][0]["collection_date"]["has_raw_value"]
        '2021-04-15'
        >>> db["biosample_set"][1]
        {'id': 'nmdc:bsm-2', 'type': 'nmdc:Biosample'}
        """
        self._warn_if_commit_ignored(commit_changes)

        if isinstance(self.adapter, MongoAdapter):
            try:
                self.adapter.process_collections_in_transaction(
                    collection_names=["biosample_set"],
                    document_processor=self.drop_collection_date_inc,
                    commit_changes=commit_changes,
                )
                if commit_changes:
                    self.logger.info("Transaction committed (changes have been saved)")
                else:
                    self.logger.info("Transaction rolled back (no changes were committed)")
            except Exception as e:
                self.logger.error(f"Migration failed: {e}")
                raise
        else:
            self.adapter.process_each_document(
                "biosample_set", [self.drop_collection_date_inc]
            )
            if not commit_changes:
                self.logger.info(
                    "Note: Non-MongoDB adapter doesn't support rollback - changes are applied immediately"
                )

    def drop_collection_date_inc(self, document: dict) -> dict:
        r"""Remove ``collection_date_inc`` from a biosample document.

        >>> m = Migrator()
        >>> m.drop_collection_date_inc({"id": "nmdc:bsm-1", "collection_date_inc": "2021-04-22"})
        {'id': 'nmdc:bsm-1'}

        A document without the field is returned unchanged:
        >>> m.drop_collection_date_inc({"id": "nmdc:bsm-2", "collection_date": "2021-04-15"})
        {'id': 'nmdc:bsm-2', 'collection_date': '2021-04-15'}

        An empty-string value is dropped just like a populated one:
        >>> m.drop_collection_date_inc({"id": "nmdc:bsm-3", "collection_date_inc": ""})
        {'id': 'nmdc:bsm-3'}
        """
        document.pop(FIELD_NAME, None)
        return document
