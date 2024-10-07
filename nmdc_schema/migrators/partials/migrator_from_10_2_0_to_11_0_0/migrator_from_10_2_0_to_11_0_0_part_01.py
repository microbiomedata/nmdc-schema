
from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    """
    Migrates data from X to an unknown PR, namely removes the 'designated_class' slot from
    all classes it is used.
    """

    _from_version = "X"
    _to_version = "unknown"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        collection_names = [
            "omics_processing_set",
            "pooling_set",
            "library_preparation_set",
            "extraction_set"
        ]
        
        for collection_name in collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_designated_class_slot],
            )

    def remove_designated_class_slot(self, document:dict):
        r"""
        Removes the slot `designated_class` from collections that use it. 

        >>> m = Migrator()
        >>> m.remove_designated_class_slot({'id': 123, 'designated_class': 'nmdc:OmicsProcessing'}) 
        {'id': 123}
        """

        if "designated_class" in document:
            document.pop('designated_class')
            self.logger.info(f"Removing slot designated_class from doc {document['id']}")
                
        return document