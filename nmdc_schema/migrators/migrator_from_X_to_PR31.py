from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    r"""
    Migrates data from X to PR31, removes used slot from WorkflowExecution subclasses and checks that the 
    value in the used slot on the WorkflowExecution classes matches the value on the DataGeneration 
    instances in the instrument_name slot.
    """

    _from_version = "X"
    _to_version = "PR31"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        
        workflow_execution_collection_names = [
            "metaproteomics_analysis_set",
            "nom_analysis_set",
            "metabolomics_analysis_set",
            "read_based_taxonomy_analysis_set",
            "read_qc_analysis_set",
            "metagenome_sequencing_set",
            "mags_set",
            "metatranscriptome_analysis_set",
            "metagenome_annotation_set",
            "metagenome_assembly_set"
        ]

        self.adapter.process_each_document("omics_processing_set", [self.check_instrument_name])

        for collection_name in workflow_execution_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_used_slot],
            )
    
    def remove_used_slot(self, doc: dict) -> dict:
        r"""
        Removes the used slot from WorkflowExecution subclasses.

        >>> m = Migrator()  
        >>> m.remove_used_slot({'id': 123, 'used': 'abc'})  
        {'id': 123}
        """

        if "used" in doc:
            doc.pop("used")
        
        return doc
    
    def check_instrument_name(self, workflow_execution: dict) -> dict:
        r"""
        Checks that the value in the used slot on the WorkflowExecution classes matches the value
        in the `instrument_name` field of a related `OmicsProcessing` (soon to be renamed to `DataGeneration`) instance. 
        If it matches, then remove used from the WorkflowExecution instance.

        >>> m = Migrator()
        >>> m.check_instrument_name({'id': 123, 'used': 'abc'})
        {'id': 123, 'used': 'abc'}
        """
        
        if "used" in workflow_execution:
            
            try: 
                data_generation_doc = self.adapter.get_document_having_value_in_field(
                    collection_name="omics_processing_set", field_name="instrument_name", value=workflow_execution["used"]
                    )

                if workflow_execution["used"] == data_generation_doc["instrument_name"]:
                    workflow_execution.pop("used")

            except:
                self.logger.error(f"WorkflowExecution {workflow_execution['id']} used: {workflow_execution['used']} does not match OmicsProcessing instrument_name.")
        
        return workflow_execution
    
