from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "PR104"
    _to_version = "PR195"

    # Map the names of the collections that store documents representing instances of direct
    # subclasses of `PlannedProcess`, to a list of the collections that do/would store documents
    # representing instances of that subclass's subclasses.
    # Reference: https://microbiomedata.github.io/berkeley-schema-fy24/PlannedProcess/
    collection_names_hierarchy = {
        "collecting_biosamples_from_site_set": [],
        "protocol_execution_set": [],
        "storage_process_set": [],
        "material_processing_set": [
            "pooling_set",
            "extraction_set",
            "library_preparation_set",
            "sub_sampling_process_set",
            "mixing_process_set",
            "filtration_process_set",
            "chromatographic_separation_process_set",
            "dissolving_process_set",
            "chemical_conversion_process_set",
        ],
        "data_generation_set": [
            "nucleotide_sequencing_set",
            "mass_spectrometry_set",
        ],
        "workflow_execution_set": [
            "metagenome_annotation_set",
            "metagenome_assembly_set",
            "metatranscriptome_assembly_set",
            "metatranscriptome_annotation_set",
            "metatranscriptome_analysis_set",
            "metatranscriptome_expression_analysis_set",  # included in order to accommodate: https://github.com/microbiomedata/nmdc-schema/pull/2117
            "mags_set",
            "metagenome_sequencing_set",
            "read_qc_analysis_set",
            "read_based_taxonomy_analysis_set",
            "metabolomics_analysis_set",
            "metaproteomics_analysis_set",
            "nom_analysis_set",
        ],
    }

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        In PR195, the schema changed so that the `Database` class has a slot for each direct subclass of
        `PlannedProcess`; but does not have slots for _their_ subclasses. This migrator creates collections,
        moves documents between collections, and deletes collections, in accordance with that schema change.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'material_processing_set': [{'id': 'mp'}],
        ...             'pooling_set': [{'id': 'p'}],
        ...             'metatranscriptome_expression_analysis_set': [{'id': 'ma1'}],
        ...             'nom_analysis_set': [{'id': 'na1'}, {'id': 'na2'}, {'id': 'na3'}]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.upgrade()
        >>> len(database['material_processing_set'])  # ensure migrator moves document to "parent" collection
        2
        >>> 'pooling_set' in database  # ensure migrator deletes "child" collection
        False
        >>> len(database['workflow_execution_set'])  # ensure migrator creates "parent" collection (if nonexistent)
        4
        >>> 'metatranscriptome_expression_analysis_set' in database
        False
        >>> 'nom_analysis_set' in database
        False
        """

        # Iterate over each parent collection name.
        for (
            parent_collection_name,
            child_collection_names,
        ) in self.collection_names_hierarchy.items():
            self.logger.info(f"Processing collection (parent): {parent_collection_name}")

            # Create the parent collection (if it doesn't already exist).
            self.adapter.create_collection(collection_name=parent_collection_name)

            # Iterate over each of this parent's child collection names.
            for child_collection_name in child_collection_names:
                self.logger.info(
                    f"Moving documents from '{child_collection_name}' (child) "
                    f"to '{parent_collection_name}' (parent)"
                )

                # Insert a copy of each document currently in the child collection,
                # into the parent collection.
                self.adapter.do_for_each_document(
                    collection_name=child_collection_name,
                    action=lambda document: self.adapter.insert_document(
                        collection_name=parent_collection_name, document=document
                    ),
                )

                # Delete the child collection, now that the parent collection contains a copy of
                # each of its documents.
                self.logger.info(f"Deleting collection (child): {child_collection_name}")
                self.adapter.delete_collection(collection_name=child_collection_name)
