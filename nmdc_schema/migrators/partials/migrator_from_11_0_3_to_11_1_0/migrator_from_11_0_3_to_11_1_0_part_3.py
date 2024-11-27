from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    This migrator removes the `has_peptide_quantificiations` field from all documents that represent an instance of the `MetaproteomicsAnalysis` class.
    """
    _from_version = "11.1.0.part_2"
    _to_version = "11.1.0.part_3"

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        """

        self.adapter.process_each_document(collection_name="workflow_execution_set", pipeline=[self.remove_has_peptide_quantificiations])

    def remove_has_peptide_quantificiations(self, workflow_doc: dict) -> dict:
        r"""
        Removes the `has_peptide_quantifications` field from all documents that represent an instance of the `MetaproteomicsAnalysis` class.

        Only documents that have a `type` field with the value `nmdc:MetaproteomicsAnalysis` are modified and they are the only documents that can have the `has_peptide_quantificiations` field.

        # Documents with the `has_peptide_quantificiations` field are modified
        >>> m = Migrator()
        >>> m.remove_has_peptide_quantificiations({'id': 'ID1', 'has_peptide_quantifications': 'a', 'type': 'nmdc:MetaproteomicsAnalysis'})
        {'id': 'ID1', 'type': 'nmdc:MetaproteomicsAnalysis'}
        >>> m.remove_has_peptide_quantificiations({'id': 'ID2', 'has_peptide_quantifications': 'b', 'foo': 'bar', 'type': 'nmdc:MetaproteomicsAnalysis'})
        {'id': 'ID2', 'foo': 'bar', 'type': 'nmdc:MetaproteomicsAnalysis'}

        # Non-MetaproteomicsAnalysis documents are not modified
        >>> m.remove_has_peptide_quantificiations({'id': 'ID3', 'type': 'nmdc:MetabolomicsAnalysis'})
        {'id': 'ID3', 'type': 'nmdc:MetabolomicsAnalysis'}

        """

        if workflow_doc.get("type") == "nmdc:MetaproteomicsAnalysis":
            if "has_peptide_quantifications" in workflow_doc.keys():
                del workflow_doc["has_peptide_quantifications"]

        return workflow_doc