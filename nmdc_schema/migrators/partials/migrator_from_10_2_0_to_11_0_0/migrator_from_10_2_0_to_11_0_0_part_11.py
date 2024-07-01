from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR3, namely changes the `type` slot to be NucleotideSequencing or 
    MassSpectrometry for the data_generation_set documents.
    """

    _from_version = "X"
    _to_version = "PR3"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.process_each_document(collection_name="data_generation_set", pipeline=[self.specify_data_gen_type])

    def specify_data_gen_type(self, data_gen_doc: dict) -> dict:
        r"""
        Changes the `type` slot to be either nmdc:NucleotideSequencing or nmdc:MassSpectrometry based 
        on the value of the analyte_category slot of the DataGeneration document

        >>> m = Migrator()  
        >>> m.specify_data_gen_type({'id': 123, 'analyte_category': 'nom', 'type': 'nmdc:DataGeneration'})  
        {'id': 123, 'analyte_category': 'nom', 'type': 'nmdc:MassSpectrometry'}
        >>> m.specify_data_gen_type({'id': 234, 'analyte_category': 'metagenome', 'type': 'nmdc:DataGeneration'})
        {'id': 234, 'analyte_category': 'metagenome', 'type': 'nmdc:NucleotideSequencing'}
        """


        nucleotide_seqs = ["metagenome", "metatranscriptome"]
        mass_spec = ['metaproteome', 'metabolome', 'lipidome', 'nom']

        if data_gen_doc["analyte_category"] in nucleotide_seqs:
            data_gen_doc["type"] = 'nmdc:NucleotideSequencing'
        elif data_gen_doc["analyte_category"] in mass_spec:
            data_gen_doc["type"] = 'nmdc:MassSpectrometry'
        else:
            raise ValueError(f"The 'analyte_category' value ({data_gen_doc['analyte_category']}) in document "
                             f"({data_gen_doc['id']}) is not one of: {', '.join(nucleotide_seqs + mass_spec)}.")

        return data_gen_doc
