from migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    #TODO KRH: update _from_version and _to_version
    _from_version = "X"
    _to_version = "PR236" 

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(collection_name="workflow_execution_set",
                                           pipeline=[self.update_metaproteomics_analysis])
    
    def update_metaproteomics_analysis(self, workflow_dict: dict):
        r"""
        Updates the metaproteomics_analysis records with new slot (has_protein_identifications) by migrating some contents from the peptide_identifications slot, removing the peptide_identifications slot, and deleting the extraneous nested data.

        # Example 1, two peptides mapped to two proteins
        >>> m = Migrator()
        >>> m.update_metaproteomics_analysis({'id': 123, 'type': 'MetaproteomicsAnalysis', 'peptide_identifications': [{'best_protein': 'protein1', 'all_proteins': ['protein1', 'protein2'], 'peptide_spectral_count':1}, {'best_protein': 'protein2', 'all_proteins': ['protein2', 'protein3'], 'peptide_spectral_count':3}]})
        {'id': 123, 'type': 'MetaproteomicsAnalysis', 'has_protein_identifications': [{'type': 'ProteinIdentification', 'razor_protein': 'protein1', 'peptide_sequence_count': 1, 'protein_spectral_count': 1}, {'type': 'ProteinIdentification', 'razor_protein': 'protein2', 'peptide_sequence_count': 1, 'protein_spectral_count': 3}]}

        # Example 2, two peptides mapped to the same protein
        >>> m.update_metaproteomics_analysis({'id': 234, 'type': 'MetaproteomicsAnalysis', 'peptide_identifications': [{'best_protein': 'protein1', 'all_proteins': ['protein1', 'protein2'], 'peptide_spectral_count': 5}, {'best_protein': 'protein1', 'all_proteins': ['protein1', 'protein3'], 'peptide_spectral_count': 1}]})
        {'id': 234, 'type': 'MetaproteomicsAnalysis', 'has_protein_identifications': [{'type': 'ProteinIdentification', 'razor_protein': 'protein1', 'peptide_sequence_count': 2, 'protein_spectral_count': 6}]}

        # Example 3, no peptide_identifications slot
        >>> m.update_metaproteomics_analysis({'id': 345, 'type': 'MetaproteomicsAnalysis'}) # no peptide_identifications slot
        {'id': 345, 'type': 'MetaproteomicsAnalysis'}

        # Example 4, not a MetaproteomicsAnalysis
        >>> m.update_metaproteomics_analysis({'id': 456, 'type': 'MetabolomicsAnalysis'}) # not a MetaproteomicsAnalysis
        {'id': 456, 'type': 'MetabolomicsAnalysis'}
        """
        analysis_type = workflow_dict.get("type")

        if analysis_type == "MetaproteomicsAnalysis":
            if "peptide_identifications" in workflow_dict:
                # gather all the proteins from the peptide identification nested data
                protein_dict = {}
                for peptide_iden in workflow_dict.get("peptide_identifications"):
                    # check that the peptide_identification has a best_protein and peptide_spectral_count slots
                    if "best_protein" not in peptide_iden or "peptide_spectral_count" not in peptide_iden:
                        raise ValueError("peptide_identification is missing best_protein or peptide_spectral_count slot")
                    
                    razor_protein = peptide_iden.get("best_protein")
                    if razor_protein in protein_dict:
                        protein_dict[razor_protein]["peptide_sequence_count"] += 1
                        protein_dict[razor_protein]["protein_spectral_count"] += peptide_iden.get("peptide_spectral_count")
                    else:
                        protein_dict[razor_protein] = {"type": "ProteinIdentification", "razor_protein": razor_protein, "peptide_sequence_count": 1, "protein_spectral_count": peptide_iden.get("peptide_spectral_count")}
                
                # convert dict to list
                protein_list = [x for x in protein_dict.values()]
                
                # order alphabetically so tests are reproducible
                workflow_dict['has_protein_identifications'] = protein_list

                # remove peptide_identifications slot
                del workflow_dict["peptide_identifications"]

        return workflow_dict