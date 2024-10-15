from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "PR176"
    _to_version = "PR104"

    def upgrade(self) -> None:
        r"""
        Deletes specific fields from documents (whose `type` is `nmdc:MassSpectrometry`) residing in
        the `data_generation_set` collection.
        """

        self.adapter.process_each_document(
            collection_name="data_generation_set",
            pipeline=[self.delete_obsolete_fields],
        )

    @staticmethod
    def delete_obsolete_fields(data_generation: dict) -> dict:
        r"""
        Deletes specific fields from a document representing a `DataGeneration` instance.

        If the document's `type` is not `nmdc:MassSpectrometry`, this function will not modify the document.
        If a target field exists and is empty, this function will delete the field. On the other hand, if a target
        field exists and is not empty, this function will not delete the field and will, instead, raise an exception.

        >>> m = Migrator()
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry'})  # no obsolete fields exist
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:NucleotideSequencing',
        ...                           'ncbi_project_name': ''})  # type is not relevant
        {'id': 123, 'type': 'nmdc:NucleotideSequencing', 'ncbi_project_name': ''}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'ncbi_project_name': ''})  # single-valued, is empty
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'ncbi_project_name': None})
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'gold_sequencing_project_identifiers': []})  # multivalued, is empty
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'gold_sequencing_project_identifiers': None})
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'ncbi_project_name': 'a'})  # single-valued, is not empty
        Traceback (most recent call last):
        ...
        ValueError: Field "ncbi_project_name" in document "123" is not empty (contains value "a").
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'gold_sequencing_project_identifiers': ['a']})  # multivalued, is not empty
        Traceback (most recent call last):
        ...
        ValueError: Field "gold_sequencing_project_identifiers" in document "123" is not empty (contains value "['a']").
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'ncbi_project_name': None,
        ...                           'target_gene': '',
        ...                           'target_subfragment': '',
        ...                           'gold_sequencing_project_identifiers': None,
        ...                           'insdc_bioproject_identifiers': [],
        ...                           'insdc_experiment_identifiers': []})  # multiple obsolete fields
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        """

        # If this document's `type` is not "nmdc:MassSpectrometry", leave the document as-is.
        if data_generation["type"] != "nmdc:MassSpectrometry":
            return data_generation

        # List the names of the single-valued fields we want to delete.
        # Note: Their emptiness is represented by `None` or `""`.
        single_valued_fields_to_delete = [
            "ncbi_project_name",
            "target_gene",
            "target_subfragment",
        ]

        # List the names of the multivalued fields we want to delete.
        # Note: Their emptiness is represented by `None` or `[]`.
        multi_valued_fields_to_delete = [
            "gold_sequencing_project_identifiers",
            "insdc_bioproject_identifiers",
            "insdc_experiment_identifiers",
        ]

        # Combine the two lists.
        field_names = single_valued_fields_to_delete + multi_valued_fields_to_delete

        for field_name in field_names:
            # Check whether the field exists.
            if field_name in data_generation:
                value = data_generation[field_name]

                # Check whether the field is empty (using emptiness criteria appropriate for the field).
                if (
                    field_name in single_valued_fields_to_delete and value in [None, ""]
                ) or (
                    field_name in multi_valued_fields_to_delete and value in [None, []]
                ):
                    del data_generation[field_name]
                else:
                    document_id = data_generation["id"]
                    raise ValueError(
                        f'Field "{field_name}" in document "{document_id}" is not empty (contains value "{value}").'
                    )

        return data_generation
