"""Check that no Biosample still uses the removed ``collection_time_inc`` slot.

https://github.com/microbiomedata/nmdc-schema/pull/3470 removed the slot. Its replacement,
``collection_time``, belongs to the harvested sample, and an incubation's own times belong to
a processing step, so there is no transformation a migrator can apply on its own. If a record
still has the slot, this partial raises so that a person can decide where the value goes.

See https://github.com/microbiomedata/nmdc-schema/issues/3489.
"""

from nmdc_schema.migrators.migrator_base import MigratorBase

REMOVED_BIOSAMPLE_SLOTS = ["collection_time_inc"]


class Migrator(MigratorBase):
    r"""Raise if any ``biosample_set`` document has a slot removed in this release."""

    _from_version = "11.24.1"
    _to_version = "11.25.0.part_1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Check every ``biosample_set`` document. Nothing is changed.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {"biosample_set": [{"id": "nmdc:bsm-1", "type": "nmdc:Biosample", "collection_time": "05:42+0000"}]}
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["biosample_set"][0]
        {'id': 'nmdc:bsm-1', 'type': 'nmdc:Biosample', 'collection_time': '05:42+0000'}
        >>> db = {"biosample_set": [{"id": "nmdc:bsm-2", "type": "nmdc:Biosample", "collection_time_inc": "13:42+0000"}]}
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        Traceback (most recent call last):
        ...
        Exception: Field `collection_time_inc` present in biosample nmdc:bsm-2.
        """
        self.adapter.do_for_each_document("biosample_set", self.check_for_fields)

    def check_for_fields(self, biosample: dict) -> None:
        r"""
        Raise if the biosample has any of the removed slots, even with an empty value.

        >>> m = Migrator()
        >>> m.check_for_fields({"id": "nmdc:bsm-3", "type": "nmdc:Biosample", "collection_time_inc": ""})
        Traceback (most recent call last):
        ...
        Exception: Field `collection_time_inc` present in biosample nmdc:bsm-3.
        >>> m.check_for_fields({"id": "nmdc:bsm-4", "type": "nmdc:Biosample"})
        """
        for slot in REMOVED_BIOSAMPLE_SLOTS:
            if slot in biosample:
                raise Exception(f"Field `{slot}` present in biosample {biosample.get('id')}.")
