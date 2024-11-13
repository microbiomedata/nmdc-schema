from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    # Note: This migrator was introduced via PR 2203 (i.e. https://github.com/microbiomedata/nmdc-schema/pull/2203).
    _from_version = "11.1.0.part_1"
    _to_version = "11.1.0.part_2" 

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        Updates each document in the `functional_annotation_agg` collection so that
        its `metagenome_annotation_id` field is effectively renamed to `was_generated_by`.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'functional_annotation_agg': [
        ...     {'metagenome_annotation_id': 'x', 'other': 'a'},
        ...     {'metagenome_annotation_id': 'y', 'other': 'b'},
        ...   ],
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.upgrade()
        >>> all('metagenome_annotation_id' not in doc for doc in db['functional_annotation_agg'])
        True
        >>> all('was_generated_by' in doc for doc in db['functional_annotation_agg'])
        True
        >>> db['functional_annotation_agg'][0]
        {'other': 'a', 'was_generated_by': 'x'}
        >>> db['functional_annotation_agg'][1]
        {'other': 'b', 'was_generated_by': 'y'}
        """

        self.adapter.copy_value_from_field_to_field_in_each_document(
            collection_name="functional_annotation_agg",
            source_field_name="metagenome_annotation_id",
            destination_field_name="was_generated_by",
        )

        self.adapter.remove_field_from_each_document(
            collection_name="functional_annotation_agg",
            field_name="metagenome_annotation_id",
        )
