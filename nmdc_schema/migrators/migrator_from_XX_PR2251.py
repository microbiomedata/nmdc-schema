from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_0_3_to_11_1_0 import (
    get_migrator_classes,
)


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    This migrator removes the `has_peptide_quantificiations` field from all documents that represent an instance of the `MetaproteomicsAnalysis` class.
    """

    #TODO KRH: Update these values when known
    _from_version = "XX"
    _to_version = "XX" 

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'workflow_analysis_set': [
        ...     {'id': 'ID1', 'has_peptide_quantificiations': 'a'},
        ...     {'id': 'ID2', 'has_peptide_quantificiations': 'b', 'foo': 'bar'},
        ...   ]
        ... }
        >>> any("has_peptide_quantificiations" in document for document in db["workflow_analysis_set"])
        True
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.upgrade()
        >>> any("has_peptide_quantificiations" in document for document in db["workflow_analysis_set"])
        False
        """

        self.adapter.process_each_document(collection_name="data_generation_set", pipeline=[self.remove_has_peptide_quantificiations])

    def remove_has_peptide_quantificiations(self, data_gen_doc: dict) -> dict:
        r"""
        Removes the `has_peptide_quantificiations` field from all documents that represent an instance of the `MetaproteomicsAnalysis` class.

        Only documents that have a `type` field with the value `nmdc:MetaproteomicsAnalysis` are modified and they are the only documents that can have the `has_peptide_quantificiations` field.

        >>> m = Migrator()
        >>> m.remove_has_peptide_quantificiations({'id': 'ID1', 'has_peptide_quantificiations': 'a'})
        {'id': 'ID1'}
        >>> m.remove_has_peptide_quantificiations({'id': 'ID2', 'has_peptide_quantificiations': 'b', 'foo': 'bar'})
        {'id': 'ID2', 'foo': 'bar'}

        # Non-MetaproteomicsAnalysis documents are not modified
        >>> m.remove_has_peptide_quantificiations({'id': 'ID3', 'type': 'nmdc:MetabolomicsAnalysis'})
        {'id': 'ID3', 'type': 'nmdc:MetabolomicsAnalysis'}

        """

        if data_gen_doc.get("type") == "nmdc:MetaproteomicsAnalysis":
            data_gen_doc.pop("has_peptide_quantificiations", None)

        return data_gen_doc
