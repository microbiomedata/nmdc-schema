from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    This migrator removes the `part_of` field from all documents that represent an instance of
    the `WorkflowExecution` class or any of its subclasses.

    The creation of this migrator was prompted by this GitHub comment:
    https://github.com/microbiomedata/berkeley-schema-fy24/pull/210#pullrequestreview-2119492107

    This migrator was designed to be run before `migrator_from_10_2_0_to_11_0_0_part_16.py`, since that one
    moves the documents from all of these collections into one named `workflow_execution_set`.
    """

    _from_version = "X"
    _to_version = "PR104"

    collection_names = [
        "workflow_execution_set",
        "metagenome_annotation_set",
        "metagenome_assembly_set",
        "metatranscriptome_assembly_set",
        "metatranscriptome_annotation_set",
        "metatranscriptome_analysis_set",
        "mags_set",
        "metagenome_sequencing_set",
        "read_qc_analysis_set",
        "read_based_taxonomy_analysis_set",
        "metabolomics_analysis_set",
        "metaproteomics_analysis_set",
        "nom_analysis_set",
    ]

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'workflow_execution_set': [
        ...     {'id': 1},
        ...     {'id': 2, 'part_of': 'a'},
        ...     {'id': 3, 'part_of': 'b', 'foo': 'bar'},
        ...   ],
        ...   'metagenome_annotation_set': [
        ...     {'id': 1},
        ...     {'id': 2, 'part_of': 'a'},
        ...     {'id': 3, 'part_of': 'b', 'foo': 'bar'},
        ...   ]
        ... }
        >>> any("part_of" in document for document in db["workflow_execution_set"])
        True
        >>> any("part_of" in document for document in db["metagenome_annotation_set"])
        True
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.upgrade()
        >>> any("part_of" in document for document in db["workflow_execution_set"])
        False
        >>> any("part_of" in document for document in db["metagenome_annotation_set"])
        False
        """

        for collection_name in self.collection_names:
            self.logger.info(f"Processing collection: {collection_name}")
            self.adapter.process_each_document(
                collection_name=collection_name, pipeline=[self.remove_part_of_field]
            )

    def remove_part_of_field(self, workflow_execution) -> dict:
        r"""
        Removes the `part_of` field from the document.

        >>> m = Migrator()
        >>> m.remove_part_of_field({'id': 123, 'part_of': 'whole'})
        {'id': 123}
        >>> m.remove_part_of_field({'id': 123, 'other': 'potato'})
        {'id': 123, 'other': 'potato'}
        >>> m.remove_part_of_field({'id': 123, 'other': 'potato', 'part_of': 'whole'})
        {'id': 123, 'other': 'potato'}
        """

        if "part_of" in workflow_execution:
            del workflow_execution["part_of"]

        return workflow_execution
