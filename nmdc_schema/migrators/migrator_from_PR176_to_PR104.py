from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    This migrator removes fields from documents of type `nmdc:MassSpectrometry` in the `data_generation_set` collection.
    """

    _from_version = "PR176"
    _to_version = "PR104"

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.process_each_document(
            collection_name="data_generation_set",
            pipeline=[self.delete_obsolete_fields],
        )

    @staticmethod
    def delete_obsolete_fields(data_generation: dict) -> dict:
        r"""
        Deletes fields from the specified document of type `nmdc:MassSpectrometry`.

        If the document is not of type `nmdc:MassSpectrometry`, this function will not modify the document.
        If the field exists and is empty, this function will delete the field.
        If the field exists and is not empty, this function will raise an exception.

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
        ValueError: Field "ncbi_project_name" in document "123" is not empty (has value "a").
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'gold_sequencing_project_identifiers': ['a']})  # multivalued, is not empty
        Traceback (most recent call last):
        ...
        ValueError: Field "gold_sequencing_project_identifiers" in document "123" is not empty (has value "['a']").
        >>> m.delete_obsolete_fields({'id': 123, 'type': 'nmdc:MassSpectrometry',
        ...                           'ncbi_project_name': None,
        ...                           'target_gene': '',
        ...                           'target_subfragment': '',
        ...                           'gold_sequencing_project_identifiers': None,
        ...                           'insdc_bioproject_identifiers': [],
        ...                           'insdc_experiment_identifiers': []})  # multiple obsolete fields
        {'id': 123, 'type': 'nmdc:MassSpectrometry'}
        """

        # If this document is not of type "nmdc:MassSpectrometry", return the document as-is (i.e. no changes).
        if data_generation["type"] != "nmdc:MassSpectrometry":
            return data_generation

        # Emptiness is represented by: None or ""
        single_valued_fields_to_delete = [
            "ncbi_project_name",
            "target_gene",
            "target_subfragment",
        ]

        # Emptiness is represented by: None or []
        multi_valued_fields_to_delete = [
            "gold_sequencing_project_identifiers",
            "insdc_bioproject_identifiers",
            "insdc_experiment_identifiers",
        ]

        for field_name in (
            single_valued_fields_to_delete + multi_valued_fields_to_delete
        ):
            # Check whether the field exists.
            if field_name in data_generation:
                document_id = data_generation["id"]
                value = data_generation[field_name]

                # Check whether the field is empty (using emptiness criteria appropriate for the field).
                if (
                    field_name in single_valued_fields_to_delete
                    and value not in [None, ""]
                ) or (
                    field_name in multi_valued_fields_to_delete
                    and value not in [None, []]
                ):
                    raise ValueError(
                        f'Field "{field_name}" in document "{document_id}" is not empty (has value "{value}").'
                    )
                else:
                    data_generation.pop(field_name)

        return data_generation
