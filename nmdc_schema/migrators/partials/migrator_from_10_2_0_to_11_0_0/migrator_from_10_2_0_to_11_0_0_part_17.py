from migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    #TODO KRH: update _from_version and _to_version
    _from_version = "X"
    _to_version = "XXX" 

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(collection_name="workflow_execution_set",
                                           pipeline=[self.update_metaproteomics_analysis])
    
    def update_metaproteomics_analysis(self, workflow_dict: dict):
        r"""
        Updates the metaproteomics_analysis records with new slot (has_protein_annotations) by migrating some contents from the peptide_identifications slot, removing the peptide_identifications slot, and deleting the extraneous nested data.

        >>> m = Migrator()
        >>> m.update_metaproteomics_analysis({'id': 123, 'type': 'MetaproteomicsAnalysis', 'peptide_identifications': [{'best_protein': 'protein1', 'all_proteins': ['protein1', 'protein2']}, {'best_protein': 'protein2', 'all_proteins': ['protein2', 'protein3']}]})
        {'id': 123, 'type': 'MetaproteomicsAnalysis', 'has_protein_annotations': ['protein1', 'protein2']}

        >>> m.update_metaproteomics_analysis({'id': 234, 'type': 'MetaproteomicsAnalysis', 'peptide_identifications': [{'best_protein': 'protein1'}, {'best_protein': 'protein1'}]})
        {'id': 234, 'type': 'MetaproteomicsAnalysis', 'has_protein_annotations': ['protein1']}

        >>> m.update_metaproteomics_analysis({'id': 345, 'type': 'MetaproteomicsAnalysis'}) # no peptide_identifications slot
        {'id': 345, 'type': 'MetaproteomicsAnalysis'}

        >>> m.update_metaproteomics_analysis({'id': 456, 'type': 'MetabolomicsAnalysis'}) # not a MetaproteomicsAnalysis
        {'id': 456, 'type': 'MetabolomicsAnalysis'}

        """
        analysis_type = workflow_dict.get("type")

        if analysis_type == "MetaproteomicsAnalysis":
            if "peptide_identifications" in workflow_dict:
                # gather all the proteins from the peptide identification nested data
                protein_list = []
                for peptide_iden in workflow_dict.get("peptide_identifications"):
                    protein_list.append(peptide_iden.get("best_protein"))
                
                # remove duplicates
                protein_list = list(set(protein_list))
                workflow_dict['has_protein_annotations'] = protein_list

                # remove peptide_identifications slot
                del workflow_dict["peptide_identifications"]

        return workflow_dict

m = Migrator()
workflow_dict = {'id': 123, 'type': 'MetaproteomicsAnalysis', 'peptide_identifications': [{'best_protein': 'protein1', 'all_proteins': ['protein1', 'protein2']}, {'best_protein': 'protein2', 'all_proteins': ['protein2', 'protein3']}]}
m.update_metaproteomics_analysis(workflow_dict)