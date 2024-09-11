from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "XX"
    _to_version = "FIXES_ISSUE_2180"

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        Should be run after migrator_from_10_2_0_to_11_0_0_part_16.py.
        """
        # Add a type slot on the Protocol class within the protocol_link slot on each document
        collections_to_update = [
            "data_generation_set",
            "material_processing_set",
            "collecting_biosamples_from_site_set",
            "protocol_execution_set",
            "storage_process_set",
            "workflow_execution_set",
            "study_set"
        ] 

        for collection_name in collections_to_update:
            self.adapter.process_each_document(collection_name, [self.add_type_to_protocol_link])
    
    def add_type_to_protocol_link(self, document: dict) -> dict:
        r"""
        Add a type slot on the Protocol class within the protocol_link slot on each document

        >>> m = Migrator()
        >>> m.add_type_to_protocol_link({'id': 123})  # no protocol_link field
        {'id': 123}
        >>> m.add_type_to_protocol_link({'id': 123, 'protocol_link': {'id': 456}})
        {'id': 123, 'protocol_link': {'id': 456, 'type': 'nmdc:Protocol'}}
        >>> m.add_type_to_protocol_link({'id': 123, 'protocol_link': {'id': 456, 'type': 'nmdc:Protocol'}}) # test: does not overwrite existing type slot
        {'id': 123, 'protocol_link': {'id': 456, 'type': 'nmdc:Protocol'}}
        """

        self.logger.info(f"Starting migration of {document['id']}")
        if "protocol_link" in document:
            if "type" not in document["protocol_link"]:
                document["protocol_link"]["type"] = "nmdc:Protocol"

        return document