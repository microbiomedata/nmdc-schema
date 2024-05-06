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
            "mags_activity_set",
            "metabolomics_analysis_activity_set",
            "metagenome_annotation_activity_set",
            "metagenome_assembly_set",
            "metagenome_sequencing_activity_set",
            "metatranscriptome_activity_set",
            "nom_analysis_activity_set",
            "omics_processing_set",
            "read_based_taxonomy_analysis_activity_set",
            "read_qc_analysis_activity_set"
            "metaproteomics_analysis_activity_set"   
        ]

        for collection_name in workflow_execution_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_used_slot],
            )
    
    def remove_used_slot(self, doc: dict) -> dict:
        r"""
        Removes the used slot from WorkflowExecution subclasses.

        If the value of the `used` slot does not match the value of the `instrument_name` slot of a related `OmicsProcessing`,
        log the error.

        >>> m = Migrator()  
        >>> m.remove_used_slot({'id': 123, 'used': 'abc'})  
        {'id': 123}
        """
        data_generation_doc = None
        if "used" in doc:
            try:
                data_generation_doc = self.adapter.get_document_having_value_in_field(
                    collection_name="omics_processing_set", field_name="id", value=doc["was_informed_by"]
                    )
                data_generation_doc = data_generation_doc

                if doc["used"] == data_generation_doc["instrument_name"]:
                    doc.pop("used")

            except:
                self.logger.error(f"WorkflowExecution {doc['id']} used: {doc['used']} does not match OmicsProcessing {data_generation_doc['id']} instrument_name {data_generation_doc['instrument_name']}.")

            doc.pop("used")
        
        return doc
    
