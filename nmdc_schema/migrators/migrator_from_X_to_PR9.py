from nmdc_schema.migrators.migrator_base import MigratorBase
import uuid

# TODO: Create documents in WorkflowChain
# TODO: figure out why metatranscriptome_activity_set and metaproteomics_analysis_activity_set are not being retrieved in project.makefile unvalidated command
# TODO: remove import uuid and fix minter function to how we will actually mint ids.
# TODO: figure out workflow chain for metatranscriptomics_analysis_set (does it come after metagenome_annotation_activity_set? From Alicia, but we're not sure)
# TODO: Implement for metaproteomics and metabolomics

class Migrator(MigratorBase):
    """
    Migrates data from X to PR9, namely creates the workflow_chain_set, moves was_informed_by onto the
    WorkflowChain instances, and changes the part_of slots on WorkflowExecution subclass instances to the id
    of the corresponding WorfklowChain.
    """

    _from_version = "X"
    _to_version = "PR9"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.create_collection("workflow_chain_set")
        
        workflow_match_dict = self.adapter.process_each_document(collection_name="read_qc_analysis_activity_set", pipeline=[self.get_was_informed_by])

        agenda = dict(
            read_qc_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, workflow_match_dict)],
            metagenome_assembly_set=[lambda document: self.add_type_slot_with_class_uri(document, workflow_match_dict)],
        )

    
    def mint_ids(self):

        return str(uuid.uuid4())


    # update to make read_qc_doc variable generalizable so it works for metaproteomic, metabolomics, metatranscriptomics starting point
    def get_was_informed_by(self, read_qc_doc: dict):
        r"""
        Get the was_informed_by value (an omics processing id) from the read_qc_analysis document and creates a dictionary of the
        omics processing id with its corresponding worfklow chain id"""

        # Initialize an empty dictionary to store omics processing ids with their newly minted .
        workflow_omics_dict = {}
        workflow_chain_id = self.mint_ids()

        # Get the omics_processing_id from the was_informed_by slot of the read_qc_doc
        omics_processing_id = read_qc_doc["was_informed_by"]

        workflow_omics_dict[omics_processing_id] = workflow_chain_id

        return workflow_omics_dict
    
    
    def update_part_of_slot(self, doc: dict, workflow_omics_dict: dict):

        informed_by_omics_id = doc["was_informed_by"]
        workflow_chain_id = workflow_omics_dict.get(informed_by_omics_id)
        
        doc["part_of"] = [workflow_chain_id]

        return doc